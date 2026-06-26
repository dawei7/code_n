# Decode XORed Permutation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1734 |
| Difficulty | Medium |
| Topics | Array, Bit Manipulation |
| Official Link | [decode-xored-permutation](https://leetcode.com/problems/decode-xored-permutation/) |

## Problem Description & Examples
### Goal
An encoded array was created from a permutation of `1..n` by XORing adjacent elements. Recover the original permutation, where `n` is odd.

### Function Contract
**Inputs**

- `encoded`: a list where `encoded[i] = perm[i] XOR perm[i + 1]`.

**Return value**

Return the original permutation.

### Examples
**Example 1**

- Input: `encoded = [3,1]`
- Output: `[1,2,3]`

**Example 2**

- Input: `encoded = [6,5,4,6]`
- Output: `[2,4,1,5,3]`

**Example 3**

- Input: `encoded = [4,3,1,7]`
- Output: `[5,1,2,3,4]`

---

## Underlying Base Algorithm(s)
XOR all numbers from `1` to `n` to get the XOR of the full permutation. XOR encoded values at odd indices to get `perm[1] XOR perm[2] ... XOR perm[n - 1]`. Combining those gives `perm[0]`. Then decode forward using `perm[i + 1] = perm[i] XOR encoded[i]`.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)` besides the output array
