# Divide Array Into Equal Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2206 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Bit Manipulation, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/divide-array-into-equal-pairs/) |

## Problem Description

### Goal

An integer array `nums` contains exactly $2n$ elements. Divide all of its element occurrences into exactly $n$ pairs, with every occurrence used in one and only one pair.

A pair is valid only when its two elements have equal values. Determine whether a complete division satisfying both conditions exists. The positions of equal values do not need to be adjacent, and rearranging the occurrences conceptually does not change the answer.

### Function Contract

**Inputs**

- `nums`: an integer array of length $m=2n$, where $1 \le n \le 500$ and every value is between $1$ and $500$.

**Return value**

Return `true` when all occurrences can be divided into equal-value pairs; otherwise return `false`.

### Examples

**Example 1**

- Input: `nums = [3, 2, 3, 2, 2, 2]`
- Output: `true`
- Explanation: the occurrences can form `(3, 3)`, `(2, 2)`, and `(2, 2)`.

**Example 2**

- Input: `nums = [1, 2, 3, 4]`
- Output: `false`
- Explanation: each value occurs only once, so no equal pair can be formed.

**Example 3**

- Input: `nums = [7, 7]`
- Output: `true`
- Explanation: the two occurrences form the single required pair.
