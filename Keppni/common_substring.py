from os.path import commonprefix as c
from itertools import product as h

def r(e):
    return e[1:] + e[:1]

def g(l):
    m = l.pop()    
    if len(l) > 1:
        b = g(l)
    else:
        b = [l[0]]
    n = ['']
    for e in b:
        for _ in e:
            for _ in m:
                t = c([e, m])
                if not (t in n):
                    n.append(t)
                m = r(m)
            e = r(e)
    return n
    
def longest_common_substring(s):
    return max(map(lambda x: len(x), g(s)))
