# Find the Maximum Achievable Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2769 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [2769. Find the Maximum Achievable Number](https://leetcode.com/problems/find-the-maximum-achievable-number/) |

## Problem Description

### Goal

Start with the given integer `num` and consider another integer $x$. In one operation, change $x$ by either $1$ or $-1$ and, at the same time, independently change `num` by either $1$ or $-1$. The two values need not move in the same direction.

A value of $x$ is achievable when some sequence of at most `t` such operations can make the resulting $x$ equal the resulting `num`. Determine the greatest initial value of $x$ for which this meeting is possible. Using fewer than `t` operations is allowed, but the requested result is the maximum over every permitted sequence.

### Function Contract

**Inputs**

- `num`: The initial value of the distinguished integer, with $1 \le \texttt{num} \le 50$.
- `t`: The maximum permitted number of simultaneous operations, with $1 \le t \le 50$.

**Return value**

Return the maximum achievable initial value of $x$.

### Examples

**Example 1**

- Input: `num = 4, t = 1`
- Output: `6`
- Explanation: Starting with $x=6$, decrease $x$ to $5$ while increasing `num` to $5$.

**Example 2**

- Input: `num = 3, t = 2`
- Output: `7`
- Explanation: Two operations decrease $x$ from $7$ to $5$ and increase `num` from $3$ to $5$.
