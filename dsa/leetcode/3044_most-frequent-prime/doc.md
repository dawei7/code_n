# Most Frequent Prime

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3044 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Matrix, Counting, Enumeration, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [most-frequent-prime](https://leetcode.com/problems/most-frequent-prime/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/most-frequent-prime/).

### Goal
Given a 2D grid of digits, identify all possible numbers formed by traversing the grid in any of the eight cardinal or ordinal directions (horizontal, vertical, or diagonal). Among all numbers greater than 10 that are prime, return the one that appears most frequently. If multiple primes share the same maximum frequency, return the largest prime. If no such prime exists, return -1.

### Function Contract
**Inputs**

- `mat`: A `List[List[int]]` representing the grid of digits.

**Return value**

- `int`: The most frequent prime number found, or -1 if none exist.

### Examples
**Example 1**

- Input: `mat = [[1,1],[3,4]]`
- Output: `13`
- Explanation: Possible numbers include 11, 13, 14, 31, 34, 41, 43, etc. 13 is prime and appears most frequently.

**Example 2**

- Input: `mat = [[7]]`
- Output: `-1`
- Explanation: Numbers must be greater than 10 to be considered.

**Example 3**

- Input: `mat = [[9,7,8],[4,6,5],[2,8,6]]`
- Output: `97`

---

## Solution
### Approach
The solution utilizes a brute-force traversal of the grid in all 8 directions. For every cell `(r, c)` and every direction `(dr, dc)`, we construct all possible numbers by extending the path until the grid boundaries are reached. We use a Sieve of Eratosthenes or a primality test to validate numbers, and a hash map (dictionary) to track the frequency of each prime found.

### Complexity Analysis
- **Time Complexity**: `O(R * C * max(R, C) * sqrt(N))`, where `R` and `C` are grid dimensions and `N` is the maximum possible number formed (limited by grid size).
- **Space Complexity**: `O(R * C * max(R, C))` to store the frequencies of the generated numbers in a hash map.

### Reference Implementations
<details>
<summary>python</summary>

```python
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
```
</details>
