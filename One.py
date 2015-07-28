__author__ = 'williamsb'

multiple_3 = 3
multiple_5 = 5
sum = 0

while multiple_3 < 1000:
    if multiple_3 % 5 != 0:
        sum += multiple_3
    multiple_3 += 3

while multiple_5 < 1000:
    sum += multiple_5
    multiple_5 += 5

print sum