# Summary Ranges

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 228 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/summary-ranges/) |

## Problem Description
### Goal
Given a unique integer array `nums` sorted in ascending order, divide its values into maximal ranges of consecutive integers. A range continues while each next value is exactly one greater than the previous value and ends at any larger gap.

Return one string per run in the original ascending order. Represent a one-value run as `"a"`, and a run containing at least two values from `a` through `b` as `"a->b"`. Every input value must belong to exactly one summary range, ranges may not bridge missing integers, and an empty input produces an empty list.

### Function Contract
**Inputs**

- `nums`: a strictly increasing list of distinct integers

**Return value**

A list of strings. A one-value range is written as `"a"`; a longer range from `a` through `b` is written as `"a->b"`.

### Examples
**Example 1**

- Input: `nums = [0, 1, 2, 4, 5, 7]`
- Output: `["0->2", "4->5", "7"]`

**Example 2**

- Input: `nums = [0, 2, 3, 4, 6, 8, 9]`
- Output: `["0", "2->4", "6", "8->9"]`

**Example 3**

- Input: `nums = []`
- Output: `[]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Extend a run until the first gap**

Keep the first value of the current range. Advance one index while adjacent values differ by exactly one. The first non-consecutive value closes the current maximal range and begins the next.

At the start of each outer iteration, every value before the current index has been emitted exactly once, and the current index is the first value of the next not-yet-emitted range.

**A first gap proves the range is maximal**

If its first and last values match, emit the single number. Otherwise emit the two endpoints joined by `->`. Intermediate values need no separate storage.

In `[0,1,2,4,5,7]`, the first scan stops after `2`, producing `0->2`. The next stops after `5`, producing `4->5`, and the final singleton produces `7`.

The inner scan extends a range exactly while consecutive membership holds and stops at the first value that cannot belong to it. Thus every emitted interval is maximal. The outer scan resumes at that first excluded value, so the ranges are ordered, disjoint, and cover the entire input.

#### Complexity detail

Each element advances an index once, giving $O(n)$ time. Apart from the required output strings, only indices and endpoint values are stored, giving $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **A set followed by repeated searches:** loses the given order and uses extra space.
- **Expanding every integer inside a range:** does unnecessary work and can be unsafe near integer limits.
- Empty input returns no ranges; negative values and boundary-sized integers are formatted normally.

</details>
