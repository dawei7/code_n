# Guided Example: Spiral Matrix III

We trace the step-by-step arithmetic step-length progression ($1, 1, 2, 2, 3, 3, \dots$), 4-directional clockwise expansion (East $\to$ South $\to$ West $\to$ North), virtual unbounded coordinate roaming, boundary-filtered inclusion, and complete grid coverage termination on representative rectangular matrices:

- **Input:**
  $$
  rows = 1, \quad cols = 4, \quad rStart = 0, \quad cStart = 0
  $$
- **Required output:**
  $$
  [[0, 0], [0, 1], [0, 2], [0, 3]]
  $$
  - Spiral matrix walk rules:
    - We start at cell $(rStart, cStart) = (0, 0)$ facing **East**.
    - We walk in an expanding clockwise spiral:
      - Turn right whenever we complete the required leg length for the current direction.
      - Sequence of directions: East $(0, 1) \to$ South $(1, 0) \to$ West $(0, -1) \to$ North $(-1, 0)$.
    - We walk on an **unbounded infinite plane**: coordinates can step outside $[0, rows - 1] \times [0, cols - 1]$.
    - Only positions that lie strictly **inside the grid** ($0 \le r < rows$ and $0 \le c < cols$) are appended to the answer list.
    - We terminate the moment all $rows \times cols = 1 \times 4 = 4$ grid cells have been recorded.
    - For $1 \times 4$ starting at $(0, 0)$:
      - The spiral visits $(0, 0)$ first.
      - Spanning outward, it visits $(0, 1)$, loops outside the single-row boundary, re-enters at $(0, 2)$, loops again, and visits $(0, 3)$.
      - All 4 cells collected: `[[0, 0], [0, 1], [0, 2], [0, 3]]`.
- **The Step-Length Growth & Directional Invariant:**
  - **The Step Sequence Formula:**
    - Observe the distances walked in each leg of an Archimedean square spiral:
      - East: $1$ step
      - South: $1$ step
      - West: $2$ steps
      - North: $2$ steps
      - East: $3$ steps
      - South: $3$ steps
      - West: $4$ steps
      - North: $4$ steps
    - Notice that **every two directional turns, the leg length increases by $1$**!
    - Parameterized by round $k = 1, 3, 5, \dots$:
      1. East $(0, 1)$: length $k$
      2. South $(1, 0)$: length $k$
      3. West $(0, -1)$: length $k + 1$
      4. North $(-1, 0)$: length $k + 1$
      5. Advance round: $k \leftarrow k + 2$.
  - **Boundary Filtering Invariant:**
    - The robot steps blindly through virtual space.
    - At every individual unit step $(r, c)$:
      $$
      \text{If } 0 \le r < rows \land 0 \le c < cols \implies \text{append } [r, c]
      $$
    - Termination is verified immediately after appending: $|ans| == rows \times cols$.

---

## 1. Instance & Teaching Goal

Given a $1 \times 4$ grid starting at $(0, 0)$, trace the spiral expansions as they loop in and out of the grid.

```text
Grid Cells: (0, 0), (0, 1), (0, 2), (0, 3)

Spiral Pattern:
  Start: (0, 0) [IN GRID #1]
  Round 1 (k = 1):
    East 1:  (0, 1) [IN GRID #2]
    South 1: (1, 1) [Out]
    West 2:  (1, 0) [Out], (1, -1) [Out]
    North 2: (0, -1) [Out], (-1, -1) [Out]
  Round 2 (k = 3):
    East 3:  (-1, 0) [Out], (-1, 1) [Out], (-1, 2) [Out]
    South 3: (0, 2) [IN GRID #3], (1, 2) [Out], (2, 2) [Out]
    West 4:  all out...
    North 4: all out...
  Round 3 (k = 5):
    East 5:  hits (0, 3) [IN GRID #4 -> ALL 4 FOUND!]

Output: [[0, 0], [0, 1], [0, 2], [0, 3]]
```

The teaching goal is to show how separating the unconstrained infinite spiral generator from grid boundary filtration simplifies state logic.

---

## 2. Conceptual Foundation & Invariants

### 1. Clockwise Direction Vectors:
$$
\Delta = [(0, 1), \; (1, 0), \; (0, -1), \; (-1, 0)]
$$
Leg lengths per cycle of 4 directions: $[k, k, k + 1, k + 1]$ where $k$ starts at $1$ and increments by $2$ each cycle.

### 2. Termination Condition:
$$
|ans| = rows \times cols
$$

---

## 3. Step-by-Step Worked Execution

Grid: $1 \times 4$, cells to find: $4$.
Start: $r = 0, c = 0$.
Record initial cell: $ans = [[0, 0]]$. Count $= 1$.
Initialize round variable: $k = 1$.

---

### Phase 1: Round $k = 1$
1. **East leg (length $k = 1$, direction $(0, 1)$):**
   - Step 1: $(0, 0) + (0, 1) = (0, 1)$.
   - Boundary check: $0 \le 0 < 1 \land 0 \le 1 < 4 \implies$ **Inside!**
   - Append $[0, 1]$. Count $= 2$.
2. **South leg (length $k = 1$, direction $(1, 0)$):**
   - Step 1: $(0, 1) + (1, 0) = (1, 1)$.
   - Boundary check: row $1 \ge rows = 1 \implies$ Outside.
3. **West leg (length $k + 1 = 2$, direction $(0, -1)$):**
   - Step 1: $(1, 1) + (0, -1) = (1, 0)$ (Outside).
   - Step 2: $(1, 0) + (0, -1) = (1, -1)$ (Outside).
