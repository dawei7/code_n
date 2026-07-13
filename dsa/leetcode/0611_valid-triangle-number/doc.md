# Valid Triangle Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 611 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Binary Search, Greedy, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/valid-triangle-number/) |

## Problem Description
### Goal
Given an integer array `nums`, choose triplets of distinct indices and treat their values as the side lengths of a triangle. Count a triplet only when the three selected lengths can form a nondegenerate triangle, meaning every length is positive and the sum of the two shorter sides is strictly greater than the longest side.

Return the number of valid index triplets. Equal values stored at different indices represent different choices, so two triplets with the same three lengths can both count when they select different occurrences from the array.

### Function Contract
**Inputs**

- `nums`: a list of nonnegative integer side lengths

**Return value**

- The number of triples of distinct indices whose three values satisfy the triangle inequalities
- Equal values at different indices are separate choices

### Examples
**Example 1**

- Input: `nums = [2, 2, 3, 4]`
- Output: `3`

**Example 2**

- Input: `nums = [4, 2, 3, 4]`
- Output: `4`

**Example 3**

- Input: `nums = [1, 2, 3]`
- Output: `0`

### Required Complexity

- **Time:** $O(n^2)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Reduce three inequalities to one**

Sort a copy of the lengths. For indices `left < right < largest`, the two values at `left` and `right` cannot exceed the value at `largest`. With nonnegative sorted values, the only triangle inequality that can fail is therefore `values[left] + values[right] > values[largest]`.

**Fix the largest side and sweep inward**

Choose each index from the end as `largest`, then place `left` at the beginning and `right` immediately before `largest`. If the two pointed values do not beat the largest value, increasing `right` is impossible while it is fixed, so advance `left` to raise the sum.

**Count a whole valid range**

When `values[left] + values[right] > values[largest]`, replacing `left` by any index between `left` and `right - 1` only makes the smaller-side sum at least as large. Thus all `right - left` pairs ending at `right` are valid with this largest side. Add that count and decrement `right`; every pair is counted exactly once at its right endpoint.

The sweep terminates after the pointers cross. Repeating it for every largest-side index covers every index triple once, because every triple has one unique greatest index in sorted order.

#### Complexity detail

Sorting costs $O(n \log n)$ time. For each of $O(n)$ choices of the largest index, the two pointers move inward at most `n` times in total, so the sweeps cost $O(n^2)$ and dominate. Sorting a copy preserves the caller's list and uses $O(n)$ space.

#### Alternatives and edge cases

- **Enumerate every triple:** directly testing all three chosen values is simple and correct but costs $O(n^3)$ time.
- **Binary search per pair:** after sorting, find the first value not smaller than each pair sum; this costs $O(n^2 \log n)$ time.
- Zero cannot contribute to a valid triangle because the remaining two sorted sides cannot satisfy a strict sum inequality with it as one of the smaller values.
- Equality is degenerate: $1 + 2 = 3$ is not a triangle.
- Repeated values remain distinct by index, so four equal positive lengths contribute four triples.
- Lists with fewer than three elements contribute zero.

</details>
