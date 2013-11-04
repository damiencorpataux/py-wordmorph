#!/usr/bin/python

import sys

def read(file):
    if not file:
        for line in sys.stdin: yield line
    else:
        with open(file, 'r') as f: 
            for line in f: yield line

def strip(lines):
    for line in lines:
        # FIXME: Proposal: if line letters not in /[a-z]/
        #        which is the condition for the algorithm to work
        if [l for l in line if l.isupper()] or "'" in line: continue
        yield line

def write(file, lines):
    if not file:
        for line in lines: sys.stdout.write(line)
    else:
        try:
            with open(file, 'w') as f:
                for line in lines: f.write(line)
        except Exception as e:
            raise e
        finally:
            f.close()
            

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Strips unclean words for script.py')
    parser.add_argument('-i, --input',
        dest='infile',
        metavar='source',
        help='The source filename to parse (reads stdin if not specified)'
    )
    parser.add_argument('-o, --output',
        dest='outfile',
        metavar='destination',
        help='The destination filename to write (writes to stdout if not specified)'
    )   
    args = parser.parse_args().__dict__
    write(args.get('outfile'), strip(read(args.get('infile'))))
