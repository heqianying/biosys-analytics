#!/usr/bin/env python3
"""
Author : qhe0310
Date   : 2019-02-20
Purpose: Rock the Casbah
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='prints the first line of the contents of each file in a directory along with source file name',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-w',
        '--width',
        help='the width of the space to print',
        metavar='int',
        type=int,
        default=50)

    parser.add_argument(
        '-DIR',
        help='A directory',
        metavar='DIR',
        type=str,
        nargs='+',
        required=True)

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
def main():
    """Make a jazz noise here"""
    args=get_args()
    dir_name=args.directory
    width_num=args.width
    
    if not os.path.isdir(dir_name):
        die('"{}" is not a directory'.format(dir_name))
    

    
# --------------------------------------------------
if __name__ == '__main__':
    main()
