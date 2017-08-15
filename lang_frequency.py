from collections import Counter
import sys
import os
import re
import argparse


def parse_args(args):

    parser = argparse.ArgumentParser(description='Pritty print for JSON')
    parser.add_argument('filepath', help='File path to the file', type=argparse.FileType('r'))

    return parser.parse_args(args)


def load_data(file_path):

    if not file_path or not os.path.exists(file_path):
        return None

    with open(file_path, 'r') as file_handler:
        return file_handler.read()


def get_most_frequent_words(text):
    if not text:
        return None

    text_split = re.split("[\W\d]+", text)
    top10 = Counter(text_split).most_common(10)
    return [item[0] for item in top10]


if __name__ == '__main__':
    try:
        parser = parse_args(sys.argv[1:])

        file_path = parser.filepath.name
    except IOError:
        file_path = None

    text = load_data(file_path)

    print('Top 10 most used words in this text are: %s' % str(get_most_frequent_words(text)))


