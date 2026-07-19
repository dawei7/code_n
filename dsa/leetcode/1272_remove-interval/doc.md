# Remove Interval

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1272 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/remove-interval/) |

## Problem Description

### Goal

A set of real numbers is represented by a sorted list of pairwise-disjoint half-open intervals. Each pair `[a, b]` denotes $[a,b)$: it contains every real number $x$ satisfying $a \le x < b$. The right endpoint is excluded, so intervals that only touch at an endpoint do not overlap.

Given this list and another half-open interval `toBeRemoved`, subtract every number in the removal interval from the represented set. Return the remainder as a sorted list of disjoint, nonempty half-open intervals. An input interval may remain unchanged, disappear completely, lose one side, or split into two pieces.

### Function Contract

**Inputs**

- `intervals`: a sorted list of $n$ disjoint pairs `[start, end]`, with $1 \le n \le 10^4$ and $-10^9 \le \texttt{start} < \texttt{end} \le 10^9$.
- `to_be_removed`: a pair `[remove_start, remove_end]` representing the half-open interval to subtract.

**Return value**

- Return the sorted disjoint half-open intervals representing the original union minus `to_be_removed`.

### Examples

**Example 1**

- Input: `intervals = [[0,2],[3,4],[5,7]], to_be_removed = [1,6]`
- Output: `[[0,1],[6,7]]`

**Example 2**

- Input: `intervals = [[0,5]], to_be_removed = [2,3]`
- Output: `[[0,2],[3,5]]`

**Example 3**

- Input: `intervals = [[-5,-4],[-3,-2],[1,2],[3,5],[8,9]], to_be_removed = [-1,4]`
- Output: `[[-5,-4],[-3,-2],[4,5],[8,9]]`
