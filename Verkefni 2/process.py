def process_ls(a):
    return [ ' '.join(y[8:]) for y in sorted( [x.split() for x in a.splitlines() if x[0] == '-'], key=lambda x: int(x[4]), reverse=True) ]
