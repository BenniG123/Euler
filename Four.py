__author__ = 'williamsb'

def is_palindrome(number):
    string = str(number)
    start = 0
    end = len(string) - 1

    while string[start] == string[end] and start < end:
            start += 1
            end -= 1

    return start > end

max_palindrome = 1

for i in range(0, 999):
    for j in range(0, 999):
        if is_palindrome(i * j) and max_palindrome < i*j:
            max_palindrome = i*j

print max_palindrome
