# Roads Construction in  Chefs Country

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFSCOUNTRY |
| Difficulty Band | Graphs |
| Path | Data Structures and Algorithms |
| Lesson | Connectivity and Cycles in Graphs |
| Official Link | [CHEFSCOUNTRY](https://www.codechef.com/learn/course/graphs/GRAPHCOMP/problems/CHEFSCOUNTRY) |

---

## Problem Statement

Chef's country has `N` cities, and `M` roads between them. The goal is to construct new roads so that there is a route between any two cities.

Find out the minimum number of roads required.

---

## Input Format

- The first line consists of two space separated integers, `N` and `M`, representing the number of cities and number of roads between them.
- Cities are numbered from `1` to `N`.
- The subsequent `M` lines describe the roads, each containing two integers, `u` and `v`, describing a road between city `u` and city `v`.
- Each road links two distinct cities, and at most one road exists between any two cities.

---

## Output Format

- Output the number of minimum roads required to connect all the cities.

---

## Constraints

- $1 \leq N \leq 200000$
- $1 \leq M \leq N(N-1)/2$
- $1 \leq u_i, v_i \leq N$
- $u_i \neq v_i$ for each $1 \leq i \leq M$.

---

## Examples

**Example 1**

**Input**

```text
5 6
1 2
2 3
1 3
3 5
2 4
4 5
```

**Output**

```text
0
```

**Explanation**

There already exists paths between any two pair of cities and hence no new road needs to be constructed.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:** Graphs, DFS or BFS, Connected Components

**Problem:** Chef’s country has N cities, and M roads between them. The goal is to construct new roads so that there is a route between any two cities.

Find out the minimum number of roads required.

**Solution Approach:** The solution uses BFS(we can use DFS also) to find connected components in the graph. The number of connected components minus one represents the minimum number of roads needed to connect all cities. Why? Connecting any two cities within the same connected component requires only one road. Connecting C components requires C-1 roads because each road connects two components, and the last component doesn’t need an additional road.

**Time complexity:** O(N + M) as we need to explore all cities using BFS.

**Space complexity:** O(N) as we need to enqueue all nodes in a queue during bfs traversal.

</details>
