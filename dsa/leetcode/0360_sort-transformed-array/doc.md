# Sort Transformed Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 360 |
| Difficulty | Medium |
| Topics | Array, Math, Two Pointers, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/sort-transformed-array/) |

## Problem Description
### Goal
Given an integer array `nums` sorted in ascending order and coefficients $a$, $b$, and $c$, transform every occurrence $x$ with the quadratic function $f(x)=ax^2+bx+c$. Preserve duplicate occurrences even when several inputs produce the same output.

Return all transformed values in ascending order. Use the input order and the parabola's direction to construct the result in linear time rather than transforming and comparison-sorting from scratch. Handle positive, zero, and negative `a`, including the linear-function case. The function returns values only and does not modify their multiplicities or omit points around the quadratic vertex.

### Function Contract
**Inputs**

- `nums`: a nondecreasing list of integers
- `a`: the quadratic coefficient
- `b`: the linear coefficient
- `c`: the constant coefficient

**Return value**

- A nondecreasing list containing `f(x)` for every `x` in `nums`, with multiplicities preserved.

### Examples
**Example 1**

- Input: `nums = [-4,-2,2,4], a = 1, b = 3, c = 5`
- Output: `[3,9,15,33]`

**Example 2**

- Input: `nums = [-4,-2,2,4], a = -1, b = 3, c = 5`
- Output: `[-23,-5,1,7]`

**Example 3**

- Input: `nums = [-4,-2,2,4], a = 0, b = -3, c = 5`
- Output: `[-7,-1,11,17]`
