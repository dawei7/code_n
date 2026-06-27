# Most Frequent Prime

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3044 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Math, Matrix, Counting, Enumeration, Number Theory |
| Official Link | [most-frequent-prime](https://leetcode.com/problems/most-frequent-prime/) |

## Problem Description & Examples
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

## Underlying Base Algorithm(s)
The solution utilizes a brute-force traversal of the grid in all 8 directions. For every cell `(r, c)` and every direction `(dr, dc)`, we construct all possible numbers by extending the path until the grid boundaries are reached. We use a Sieve of Eratosthenes or a primality test to validate numbers, and a hash map (dictionary) to track the frequency of each prime found.

---

## Complexity Analysis
- **Time Complexity**: `O(R * C * max(R, C) * sqrt(N))`, where `R` and `C` are grid dimensions and `N` is the maximum possible number formed (limited by grid size).
- **Space Complexity**: `O(R * C * max(R, C))` to store the frequencies of the generated numbers in a hash map.
