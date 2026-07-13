# Wiggle Sort

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 280 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/wiggle-sort/) |

## Problem Description
### Goal
Given a mutable integer array, rearrange its existing values into wiggle order. Starting at index zero, adjacent comparisons must alternate as `nums[0] <= nums[1] >= nums[2] <= nums[3] >= ...` through the full array.

Modify the array in place and return nothing. Use exactly the original multiset, including every duplicate occurrence, without introducing or deleting values. The inequalities are non-strict, so equal neighbors are allowed and a valid arrangement always exists. Many outputs may satisfy the pattern; any one is acceptable, including the unchanged input when it already has the required alternating comparisons.

### Function Contract
**Inputs**

- `nums`: the mutable integer array

**Return value**

Returns `None`; after in-place mutation, `nums[0] <= nums[1] >= nums[2] <= nums[3] ...`, using exactly the original multiset.

### Examples
**Example 1**

- Input: `nums = [3,5,2,1,6,4]`
- Output: one valid result is `[3,5,1,6,2,4]`

**Example 2**

- Input: `nums = [1,2,3,4]`
- Output: one valid result is `[1,3,2,4]`

**Example 3**

- Input: `nums = [2,2,2]`
- Output: `[2,2,2]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Repair the next alternating inequality locally**

Scan left to right. At odd index `i`, require `nums[i - 1] <= nums[i]`; at even index, require `nums[i - 1] >= nums[i]`. Swap the adjacent values exactly when the required relation is violated.

Before processing index `i`, every relation ending before `i` already wiggles. The optional swap fixes the relation at `i` without breaking the preceding one because the value moved left is an even better local low or high for that preceding requirement.

**The swap cannot break the inequality behind it**

At a position that must be a local high, a violating pair is swapped so the larger value moves right; the smaller value moving left can only strengthen the preceding local-low relation. At a position that must be a local low, the symmetric swap moves the larger value left and likewise strengthens the preceding local-high relation. Each step fixes the new relation without disturbing the established prefix, so induction yields a valid wiggle ordering.

#### Complexity detail

One comparison and at most one swap per adjacent pair gives $O(n)$ time and $O(1)$ space.

#### Alternatives and edge cases

- **Sort then interleave:** works but costs $O(n \log n)$.
- **Quadratic sorting before interleaving:** is unnecessarily slow.
- Equal values satisfy both non-strict inequalities; empty and singleton arrays already qualify.

</details>
