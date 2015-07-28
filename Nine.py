__author__ = 'williamsb'

# a + b + c = 1000
# a^2 + b^2 = c^2
# a < b < c

def is_py(a, b, c):
    return a**2 + b**2 == c**2

def adds_to_thousand(a, b, c):
    return a + b + c == 1000

for c in range (1, 1000):
    for b in range (1, c):
        for a in range(1 , b):
            if is_py(a, b, c) and adds_to_thousand(a, b, c):
                print a * b * c
                exit()