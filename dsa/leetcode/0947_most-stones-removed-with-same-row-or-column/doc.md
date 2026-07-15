# Most Stones Removed with Same Row or Column

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 947 |
| Difficulty | Medium |
| Topics | Hash Table, Depth-First Search, Union-Find, Graph Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/) |

## Problem Description

### Goal

There are $n$ stones at distinct integer coordinate points on a two-dimensional plane. A stone may be removed only when at least one other stone that has not yet been removed lies in the same row or in the same column.

Given every stone position as `[x, y]`, choose a legal removal order that deletes as many stones as possible. Return that maximum number; stones that no longer share a row or column with any remaining stone must stay on the plane.

### Function Contract

Let $n$ be the number of stones, and let $\alpha(n)$ denote the inverse Ackermann factor for disjoint-set operations.

**Inputs**

- `stones`: a list of $n$ distinct coordinate pairs with $1 \le n \le 1000$.
- Each pair `[x, y]` satisfies $0 \le x,y \le 10^4$, and no coordinate point appears twice.

**Return value**

Return the largest number of stones that can be removed under the same-row-or-same-column rule.

### Examples

**Example 1**

- Input: `stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]`
- Output: `5`

All six stones belong to one row-or-column connected component, so one stone must remain and five can be removed.

**Example 2**

- Input: `stones = [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]`
- Output: `3`

The isolated stone `[1, 1]` forms one component and the other four stones form another, leaving two stones in total.

**Example 3**

- Input: `stones = [[0, 0]]`
- Output: `0`

### Required Complexity

- **Time:** $O(n\alpha(n))$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Translate removal reachability into components.** Treat each stone as a graph vertex and connect two vertices when their stones share a row or column. Stones related through a chain of such connections belong to one component, even when the endpoints do not directly share a coordinate.

A component containing $k$ stones can lose exactly $k-1$ stones. It cannot lose all $k$, because the final stone has no other remaining stone in its component and there are no edges to another component. Conversely, choose a spanning tree of the component and remove non-root vertices from the leaves inward. Each removed vertex still shares a row or column with its parent, which remains at that moment. Thus one stone can remain and all others can be removed. Summed over all components, the answer is $n$ minus the component count.

**Build components without comparing every pair.** Give each stone a disjoint-set index. Store one previously seen representative for each row and for each column. When processing a stone, union it with the stored representative of its row, if one exists, and do the same for its column. Otherwise record the current stone as that coordinate's representative. Any later stone sharing that row or column joins the same set, so these representative edges preserve exactly the graph's connected components.

After all unions, find the root of every stone and count distinct roots. Path compression and union by size keep the operations nearly constant time.

#### Complexity detail

Each stone performs at most two unions and one final find. With union by size and path compression, this is $O(n\alpha(n))$ time. The parent, size, row-representative, column-representative, and root sets together use $O(n)$ space.

#### Alternatives and edge cases

- **DFS with row and column buckets:** Group stone indices by row and column, then traverse each bucket at most once while exploring components. This can also run in $O(n)$ expected time with careful bucket clearing.
- **Union row nodes with column nodes:** Treat every used row and every used column as disjoint-set nodes and union the two coordinates for each stone. Counting roots among used coordinates yields the same component total.
- **Compare every stone pair:** Union two indices whenever their coordinates match in one dimension. This is correct but spends $O(n^2)$ time discovering edges.
- **One stone:** It forms one component, so `n - components` is zero.
- **All stones isolated:** Every stone is its own component and none can be removed.
- **One shared row or column:** All stones form a single component, allowing exactly $n-1$ removals.
- **Indirect connection:** Stones need not share a coordinate directly to belong to the same removable group; alternating row and column links are enough.

</details>
