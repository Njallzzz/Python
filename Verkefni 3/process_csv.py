import csv

def process_csv(p):
    returndict = {}
    with open(p, encoding='UTF-8') as f:
        data = csv.reader(f)
        for row in data:
            returndict.setdefault(row[0], 0)
            returndict[row[0]] += int(row[2])* int(row[3]) 
    return returndict
