# Arithmetic Slices

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 413 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Sliding Window |
| Official Link | [LeetCode](https://leetcode.com/problems/arithmetic-slices/) |

## Problem Description
### Goal
Given an integer array, an arithmetic slice is a contiguous subarray of at least three elements in which every adjacent pair has the same difference. The common difference may be positive, negative, or zero.

Return the total number of arithmetic slices. Different start or end positions count as different subarrays, so a long arithmetic run contains several shorter qualifying slices within it. Noncontiguous subsequences do not count, and arrays with fewer than three elements return `0`. The function returns only the count rather than the ranges or their common differences.

### Function Contract
**Inputs**

- `nums`: the integer array

**Return value**

- Return the number of contiguous arithmetic subarrays with at least three elements.

### Examples
**Example 1**

- Input: `nums = [1,2,3,4]`
- Output: `3`

**Example 2**

- Input: `nums = [1]`
- Output: `0`

**Example 3**

- Input: `nums = [1,3,5,7,9]`
- Output: `6`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Count valid slices ending at the current index**

Maintain `ending`, the number of arithmetic slices whose right endpoint is the previous index. When the newest adjacent difference equals the preceding one, the last three values form one new slice.

**Extend every prior ending slice**

Under the same equal-difference condition, appending the current value also extends each of the `ending` slices that ended one position earlier. Therefore update `ending += 1` and add that entire value to the global total.

**Reset when the difference changes**

If the two adjacent differences differ, no arithmetic slice ending at the current index can cross that break. Set `ending` to zero; a future equal pair of differences can begin a new run.

**Why every slice is counted once**

Every valid contiguous arithmetic slice has one unique right endpoint. At that endpoint, repeated extensions from its three-element base contribute it to `ending`. The algorithm adds all such endings exactly at their endpoint and resets across invalid boundaries, so it neither misses nor duplicates a slice.

#### Complexity detail

The scan performs constant work at each index from two onward, giving $O(n)$ time. The ending count and total use $O(1)$ space.

#### Alternatives and edge cases

- **Measure each maximal equal-difference run:** a run supporting `r` consecutive equal differences contributes $r(r - 1) / 2$ slices; this is another linear formulation.
- **Enumerate every start and end:** can verify differences incrementally but takes $O(n^2)$ time on long arithmetic runs.
- **Recheck every candidate subarray:** adds an inner validation scan and can take $O(n^3)$.
- Arrays shorter than three contain no slices.
- A constant-valued run is arithmetic with difference zero.
- Negative differences are handled identically.
- A difference change separates slices on its two sides.

</details>
