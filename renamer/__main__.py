import argparse

from renamer.operator import operator


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--src', default='.', dest='src_dir',
                        help='src directory to search files.')
    parser.add_argument('-i', '--index', default=1, type=int,
                        help='start number to count (e.g. 001, 002, ...)')
    parser.add_argument('-r', '--recursive', action='store_true',
                        help='search src directories recursively.')
    args = parser.parse_args()

    operator(args.src_dir, args.index, args.recursive)


if __name__ == '__main__':
    main()
