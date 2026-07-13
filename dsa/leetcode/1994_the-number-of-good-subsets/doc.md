# The Number of Good Subsets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1994 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Dynamic Programming, Bit Manipulation, Counting, Number Theory, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [the-number-of-good-subsets](https://leetcode.com/problems/the-number-of-good-subsets/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/the-number-of-good-subsets/).

### Goal
Count non-empty subsets whose product can be written as a product of distinct prime numbers, with no prime factor repeated.

### Function Contract
**Inputs**

- `nums`: integers in the range covered by the problem constraints.

**Return value**

Return the number of good subsets modulo `1_000_000_007`.

### Examples
**Example 1**

- Input: `nums = [1,2,3,4]`
- Output: `6`

**Example 2**

- Input: `nums = [4,2,3,15]`
- Output: `5`

**Example 3**

- Input: `nums = [1,1,2]`
- Output: `4`

---

## Solution
### Approach
Represent each valid number by a prime-factor bitmask; numbers containing a squared prime factor are ignored. Run subset DP over masks, adding each value count when its mask is disjoint from the current mask. Ones multiply the final count by `2^count(1)`.

### Complexity Analysis
- **Time Complexity**: `O(U * 2^P)`, where `U` is the value range and `P` is the number of tracked primes.
- **Space Complexity**: `O(2^P)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
