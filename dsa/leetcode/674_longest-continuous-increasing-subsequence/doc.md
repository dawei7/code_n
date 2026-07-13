# Longest Continuous Increasing Subsequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 674 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-continuous-increasing-subsequence/) |

## Problem Description
### Goal
Given an unsorted integer array `nums`, find its longest continuous increasing subsequence, meaning a subarray whose elements occupy adjacent indices. Within that subarray, every value must be strictly greater than the value immediately before it.

Return the length of the longest such continuous subsequence. A longer increasing subsequence formed by skipping intervening elements does not qualify, and equal neighboring values break the current run because the comparison is strict. Every single element is itself a valid run of length `1`.

### Function Contract
**Inputs**

- `nums`: a nonempty list of integers

**Return value**

- The length of the longest contiguous strictly increasing segment

### Examples
**Example 1**

- Input: `nums = [1,3,5,4,7]`
- Output: `3`

**Example 2**

- Input: `nums = [2,2,2,2,2]`
- Output: `1`

**Example 3**

- Input: `nums = [1,3,5,7]`
- Output: `4`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**A run is determined by adjacent comparisons**

Because the requested sequence must be continuous, every element after the first can do only one of two things: extend the current run when it is strictly larger than its predecessor, or begin a new length-one run otherwise. No earlier nonadjacent value can help after a break.

**Track the current and best run lengths**

Initialize both lengths to one for the nonempty input. Scan from left to right, incrementing the current length after an increasing adjacent pair and resetting it to one after an equality or decrease. Update the maximum with each current length.

**Why a reset cannot discard an answer**

When `nums[i] <= nums[i - 1]`, no strictly increasing contiguous segment can include both positions, so every increasing segment ending at `i` must start at `i). When the comparison is increasing, appending `nums[i]` to the longest valid segment ending at `i - 1` gives the longest one ending at `i`. Thus the maintained current length is exact at every index, and its maximum is the global answer.

#### Complexity detail

The scan performs one comparison for each adjacent pair, taking $O(N)$ time. It stores only the current run length and the best length, using $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Track the current run's start index:** compute each length as `i - start + 1`; this is another $O(N)$ formulation with the same constant space.
- **Expand from every starting index:** follows the definition directly but can rescan an increasing suffix from many starts and take $O(N^2)$ time.
- **Longest increasing subsequence dynamic programming:** allows skipping elements and solves a different problem; continuity makes it unnecessary and incorrect here.
- Equal adjacent values break a run because the increase must be strict.
- A decreasing or constant nonempty array has answer one.
- Negative values need no special handling because only their ordering matters.

</details>
