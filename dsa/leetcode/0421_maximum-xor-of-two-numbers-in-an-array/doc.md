# Maximum XOR of Two Numbers in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 421 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Bit Manipulation, Trie |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) |

## Problem Description
### Goal
Given an array of nonnegative integers, choose two available element positions and compute the bitwise XOR of their values. Seek the pair whose XOR has the greatest numerical value, prioritizing higher differing bit positions.

Return that maximum XOR value, not the chosen numbers or indices. Duplicate values at different positions are valid choices, and a one-element input has result `0` by pairing the sole value under the app contract. Meet the required near-linear fixed-bit-width complexity rather than comparing every pair, while accounting for all significant bits present in the input range.

### Function Contract
**Inputs**

- `nums`: an array of nonnegative integers

**Return value**

- Return the largest value of `nums[i] ^ nums[j]` over any two array positions; choosing the sole value twice yields zero for a one-element array.

### Examples
**Example 1**

- Input: `nums = [3, 10, 5, 25, 2, 8]`
- Output: `28`

**Example 2**

- Input: `nums = [0]`
- Output: `0`

**Example 3**

- Input: `nums = [2, 4]`
- Output: `6`
