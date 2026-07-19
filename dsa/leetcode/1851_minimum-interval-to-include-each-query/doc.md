# Minimum Interval to Include Each Query

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/minimum-interval-to-include-each-query/) |
| Frontend ID | 1851 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Sweep Line, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Each element of `intervals` is a closed integer interval `[left, right]`. Its size is `right - left + 1`, and it includes a query value `q` exactly when `left <= q <= right`.

For every value in `queries`, find the size of the smallest input interval that includes it. If no interval covers that query, use `-1`. Return answers in the same order as the original query array, including repeated queries.

### Function Contract

**Inputs**

- `intervals`: between 1 and $10^5$ closed intervals `[left, right]`, with $1\le\texttt{left}\le\texttt{right}\le10^7$.
- `queries`: between 1 and $10^5$ integers, each between 1 and $10^7$.
- Let $n=\lvert\texttt{intervals}\rvert$ and $q=\lvert\texttt{queries}\rvert$.

**Return value**

- Return an array of length $q$ whose entry at index $i$ is the minimum $r-l+1$ over all intervals satisfying $l\le\texttt{queries[i]}\le r$.
- Use `-1` when that set of covering intervals is empty.

### Examples

**Example 1**

- Input: `intervals = [[1, 4], [2, 4], [3, 6], [4, 4]]`, `queries = [2, 3, 4, 5]`
- Output: `[3, 3, 1, 4]`

**Example 2**

- Input: `intervals = [[2, 3], [2, 5], [1, 8], [20, 25]]`, `queries = [2, 19, 5, 22]`
- Output: `[2, -1, 4, 6]`

**Example 3**

- Input: `intervals = [[5, 5]]`, `queries = [4, 5, 6]`
- Output: `[-1, 1, -1]`

### Required Complexity

- **Time:** $O((n+q)\log(n+q))$
- **Space:** $O(n+q)$

<details>
<summary>Approach</summary>

#### General

Sort intervals by left endpoint and pair each query with its original index before sorting the queries by value. Sweep queries from small to large. Before answering query $x$, add every interval with `left <= x` to a min-heap keyed first by interval size and then by right endpoint.

Some added intervals may have expired because their right endpoint is less than $x$. Remove expired intervals while one is at the heap top. An expired interval hidden below the top cannot affect the answer; if it later reaches the top, it will be removed before use.

After this cleanup, every remaining heap entry started no later than $x$, and the top also ends no earlier than $x$. It therefore covers the query. Since interval size is the primary heap key, the top is the smallest covering interval. If the heap is empty, no interval covers $x$. Store the result at the query's saved original index.

#### Complexity detail

Sorting takes $O(n\log n+q\log q)$. Every interval is pushed once and popped at most once, adding $O(n\log n)$; answering queries adds $O(q)$ heap inspections. This is $O((n+q)\log(n+q))$ time. Sorted queries, answers, and the heap use $O(n+q)$ space.

#### Alternatives and edge cases

- **Scan every interval per query:** Directly test coverage and keep the shortest length, but costs $O(nq)$ time.
- **Sort by interval size:** Processing intervals shortest-first can work with a disjoint-set query structure, but is more involved.
- **Closed endpoints:** A query equal to either endpoint is included.
- **No covering interval:** Return `-1`, not zero.
- **Duplicate queries:** Preserve one answer per input position.
- **Duplicate or nested intervals:** Heap ordering naturally selects the minimum size.
- **Original order:** Sorting queries is only an internal sweep; restore answers by saved indices.
- **Expired non-top entries:** They may remain lazily because they cannot win while a smaller valid interval is above them.

</details>
