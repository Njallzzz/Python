
def balanced(s):
    l = []
    for c in s:
        if c == '(':
            l.append(c)
        else:
            try:
                l.pop()
            except:
                return False

    return not bool(len(l))
