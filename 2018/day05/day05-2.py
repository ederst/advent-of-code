#!/usr/bin/python

import re, sys

def char_range(c1, c2):
    for c in xrange(ord(c1), ord(c2)+1):
        yield chr(c)

search_string = "(aA|Aa|bB|Bb|cC|Cc|dD|Dd|eE|Ee|fF|Ff|gG|Gg|hH|Hh|iI|Ii|jJ|Jj|kK|Kk|lL|Ll|mM|Mm|nN|Nn|oO|Oo|pP|Pp|qQ|Qq|rR|Rr|sS|Ss|tT|Tt|uU|Uu|vV|Vv|wW|Ww|xX|Xx|yY|Yy|zZ|Zz)"
regex = re.compile(search_string)

file = open("input.txt")
lines = file.read().split("\n")


for line in lines:
    best = sys.maxint
    for polymer in char_range('a','z'):
        print "Processing: %s" % polymer
        lineNoPoly = re.sub(polymer, "", line, flags=re.IGNORECASE)
        while regex.search(lineNoPoly) is not None:
            lineNoPoly = regex.sub("", lineNoPoly)
        
        current = len(lineNoPoly)
        if current < best:
            best = current

print best
