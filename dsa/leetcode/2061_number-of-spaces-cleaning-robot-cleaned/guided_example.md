# Guided Example: Number of Spaces Cleaning Robot Cleaned

We trace the step-by-step deterministic state-space simulation and cycle detection of an automated cleaning robot on a representative grid:

- **Input:** $\text{room} = [[0, 0, 0], [1, 1, 0], [0, 0, 0]]$
- **Expected Output:** $7$

---

## 1. Problem Overview & Representative Instance

A room is represented as an $R \times C$ binary grid where:
- `0` denotes an accessible, cleanable space.
- `1` denotes an obstacle (object).
The cleaning robot starts at coordinate $(0, 0)$ facing **East** (right). It cleans its current square immediately upon arrival.

### Movement Rules
At each step:
1. The robot checks the space directly ahead along its current heading.
2. **Move Forward:** If the candidate space is within the grid boundaries and is not an obstacle, the robot advances into it and maintains its current heading.
3. **Turn Clockwise:** If the space ahead is out of bounds or contains an obstacle, the robot remains in place and turns $90^\circ$ clockwise (East $\to$ South $\to$ West $\to$ North $\to$ East).
4. The simulation terminates when the robot enters a directed state $(r, c, d)$ that it has previously occupied, proving that it has entered a periodic orbit.

The goal is to determine the total number of **distinct empty spaces** cleaned.

```mermaid
flowchart TD
    accTitle: Cleaning Robot Grid Traversal Path
    accDescr: 3 by 3 room showing robot path winding along the outer boundary avoiding obstacles at (1,0) and (1,1).
    subgraph Grid["Room Grid (3 x 3)"]
        direction TB
        subgraph Row0["Row 0"]
            direction LR
            C00["(0, 0) Cleaned"] --> C01["(0, 1) Cleaned"] --> C02["(0, 2) Cleaned"]
        end
        subgraph Row1["Row 1"]
            direction LR
            O10["(1, 0) Obstacle"] ~~~ O11["(1, 1) Obstacle"] ~~~ C12["(1, 2) Cleaned"]
        end
        subgraph Row2["Row 2"]
            direction LR
            C20["(2, 0) Cleaned"] <-- C21["(2, 1) Cleaned"] <-- C22["(2, 2) Cleaned"]
        end
        C02 --> C12 --> C22
    end

    classDef cleaned fill:#dcfce7,stroke:#15803d,stroke-width:2px;
    classDef obs fill:#fee2e2,stroke:#b91c1c,stroke-width:2px;
    class C00,C01,C02,C12,C22,C21,C20 cleaned;
    class O10,O11 obs;
```

In the representative room:
- Row $0$: Three open cells $(0, 0), (0, 1), (0, 2)$.
- Row $1$: Two obstacles at $(1, 0)$ and $(1, 1)$; open cell at $(1, 2)$.
- Row $2$: Three open cells $(2, 0), (2, 1), (2, 2)$.
- Total open cells available: $7$.
- The robot navigates around the obstacles along the outer boundary and cleans all $7$ open spaces.

---

## 2. Theoretical Invariants & Directed State Representation

A physical coordinate alone $(r, c)$ does not uniquely dictate the future trajectory of the robot. From the exact same cell $(r, c)$, facing East produces a completely different action than facing South.

### Full Directed State Invariant
We define the robot state as a triple $(r, c, d)$:
- Row index $r \in [0, R - 1]$
- Column index $c \in [0, C - 1]$
- Heading index $d \in \{0, 1, 2, 3\}$, corresponding to direction vectors:
  $$d_0 = (0, +1) \text{ [East]}, \quad d_1 = (+1, 0) \text{ [South]}, \quad d_2 = (0, -1) \text{ [West]}, \quad d_3 = (-1, 0) \text{ [North]}$$

### Orbit Periodic Invariant
Because the environment is static and the movement rules are strictly deterministic:
- The state space contains at most $4 \cdot R \cdot C$ total directed states.
- If the robot ever encounters a state $(r, c, d)$ that has already been recorded in the visited history set $\text{vis}$, all subsequent states will repeat in an identical infinite loop.
- No new spaces can ever be cleaned after entering a cycle. Therefore, halting at the first revisited directed state is sound and exact.

---

## 3. Step-by-Step State Execution Trace

We trace the robot's state evolution starting from $(0, 0, 0)$ [Facing East]:

