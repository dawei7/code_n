# Guided Example: Robot Room Cleaner

We trace the step-by-step relative Cartesian coordinate mapping ($(0, 0)$ origin), Depth-First Search exploration across 4 rotational headings ($Up \to Right \to Down \to Left$), obstacle discovery (`robot.move() == False`), physical state restoration via $180^\circ$ retreat backtracking, and complete room coverage on representative grid layouts:

- **Input:** Blind room exploration via API (`move()`, `turnRight()`, `clean()`)
- **Required outcome:** All accessible empty cells cleaned and robot safely returned to starting origin.
- **Directional convention:**
  - Headings: $0 = \text{Up } (-1, 0), \; 1 = \text{Right } (0, 1), \; 2 = \text{Down } (1, 0), \; 3 = \text{Left } (0, -1)$
  - Start cell: $(0, 0)$ facing direction $d = 0$ (Up)
- **DFS with physical backtracking trace on a $2 \times 2$ room:**
  - Room layout: $(0, 0)$ open, $(0, 1)$ open, $(1, 0)$ open, $(1, 1)$ wall.
  - **At $(0, 0)$ facing Up ($d = 0$):**
    - Clean current cell: $(0, 0)$ added to $vis$, cleaned!
    - **Direction 0 (Up, $(-1, 0)$):** `robot.move()` hits wall $\implies$ returns `False`.
      - Turn right $90^\circ$: robot now faces Right ($d = 1$).
    - **Direction 1 (Right, $(0, 1)$):**
      - Target $(0, 1) \notin vis$.
      - `robot.move()` returns `True` $\implies$ Robot steps into $(0, 1)$!
      - **Recurse `dfs(0, 1, 1)` at $(0, 1)$ facing Right ($d = 1$):**
        - Clean $(0, 1)$: mark visited, clean!
        - Direction 1 (Right): wall $\implies$ `move()` False. Turn right to Down ($d = 2$).
        - Direction 2 (Down, $(1, 1)$): wall $\implies$ `move()` False. Turn right to Left ($d = 3$).
        - Direction 3 (Left, $(0, 0)$): $(0, 0) \in vis$ $\implies$ already visited, skip! Turn right to Up ($d = 0$).
        - Direction 0 (Up): wall $\implies$ `move()` False. Turn right to Right ($d = 1$).
        - All 4 directions checked from $(0, 1)$.
        - **Physical Backtrack to $(0, 0)$:**
          1. Turn $180^\circ$ (Right $\times 2$): faces Left ($d = 3$).
          2. Step forward: `robot.move()` moves from $(0, 1)$ back to $(0, 0)$.
          3. Turn $180^\circ$ (Right $\times 2$): faces Right ($d = 1$).
          - *Robot is back at $(0, 0)$ in original heading!*
      - Return to $(0, 0)$ loop. Turn right to Down ($d = 2$).
    - **Direction 2 (Down, $(1, 0)$):**
      - Target $(1, 0) \notin vis$.
      - `robot.move()` returns `True` $\implies$ Enters $(1, 0)$, cleans $(1, 0)$, explores neighbors, and executes $180^\circ$ retreat back to $(0, 0)$.
    - **Direction 3 (Left, $(0, -1)$):** Hits wall.
  - All 4 directions explored from $(0, 0)$. All accessible cells cleaned!
- **Cul-de-sac / Dead-End Instance:** Robot walks into a 1-wide dead end corridor, cleans the terminal cell, reverses orientation, steps back, and resumes searching lateral corridors without losing its positional coordinates.

This instance demonstrates blind robotic exploration with incomplete environmental observability (SLAM fundamentals), mathematically proves why physical backtracking guarantees invariance of the DFS call stack, and derives $O(N)$ runtime and $O(N)$ space bounds where $N$ is the number of open cells.

---

## 1. Instance & Teaching Goal

