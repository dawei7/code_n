# 3Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 15 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/3sum/) |

## Problem Description
### Goal
Given an integer array `nums`, choose three different indices whose values sum to zero. Find every distinct triplet of values that can be formed this way; the same array position cannot supply more than one member of a triplet.

Return the complete collection of zero-sum triplets. Two results containing the same three values in a different order are the same triplet and must appear only once, even when duplicate input values allow many index choices. The triplets and the values within them may be returned in any order.

### Function Contract
**Inputs**

- `nums`: `List[int]`

**Return value**

A `List[List[int]]` containing all unique zero-sum triplets.

### Examples
**Example 1**

- Input: `nums = [-1, 0, 1, 2, -1, -4]`
- Output: `[[-1, -1, 2], [-1, 0, 1]]`

**Example 2**

- Input: `nums = [0, 1, 1]`
- Output: `[]`

**Example 3**

- Input: `nums = [0, 0, 0]`
- Output: `[[0, 0, 0]]`

### Required Complexity

- **Time:** $O(n^2)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Sorting turns the remaining pair sum into a monotone search**

After sorting, fix one value at index `i`. The remaining task is to find two values to its right summing to `-values[i]`. Put one pointer immediately after `i` and one at the end.

If the total is too small, moving the right pointer left cannot help: it replaces the largest remaining value with an equal or smaller one. Only moving the left pointer right can increase the sum. Symmetrically, if the total is too large, only moving the right pointer left can decrease it. This direction rule eliminates an entire row or column of candidate pairs at each step.

**Remove duplicates where each value is chosen**

Skip a fixed value equal to the previous fixed value, because it would launch an identical pair-sum search and reproduce the same value triplets. After recording a triplet, move both pointers once and then past every duplicate of the values just used. This emits each value combination once without maintaining a separate set of result tuples.

If the fixed value is positive, all values to its right are also positive, so no later triplet can sum to zero and the scan can stop.

**What pointer movement proves impossible**

For a fixed index, every pair outside the current pointer interval has either been examined or ruled out by monotonicity. Moving left after a small sum discards only pairs with an even smaller or equal left value; moving right after a large sum discards only pairs with an even larger or equal right value.

Duplicate skipping removes only value-identical candidates, never a new triplet.

**Trace the duplicate handling**

Sort `[-1, 0, 1, 2, -1, -4]` into `[-4, -1, -1, 0, 1, 2]`. No pair completes `-4`. Fix the first `-1`: pointers find $-1 + -1 + 2 = 0$, then $-1 + 0 + 1 = 0$. The second fixed `-1` is skipped, leaving exactly the two unique answers.

**Why every value triplet appears once**

In sorted order, every valid triplet has a first value. The outer scan eventually fixes that value; skipping a repeated fixed value loses no new value combination because its remaining suffix offers no elements unavailable to the earlier identical occurrence.

For a fixed value, a sum below zero can be repaired only by moving the left pointer to a no-smaller value, while a sum above zero can be repaired only by moving the right pointer to a no-larger value. Those moves discard no possible zero-sum pair. When a match is found, advancing past equal pointer values removes only duplicate spellings of the same triplet. The scan therefore finds every valid value triplet and emits each exactly once.

#### Complexity detail

Sorting costs $O(n \log n)$. For each of at most `n` fixed indices, the two pointers cross the remaining suffix once, costing $O(n)$; the total is therefore $O(n^2)$. A language's in-place sort may use $O(\log n)$ stack space, while implementations that copy or whose sort allocates working storage use up to $O(n)$ auxiliary space. The returned triplets are output space and are not avoidable.

#### Alternatives and edge cases

- **Three nested loops:** straightforward but requires $O(n^3)$ time, plus deduplication.
- **Hash a two-sum search per fixed index:** reaches expected $O(n^2)$ time but needs per-iteration hash storage and more explicit duplicate normalization.
- **Frequency enumeration:** can be effective when the value range is small, but its complexity depends on the number of distinct values.
- Fewer than three values produce no triplet. Three or more zeroes still produce only `[0, 0, 0]` once.
- Duplicate skipping must occur after a valid triplet and for repeated fixed values; skipping values indiscriminately before evaluating them can miss a combination requiring two equal numbers.

</details>
