from itertools import product
from itertools import chain
from pprint import pprint as print

def hangman(path, semifilled, guessed):
    with open(path) as file:
       data = file.read().splitlines()

    data = [ x for x in set(data) if len(x) == len(semifilled) and x.isalpha() ]        # Remove all not of equal length and limits to english chars only
    data = [ x for x in data if all(map(lambda n: semifilled[n[0]] == n[1] or semifilled[n[0]] == '-', enumerate(x))) ]
    
    data = [ x for x in data if not any(map(lambda n: semifilled[n[0]] == '-' and n[1] in guessed, enumerate(x))) ]
    
    print(data)
    
def _test(a,b,c,d):
    print( hangman(a,b,c) == d )

def test():
    _test('all_words.txt', 's-a--o--s', 'aeiosu', ['scaffolds', 'shamrocks', 'standoffs'])

test()
