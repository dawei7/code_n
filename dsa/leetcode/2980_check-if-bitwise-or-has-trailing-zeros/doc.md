# Check if Bitwise OR Has Trailing Zeros

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2980 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/) |

## Problem Description

### Goal

You are given an array `nums` of positive integers. Select at least two array
elements and compute their bitwise OR.

Return `true` if some valid selection has at least one trailing zero in its
binary representation. Return `false` if every selection of two or more
elements produces an odd result.

A trailing zero means that the least significant binary bit is zero. The
chosen elements come from distinct array positions, and the selection may
contain more than two values.

### Function Contract

**Inputs**

- `nums`: the positive integers available for selection

Let $N=\lvert\texttt{nums}\rvert$. The contract guarantees $2\le N\le100$
and $1\le\texttt{nums[i]}\le100$.

**Return value**

Whether at least two elements can be selected whose bitwise OR has a zero
least-significant bit.

### Examples

#### Example 1

- **Input:** `nums = [1,2,3,4,5]`
- **Output:** `true`
- **Explanation:** `2 | 4` equals `6`, whose binary representation ends in zero.

#### Example 2

- **Input:** `nums = [2,4,8,16]`
- **Output:** `true`
- **Explanation:** Any pair consists of even values and therefore has an even OR.

#### Example 3

- **Input:** `nums = [1,3,5,7,9]`
- **Output:** `false`
- **Explanation:** Every selected set contains only values whose least-significant bit is one.
