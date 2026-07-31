# Find the Count of Good Integers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3272 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Hash Table, Math, Combinatorics, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-count-of-good-integers/) |

## Problem Description

### Goal

An integer is `k`-palindromic when its decimal representation is a palindrome and its value is divisible by `k`. An $n$-digit integer is good when its digits can be rearranged to form some $n$-digit `k`-palindromic integer.

Count all good $n$-digit integers. Neither an original integer nor its palindromic rearrangement may begin with zero. Different integer arrangements of the same digit multiset are counted separately, but a single integer is counted only once even if its digits can form several divisible palindromes.

### Function Contract

**Inputs**

- `n`: The required digit count, where $1 \le n \le 10$.
- `k`: The divisor, where $1 \le k \le 9$.

Let $h = \lceil n/2 \rceil$ and let

$$
p = 9 \cdot 10^{h-1}
$$

be the number of legal $h$-digit palindrome halves.

**Return value**

- The number of $n$-digit integers whose digit multiset can form at least one $n$-digit palindrome divisible by `k`.

### Examples

**Example 1**

- Input: `n = 3, k = 5`
- Output: `27`

For example, `551` can become `515`, and `525` already qualifies.

**Example 2**

- Input: `n = 1, k = 4`
- Output: `2`

The qualifying one-digit integers are `4` and `8`.

**Example 3**

- Input: `n = 5, k = 6`
- Output: `2468`
