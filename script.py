#!/usr/bin/python

# FIXME: Handle from:cast to:cast case
#        Yield results to enable yielding found paths
#        Optimize to find shortest parth first, better algo complexity:
#        try to change nextpath() instructions order to test shorter combinaisons first

dictionary_cache = []
def dictionary(file='wordlist.clean'):
    global dictionary_cache
    if (dictionary_cache): return dictionary_cache
    with open(file) as f:
        dictionary_cache = f.read().splitlines()
    return dictionary_cache

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
            yield candidate

def nextpath(path, distance):
    words = set(dictionary()) - set(path)
    for word in neighbourhood(path[-1], words, distance): yield path+[word]

def combine(word, length, distance, path=[]):
    """Returns all possible combinations of paths starting with path
    with fixed length and neighbourhood distance
    """
    if not path: path = [word]
    for p in nextpath(path, distance):
        if len(p) == length: yield p
        if len(p) < length:
            for x in combine(None, length, distance, p):
                yield x

def find(source, target, maxlength=None, distance=None):
    # Inneficient but simple logic that yields shortests first
    for length in range(2, maxlength+1):
        for candidate in combine(source, length, distance):
            if candidate[-1] == target:
                yield candidate

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
        default=4,
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
