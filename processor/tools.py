#!/usr/bin/python

import sys

def isdistance(distance, word1, word2):
    """Returns True if the distance between 'word1' and 'word2' is 'distance',
    False otherwise.
    The distance is the count of different characters between the given words.
    For optimization purpose and fitness to our usecase, None is returned
    if words have different lengths.
    """
    if len(word1) != len(word2): return None
    actual = 0
    for i, l in enumerate(word1):
        if actual > distance: return False
        if word1[i] != word2[i]: actual += 1
    if actual == distance: return True 
    else: return False

def neighbourhood(word, words, distance=1):
    """Determines and returns the neighbours of the given word.
    A neighbour is a word from the 'words' list that has the same
    length as the 'word', and a maximum number of n characters
    defined by 'max_distance'
    """
    for candidate in words:
        if isdistance(distance, candidate, word):
            yield candidate

def nextpath(path, words, distance):
    """Returns list of next possible words-paths
    according the given 'path' and 'distance'.
    The returned list never contains duplicate words
    (this is mandatory for avoiding graph loops).
    """
    words = set(words) - set(path)
    for word in neighbourhood(path[-1], words, distance): yield path+[word]

def read(file):
    """Yields file lines if specified, stdin otherwise.
    """
    if not file:
        for line in sys.stdin: yield line
    else:
        with open(file, 'r') as f: 
            for line in f: yield line

def strip(lines):
    """Strips words from lines for use with wordmorph
    """
    for line in lines:
        # FIXME: Proposal: if line letters not in /[a-z]/
        #        which is the condition for the algorithm to work
        if [l for l in line if l.isupper()] or "'" in line: continue
        yield line

def write(file, lines):
    """Writes lines to file if specified, stdout otherwise
    """
    if not file:
        for line in lines: sys.stdout.write(line)
    else:
        try:
            with open(file, 'w') as f:
                for line in lines: f.write(line)
        except Exception as e:
            raise e
        finally:
            f.close()
