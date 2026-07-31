# Partition Array for Maximum XOR and AND

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3630 |
| Difficulty | Hard |
| Topics | Array, Math, Greedy, Bit Manipulation, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/partition-array-for-maximum-xor-and-and/) |

## Problem Description
### Goal

Given an integer array `nums`, assign every element to exactly one of three subsequences `A`, `B`, and `C`. Any of the three subsequences may be empty, and the original relative order within a subsequence does not affect its bitwise aggregate.

The value of a partition is `XOR(A) + AND(B) + XOR(C)`. The XOR of an empty subsequence and the AND of an empty subsequence are both defined as zero for this problem. Determine the greatest value obtainable over all valid assignments of the array elements.

Only the maximum numeric value is required. If several partitions achieve it, any of them is equally valid.

### Function Contract
**Inputs**

- `nums`: A list of $n$ positive integers, where $1 \le n \le 19$ and $1 \le \texttt{nums[i]} \le 10^9$.

**Return value**

Return an integer equal to the maximum possible value of `XOR(A) + AND(B) + XOR(C)` over all three-way partitions.

### Examples
**Example 1**

- Input: `nums = [2, 3]`
- Output: `5`
- Explanation: Put 3 in `A`, 2 in `B`, and leave `C` empty to obtain $3+2+0=5$.

**Example 2**

- Input: `nums = [1, 3, 2]`
- Output: `6`
- Explanation: The singleton groups `A = [1]`, `B = [2]`, and `C = [3]` contribute $1+2+3=6$.

**Example 3**

- Input: `nums = [2, 3, 6, 7]`
- Output: `15`
- Explanation: One optimum uses `A = [7]`, `B = [2, 3]`, and `C = [6]`, giving $7+2+6=15$.
