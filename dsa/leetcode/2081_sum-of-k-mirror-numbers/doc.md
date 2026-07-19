# Sum of k-Mirror Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2081 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-k-mirror-numbers/) |

## Problem Description

### Goal

A positive integer is a `k`-mirror number when its representation has no leading zero and is a palindrome in both ordinary base 10 and base `k`. Palindromic means that the digit sequence is identical when read from left to right or from right to left.

For example, decimal 9 qualifies for base 2 because its binary representation is `1001`, while decimal 4 does not because binary `100` is not palindromic. Given `k` and a count `n`, find the `n` smallest qualifying positive integers and return their sum.

### Function Contract

**Inputs**

- `k`: the second numeral base, where $2 \le k \le 9$.
- `n`: the number of smallest qualifying integers to sum, where $1 \le n \le 30$.

**Return value**

- Return the sum of the $n$ smallest positive integers whose base-10 and base-`k` digit sequences are both palindromes.

### Examples

**Example 1**

- Input: `k = 2, n = 5`
- Output: `25`
- Explanation: The first five values are `1, 3, 5, 7, 9`, whose binary forms are also palindromes.

**Example 2**

- Input: `k = 3, n = 7`
- Output: `499`
- Explanation: The values are `1, 2, 4, 8, 121, 151, 212`.

**Example 3**

- Input: `k = 7, n = 17`
- Output: `20379000`
- Explanation: The first seventeen include the one-digit values `1` through `6`, followed by larger numbers that remain palindromic in both bases.
