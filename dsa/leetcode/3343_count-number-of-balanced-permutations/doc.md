# Count Number of Balanced Permutations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3343 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, String, Dynamic Programming, Combinatorics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-number-of-balanced-permutations/) |

## Problem Description

### Goal

You are given a decimal digit string `num`. A permutation uses every character exactly once, including every repeated copy and every zero. Two permutations are distinct only when their resulting digit strings differ; exchanging equal copies does not create another result.

Using zero-based indices, a permutation is balanced when the sum of its digits at even indices equals the sum at odd indices. Count all distinct balanced permutations of `num`. Because this count can be very large, return it modulo $10^9+7$.

### Function Contract

**Inputs**

- `num`: A string of $n$ decimal digits, where $2 \le n \le 80$.

**Return value**

- The number of distinct balanced permutations, reduced modulo $10^9+7$.

### Examples

#### Example 1

- **Input:** `num = "123"`
- **Output:** `2`
- **Explanation:** Among its six permutations, `"132"` and `"231"` have equal even- and odd-index sums.

#### Example 2

- **Input:** `num = "112"`
- **Output:** `1`
- **Explanation:** Only `"121"` is balanced; swapping the two equal `1` digits does not create another permutation.

#### Example 3

- **Input:** `num = "12345"`
- **Output:** `0`
