# Find All Numbers Disappeared in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 448 |
| Difficulty | Easy |
| Topics | Array, Hash Table |
| Official Link | [LeetCode](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) |

## Problem Description
### Goal
Given an integer array `nums` of length `n`, every entry lies in the inclusive range `1..n`, but some values may occur more than once. Determine which values from that complete range have no occurrence in the array.

Return all missing values. Duplicate input occurrences do not create extra output and may correspond to several absent values elsewhere. Meet the required linear time and constant auxiliary space beyond the returned list; modifying the input array to mark observed values is permitted. An array containing every range value once returns an empty list.

### Function Contract
**Inputs**

- `nums`: an integer array of length `n` whose values all lie in `[1, n]`

**Return value**

- Return all missing values from `[1, n]`, in increasing order. The input array may be modified.

### Examples
**Example 1**

- Input: `nums = [4, 3, 2, 7, 8, 2, 3, 1]`
- Output: `[5, 6]`

**Example 2**

- Input: `nums = [1, 1]`
- Output: `[2]`

**Example 3**

- Input: `nums = [1]`
- Output: `[]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Map each possible value to one marker position**

Value `v` corresponds to array index $v - 1$ because all values lie in `[1, n]`. Reuse the sign at that index to record whether `v` appears, avoiding a separate presence table.

**Mark every encountered value negative**

For each current element, take its absolute value because its position may already have been negated by another value. Set `nums[value - 1]` to the negative of its absolute value. Repeated occurrences simply leave the same marker negative.

**Read unmarked positions as missing values**

After marking, a positive value at index `i` proves no input element ever mapped to that position, so $i + 1$ is missing. A negative marker proves at least one occurrence. Scanning indices from left to right naturally returns missing values in increasing order.

**Why duplicates do not disturb the encoding**

Every occurrence of the same value targets the same index, and idempotent negative marking preserves the fact of presence regardless of repetition. Taking absolute values prevents earlier markers from changing the numeric identity of later elements.

#### Complexity detail

One pass marks presence and one pass collects missing values, giving $O(n)$ time. The input array stores all markers, so auxiliary space is $O(1)$ beyond the required output.

#### Alternatives and edge cases

- **Cyclic placement:** swap values toward index `value - 1`, then report mismatched positions; this also takes $O(n)$ time and $O(1)$ space.
- **Hash set:** makes the final membership checks simple but uses $O(n)$ extra space.
- **Scan the full array for every candidate:** is correct but takes $O(n^2)$ time.
- **All values present:** every marker is negative and the result is empty.
- **One repeated value:** every other value is missing.
- **Duplicate occurrences:** mark the same position repeatedly without changing the result.

</details>
