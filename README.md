# Frequency Analysis of Words

This script return 10 most common words in given text.
Multi language support: works with non ascii characters.

# How to run

script require python3.5
Example of script launch on Linux, Python 3.5:

```#!bash
$ python lang_frequency.py <filename> # possibly requires call of python3 executive instead of just python
$ python lang_frequency.py text.txt

# output example
>>> Top 10 most used words in this text are: ['the', 'of', 'and', 'in', 'is', 'to', 'a', 'for', 'response', 'with']

$ python lang_frequency.py Статья.txt
# output example
>>> Top 10 most used words in this text are: ['в', 'и', 'править', 'с', 'вики', 'не', 'текст', 'на', 'из', 'женщины']

python3 lang_frequency.py -h
>>> usage: lang_frequency.py [-h] filepath
>>>
>>> Pritty print for JSON
>>>
>>> positional arguments:
>>>   filepath    File path to the file
>>>
>>> optional arguments:
>>>   -h, --help  show this help message and exit

```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
