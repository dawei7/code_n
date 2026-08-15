# Maximize Score After Pair Deletions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3496 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximize-score-after-pair-deletions/) |

## Problem Description

### Goal

Begin with the integer array `nums`. While it contains more than two elements, an operation must delete exactly two current boundary elements: either the first two, the last two, or the first and last. Add both deleted values to the accumulated score, including negative values when they are selected.

Operations stop as soon as at most two elements remain; those survivors do not contribute to the score. Choose the deletion sequence that makes the total score as large as possible and return that maximum. The original order of all elements that remain after any operation is preserved.

### Function Contract

**Inputs**

- `nums`: A list of integers whose current boundaries determine which pairs may be deleted.

The length satisfies $1\le n\le10^5$, and every value is between $-10^4$ and $10^4$.

**Return value**

Return the maximum score obtainable when operations continue until no more are allowed.

### Examples

#### Example 1

- **Input:** `nums = [2,4,1]`
- **Output:** `6`
- **Explanation:** Removing the first two elements scores `2 + 4`; the remaining one-element array ends the process.

#### Example 2

- **Input:** `nums = [5,-1,4,2]`
- **Output:** `7`
- **Explanation:** Removing the first and last elements scores `5 + 2` and leaves the adjacent pair `[-1,4]`.
