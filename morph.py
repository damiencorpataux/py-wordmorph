#!/usr/bin/python

options = {
    'from': 'cast',
    'to': 'hurt',
    'wordlist': 'wordlist.clean'
}

cache = {
    'words' : []
}

# FIXME: Proposal: yield data

def allwords():
    with open(options.get('wordlist')) as f:
        cache['words'] = f.read().splitlines()
    return cache.get('words')

def neighbourhood(word, words, max_distance=1):
    """Determines and returns the neighbours of the given word.
    A neighbour is a word from the 'words' list that has the same
    length as the 'word', and a maximum number of n characters
    defined by 'max_distance'
    """
    neighbours = []
    for candidate in words:
        # FIXME: Try using smth better than Theta(n^2) for the diff
        if len(candidate) != len(word): continue
        # FIXME: Express this more concisely ?
        #        And create a dedicated distance()
        distance = 0
        for i, l in enumerate(candidate):
            if distance > max_distance: continue
            if candidate[i] != word[i]: distance += 1
        if distance <= max_distance:
            neighbours.append(candidate)
    return neighbours

def fu(source, target, maxlength=10, current=[], paths=[]):
    if not current: current = [source]
    words = set(allwords()) - set(current)
    for word in neighbourhood(current[-1], words):
        current.append(word)
        print len(current), maxlength
        if (word == target):
            print "FOUND:", len(current), current
            #paths.append(current)
        if len(current) < maxlength:
            fu(current[-1], target, maxlength, current, paths)

def nextpath(path):
    words = set(allwords()) - set(path)
    return [path+[word] for word in neighbourhood(path[-1], words)]
         

def find(source, target):
    path = []
    solutions = []
    if not path: path = [source]
    for p in nextpath(path):
        print p
        if p[-1] == target:
            solutions.append(p)
            print "FOUND:", p
    return solutions


if __name__ == '__main__':
    paths = find('cast', 'cash')
    print "--8<-----"
    print paths
    #paths = fu('cast', 'cash', 10)#'hurt')
    #print 'RESULT:'
    #for path in paths:
    #    print len(path), path
