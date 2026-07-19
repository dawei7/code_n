# Count Triplets That Can Form Two Arrays of Equal XOR

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1442 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Math, Bit Manipulation, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/) |

## Problem Description
### Goal

Given an integer array `arr`, choose indices `i`, `j`, and `k` satisfying
$0 \le i < j \le k < n$, where $n$ is the length of `arr`. The first
contiguous part begins at `i` and ends immediately before `j`; the second
begins at `j` and ends at `k`.

Let $a$ be the bitwise XOR of `arr[i]` through `arr[j - 1]`, and let $b$ be
the bitwise XOR of `arr[j]` through `arr[k]`. Count all distinct triplets
$(i,j,k)$ for which $a=b$. Triplets with the same outer endpoints but different
split indices are counted separately.

### Function Contract
**Inputs**

- `arr`: a list of $n$ positive integers, where $1 \le n \le 300$ and
  $1 \le \texttt{arr[i]} \le 10^8$.

**Return value**

Return the number of index triplets $(i,j,k)$ satisfying the stated bounds and
equal-XOR condition.

### Examples
**Example 1**

- Input: `arr = [2, 3, 1, 6, 7]`
- Output: `4`
- Explanation: The valid triplets are `(0, 1, 2)`, `(0, 2, 2)`,
  `(2, 3, 4)`, and `(2, 4, 4)`.

**Example 2**

- Input: `arr = [1, 1, 1, 1, 1]`
- Output: `10`

**Example 3**

- Input: `arr = [2, 3]`
- Output: `0`
