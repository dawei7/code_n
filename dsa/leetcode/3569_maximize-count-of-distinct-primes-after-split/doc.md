# Maximize Count of Distinct Primes After Split

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3569 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Segment Tree, Number Theory, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximize-count-of-distinct-primes-after-split/) |

## Problem Description

### Goal

An integer array `nums` receives a sequence of persistent point updates. Each query gives an index and a replacement value; apply that assignment before answering the query, and retain the changed array for every later query.

After an update, choose a split position $k$ with $1\le k<n$. The split creates the non-empty prefix `nums[0..k-1]` and non-empty suffix `nums[k..n-1]`. Count how many distinct prime values occur in the prefix and how many distinct prime values occur in the suffix. A prime appearing on both sides contributes once to each count.

For every query, report the maximum possible sum of those two distinct-prime counts over all legal split positions.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$, where $2\le n\le5\cdot10^4$ and every value is between $1$ and $10^5$ inclusive.
- `queries`: A sequence of $q$ pairs `[idx, val]`, where $1\le q\le5\cdot10^4$, `idx` is a valid index of `nums`, and $1\le\texttt{val}\le10^5$.

Let $U$ be the greatest value appearing initially or in any query.

**Return value**

Return an array of $q$ integers. Its $i$th element is the maximum distinct-prime count after applying query $i$ and all preceding updates.

### Examples

#### Example 1

- **Input:** `nums = [2,1,3,1,2], queries = [[1,2],[3,3]]`
- **Output:** `[3,4]`
- **Explanation:** After the first update, a split after the first element counts prime `2` on both sides and prime `3` on the right. After the second update, splitting between the middle `3` values counts both `2` and `3` on each side.

#### Example 2

- **Input:** `nums = [2,1,4], queries = [[0,1]]`
- **Output:** `[0]`
- **Explanation:** The update removes the only prime value, so every split has a total of zero.

---
