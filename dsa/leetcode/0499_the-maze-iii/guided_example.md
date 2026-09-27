# Guided Example: The Maze III

We trace the step-by-step shortest-path raycasting (stopping at walls OR dropping into the hole), distance minimization metric, lexicographical tie-breaking (`'d' < 'l' < 'r' < 'u'`), distance table relaxation ($dist[x][y] > step$), and impossible route rejection on representative maze layouts:

- **Input:**
  - $maze = \begin{bmatrix} 0 & 0 & 0 & 0 & 0 \\ 1 & 1 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & 0 & 0 \end{bmatrix}$
  - Ball position: $ball = [4, 3]$
  - Hole position: $hole = [0, 1]$
- **Required output:** `"lul"`
  - Key Rules:
    1. Distance is the total number of cells traversed by the ball.
    2. The ball stops when it collides with a wall **OR drops into the hole**.
    3. If multiple shortest paths have the same minimum distance, pick the **lexicographically smallest** directional string (`'d' < 'l' < 'r' < 'u'`).
    4. If the hole cannot be reached, return `"impossible"`.
- **Shortest path execution trace:**
  - Initialize tables: $dist[4][3] = 0, \; path[4][3] = \text{""}$, all other cells $\infty$.
  - **From Start $(4, 3)$ with distance $0$:**
    - Test direction `'u'` $(-1, 0)$:
      - Rolls from $(4, 3) \to (3, 3) \to (2, 3) \to (1, 3) \to (0, 3)$ (hits boundary wall).
      - Halts at $(0, 3)$ after $4$ steps.
      - Update: $dist[0][3] = 4, \; path[0][3] = \text{"u"}$.
    - Test direction `'l'` $(0, -1)$:
      - Rolls $(4, 3) \to (4, 2)$ (hits wall at $(4, 1)$).
      - Halts at $(4, 2)$ after $1$ step.
      - Update: $dist[4][2] = 1, \; path[4][2] = \text{"l"}$.
    - Test direction `'r'` $(0, 1)$:
      - Rolls $(4, 3) \to (4, 4)$ (hits right boundary wall).
      - Halts at $(4, 4)$ after $1$ step.
  - **From Resting Position $(4, 2)$ with distance $1$, path `"l"`:**
    - Roll `'u'` $(-1, 0)$:
      - Rolls $(4, 2) \to (3, 2) \to (2, 2) \to (1, 2) \to (0, 2)$ (hits top boundary wall).
      - Halts at $(0, 2)$ after $4$ additional steps (total steps $1 + 4 = 5$).
      - Update: $dist[0][2] = 5, \; path[0][2] = \text{"lu"}$.
  - **From Resting Position $(0, 2)$ with distance $5$, path `"lu"`:**
    - Roll `'l'` $(0, -1)$:
      - Rolls $(0, 2) \to (0, 1)$.
      - Cell $(0, 1)$ is the **HOLE**!
      - **Ball immediately drops into the hole!** Rolling ceases at $(0, 1)$ after $1$ step.
      - Total distance to hole: $5 + 1 = \mathbf{6}$ steps.
      - Path string: $\text{"lu"} + \text{"l"} = \mathbf{\text{"lul"}}$.
      - Update: $dist[0][1] = 6, \; path[0][1] = \text{"lul"}$.
  - Comparison with alternative paths:
    - Other routes require $\ge 6$ steps or have lexicographically larger path strings (e.g. `"ul..."` vs `"lul"`: `'l' < 'u'`).
  - Shortest lexicographical path: **`"lul"`**.
- **Hole Blocked / Trapped Instance:** If hole is enclosed by walls on all sides, ball can never fall in $\implies$ returns **`"impossible"`**.

