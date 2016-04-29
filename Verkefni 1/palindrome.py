def palindrome(n, b):
    def z(n, b):
        if n < b:
            return [n]
        else:
            return z(n//b, b) + [n%b]
    return z(n,b) == z(n,b)[::-1]   
