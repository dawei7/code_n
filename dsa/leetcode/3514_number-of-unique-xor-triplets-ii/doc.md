# Number of Unique XOR Triplets II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3514 |
| Difficulty | Medium |
| Topics | Array, Math, Bit Manipulation, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-unique-xor-triplets-ii/) |

## Problem Description
### Goal
You are given an integer array `nums`. Its values need not be distinct or form a consecutive range.

Choose three indices satisfying $0 \le i \le j \le k<n$. The value of that XOR triplet is `nums[i] XOR nums[j] XOR nums[k]`. Because the inequalities are non-strict, one array position may supply two or all three operands. Different index choices can produce the same result.

Evaluate the possible triplets conceptually and return the number of distinct XOR values among them. Count each resulting integer once, regardless of how many index triplets generate it.

### Function Contract
**Inputs**

- `nums`: A list of $n$ positive integers, where $1 \le n \le 1500$ and $1 \le \texttt{nums[i]} \le 1500$.

**Return value**

Return the number of unique values `nums[i] XOR nums[j] XOR nums[k]` attainable with $i \le j \le k$.

### Examples
**Example 1**

- Input: `nums = [1, 3]`
- Output: `2`
- Explanation: Every valid triplet produces either `1` or `3`.

**Example 2**

- Input: `nums = [6, 7, 8, 9]`
- Output: `4`
- Explanation: The attainable values are `6`, `7`, `8`, and `9`.
