# Tuple with Same Product

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1726 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Counting |
| Official Link | [tuple-with-same-product](https://leetcode.com/problems/tuple-with-same-product/) |

## Problem Description & Examples
### Goal
Count ordered tuples `(a, b, c, d)` made from four distinct elements of `nums` such that `a * b == c * d`.

### Function Contract
**Inputs**

- `nums`: a list of distinct positive integers.

**Return value**

Return the number of valid ordered tuples.

### Examples
**Example 1**

- Input: `nums = [2,3,4,6]`
- Output: `8`

**Example 2**

- Input: `nums = [1,2,4,5,10]`
- Output: `16`

**Example 3**

- Input: `nums = [2,3,5,7]`
- Output: `0`

---

## Underlying Base Algorithm(s)
Compute every unordered pair product and count how many pairs produce each product. When a product has `c` pairs, choose any two pairs in `c * (c - 1) / 2` ways; each pair-pair choice creates `8` ordered tuples by swapping elements inside pairs and swapping the two pairs.

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n^2)`
