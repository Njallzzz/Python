def birthdays(a):
    r = tuple(a.splitlines())
    l = []
    for i,x in enumerate(r):
        for y in r[i:]:
            if x[:4] == y[:4] and x != y:
                e = False
                for z in l:
                    for v in z:
                        if v == x:
                            e = True
                        elif v == y:
                            e = -1
                if e == True:
                    n = -1
                    for i,z in enumerate(l):
                        for v in z:
                            if v == x:
                                n = i
                        if n != -1:
                            l[i] = l[i] + (y,)
                            break
                elif e == False:
                    l.append((x,y))
    return l
