#!/usr/bin/env python3
"""
Author : qhe0310
Date   : 2019-02-12
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA to AA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-h',
        '--help',
        help='usage: translate_proteins.py [-h] -c FILE [-o FILE] STR',
        metavar='str',
        type=str,
        default='')

    parser.add_argument(
        '-o',
        '--outfile FILE',
        help='Output filename',
        metavar='str',
        type=str,
        default='out.txt')

    parser.add_argument(
        '-c FILE',
        '--codons FILE'
        help='A file with codon translations',
        metavar='str',
        type=str,
        default=None)


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
    FILE = args[0]
    
    if len (sys.argv) == 0:
        print('usage: translate_proteins.py [-h] -c FILE [-o FILE] STR')
        print('translate_proteins.py: error: the following arguments are required: STR, -c/--codons')
        sys.ext(1)
    
    if not os.path.isfile(FILE):
        print('--condons "{}" is not a file'.format(FILE))
    
# --------------------------------------------------
if __name__ == '__main__':
    main()
