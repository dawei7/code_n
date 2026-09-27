# Guided Example: Walls and Gates

We trace the step-by-step multi-source breadth-first search (BFS) propagation, simultaneous frontier wave expansion from all gates (value $0$), in-place $\text{INF}$ distance overwriting, and obstacle avoidance (walls $-1$) on representative grid layouts:

- **Input:**
  $$
  \text{rooms} = \begin{bmatrix}
  \text{INF} & -1 & 0 & \text{INF} \\
  \text{INF} & \text{INF} & \text{INF} & -1 \\
  \text{INF} & -1 & \text{INF} & -1 \\
  0 & -1 & \text{INF} & \text{INF}
  \end{bmatrix} \quad (\text{where } \text{INF} = 2^{31} - 1 = 2147483647)
  $$
- **Required output:**
  $$
  \begin{bmatrix}
  3 & -1 & 0 & 1 \\
  2 & 2 & 1 & -1 \\
  1 & -1 & 2 & -1 \\
  0 & -1 & 3 & 4
  \end{bmatrix}
  $$
- **Unreachable Room Guard:** Rooms completely enclosed by walls retain their initial $\text{INF}$ value
- **No Gates Boundary:** If the grid contains no gates, the queue remains empty and all $\text{INF}$ rooms stay untouched
- **Single Wall Base Case:** $\text{rooms} = [[-1]] \implies [[-1]]$

This instance demonstrates multi-source BFS on unweighted grids, mathematically proves why initializing the queue with all gates simultaneously guarantees that the first arrival at any room is its globally minimal distance, eliminates the need for a separate visited set by reusing $\text{rooms}[r][c] == \text{INF}$ as the unvisited predicate, and executes in strictly $O(M \times N)$ linear time and space.

---

## 1. Instance & Teaching Goal

Given an $m \times n$ grid of rooms ($4 \times 4$):
- `-1`: Wall or obstacle (cannot pass through).
- `0`: Gate (distance to nearest gate is $0$).
- `INF` ($2147483647$): Empty room.

Calculate the shortest distance from each empty room to its nearest gate.

```text
Initial grid:
INF  -1    0  INF
INF  INF  INF  -1
INF  -1   INF  -1
  0  -1   INF  INF

Two gates: (0, 2) and (3, 0).
Distances radiate outward like ripples in a pond.
```

### Why Single-Source Search Fails
- Running BFS from each empty room toward the nearest gate would repeat grid traversals $O(M N)$ times, taking $O((M N)^2)$ time.
- Running separate BFS runs from each gate would overwrite cells and require repeated distance comparisons.
- **Multi-Source BFS:** We enqueue all gates simultaneously at distance 0. The search expands in concentric frontiers (distance 1, distance 2, $\dots$). The first wave to touch an empty room delivers its globally minimal shortest path!

---

## 2. Conceptual Foundation & Invariants

### Multi-Source BFS Protocol
1. **Queue Initialization (Layer 0):**
   Scan the entire grid. For every cell $(r, c)$ where $\text{rooms}[r][c] == 0$:
   Enqueue $(r, c)$.
2. **Frontier Expansion:**
   While queue is non-empty:
   Pop $(r, c)$.
   For each cardinal neighbor $(nr, nc) \in \{(r+1, c), (r-1, c), (r, c+1), (r, c-1)\}$:
   - Check grid boundaries: $0 \le nr < m$ and $0 \le nc < n$.
   - Check unvisited status:
     $$
     \text{rooms}[nr][nc] == \text{INF}
     $$
     *(Walls $-1$, gates $0$, and already-visited rooms $< \text{INF}$ are automatically skipped!)*
   - When $\text{rooms}[nr][nc] == \text{INF}$:
     $$
     \text{rooms}[nr][nc] \leftarrow \text{rooms}[r][c] + 1
     $$
     Enqueue $(nr, nc)$.

