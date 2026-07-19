# Valid Perfect Square

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 367 |
| Difficulty | Easy |
| Topics | Math, Binary Search |
| Official Link | [LeetCode](https://leetcode.com/problems/valid-perfect-square/) |

## Problem Description
### Goal
Given a positive integer `num`, determine whether some integer `r` satisfies `r * r = num`. Such values are perfect squares, including `1`, while values strictly between consecutive integer squares are not.

Return `True` only for an exact square and `False` otherwise. Do not use a built-in square-root function or a floating-point approximation whose rounding could misclassify large inputs. The task asks only for the boolean result, not for `r`; use integer arithmetic that avoids overflow or controls it when comparing candidate squares.

### Function Contract
**Inputs**

- `num`: a positive integer

**Return value**

- `True` exactly when there is an integer `r` such that `r * r = num`; otherwise `False`.

### Examples
**Example 1**

- Input: `num = 16`
- Output: `True`

**Example 2**

- Input: `num = 14`
- Output: `False`

**Example 3**

- Input: `num = 1`
- Output: `True`
