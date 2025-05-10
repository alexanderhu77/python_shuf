#!/usr/bin/python3

import sys
import argparse
import random

def parse_range(range_str):
    start_str, end_str = range_str.split('-', 1)
    start = int(start_str)
    end = int(end_str)
    return [str(i) for i in range(start, end + 1)]

def main():
    parser = argparse.ArgumentParser(
        description="Python implementation of GNU shuf",
        usage="%(prog)s [OPTION]... [FILE]"
    )
    parser.add_argument("-e", "--echo", action="store_true",
                        help="treat each command-line operand as an input line")
    parser.add_argument("-i", "--input-range", metavar="LO-HI",
                        help="treat each number LO through HI as an input line")
    parser.add_argument("-n", "--head-count", type=int,
                        help="output at most COUNT lines")
    parser.add_argument("-r", "--repeat", action="store_true",
                        help="output lines can be repeated")
    parser.add_argument("operand", nargs="*")

    args = parser.parse_args()

    if args.input_range is not None:
        lines = parse_range(args.input_range)
    elif args.echo:
        lines = args.operand
    else:
        if len(args.operand) == 0 or args.operand[0] == "-":
            lines = [line.rstrip('\n') for line in sys.stdin]
        else:
            with open(args.operand[0], 'r') as f:
                lines = [line.rstrip('\n') for line in f]

    count = args.head_count if args.head_count is not None else len(lines)

    if args.repeat:
        if args.head_count is None:
            while True:
                sys.stdout.write(random.choice(lines) + '\n')
        else:
            for _ in range(count):
                sys.stdout.write(random.choice(lines) + '\n')
    else:
        random.shuffle(lines)
        for line in lines[:count]:
            sys.stdout.write(line + '\n')

if __name__ == "__main__":
    main()
