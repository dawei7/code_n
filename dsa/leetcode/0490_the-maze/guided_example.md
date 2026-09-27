# Guided Example: The Maze

We trace the step-by-step ray-marching rolling ball simulation (continuous motion until wall collision), stopping-cell graph abstraction (nodes are resting points, not passing cells), 4-directional raycasting ($Up, Down, Left, Right$), visited state tracking ($vis[x][y]$), and destination halting verification on representative grid mazes:

- **Input:**
  - $maze = \begin{bmatrix} 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 \\ 1 & 1 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}$
  - Starting position: $start = [0, 4]$
  - Destination position: $destination = [4, 4]$
- **Required output:** `true`
  - Critical Rule: The ball **cannot stop voluntarily** in an open corridor. It rolls continuously in a chosen direction until it hits a wall ($1$) or the grid boundary. The ball must **come to a complete stop** at the destination to succeed. Passing through the destination without a wall to halt it does not count.
- **Ray-marching DFS execution trace:**
  - Initial resting point: $start = [0, 4]$, mark $vis[0][4] = \text{True}$.
  - **From $(0, 4)$, shoot rays in all 4 directions:**
    - **Direction Left $(0, -1)$:**
      - Rolls through $(0, 3) \to$ hits wall at $(0, 2)$ ($maze[0][2] = 1$).
      - Halts at resting cell: $\mathbf{(0, 3)}$.
      - Recurse from $(0, 3)$:
        - From $(0, 3)$, rolling Down $(1, 0)$ rolls through $(1, 3), (2, 3) \to$ wall at $(3, 3)$.
        - Halts at resting cell: $\mathbf{(2, 3)}$.
        - From $(2, 3)$, rolling Down hits wall at $(3, 3)$. Rolling Left $(0, -1)$ passes $(2, 2), (2, 1), (2, 0)$ to boundary wall $\to$ halts at $\mathbf{(2, 0)}$.
    - **Direction Down $(1, 0)$ from $(0, 4)$:**
      - Rolls through $(1, 4), (2, 4) \to$ hits wall at $(3, 4)$ ($maze[3][4] = 1$).
      - Halts at resting cell: $\mathbf{(2, 4)}$.
      - Recurse from $(2, 4)$:
        - Rolling Left $(0, -1)$ hits wall at $(2, 3)$.
        - Rolling Up $( -1, 0)$ returns to $(0, 4)$ (already visited).
        - Rolling Down $(1, 0)$ is blocked by $(3, 4)$.
    - **From resting cell $(2, 0)$:**
      - Rolling Down $(1, 0)$ is blocked by $(3, 0)$ ($maze[3][0] = 1$).
      - Rolling Up $(-1, 0)$ halts at $(0, 0)$.
    - **From resting cell $(3, 2)$ via downward roll:**
      - Rolls Down through open cell $(4, 2)$ to bottom boundary.
      - Halts at $\mathbf{(4, 2)}$.
    - **From resting cell $(4, 2)$:**
      - Roll Right $(0, 1)$:
        - Rolls through $(4, 3) \to$ rolls through $(4, 4) \to$ hits right boundary wall ($y = 5$).
        - Ball hits the boundary wall and comes to a complete rest at cell $\mathbf{(4, 4)}$!
  - Ball comes to a complete halt at destination $[4, 4]$.
  - Return **`true`**.
- **Passing Through Without Stopping Instance:**
  - If destination is at $(1, 4)$, the ball rolling from $(0, 4)$ to $(2, 4)$ passes through $(1, 4)$ but cannot stop there because there is no wall. If no other path allows halting at $(1, 4)$, the result is $\mathbf{false}$.

