# Vertex Colouring Problem

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | VERTEXCOLOR |
| Difficulty Band | Recursion |
| Path | Data Structures and Algorithms |
| Lesson | Fundamentals of Recursion |
| Official Link | [VERTEXCOLOR](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/VERTEXCOLOR) |

---

## Problem Statement

Chef has an undirected graph with $N$ vertices and $E$ edges. Chef wants to know if it is possible to colour the vertices of the graph using **at most M different colours** such that no two adjacent vertices have the same colour. \
Help Chef determine if such a colouring is possible.

### Function Declaration

### Function Name
$canColorGraph$ – This function checks whether the given graph can be coloured using at most $M$ colours without any two adjacent vertices sharing the same colour.

### Parameters

* $N$ : The number of vertices in the graph.
* $M$ : The maximum number of colours available.
* $E$ : The number of edges in the graph.
* $edges$ : A reference to a array of edges, each represented as a pair of integers $(u, v)$.

### Return Value

* Returns $true$ if the graph can be coloured with at most $M$ colours.
* Returns $false$ otherwise.

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N \leq 20$
- $0 \leq E \leq \frac{N \cdot (N-1)}{2}$
- $1 \leq M \leq N$
- $0 \leq u, v < N$
- The graph has no self-loops or multiple edges.

---

## Input Format

* The first line contains a single integer $T$ — the number of test cases.
* For each test case:

  * The first line contains three integers: $N$, $M$, and $E$.
  * The next $E$ lines each contain two integers $u$ and $v$ representing an edge between vertex $u$ and vertex $v$.

---

## Output Format

* For each test case, print $true$ if the graph can be coloured with at most $M$ colours, or $false$ otherwise.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $1 \leq M \leq N\cdot(N-1)/2$
- $1 \leq u_i, v_i \leq N$
- $u_i \neq v_i$ for each $1 \leq i \leq M$.
- The sum of $N$ over all test cases won't exceed $100$.

---

## Examples

**Example 1**

**Input**

```text
2
4 3 5
0 1
1 2
2 3
3 0
0 2
3 2 3
0 1
1 2
0 2
```

**Output**

```text
true
false
```

**Explanation**

**Test Case 1:**
With 3 colors, one possible coloring is:

* Vertex 0 -> Color 1
* Vertex 1 -> Color 2
* Vertex 2 -> Color 3
* Vertex 3 -> Color 2

All adjacent vertices have different colors. Hence, output is `true`.

**Test Case 2:**
With 2 colors, the triangle graph cannot be colored without two adjacent vertices sharing a color. Hence, output is `false`.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 3 5
0 1
1 2
2 3
3 0
```

**Output for this case**

```text
true
```



#### Test case 2

**Input for this case**

```text
0 2
3 2 3
0 1
1 2
0 2
```

**Output for this case**

```text
false
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### Problem Understanding

The problem requires determining whether a given undirected graph can be colored using **at most M colors** such that no two adjacent vertices share the same color.

Key points to note:

* A valid coloring means **every edge connects vertices with different colors**.
* We need to check **possibility**, not the exact coloring.
* Graph size is small: **1 ≤ N ≤ 20**, so backtracking approaches are feasible.

---

### Constraints and Observations

* **Number of vertices (N):** 1 to 20
* **Number of edges (E):** 1 to N * (N-1)/2
* **Number of colors (M):** 1 to N
* Graph has **no self-loops** or multiple edges.

Observations:

1. If `M ≥ N`, the graph can always be colored because every vertex can get a unique color.
2. A **complete graph** with `N` vertices requires exactly `N` colors.
3. Small graphs allow **exhaustive search (backtracking)** without performance issues.
4. Odd cycles require at least 3 colors.

---

### Approach

#### 1. Backtracking (Recursive)

1. **Assign colors to vertices one by one:**

   * Start with the first vertex and try each color from 1 to M.
   * For each color, check if it is **safe** (no adjacent vertex has the same color).
   * If safe, assign the color and move to the next vertex recursively.

2. **Base case:**

   * If all vertices are assigned a color, return **true**.

3. **Backtrack:**

   * If a color assignment leads to a dead end, reset it and try the next color.
   * If no color works for a vertex, return **false**.

#### 2. Checking Safety

* To check if a color can be assigned to a vertex:

  * Iterate over all adjacent vertices.
  * If any neighbor has the same color, it is **not safe**.
  * Otherwise, assign the color.

#### 3. Complexity

* Worst-case complexity: **O(M^N)**

  * Each vertex can have M choices.
  * For N vertices, we explore M^N combinations in the worst case.
* Practical performance:

  * Since N ≤ 20 and M ≤ N, backtracking with pruning works efficiently.
  * The "isSafe" check prunes invalid branches early.

---

### Example Walkthrough

**Example 1:**

```
N = 4, M = 3, Edges = [(0,1), (1,2), (2,3), (3,0), (0,2)]
```

* Start coloring vertex 0 with color 1.
* Vertex 1 can be color 2.
* Vertex 2 can be color 3.
* Vertex 3 can be color 2.
* All vertices colored safely → return **true**.

**Example 2:**

```
N = 3, M = 2, Edges = [(0,1), (1,2), (0,2)]
```

* Try coloring vertex 0 with color 1.
* Vertex 1 can be color 2.
* Vertex 2 is adjacent to both 0 and 1, cannot use color 1 or 2.
* No valid coloring → return **false**.

---

### Alternative Approaches

1. **Graph Reduction / Heuristics:**

   * For larger graphs, one could use heuristics like **DSATUR** (degree of saturation) to select vertices with the most constraints first.

2. **Bitmasking + DP:**

   * For small N, a **bitmask dynamic programming** approach is possible but more complex than simple backtracking.

3. **Constraint Satisfaction Problem (CSP) Solvers:**

   * M-Coloring is a classical CSP; generic solvers like backtracking with forward checking can be used.

---

### Tips for Implementation

* Represent the graph as **adjacency list** or **adjacency matrix**.
* Use **0 for uncolored** and 1..M for assigned colors.
* Always **backtrack** after exploring a branch.
* For multiple test cases, ensure **graph and color arrays are reinitialized**.

---

### Edge Cases

1. **Single vertex:** N = 1, M = 1 → always true.
2. **No edges:** Any M ≥ 1 → always true.
3. **Complete graph:** N vertices require N colors.
4. **Insufficient colors:** Odd cycles with M < 3 → false.
5. **Disconnected graphs:** Color each connected component independently.

---

### Summary

* **Type:** Graph coloring / backtracking problem.
* **Constraints:** Small N allows exhaustive search.
* **Approach:** Recursive backtracking with safety check.
* **Edge cases:** Single vertex, complete graph, disconnected graph, insufficient colors.
* **Complexity:** Exponential in N but feasible for N ≤ 20.

This approach ensures **all cases are handled correctly**, from trivial to worst-case fully connected graphs.

</details>
