# Maximum Ascending Subarray Sum

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/maximum-ascending-subarray-sum/) |
| Frontend ID | 1800 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

An ascending subarray is a contiguous, nonempty part of an integer array in which every value after the first is strictly greater than the value immediately before it. Equal adjacent values therefore end an ascending subarray; elements cannot be skipped to preserve the relation.

Given the positive integer array `nums`, consider every ascending subarray and calculate the sum of its elements. Return the largest such sum. A single element is itself a valid ascending subarray.

### Function Contract

**Inputs**

- `nums`: a list of $n$ positive integers, where $1 \le n \le 100$ and $1 \le \texttt{nums[i]} \le 100$.

**Return value**

- Return the maximum element sum among all contiguous strictly ascending subarrays of `nums`.

### Examples

**Example 1**

- Input: `nums = [10,20,30,5,10,50]`
- Output: `65`

The final ascending run `[5,10,50]` has the greatest sum.

**Example 2**

- Input: `nums = [10,20,30,40,50]`
- Output: `150`

The entire array is strictly ascending.

**Example 3**

- Input: `nums = [12,17,15,13,10,11,12]`
- Output: `33`

The best run is `[10,11,12]`.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Partition the array at every failed comparison**

Whenever `nums[i] <= nums[i - 1]`, no strictly ascending subarray can cross that boundary. The array is therefore partitioned into maximal ascending runs, and every valid ascending subarray lies entirely inside one of them.

**Keep only the current run sum**

Scan from left to right. If the current value is greater than the previous value, add it to the current run sum. Otherwise begin a new run whose sum is the current value. Track the largest run sum seen.

All values are positive, so within one maximal ascending run its complete sum is at least the sum of any shorter subarray inside it. Consequently, comparing the sums of maximal runs is sufficient. The scan constructs exactly those sums, which proves the reported maximum is correct.

#### Complexity detail

The scan visits each of the $n$ values once, taking $O(n)$ time. It retains only the current sum and the best sum, so it uses $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Enumerate every starting position:** Extending each possible ascending subarray is correct but can take $O(n^2)$ time on a fully ascending array.
- **Prefix sums plus boundary search:** Prefix sums can evaluate a known run, but finding and storing all boundaries adds machinery without improving the linear bound.
- **Single element:** Its value is the only valid subarray sum.
- **Equal adjacent values:** Equality breaks the run because ascending means strictly greater, not non-decreasing.
- **Fully descending array:** Every maximal run has length one, so the answer is the largest element.
- **Best run at either edge:** Update the maximum throughout the scan so no special finalization case is needed.

</details>
