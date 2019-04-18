#!/usr/bin/env python3
"""
Author : qianying
Date   : 2019-04-15
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import logging

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Hamming distance',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='FILE', help='File inputs', nargs=2)


    parser.add_argument(
        '-d', '--debug', help='Debug', action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


# --------------------------------------------------
def dist(s1, s2):
    """Haming distance calculation function"""
    m = 0
    l1 = s1.split()
    l2 = s2.split()
    #print(l1)



    for i, x in enumerate(l1):
        if len(l1[i]) >= len(l2[i]):
            #print('l1 longer')
            compare1 = l1[i]
            compare2 = l2[i]
        else:
            #print('l2 longer')
            compare1 = l2[i]
            compare2 = l1[i]

        #print(compare1, compare2)
        for j, y in enumerate(compare2):
            if compare1[j] != y:
                m +=1
            #print(y)
        for num in range(0, len(compare1) - len(compare2)):
            #print(num)
            m +=1

    #print(m)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    debug_arg = args.debug
    pos_arg = args.positional

    logging.basicConfig(
    filename='.log',
    filemode='w',
    level=logging.DEBUG if args.debug else logging.CRITICAL
    )

    for x in pos_arg:
        if not os.path.isfile(x):
            print('"{}" is not a file'.format(x), file=sys.stderr)
            sys.exit(1)

    s1 = ''
    with open(pos_arg[0], 'r') as f:
        for line in f:
            s1 += line

    s2 = ''
    with open(pos_arg[1], 'r') as f:
        for line in f:
            s2 += line

    #print(s2)
    m = dist(s1, s2)
    print(m)



# --------------------------------------------------
if __name__ == '__main__':
    main()
