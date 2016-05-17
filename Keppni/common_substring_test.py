from pprint import pprint
from itertools import product as p
from os.path import commonprefix as c

def longest_common_substring(s):
    def r(k):
        s[k] = s[k][1:] + s[k][:1]

    l = 0
    k = [0]*len(s)
    for d in p(*map(lambda x: range(len(x)), s)):
        v = len(c(s))
        if v > l:
            l = v
        for i, n in enumerate(d):
            if n != k[i]:
                r(i)
                k[i] = n
        
    return l
