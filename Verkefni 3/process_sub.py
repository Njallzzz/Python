import os

def parse_submissions(f):
    l = []
    for p, k, v in os.walk(f):
        if v:
            for i in v:
                l.append(os.path.join(p, i))
    r = []
    for b in l:
        o = [[],[],[],[]]
        with open(b) as cf:
            d = list(map(lambda x: x.split(), cf.read().splitlines()))
        for n in d:
            if 'Classify' in n[1]:
                o[0] = n[2]
            if 'Team' in n[1]:
                o[1] = n[2]
            if 'Problem' in n[1]:
                o[2] = n[2]
            if 'Date' in n[1]:
                o[3] = n[2]
        if o[0] == 'Accepted':
            del o[0]
            r.append(o)
    return list(map(lambda x: (x[0], x[1]), sorted(r, key=lambda x: x[2])))
