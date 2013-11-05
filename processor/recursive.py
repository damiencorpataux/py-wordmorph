#!/usr/bin/python

import tools
import logging

log = logging.getLogger(__name__)

def find(source, target, words, maxlength=3, distance=1):
    """Recursively looks up for all possible word-paths between two words.
    Valid paths satisfy 2 conditions:
    - the 'distance' between two nodes in the path
    - the 'maxlength' of the path
    """
    if not isinstance(source, list): source = [source]
    if len(source) < maxlength:
        for path in tools.nextpath(source, words, distance):
            if path[-1] == target:
                log.info('Found path: %s', path)
                yield path
            for path in find(path, target, words, maxlength, distance):
                yield path
