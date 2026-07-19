# Check if All the Integers in a Range Are Covered

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/) |
| Frontend ID | 1893 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Each element `ranges[i] = [start_i, end_i]` describes an inclusive interval of integers. An integer $x$ is covered when at least one interval satisfies $\textit{start}_i \le x \le \textit{end}_i$.

Given inclusive target bounds `left` and `right`, determine whether every integer from `left` through `right` is covered. Intervals may overlap, touch at endpoints, extend beyond the target, or leave gaps. Return `true` only when no target integer is uncovered.

### Function Contract

**Inputs**

- `ranges`: an array of $N$ inclusive integer intervals.
- `left`, `right`: the inclusive target bounds.
- $1 \le N \le 50$.
- Every interval endpoint and both target bounds lie from $1$ through $50$, with each start no greater than its end and `left <= right`.
- Let $V$ be the greatest coordinate swept, at most $50$.

**Return value**

- Return `true` if every integer in `[left, right]` belongs to at least one interval; otherwise return `false`.

### Examples

**Example 1**

- Input: `ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5`
- Output: `true`

The three intervals collectively cover integers `2`, `3`, `4`, and `5`.

**Example 2**

- Input: `ranges = [[1,10],[10,20]], left = 21, right = 21`
- Output: `false`

Neither interval includes `21`.

**Example 3**

- Input: `ranges = [[1,2],[4,5]], left = 1, right = 5`
- Output: `false`

Integer `3` is the uncovered gap.