> **Invariant.** At any BFS step, the queue contains cells sorted monotonically by distance. When cell $(nr, nc)$ is first reached from $(r, c)$, $\text{rooms}[r][c] + 1$ is the globally minimal unweighted shortest distance from any gate to $(nr, nc)$.

### Why One Predicate Replaces the Visited Set

Every value a neighbor can hold when it is inspected falls into exactly one class, and the single test $\text{rooms}[nr][nc] == \text{INF}$ answers all four correctly:

| Value read at $(nr, nc)$ | Cell class | Passes the $\text{INF}$ test? | Action taken | Why the action is right |
|:---:|:---|:---:|:---|:---|
| $2147483647$ | Unfilled room | Yes | Write $\text{rooms}[r][c] + 1$ and enqueue | It has never been reached, so this first arrival is its shortest distance |
| $-1$ | Wall | No | Skip | Walls cannot be traversed and must survive the pass unchanged |
| $0$ | Gate | No | Skip | Its distance is already the minimum possible, so overwriting would corrupt a source |
| $1 \dots d$ | Room settled by an earlier or equal round | No | Skip | Its stored value is already minimal, and revisiting it would only re-enqueue settled work |

Because the test is a value predicate rather than an identity test, it doubles as the open-room check and the visited check, and no second matrix is allocated.

---

## 3. Step-by-Step Worked Execution

We trace the multi-source BFS on the $4 \times 4$ grid:
Gates located at $(0, 2)$ and $(3, 0)$.

---

### Step 1: Queue Seeding ($d = 0$)
Queue contains:
$$
Q = [(0, 2), \; (3, 0)]
$$

---

### Step 2: Expand Layer 0 ($d = 0 \to d = 1$)
- **Pop $(0, 2)$ (Gate 1):**
  - Left $(0, 1) = -1$ (Wall, skip).
  - Down $(1, 2) = \text{INF} \implies \text{rooms}[1][2] = 0 + 1 = \mathbf{1}$. Enqueue $(1, 2)$.
  - Right $(0, 3) = \text{INF} \implies \text{rooms}[0][3] = 0 + 1 = \mathbf{1}$. Enqueue $(0, 3)$.
- **Pop $(3, 0)$ (Gate 2):**
  - Up $(2, 0) = \text{INF} \implies \text{rooms}[2][0] = 0 + 1 = \mathbf{1}$. Enqueue $(2, 0)$.
  - Right $(3, 1) = -1$ (Wall, skip).

Queue for Layer 1:
$$
Q = [(1, 2), \; (0, 3), \; (2, 0)]
$$

---

### Step 3: Expand Layer 1 ($d = 1 \to d = 2$)
- **Pop $(1, 2)$ (Distance 1):**
  - Up $(0, 2) = 0$ (Gate, skip).
  - Down $(2, 2) = \text{INF} \implies \text{rooms}[2][2] = 1 + 1 = \mathbf{2}$. Enqueue $(2, 2)$.
  - Left $(1, 1) = \text{INF} \implies \text{rooms}[1][1] = 1 + 1 = \mathbf{2}$. Enqueue $(1, 1)$.
  - Right $(1, 3) = -1$ (Wall, skip).
- **Pop $(0, 3)$ (Distance 1):**
  - Left $(0, 2) = 0$ (Gate, skip).
  - Down $(1, 3) = -1$ (Wall, skip).
- **Pop $(2, 0)$ (Distance 1):**
  - Down $(3, 0) = 0$ (Gate, skip).
  - Up $(1, 0) = \text{INF} \implies \text{rooms}[1][0] = 1 + 1 = \mathbf{2}$. Enqueue $(1, 0)$.
  - Right $(2, 1) = -1$ (Wall, skip).

Queue for Layer 2:
$$
Q = [(2, 2), \; (1, 1), \; (1, 0)]
$$

---

