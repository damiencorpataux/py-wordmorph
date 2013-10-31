#!/usr/bin/python

options = {
    'from': 'cast',
    'to': 'hurt',
    'wordlist': 'wordlist.clean'
}

dictionary_cache = []
def dictionary(file='wordlist'):
    """Returns a list of words contained in the given file.
    The given file should contain EOL-separated words.
    """
    global dictionary_cache
    if (dictionary_cache): return dictionary_cache
    with open(options.get(file)) as f:
        dictionary_cache = f.read().splitlines()
    return dictionary_cache

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
    return [candidate for candidate in words if isdistance(distance, candidate, word)]

def nextpath(path, distance):
    """Returns list of next possible words-paths
    according the given 'path' and 'distance'.
    The returned list never contains duplicate words
    (this is mandatory for avoiding
    loops).
    """
    words = set(dictionary()) - set(path)
    return [path+[word] for word in neighbourhood(path[-1], words, distance)]
         

def find(source, target, maxlength=3, distance=1, path=[]):
    """Recursively looks up for all possible word-paths between two words.
    Valid paths satisfy 2 conditions:
    - the 'distance' between two nodes in the path
    - the 'maxlength' of the path
    """
    if not path: path = [source]
    solutions = []
    if len(path) < maxlength:
        for p in nextpath(path, distance):
            if p[-1] == target: solutions.append(p)
            solutions += find(p[-1], target, maxlength, distance, p)
    return solutions


if __name__ == '__main__':
    paths = find('cast', 'cash', 3)
    for path in paths:
        print len(path), path
