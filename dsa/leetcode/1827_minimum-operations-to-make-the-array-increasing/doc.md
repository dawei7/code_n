# Minimum Operations to Make the Array Increasing

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/) |
| Frontend ID | 1827 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

An operation selects one element of the 0-indexed integer array `nums` and increases that element by exactly 1. Operations may be applied repeatedly to the same position, but values can never be decreased.

Make the array strictly increasing, meaning every element is smaller than the element immediately after it. Return the minimum total number of increment operations. A one-element array already satisfies the condition.

### Function Contract

**Inputs**

- `nums`: an array of $n$ positive integers, where $1 \le n \le 5000$.
- Each original value satisfies $1 \le \texttt{nums[i]} \le 10^4$.

**Return value**

- Return the fewest unit increments required to make every adjacent relation strictly increasing.

### Examples

**Example 1**

- Input: `nums = [1,1,1]`
- Output: `3`

The least possible adjusted array is `[1,2,3]`, requiring zero, one, and two increments.

**Example 2**

- Input: `nums = [1,5,2,4,1]`
- Output: `14`

**Example 3**

- Input: `nums = [8]`
- Output: `0`
