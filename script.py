#!/usr/bin/python

def args():
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
    return args

def process():
    # from processor import {} as processor
    for path in processor.find(): yield path
    # Results display
    paths = find(**args)
    for path in paths:
        print "{0}: {1}".format(len(path), path)

def cli():
    process(args())

if __name__ == '__main__':
    cli()
