# Number of Longest Increasing Subsequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 673 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Binary Indexed Tree, Segment Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-longest-increasing-subsequence/) |

## Problem Description
### Goal
Given an integer array `nums`, consider all subsequences formed without changing the relative order of selected elements. Find the maximum possible length of a strictly increasing subsequence.

Return the number of longest increasing subsequences having that maximum length. Equal values cannot extend one another because the sequence must be strictly increasing, but subsequences choosing different index occurrences are counted separately even when their value sequences are identical. The required result is the count, not the length itself.

### Function Contract
**Inputs**

- `nums`: a nonempty list of integers

**Return value**

- The number of longest strictly increasing subsequences in `nums`

### Examples
**Example 1**

- Input: `nums = [1,3,5,4,7]`
- Output: `2`

**Example 2**

- Input: `nums = [2,2,2,2,2]`
- Output: `5`

**Example 3**

- Input: `nums = [1,2,4,3,5,4,7,2]`
- Output: `3`

### Required Complexity

- **Time:** $O(N \log N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Store both the best length and its multiplicity**

For a subsequence ending at value `x`, the relevant predecessor information is a pair `(length, count)`: the greatest increasing-subsequence length ending at a smaller value, and how many subsequences attain that length. Extending those predecessors produces `(length + 1, count)`. When no smaller predecessor exists, `x` starts one length-one subsequence.

**Combine states by keeping length before adding counts**

When two disjoint value ranges are combined, retain the pair with the greater length. If their lengths tie, add their counts because both ranges provide different predecessor indices achieving the same optimum. The neutral state is `(0, 0)`. This merge is associative, so a Fenwick tree can maintain prefix aggregates.

**Query only strictly smaller values**

Coordinate-compress the distinct numbers into increasing ranks. Before processing `nums[i]` at rank `r`, query the Fenwick prefix ending at $r - 1$; excluding rank `r` prevents equal values from extending one another. Update rank `r` with the new ending pair. Processing from left to right ensures every stored count comes from an earlier index, so equal pairs merged at a rank count distinct index choices without violating subsequence order.

**Why the final aggregate answers the question**

By induction over processed indices, every Fenwick prefix stores the maximum length achievable with an ending value in that prefix and the exact number of subsequences attaining it. The update for each new index considers precisely all valid smaller predecessors and counts every extension once by its final index. Querying the full value range after the last element therefore returns the global LIS length together with its total number of index-distinct realizations.

#### Complexity detail

Sorting the distinct values for coordinate compression takes $O(N \log N)$ time. Each of the `N` elements performs one Fenwick prefix query and one update in $O(\log N)$ time, so total time is $O(N \log N)$. The rank map and Fenwick pairs use $O(N)$ space.

#### Alternatives and edge cases

- **Quadratic dynamic programming:** maintain a length and count for every ending index and inspect all earlier indices; it is direct and correct but takes $O(N^2)$ time.
- **Segment tree of length-count pairs:** supports the same prefix aggregation in $O(N \log N)$ time with a larger constant and more storage.
- **Patience sorting lengths alone:** finds the LIS length in $O(N \log N)$, but ordinary tail replacement discards the multiplicities needed here.
- Equal values cannot follow one another, but each occurrence can start or extend a distinct subsequence from smaller values.
- In a constant array of length `N`, the longest length is one and the answer is `N`.
- In a strictly decreasing array, every individual element is a longest subsequence, so the answer is also `N`.

</details>
