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

def words():
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
            if candidate[i] != word[i]: distance += 1
            if distance > max_distance: continue
        if distance <= max_distance:
            neighbours.append(candidate)
    return neighbours

def next():
    pass

if __name__ == '__main__':
    print neighbourhood('cast', words(), 2)
