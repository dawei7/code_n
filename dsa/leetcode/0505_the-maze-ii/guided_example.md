# Guided Example: The Maze II

We trace the step-by-step weighted resting-state graph formulation, continuous momentum raycasting (stopping only at boundaries or walls), cumulative travel distance tracking ($k + 1$ per cell traversed), relaxation pruning ($k < dist[x][y]$), and shortest path discovery on representative grid mazes:

- **Input:**
  - $maze = \begin{bmatrix} 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 \\ 1 & 1 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}$
  - Starting position: $start = [0, 4]$
  - Destination position: $destination = [4, 4]$
- **Required output:** `12`
  - Distance definition: Each single grid cell traversed while rolling adds $+1$ unit of distance.
  - Stopping condition: The ball cannot stop voluntarily in open space; it rolls until it hits a wall or boundary. It must come to a complete halt at the destination.
- **Shortest path execution trace:**
  - Initialize distance matrix: $dist[0][4] = 0$, all other cells $\infty$.
  - Enqueue $start = (0, 4)$.
  - **From $(0, 4)$ with distance $0$:**
    - Roll Left $(0, -1)$:
      - Path: $(0, 3)$, blocked by wall at $(0, 2)$.
      - Halts at $(0, 3)$ with distance $1$.
      - $dist[0][3] \leftarrow 1$, enqueue $(0, 3)$.
    - Roll Down $(1, 0)$:
      - Path: $(1, 4) \to (2, 4)$, blocked by wall at $(3, 4)$.
      - Halts at $(2, 4)$ with distance $2$.
      - $dist[2][4] \leftarrow 2$, enqueue $(2, 4)$.
  - **From $(0, 3)$ with distance $1$:**
    - Roll Down $(1, 0)$:
      - Path: $(1, 3) \to (2, 3)$, blocked by wall at $(3, 3)$.
      - Steps: $2$ additional steps. Total distance: $1 + 2 = 3$.
      - $dist[2][3] \leftarrow 3$, enqueue $(2, 3)$.
  - **From $(2, 3)$ with distance $3$:**
    - Roll Left $(0, -1)$:
      - Path: $(2, 2) \to (2, 1) \to (2, 0)$, hits left boundary.
      - Steps: $3$ additional steps. Total distance: $3 + 3 = 6$.
      - $dist[2][0] \leftarrow 6$, enqueue $(2, 0)$.
  - **From $(2, 0)$ with distance $6$:**
    - Roll Up $(-1, 0)$:
      - Path: $(1, 0) \to (0, 0)$, hits top boundary.
      - Steps: $2$. Total distance: $6 + 2 = 8$.
      - $dist[0][0] \leftarrow 8$, enqueue $(0, 0)$.
  - **From $(0, 0)$ with distance $8$:**
    - Roll Right $(0, 1)$:
      - Path: $(0, 1)$, hits wall at $(0, 2)$.
      - Steps: $1$. Total distance: $8 + 1 = 9$.
      - $dist[0][1] \leftarrow 9$, enqueue $(0, 1)$.
  - **From $(0, 1)$ with distance $9$:**
    - Roll Down $(1, 0)$:
      - Path: $(1, 1) \to (2, 1)$, hits wall at $(3, 1)$.
      - Steps: $2$. Total: $9 + 2 = 11$.
      - $dist[2][1] \leftarrow 11$.
  - **Alternative Path reaching lower corridor:**
    - At $(3, 2)$ open channel, rolling Down reaches $(4, 2)$ at distance $6 + 3 = 9$.
    - From resting position $(4, 2)$ with distance $10$:
      - Roll Right $(0, 1)$:
        - Path: $(4, 3) \to (4, 4)$, hits right boundary wall ($y = 5$).
        - Steps: $2$ additional steps.
        - Total accumulated distance: $10 + 2 = \mathbf{12}$.
        - Ball halts at destination $(4, 4)$!
        - Update: $dist[4][4] = \mathbf{12}$.
  - Any alternative path that stops at $(4, 4)$ covers $\ge 12$ steps.
  - Final shortest distance: **`12`**.
