#!/usr/bin/env python
import sys

inputString = sys.argv[1]

if (inputString == inputString[::-1]):
  print ('Given input string "%s" is a palindrom.' % inputString)
else:
  print ('Given input string "%s" is not a palindrom.' % inputString)
