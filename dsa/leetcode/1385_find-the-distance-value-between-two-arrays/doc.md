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

### Required Complexity

- **Time:** $O(m log m + n log m)$
- **Space:** $O(m)$

<details>
<summary>Approach</summary>

#### General

**Sort the comparison array.** Create a sorted copy of `arr2`. For each value `x` from `arr1`, use binary search to find the first sorted value that is not smaller than `x`.

Only the insertion position and its immediate predecessor can be closest to `x`: every value farther right is at least as large as the insertion candidate, and every value farther left is no larger than the predecessor. Check each existing neighbor. If either absolute difference is at most `d`, `x` is disqualified; otherwise count it.

This nearest-neighbor argument covers every element of `arr2`, so a counted occurrence satisfies the universal distance condition and every disqualified occurrence has a concrete comparison value within the forbidden threshold.

#### Complexity detail

Sorting the $m$ comparison values takes $O(m \log m)$ time. The $n$ binary searches take $O(n \log m)$ time. The sorted copy uses $O(m)$ space.

#### Alternatives and edge cases

- **Compare every pair:** Test each `arr1` occurrence against all of `arr2`. It is direct and correct but takes $O(nm)$ time.
- **Two sorted arrays:** Sort both arrays and sweep nearest neighbors with two pointers in $O(n \log n + m \log m)$ time.
- **Exact threshold:** A difference equal to `d` disqualifies the value because qualifying differences must be strictly greater.
- **Zero threshold:** Only equal values are too close when `d = 0`.
- **Repeated values:** Count occurrences from `arr1`, not distinct values.
- **Insertion at an end:** Check only the one neighbor that exists.
- **Negative integers:** Absolute difference and sorted order handle them without special cases.

</details>
