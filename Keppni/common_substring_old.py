from pprint import pprint
from itertools import product as p
from os.path import commonprefix as c

def longest_common_substring(s):
    def r(k):
        s[k] = s[k][1:] + s[k][:1]

    l = 0
    k = [0] * len(s)
    for d in p(*map(lambda x: range(len(x)), s)):
        #print(s)
        #print(k)
        v = len(c(s))
        if v > l:
            l = v
        for i, n in enumerate(d):
            if n != k[i]:
                r(i)
                k[i] = n
        
    return l
    
def _test(a,b):
    value = longest_common_substring(a)
    pprint(value)
    pprint(value == b)

def test():
    _test(['disenchanter', 'hapus', 'hanger', 'haematogenic', 'haughtier', 'hardboot', 'shaled', 'chairmans', 'downhaul', 'charlock', 'mumchances', 'hallucination', 'relishable'], 2)
    _test(['lollipop','kiloliters','xylology'], 3)
    _test(['hello','hello','helloed'], 5)
    _test(['nooooo','yeeeesss'], 0)

test()
