# Prime In Diagonal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2614 |
| Difficulty | Easy |
| Topics | Array, Math, Matrix, Number Theory |
| Official Link | [prime-in-diagonal](https://leetcode.com/problems/prime-in-diagonal/) |

## Problem Description & Examples
### Goal
Given a square matrix of integers, identify the largest prime number that appears on either the primary diagonal (top-left to bottom-right) or the secondary diagonal (top-right to bottom-left). If no prime numbers are found on these diagonals, return 0.

### Function Contract
**Inputs**

- `nums`: A list of lists of integers representing a square $n \times n$ matrix.

**Return value**

- An integer representing the maximum prime number found on the diagonals, or 0 if none exist.

### Examples
**Example 1**

- Input: `[[1,2,3],[5,6,7],[9,10,11]]`
- Output: `11`
- Explanation: The diagonals contain [1, 6, 11] and [3, 6, 9]. The primes are 3 and 11. The maximum is 11.

**Example 2**

- Input: `[[1,2,3],[5,17,7],[9,11,1]]`
- Output: `17`
- Explanation: The diagonals contain [1, 17, 1] and [3, 17, 9]. The prime is 17.

**Example 3**

- Input: `[[4,4],[4,4]]`
- Output: `0`
- Explanation: No prime numbers exist on the diagonals.

---

## Underlying Base Algorithm(s)
The solution utilizes a primality test (trial division up to the square root of the number) combined with a linear scan of the matrix diagonals. Since the matrix is square, the primary diagonal elements are at `nums[i][i]` and the secondary diagonal elements are at `nums[i][n - 1 - i]`.

---

## Complexity Analysis
- **Time Complexity**: $O(n \sqrt{m})$, where $n$ is the dimension of the matrix and $m$ is the maximum value in the matrix. We iterate through $2n$ diagonal elements and perform a primality test on each.
- **Space Complexity**: $O(1)$, as we only store the current maximum prime found.
