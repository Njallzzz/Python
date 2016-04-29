from pprint import pprint as pri
import re

def zen_expand(command):
    filt = re.compile(r'^(?P<param>[^*]+)[*]{0,1}(?P<mult>[0-9]*)')
    ret = ''

    for bracket in command.split('>'):
        for plus in bracket.split('+'):
            pri(plus)
            m = filt.match(plus)
            m = map(lambda x: x['param'], m.groupdict())
            
            pri(m.group() + ':' + str(m.groupdict()))
        
    return ret

def _test(a,b):
    value = zen_expand(a)
    pri('Returned: ' + value)
    pri( value == b )

def test():
    _test("a+div+p*3", "<a></a><div></div><p></p><p></p><p></p>")
    _test("dd", "<dd></dd>")
    _test("table>tr*3>td*2", "<table><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr></table>")

test()
