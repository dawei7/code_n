# Maximum Possible Number by Binary Concatenation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3309 |
| Difficulty | Medium |
| Topics | Array, Bit Manipulation, Enumeration |
| Official Link | [maximum-possible-number-by-binary-concatenation](https://leetcode.com/problems/maximum-possible-number-by-binary-concatenation/) |

## Problem Description & Examples
### Goal
Given an array of three integers, determine the largest possible integer that can be formed by concatenating the binary representations of these three integers in any arbitrary order.

### Function Contract
**Inputs**

- `nums`: A list of exactly three integers (where each integer is between 1 and 127).

**Return value**

- An integer representing the maximum value achievable after concatenating the binary strings of the input numbers in any permutation.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3]`
- Output: `30`
- Explanation: Binary representations are 1 (1), 2 (10), 3 (11). Concatenating as 3, 2, 1 gives "11101" which is 29, but 3, 1, 2 gives "11110" which is 30.

**Example 2**

- Input: `nums = [2, 8, 16]`
- Output: `1296`
- Explanation: Concatenating 16, 8, 2 gives "10000100010" which is 1296.

**Example 3**

- Input: `nums = [1, 1, 1]`
- Output: `7`
- Explanation: Concatenating 1, 1, 1 gives "111" which is 7.

---

## Underlying Base Algorithm(s)
The problem is solved using **Permutation Enumeration**. Since the input array size is fixed at 3, there are only $3! = 6$ possible permutations. We generate all permutations, convert each integer to its binary string representation (excluding the '0b' prefix), concatenate them, and convert the resulting binary string back to a decimal integer to find the maximum.

---

## Complexity Analysis
- **Time Complexity**: $O(1)$. Since the input size is fixed at 3, the number of permutations is constant (6), and the bit length of each number is small (max 7 bits), leading to constant time execution.
- **Space Complexity**: $O(1)$. We only store a constant number of strings and integers regardless of the input values.
