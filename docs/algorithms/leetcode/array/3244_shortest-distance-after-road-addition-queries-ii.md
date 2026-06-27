# Shortest Distance After Road Addition Queries II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3244 |
| Difficulty | Hard |
| Topics | Array, Greedy, Graph Theory, Ordered Set |
| Official Link | [shortest-distance-after-road-addition-queries-ii](https://leetcode.com/problems/shortest-distance-after-road-addition-queries-ii/) |

## Problem Description & Examples
### Goal
Given a linear path of $n$ cities indexed from $0$ to $n-1$ with initial roads connecting city $i$ to $i+1$, we receive a series of queries. Each query adds a new directed road from city $u$ to city $v$. After each addition, calculate the shortest path distance from city $0$ to city $n-1$. The roads are always added such that $u < v$, and the new roads never cross existing ones in a way that would invalidate the path structure.

### Function Contract
**Inputs**

- `n`: An integer representing the number of cities.
- `queries`: A list of lists, where each inner list `[u, v]` represents a new directed road from city `u` to city `v`.

**Return value**

- A list of integers representing the shortest path distance from city $0$ to city $n-1$ after each query is processed.

### Examples
**Example 1**

- Input: `n = 5, queries = [[2, 4], [0, 2], [0, 4]]`
- Output: `[3, 2, 1]`

**Example 2**

- Input: `n = 5, queries = [[0, 3], [0, 2]]`
- Output: `[2, 2]`

**Example 3**

- Input: `n = 4, queries = [[0, 3]]`
- Output: `[1]`

---

## Underlying Base Algorithm(s)
The problem can be solved using a greedy approach combined with a data structure to manage active intervals. Since we only add roads that skip intermediate nodes, we can maintain a set of "active" nodes that are part of the current shortest path. When a new road $(u, v)$ is added, any existing nodes between $u$ and $v$ are bypassed. We use a sorted collection (or a Disjoint Set Union / SortedList) to track the next reachable node from any given city, allowing us to efficiently remove nodes that are no longer part of the shortest path.

---

## Complexity Analysis
- **Time Complexity**: $O(q \log n)$, where $q$ is the number of queries. We use a sorted data structure to find and remove bypassed nodes, and each node is removed at most once.
- **Space Complexity**: $O(n)$, to store the mapping of the next reachable city for each node.
