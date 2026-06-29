# Galactic Network

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | GALACTICNW |
| Difficulty Band | Graphs |
| Path | Data Structures and Algorithms |
| Lesson | Connectivity and Cycles in Graphs |
| Official Link | [GALACTICNW](https://www.codechef.com/learn/course/graphs/GRAPHCOMP/problems/GALACTICNW) |

---

## Problem Statement

You are given **N planets** (represented as nodes) and **M connections** between some pairs of planets (represented as undirected edges).

A **group** (connected component) is defined as a set of planets where each planet is reachable from any other planet in the same set via the given connections. Planets in different groups cannot reach each other through the existing connections.

Your task is to **find the number of disconnected groups (connected components) in the galaxy network** based on the given connections.

---

## Input Format

* The first line contains two space-separated integers, `N` and `M`, representing the number of planets and connections.
* Planets are numbered from `1` to `N`.
* The next `M` lines describe the connections, each containing two integers, `u` and `v`, representing a bidirectional connection between planets `u` and `v`.
* Each connection links two distinct planets, and at most one connection exists between any two planets.

---

## Output Format

- On a single line, print a single integer - the number of connected components.

---

## Constraints

* $1 \leq N \leq 200{,}000$
* $0 \leq M \leq 200{,}000$
* $1 \leq u_i, v_i \leq N$
* $u_i \neq v_i$ for each $1 \leq i \leq M$

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
1
```

**Explanation**

Since all the planets are already interconnected so there is only 1 connected group.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:** Graphs, DFS or BFS, Connected Components

**Problem:** In the vast galaxy, there are N planets connected by wormholes, forming a unique galactic network. Unfortunately, some planets are unreachable due to malfunctioning wormholes. To make all planets interconnected, scientists decided to place satellites in some planets and create inter-planet connections. The goal is to find the minimum number of satellites needed to connect all N planets.

**Solution Approach:** We can use DFS to find connected components in the graph. Each connected component represents a group of planets that can be connected with a single satellite. Basically we need at least one satellite in each connected group of planets so that it can connect with other groups of planets. Hence, total no. of connected groups of planets = minimum no. of satellite needed.

**Time complexity:**  O(N + M) as we need to explore all planets using DFS.

**Space complexity:** O(N) as we need to store the visited states in an array.

</details>
