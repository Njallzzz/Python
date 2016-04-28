from itertools import product as p
from itertools import chain as c

def insert_operators(e, t):
    for d in p(['+', '-', ''], repeat=len(e)-1):
        k = ''.join( str(v) for v in list(c.from_iterable(zip(e, d))) + [e[-1]] )
        if eval(k) == t:
            return k + "=" + str(t)

