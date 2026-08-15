# Make Array Elements Equal to Zero

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3354 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Simulation, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/make-array-elements-equal-to-zero/) |

## Problem Description

### Goal

You are given a nonnegative integer array `nums` containing at least one zero. Choose a starting index `curr` whose value is zero and choose an initial direction, either left or right. While `curr` remains inside the array, a zero lets the pointer take one step in its current direction.

When the pointer instead reaches a positive value, decrement that value by one, reverse the direction, and take one step in the new direction. The process stops as soon as the pointer leaves the array. A selection consists of both its starting zero and its initial direction; it is valid only when every array element is zero at termination. Return the number of valid selections.

### Function Contract

**Inputs**

- `nums`: The nonnegative integer array on which the movement process operates.

Let $n=\lvert\texttt{nums}\rvert$. The source guarantees $1 \le n \le 100$, $0 \le \texttt{nums[i]} \le 100$, and at least one element equals zero.

**Return value**

- Return the number of valid `(starting index, initial direction)` selections.

### Examples

#### Example 1

- **Input:** `nums = [1, 0, 2, 0, 3]`
- **Output:** `2`
- **Explanation:** Starting at index $3$ succeeds in either initial direction; every other selection leaves a positive value behind.

#### Example 2

- **Input:** `nums = [2, 3, 4, 0, 4, 1, 0]`
- **Output:** `0`
- **Explanation:** No starting zero and direction can decrement every value before the pointer exits.
