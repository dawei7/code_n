# The Two Sneaky Numbers of Digitville

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3289 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/) |

## Problem Description

### Goal

Digitville is meant to have a list containing every integer from $0$ through $n-1$ exactly once. Two distinct numbers have each appeared one additional time, so the resulting array `nums` has length $n+2$.

Find the two numbers that occur twice. Return them in an array of length two; either order is accepted. The input guarantee means every other value in the range appears exactly once, and there are no values outside that range.

### Function Contract

**Inputs**

- `nums`: A list of $n+2$ integers drawn from $0$ through $n-1$.

The constraints guarantee $2 \le n \le 100$ and exactly two distinct repeated elements.

**Return value**

- A list containing the two repeated numbers in any order.

### Examples

**Example 1**

- Input: `nums = [0,1,1,0]`
- Output: `[0,1]`
- Explanation: Both 0 and 1 occur twice.

**Example 2**

- Input: `nums = [0,3,2,1,3,2]`
- Output: `[2,3]`
- Explanation: Both 2 and 3 occur twice.

**Example 3**

- Input: `nums = [7,1,5,4,3,4,6,0,9,5,8,2]`
- Output: `[4,5]`
- Explanation: Both 4 and 5 occur twice.
