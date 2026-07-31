# Find the Maximum Factor Score of Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3334 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-maximum-factor-score-of-array/) |

## Problem Description

### Goal

For a nonempty integer array, define its factor score as the greatest common divisor of all its elements multiplied by their least common multiple. The GCD and LCM of a one-element array are both that single value, so such an array has the square of its element as its score.

Given `nums`, you may keep the array unchanged or remove exactly one element. Removing the only element produces an empty array, whose factor score is defined to be $0$. Return the largest factor score among every permitted choice.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers, where $1 \le n \le 100$ and each value is between $1$ and $30$.

**Return value**

- The maximum product of the remaining array's GCD and LCM after removing at most one element.

### Examples

**Example 1**

- Input: `nums = [2, 4, 8, 16]`
- Output: `64`
- Explanation: Removing $2$ leaves GCD $4$ and LCM $16$, whose product is $64$.

**Example 2**

- Input: `nums = [1, 2, 3, 4, 5]`
- Output: `60`
- Explanation: Keeping every element gives GCD $1$ and LCM $60$.

**Example 3**

- Input: `nums = [3]`
- Output: `9`
- Explanation: Keeping the element gives $3\cdot3=9$, whereas removing it gives $0$.
