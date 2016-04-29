def excel_index(a):
    num = 0
    for o,y in enumerate(a[::-1]):
        num += 26 ** o * (ord(y) - 64)
    return num
