import math

primes = [2, 3, 5, 7, 11, 13, 17, 19]

def is_square_free(n):
    for p in primes:
        if n % (p * p) == 0:
            return False
    return True

def count_square_free_divisors(N):
    square_free_count = 0
    for i in range(1, int(math.sqrt(N)) + 1):
        if N % i == 0:
            if i != 1 and is_square_free(i):
                square_free_count += 1
            
            if i != N // i:
                if (N // i) != 1 and is_square_free(N // i):
                    square_free_count += 1
    return square_free_count

N = int(input())

print(count_square_free_divisors(N))