### Step 4: Expand Layer 2 ($d = 2 \to d = 3$)
- **Pop $(2, 2)$ (Distance 2):**
  - Down $(3, 2) = \text{INF} \implies \text{rooms}[3][2] = 2 + 1 = \mathbf{3}$. Enqueue $(3, 2)$.
  - Right $(2, 3) = -1$ (Wall, skip).
- **Pop $(1, 1)$ (Distance 2):**
  - Up $(0, 1) = -1$ (Wall, skip).
  - Down $(2, 1) = -1$ (Wall, skip).
  - Left $(1, 0) = 2$ (Already visited).
  - Right $(1, 2) = 1$ (Already visited).
- **Pop $(1, 0)$ (Distance 2):**
  - Up $(0, 0) = \text{INF} \implies \text{rooms}[0][0] = 2 + 1 = \mathbf{3}$. Enqueue $(0, 0)$.
  - Down $(2, 0) = 1$ (Already visited).
  - Right $(1, 1) = 2$ (Already visited).

Queue for Layer 3:
$$
Q = [(3, 2), \; (0, 0)]
$$

---

### Step 5: Expand Layer 3 ($d = 3 \to d = 4$)
- **Pop $(3, 2)$ (Distance 3):**
  - Right $(3, 3) = \text{INF} \implies \text{rooms}[3][3] = 3 + 1 = \mathbf{4}$. Enqueue $(3, 3)$.
  - Left $(3, 1) = -1$ (Wall, skip).
  - Up $(2, 2) = 2$ (Already visited).
- **Pop $(0, 0)$ (Distance 3):**
  - Down $(1, 0) = 2$ (Already visited).
  - Right $(0, 1) = -1$ (Wall, skip).

---

### Step 6: Expand Layer 4 & Termination
- **Pop $(3, 3)$ (Distance 4):**
  - Up $(2, 3) = -1$ (Wall, skip).
  - Left $(3, 2) = 3$ (Already visited).
- Queue is now empty. Multi-source BFS terminates.

Final grid:
$$
\begin{bmatrix}
3 & -1 & 0 & 1 \\
2 & 2 & 1 & -1 \\
1 & -1 & 2 & -1 \\
0 & -1 & 3 & 4
\end{bmatrix}
$$

---

## 4. Complete Execution Trace

```text
Initial Gates: (0, 2), (3, 0)

Distance 0:
  (0, 2) -> sets (1, 2)=1, (0, 3)=1
  (3, 0) -> sets (2, 0)=1

Distance 1:
  (1, 2) -> sets (2, 2)=2, (1, 1)=2
  (0, 3) -> no open neighbors
  (2, 0) -> sets (1, 0)=2

Distance 2:
  (2, 2) -> sets (3, 2)=3
  (1, 1) -> all neighbors blocked/visited
  (1, 0) -> sets (0, 0)=3

Distance 3:
  (3, 2) -> sets (3, 3)=4
  (0, 0) -> no open neighbors

Distance 4:
  (3, 3) -> no open neighbors
Queue empty -> Done!
```

| BFS Wave Layer | Front Node $(r, c)$ | Current Dist | Neighbor $(nr, nc)$ | Previous Value | Updated Value |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **Layer 0** | $(0, 2)$ | 0 | $(1, 2)$ | $\text{INF}$ | **1** |
| | $(0, 2)$ | 0 | $(0, 3)$ | $\text{INF}$ | **1** |
| | $(3, 0)$ | 0 | $(2, 0)$ | $\text{INF}$ | **1** |
| **Layer 1** | $(1, 2)$ | 1 | $(2, 2)$ | $\text{INF}$ | **2** |
| | $(1, 2)$ | 1 | $(1, 1)$ | $\text{INF}$ | **2** |
| | $(2, 0)$ | 1 | $(1, 0)$ | $\text{INF}$ | **2** |
| **Layer 2** | $(2, 2)$ | 2 | $(3, 2)$ | $\text{INF}$ | **3** |
| | $(1, 0)$ | 2 | $(0, 0)$ | $\text{INF}$ | **3** |
| **Layer 3** | $(3, 2)$ | 3 | $(3, 3)$ | $\text{INF}$ | **4** |
| **Layer 4** | $(3, 3)$ | 4 | - | - | - |

