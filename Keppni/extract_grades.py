from re import match as m

def extract(s):
    for x in zip('Ool', '001'):
        s = s.replace(*x)
    s = [ x for x in s.upper() if m('[0-9A-Z]', x) ]

    d = []
    for i, e in enumerate(zip(s, s[1:])):
        if e == ('1', '0'):
            s[i] = '10'
            d.append(i+1)
    for e in d[::-1]:
        del s[e]

    if any(map(lambda x: not m(r'^[4-9SM]|10$', x), s)):
        return None
    return s
