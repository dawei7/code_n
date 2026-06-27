# Smallest Substring With Identical Characters I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3398 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Enumeration |
| Official Link | [smallest-substring-with-identical-characters-i](https://leetcode.com/problems/smallest-substring-with-identical-characters-i/) |

## Problem Description & Examples
### Goal
Given a binary string `s` and an integer `numOps`, determine the minimum possible value of the maximum length of any contiguous substring consisting of identical characters, after performing at most `numOps` operations. An operation consists of flipping a character (changing '0' to '1' or vice versa).

### Function Contract
**Inputs**

- `s` (str): A binary string consisting of '0's and '1's.
- `numOps` (int): The maximum number of character flips allowed.

**Return value**

- `int`: The smallest possible value for the maximum length of any contiguous block of identical characters.

### Examples
**Example 1**

- Input: `s = "0001111", numOps = 1`
- Output: `3`

**Example 2**

- Input: `s = "0101", numOps = 0`
- Output: `1`

**Example 3**

- Input: `s = "00000", numOps = 2`
- Output: `2`

---

## Underlying Base Algorithm(s)
The problem exhibits a monotonic property: if it is possible to achieve a maximum identical substring length of `k`, it is also possible for any length greater than `k`. This allows us to use **Binary Search on the Answer**. For a fixed length `mid`, we calculate the minimum number of operations required to ensure no contiguous block exceeds length `mid`. This is done by identifying all contiguous blocks of identical characters and calculating how many flips are needed to break them into segments of size at most `mid`.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`, where `n` is the length of the string. The binary search runs in `O(log n)` iterations, and each check takes `O(n)` time to traverse the string.
- **Space Complexity**: `O(n)` to store the lengths of contiguous blocks, though this can be optimized to `O(1)` by processing the string on the fly.
