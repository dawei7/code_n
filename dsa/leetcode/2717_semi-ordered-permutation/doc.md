# Semi-Ordered Permutation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2717 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/semi-ordered-permutation/) |

## Problem Description

### Goal

A 0-indexed array `nums` is a permutation of the integers from $1$ through $n$. It is called semi-ordered when its first element is $1$ and its last element is $n$; the values between those endpoints may appear in any order.

One operation swaps any pair of adjacent elements. Apply this operation as many times as needed and return the minimum number of swaps that makes the permutation semi-ordered. Moving $1$ and $n$ can interact when their original order is reversed, so the result is not always the sum of two independent endpoint distances.

### Function Contract

**Inputs**

- `nums`: A permutation of length $n$, where $2 \le n \le 50$, containing every integer from $1$ through $n$ exactly once.

**Return value**

Return the minimum number of adjacent swaps needed to place $1$ first and $n$ last.

### Examples

#### Example 1

- **Input:** `nums = [2,1,4,3]`
- **Output:** `2`
- **Explanation:** Swap $1$ left once and $4$ right once to obtain `[1,2,3,4]`.

#### Example 2

- **Input:** `nums = [2,4,1,3]`
- **Output:** `3`
- **Explanation:** Moving $1$ two places left crosses $4$ and helps move $4$ one place right; one more swap puts it last.

#### Example 3

- **Input:** `nums = [1,3,4,2,5]`
- **Output:** `0`
- **Explanation:** The permutation already starts with $1$ and ends with $5$.
