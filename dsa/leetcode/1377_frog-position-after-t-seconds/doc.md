# Frog Position After T Seconds

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1377 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Breadth-First Search, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/frog-position-after-t-seconds/) |

## Problem Description

### Goal

An undirected tree has `n` vertices numbered from `1` through `n`. A frog starts at vertex `1`. Every second, if the current vertex has any adjacent vertex that the frog has not visited, the frog chooses uniformly among those unvisited neighbors and jumps to one of them.

The frog never revisits a vertex. If no unvisited neighbor is available, it remains at its current vertex for every later second. Given a time `t` and a `target` vertex, return the probability that the frog is at `target` after exactly `t` seconds.

### Function Contract

**Inputs**

- `n`: the number of vertices, with $1 \le n \le 100$.
- `edges`: the `n - 1` undirected edges of the tree.
- `t`: the number of elapsed seconds, with $1 \le t \le 50$.
- `target`: the vertex whose probability is requested.

**Return value**

- The probability that the frog occupies `target` after exactly `t` seconds.

### Examples

**Example 1**

- Input: `n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4`
- Output: `0.16666666666666666`

**Example 2**

- Input: `n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 1, target = 7`
- Output: `0.3333333333333333`

**Example 3**

- Input: `n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 20, target = 6`
- Output: `0.16666666666666666`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Root the tree at the starting vertex.** Build an adjacency list, then traverse states containing a vertex, its parent, elapsed time, and the probability of reaching it. The parent is the only previously visited neighbor because an undirected tree has one unique path from vertex `1` to every vertex.

For a state at `node`, its available choices are the adjacent vertices other than `parent`. If there are `k` such children, each receives `probability / k` one second later. When the target is reached, its probability is valid if the elapsed time is exactly `t`, or if it has no children and the frog can remain there for all unused time. If the target is reached early with a child available, its final probability is zero because the frog must leave.

The tree has a unique root-to-target path. Multiplying the reciprocal choice counts along that path gives exactly the probability carried by the traversal, and the timing rule above determines whether that path leaves the frog at the target at second `t`.

#### Complexity detail

Constructing the adjacency list and visiting each relevant tree vertex at most once take $O(n)$ time. The adjacency lists and explicit traversal stack use $O(n)$ space.

#### Alternatives and edge cases

- **Second-by-second probability simulation:** Propagate a full probability distribution for all `t` seconds. It is correct but may revisit stationary leaf states and do more work than the single tree traversal.
- **Rescan the raw edges:** Discover every node's neighbors by examining all edges each time, which raises the traversal to $O(n^2)$ time.
- **Target reached too early:** An internal target has probability zero at a later time because the frog must continue to an unvisited child.
- **Leaf reached early:** A leaf retains its arrival probability for every remaining second.
- **Insufficient time:** If the target depth exceeds `t`, the frog cannot reach it.
- **Starting vertex:** Vertex `1` has probability one after positive time only when it has no child; otherwise the frog leaves after the first second.
- **Uniform choice:** Divide only by unvisited children, never by the parent edge.

</details>
