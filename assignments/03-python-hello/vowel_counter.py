#!/usr/bin/env python3

import os
import sys

def main():
	STRING = sys.argv[1:]
	
	if len(STRING) != 1:
	 print('Usage: {} STRING'.format(os.path.basename(sys.argv[0])))
	 sys.exit(1)
	
	if len (STRING) > 0:
	 VOWELS = "aeiouAEIOU"
	 count = 0
	 for i in VOWELS:
	 for j in STRING:
		if i != j:
		 print('There are 0 vowels in "{}."'.format(STRING))
		if i = j
		count = count + 1
		 if count = 1:
			print('There is {} vowel in "{}.".format(count, STRING))
		 if count > 1:
			print('There are {} vowels in "{}.".format(count, STRING))


main()
