# http://codeforces.com/problemset/problem/1/B
from math import log, ceil

def debug(s):
    if False:
        print s

def string_of_int(n):
    s = ['' for i in range(int(ceil(log(n) / log(26))))]
    i = len(s) - 1
    while i >= 0:
        r = (n - 1) % 26
        s[i] = chr(ord('A') + r)
        n /= 26
        i -= 1
    return ''.join(s)

def int_of_string(s):
    n = 0
    for i in range(len(s)):
        p = len(s) - i - 1
        digit = ord(s[i]) - ord('A') + 1
        n += digit * (26**p)
    return n

n = int(raw_input())

for _ in range(n):
    s = raw_input()

    # FIRST: Determine whether we're converting from rowcol or from excel
    i = 0
    # get index of first non-alphabet character
    for char in s:
        if not (ord('A') <= ord(char) <= ord('Z')):
            break
        i += 1
    # we now have i, index of first non alphabet char, i.e. 2 in R23C55
    # or 2 in BC23
    # if there are alphanumeric characters after i, it must be rowcol
    # otherwise, must be excel-type
    rowcol = False
    j = 0
    for ind in range(i, len(s)):
        if (ord('A') <= ord(s[ind]) <= ord('Z')):
            rowcol = True
            j = ind
            break

    if rowcol:
        row = int(s[i:j])
        col = int(s[j + 1:])
        debug("converting from row col format; src %s, %s" % (row, col))
        colstr = string_of_int(col)
        print "%s%s" % (colstr, row)
    else:
        col = s[:i]
        row = int(s[i:])
        debug("converting from excel format; src %s, %s" % (row, col))
        colnum = int_of_string(col)
        print "R%sC%s" % (row, colnum)
