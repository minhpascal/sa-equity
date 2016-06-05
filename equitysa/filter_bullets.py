
import re
import collections as co


def focus(bullets):
    '''
    assume that bullets is a 2d list where each list contains from an
    event frame on SA
    '''
    
    return [filter_event_frame(frame) for frame in bullets]
    
def filter_event_frame(bulletSet):   
    '''
    each event frame is distinct, so we choose >=1 bullet from each
    '''

    scoring_dict = {bullet:[] for bullet in bulletSet}

    score_fns = [target_freq, ticker_freq,money_freq]
    
    for score_fn in score_fns:
        scoring_dict = add_score(scoring_dict,score_fn)
    
    #print(scoring_dict)
    
    return get_best_bullet(scoring_dict)
    
def get_best_bullet(scoring_dict):
    maxScore, bestSentence= 0, ''
    for key,value in scoring_dict.items():
        score = 0
        for value in scoring_dict.values():
            score+=compute_score(value)
            
        if (score>maxScore):
            bestSentence= key
    #print(bestSentence)
    return bestSentence
                

def compute_score(score_list):
    score = 0
    for sub_score in score_list:
        if (type(sub_score)==int):
            score+=sub_score
        elif (type(sub_score)==dict):
            score+= sub_score['distinct']
    return score

def add_score(scoring_dict, score_fn):
    for key,value in scoring_dict.items():
        value.append(score_fn(key,scoring_dict))
    return scoring_dict


#Scoring functions:

def money_freq(s,scoring_dict):
    mn_regex= co.Counter(re.findall("\$.*?[M,mm,B]",s))
    return {'total':sum(mn_regex.values()), 'distinct':len(mn_regex.keys())}
    
def ticker_freq(s, scoring_dict):
    '''
    tickers as regex are 2-3 capital letters
    '''
    ticker_as_re = "[A-Z]{2,3}"
    
    # double counts strs where : "...TKCR (TKCR 0.5%)"
    tk_regex = co.Counter(re.findall(ticker_as_re,s))  
    return {'total':sum(tk_regex.values()), 'distinct':len(tk_regex.keys())}
    

def target_freq(s,scoring_dict):
    '''
    scores string based on target inclusion
    '''
    with open("resources/target_keywords.txt") as f:
        target_str = f.read()
    targets = [word.strip() for word in target_str.split(',')]
    l = s.split()
    score = 0
    for target in targets:
        score+=len([x for x in l if target in x.lower()])
    return score        
