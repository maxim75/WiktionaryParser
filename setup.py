from setuptools import setup,find_packages

with open('readme.md', 'r') as readme:
  long_desc = readme.read()

setup(
  name = 'wiktionaryparser-ml',
  version = '0.0.1',
  description = 'A tool to parse word data from wiktionary.com into a JSON object. Based on wiktionary parser by Suyash Behera',
  long_description = long_desc,
  long_description_content_type='text/markdown',
  packages = ['', 'tests', 'utils'],
  data_files=[('testOutput', ['tests/testOutput.json']), ('readme', ['readme.md']), ('requirements', ['requirements.txt'])],
  author = 'Maksym Kozlenko',
  author_email = 'max@kozlenko.info',
  url = 'https://github.com/Maxim75/WiktionaryParser', 
  download_url = 'https://github.com/Maxim75/WiktionaryParser/archive/master.zip', 
  keywords = ['Parser', 'Wiktionary'],
  install_requires = ['beautifulsoup4','requests'],
  classifiers=[
   'Development Status :: 5 - Production/Stable',
   'License :: OSI Approved :: MIT License',
  ],
)