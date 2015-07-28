__author__ = 'williamsb'

n= 500

triangle_num_0, triangle_num_1 = 0, 1
triangle_num = 0

def divisors(number):
    divisor_count = 0
    for j in range(1, number):
        if number % j == 0:
            divisor_count += 1
            if divisor_count > 500:
                return True
    return divisor_count

i = 2

while True:
    triangle_num = triangle_num_0 + triangle_num_1
    print triangle_num, divisors(triangle_num)
    triangle_num_0 = triangle_num_1
    triangle_num_1 = triangle_num
