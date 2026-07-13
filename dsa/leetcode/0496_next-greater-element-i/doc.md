# Next Greater Element I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 496 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Stack, Monotonic Stack |
| Official Link | [LeetCode](https://leetcode.com/problems/next-greater-element-i/) |

## Problem Description
### Goal
You are given two distinct 0-indexed integer arrays `nums1` and `nums2`. Every value in both arrays is unique, and `nums1` is a subset of `nums2`. For each `nums1[i]`, locate its matching position in `nums2` and inspect values to the right of that position.

Return an answer of length `len(nums1)` whose entry is the first value to the right in `nums2` that is strictly greater than `nums1[i]`. Use `-1` when no such value exists. The task asks for the greater value rather than its index, and later values cannot be chosen when an earlier qualifying value already appears.

### Function Contract
**Inputs**

- `nums1`: distinct query values
- `nums2`: distinct values containing every element of `nums1`

**Return value**

- One next-greater result for each value of `nums1`, in query order

### Examples
**Example 1**

- Input: `nums1 = [4, 1, 2], nums2 = [1, 3, 4, 2]`
- Output: `[-1, 3, -1]`

**Example 2**

- Input: `nums1 = [2, 4], nums2 = [1, 2, 3, 4]`
- Output: `[3, -1]`

**Example 3**

- Input: `nums1 = [1], nums2 = [1, 2]`
- Output: `[2]`

### Required Complexity

- **Time:** $O(n + m)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Keep values still waiting for a greater successor**

Scan `nums2` from left to right with a stack whose values decrease from bottom to top. Every stacked value has not yet encountered a greater value to its right.

**Resolve all smaller stack tops**

When the current value exceeds the stack top, it is the first greater value seen since that top was pushed. Pop and map that value to the current one. Continue popping while the condition holds, then push the current value as another unresolved candidate.

**Answer queries through the map**

Values left on the stack have no greater successor and need no explicit entry. For each value in `nums1`, return its mapped successor or `-1` when absent.

**Why the mapped value is the first greater one**

A value remains on the stack through every intervening value that is not greater. It is popped at the first scan position that is greater, so the recorded successor satisfies both the value and nearest-right requirements. Distinct input values make the value-to-answer map unambiguous.

#### Complexity detail

Each of the `n` values in `nums2` is pushed once and popped at most once, and the `m` queries each take constant expected lookup time. Total time is $O(n + m)$ and the stack plus map use $O(n)$ space.

#### Alternatives and edge cases

- **Scan right from every query position:** is correct but can take $O(n \cdot m)$ time.
- **Reverse monotonic stack:** scanning right to left maps each value to the surviving greater stack top with the same linear bounds.
- **Index map plus scans:** locates queries quickly but still repeats suffix work without a monotonic structure.
- **Strictly decreasing `nums2`:** every answer is `-1`.
- **Strictly increasing `nums2`:** each value except the last maps to its immediate successor.
- **Last element:** never has a greater value to its right.
- **Query order:** answers follow `nums1`, not their order in `nums2`.

</details>
