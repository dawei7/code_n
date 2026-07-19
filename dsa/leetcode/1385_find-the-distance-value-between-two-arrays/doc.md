# Find the Distance Value Between Two Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1385 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Two Pointers, Binary Search, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/find-the-distance-value-between-two-arrays/) |

## Problem Description

### Goal

Given two integer arrays, `arr1` and `arr2`, and a nonnegative integer `d`, define an element `arr1[i]` as qualifying when its absolute difference from every element of `arr2` is strictly greater than `d`.

Count and return the number of qualifying elements in `arr1`. Each occurrence in `arr1` is counted separately, even when values repeat, and a pair whose absolute difference is exactly `d` prevents that occurrence from qualifying.

### Function Contract

**Inputs**

- `arr1`: an integer array of length $n$.
- `arr2`: a nonempty integer array of length $m$.
- `d`: the inclusive disqualifying distance threshold.

**Return value**

- The number of occurrences $x$ in `arr1` for which $lvert x-y\rvert > d$ for every $y$ in `arr2`.

### Examples

**Example 1**

- Input: `arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2`
- Output: `2`

**Example 2**

- Input: `arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3`
- Output: `2`

**Example 3**

- Input: `arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6`
- Output: `1`
