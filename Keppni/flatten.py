def a(l):
    def c(v):
        return sum( [ 1 for x in l if l[v] > x ] )
    return c
 
def flatten(l):
    d = a(l)
    return list(map(d, range(len(l))))
