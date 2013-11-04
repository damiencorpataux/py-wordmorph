#!/usr/bin/python

import sys

def load():
    # wget or curl unixwords url
    pass

def strip(lines):
    for line in lines:
        # FIXME: Proposal: if line letters not in /[a-z]/
        #        which is the condition for the 'morph' algorithm to work
        #        Proposal: also remove duplicate
        # TODO: Do positive logic: if ...: yield line
        if [l for l in line if l.isupper()] or "'" in line: continue
        yield line

def write():
    with open('tmp/wordlist.clean', 'w') as f: 
        for line in strip(): f.write(line)

dictionary_cache = []
def get(file='wordlist.clean'):
    """Returns a list of words contained in the given file.
    The given file should contain EOL-separated words.
    """
    global dictionary_cache
    if (dictionary_cache): return dictionary_cache
    with open(file) as f:
        dictionary_cache = f.read().splitlines()
    return dictionary_cache

if __name__ == '__main__':
    write()
