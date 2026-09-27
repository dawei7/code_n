# Guided Example: Cut Off Trees for Golf Event

We trace the step-by-step tree coordinate collection and height-based sort ordering ($\text{sort by } height$), sequential waypoint routing ($(\text{curr}_x, \text{curr}_y) \to (\text{target}_x, \text{target}_y)$), shortest path breadth-first search / A* with Manhattan distance heuristic ($h(c, d) = |c - x| + |d - y|$), obstacle circumvention ($grid \ne 0$), cumulative walking step aggregation, and reachability validation on representative forest grid matrices:

- **Input:**
  $$
  forest = \begin{bmatrix}
  1 & 2 & 3 \\
  0 & 0 & 4 \\
  7 & 6 & 5
  \end{bmatrix}
  $$
- **Required output:** `6`
  - Terrain rules:
    - Cell value $0$: Impassable obstacle (cannot be traversed).
    - Cell value $1$: Empty grass (walkable).
    - Cell value $> 1$: A tree of specified height (walkable at any time, but must be cut in order).
    - Starting point: Cell $(0, 0)$ (top-left corner).
    - Cutting constraint: Trees must be visited and cut down in **strictly ascending order of their heights** (from the lowest tree to the tallest).
    - Objective: Calculate the minimum total steps required to cut down every tree. If any required tree cannot be reached, return $-1$.
- **Sequential Waypoint Decomposition & Shortest Path Invariant:**
  - **Sequential Independence:**
    - Because the order of cuts is strictly fixed by tree heights, the global optimization problem decouples into a series of **independent point-to-point shortest path queries**:
      $$
      \text{Start } (0, 0) \to T_1 \to T_2 \to \dots \to T_k
      $$
    - The minimum total steps is simply the sum of the shortest paths connecting consecutive waypoints:
      $$
      \text{Total Steps} = \sum_{p=0}^{k-1} \text{dist}(W_p, \; W_{p+1}) \quad \text{where } W_0 = (0, 0)
      $$
  - **Point-to-Point Search (A* with Manhattan Heuristic):**
    - To find the shortest path between $(i, j)$ and target $(x, y)$:
      - Allowed moves: Up, Down, Left, Right into cells with value $> 0$.
      - Admissible Manhattan heuristic:
        $$
        h(i, j, x, y) = |i - x| + |j - y|
        $$
      - If BFS exhausts all reachable cells without reaching $(x, y)$, the target is unreachable $\implies$ return **`-1`**.