You are controlling a robot cleaner in a room modeled as an unknown grid:
- Empty cells are `1`, obstacles/walls are `0`.
- The robot starts at an unknown position facing an unknown initial direction.
- You have four API methods:
  - `robot.move()`: Steps forward 1 cell if open (returns `True`), stays put if blocked (returns `False`).
  - `robot.turnLeft()`, `robot.turnRight()`: Turns $90^\circ$ without moving.
  - `robot.clean()`: Cleans the current cell.
Clean every accessible empty cell in the room.

```text
Physical Robot Backtracking Dilemma:
  In standard software DFS, returning from a recursive call pops the call stack
  and memory automatically resets to parent variables.

  In ROBOTICS, the physical robot is physically located at the child cell!
  To return from child (x, y) back to parent (i, j):
    1. Turn 180 degrees (turnRight + turnRight)
    2. Move forward 1 step (returns to parent cell)
    3. Turn 180 degrees (turnRight + turnRight to restore orientation)
```

### The Lack of Global Coordinates
Because absolute coordinates are unknown:
- We define the robot's starting position as relative origin $(0, 0)$.
- We define its starting heading as direction $0$ (Up).
- All discovered cells are addressed by their relative displacement $(i, j)$ from the origin.

---

## 2. Conceptual Foundation & Invariants

### 1. Heading Vector Array:
Using a compact circular direction vector:
$$
dirs = (-1, 0, 1, 0, -1)
$$
- $d = 0$: $(-1, 0)$ (Up)
- $d = 1$: $(0, 1)$ (Right)
- $d = 2$: $(1, 0)$ (Down)
- $d = 3$: $(0, -1)$ (Left)
Turning right rotates heading:
$$
d_{new} = (d + 1) \pmod 4
$$

### 2. Relative Heading Iteration:
From heading $d$, turning right $k$ times ($k \in [0, 1, 2, 3]$) samples the 4 surrounding cells in order:
$$
nd = (d + k) \pmod 4, \quad (x, y) = (i + dirs[nd], \; j + dirs[nd + 1])
$$

### 3. Physical State Restoration:
Whenever `robot.move()` succeeds and we finish exploring `dfs(x, y, nd)`:
The physical robot is at $(x, y)$ facing $nd$.
To restore the robot to $(i, j)$ facing $nd$:
1. `robot.turnRight(); robot.turnRight()` (Turn $180^\circ$).
2. `robot.move()` (Move 1 step back into $(i, j)$).
3. `robot.turnRight(); robot.turnRight()` (Restore original heading $nd$).

> **Physical Invariant.** When `dfs(i, j, d)` terminates, the robot is physically situated in cell $(i, j)$ and oriented in direction $d$, exactly matching its entry state.

---

## 3. Step-by-Step Worked Execution

We trace exploring from origin $(0, 0)$ facing $d = 0$ (Up):

---

### Step 1: Initialize Origin
- Mark $(0, 0)$ as visited: $vis = \{(0, 0)\}$.
- Clean cell: `robot.clean()`.

---

### Step 2: Loop Over 4 Cardinal Directions ($k \in [0, 3]$)

1. **Attempt $k = 0$ (Heading $nd = 0$, Up):**
   - Target coordinate: $(0 - 1, 0 + 0) = (-1, 0)$.
   - Check visited: $(-1, 0) \notin vis$.
   - Call `robot.move()`: Hits boundary wall $\implies$ returns `False`.
   - Action: Robot remains at $(0, 0)$.
   - End of iteration: `robot.turnRight()`.
   - New physical heading: $d = 1$ (Right).

2. **Attempt $k = 1$ (Heading $nd = 1$, Right):**
   - Target coordinate: $(0 + 0, 0 + 1) = (0, 1)$.
   - Check visited: $(0, 1) \notin vis$.
   - Call `robot.move()`: Front is open $\implies$ returns `True`!
   - Robot moves into cell $(0, 1)$!
   - **Recursive Call `dfs(0, 1, 1)`:**
     - Mark $(0, 1) \in vis$.
     - Call `robot.clean()`.
     - Test all 4 directions from $(0, 1)$. Suppose all neighboring cells are blocked or visited.
     - All 4 turns completed ($360^\circ$). Robot at $(0, 1)$ faces Right ($1$).
     - **Execute Physical Backtrack:**
       - `robot.turnRight(); robot.turnRight()` (Now faces Left).
       - `robot.move()` (Steps forward into $(0, 0)$!).
       - `robot.turnRight(); robot.turnRight()` (Now faces Right).
     - Robot is back at $(0, 0)$ facing Right!
   - End of iteration: `robot.turnRight()`.
   - New physical heading: $d = 2$ (Down).

