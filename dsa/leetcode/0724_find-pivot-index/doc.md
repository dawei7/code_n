# Find Pivot Index

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 724 |
| Difficulty | Easy |
| Topics | Array, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/find-pivot-index/) |

## Problem Description
### Goal
Given an integer array `nums`, a pivot index is an index where the sum of all numbers strictly to its left equals the sum of all numbers strictly to its right. The value at the pivot belongs to neither sum.

Return the leftmost pivot index, or `-1` if none exists. At the left edge, the empty left side has sum `0`; at the right edge, the empty right side also has sum `0`, so either endpoint can qualify under the same rule.

### Function Contract
**Inputs**

- `nums`: a nonempty integer array

**Return value**

- The smallest pivot index, or `-1` if every index has unequal left and right sums

### Examples
**Example 1**

- Input: `nums = [1,7,3,6,5,6]`
- Output: `3`

**Example 2**

- Input: `nums = [1,2,3]`
- Output: `-1`

**Example 3**

- Input: `nums = [2,1,-1]`
- Output: `0`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Express the right sum from the total**

Compute the sum of the entire array once. Before processing an index `i`, keep `left_sum` equal to the sum of `nums[0:i]`. The elements strictly to the right then sum to `total - left_sum - nums[i]`; subtracting the current value matters because a pivot belongs to neither side.

**Check before extending the left side**

Compare `left_sum` with the derived right sum, then add `nums[i]` to `left_sum` for the next iteration. At the first index, the maintained left sum is zero, correctly representing an empty left side. After the comparison at the last index, the derived right sum is zero, correctly representing an empty right side.

**Why the first match is the required answer**

The scan visits indices from left to right, and the maintained and derived sums exactly represent the two sides of each visited index. Therefore every returned index satisfies the pivot condition. Returning immediately on the first equality makes it the leftmost valid pivot; reaching the end proves that no pivot exists.

#### Complexity detail

The initial total and the left-to-right scan each process `n` values, so the time complexity is $O(n)$. The algorithm stores only the total, the running left sum, and loop state, for $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Prefix-sum array:** precompute a sum for every prefix and query both sides in constant time per index; it remains $O(n)$ time but uses $O(n)$ extra space unnecessarily.
- **Re-sum both sides at every index:** directly compute `sum(nums[:i])` and `sum(nums[i + 1:])`; it is straightforward but takes $O(n^2)$ time in the worst case.
- **Single element:** both sides are empty, so index `0` is the pivot.
- **Negative values:** totals and running sums remain valid without any monotonicity assumption.
- **Multiple pivots:** the left-to-right scan must return the smallest one.
- **No pivot:** return `-1` only after every index has been checked.

</details>
