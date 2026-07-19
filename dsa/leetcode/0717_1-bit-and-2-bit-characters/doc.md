# 1-bit and 2-bit Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 717 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [LeetCode](https://leetcode.com/problems/1-bit-and-2-bit-characters/) |

## Problem Description
### Goal
An encoding contains two character types: a one-bit character represented by `0`, and a two-bit character represented by either `10` or `11`. You are given a valid binary array `bits` whose final bit is `0`.

Return `True` if that final array element must be decoded as a standalone one-bit character, and `False` if it is the second bit of the last two-bit character. Decode from the beginning according to the character prefixes; individual bits cannot be regrouped out of order.

### Function Contract
**Inputs**

- `bits`: a valid nonempty binary encoding whose final element is `0`

**Return value**

- `true` when the final array element starts a one-bit character; otherwise `false` because it is the second bit of a two-bit character

### Examples
**Example 1**

- Input: `bits = [1,0,0]`
- Output: `true`

**Example 2**

- Input: `bits = [1,1,1,0]`
- Output: `false`

**Example 3**

- Input: `bits = [0]`
- Output: `true`