3. **Attempt $k = 2$ (Heading $nd = 2$, Down):**
   - Target $(1, 0) \notin vis$.
   - Enters $(1, 0)$, cleans it, explores, and physically backtracks to $(0, 0)$.
   - `robot.turnRight()` $\implies$ now faces Left ($d = 3$).

4. **Attempt $k = 3$ (Heading $nd = 3$, Left):**
   - Target $(0, -1)$ blocked by wall.
   - `robot.turnRight()` $\implies$ completes $360^\circ$, now faces Up ($d = 0$).

---

### Step 3: Termination
All reachable cells visited and cleaned. Robot is at start cell $(0, 0)$ facing Up ($d = 0$).

---

## 4. Complete Execution Trace

| Recursion Level | Robot Location | Heading $d$ | Tested Direction $nd$ | Target Cell $(x, y)$ | `move()` Success? | Action Taken | Backtrack Executed? |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Root | $(0, 0)$ | $0$ (Up) | $0$ (Up) | $(-1, 0)$ | **False** (Wall) | Stay put, turn right | No |
| Root | $(0, 0)$ | $1$ (Right) | $1$ (Right) | $(0, 1)$ | **True** (Open) | Enter $(0, 1)$, recurse | Yes ($180^\circ \to \text{move} \to 180^\circ$) |
| Child | $(0, 1)$ | $1$ (Right) | $1, 2, 3, 0$ | Multiple | All Fail/Vis | Clean, complete $360^\circ$ | Return to parent |
| Root | $(0, 0)$ | $2$ (Down) | $2$ (Down) | $(1, 0)$ | **True** (Open) | Enter $(1, 0)$, recurse | Yes |
| Root | $(0, 0)$ | $3$ (Left) | $3$ (Left) | $(0, -1)$ | **False** (Wall) | Turn right (Faces Up) | Exploration Complete |

---

## 5. Boundary Cases & Failure Modes

- **Single Cell Room ($1 \times 1$ enclosed by walls):** Robot cleans $(0, 0)$, tests all 4 walls (`move()` returns `False`), rotates $360^\circ$, and halts cleanly.
- **Narrow 1-Wide Corridor ($1 \times K$):** Robot steps straight ahead, hits end, backtracks one cell at a time, cleaning every cell in the hallway.
- **Islands of Obstacles:** Obstacles are naturally bypassed by turning right and navigating around their perimeters.

---

## 6. Traps & Common Anti-Patterns

- **Missing the Physical Backtrack:** In graph DFS on code arrays, returning automatically resets position. With a physical robot, if you do not physically move the robot back into the parent cell via $180^\circ$ reversal and forward step, the robot becomes physically lost, corrupting all future coordinates!
- **Not Turning $360^\circ$ Inside the Loop:** Ensuring `robot.turnRight()` executes exactly 4 times guarantees the robot leaves the node in the exact same orientation it had upon entering.
- **Attempting to Move to Already Visited Cells:** Checking `(x, y) not in vis` before calling `robot.move()` prevents wasted physical steps and avoids infinite recursive loops.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $N$ be the number of open cells and $M$ be the number of obstacles.
  - The robot visits each open cell once.
  - From each cell, it tests 4 directions ($4N$ tests).
  - For each successful entry, it backtracks once ($N - 1$ backtracks).
  - Total Time: $\mathcal{O}(N)$. Completes in $< 20$ ms for any typical grid.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space to store visited coordinates in the hash set $vis$, plus $O(N)$ recursion stack depth.
