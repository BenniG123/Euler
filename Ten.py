__author__ = 'williamsb'

# I solved this using the Sieve of Eratosthenes

max_prime = 2000000
prime_sum = 0
numbers = range(2, max_prime)
is_prime = [True] * len(numbers)

for p in numbers:
    if is_prime[p - 2]:
        print p
        p_remove = p + p
        while p_remove < max_prime:
            is_prime[p_remove - 2] = False
            p_remove += p

for i in xrange(0, len(is_prime)):
    if is_prime[i]:
        print numbers[i]
        prime_sum += numbers[i]

print prime_sum
