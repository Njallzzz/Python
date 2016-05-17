from pprint import pprint
from datetime import datetime as date

def c(s):
    n = list(range(2,8))[::-1]
    mod = 11 - (sum([ n[x-2] * int(s[x]) for x in range(8) ]) % 11)
    return mod

def valid(s):
    try:
        if s[9] == '9':
            y = '19'
        elif s[9] == '0':
            y = '20'
        if date.strptime(s[:4]+y+s[4:6], '%d%m%Y') and int(s[8]) == c(s[:8]):
            return True
    except:
        pass
    return False
