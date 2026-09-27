# Guided Example: Shortest Distance from All Buildings

We trace the step-by-step multi-source building breadth-first search (BFS), reachability count tracking (`cnt[x][y] == total`), cumulative shortest distance accumulation (`dist[x][y] += d`), obstacle avoidance, and global minimum distance extraction on representative grid instances:

- **Input:**
  $$
  \text{grid} = \begin{bmatrix}
  1 & 0 & 2 & 0 & 1 \\
  0 & 0 & 0 & 0 & 0 \\
  0 & 0 & 1 & 0 & 0
  \end{bmatrix}
  $$
- **Required output:** $7$
  - Three buildings located at $(0, 0)$, $(0, 4)$, and $(2, 2)$ ($\text{total} = 3$)
  - One obstacle located at $(0, 2)$
  - Optimal house location on empty land: cell $(1, 2)$
    - Distance from Building $(0, 0) \to (1, 2)$ is $3$
    - Distance from Building $(0, 4) \to (1, 2)$ is $3$
    - Distance from Building $(2, 2) \to (1, 2)$ is $1$
    - Cumulative distance sum $= 3 + 3 + 1 = \mathbf{7}$
- **Disconnected Land / Obstacle Enclosure:** If any building is completely walled off, no empty cell reaches $\text{cnt} == \text{total}$, correctly returning $-1$
- **No Empty Land Available:** If the grid contains only buildings and obstacles with zero empty cells, returns $-1$
- **Single Building Instance:** With only one building, any adjacent empty cell achieves minimum distance $1$

This instance demonstrates reversing shortest path search directions by launching BFS from $B$ buildings rather than all $O(M N)$ empty cells, formalizes the distinction between reachability counting and distance accumulation, proves why obstacles require true BFS pathfinding rather than Manhattan approximations, and operates in $O(B \cdot M N)$ time and $O(M N)$ space.

---

## 1. Instance & Teaching Goal

Given an $M \times N = 3 \times 5$ grid where $0 = \text{empty land}$, $1 = \text{building}$, and $2 = \text{obstacle}$:
Find an empty land cell $(r, c)$ to build a house that minimizes the total travel distance to **all** buildings:
$$
\text{Total Distance}(r, c) = \sum_{b \in \text{Buildings}} \text{dist}((r, c), b)
$$
Movement is restricted to 4 cardinal directions (up, down, left, right) through empty land ($0$). Neither buildings ($1$) nor obstacles ($2$) can be traversed.

```text
Grid Layout:
[ B1,  .,  X,  ., B2 ]
[  .,  .,  H,  .,  . ]
[  .,  ., B3,  .,  . ]

B1 = (0, 0), B2 = (0, 4), B3 = (2, 2)
X  = (0, 2) (Obstacle)
H  = (1, 2) (Chosen House)

Path from B1 to H: (0,0) -> (1,0) -> (1,1) -> (1,2) [Length 3]
Path from B2 to H: (0,4) -> (1,4) -> (1,3) -> (1,2) [Length 3]
Path from B3 to H: (2,2) -> (1,2)                   [Length 1]
Total Distance: 3 + 3 + 1 = 7
```

### Why Launch BFS from Buildings Instead of Empty Cells?
- In a grid with many empty cells and few buildings ($B \ll M N$), launching BFS from each empty cell takes $O((MN)^2)$.
- Instead, launch BFS **from each of the $B$ buildings**!
  - Because movement is undirected, $\text{dist}(\text{building}, \text{land}) = \text{dist}(\text{land}, \text{building})$.
  - Each building propagates its exact shortest distance to all reachable empty cells in a single $O(M N)$ BFS.
  - Total time drops to $O(B \cdot M N)$.

---

## 2. Conceptual Foundation & Invariants

### State Matrices
1. `cnt[r][c]`: Count of distinct buildings that can reach empty cell $(r, c)$.
2. `dist[r][c]`: Cumulative sum of shortest distances from all buildings that reached $(r, c)$.
3. `total`: Total number of buildings in the grid.

