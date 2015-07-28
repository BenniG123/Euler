__author__ = 'williamsb'

prime_counter = 0
next_prime = 0

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

while prime_counter < 10002:
    next_prime += 1
    if is_prime(next_prime):
        prime_counter += 1
        print next_prime

print next_prime