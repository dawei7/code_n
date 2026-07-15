# Sort Items by Groups Respecting Dependencies

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1203 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/) |

## Problem Description

### Goal

There are `n` zero-indexed items. Each item belongs either to one of `m` zero-indexed groups or to no group: `group[i]` gives item `i`'s group, while `-1` denotes an ungrouped item. A group is allowed to contain no items.

Produce an ordering of all items in which every item from the same group appears in one contiguous block. The dependency list `beforeItems[i]` contains every item that must occur to the left of item `i` in that ordering. Return any ordering satisfying both the dependency and contiguity requirements. If no such ordering exists, return an empty list.

### Function Contract

**Inputs**

- `n`: The number of items, labeled from `0` through `n - 1`, where $1\le n\le3\times10^4$.
- `m`: The number of original groups, where $1\le m\le n$.
- `group`: A length-$n$ array with `group[i]` between `-1` and `m - 1`.
- `beforeItems`: A length-$n$ dependency list. Each `beforeItems[i]` contains distinct item indices other than `i`.
- Let $e=\sum_{i=0}^{n-1}\lvert\texttt{beforeItems[i]}\rvert$ be the total number of dependency relations.
- Let $g$ be `m` plus the number of items whose original group is `-1`.

**Return value**

- Any permutation of all $n$ items that respects every dependency and keeps each group's items next to one another, or `[]` if none exists.

### Examples

**Example 1**

- Input: `n = 8`, `m = 2`, `group = [-1,-1,1,0,0,1,0,-1]`, `beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]`
- Output: `[6,3,4,1,5,2,0,7]`

Other valid orders may also be returned.

**Example 2**

- Input: `n = 8`, `m = 2`, `group = [-1,-1,1,0,0,1,0,-1]`, `beforeItems = [[],[6],[5],[6],[3],[],[4],[]]`
- Output: `[]`

Compared with the first example, item `4` must now precede item `6`; the resulting requirements cannot be satisfied while group `0` remains contiguous.

### Required Complexity

- **Time:** $O(n+g+e)$
- **Space:** $O(n+g+e)$

<details>
<summary>Approach</summary>

#### General

**Give every ungrouped item its own block.** An item labeled `-1` has no contiguity obligation with any other ungrouped item. Assigning each such item a fresh group identifier therefore preserves every valid answer while making every item belong to exactly one group.

**Separate the two kinds of precedence.** For every relation from `previous` to `current`, add an edge to an item graph. This graph captures the exact order required among individual items. If the endpoints belong to different groups, also add an edge from `group[previous]` to `group[current]` in a group graph. Parallel group edges are harmless: each contributes once to the indegree and is removed once during traversal.

**Topologically sort both graphs.** Kahn's algorithm repeatedly removes a zero-indegree vertex and releases its outgoing edges. If it cannot emit every item, the original dependencies contain an item cycle. If it cannot emit every group, the cross-group requirements force a group cycle. Either condition makes a valid answer impossible.

**Combine compatible orders.** Bucket the items according to their groups while visiting them in item topological order. Then visit groups in group topological order and append each group's bucket. The group order makes every block contiguous and respects every cross-group edge. Within a block, the item topological order respects every same-group edge. A cross-group item edge is also respected because its source block precedes its destination block, so the combined result satisfies all dependencies.

#### Complexity detail

Assigning groups and building the two graphs takes $O(n+e)$ time. Their topological sorts visit $n+g$ vertices and at most $2e$ stored edges, and bucketing plus assembly takes $O(n+g)$ time. The total is $O(n+g+e)$. The graphs, indegrees, orders, and buckets occupy $O(n+g+e)$ space.

#### Alternatives and edge cases

- **Depth-first topological sorting:** DFS with three-state cycle detection gives the same asymptotic bounds, but Kahn's algorithm exposes cycle detection directly through the emitted vertex count.
- **Topologically sort only items:** A valid item order can interleave two groups; regrouping it afterward may violate a cross-group dependency, so the group graph is also necessary.
- **Treat each group as one graph vertex only:** This preserves block order but loses dependencies among items inside the same group, so an item-level graph is also necessary.
- **Repeated dependency scans:** Repeatedly searching for currently eligible items is correct but can take $O(n^2+ne)$ time on a reverse chain.
- **Ungrouped items:** Each receives a distinct fresh group and may therefore appear independently.
- **Empty original groups:** They participate as isolated vertices and contribute no items when the final buckets are joined.
- **Parallel cross-group relations:** Keeping duplicate group edges is valid as long as indegrees and adjacency entries count them consistently.
- **Item cycle:** No linear ordering can satisfy all individual precedence relations, so the result is empty.
- **Group cycle without an item cycle:** The item relations may be acyclic yet require group blocks to precede one another cyclically; contiguity still makes the result impossible.

</details>
