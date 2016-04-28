def countdown(p, l):
    l = [ [x, True] for x in (sorted(l)) ]

    with open(p) as f:
        f = f.read().splitlines()
    returnlist = []
    
    for name in f:
        lis = l.copy()
        word_valid = True
        for name_let in name:
            inside = False
            for i,ref_let in enumerate(l):
                if name_let in lis[i][0] and lis[i][1] and not inside:
                    lis[i] = [name_let, False]
                    inside = True
                    break
            if not inside:
              word_valid = False
        if word_valid:
            returnlist.append(name)

    return returnlist
