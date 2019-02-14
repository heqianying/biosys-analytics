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
        description='Tic-Tac-Toe board',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-s',
        '--state',
        help='board state',
        metavar='str',
        type=str,
        default='.........')

    parser.add_argument(
        '-p',
        '--player',
        help='The player to modify the state',
        metavar='str',
        type=str,
        default='')

    parser.add_argument(
        '-c',
        '--cell',
        help='The cell to alter',
        metavar='int',
        type=int,
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
    grid_num = list(range(1,10))
    grid = [grid_num[i:i+3] for i in range (0,9,3)]
    args = get_args()
    state = args.state
    player = args.player
    cell = args.cell
    
    if len (sys.argv) == 1:
        print('-'*13)
        for row in grid:
            print('|', row[0], '|', row[1], '|', row[2], '|')
            print('-'*13)
        sys.ext(0)
    
    state_character = '.-XO'
    for character in state:
        if state != '.........' and (len(state) != 9 or (character not in state_character)):
            print(die(msg='Invalid state "{}",must be 9 characters of only -,X,O'.format(state)))
    
    player_character = 'XO'
    if player not in player_character:
        print(die(msg='Invalid player "{}",must be X or O'.format(player)))
    
    if cell is not None and not 1 <= cell <= 9:
        print(die(msg='Invalid cell "{}",must be 1-9'.format(cell)))
    
    if (any([cell,player]) and not all ([cell,player])) is True:
        print('Must provided both --player and --cell')
        sys.exit(1)
    


# --------------------------------------------------
if __name__ == '__main__':
    main()