### Single Building BFS Protocol:
When a building at $(i, j)$ is detected:
1. Increment `total += 1`.
2. Initialize BFS queue $q = \text{deque}([(i, j)])$, distance level $d = 0$, and local visited set $vis = \text{set}()$.
3. Level-by-level BFS:
   - Increment $d \mathrel{+}= 1$.
   - For all cells in current level:
     - For each of 4 cardinal neighbors $(x, y)$:
       - If $(x, y)$ is within bounds, $\text{grid}[x][y] == 0$, and $(x, y) \notin vis$:
         - `cnt[x][y] += 1`
         - `dist[x][y] += d`
         - Enqueue $(x, y)$ and add to $vis$.

### Final Optimal Extraction:
Scan all empty cells $(i, j)$ where $\text{grid}[i][j] == 0$:
- If `cnt[i][j] == total`:
  $$
  \text{ans} = \min(\text{ans}, \; \text{dist}[i][j])
  $$
If $\text{ans} == \infty$, return $-1$.

> **Invariant.** An empty cell $(r, c)$ is a valid candidate if and only if $\text{cnt}[r][c] == \text{total}$. For valid candidates, $\text{dist}[r][c]$ equals the exact sum of shortest path distances from all buildings.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on the $3 \times 5$ grid:
Buildings: $B_1(0, 0), B_2(0, 4), B_3(2, 2) \implies \text{total} = 3$.
Obstacle at $(0, 2)$.

---

### Step 1: BFS from Building $B_1$ at $(0, 0)$
- Level $d = 1$: Neighbors of $(0, 0)$ are $(0, 1)$ and $(1, 0)$.
  - $(0, 1): \text{dist} = 1, \text{cnt} = 1$.
  - $(1, 0): \text{dist} = 1, \text{cnt} = 1$.
- Level $d = 2$:
  - From $(0, 1)$: neighbor $(0, 2)$ is an obstacle (blocked!).
  - From $(1, 0)$: neighbor $(1, 1)$ has $\text{dist} = 2, \text{cnt} = 1$.
  - Neighbor $(2, 0)$ has $\text{dist} = 2, \text{cnt} = 1$.
- Level $d = 3$:
  - From $(1, 1)$: neighbor $(1, 2)$ has $\text{dist} = 3, \text{cnt} = 1$.
  - Neighbor $(2, 1)$ has $\text{dist} = 3, \text{cnt} = 1$.
- At candidate cell $(1, 2)$:
  $$
  \text{dist}[1][2] = 3, \quad \text{cnt}[1][2] = 1
  $$

---

### Step 2: BFS from Building $B_2$ at $(0, 4)$
- Level $d = 1$:
  - Neighbors $(0, 3)$ and $(1, 4)$ reached with $d = 1$.
- Level $d = 2$:
  - From $(0, 3)$: neighbor $(0, 2)$ is an obstacle (blocked!).
  - Neighbors $(1, 3)$ and $(2, 4)$ reached with $d = 2$.
- Level $d = 3$:
  - From $(1, 3)$: neighbor $(1, 2)$ reached!
  - Neighbor $(2, 3)$ reached.
- Update candidate cell $(1, 2)$:
  $$
  \text{dist}[1][2] \leftarrow 3 + 3 = 6, \quad \text{cnt}[1][2] \leftarrow 1 + 1 = 2
  $$

---

### Step 3: BFS from Building $B_3$ at $(2, 2)$
- Level $d = 1$:
  - Neighbors of $(2, 2)$ are $(1, 2)$, $(2, 1)$, and $(2, 3)$.
  - Candidate cell $(1, 2)$ is directly adjacent!
  - Distance: $d = 1$.
- Update candidate cell $(1, 2)$:
  $$
  \text{dist}[1][2] \leftarrow 6 + 1 = \mathbf{7}, \quad \text{cnt}[1][2] \leftarrow 2 + 1 = \mathbf{3}
  $$

---

