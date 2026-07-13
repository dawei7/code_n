# Longest Harmonious Subsequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 594 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Sliding Window, Sorting, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-harmonious-subsequence/) |

## Problem Description
### Goal
A harmonious array is one whose maximum value and minimum value differ by exactly `1`. Given an integer array `nums`, consider all subsequences obtainable by deleting zero or more elements while preserving the relative order of those that remain.

Return the length of the longest harmonious subsequence. A valid result must contain values at both ends of the one-value difference; a subsequence containing only repeated copies of one number has difference `0` and is not harmonious. If no pair of values differing by exactly `1` occurs, return `0`.

### Function Contract
**Inputs**

- `nums: list[int]`: the source values

**Return value**

- The length of the longest subsequence containing exactly two values that differ by one
- Return `0` when no such pair of values occurs

### Examples
**Example 1**

- Input: `nums = [1,3,2,2,5,2,3,7]`
- Output: `5`

**Example 2**

- Input: `nums = [1,2,3,4]`
- Output: `2`

**Example 3**

- Input: `nums = [1,1,1,1]`
- Output: `0`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**A harmonious subsequence uses one adjacent-value pair**

If a subsequence has minimum `x` and maximum $x + 1$, every selected value must be either `x` or $x + 1$. No other value can appear without changing one of the extrema.

**Take every occurrence of both values**

Once an adjacent pair exists, including another occurrence of either member never changes the difference between maximum and minimum. Therefore the longest subsequence for that pair has length `count[x] + count[x + 1]`.

**Evaluate pairs through a frequency map**

Count all array values once. For each distinct `x`, check whether $x + 1$ exists; if so, update the maximum with the two frequencies. Pairs are considered once from their smaller value.

**Why the maximum is optimal**

Every valid subsequence corresponds to some adjacent pair and cannot contain more elements than the total occurrences of those two values. The algorithm evaluates that exact attainable total for every possible pair, so its largest candidate equals the global optimum. Requiring both keys prevents an all-equal collection from being mistaken for harmonious.

#### Complexity detail

Building the frequency map and scanning its at most `n` keys take $O(n)$ expected time. The map stores at most `n` distinct values, so extra space is $O(n)$.

#### Alternatives and edge cases

- **Sort and use a sliding window:** maintains a range of at most one in $O(n \log n)$ time; the window must contain both endpoint values.
- **Repeated list membership and counts:** is correct but can rescan the full input for many candidates and take $O(n^2)$ time.
- **Enumerate subsequences:** is exponential and unnecessary because only frequencies matter.
- **All values equal:** returns zero because maximum minus minimum would be zero.
- **One element:** cannot form the required two-value range.
- **Negative values:** adjacent keys are handled identically.
- **Several adjacent pairs:** compare their combined frequencies.
- **Input order:** does not matter because subsequences may omit elements without reordering selected occurrences.

</details>
