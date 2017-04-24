#!/usr/bin/env python
import sys
givenString = sys.argv[1].lower()
sortedGivenString = sorted(givenString)

countNumberOfOddCharacter = 0

for char in sortedGivenString:
  if (sortedGivenString.count(char) == 1 or sortedGivenString.count(char) % 2 == 1):
    countNumberOfOddCharacter +=1

if (countNumberOfOddCharacter > 1 ):
  print ('No, Can not create palindrom using given sring: "%s"' %givenString)
else:
  print ('Yes. Can create palindrom using given sring: "%s"' %givenString)
