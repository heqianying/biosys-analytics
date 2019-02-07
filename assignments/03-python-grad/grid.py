#!/usr/bin/env python3
"""
Author : qhe0310
Date   : 2019-02-06
Purpose: Rock the Casbah
"""

import os
import sys


# --------------------------------------------------
def main():
    NUM = sys.argv[1:]

    if len(NUM) == 0:
        print('Usage: {} NUM'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    i= int (NUM[0])
    if not 1 < i < 10:
        print('NUM ({}) must be between 1 and 9'.format(i))
        sys.exit(1)
    
    i = int (NUM[0])
    d = range(2,10)
    all = d * d 
    x = list(range(all))
    i=0
    while i < all:
        print(" ".join(map(str,x[i:i+d])))
        i += d

# --------------------------------------------------
main()
