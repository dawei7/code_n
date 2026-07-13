# H-Index

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 274 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sorting, Counting Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/h-index/) |

## Problem Description
### Goal
Given one nonnegative citation count for each of a researcher's papers, compute the researcher's h-index. An integer `h` is valid when at least `h` papers have received at least `h` citations each.

Return the largest valid `h`. Papers beyond those `h` may have any smaller or larger counts, and citation values above the number of papers do not make the index exceed the paper count. For one paper, the h-index is `1` when it has at least one citation and `0` otherwise. The result is a rank-like integer rather than a citation total or the number of distinct citation values.

### Function Contract
**Inputs**

- `citations`: nonnegative citation counts, one per paper

**Return value**

The researcher's h-index.

### Examples
**Example 1**

- Input: `citations = [3,0,6,1,5]`
- Output: `3`

**Example 2**

- Input: `citations = [1,3,1]`
- Output: `1`

**Example 3**

- Input: `citations = [10,8,5,4,3]`
- Output: `4`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Counts above `n` are equivalent for the h-index**

An h-index cannot exceed the number of papers `n`, so place every citation count at least `n` into bucket `n`; otherwise use its exact count as the bucket index.

**Descending accumulation tests candidates from best to worst**

Scan buckets downward while maintaining how many papers have at least the current citation threshold. The first threshold whose cumulative count reaches that threshold is the largest valid h-index.

At bucket index `h`, the cumulative total equals exactly the number of papers with at least `h` citations.

**The first feasible threshold is maximal**

At threshold `h`, the cumulative bucket total counts precisely the papers with at least `h` citations. Thus `total >= h` is exactly the h-index feasibility condition. Since thresholds are tested from `n` downward, no larger value is feasible when the first success is reached, making it the maximum h-index.

#### Complexity detail

Populating and scanning $n + 1$ buckets takes $O(n)$ time and $O(n)$ space.

#### Alternatives and edge cases

- **Sort citations:** is simple but takes $O(n \log n)$.
- **Count qualifying papers separately for every candidate h:** takes $O(n^2)$.
- Empty and all-zero inputs return zero; very large citation counts are safely capped at `n`.

</details>
