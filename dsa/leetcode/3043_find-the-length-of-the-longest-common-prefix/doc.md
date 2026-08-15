# Find the Length of the Longest Common Prefix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3043 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Trie |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/) |

## Problem Description

### Goal

You are given two arrays, `arr1` and `arr2`, whose entries are positive integers.

A prefix of an integer is formed from one or more consecutive digits beginning at its leftmost digit. Thus, `123` is a prefix of `12345`, but `234` is not. A common prefix of two integers is a positive integer that is a prefix of both. For example, `5655359` and `56554` share the prefixes `565` and `5655`, whereas `1223` and `43456` share none.

Consider every cross-array pair `(x, y)` with `x` chosen from `arr1` and `y` chosen from `arr2`. Return the greatest number of digits in a common prefix of any such pair. Return `0` when no cross-array pair begins with the same digit. Prefixes shared only by two entries of the same array do not count.

### Function Contract

Let $n=\lvert\texttt{arr1}\rvert$, $m=\lvert\texttt{arr2}\rvert$, and let $d$ be the maximum number of decimal digits in any input value.

**Inputs**

- `arr1`: An array of $n$ positive integers.
- `arr2`: An array of $m$ positive integers.

Both arrays satisfy $1 \le n,m \le 5\cdot10^4$. Every entry is between $1$ and $10^8$ inclusive, so $1 \le d \le 9$.

**Return value**

Return the maximum length of a decimal prefix shared by one value from each array, or `0` if no such prefix exists.

### Examples

#### Example 1

- **Input:** `arr1 = [1,10,100], arr2 = [1000]`
- **Output:** `3`
- **Explanation:** The three cross-array pairs have longest common prefixes `1`, `10`, and `100`; the last has length `3`.

#### Example 2

- **Input:** `arr1 = [1,2,3], arr2 = [4,4,4]`
- **Output:** `0`
- **Explanation:** No value from the first array begins with the same digit as a value from the second array. Similarity between values inside one array is irrelevant.
