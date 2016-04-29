def rank_hand(l):
    c = "123456789TJQKA"
    l = [ [c.index(x[0]), x[1]] for x in sorted(l, key=lambda x: c.index(x[0])) ]
    t = list(zip(*l))

    p = 0
    m = 0
    f = 0
    for x in set(t[0]):
        if t[0].count(x) == 2:
            p += 1
        elif t[0].count(x) == 3:
            m += 1
        elif t[0].count(x) == 4:
            f += 1
    u = len(set(t[0]))
    s = all( [ x == y-1 for x,y in zip(t[0], t[0][1:]) ] )

    if f:
        return 7
    if m and p:
        return 6
    if( len(set(t[1])) == 1 ):
        if t[0][0] == 9 and s:
            return 9
        if s:
            return 8
        return 5
    if s:
        return 4
    if m:
        return 3
    if u < 5:
        return 5 - u
    return 0
