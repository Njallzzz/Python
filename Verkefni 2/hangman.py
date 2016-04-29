import string

def hangman(path, semifilled, guessed):
    with open(path) as file:
       data = file.read().splitlines()

    data = [ x for x in set(data) if len(x) == len(semifilled) and x.isalpha() and x.islower() ]
    data = [ x for x in data if all(map(lambda n: (semifilled[n[0]] == n[1] or semifilled[n[0]] == '-') and n[1] in string.ascii_lowercase, enumerate(x))) ]
    data = [ x for x in data if not any(map(lambda n: semifilled[n[0]] == '-' and n[1] in guessed, enumerate(x))) ]
    return data
