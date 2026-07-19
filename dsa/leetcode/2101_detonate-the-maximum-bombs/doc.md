# Detonate the Maximum Bombs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2101 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Depth-First Search, Breadth-First Search, Graph Theory, Geometry |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/detonate-the-maximum-bombs/) |

## Problem Description

### Goal

Each bomb is represented by `[x, y, radius]`. Its effect covers the closed circle centered at $(x,y)$ with the given radius. When one bomb detonates, every other bomb whose center lies inside or on that circle also detonates. Each newly detonated bomb can trigger further bombs within its own range.

You may manually detonate exactly one starting bomb. Choose the start that produces the largest chain reaction and return the number of bombs that eventually detonate.

### Function Contract

Let $n$ be the number of bombs.

**Inputs**

- `bombs`: a list of $n$ triples `[x, y, radius]`, where $1 \le n \le 100$ and every coordinate and radius is between $1$ and $10^5$ inclusive.

**Return value**

Return the maximum number of bombs reachable through a chain reaction from one chosen starting bomb.

### Examples

**Example 1**

- Input: `bombs = [[2,1,3],[6,1,4]]`
- Output: `2`
- Explanation: The right bomb reaches the left bomb, although the left bomb does not reach the right one.

**Example 2**

- Input: `bombs = [[1,1,5],[10,10,5]]`
- Output: `1`
- Explanation: Neither center lies within the other bomb's range.

**Example 3**

- Input: `bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]`
- Output: `5`
- Explanation: Starting with bomb `0` triggers bombs `1` and `2`; later detonations continue the chain through bombs `3` and `4`.

### Required Complexity

- **Time:** $O(n^3)$
- **Space:** $O(n^2)$

<details>
<summary>Approach</summary>

#### General

**Turning circular ranges into directed edges**

Create one graph vertex per bomb. Bomb `i` has a directed edge to bomb `j` when `j`'s center lies within `i`'s radius:

$$
(x_i-x_j)^2 + (y_i-y_j)^2 \le r_i^2.
$$

Use squared integers rather than square roots, avoiding floating-point boundary errors. The relation is directed because $r_i$ and $r_j$ may differ.

**Exploring every possible initial detonation**

For each bomb as the starting vertex, perform depth-first search over outgoing edges. A visited set prevents a cycle from counting or processing a bomb more than once. The number of visited vertices is exactly the number detonated by that initial choice.

Keep the largest visited count across all starts. Building the graph once separates the geometric work from the repeated reachability searches.

**Why graph reachability matches the chain reaction**

Every graph edge represents a direct physical trigger, so following a path describes a valid sequence of detonations. Conversely, every bomb activated during the real chain reaction is triggered by an already active bomb, giving one more directed edge on a path from the start. Thus the bombs reached by graph search are exactly those that detonate.

Trying every possible start therefore includes the optimal manually detonated bomb, and taking the maximum reachable count returns the requested result.

#### Complexity detail

Testing all ordered bomb pairs takes $O(n^2)$ time and stores at most $O(n^2)$ directed edges. A search from one start costs $O(n + e)$ for $e$ stored edges; performing it from all $n$ starts costs $O(n(n+e))$, which is $O(n^3)$ in the dense worst case. The adjacency lists and a search's visited state use $O(n^2)$ space overall.

#### Alternatives and edge cases

- **On-demand geometry during each search:** Instead of storing edges, compare every reached bomb with all targets. This keeps auxiliary storage near $O(n)$ but still takes $O(n^3)$ worst-case time.
- **Breadth-first search:** A queue computes the same reachable set and has the same complexity as iterative depth-first search.
- **Transitive closure:** Floyd-Warshall can compute all reachability in $O(n^3)$ time and $O(n^2)$ space, but it does more uniform work than necessary on sparse graphs.
- A bomb always counts itself after it is chosen, so the answer is at least `1`.
- A center exactly on a range boundary is triggered because the distance comparison is inclusive.
- Two bombs at the same center trigger each other regardless of their positive radii.
- Large coordinates require squared arithmetic wide enough to avoid integer overflow in fixed-width languages.
- Reachability may be asymmetric: bomb `i` can trigger bomb `j` even when `j` cannot trigger `i`.

</details>
