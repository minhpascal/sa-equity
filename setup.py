from distutils.core import setup

setup(name='saequity',
			version='0.1.0',
			author='Vineet Apte',
			author_email='aptebros@gmail.com',
			packages=['saequity'],
			scripts=[],
			url='',
			license="MIT",
			description="SeekingAlpha webscraper for equity research",
			long_description=open('README.md').read(),
			install_requires=[
				'pandas',
				'bs4',
				'openpyxl'
				'PyYaml'
			],
		)
