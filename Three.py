__author__ = 'williamsb'


def is_prime(factor):
    if factor == 2:
        return True

    for i in range(2, factor):
        if factor % i == 0:
            return False

    # print "Next prime factor ", factor
    return True

number = 600851475143
prime_factor = 2
max_prime_factor = 1

while True:
    if number % prime_factor == 0:
        number /= prime_factor
        max_prime_factor = prime_factor
        print max_prime_factor, number
    elif number == 1:
        break
    else:
        prime_factor += 1
        while not is_prime(prime_factor):
            prime_factor += 1

print max_prime_factor