# Possible Bipartition

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 886 |
| Difficulty | Medium |
| Topics | Depth-First Search, Breadth-First Search, Union-Find, Graph Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/possible-bipartition/) |

## Problem Description
### Goal
A group contains `n` people labeled from `1` through `n`. Each pair `[a, b]` in `dislikes` states that person `a` dislikes person `b`, so those two people must not be placed together.

Determine whether everyone can be split into two groups of any size such that the endpoints of every dislike pair belong to different groups. Every person must be assigned to one of the two groups; return `true` when such a bipartition exists and `false` otherwise.

### Function Contract
Let $m = \lvert \texttt{dislikes} \rvert$.

**Inputs**

- `n`: the number of people, where $1 \leq n \leq 2000$.
- `dislikes`: $m$ unique pairs `[a, b]`, where $0 \leq m \leq 10^4$ and $1 \leq a < b \leq n$.

**Return value**

Return `true` if all people can be assigned to two groups while separating every dislike pair; otherwise return `false`.

### Examples
**Example 1**

- Input: `n = 4, dislikes = [[1,2],[1,3],[2,4]]`
- Output: `true`

One valid split is `[1,4]` and `[2,3]`.

**Example 2**

- Input: `n = 3, dislikes = [[1,2],[1,3],[2,3]]`
- Output: `false`

All three people dislike one another, so two groups cannot separate every pair.

**Example 3**

- Input: `n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]`
- Output: `false`

### Required Complexity
- **Time:** $O(n+m)$
- **Space:** $O(n+m)$

<details>
<summary>Approach</summary>

#### General

**Interpret the two groups as two graph colors**

Create an undirected graph with one vertex per person and one edge per dislike pair. Assigning the edge's endpoints to different groups is exactly the bipartite-graph requirement that adjacent vertices have opposite colors.

**Color every connected component**

Store `0` for an uncolored person and opposite signs for the two groups. For each still-uncolored person, choose one color and traverse that component with an explicit stack. An uncolored neighbor receives the opposite color; a neighbor already having the current person's color proves that no valid split exists.

Within a component, every traversal edge fixes the neighbor's color relative to the current vertex. If a conflict appears, the connecting paths form an odd cycle, whose endpoints cannot alternate between only two groups. If traversal finishes without conflict, every edge joins opposite colors. Starting the same process for each unvisited component handles disconnected dislike relationships, and independent components may choose either orientation of the two groups.

#### Complexity detail

Building the adjacency list takes $O(n+m)$ time and space. Each person is colored once and each undirected edge is inspected from both endpoints, so traversal also costs $O(n+m)$ time. The graph, color array, and stack use $O(n+m)$ space.

#### Alternatives and edge cases

- **Breadth-first coloring:** A queue instead of a stack gives the same $O(n+m)$ bounds and correctness argument.
- **Union-find with enemy representatives:** Each person's disliked neighbors can be unioned into the opposite side, but the bookkeeping is less direct than two-coloring.
- **Try every two-group assignment:** Exhaustive search is correct but may require $O(2^n m)$ time.
- **Rescan every dislike pair for each person:** This avoids an adjacency list but can cost $O(nm)$ time.
- **Disconnected components:** Begin a new coloring traversal from every uncolored person rather than only from person `1`.
- **No dislike pairs:** Every grouping is valid, including placing all people in one group.
- **Odd and even cycles:** An odd cycle makes bipartition impossible, while an even cycle can alternate colors successfully.

</details>
