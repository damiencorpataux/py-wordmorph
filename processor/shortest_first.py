#!/usr/bin/python

# FIXME: Handle from:cast to:cast case
#        Yield results to enable yielding found paths
#        Optimize to find shortest parth first, better algo complexity:
#        try to change nextpath() instructions order to test shorter combinaisons first

def isdistance(distance, word1, word2):
    if len(word1) != len(word2): return None
    actual = 0
    for i, l in enumerate(word1):
        if actual > distance: return False
        if word1[i] != word2[i]: actual += 1
    if actual == distance: return True 
    else: return False

def neighbourhood(word, words, distance=1):
    for candidate in words:
        if isdistance(distance, candidate, word):
            print candidate
            yield candidate

def nextpath(path, words, distance):
    w = set(words) - set(path)
    for word in neighbourhood(path[-1], w, distance): yield path+[word]

def combine(word, words, length, distance, path=[]):
    """Returns all possible combinations of words starting with word
    with fixed length and neighbourhood distance
    """
    if not path: path = [word]
    for p in nextpath(path, words, distance):
        if len(p) == length: yield p
        if len(p) < length:
            for x in combine(None, words, length, distance, p):
                yield x

def find(source, target, words, maxlength=None, distance=None):
    # Inneficient but simple logic that yields shortests first
    for length in range(2, maxlength+1):
        for candidate in combine(source, words, length, distance):
            if candidate[-1] == target:
                print candidate
                yield candidate
