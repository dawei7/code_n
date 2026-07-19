# Maximize Score After N Operations

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/maximize-score-after-n-operations/) |
| Frontend ID | 1799 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Backtracking, Bit Manipulation, Number Theory, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

An even-length integer array `nums` contains $2n$ positive values. You perform exactly $n$ operations, numbered from $1$ through $n$. During operation $i$, choose any two elements that have not previously been chosen.

The operation adds $i \cdot \gcd(x,y)$ to the score, where $x$ and $y$ are the selected values, and both selected array positions then become unavailable. Choose both the pairing and the order in which pairs are taken to maximize the final score.

### Function Contract

**Inputs**

- `nums`: a list of $m=2n$ positive integers, where $1 \le n \le 7$ and $1 \le \texttt{nums[i]} \le 10^6$.
- Equal values at different indices are separate selectable elements.

**Return value**

- Return the maximum score after all $n$ operations have selected every array position exactly once.

### Examples

**Example 1**

- Input: `nums = [1,2]`
- Output: `1`

The only operation contributes $1 \cdot \gcd(1,2)=1$.

**Example 2**

- Input: `nums = [3,4,6,8]`
- Output: `11`

Choosing `3` with `6` first and `4` with `8` second scores $3+2\cdot4=11$.

**Example 3**

- Input: `nums = [1,2,3,4,5,6]`
- Output: `14`

An optimal ordering places a pair with a larger GCD under a later multiplier.
