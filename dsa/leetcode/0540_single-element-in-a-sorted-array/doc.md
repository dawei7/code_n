# Single Element in a Sorted Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 540 |
| Difficulty | Medium |
| Topics | Array, Binary Search |
| Official Link | [LeetCode](https://leetcode.com/problems/single-element-in-a-sorted-array/) |

## Problem Description
### Goal
Given a nonempty integer array `nums` sorted in ascending order, exactly one value appears once and every other value appears exactly twice. Equal pairs are adjacent because of the sorted order.

Return the single value that lacks a matching occurrence. Do not return its index, and do not treat one member of a normal pair as the answer. Meet the required $O(\log n)$ time and $O(1)$ extra space by exploiting how pair alignment changes around the singleton rather than scanning or copying the complete array.

### Function Contract
**Inputs**

- `nums`: a nonempty sorted integer array of odd length with one singleton and adjacent duplicate pairs

**Return value**

- The unique value that occurs once

### Examples
**Example 1**

- Input: `nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]`
- Output: `2`

**Example 2**

- Input: `nums = [3, 3, 7, 7, 10, 11, 11]`
- Output: `10`

**Example 3**

- Input: `nums = [1]`
- Output: `1`

### Required Complexity

- **Time:** $O(\log n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Observe where pair alignment changes**

Before the singleton, every duplicate pair begins at an even index and ends at the following odd index. The singleton consumes one position, so every pair after it begins at an odd index instead.

**Compare an even midpoint with its partner**

Choose the midpoint and move it one position left when it is odd, making it the possible start of a pair. If `nums[mid] = nums[mid + 1]`, pair alignment is still normal through that pair, so the singleton lies strictly to its right. Otherwise the alignment has already broken, so the singleton is at `mid` or to its left.

**Maintain a search interval containing the singleton**

On a matching pair, move the lower bound past both elements. On a mismatch, retain the even midpoint as the new upper bound. Each update preserves the singleton and removes at least half of the remaining candidates.

**Why convergence identifies the unique value**

The parity rule is true for every complete pair before and after the singleton. Therefore a matching even-index pair proves the singleton is later, while a mismatch proves it is no later than that index. When the bounds meet, the invariant leaves exactly the singleton index, whose value is returned.

#### Complexity detail

Each comparison halves the search interval, so the algorithm takes $O(\log n)$ time. It uses only bounds and a midpoint, giving $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **XOR every value:** cancels duplicate pairs in $O(n)$ time and $O(1)$ space but misses the logarithmic requirement.
- **Linear neighbor scan:** can return the first unpaired value but also takes $O(n)$ time.
- **Frequency map:** is correct without sorted input but costs $O(n)$ time and space.
- **Singleton at the first index:** the first even comparison mismatches and keeps the left boundary.
- **Singleton at the last index:** every preceding even pair matches and is discarded.
- **One element:** the bounds already coincide, so that value is returned immediately.
- **Negative values:** only equality and sorted positions matter.

</details>
