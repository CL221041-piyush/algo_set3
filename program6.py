def is_palindrome(s):
    return s == s[::-1]

def min_cyclic_shifts_to_palindrome(s):
    n = len(s)
    
    # Check all cyclic shifts of the string
    for i in range(n):
        # Generate the string after cyclic shift by i positions
        shifted_s = s[i:] + s[:i]
        # Check if this shifted string is a palindrome
        if is_palindrome(shifted_s):
            return i
    return -1

# Read number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    s = input().strip()
    result = min_cyclic_shifts_to_palindrome(s)
    print(result)