This instance demonstrates state-space graph abstraction over physical momentum constraints, mathematically proves why visited sets must index halting states rather than traversal paths, and derives $O(M \cdot N \cdot \max(M, N))$ runtime and $O(M \cdot N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an $m \times n$ grid representing a maze:
- Empty spaces are `0`, walls are `1`.
- A ball starts at `start` and wants to reach `destination`.
- The ball can roll **Up, Down, Left, or Right**, but it **will not stop rolling until it hits a wall**.
- When the ball stops, it can choose its next direction.
Return `true` if the ball can **stop at the destination**, or `false` otherwise.

```text
Maze Physics (Momentum Rule):
  Start (0, 4)  .  .  [Wall at (0, 2)]
  Ball rolls LEFT -> Cannot stop at (0, 3) voluntarily!
  It hits the wall at (0, 2) and STOPS at (0, 3).

Graph Nodes:
  Nodes in our search graph are NOT every grid cell.
  Nodes are ONLY cells where the ball can come to a COMPLETE REST!
```

### The "Passing Through" Trap
A cell is only reached if the ball can **stop** on it.
If the destination lies in the middle of a long empty hallway, the ball may fly directly over it without stopping. Only paths that cause the ball to hit a wall directly adjacent to the destination count as a valid arrival.

---

## 2. Conceptual Foundation & Invariants

### 1. Ray-Marching Collision Transition:
From a current resting cell $(i, j)$, for each direction $(a, b) \in \{(0, -1), (0, 1), (1, 0), (-1, 0)\}$:
- Advance $(x, y)$ while the front cell is inside the grid and is open ($maze[x + a][y + b] == 0$):
  $$
  \text{while } 0 \le x + a < m \text{ and } 0 \le y + b < n \text{ and } maze[x + a][y + b] == 0:
  $$
  $$
  x \leftarrow x + a, \quad y \leftarrow y + b
  $$
- The terminal coordinate $(x, y)$ is the **new resting state**.

### 2. Visited Halting States:
We maintain a 2D boolean array $vis[m][n]$:
- $vis[x][y] = \text{True}$ means we have already explored branching from resting position $(x, y)$.
- Marking resting positions prevents infinite ping-pong cycles between opposing walls.

> **Resting State Invariant.** Graph edges connect resting position $u$ to resting position $v$ via collision raycasts. The destination is reachable if and only if $destination$ is in the connected component of $start$ in the resting-state graph.

---

## 3. Step-by-Step Worked Execution

We trace $start = [0, 4]$ and $destination = [4, 4]$:

---

### Step 1: Initial Resting Point $(0, 4)$
- Mark $vis[0][4] = \text{True}$.
- Check destination: $(0, 4) \ne (4, 4)$.

---

### Step 2: Raycast in 4 Directions from $(0, 4)$
1. **Left $(0, -1)$:**
   - Moves to $(0, 3)$. Next cell $(0, 2)$ is a wall.
   - Halts at $(0, 3)$. Recurse on $(0, 3)$.
2. **Down $(1, 0)$:**
   - Moves to $(1, 4)$, then $(2, 4)$. Next cell $(3, 4)$ is a wall.
   - Halts at $(2, 4)$. Recurse on $(2, 4)$.
3. **Right $(0, 1)$:**
   - Boundary wall $\implies$ stays at $(0, 4)$ (already visited).
4. **Up $(-1, 0)$:**
   - Boundary wall $\implies$ stays at $(0, 4)$.

---

### Step 3: Branching from $(0, 3)$
From resting position $(0, 3)$:
- Down $(1, 0)$:
  - Moves through $(1, 3) \to (2, 3)$. Next cell $(3, 3)$ is a wall.
  - Halts at $(2, 3)$. Recurse on $(2, 3)$.

---

### Step 4: Branching from $(2, 3)$
From resting position $(2, 3)$:
- Left $(0, -1)$:
  - Moves through $(2, 2) \to (2, 1) \to (2, 0)$. Hits left boundary wall.
  - Halts at $(2, 0)$. Recurse on $(2, 0)$.

---

### Step 5: Path to Lower Corridor
- From $(2, 0)$, roll Down $(1, 0) \to$ hits wall at $(3, 0)$.
- From $(2, 1)$, roll Down through $(3, 2)$ which is open!
  - Rolls through $(3, 2) \to (4, 2)$.
  - Hits bottom boundary wall ($x = 5$).
  - Halts at resting cell $\mathbf{(4, 2)}$.

---

### Step 6: Arrival at Destination from $(4, 2)$
From resting position $(4, 2)$:
- Shoot ray Right $(0, 1)$:
  - $(4, 2) \to (4, 3) \to \mathbf{(4, 4)}$.
  - Next cell $(4, 5)$ is the right boundary wall!
  - Ball collides with the boundary wall and stops at:
    $$
    (x, y) = \mathbf{(4, 4)} == destination
    $$
- Mark $vis[4][4] = \text{True}$.
- Goal reached as a valid stopping position!
- Return **`true`**.

---

## 4. Complete Execution Trace

| Step | Current Resting Cell | Roll Direction | Path Traversed | Obstacle Hit | New Resting Cell | Visited Before? |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **$0$** | $(0, 4)$ (Start) | Left $(0, -1)$ | $(0, 3)$ | Wall at $(0, 2)$ | $(0, 3)$ | No |
| **$1$** | $(0, 3)$ | Down $(1, 0)$ | $(1, 3) \to (2, 3)$ | Wall at $(3, 3)$ | $(2, 3)$ | No |
| **$2$** | $(2, 3)$ | Left $(0, -1)$ | $(2, 2) \to (2, 1) \to (2, 0)$ | Left Wall ($y = -1$) | $(2, 0)$ | No |
| **$3$** | $(2, 1)$ | Down $(1, 0)$ | $(3, 2) \to (4, 2)$ | Bottom Wall ($x = 5$) | $(4, 2)$ | No |
| **$4$** | **$(4, 2)$** | **Right $(0, 1)$** | **$(4, 3) \to (4, 4)$** | **Right Wall ($y = 5$)** | **$(4, 4)$** | **Destination Reached!** |

---

## 5. Boundary Cases & Failure Modes

- **Start Equals Destination ($start == destination$):** The ball is already at rest at destination $\implies \mathbf{true}$.
- **Completely Enclosed Start:** Ball cannot roll in any direction $\implies \mathbf{false}$.
- **Endless Corridors:** Ball bounces back and forth between two walls. Visited check $vis[x][y]$ halts the cycle immediately.
- **Fly-Over Destination:** Destination is an open cell with no adjacent wall in the direction of travel $\implies$ ball rolls through without stopping, correctly recognized as non-stopping.

---

## 6. Traps & Common Anti-Patterns

- **Marking Every Traversed Cell as Visited:** If you mark cells that the ball *rolls through* as visited, you block other valid rolling paths from crossing that hallway later in a perpendicular direction. Only mark cells where the ball comes to a complete **STOP**!
- **Stopping One Step Too Late:** Advancing $(x, y)$ inside the while loop without checking `maze[x+a][y+b] == 0` steps inside the wall. The standard `while ...: x += a; y += b` loop stops at the last open cell before the obstacle.
- **Checking Destination During Traversal:** Checking `if [x, y] == destination` inside the rolling loop falsely accepts cases where the ball merely flies past the destination without stopping. The check must be performed strictly on resting cells.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - There are at most $M \times N$ distinct resting cells in the grid.
  - From each resting cell, raycasting in 4 directions traverses at most $\max(M, N)$ cells.
  - Total Time: $\mathcal{O}(M \cdot N \cdot \max(M, N))$. For a $100 \times 100$ maze, operations are bounded by $10^4 \times 100 = 10^6$, running in $< 20$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(M \cdot N)$ memory for the $vis$ matrix and recursion call stack depth.