4. **North leg (length $k + 1 = 2$, direction $(-1, 0)$):**
   - Step 1: $(1, -1) + (-1, 0) = (0, -1)$ (Outside).
   - Step 2: $(0, -1) + (-1, 0) = (-1, -1)$ (Outside).
- Increment $k \leftarrow 1 + 2 = 3$.

---

### Phase 2: Round $k = 3$
1. **East leg (length $k = 3$, direction $(0, 1)$):**
   - Steps from $(-1, -1)$:
     - Step 1: $(-1, 0)$ (Outside).
     - Step 2: $(-1, 1)$ (Outside).
     - Step 3: $(-1, 2)$ (Outside).
2. **South leg (length $k = 3$, direction $(1, 0)$):**
   - Step 1: $(-1, 2) + (1, 0) = (0, 2)$.
   - Boundary check: $0 \le 0 < 1 \land 0 \le 2 < 4 \implies$ **Inside!**
   - Append $[0, 2]$. Count $= 3$.
   - Step 2: $(0, 2) + (1, 0) = (1, 2)$ (Outside).
   - Step 3: $(1, 2) + (1, 0) = (2, 2)$ (Outside).
3. **West leg (length $k + 1 = 4$, direction $(0, -1)$):**
   - Steps: $(2, 1), (2, 0), (2, -1), (2, -2)$ (all outside).
4. **North leg (length $k + 1 = 4$, direction $(-1, 0)$):**
   - Steps: $(1, -2), (0, -2), (-1, -2), (-2, -2)$ (all outside).
- Increment $k \leftarrow 3 + 2 = 5$.

---

### Phase 3: Round $k = 5$
1. **East leg (length $k = 5$, direction $(0, 1)$):**
   - Steps from $(-2, -2)$:
     - Step 1: $(-2, -1)$
     - Step 2: $(-2, 0)$
     - Step 3: $(-2, 1)$
     - Step 4: $(-2, 2)$
     - Step 5: $(-2, 3)$ (all row $-2$, outside).
2. **South leg (length $k = 5$, direction $(1, 0)$):**
   - Step 1: $(-2, 3) + (1, 0) = (-1, 3)$ (Outside).
   - Step 2: $(-1, 3) + (1, 0) = (0, 3)$.
   - Boundary check: $0 \le 0 < 1 \land 0 \le 3 < 4 \implies$ **Inside!**
   - Append $[0, 3]$. Count $= 4$.
   - Check termination: $|ans| == 4 == rows \times cols$.
   - **All cells collected! Terminate immediately.**

---

### Termination:
- **Output:** **`[[0, 0], [0, 1], [0, 2], [0, 3]]`**.

---

## 4. Complete Execution Trace

| Round $k$ | Direction | Leg Steps Allocated | Step Number | Candidate Coordinate | In Grid? | Collected Order | Current Answer Size |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Start | — | — | — | $(0, 0)$ | **Yes** | 1st | $1$ |
| $1$ | East | $1$ | $1$ | $(0, 1)$ | **Yes** | 2nd | $2$ |
| $1$ | South | $1$ | $1$ | $(1, 1)$ | No | — | $2$ |
| $1$ | West | $2$ | $1, 2$ | $(1, 0), (1, -1)$ | No | — | $2$ |
| $1$ | North | $2$ | $1, 2$ | $(0, -1), (-1, -1)$ | No | — | $2$ |
| $3$ | East | $3$ | $1, 2, 3$ | $(-1, 0), (-1, 1), (-1, 2)$ | No | — | $2$ |
| $3$ | South | $3$ | $1$ | $(0, 2)$ | **Yes** | 3rd | $3$ |
| $3$ | South | $3$ | $2, 3$ | $(1, 2), (2, 2)$ | No | — | $3$ |
| $3$ | West | $4$ | $1..4$ | $(2, 1) \dots (2, -2)$ | No | — | $3$ |
| $3$ | North | $4$ | $1..4$ | $(1, -2) \dots (-2, -2)$ | No | — | $3$ |
| $5$ | East | $5$ | $1..5$ | $(-2, -1) \dots (-2, 3)$ | No | — | $3$ |
| **$5$** | **South** | **$5$** | **$2$** | **$(0, 3)$** | **Yes** | **4th** | **`4 (Done!)`** |

---

## 5. Boundary Cases & Failure Modes

- **$1 \times 1$ Grid ($rows = 1, cols = 1$):** Starting cell $(rStart, cStart)$ is the only cell. Terminating condition $|ans| == 1$ triggers at step 0 without entering loops $\implies [[rStart, cStart]]$.
- **Starting at the Border or Corner:** The spiral begins within the grid and immediately wanders outside; the loop continues without error until it sweeps back across remaining rows.
- **Large Rectangular Aspects (e.g. $1 \times 100$ or $100 \times 1$):** Handled identically; virtual steps grow at rate $\mathcal{O}(\max(R, C)^2)$.

---

## 6. Traps & Common Anti-Patterns

- **Attempting to Clip Turns to Grid Boundaries:** Changing direction early when hitting a grid boundary warps the spiral geometry, causing missed cells and infinite loops. The spiral must unfold freely in infinite 2D space.
- **Dynamic Visited Sets:** Because the spiral visits each coordinate on the infinite plane at most once, a visited set is redundant. A simple count comparison $|ans| == rows \times cols$ is sufficient.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Maximum radius of the spiral from starting point to the farthest corner is at most $2 \times \max(rows, cols)$.
  - Total unit steps evaluated on the plane is bounded by $\mathcal{O}(\max(rows, cols)^2)$.
  - For $rows, cols \le 100$, maximum steps $\le (200)^2 = 40,000$, executing in $< 5$ ms.
- **Auxiliary Space Complexity:**
  - Output list storing all $rows \times cols$ coordinates: $\mathcal{O}(rows \cdot cols)$ space.
