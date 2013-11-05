#!/usr/bin/python

import sys, argparse
import logging

def dictionary(file):
    f = open(file, 'r') if file else sys.stdin
    for line in f: yield line.strip()

def args():
    parser = argparse.ArgumentParser(description='Outputs the shortest path between two words')
    parser.add_argument('--from',
        dest='source',
        metavar='word',
        help='word to be used as source node (mandatory)'
    )
    parser.add_argument('--to',
        dest='target',
        metavar='word',
        help='word to be used as target node (mandatory)'
    )
    parser.add_argument('--wordlist',
        dest='wordlist',
        metavar='filename',
        help='filename of the wordlist to be used (reads stdin if not specified)'
    )
    parser.add_argument('--processor',
        default='combinatory',
        dest='processor',
        metavar='name',
        help='algorithm implementation to use for word processing (default: combinatory)'
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
    parser.add_argument('--log',
        metavar='level',
        help='logging level (DEBUG, INFO)'
    )
    args = parser.parse_args().__dict__
    # --from and --to are mandatory, although argparser doesnt support this
    missing = [key for key in ['source', 'target'] if not args.get(key)]
    if missing:
        parser.print_help()
        sys.exit(1)
    # Setups loggin level
    level = args.pop('log', None)
    if level: logging.basicConfig(level=getattr(logging, level))
    return args

def process(args):
    # from processor import {processor} as p
    processor = args.pop('processor')
    p = getattr(__import__('processor', globals(), locals(), [processor], -1), processor)
    words = dictionary(args.pop('wordlist'))
    for path in p.find(words=words, **args):
        for word in path:
            print word
        
if __name__ == '__main__':
    process(args())
