from itertools import product as p
from itertools import chain as c

def hangman(path, semi, guessed):
    for d in p(['+', '-', ''], repeat=len(e)-1):
        k = ''.join( str(v) for v in list(c.from_iterable(zip(e, d))) + [e[-1]] )
        if eval(k) == t:
            return k + "=" + str(t)

def _test(a,b,c,d):
    print( hangman(a,b,c) == d )


def test():
    _test('all_words.txt', 's-a--o--s', 'aeiosu', ['scaffolds', 'shamrocks', 'standoffs'])

test()
