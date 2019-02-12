#!/usr/bin/env python3
"""
Author : qhe0310
Date   : 2019-02-10
Purpose: Rock the Casbah
"""

import os
import sys

# --------------------------------------------------
def main():
    args = sys.argv[1:]
    
    if len(args) == 0:
        print('Usage: {} FILE [NUM_LINES]'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)
    
    file = args[0]
    if not os.path.isfile(file):
        print ('{} is not a file'.format(file),file=sys.stderr)
        sys.exit(1)
    
    i = int (num)
    num = args[1] if i == 2 else 3
    
    if i < 0:
        print ('lines ({}) must be a postive number'.format(i))
    
    with open(file) as f:
        head = [next(f) for x in range(i)]
        print(head)
# --------------------------------------------------
main()
