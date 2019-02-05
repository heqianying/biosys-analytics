#!/usr/bin/env python3

import os
import sys

def main ():
	NAMES = sys.argv [1:]

	if len (NAMES) == 0:
		script=os.path.basename(sys.argv[0])
		print('Usage: {} NAME [NAME2 ...]'.format(script))
		sys.exit(1)

	if len (NAMES) == 1:
		print ('Hello to the 1 of you: ' + NAMES[0] + '!')

	if len (NAMES) == 2:
		print ('Hello to the 2 of you: {}!'.format(' and '.join(NAMES)))

	if len (NAMES) > 2:
		NUM = len(NAMES)
		last = NAMES.pop()
		print('Hello to the {} of you: {}, and {}!'.format(NUM, ', '.join(NAMES), last))

main()
