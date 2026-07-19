# Find XOR Sum of All Pairs Bitwise AND

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/) |
| Frontend ID | 1835 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

The XOR sum of a nonempty list is the bitwise XOR of all its elements. You are given two 0-indexed arrays `arr1` and `arr2` containing non-negative integers.

Form one value `arr1[i] & arr2[j]` for every pair of valid indices, using bitwise AND. Return the XOR sum of that complete Cartesian-product list. Repeated values and repeated pair results are included separately.

### Function Contract

**Inputs**

- `arr1`: an array of $p$ integers, where $1 \le p \le 10^5$ and $0 \le \texttt{arr1[i]} \le 10^9$.
- `arr2`: an array of $q$ integers, where $1 \le q \le 10^5$ and $0 \le \texttt{arr2[j]} \le 10^9$.

**Return value**

- Return the XOR of all $pq$ values `arr1[i] & arr2[j]`.

### Examples

**Example 1**

- Input: `arr1 = [1,2,3], arr2 = [6,5]`
- Output: `0`

The pair results are `[0,1,2,0,2,1]`, whose equal nonzero values cancel under XOR.

**Example 2**

- Input: `arr1 = [12], arr2 = [4]`
- Output: `4`

There is only one pair, and `12 & 4 = 4`.

**Example 3**

- Input: `arr1 = [5,1], arr2 = [3,7]`
- Output: `4`
