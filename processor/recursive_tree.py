#!/usr/bin/python

# FIXME: Handle from:cast to:cast case

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

def find(source, target, words, maxlength=3, distance=1, path=[]):
    """Recursively looks up for all possible word-paths between two words.
    Valid paths satisfy 2 conditions:
    - the 'distance' between two nodes in the path
    - the 'maxlength' of the path
    """
    if not path: path = [source]
    if len(path) < maxlength:
        for p in nextpath(path, words, distance):
            if p[-1] == target: yield p
            for x in find(p[-1], target, maxlength, distance, p):
                yield x