### Step 4: Candidate Inspection & Global Minimum
All 3 building BFS passes complete ($\text{total} = 3$).
Inspect valid empty cells with $\text{cnt} == 3$:
- Cell $(1, 2)$: $\text{cnt} = 3, \; \text{dist} = 3 + 3 + 1 = \mathbf{7}$.
- Cell $(1, 1)$: $\text{cnt} = 3, \; \text{dist} = 2 + 4 + 2 = 8$.
- Cell $(1, 3)$: $\text{cnt} = 3, \; \text{dist} = 4 + 2 + 2 = 8$.
- Cell $(0, 1)$: $\text{cnt} = 3, \; \text{dist} = 1 + 5 + 3 = 9$ (detours around obstacle).

Minimum distance among all valid cells:
$$
\text{ans} = \mathbf{7}
$$

---

## 4. Complete Execution Trace

```text
Grid (3x5):
[ 1, 0, 2, 0, 1 ]
[ 0, 0, 0, 0, 0 ]
[ 0, 0, 1, 0, 0 ]

Buildings: (0, 0), (0, 4), (2, 2) -> total = 3

Building (0, 0) BFS: dist to (1, 2) = 3, cnt[1][2] = 1
Building (0, 4) BFS: dist to (1, 2) = 3, cnt[1][2] = 2
Building (2, 2) BFS: dist to (1, 2) = 1, cnt[1][2] = 3

Cell (1, 2) reached by all 3 buildings!
Total Distance = 3 + 3 + 1 = 7

Global Minimum = 7
```

| Candidate Cell $(r, c)$ | Dist from $B_1(0, 0)$ | Dist from $B_2(0, 4)$ | Dist from $B_3(2, 2)$ | Total Buildings Reached (`cnt`) | Cumulative Distance (`dist`) | Valid House Candidate? |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **$(1, 2)$** | **3** | **3** | **1** | **3 (All)** | **7** | **Yes (Optimal)** |
| $(1, 1)$ | 2 | 4 | 2 | 3 (All) | 8 | Yes |
| $(1, 3)$ | 4 | 2 | 2 | 3 (All) | 8 | Yes |
| $(0, 1)$ | 1 | 5 (detour) | 3 | 3 (All) | 9 | Yes |
| $(0, 3)$ | 5 (detour) | 1 | 3 | 3 (All) | 9 | Yes |
| $(2, 0)$ | 2 | 6 | 3 | 3 (All) | 11 | Yes |

---

## 5. Algorithmic Correctness

**Soundness.** BFS on an unweighted grid discovers cells in order of strictly increasing shortest path distances. Because paths between empty cells are reversible, the distance from building $B$ to empty cell $E$ exactly equals the distance from $E$ to $B$. Accumulating $d$ across all building runs guarantees that `dist[r][c]` equals the exact total travel distance to all reached buildings.

**Completeness.** A house is viable if and only if it can reach every single building. Requiring $\text{cnt}[r][c] == \text{total}$ strictly rejects any cell isolated by obstacles or buildings from one or more structures. Testing all cells with $\text{cnt} == \text{total}$ guarantees finding the global minimum without omission.

---

## 6. Traps This Instance Exposes

- **Manhattan Distance vs True Pathfinding:** Manhattan distance assumes an unobstructed grid. Obstacles (like cell $(0, 2)$) force paths to detour around them (e.g. from $(0, 1)$ to $(0, 4)$ costs 5 steps, not $|0-0| + |1-4| = 3$). BFS is mandatory.
- **Universal Reachability Invariant:** An empty cell might have a small distance sum from 2 buildings but be completely unreachable from a 3rd building. Checking $\text{cnt}[r][c] == \text{total}$ prevents selecting disconnected cells.
- **Reusing Visited Across Buildings:** The `vis` set must be freshly instantiated for each building BFS. Reusing a global visited set would prevent subsequent buildings from traversing cells already visited by earlier searches.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(B \cdot M N)$, where $B$ is the number of buildings and $M, N$ are grid dimensions. In the worst case $B \le M N$, but typically $B \ll M N$. Each building BFS visits each cell at most once.
- **Auxiliary Space Complexity:** $O(M N)$ auxiliary memory to store `cnt`, `dist`, the BFS queue, and the visited set `vis`.
