from functools import cache
@cache
def is_interesting_number(num):
    digit_sum = sum(int(digit) for digit in str(num))
    return num % digit_sum == 0

def count_interesting_numbers(N):
    count = 0
    for num in range(1, N+1):
        if is_interesting_number(num):
            count += 1
    return count

N = int(input())
count = count_interesting_numbers(N)
print(count)
