# Power of Two

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 231 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Bit Manipulation, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/power-of-two/) |

## Problem Description
### Goal
Given a signed integer `n`, determine whether it can be written exactly as $2^{x}$ for some integer exponent $x \ge 0$. Valid values begin with $1 = 2^{0}$ and continue by repeated doubling.

Return `True` only for positive integers whose binary representation contains one set bit and no remainder beyond a power of two. Return `False` for zero, every negative integer, and positive values lying between consecutive powers. The task is a classification rather than a request for the exponent, and the input itself must not be approximated or rounded to a nearby power.

### Function Contract
**Inputs**

- `n`: a signed integer

**Return value**

`True` exactly when there is an integer $x \ge 0$ such that $n = 2^{x}$; otherwise `False`.

### Examples
**Example 1**

- Input: `n = 1`
- Output: `True`

**Example 2**

- Input: `n = 16`
- Output: `True`

**Example 3**

- Input: `n = 3`
- Output: `False`
