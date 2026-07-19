# Ugly Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 263 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/ugly-number/) |

## Problem Description
### Goal
An ugly number is a positive integer whose prime factors, if any, are limited to `2`, `3`, and `5`. Repeated factors are allowed, and `1` is included because it has no prime factors outside the permitted set.

Given an integer `n`, return `True` when it is ugly and `False` otherwise. Zero and negative integers are never ugly. A positive number fails as soon as any remaining prime factor other than `2`, `3`, or `5` is required, even when it also contains permitted factors; the task returns only the classification, not a factorization.

### Function Contract
**Inputs**

- `n`: an integer

**Return value**

`True` exactly when `n` is positive and all of its prime factors belong to `{2,3,5}`.

### Examples
**Example 1**

- Input: `n = 6`
- Output: `true`

**Example 2**

- Input: `n = 1`
- Output: `true`

**Example 3**

- Input: `n = 14`
- Output: `false`