The same run viewed as a frontier evolution, which is what makes the "first arrival is minimal" claim checkable: every room leaves the $\text{INF}$ set in the round whose index equals its final distance, and each filled room is owned by a specific gate.

| Expansion round | Queue on entry | Rooms filled in this round | Queue on exit | Rooms still $\text{INF}$ | Owning gate of the filled rooms |
|:---:|:---|:---|:---|:---|:---|
| Seeding | empty | $(0, 2)$ and $(3, 0)$ are gates and already hold $0$ | $(0, 2), \; (3, 0)$ | $(0,0), (0,3), (1,0), (1,1), (1,2), (2,0), (2,2), (3,2), (3,3)$ | the gates themselves |
| $d = 1$ | $(0, 2), \; (3, 0)$ | $(1,2)$ and $(0,3)$ from $(0,2)$; $(2,0)$ from $(3,0)$ | $(1,2), \; (0,3), \; (2,0)$ | $(0,0), (1,0), (1,1), (2,2), (3,2), (3,3)$ | $(0,2)$ for $(1,2)$ and $(0,3)$; $(3,0)$ for $(2,0)$ |
| $d = 2$ | $(1,2), \; (0,3), \; (2,0)$ | $(2,2)$ and $(1,1)$ from $(1,2)$; $(1,0)$ from $(2,0)$ | $(2,2), \; (1,1), \; (1,0)$ | $(0,0), (3,2), (3,3)$ | $(0,2)$ for $(2,2)$ and $(1,1)$; $(3,0)$ for $(1,0)$ |
| $d = 3$ | $(2,2), \; (1,1), \; (1,0)$ | $(3,2)$ from $(2,2)$; $(0,0)$ from $(1,0)$ | $(3,2), \; (0,0)$ | $(3,3)$ | $(0,2)$ for $(3,2)$; $(3,0)$ for $(0,0)$ |
| $d = 4$ | $(3,2), \; (0,0)$ | $(3,3)$ from $(3,2)$ | $(3,3)$ | none | $(0,2)$ |
| $d = 5$ | $(3,3)$ | none: its right and up neighbors are a gate-adjacent filled room and a wall | empty | none | — |

Two entries are decided by walls rather than by straight-line proximity: $(3,2)$ and $(3,3)$ lie at Manhattan distance $2$ and $3$ from the gate at $(3,0)$, but the wall at $(3,1)$ closes that route, so both are instead reached the long way round from $(0,2)$ at distances $3$ and $4$.

---

## 5. Algorithmic Correctness

**Soundness.** In an unweighted graph, standard BFS guarantees that nodes are visited in non-decreasing order of distance from the source set. By initializing the queue with all gates simultaneously (at distance 0), the first time an unvisited room $(\text{rooms}[r][c] == \text{INF})$ is reached, the path length from the originating gate is guaranteed to be minimal.

**Completeness.** Every reachable empty room is connected via some path of open rooms to at least one gate. The BFS frontier expands exhaustively across all connected components, ensuring every reachable room receives its correct shortest distance. Any room separated by walls remains $\text{INF}$.

---

## 6. Traps This Instance Exposes

- **Single-Source Repeated BFS ($O((MN)^2)$):** Running BFS starting from each empty room leads to massive re-computation and causes Time Limit Exceeded. Reversing search direction to multi-source BFS from gates takes strictly $O(M N)$.
- **Using an Auxiliary Visited Matrix:** A separate `visited` boolean matrix takes unnecessary memory. The condition $\text{rooms}[nr][nc] == \text{INF}$ serves as both the open-room check and the unvisited check.
- **Overwriting Non-INF Cells:** If the neighbor check allows values other than $\text{INF}$ (e.g. `<= rooms[r][c] + 1`), search waves could overwrite walls ($-1$) or gates ($0$). Restricting transitions strictly to $\text{rooms}[nr][nc] == \text{INF}$ preserves all obstacles and gates.