- **Step-by-Step Worked Execution Trace on the $3 \times 3$ Forest:**
  - **Step 1: Identify and Sort All Trees ($forest[i][j] > 1$):**
    - Cell $(0, 1)$: Height $2$
    - Cell $(0, 2)$: Height $3$
    - Cell $(1, 2)$: Height $4$
    - Cell $(2, 2)$: Height $5$
    - Cell $(2, 1)$: Height $6$
    - Cell $(2, 0)$: Height $7$
    - Sorted waypoint sequence:
      $$
      \text{Trees} = [ (2, 0, 1), \; (3, 0, 2), \; (4, 1, 2), \; (5, 2, 2), \; (6, 2, 1), \; (7, 2, 0) ]
      $$
  - **Step 2: Traverse from Start $(0, 0)$ to Waypoint 1 $(0, 1)$ [Height 2]:**
    - From $(0, 0)$ to $(0, 1)$:
    - Move Right: $(0, 0) \to (0, 1)$.
    - Steps: $\mathbf{1}$.
    - Cut tree of height 2.
    - Total steps: $ans \leftarrow 0 + 1 = \mathbf{1}$. Current pos: $(0, 1)$.
  - **Step 3: Traverse to Waypoint 2 $(0, 2)$ [Height 3]:**
    - From $(0, 1)$ to $(0, 2)$:
    - Move Right: $(0, 1) \to (0, 2)$.
    - Steps: $\mathbf{1}$.
    - Cut tree of height 3.
    - Total steps: $ans \leftarrow 1 + 1 = \mathbf{2}$. Current pos: $(0, 2)$.
  - **Step 4: Traverse to Waypoint 3 $(1, 2)$ [Height 4]:**
    - From $(0, 2)$ to $(1, 2)$:
    - Move Down: $(0, 2) \to (1, 2)$.
    - Steps: $\mathbf{1}$.
    - Cut tree of height 4.
    - Total steps: $ans \leftarrow 2 + 1 = \mathbf{3}$. Current pos: $(1, 2)$.
  - **Step 5: Traverse to Waypoint 4 $(2, 2)$ [Height 5]:**
    - From $(1, 2)$ to $(2, 2)$:
    - Move Down: $(1, 2) \to (2, 2)$.
    - Steps: $\mathbf{1}$.
    - Cut tree of height 5.
    - Total steps: $ans \leftarrow 3 + 1 = \mathbf{4}$. Current pos: $(2, 2)$.
  - **Step 6: Traverse to Waypoint 5 $(2, 1)$ [Height 6]:**
    - From $(2, 2)$ to $(2, 1)$:
    - Move Left: $(2, 2) \to (2, 1)$.
    - Steps: $\mathbf{1}$.
    - Cut tree of height 6.
    - Total steps: $ans \leftarrow 4 + 1 = \mathbf{5}$. Current pos: $(2, 1)$.
  - **Step 7: Traverse to Waypoint 6 $(2, 0)$ [Height 7]:**
    - From $(2, 1)$ to $(2, 0)$:
    - Move Left: $(2, 1) \to (2, 0)$.
    - Steps: $\mathbf{1}$.
    - Cut tree of height 7.
    - Total steps: $ans \leftarrow 5 + 1 = \mathbf{6}$. Current pos: $(2, 0)$.
  - **Step 8: Output:**
    - All trees cut down in strictly increasing order of height.
    - Total walking distance:
      $$
      ans = \mathbf{6}
      $$
- **Blocked Obstacle Instance ($forest = [[1, 2, 3], [0, 0, 0], [7, 6, 5]]$):**
  - Row 1 is a solid barrier of zeros `[0, 0, 0]`.
  - Waypoint 4 (tree 4 is missing, next is 5 at $(2, 2)$) cannot be reached from row 0.
  - BFS returns $-1 \implies$ Entire algorithm immediately outputs **`-1`**.
- **Starting on a Tree ($forest[0][0] > 1$):**
  - If the lowest tree is already at $(0, 0)$, distance to cut it is $0$ steps.

