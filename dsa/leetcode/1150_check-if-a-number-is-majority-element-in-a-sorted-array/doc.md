# Check If a Number Is Majority Element in a Sorted Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1150 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/) |

## Problem Description

### Goal

Given an integer array `nums` sorted in non-decreasing order and an integer `target`, determine whether `target` is a majority element of the array. Because the input is sorted, every occurrence of a value occupies one contiguous interval.

A majority element is an element that appears more than half the array length. The comparison is strict: when `target` occurs exactly `nums.length / 2` times, it is not a majority. Return `true` only when the number of occurrences exceeds that threshold; otherwise return `false`.

### Function Contract

**Inputs**

- `nums`: an integer array of length $n$, where $1 \le n \le 1000$.
- `nums` is sorted in non-decreasing order.
- `target`: the value to test, with $1 \le \texttt{nums[i]}, \texttt{target} \le 10^9$.

**Return value**

`true` if `target` occurs more than $n/2$ times in `nums`; otherwise `false`.

### Examples

**Example 1**

- Input: `nums = [2,4,5,5,5,5,5,6,6], target = 5`
- Output: `true`
- Explanation: `5` occurs five times, and $5 > 9/2$.

**Example 2**

- Input: `nums = [10,100,101,101], target = 101`
- Output: `false`
- Explanation: Two occurrences equal half the array length but do not exceed it.