This instance demonstrates constrained shortest-path search with absorption sink states, mathematically proves how lexicographical tie-breaking enforces unique optimal paths, and derives $O(M \cdot N \cdot \max(M, N))$ runtime and $O(M \cdot N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a 2D maze of size $m \times n$:
- The ball rolls in one of 4 directions: `'u'` (up), `'d'` (down), `'l'` (left), `'r'` (right).
- The ball continues rolling until:
  1. It hits a wall (stops at the last open cell).
  2. Or it reaches the **hole** (drops in immediately, even in mid-roll!).
Find the path to the hole with the **minimum total distance**.
If there are ties in distance, return the **lexicographically smallest** path string.
If unreachable, return `"impossible"`.

```text
Lexicographical Precedence of Directions:
  'd' (down)  <  'l' (left)  <  'r' (right)  <  'u' (up)

Sink State Rule:
  In Maze I/II, the ball only stopped at walls.
  In Maze III, the HOLE acts as an instant sink:
  The moment the ball touches (rh, ch), motion HALTS immediately!
```

---

## 2. Conceptual Foundation & Invariants

### 1. The Absorption Raycast Loop:
From resting position $(i, j)$:
Advance $(x, y)$ in direction $(a, b)$ while:
1. $(x + a, y + b)$ is within bounds.
2. $maze[x + a][y + b] == 0$ (open space).
3. $(x, y)$ has **not yet reached the hole**:
   $$
   x \ne rh \quad \text{or} \quad y \ne ch
   $$
Increment $step \leftarrow step + 1$ for each cell stepped through.

### 2. Dual-Criteria Relaxation Condition:
Let $dist[x][y]$ be the shortest distance found so far, and $path[x][y]$ be its corresponding directional string.
We update $(x, y)$ if:
1. $step < dist[x][y]$ (Strictly fewer steps).
2. OR $step == dist[x][y]$ and $(path[i][j] + d) < path[x][y]$ (Equal steps, but lexicographically smaller string!).
When updated, if $(x, y) \ne hole$, push $(x, y)$ to the BFS queue to propagate improvements.

> **Lexicographical Relaxation Invariant.** Storing the pair $(dist[x][y], path[x][y])$ guarantees that any path reaching the sink state achieves Pareto optimality across both distance and dictionary order.

---

## 3. Step-by-Step Worked Execution

We trace $ball = [4, 3], hole = [0, 1]$:

---

### Step 1: Initialize Distance and Path Tables
- $dist[4][3] = 0$, $path[4][3] = \text{""}$.
- All other cells have $dist = \infty, path = \text{None}$.
- Enqueue $(4, 3)$.

---

### Step 2: Pop $(4, 3)$ ($dist = 0, path = \text{""}$)
Explore 4 directions in alphabetical order:
1. **Direction `'d'` $(1, 0)$:** Blocked by bottom wall.
2. **Direction `'l'` $(0, -1)$:**
   - Rolls $(4, 3) \to (4, 2)$ ($1$ step). Wall at $(4, 1)$.
   - $dist[4][2] > 1 \implies dist[4][2] \leftarrow 1, \; path[4][2] \leftarrow \text{"l"}$.
   - Enqueue $(4, 2)$.
3. **Direction `'r'` $(0, 1)$:**
   - Rolls $(4, 3) \to (4, 4)$ ($1$ step).
   - $dist[4][4] \leftarrow 1, \; path[4][4] \leftarrow \text{"r"}$.
4. **Direction `'u'` $(-1, 0)$:**
   - Rolls $(4, 3) \to (0, 3)$ ($4$ steps).
   - $dist[0][3] \leftarrow 4, \; path[0][3] \leftarrow \text{"u"}$.

---

### Step 3: Pop $(4, 2)$ ($dist = 1, path = \text{"l"}$)
Explore direction `'u'` $(-1, 0)$:
- Rolls $(4, 2) \to (3, 2) \to (2, 2) \to (1, 2) \to (0, 2)$ ($4$ steps).
- Total distance: $1 + 4 = 5$.
- Path string: $\text{"l"} + \text{"u"} = \text{"lu"}$.
- $dist[0][2] \leftarrow 5, \; path[0][2] \leftarrow \text{"lu"}$.
- Enqueue $(0, 2)$.

---

### Step 4: Pop $(0, 2)$ ($dist = 5, path = \text{"lu"}$)
Explore direction `'l'` $(0, -1)$:
- Next cell is $(0, 1)$.
- Cell $(0, 1)$ is the **HOLE**!
- Distance: $5 + 1 = \mathbf{6}$.
- Path: $\text{"lu"} + \text{"l"} = \mathbf{\text{"lul"}}$.
- Since $(0, 1)$ is the hole, motion stops immediately.
- Update hole: $dist[0][1] \leftarrow 6, \; path[0][1] \leftarrow \text{"lul"}$.
- Do not enqueue hole (terminal state).

---

### Step 5: Exhaust Queue
All other alternative routes either take $\ge 6$ steps or have lexicographically larger paths (e.g. path `"u..."` starts with `'u'`, but `'l' < 'u'`).
Result: **`"lul"`**.

---

## 4. Complete Execution Trace

| Queue Step | Current Cell | Direction Chosen | Stepped Cells Traversed | Final Cell $(x, y)$ | Steps Added | Total Distance | Path Recorded |
|:---:|:---:|:---:|:---|:---:|:---:|:---:|:---:|
| **$0$** | $(4, 3)$ (Start) | `'l'` | $(4, 2)$ | $(4, 2)$ | $1$ | $1$ | `"l"` |
| **$0$** | $(4, 3)$ | `'u'` | $(3, 3) \to (0, 3)$ | $(0, 3)$ | $4$ | $4$ | `"u"` |
| **$1$** | $(4, 2)$ | `'u'` | $(3, 2) \to (0, 2)$ | $(0, 2)$ | $4$ | $5$ | `"lu"` |
| **$2$** | **$(0, 2)$** | **`'l'`** | **$(0, 1)$ (Hole!)** | **$(0, 1)$** | **$1$** | **$6$** | **`"lul"`** |
| **Done** | Hole $(0, 1)$ | — | — | — | — | **$6$** | **Result: `"lul"`** |

---

## 5. Boundary Cases & Failure Modes

- **Start in Front of Hole ($ball = [0, 2], hole = [0, 1]$):** 1 step left drops in $\implies \text{"l"}$.
- **Hole Surrounded by Walls:** Queue exhausts with $path[rh][ch] = \text{None} \implies \mathbf{\text{"impossible"}}$.
- **Equal Distance Ties (`"dr"` vs `"rd"`):** String comparison evaluates `'d' < 'r'`, picking `"dr"`.

---

## 6. Traps & Common Anti-Patterns

- **Rolling Past the Hole:** In Maze I, the ball only stopped at walls. If you do not stop immediately upon hitting the hole (`x != rh or y != ch`), the ball will roll through the hole and crash into a wall beyond it, failing the simulation.
- **Priority Queue Without Lexicographical Tie-Breaking:** Comparing only distance allows an inferior lexicographical string with equal distance to overwrite the optimal path. Both distance and string must be compared.
- **Enqueuing the Hole:** The hole is an absorbing sink state. Enqueuing the hole allows the ball to roll *out* of the hole, violating the rules.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - In a grid of size $M \times N$, each cell is updated at most a constant number of times.
  - Each raycast rolls at most $\max(M, N)$ steps.
  - Total Time: $\mathcal{O}(M \cdot N \cdot \max(M, N))$. For a $30 \times 30$ maze, finishes in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(M \cdot N)$ to store distance and string matrices.