This instance demonstrates metric waypoint sequence decomposition on constrained grid graphs, mathematically proves why fixed-order path finding reduces to iterated unweighted shortest-path queries, and derives $O(T \cdot M \cdot N)$ runtime and $O(M \cdot N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a forest grid with walkable trees ($> 1$), grass ($1$), and obstacles ($0$):
Cut down all trees in order from **shortest to tallest**.
Find the **minimum walking steps** starting at $(0, 0)$. If impossible, return $-1$.

```text
forest:
  1  2  3
  0  0  4
  7  6  5

Trees in order of height:
  Tree 2 at (0, 1) -> from (0, 0): 1 step
  Tree 3 at (0, 2) -> from (0, 1): 1 step
  Tree 4 at (1, 2) -> from (0, 2): 1 step
  Tree 5 at (2, 2) -> from (1, 2): 1 step
  Tree 6 at (2, 1) -> from (2, 2): 1 step
  Tree 7 at (2, 0) -> from (2, 1): 1 step

Total Steps = 1 + 1 + 1 + 1 + 1 + 1 = 6
```

### The Invariant of Fixed Waypoint Order
- The problem is NOT a Traveling Salesperson Problem (NP-hard), because the visitor sequence is **strictly deterministic**:
  $$
  (0, 0) \to W_1 \to W_2 \to \dots \to W_T
  $$
- The overall distance is simply the sum of $T$ independent shortest-path queries on an unweighted grid.

---

## 2. Conceptual Foundation & Invariants

### 1. The Global Waypoint Sum:
$$
ans = \sum_{p=0}^{T-1} \text{BFS}(W_p, \; W_{p+1})
$$
If any $\text{BFS}(W_p, W_{p+1}) == -1 \implies \text{return } -1$.

### 2. A* Manhattan Lower Bound:
For search from $(i, j)$ to $(x, y)$:
$$
f(i, j) = g(i, j) + |i - x| + |j - y|
$$
Because the heuristic is consistent and admissible, A* finds the true shortest path with minimal node expansions.

> **Deterministic Waypoint Splitting Invariant.** Imposing a total order on the target set $T$ decomposes graph path optimization into $T$ orthogonal sub-queries whose optimal substructure is independent and globally additive.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Waypoint Sequence
- $W_0 = (0, 0)$.
- $W_1 = (0, 1)$ [h=2].
- $W_2 = (0, 2)$ [h=3].
- $W_3 = (1, 2)$ [h=4].
- $W_4 = (2, 2)$ [h=5].
- $W_5 = (2, 1)$ [h=6].
- $W_6 = (2, 0)$ [h=7].

---

### Step 2: Segment Distances
- $(0, 0) \to (0, 1) = 1$.
- $(0, 1) \to (0, 2) = 1$.
- $(0, 2) \to (1, 2) = 1$.
- $(1, 2) \to (2, 2) = 1$.
- $(2, 2) \to (2, 1) = 1$.
- $(2, 1) \to (2, 0) = 1$.

---

### Step 3: Sum
$$
1 + 1 + 1 + 1 + 1 + 1 = \mathbf{6}
$$

---

## 4. Complete Execution Trace

| Segment Step | Current Start $(i, j)$ | Target Waypoint $(x, y)$ | Target Tree Height | Route Taken | Segment Steps | Cumulative Walking Steps |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | $(0, 0)$ | $(0, 1)$ | $2$ | Right | $1$ | $1$ |
| $2$ | $(0, 1)$ | $(0, 2)$ | $3$ | Right | $1$ | $2$ |
| $3$ | $(0, 2)$ | $(1, 2)$ | $4$ | Down | $1$ | $3$ |
| $4$ | $(1, 2)$ | $(2, 2)$ | $5$ | Down | $1$ | $4$ |
| $5$ | $(2, 2)$ | $(2, 1)$ | $6$ | Left | $1$ | $5$ |
| **$6$** | **$(2, 1)$** | **$(2, 0)$** | **$7$** | **Left** | **$1$** | **`6`** |

---

## 5. Boundary Cases & Failure Modes

- **Unreachable Tree:** Target surrounded by 0s $\implies$ BFS returns $-1 \implies$ global output is $-1$.
- **Starting Cell is Blocked ($forest[0][0] == 0$):** Cannot even move $\implies -1$.
- **Starting Cell Has Lowest Tree ($forest[0][0] = \min(trees)$):** First segment takes 0 steps.
- **Tree Count $T = 1$:** Single BFS from $(0, 0)$ to the sole tree.

---

## 6. Traps & Common Anti-Patterns

- **Treating Uncut Trees as Obstacles:** You can freely walk through a tree without cutting it yet! Only cells with value $0$ are obstacles.
- **Re-Sorting After Every Cut:** Tree heights are fixed and distinct; sorting the list once at the beginning gives the exact visit order.
- **Using Plain Dijkstra Without Manhattan Heuristic:** A* with Manhattan distance dramatically reduces grid states explored compared to unguided Dijkstra.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Sorting $T$ trees: $\mathcal{O}(T \log T)$.
  - Point-to-point BFS / A* takes at most $\mathcal{O}(M \cdot N)$ per segment.
  - Number of segments is $T \le M \cdot N$.
  - Total Time: $\mathcal{O}(T \cdot M \cdot N) \le \mathcal{O}((MN)^2)$.
  - For $M = N = 50$, executes well within the 1-second time limit.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(M \cdot N)$ space for the BFS queue and distance table.
