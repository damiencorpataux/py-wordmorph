#!/usr/bin/python

import tools

def find(source, target, words, maxlength=3, distance=1):
    """Recursively looks up for all possible word-paths between two words.
    Valid paths satisfy 2 conditions:
    - the 'distance' between two nodes in the path
    - the 'maxlength' of the path
    """
    if not isinstance(source, list): source = [source]
    if len(source) < maxlength:
        for path in tools.nextpath(source, words, distance):
            if path[-1] == target: yield path
            for path in find(path, target, words, maxlength, distance):
                yield path

if __name__ == '__main__':
    import sys
    for path in find(
        source='cast',
        target='hurt',
        maxlength=4,
        words=[l.strip() for l in sys.stdin]
    ):
        print path
