__author__ = 'williamsb'

num = 1

def is_divisible(number):
    for i in range(1, 21):
        if number % i != 0:
            return False
    return True

for i in range(2, 21):
    num *= i

counter = 1

while True:
    for i in range(2, 21):
        if num % i == 0:
            if is_divisible(num/i):
                num /= i
                print num