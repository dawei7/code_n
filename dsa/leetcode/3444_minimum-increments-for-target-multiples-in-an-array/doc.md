# Minimum Increments for Target Multiples in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3444 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Bit Manipulation, Number Theory, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-increments-for-target-multiples-in-an-array/) |

## Problem Description

### Goal

Given arrays `nums` and `target`, one operation increments a chosen element of `nums` by one. Apply as few operations as possible so that every value in `target` divides at least one resulting value in `nums`.

The same element of `nums` may satisfy several target values when it becomes a common multiple of them. Elements may be incremented repeatedly, and elements that are not useful do not need to change.

### Function Contract

**Inputs**

- `nums`: Between $1$ and $5\cdot10^4$ positive integers.
- `target`: Between $1$ and $4$ positive target values, with no more entries than `nums`.

Every input value is between $1$ and $10^4$, inclusive.

**Return value**

Return the minimum total number of unit increments needed so every target has at least one multiple in the resulting `nums` array.

### Examples

**Example 1**

- Input: `nums = [1,2,3], target = [4]`
- Output: `1`

Incrementing `3` once produces the required multiple `4`.

**Example 2**

- Input: `nums = [8,4], target = [10,5]`
- Output: `2`

Incrementing `8` to `10` makes one number divisible by both targets.

**Example 3**

- Input: `nums = [7,9,10], target = [7]`
- Output: `0`

The existing value `7` already satisfies the target.
