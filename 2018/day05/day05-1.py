#!/usr/bin/python

import re

search_string = "(aA|Aa|bB|Bb|cC|Cc|dD|Dd|eE|Ee|fF|Ff|gG|Gg|hH|Hh|iI|Ii|jJ|Jj|kK|Kk|lL|Ll|mM|Mm|nN|Nn|oO|Oo|pP|Pp|qQ|Qq|rR|Rr|sS|Ss|tT|Tt|uU|Uu|vV|Vv|wW|Ww|xX|Xx|yY|Yy|zZ|Zz)"
regex = re.compile(search_string)

file = open("input.txt")
lines = file.read().split("\n")

for line in lines:
    while regex.search(line) is not None:
        line = regex.sub("", line)

print line, len(line)
