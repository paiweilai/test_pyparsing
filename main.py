import sys

import utils
from patterns import sqla_count


def process(text):
    found_results = [
        (string, (start, end))  # found_string, interval
        for string, start, end in sqla_count.find(text)
    ]
    if not found_results:
        return text  # no change

    found_strings, intervals = zip(*found_results)
    new_strings = [
        sqla_count.replace(found_string) for found_string in found_strings
    ]

    new_text = utils.replace_with(text, new_strings, intervals)
    return new_text


if __name__ == "__main__":
    try:
        fileobj = open(sys.argv[1], 'r')
    except IndexError:
        fileobj = sys.stdin

    with fileobj:
        text = fileobj.read()

    print process(text)
