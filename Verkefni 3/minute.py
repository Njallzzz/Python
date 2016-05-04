from pprint import pprint
import re

def jam(data):
    returndict = {}
    lis = []
    m = re.compile(r'[0-9]{4}, (.*) with ([^,]*), ([^,]*), (.*) and ([^,]*),')
    m2 = re.compile(r'[0-9]{4}, (.*) with ([^,]*), (.*) and ([^,]*),')
    m3 = re.compile(r'[0-9]{4}, (.*),')
    for row in data.splitlines():
        if len(row.split(',')) == 5 and m.search(row):
            lis.append(m.search(row).groups())
        elif len(row.split(',')) == 4 and m2.search(row):
            lis.append(m2.search(row).groups())
        else:
            if m3.search(row):
                print(m3.search(row).group(1))

            else:
                print('Unable to parse: %s' % row)

    #pprint(lis)

    for day in lis:
        for entry in day:
            returndict.setdefault(entry, 0)
            returndict[entry] += 1
    return returndict
   
def _test(a,b):
    value = jam(a)
    pprint(value)
    pprint(value == b)

def test():
    inputs = """1/1/1 22 December 1967, Nicholas Parsons with Derek Nimmo, Clement Freud, Wilma Ewart and Beryl Reid, excuses for being late.
2/1/2 29 December 1967, Nicholas Parsons with Derek Nimmo, Clement Freud, Sheila Hancock and Carol Binstead, bedrooms.
3/1/3 5 January 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Betty Marsden and Elisabeth Beresford, ?
4/1/4 12 January 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Isobel Barnett and Bettine Le Beau, ?
5/1/5 20 January 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Andree Melly and Prunella Scales, the brownies
6/1/6 27 January 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Marjorie Proops and Millie Small, ?
7/1/7 2 February 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Aimi Macdonald and Una Stubbs, my honeymoon.
8/1/8 9 February 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Lucy Bartlett and Anona Winn, bloomer.
9/1/9 17 February 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Andree Melly and Charmian Innes, ?
10/1/10 23 February 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Barbara Blake and Renee Houston, my first grown-up dress.
19/2/3 14 October 1968, Geraldine Jones with Kenneth Williams, Clement Freud and Nicholas Parsons, how to eat macaroni delicately and without cutting it.
577/42/1 1 January 2003, Nicholas Parsons with Paul Merton, Clement Freud, Sheila Hancock and Graham Norton, plus Gyles Brandreth, Jenny Eclair, Ross Noble, Chris Neill, Steve Frost, Charles Collingwood, Pam Ayres, Helen Boaden and Malcolm Messiter, Just A Minute in 2050.
683/52/1 31 December 2007, Nicholas Parsons with Paul Merton, Kenneth Williams, Clement Freud and Graham Norton, plus Derek Nimmo, Peter Jones, Tony Hawks, Sheila Hancock, Gyles Brandreth, Julian Clary, Linda Smith, Jenny Eclair, Ross Noble, Stephen Fry, Chris Neill, Alfred Marks, Barry Took, Tommy Trinder, Kenny Everett and Bob Monkhouse, 40th anniversary special."""

    _test(inputs, {'Aimi Macdonald': 1,
 'Andree Melly': 2,
 'Anona Winn': 1,
 'Barbara Blake': 1,
 'Beryl Reid': 1,
 'Paul Merton': 1,
 'Bettine Le Beau': 1,
 'Betty Marsden': 1,
 'Carol Binstead': 1,
 'Charmian Innes': 1,
 'Clement Freud': 12,
 'Derek Nimmo': 10,
 'Graham Norton': 1,
 'Gyles Brandreth': 1,
 'Jenny Eclair': 1,
 'Steve Frost': 1,
 'Charles Collingwood': 1,
 'Helen Boaden': 1,
 'Malcom Messiter': 1,
 'Ross Noble': 1,
 'Chris Neill': 1,
 'Elisabeth Beresford': 1,
 'Isobel Barnett': 1,
 'Lucy Bartlett': 1,
 'Marjorie Proops': 1,
 'Millie Small': 1,
 'Nicholas Parsons': 12,
 'Kenneth Williams': 1,
 'Geraldine Jones': 1,
 'Prunella Scales': 1,
 'Renee Houston': 1,
 'Sheila Hancock': 2,
 'Una Stubbs': 1,
 'Wilma Ewart': 1})

test()
