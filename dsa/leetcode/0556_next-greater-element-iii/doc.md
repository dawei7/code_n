# Next Greater Element III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 556 |
| Difficulty | Medium |
| Topics | Math, Two Pointers, String |
| Official Link | [LeetCode](https://leetcode.com/problems/next-greater-element-iii/) |

## Problem Description
### Goal
Given a positive integer `n` that fits in signed 32-bit range, rearrange exactly its existing decimal digit occurrences without adding or deleting any digit. Among the rearrangements strictly greater than `n`, find the smallest numerical value.

Return that next greater value when it exists and still fits in a signed 32-bit integer; otherwise return `-1`. Repeated digits remain separate occurrences, leading zeroes cannot create a valid shorter representation, and a merely larger permutation is insufficient when another valid permutation lies numerically closer to the original.

### Function Contract
**Inputs**

- `n`: a positive signed 32-bit integer

**Return value**

- The next greater integer using exactly the same digits, or `-1`

### Examples
**Example 1**

- Input: `n = 12`
- Output: `21`

**Example 2**

- Input: `n = 21`
- Output: `-1`

**Example 3**

- Input: `n = 230241`
- Output: `230412`
