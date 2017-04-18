#/usr/bin/env python
import re
import sys
import collections

# How to use:
# python script_name.py <filename>


# Take filename as first argument.
f = sys.argv[1]

search_term = '301'
search_term2 = '(?<=\[).*(?= -0500\])'
search_list = []

for line in open(f, 'r'):
  if re.search(search_term, line):
    if re.search(search_term2, line):
      search_term2_output = re.search(search_term2, line).group(0)
      search_list += [search_term2_output]
      if line == None:
        print 'no matches found'

output = collections.Counter(search_list).most_common()
print (output)
