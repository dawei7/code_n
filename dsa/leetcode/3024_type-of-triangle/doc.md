# Type of Triangle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3024 |
| Difficulty | Easy |
| Topics | Array, Math, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/type-of-triangle/) |

## Problem Description
### Goal
You are given a 0-indexed integer array `nums` containing exactly three positive side lengths. A valid triangle must satisfy the strict triangle inequality: the sum of every pair of side lengths is greater than the remaining length. Equality produces a degenerate shape and therefore does not count as a triangle.

If the three lengths form a triangle, classify it by its equal sides. An **equilateral** triangle has three equal lengths, an **isosceles** triangle has exactly two equal lengths, and a **scalene** triangle has three different lengths. Return the corresponding lowercase name, or return `"none"` when no triangle can be formed.

### Function Contract
**Inputs**

- `nums`: A list of exactly three integers, each between $1$ and $100$ inclusive.

**Return value**

One of `"equilateral"`, `"isosceles"`, `"scalene"`, or `"none"`, according to the validity and side-length classification.

### Examples
**Example 1**

- Input: `nums = [3, 3, 3]`
- Output: `"equilateral"`

All three equal positive lengths form an equilateral triangle.

**Example 2**

- Input: `nums = [3, 4, 5]`
- Output: `"scalene"`

Every pair has a sum greater than the third length, and all three lengths differ.
