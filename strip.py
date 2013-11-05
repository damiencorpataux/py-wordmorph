#!/usr/bin/python

import sys, argparse
import logging
from processor.tools import read, strip, write

logging.basicConfig()
log = logging.getLogger(__file__)

if __name__ == '__main__':
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
    if not args.get('infile'): log.warn('Reading from stdin')
    if not args.get('outfile'): log.warn('Writing to stdout')
    # Actual processing
    write(args.get('outfile'), strip(read(args.get('infile'))))
