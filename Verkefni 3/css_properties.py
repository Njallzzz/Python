def css_properties(s):
    d = s.replace('\n', '').split('}')
    f = ''
    for x in d:
        n  = x.split('{')
        if len(n) > 1:
            f += n[1]
    f = list(filter(None, list(map(lambda y: y.strip(), f.split(';')))))
    f = list( map(lambda x: x.split(':'), f))

    d = []
    for x in f:
        o = x[1].strip()
        j = [x[0].strip()]
        j.append(o)
        d.append(tuple(j))
        
    return d