The boundaries that follow are the ones a submitted solution is actually judged on, and each one is decided by a property of the same single predicate:

| Boundary | Instance | What the waves do | Result | Why that result is forced |
|:---|:---|:---|:---|:---|
| The grid holds no gate | $[[\text{INF}]]$ | Seeding finds no cell equal to $0$, so the queue is empty before the first expansion and no neighbor is ever inspected | $[[\text{INF}]]$ | No gate can reach the room, and only $\text{INF}$ cells are ever written, so nothing changes |
| The grid is a single wall | $[[-1]]$ | Same empty seeding; the wall also fails the neighbor predicate | $[[-1]]$ | Walls are read-only under the predicate and are never a source |
| A wall cuts the grid in two | $[[0, -1, \text{INF}]]$ | $(0,0)$ seeds and its right neighbor is a wall, so the expansion stops there forever | $[[0, -1, \text{INF}]]$ | The room beyond lies in a different connected component of open cells, and BFS never widens across a wall |
| Gates exist but no empty room does | $[[0, -1, 0], [-1, -1, -1], [0, -1, 0]]$ | Every neighbor of every gate is a gate or a wall, so all four waves drain without a write | unchanged | The set of $\text{INF}$ cells is empty, so there is nothing to fill |
| One-dimensional row | $[[0, \text{INF}, \text{INF}, \text{INF}]]$ | The lone gate pushes rightward one cell per round | $[[0, 1, 2, 3]]$ | On an unweighted path the round index equals the hop count, and each hop is forced |
| One-dimensional column | $[[\text{INF}], [\text{INF}], [0]]$ | Identical reasoning transposed: the gate ascends | $[[2], [1], [0]]$ | The column is the same path graph with the roles of row and column exchanged |
| Two gates equidistant from a room | $[[0, \text{INF}, 0]]$ | Both gates enter the queue at distance $0$; the middle room is filled by the left wave and is already non-$\text{INF}$ when the right wave arrives | $[[0, 1, 0]]$ | The room's value is the minimum over all gates, and a tie simply means that minimum is attained twice; the first arrival already equals it, so the later skip changes nothing |
| Walls force a detour | $[[0, -1, \text{INF}, \text{INF}], [\text{INF}, -1, \text{INF}, -1], [\text{INF}, \text{INF}, \text{INF}, -1], [\text{INF}, -1, \text{INF}, 0]]$ | The gate at $(0,0)$ feeds the left column downward; the gate at $(3,3)$ feeds upward through $(3,2)$ and $(2,2)$; the wall row blocks every straight connection between the two regions | $[[0, -1, 4, 5], [1, -1, 3, -1], [2, 3, 2, -1], [3, -1, 1, 0]]$ | Each region is served by whichever gate is genuinely closer along open cells, which is not the same as the closer gate by Manhattan distance |
| The minimum dimensions | $1 \le m, n \le 250$ with a single gate | A $1 \times 1$ grid of a gate seeds and drains immediately | $[[0]]$ | The empty queue ends the search before any neighbor test runs |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M \times N)$, where $M$ is the number of rows and $N$ is the number of columns. Initial scanning takes $O(M N)$. In the BFS phase, each room is enqueued at most once when its value transitions from $\text{INF}$ to a finite distance. Each cell inspects 4 orthogonal neighbors, performing $O(1)$ operations. Total runtime is strictly linear in grid size.
- **Auxiliary Space Complexity:** $O(M \times N)$ auxiliary memory to store coordinates in the BFS queue in the worst case (e.g. grid filled entirely with empty rooms).
