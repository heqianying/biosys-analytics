#!/usr/bin/env python3
"""
Author : qhe0310
Date   : 2019-02-27
Purpose: Rock the Casbah
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Caculate GC content',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'FASTA',
        help='fasta file',
        metavar='FASTA',
        nargs='+')

    parser.add_argument(
        '-o',
        '--outfile FILE',
        help='Output directory',
        metavar='DIR',
        default='out')
    
    parser.add_argument(
        '-p',
        '--pct_gc',
        help='Dividing line for percent GC',
        metavar='int',
        type=int,
        default=50)

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
    fasta_file=args.FASTA
    out_dir=args.out
    
    if not os.path.isfile(fasta_file):
        die('"{}" is not a file'.format(fasta_file))
        print('Done,wrote 0 sequence to out dir "out"')
    

    
# --------------------------------------------------
if __name__ == '__main__':
    main()
