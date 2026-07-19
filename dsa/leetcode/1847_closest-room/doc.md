# Closest Room

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/closest-room/) |
| Frontend ID | 1847 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Sorting, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Each entry in `rooms` supplies a unique room identifier and that room's size. Every query supplies a preferred identifier and a minimum acceptable size. A room is eligible for the query only when its size is at least that minimum.

Among eligible rooms, choose the identifier with the smallest absolute difference from the preferred identifier. If two identifiers are equally distant, choose the smaller identifier. Return the selected identifier for every query in the original query order, using `-1` when no room meets the size requirement.

### Function Contract

**Inputs**

- `rooms`: a list of `[roomId, size]` pairs with unique `roomId` values.
- `queries`: a list of `[preferred, minSize]` pairs.
- $1 \le \lvert\texttt{rooms}\rvert,\lvert\texttt{queries}\rvert \le 10^5$.
- Room IDs, preferred IDs, room sizes, and minimum sizes are positive and at most $10^7$.
- Let $r=\lvert\texttt{rooms}\rvert$ and $q=\lvert\texttt{queries}\rvert$.

**Return value**

- For each query, consider exactly rooms whose size is at least `minSize`.
- Minimize $\lvert\texttt{roomId}-\texttt{preferred}\rvert$.
- On equal distance, choose the smaller `roomId`.
- Return `-1` if the eligible set is empty.
- Preserve the original order of the queries in the output list.

### Examples

**Example 1**

- Input: `rooms = [[2, 2], [1, 2], [3, 2]]`, `queries = [[3, 1], [3, 3], [5, 2]]`
- Output: `[3, -1, 3]`

No room reaches size 3 for the second query.

**Example 2**

- Input: `rooms = [[1, 4], [2, 3], [3, 5], [4, 1]]`, `queries = [[2, 3], [2, 4], [2, 5]]`
- Output: `[2, 1, 3]`

For minimum size 4, IDs 1 and 3 are equally distant from preferred ID 2, so ID 1 wins the tie.

**Example 3**

- Input: `rooms = [[10, 2]]`, `queries = [[5, 1], [20, 3]]`
- Output: `[10, -1]`

### Required Complexity

- **Time:** $O((r+q)\log r)$
- **Space:** $O(r+q)$

<details>
<summary>Approach</summary>

#### General

**Sweep minimum sizes offline**

Sort rooms by size descending. Attach each query's original index and sort queries by `minSize` descending. Before answering a query, advance through the room list and activate every room whose size reaches the query's threshold. Because later queries have no larger threshold, activated rooms never need to be removed.

The active room IDs are therefore exactly the eligible set for the current query. What remains is an ordered-set search for the nearest ID on either side of `preferred`.

**Implement the ordered set with compressed IDs**

Sort all room IDs once and map each ID to a one-based coordinate. A Fenwick tree stores 1 for an active coordinate and 0 otherwise. Its prefix sums count active IDs up to any coordinate, and binary lifting finds the coordinate containing the $k$th active ID.

Binary search locates the coordinate boundary at `preferred`. The final active ID at or below that boundary is the predecessor candidate; the first active ID at or above it is the successor candidate. At least one exists whenever the active count is nonzero. Compare candidates by the pair `(absolute distance, room ID)`, which directly implements both the main criterion and tie rule.

For each query, the size sweep activates all and only eligible rooms. Any ID smaller than the predecessor is farther left than the predecessor, and any ID larger than the successor is farther right than the successor. Thus no other eligible ID can beat those two boundary candidates. Comparing them selects exactly the requested room, and writing by the saved query index restores input order.

#### Complexity detail

Sorting rooms, queries, and IDs costs $O(r\log r+q\log q)$. Each room activation and each query's prefix/rank searches cost $O(\log r)$, so the total is $O((r+q)\log r)$ when expressed against the room-set operations, with query sorting included in the same standard combined bound. The sorted structures, Fenwick tree, indexed queries, and answer use $O(r+q)$ space.

#### Alternatives and edge cases

- **Balanced ordered set:** A tree with predecessor and successor operations expresses the sweep directly, but Python's standard library does not provide one.
- **Scan all rooms per query:** It is simple and correct but takes $O(rq)$ time.
- **Insert into a sorted list:** Binary search finds the insertion point, but shifting list elements makes activation $O(r)$ each.
- **No eligible room:** Leave the answer as `-1`.
- **Exact preferred ID:** If eligible, its distance is zero and it must be selected.
- **Equal distance:** Compare IDs after distance so the smaller one wins.
- **Threshold equality:** A room with `size == minSize` is eligible.
- **One-sided candidates:** The preferred ID may lie below every active ID or above every active ID.
- **Repeated queries:** Each is answered independently and returned at its own original position.

</details>