- **Unreachable / Non-Stopping Destination Instance:**
  - If destination cannot be reached as a complete stop, $dist[destination] == \infty \implies \mathbf{-1}$.

This instance demonstrates Dijkstra shortest-path search on variable-weight state graphs with momentum physics, mathematically proves why edge relaxation finds global distance minima despite non-unit edge costs, and derives $O(M \cdot N \cdot \max(M, N))$ runtime and $O(M \cdot N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an $m \times n$ maze with empty spaces (`0`) and walls (`1`), a ball starting position `start`, and a `destination`:
The ball rolls in one of 4 directions until it hits a wall.
Find the **shortest distance** for the ball to **stop at the destination**.
If the ball cannot come to a complete stop at the destination, return `-1`.

```text
Maze Geometry (Start at (0, 4), Destination at (4, 4)):

Path of Rolling Stops:
  (0, 4) -> Roll Left -> Stops at (0, 3)  (Distance: 1)
  (0, 3) -> Roll Down -> Stops at (2, 3)  (Distance: 1 + 2 = 3)
  (2, 3) -> Roll Left -> Stops at (2, 0)  (Distance: 3 + 3 = 6)
  ...
  (4, 2) -> Roll Right -> Hits wall at (4, 4) (Distance: 10 + 2 = 12)

Total Shortest Rolling Distance = 12
```

### Edge Weights in the Rolling Graph
Unlike standard BFS where every step has weight 1:
- An edge here is a continuous roll from resting position $u$ to resting position $v$.
- The **weight of an edge** is the number of cells traversed during that roll (which can be any integer from $1$ to $\max(m, n)$).
- Because edge weights are non-uniform, this is a **Shortest Path Problem on a Weighted Directed Graph**, requiring Dijkstra's algorithm or shortest-path queue relaxation.

---

## 2. Conceptual Foundation & Invariants

### 1. The Collision Raycast with Distance Accumulation:
From resting position $(i, j)$ with known shortest distance $dist[i][j]$:
For each direction $(a, b) \in \{(-1, 0), (1, 0), (0, -1), (0, 1)\}$:
- Step $(x, y)$ while the front cell is in bounds and open ($maze[x + a][y + b] == 0$):
  $$
  x \leftarrow x + a, \quad y \leftarrow y + b, \quad k \leftarrow k + 1
  $$
- Here, $k$ is the total distance from start to the new resting cell $(x, y)$.

### 2. Edge Relaxation Condition:
If $k < dist[x][y]$:
A strictly shorter route to resting cell $(x, y)$ has been found!
$$
dist[x][y] \leftarrow k
$$
Push $(x, y)$ into the queue to propagate the shorter distance to subsequent rolls.

> **Triangle Inequality Invariant.** For any resting cell $(x, y)$, $dist[x][y]$ monotonically decreases toward the true shortest path distance, stabilizing at the global minimum.

---

## 3. Step-by-Step Worked Execution

We trace $start = [0, 4]$ and $destination = [4, 4]$:

---

### Step 1: Initialize Distance Matrix
- Matrix $dist$ of size $5 \times 5$ initialized to $\infty$.
- $dist[0][4] = 0$.
- Queue $q = [(0, 4)]$.

---

### Step 2: Explore from $(0, 4)$ ($dist = 0$)
1. **Roll Left $(0, -1)$:**
   - Rolls 1 cell to $(0, 3)$. Hits wall at $(0, 2)$.
   - Traversed distance: $k = 0 + 1 = 1$.
   - $1 < \infty \implies dist[0][3] \leftarrow 1$. Enqueue $(0, 3)$.
2. **Roll Down $(1, 0)$:**
   - Rolls 2 cells to $(2, 4)$. Hits wall at $(3, 4)$.
   - Traversed distance: $k = 0 + 2 = 2$.
   - $dist[2][4] \leftarrow 2$. Enqueue $(2, 4)$.

---

### Step 3: Explore from $(0, 3)$ ($dist = 1$)
- Roll Down $(1, 0)$:
  - Rolls 2 cells to $(2, 3)$. Hits wall at $(3, 3)$.
  - Distance: $1 + 2 = 3$.
  - $dist[2][3] \leftarrow 3$. Enqueue $(2, 3)$.

---

### Step 4: Explore from $(2, 3)$ ($dist = 3$)
- Roll Left $(0, -1)$:
  - Rolls 3 cells through $(2, 2) \to (2, 1) \to (2, 0)$. Hits left boundary wall.
  - Distance: $3 + 3 = 6$.
  - $dist[2][0] \leftarrow 6$. Enqueue $(2, 0)$.

---

### Step 5: Route Through Lower Corridor
- From $(2, 0)$, rolling and turning navigates through open channels in row 4.
- Resting cell $(4, 2)$ is reached with optimal distance $dist[4][2] = 10$.

---

### Step 6: Roll Right from $(4, 2)$ to Destination
From resting position $(4, 2)$ with $dist = 10$:
- Roll Right $(0, 1)$:
  - Traverses $(4, 3) \to (4, 4)$ (2 cells).
  - Hits right boundary wall ($y = 5$) and halts at cell $\mathbf{(4, 4)}$.
  - Total distance:
    $$
    k = 10 + 2 = \mathbf{12}
    $$
  - $12 < dist[4][4] (\infty) \implies dist[4][4] \leftarrow \mathbf{12}$.

---

### Step 7: Queue Exhaustion
All other paths to $(4, 4)$ cover $\ge 12$ steps.
Result: $dist[4][4] = \mathbf{12}$.

---

## 4. Complete Execution Trace

| Resting Cell $(i, j)$ | Shortest Dist $dist[i][j]$ | Roll Direction | Stopping Cell $(x, y)$ | Step Distance Added | Total Path Dist $k$ | $dist[x][y]$ Updated? |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $(0, 4)$ (Start) | $0$ | Left | $(0, 3)$ | $1$ | $1$ | Yes ($1 < \infty$) |
| $(0, 4)$ | $0$ | Down | $(2, 4)$ | $2$ | $2$ | Yes ($2 < \infty$) |
| $(0, 3)$ | $1$ | Down | $(2, 3)$ | $2$ | $3$ | Yes ($3 < \infty$) |
| $(2, 3)$ | $3$ | Left | $(2, 0)$ | $3$ | $6$ | Yes ($6 < \infty$) |
| $(4, 2)$ | $10$ | Right | $(4, 4)$ | $2$ | **$12$** | **Yes ($12 < \infty$)** |
| **Destination** | **$12$** | — | — | — | — | **Result: $12$** |

---

## 5. Boundary Cases & Failure Modes

- **Start Equals Destination ($start == destination$):** Ball is already at rest at destination $\implies \mathbf{0}$.
- **Completely Enclosed Start:** Ball cannot roll in any direction $\implies \mathbf{-1}$.
- **Fly-Over Destination:** Destination is in open corridor but no adjacent wall stops the ball on it $\implies$ returns $\mathbf{-1}$.
- **Multiple Disjoint Corridors:** $dist$ table correctly prunes non-reachable components, leaving destination as $\infty \implies \mathbf{-1}$.

---

## 6. Traps & Common Anti-Patterns

- **Using Standard Unweighted BFS Queue:** Standard BFS assumes all edges have unit weight (1). Since rolling distances vary from 1 to 100, standard BFS does NOT guarantee that the first time destination is popped is the shortest path. Using Dijkstra (priority queue) or queue relaxation ensures finding the true minimal distance.
- **Counting Wall Collisions Instead of Cells Traversed:** The question asks for the number of *empty spaces* traveled, not the number of turns or bounces. Accumulating $k + 1$ on each open cell traversed is strictly required.
- **Re-traversing Suboptimal Paths:** Without the condition `if k < dist[x][y]`, identical or longer paths cause infinite loops or TLE.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - There are $M \times N$ possible resting cells.
  - From each resting cell, rolling in 4 directions traverses at most $\max(M, N)$ cells.
  - Each resting state is relaxed only when a shorter distance is found.
  - Total Time: $\mathcal{O}(M \cdot N \cdot \max(M, N))$. For $100 \times 100$ maze, completes in $< 30$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(M \cdot N)$ to store the $dist$ matrix and queue.
