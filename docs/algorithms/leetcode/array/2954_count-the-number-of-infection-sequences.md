# Count the Number of Infection Sequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2954 |
| Difficulty | Hard |
| Topics | Array, Math, Combinatorics |
| Official Link | [count-the-number-of-infection-sequences](https://leetcode.com/problems/count-the-number-of-infection-sequences/) |

## Problem Description & Examples
### Goal
Given an integer `n` representing the total number of computers (indexed 0 to n-1) and an array `sick` representing the indices of initially infected computers, calculate the total number of distinct sequences in which the remaining healthy computers can become infected. An infection spreads to adjacent healthy computers at each time step. The result should be returned modulo 10^9 + 7.

### Function Contract
**Inputs**

- `n`: An integer representing the total number of computers.
- `sick`: A list of integers representing the indices of initially infected computers.

**Return value**

- An integer representing the total number of valid infection sequences modulo 10^9 + 7.

### Examples
**Example 1**

- Input: `n = 5, sick = [0, 4]`
- Output: `4`

**Example 2**

- Input: `n = 4, sick = [1]`
- Output: `3`

**Example 3**

- Input: `n = 4, sick = [0, 1, 2, 3]`
- Output: `1`

---

## Underlying Base Algorithm(s)
The problem is solved using combinatorics. We identify the gaps of healthy computers between infected ones. 
1. For gaps at the ends (before the first sick computer or after the last), there is only one way to fill them (inward).
2. For gaps between two sick computers of size `k`, there are `2^(k-1)` ways to fill them.
3. The total number of ways is the multinomial coefficient of the sizes of all gaps multiplied by the product of the ways to fill each internal gap.

---

## Complexity Analysis
- **Time Complexity**: `O(n)` to precompute factorials and modular inverses.
- **Space Complexity**: `O(n)` to store factorials and their inverses.
