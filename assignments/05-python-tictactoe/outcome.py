#!/usr/bin/env python3
"""
Author : qhe0310
Date   : 2019-02-21
Purpose: Rock the Casbah
"""

import os
import sys



# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} STATE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)
        
    state = args[0]

    wins = [('X', 'XXX......'), ('O', 'OOO......'), ('X', '...XXX...'),
            ('O', '...OOO...'), ('X', '......XXX'), ('O', '......OOO'),
            ('X', 'X..X..X..'), ('O', 'O..O..O..'), ('X', '.X..X..X.'),
            ('O', '.O..O..O.'), ('X', '..X..X..X'), ('O', '..O..O..O'),
            ('X', 'X...X...X'), ('O', 'O...O...O'), ('X', '..X.X.X..'),
            ('O', '..O.O.O..')]

    for state in wins:
        print('X has won')
    else:
        pirnt('State "{}" must be 9 characters of only ., X, O')
        

        
# --------------------------------------------------
main()
