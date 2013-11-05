#!/usr/bin/python

import tools
import logging as log

def combine(path, words, length, distance):
    """Returns all possible combinations of words starting with path
    with fixed length and neighbourhood distance
    """
    if not isinstance(path, list): path = [path]
    for p in tools.nextpath(path, words, distance):
        if len(p) == length: yield p
        if len(p) < length:
            for x in combine(p, words, length, distance):
                yield x

def find(source, target, words, maxlength=4, distance=1):
    # Inneficient but simple logic that yields shortests first
    for length in range(2, maxlength+1):
        for candidate in combine(source, words, length, distance):
            if candidate[-1] == target:
                log.info('Found path: %s', candidate)
                yield candidate

if __name__ == '__main__':
    import sys
    for path in find(
        source='cast',
        target='hurt',
        maxlength=4,
        words=[l.strip() for l in sys.stdin]
    ):
        print path
