# Non-decreasing Subsequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 491 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Backtracking, Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/non-decreasing-subsequences/) |

## Problem Description
### Goal
Given an integer array `nums`, form subsequences by selecting indices in their original left-to-right order without requiring the positions to be contiguous. A subsequence is non-decreasing when every selected value is greater than or equal to the preceding selected value.

Return all the different possible non-decreasing subsequences containing at least two elements, in any order. Equal values from different indices may appear together, but different index selections that produce the same value sequence must not duplicate the answer. Values may be negative, and a decrease between selected values invalidates that candidate.

### Function Contract
**Inputs**

- `nums`: a nonempty integer array

**Return value**

- All distinct non-decreasing subsequences of length at least two

### Examples
**Example 1**

- Input: `nums = [4, 6, 7, 7]`
- Output: `[[4,6],[4,7],[4,6,7],[4,6,7,7],[4,7,7],[6,7],[6,7,7],[7,7]]`

**Example 2**

- Input: `nums = [4, 4, 3, 2, 1]`
- Output: `[[4,4]]`

**Example 3**

- Input: `nums = [3, 2, 1]`
- Output: `[]`

### Required Complexity

- **Time:** $O(n \cdot 2^n)$
- **Space:** $O(n \cdot 2^n)$

<details>
<summary>Approach</summary>

#### General

**Build paths in index order**

Backtracking carries the next index and a current path. A value may extend the path only when it is at least the last selected value. Advancing the index after a choice preserves subsequence order.

**Emit every valid prefix**

Whenever the path reaches length two, copy it into the answer, then continue because longer extensions are also valid results.

**Deduplicate at each decision depth**

A local `used` set permits each value only once within one recursive call. Equal values chosen at that depth create the same value prefix, while the same value must remain available deeper to form sequences such as `[7, 7]`.

**Why answers are complete and unique**

Every valid subsequence defines increasing source indices that the recursion can follow. If two index choices produce the same values, their first differing equal choice occurs at one depth, where the local set suppresses the later duplicate.

#### Complexity detail

There may be $\Theta(2^{n})$ distinct answers and copying one can cost $O(n)$, so worst-case time and output space are $O(n \cdot 2^n)$. The active path and recursion data are smaller than the output bound.

#### Alternatives and edge cases

- **Enumerate bit masks:** is correct but generates all $2^{n}$ index subsets before deduplication.
- **Global tuple set:** removes duplicates only after doing duplicate work.
- **Dynamic sets by ending index:** are possible but involve heavy tuple copying.
- **All equal values:** yields one answer for every length from two through `n`.
- **Strictly decreasing input:** yields no answer.
- **Negative values:** use the same comparison.
- **Nonadjacent duplicates:** must be deduplicated without sorting the input.

</details>
