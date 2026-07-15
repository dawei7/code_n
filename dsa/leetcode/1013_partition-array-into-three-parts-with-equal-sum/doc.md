# Partition Array Into Three Parts With Equal Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1013 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/) |

## Problem Description

### Goal

You are given an integer array `arr`. Determine whether it can be partitioned, without reordering any elements, into exactly three non-empty contiguous parts whose sums are equal.

Formally, return `true` when there are indices `i` and `j` with `i + 1 < j` such that the sum from index `0` through `i`, the sum from `i + 1` through `j - 1`, and the sum from `j` through the final index are all the same. Otherwise, return `false`.

### Function Contract

**Inputs**

- `arr`: an integer array of length $N$, where $3\le N\le5\cdot10^4$ and $-10^4\le\texttt{arr[i]}\le10^4$.

**Return value**

- `True` if three non-empty contiguous equal-sum parts exist; otherwise `False`.

### Examples

**Example 1**

- Input: `arr = [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]`
- Output: `True`
- Explanation: The three sums are `0 + 2 + 1`, `-6 + 6 - 7 + 9 + 1`, and `2 + 0 + 1`, each equal to `3`.

**Example 2**

- Input: `arr = [0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]`
- Output: `False`

**Example 3**

- Input: `arr = [3, 3, 6, 5, -2, 2, 5, 1, -9, 4]`
- Output: `True`
- Explanation: The three contiguous parts each sum to `6`.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Derive the only possible part sum:** Let the array total be `total`. Equal parts require `total % 3 == 0`; otherwise no partition exists. When divisible, every part must sum to `target = total // 3`.

**Close each part as soon as its target is reached:** Scan left to right, accumulating `current`. Whenever `current == target`, count one completed non-empty part and reset `current` to zero. Closing at the earliest possible boundary leaves the longest suffix available for the remaining parts and cannot remove a feasible later boundary.

**Require at least three completed parts:** Return true once the full scan yields three or more target-sum groups. This wording matters when `target == 0`: extra zero-sum groups can be merged into the third part, preserving exactly three non-empty parts with equal sums.

If a valid partition exists, the first valid prefix reaches `target`, and taking its earliest occurrence cannot prevent the remainder from being split because the skipped difference has sum zero. Repeating the argument for the second part establishes that the greedy scan finds at least three groups exactly when a valid three-part partition exists.

#### Complexity detail

Computing the total and scanning for target-sum groups each visit the $N$ elements once, giving $O(N)$ time. The total, target, running sum, and part counter use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Try every split pair:** Prefix sums make each part sum constant-time to query, but checking all boundary pairs still costs $O(N^2)$ time and $O(N)$ space.
- **Backtracking partitions:** Exploring boundary choices is unnecessary and may become exponential without memoization.
- **Total not divisible by three:** Return false immediately.
- **Zero target:** More than three zero-sum groups are acceptable because adjacent groups can be merged.
- **Negative values:** Running sums need not be monotone, but equality with the fixed target remains valid.

</details>
