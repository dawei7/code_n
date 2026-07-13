import math
from collections import defaultdict

def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def solve(mat):
    rows = len(mat)
    cols = len(mat[0])
    counts = defaultdict(int)
    
    directions = [
        (0, 1), (0, -1), (1, 0), (-1, 0),
        (1, 1), (1, -1), (-1, 1), (-1, -1)
    ]
    
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                curr_num = 0
                curr_r, curr_c = r, c
                
                while 0 <= curr_r < rows and 0 <= curr_c < cols:
                    curr_num = curr_num * 10 + mat[curr_r][curr_c]
                    
                    if curr_num > 10:
                        if is_prime(curr_num):
                            counts[curr_num] += 1
                    
                    curr_r += dr
                    curr_c += dc
                    
    if not counts:
        return -1
    
    max_freq = 0
    best_prime = -1
    
    for prime, freq in counts.items():
        if freq > max_freq:
            max_freq = freq
            best_prime = prime
        elif freq == max_freq:
            if prime > best_prime:
                best_prime = prime
                
    return best_prime
