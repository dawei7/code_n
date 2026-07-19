# Power of Three

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 326 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/power-of-three/) |

## Problem Description
### Goal
Given a signed 32-bit integer `n`, determine whether it can be written exactly as $3^{x}$ for some integer exponent $x \ge 0$. The valid sequence begins with $1 = 3^{0}$, followed by `3`, `9`, `27`, and so on.

Return `True` only for positive exact powers of three. Return `False` for zero, negative integers, and positive numbers containing any factor or remainder outside repeated multiplication by three. The task asks for a boolean classification rather than the exponent. Satisfy the follow-up without using loops or recursion where the platform constraint requests the constant-time divisibility observation.

### Function Contract
**Inputs**

- `n`: the integer to classify

**Return value**

`True` when $n = 3^{x}$ for some integer $x \ge 0$; otherwise `False`.

### Examples
**Example 1**

- Input: `n = 27`
- Output: `True`

**Example 2**

- Input: `n = 0`
- Output: `False`

**Example 3**

- Input: `n = -1`
- Output: `False`
