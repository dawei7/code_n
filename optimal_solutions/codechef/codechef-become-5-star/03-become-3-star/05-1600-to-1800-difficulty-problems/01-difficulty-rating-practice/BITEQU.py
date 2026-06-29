import sys
import random
from time import time

# Initialize random seed based on current time
random.seed(int(time()))

def solve(n):
    mx = 10**17  # maximum value for a, b, c as per original code

    while True:
        a = random.randint(1, mx)
        
        # Ensure b is different from a
        while True:
            b = random.randint(1, mx)
            if b != a:
                break

        # Ensure c is different from a and b
        while True:
            c = random.randint(1, mx)
            if c != a and c != b:
                break

        d = (a & b) | c
        d ^= n

        # Ensure d is unique and non-zero
        if d != 0 and d != a and d != b and d != c:
            print(a, b, c, d)
            break

# Read input
input = sys.stdin.read
data = input().split()
t = int(data[0])

# Iterate over test cases
for i in range(1, t + 1):
    n = int(data[i])
    solve(n)


if __name__ == "__main__":
    solve()
