# Find First and Last Position of Element in Sorted Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 34 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) |

## Problem Description
### Goal
Given an integer array `nums` sorted in non-decreasing order, locate the complete contiguous range occupied by `target`. Duplicate target values, when present, necessarily form one block because the input is sorted.

Return the inclusive indices of the block's first and last elements as `[start, end]`. If the target does not occur, return `[-1, -1]`; an empty array has the same result. The search must take logarithmic time even when the matching block itself is large, so it cannot scan outward through every duplicate.

### Function Contract
**Inputs**

- `nums`: nondecreasing `List[int]`
- `target`: `int`

**Return value**

A two-element `List[int]` containing the inclusive target range or `[-1, -1]`.

### Examples
**Example 1**

- Input: `nums = [5, 7, 7, 8, 8, 10], target = 8`
- Output: `[3, 4]`

**Example 2**

- Input: `nums = [5, 7, 7, 8, 8, 10], target = 6`
- Output: `[-1, -1]`

**Example 3**

- Input: `nums = [], target = 0`
- Output: `[-1, -1]`

### Required Complexity

- **Time:** $O(\log n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Search for two insertion boundaries, not an arbitrary match**

Run one binary search for the first index whose value is at least `target` and another for the first index whose value is greater than `target`. These are the lower and upper insertion boundaries. Searching past equal values in opposite directions avoids a linear expansion across a long duplicate run.

If the lower boundary is outside the array or does not contain target, it is absent. Otherwise the inclusive range is `[lower, upper - 1]`.

**Lower and upper bounds use different equality decisions**

For lower-bound search over half-open interval `[left, right)`, every index before `left` is known to contain a value below target, and every index at or after `right` is known to contain a value at least target. On equality, move `right` so the search continues left.

Upper-bound search uses the analogous partition `<= target` versus `> target`. On equality it moves `left`, deliberately continuing past the duplicate run. Both searches terminate when their half-open unknown interval is empty.

**Trace the two different convergence points**

For `[5, 7, 7, 8, 8, 10]` and target 8, lower-bound search converges to index 3. Upper-bound search converges to index 5, the position of 10. Subtracting one gives final range `[3, 4]`.

**Two insertion boundaries enclose exactly the target run**

Lower-bound search returns the first position whose value is not below `target`. If that position is outside the array or contains another value, no target exists. Otherwise it is the first target occurrence because every earlier value is strictly smaller.

Upper-bound search returns the first position whose value is greater than `target`. Its predecessor is therefore the last target occurrence: sorted order places every value between the two boundaries equal to target, while values outside are respectively smaller or greater. The resulting pair encloses exactly the complete duplicate run.

#### Complexity detail

Each boundary search halves its unknown interval and takes $O(\log n)$ time; two such searches remain $O(\log n)$. The iterative indices use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Find one match then expand:** can scan a duplicate run of length `n`, violating logarithmic time.
- **Linear scan:** directly finds both endpoints but costs $O(n)$.
- **Two recursive binary searches:** has the same time bound but uses call-stack space instead of constant iterative state.
- Empty input makes both insertion boundaries zero, and the explicit presence check returns `[-1, -1]`.
- A target at every array position yields lower bound `0` and upper bound `n`, producing `[0, n - 1]` without scanning duplicates.

</details>
