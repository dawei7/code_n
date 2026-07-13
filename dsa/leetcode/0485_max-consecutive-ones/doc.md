# Max Consecutive Ones

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 485 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [LeetCode](https://leetcode.com/problems/max-consecutive-ones/) |

## Problem Description
### Goal
Given a nonempty binary array `nums`, examine its maximal contiguous runs of `1` values. A run ends whenever a `0` occurs or the array boundary is reached, and separated runs cannot be joined by skipping the zeroes between them.

Return the maximum number of consecutive `1` values in any run. An array containing only zeroes returns `0`, while an all-one array returns its complete length. The result is a length rather than the run's starting index or values, and each position is considered in its original order.

### Function Contract
**Inputs**

- `nums`: a nonempty array whose elements are either `0` or `1`

**Return value**

- The number of elements in the longest consecutive block of ones

### Examples
**Example 1**

- Input: `nums = [1, 1, 0, 1, 1, 1]`
- Output: `3`

**Example 2**

- Input: `nums = [1, 0, 1, 1, 0, 1]`
- Output: `2`

**Example 3**

- Input: `nums = [0, 0, 0]`
- Output: `0`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Track only the run that reaches the current position**

Maintain `current`, the number of consecutive ones ending at the element being processed. Reading a `1` extends that run by one. Reading a `0` proves that no run can cross this position, so reset `current` to zero.

**Preserve the best completed or active run**

After each extension, update `best` with the larger of its old value and `current`. A run is therefore recorded before a later zero resets it, and a run that reaches the end is recorded without special cleanup.

**Why one pass is sufficient**

Every contiguous run has a unique ending position. At that position, `current` equals the run's full length because it has counted every preceding adjacent one since the last zero. Taking the maximum over those ending lengths considers every possible run, so `best` is exactly the requested maximum.

#### Complexity detail

The scan visits each of the `n` elements once, giving $O(n)$ time. The two counters use $O(1)$ extra space.

#### Alternatives and edge cases

- **Group equal values:** form runs with a grouping utility and take the largest group whose key is one; this is linear but introduces iterator machinery.
- **Rescan from every one:** counting the suffix run starting at each index is correct but repeats work and takes $O(n^2)$ time on an all-one array.
- **All zeros:** no run is extended, so the answer remains zero.
- **All ones:** the active run grows to the full array length.
- **Single element:** returns that element's value as either zero or one.
- **Multiple equal maxima:** only the maximum length matters, not which run occurs first.

</details>
