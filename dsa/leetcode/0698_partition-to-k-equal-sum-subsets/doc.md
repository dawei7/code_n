# Partition to K Equal Sum Subsets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 698 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Backtracking, Bit Manipulation, Memoization, Bitmask |
| Official Link | [LeetCode](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/) |

## Problem Description
### Goal
Given an integer array `nums` and an integer `k`, determine whether the array can be divided into exactly `k` nonempty subsets whose sums are all equal.

Return `True` if such a partition exists and `False` otherwise. Every array occurrence must belong to exactly one subset, even when several occurrences have the same value; subsets need not correspond to contiguous ranges and their internal order is irrelevant. No element may be omitted or reused.

### Function Contract
**Inputs**

- `nums`: a nonempty list of positive integers
- `k`: the required number of subsets, no greater than `len(nums)`

**Return value**

- `true` when such a complete partition exists; otherwise `false`

### Examples
**Example 1**

- Input: `nums = [4,3,2,3,5,2,1], k = 4`
- Output: `true`

**Example 2**

- Input: `nums = [1,2,3,4], k = 3`
- Output: `false`

**Example 3**

- Input: `nums = [3,1], k = 2`
- Output: `false`

### Required Complexity

- **Time:** $O(n \cdot 2^n)$
- **Space:** $O(2^n)$

<details>
<summary>Approach</summary>

#### General

**Derive the only possible subset sum**

All `k` subsets together contain the complete array, so each must sum to `target = sum(nums) / k`. A non-divisible total or an element larger than `target` makes the partition impossible immediately.

**Represent chosen elements with a bitmask**

A recursive state contains the selected-element `mask` and the sum already placed in the currently open subset, reduced modulo `target`. Memoize each state so that different insertion orders leading to the same selection are solved only once. Start with the empty mask and remainder zero.

**Append one unused value without overflowing a subset**

From every state, try each unselected element. If `remainder + value <= target`, recurse on the enlarged mask with `(remainder + value) % target`. Reaching exactly `target` closes one subset and starts the next at remainder zero.

**Why one remainder per mask is sufficient**

The total sum represented by a mask is fixed, independent of insertion order. Its remainder modulo `target` is therefore fixed as well. The memo only needs to remember whether some continuation can form completed target-sized subsets after that selection. Every transition preserves this property, and every valid partition supplies an ordering that the transitions can follow.

**Why the full mask decides the answer**

If all elements are selected with remainder zero, their total has been divided into consecutive groups of sum `target`; positivity makes each completed group nonempty. Conversely, ordering the members of any valid partition group by group produces a path from the empty mask to that full-mask state.

#### Complexity detail

There are $2^{n}$ masks and each may try up to `n` elements, so the time bound is $O(n \cdot 2^n)$. The DP array contains one integer per mask, using $O(2^n)$ space.

#### Alternatives and edge cases

- **Memoized mask search:** recursively choose the next unused number while caching `(mask, remainder)` states; it explores the same state space as the iterative DP.
- **Bucket backtracking:** sort descending and place each value into one of `k` bucket sums; skipping buckets with equal current sums is essential to avoid exploring symmetric assignments repeatedly.
- **Enumerate partitions without memoization:** it can revisit the same chosen set in many orders and grows much faster than the bitmask DP.
- If the total is not divisible by `k`, no equal-sum partition exists.
- If $k = 1$, the complete nonempty array is already a valid partition.
- When $k = n$, every value must be equal because every positive-value subset contains exactly one element.
- Duplicate values are separate elements and each occurrence must be assigned once.

</details>
