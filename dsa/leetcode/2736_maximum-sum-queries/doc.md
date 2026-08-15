# Maximum Sum Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2736 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Stack, Binary Indexed Tree, Segment Tree, Sorting, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/maximum-sum-queries/) |

## Problem Description

### Goal

Two arrays `nums1` and `nums2` describe $n$ points: index $j$ corresponds to the pair `(nums1[j], nums2[j])`. Each query supplies thresholds `[x, y]`.

For every query, consider all indices whose first value is at least `x` and whose second value is at least `y`. Return the maximum possible sum `nums1[j] + nums2[j]` among those indices. If no point satisfies both lower bounds, return `-1` for that query. Answers must preserve the original query order.

### Function Contract

**Inputs**

- `nums1`: The first coordinates of $n$ points, where $1 \le n \le 10^5$ and $1 \le \texttt{nums1}[i] \le 10^9$.
- `nums2`: The corresponding second coordinates, also between $1$ and $10^9$.
- `queries`: A list of $q$ threshold pairs `[x, y]`, with $1 \le q \le 10^5$ and both thresholds between $1$ and $10^9$.

**Return value**

Return a length-$q$ array whose entry for each query is the maximum eligible coordinate sum, or `-1` when no point is eligible.

### Examples

#### Example 1

- **Input:** `nums1 = [4,3,1,2], nums2 = [2,4,9,5], queries = [[4,1],[1,3],[2,5]]`
- **Output:** `[6,10,7]`
- **Explanation:** The best eligible points have sums `6`, `10`, and `7` respectively.

#### Example 2

- **Input:** `nums1 = [3,2,5], nums2 = [2,3,4], queries = [[4,4],[3,2],[1,1]]`
- **Output:** `[9,9,9]`
- **Explanation:** Point `(5,4)` satisfies all three queries and has the largest sum.

#### Example 3

- **Input:** `nums1 = [2,1], nums2 = [2,3], queries = [[3,3]]`
- **Output:** `[-1]`
- **Explanation:** Neither point reaches both thresholds.
