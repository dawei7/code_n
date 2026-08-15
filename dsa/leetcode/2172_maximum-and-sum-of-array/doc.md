# Maximum AND Sum of Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2172 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-and-sum-of-array/) |

## Problem Description

### Goal

Given an integer array `nums` and `numSlots` slots numbered from $1$ through
`numSlots`, assign every array element to a slot. Each slot may contain at most
two numbers, and the contract guarantees enough total capacity for all
elements. Slots are allowed to remain empty.

For one placement, each number contributes the result of its bitwise AND with
the number of its assigned slot. The placement's AND sum is the sum of all
those contributions. Return the largest AND sum achievable by any valid
placement.

### Function Contract

**Inputs**

- `nums`: an array of length $n$, where $1\le n\le 2m$ and every value is
  between $1$ and $15$, inclusive.
- `numSlots`: the slot count $m$, where $1\le m\le 9$.

Every element must be assigned exactly once, and each numbered slot accepts at
most two elements.

**Return value**

Return the maximum possible sum of `nums[i] & slot` over all elements and
valid slot assignments.

### Examples

#### Example 1

- **Input:** `nums = [1, 2, 3, 4, 5, 6], numSlots = 3`
- **Output:** `9`

One optimum puts `[1, 4]` in slot 1, `[2, 6]` in slot 2, and `[3, 5]` in slot
3, producing $1+0+2+2+3+1=9$.

#### Example 2

- **Input:** `nums = [1, 3, 10, 4, 7, 1], numSlots = 9`
- **Output:** `24`

The six values can use slots 1, 3, 4, 7, and 9 while the other slots remain
empty.

#### Example 3

- **Input:** `nums = [1], numSlots = 1`
- **Output:** `1`

The single number contributes `1 & 1`.
