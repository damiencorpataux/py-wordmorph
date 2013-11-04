#!/usr/bin/python

# FIXME: Handle from:cast to:cast case
#        Yield results to enable yielding found paths
#        Optimize to find shortest parth first, better algo complexity:
#        try to change nextpath() instructions order to test shorter combinaisons first

dictionary_cache = []
def dictionary(file='wordlist.clean'):
    """Returns a list of words contained in the given file.
    The given file should contain EOL-separated words.
    """
    # FIXME: Use a cache decorator
    global dictionary_cache
    if (dictionary_cache): return dictionary_cache
    with open(file) as f:
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
    for candidate in words:
        if isdistance(distance, candidate, word):
            yield candidate

def nextpath(path, distance):
    """Returns list of next possible words-paths
    according the given 'path' and 'distance'.
    The returned list never contains duplicate words
    (this is mandatory for avoiding graph loops).
    """
    words = set(dictionary()) - set(path)
    for word in neighbourhood(path[-1], words, distance): yield path+[word]

def find(source, target, maxlength=3, distance=1, path=[]):
    """Recursively looks up for all possible word-paths between two words.
    Valid paths satisfy 2 conditions:
    - the 'distance' between two nodes in the path
    - the 'maxlength' of the path
    """
    if not path: path = [source]
    if len(path) < maxlength:
        for p in nextpath(path, distance):
            if p[-1] == target: yield p
            for x in find(p[-1], target, maxlength, distance, p):
                yield x

def cli():
    import sys, argparse
    # Using argparser to manage cli argument and help blurb
    parser = argparse.ArgumentParser(description='Generate paths between words')
    parser.add_argument('--from',
        dest='source',
        metavar='word',
        help='the word to be used as source node (mandatory)'
    )
    parser.add_argument('--to',
        dest='target',
        metavar='word',
        help='the word to be used as target node (mandatory)'
    )
    parser.add_argument('--maxlength',
        default=6,
        type=int,
        metavar='int',
        help='max words contained in a morph path'
    )
    parser.add_argument('--distance',
        default=1,
        type=int,
        metavar='int',
        help='max distance between two words'
    )
    args = parser.parse_args().__dict__
    # --from and --to are mandatory, although argparser doesnt support this
    missing = [key for key in ['source', 'target'] if not args.get(key)]
    if missing:
        parser.print_help()
        sys.exit(1)
    # Results display
    for path in find(**args):
        for word in path:
            print word
        break

if __name__ == '__main__':
    cli()
