#!/usr/bin/python

import sys

def strip():
    for line in sys.stdin:
        # FIXME: Proposal: if line letters not in /[a-z]/
        #        which is the condition for the 'morph' algorithm to work
        #        Proposal: also remove duplicate
        if [l for l in line if l.isupper()] or "'" in line: continue
        yield line

def write():
    with open('wordlist.clean', 'w') as f: 
        for line in strip(): f.write(line)

if __name__ == '__main__':
    write()