| Step | State $(r, c, d)$ | Heading | Candidate Forward Cell | Candidate Status | Action Taken | Cell Cleaned? | Total Unique Cleaned |
|---|---|---|---|---|---|---|---|
| 0 | $(0, 0, 0)$ | East | $(0, 1)$ | Valid open cell | Clean $(0, 0)$, advance | New: $(0, 0)$ | $1$ |
| 1 | $(0, 1, 0)$ | East | $(0, 2)$ | Valid open cell | Clean $(0, 1)$, advance | New: $(0, 1)$ | $2$ |
| 2 | $(0, 2, 0)$ | East | $(0, 3)$ | Out of bounds | Turn clockwise $\implies$ South ($d=1$) | New: $(0, 2)$ | $3$ |
| 3 | $(0, 2, 1)$ | South | $(1, 2)$ | Valid open cell | Advance to $(1, 2)$ | Already clean $(0, 2)$ | $3$ |
| 4 | $(1, 2, 1)$ | South | $(2, 2)$ | Valid open cell | Clean $(1, 2)$, advance | New: $(1, 2)$ | $4$ |
| 5 | $(2, 2, 1)$ | South | $(3, 2)$ | Out of bounds | Turn clockwise $\implies$ West ($d=2$) | New: $(2, 2)$ | $5$ |
| 6 | $(2, 2, 2)$ | West | $(2, 1)$ | Valid open cell | Advance to $(2, 1)$ | Already clean $(2, 2)$ | $5$ |
| 7 | $(2, 1, 2)$ | West | $(2, 0)$ | Valid open cell | Clean $(2, 1)$, advance | New: $(2, 1)$ | $6$ |
| 8 | $(2, 0, 2)$ | West | $(2, -1)$ | Out of bounds | Turn clockwise $\implies$ North ($d=3$) | New: $(2, 0)$ | $7$ |
| 9 | $(2, 0, 3)$ | North | $(1, 0)$ | Obstacle (`room[1][0] == 1`) | Turn clockwise $\implies$ East ($d=0$) | Already clean $(2, 0)$ | $7$ |
| 10 | $(2, 0, 0)$ | East | $(2, 1)$ | Valid open cell | Advance to $(2, 1)$ | Already clean $(2, 0)$ | $7$ |
| 11 | $(2, 1, 0)$ | East | $(2, 2)$ | Valid open cell | Advance to $(2, 2)$ | Already clean $(2, 1)$ | $7$ |
| 12 | $(2, 2, 0)$ | East | $(2, 3)$ | Out of bounds | Turn clockwise $\implies$ South ($d=1$) | Already clean $(2, 2)$ | $7$ |
| 13 | $(2, 2, 1)$ | South | — | State $(2, 2, 1) \in \text{vis}$ | **Cycle detected! Halt.** | — | **$7$** |

At step 13, the state $(2, 2, 1)$ recurs, terminating the simulation with $7$ distinct cleaned spaces.

---

## 4. Room Grid Final Classification Matrix

Below is the state of each space upon termination:

| Coordinate $(r, c)$ | Original Cell Content | Visited by Robot? | Final Clean Status |
|---|---|---|---|
| $(0, 0)$ | `0` (Open) | Visited (Step 0) | Cleaned |
| $(0, 1)$ | `0` (Open) | Visited (Step 1) | Cleaned |
| $(0, 2)$ | `0` (Open) | Visited (Step 2) | Cleaned |
| $(1, 0)$ | `1` (Obstacle) | Never visited | Blocked |
| $(1, 1)$ | `1` (Obstacle) | Never visited | Blocked |
| $(1, 2)$ | `0` (Open) | Visited (Step 4) | Cleaned |
| $(2, 0)$ | `0` (Open) | Visited (Step 8) | Cleaned |
| $(2, 1)$ | `0` (Open) | Visited (Step 7) | Cleaned |
| $(2, 2)$ | `0` (Open) | Visited (Step 5) | Cleaned |

All $7$ accessible spaces were cleaned.

---

## 5. Algorithmic Correctness & Soundness

1. **Finite State Pigeonhole Principle:**
   The total number of directed configurations is bounded by $4 \cdot R \cdot C$. Since every step deterministically produces the next state, the trajectory must either terminate or enter a periodic cycle within at most $4 \cdot R \cdot C$ steps.
2. **Sufficiency of Directed Cycle Detection:**
   Once a state $(r, c, d)$ is revisited, the sequence of subsequent states is strictly periodic. Since no new cell can be encountered during periodic repetition, halting immediately preserves full correctness.
3. **Decoupling Cell Cleaning from State Visitation:**
   A cell $(r, c)$ may be entered multiple times with different headings. Overwriting the cell value (e.g. Setting $\text{room}[r][c] = -1$) or using a set of coordinates ensures each distinct space increments the accumulator at most once.

---

## 6. Edge Cases, Pitfalls & Structural Traps

- **Corner Trap (Surrounded by Obstacles):**
  If $(0, 1)$ and $(1, 0)$ are obstacles, the robot turns $90^\circ$ four times in place at $(0, 0)$, cycling back to $(0, 0, 0)$ without moving. The result is correctly $1$.
- **Tracking Coordinates vs Directed States:**
  Detecting cycles using only coordinates $(r, c)$ prematurely stops the robot if it crosses its own path in a different direction (e.g. Passing through a junction horizontally and later vertically). Cycle detection must track the full triple $(r, c, d)$.
- **Center Never Visited:**
  In a large open room (e.g. $3 \times 3$ with all `0`s), the robot circumnavigates the perimeter and enters a cycle, visiting $8$ perimeter cells and never reaching the center cell $(1, 1)$. The answer is $8$, not $9$.

---

## 7. Complexity Analysis

- **Time Complexity:** $\mathcal{O}(R \cdot C)$.
  There are $4 \cdot R \cdot C$ possible states. Because each state $(r, c, d)$ is processed at most once before being recorded in the visited set, the simulation performs at most $\mathcal{O}(R \cdot C)$ transitions. For $R, C \le 300$, at most $4 \times 300 \times 300 = 360,000$ operations occur, executing in milliseconds.
- **Space Complexity:** $\mathcal{O}(R \cdot C)$ auxiliary space to store visited directed states and the recursion/queue call stack.
