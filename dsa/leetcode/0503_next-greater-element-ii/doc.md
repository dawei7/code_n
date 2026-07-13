# Next Greater Element II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 503 |
| Difficulty | Medium |
| Topics | Array, Stack, Monotonic Stack |
| Official Link | [LeetCode](https://leetcode.com/problems/next-greater-element-ii/) |

## Problem Description
### Goal
Given a nonempty circular integer array `nums`, treat the position after the final element as position zero. For each original index, scan forward in traversal order, wrapping through the beginning at most once, and seek the first later value that is strictly greater than the current value.

Return one answer per original position. Store that first greater value when it exists and `-1` otherwise. Equal values do not qualify, the search cannot use the starting occurrence as its own greater element, and a value found after wrapping is valid only when it is the earliest qualifying value along that circular traversal.

### Function Contract
**Inputs**

- `nums`: a nonempty integer array interpreted circularly

**Return value**

- One next-greater value per input position

### Examples
**Example 1**

- Input: `nums = [1, 2, 1]`
- Output: `[2, -1, 2]`

**Example 2**

- Input: `nums = [1, 2, 3, 4, 3]`
- Output: `[2, 3, 4, -1, 4]`

**Example 3**

- Input: `nums = [5, 4, 3, 2, 1]`
- Output: `[-1, 5, 5, 5, 5]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Keep unresolved positions in decreasing-value order**

Scan indices while a stack stores positions whose next greater value has not appeared. Stack values are nonincreasing from bottom to top. When the current value is greater than the top's value, it is the first qualifying value for that position, so record it and pop.

**Simulate one circular wrap**

Iterate $2 \cdot n$ positions and read `nums[index % n]`. The first pass discovers ordinary right-side answers and places every position on the stack. The second pass exposes the array prefix as the wrapped suffix.

**Push each position only once**

During the second pass, resolve existing entries but do not push indices again. After two passes, every possible later circular position has been considered. Entries still unresolved correctly retain `-1`.

**Why the first popped value is correct**

A position remains on the stack through all intervening values that are not strictly greater. It is popped at the first greater value in circular scan order. Since no position is allowed to look beyond one complete wrap, two passes cover exactly the legal search range.

#### Complexity detail

Each of `n` indices is pushed once and popped at most once; the $2 \cdot n$ loop is therefore $O(n)$ time. The result and monotonic stack use $O(n)$ space.

#### Alternatives and edge cases

- **Scan forward separately from each index:** is correct but takes $O(n^2)$ time in a descending array.
- **Reverse traversal with a doubled index range:** maintains a stack of candidate values and has the same linear bounds.
- **Physically duplicate the array:** simplifies indexing but allocates another $O(n)$ list unnecessarily.
- **All equal values:** strict comparison leaves every answer as `-1`.
- **Strictly decreasing values:** every value except the maximum wraps to that maximum.
- **Single element:** cannot use itself as a greater successor.
- **Duplicates:** equal values must not pop one another.

</details>
