import itertools
from itertools import starmap as m

def rank_hand(l):
    compare = "123456789TJQKA"
    l = [ [compare.index(x[0]), x[1]] for x in sorted(l, key=lambda x: compare.index(x[0])) ]
    t = zip(*l)

    pairs = 0
    tripairs = 0
    fourpairs = 0
    for x in set(t[0]):
        if t[0].count(x) == 2:
            pairs += 1
        elif t[0].count(x) == 3:
            tripairs += 1
        elif t[0].count(x) == 4:
            fourpairs += 1
    uniques = len(set(t[0]))
    straight = all( [ x == y-1 for x,y in zip(t[0], t[0][1:]) ] )
    #straight = all( m(lambda x,y: x == y-1, zip(t[0], t[0][1:])) )

    if fourpairs:
        return 7
    if tripairs and pairs:
        return 6
    if( len(set(t[1])) == 1 ):  # Check next if in seq then royal or straight else flush
        if t[0][0] == 9 and straight:
            return 9
        if straight:
            return 8

        if tripairs and pairs:
            return 6
        return 5 # if not royal or straight flush then flush
    if straight:
        return 4
    if tripairs:
        return 3
    if uniques < 5:     ## Deals with 1 & 2
        return 5 - uniques
    return 0


def _do_test(a, expected):
    print rank_hand(a) == expected

def test():
    _do_test([ '3D', '2H', '3C', 'QS', '8D' ], 1)
    _do_test([ 'KD', 'KH', 'KC', 'TS', 'TD' ], 6)
    _do_test([ 'JD', 'KD', 'TD', 'QD', 'AD' ], 9)
        
test()
