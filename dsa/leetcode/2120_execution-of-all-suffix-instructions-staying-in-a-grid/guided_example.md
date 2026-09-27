# Guided Example: Execution of All Suffix Instructions Staying in a Grid

We trace the step-by-step execution of the optimal suffix trajectory simulation on a representative problem instance:

- **Grid Dimension ($n$):** $3$ ($3 \times 3$ grid: rows $0 \dots 2$, columns $0 \dots 2$)
- **Starting Position ($\text{startPos}$):** $[0, 1]$
- **Instruction String ($s$):** `"RRDDLU"`
- **Expected Output:** `[1, 5, 4, 3, 1, 0]`

This instance illustrates independent trajectory evaluations across successive string suffixes, testing bounded spatial coordinates in two dimensions, and demonstrating immediate halt behavior prior to executing out-of-bounds transitions.

---

## 1. Problem Overview & Representative Instance

We are given an $n \times n$ discrete grid with coordinates $(r, c)$ bounded by $0 \le r < n$ and $0 \le c < n$. A robot is placed at initial coordinate $\text{startPos} = [r_0, c_0]$. An instruction string $s$ of length $m$ provides movement commands:
- `'L'`: Move left (column delta $-1$)
- `'R'`: Move right (column delta $+1$)
- `'U'`: Move up (row delta $-1$)
- `'D'`: Move down (row delta $+1$)

For each index $i \in [0, m - 1]$, the robot resets to $\text{startPos}$ and sequentially executes the suffix substring $s[i \dots m - 1]$. The simulation for suffix $i$ terminates if:
1. The proposed next position falls outside the grid boundaries $0 \le r' < n$ and $0 \le c' < n$, or
2. All remaining instructions of the suffix are completed.

We must determine the number of successful moves executed for every suffix $i$.

---

## 2. Mathematical & Algorithmic Principles

### Discrete Vector Translations
Each instruction character $\chi \in \{\text{'L'}, \text{'R'}, \text{'U'}, \text{'D'}\}$ corresponds to a constant displacement vector $\Delta(\chi) \in \mathbb{Z}^2$:

$$\Delta(\text{'L'}) = (0, -1), \quad \Delta(\text{'R'}) = (0, 1), \quad \Delta(\text{'U'}) = (-1, 0), \quad \Delta(\text{'D'}) = (1, 0)$$

Given a robot state $(r_t, c_t)$ at instruction step $t$, the candidate successor state is:

$$(r_{t+1}, c_{t+1}) = (r_t, c_t) + \Delta(s[i + t])$$

### Boundary Feasibility Invariant
The state remains valid if and only if:

$$0 \le r_{t+1} < n \quad \land \quad 0 \le c_{t+1} < n$$

If the boundary condition is violated, the step is aborted immediately without moving the robot or counting the move. The suffix score is recorded as $t$.
Because the maximum string length $m \le 500$, directly simulating each suffix takes at most $\mathcal{O}(m^2)$ operations in total with $\mathcal{O}(1)$ auxiliary space.

| Instruction | Direction Description | Row Offset ($\Delta r$) | Column Offset ($\Delta c$) |
|---|---|---|---|
| `'L'` | West (Left) | $0$ | $-1$ |
| `'R'` | East (Right) | $0$ | $+1$ |
| `'U'` | North (Up) | $-1$ | $0$ |
| `'D'` | South (Down) | $+1$ | $0$ |

---

## 3. Step-by-Step Walkthrough with Intermediate State

Initial coordinates: $(r, c) = (0, 1)$ on a $3 \times 3$ grid ($n = 3$).

### Suffix $i = 0$: `"RRDDLU"`
- Reset to $(0, 1)$, moves executed $t = 0$.
- Step 1: Instruction `'R'`. Candidate: $(0, 1) + (0, 1) = (0, 2)$. In-bounds ($0 \le 0 < 3, 0 \le 2 < 3$). Move executed: $(r, c) \leftarrow (0, 2)$, $t = 1$.
- Step 2: Instruction `'R'`. Candidate: $(0, 2) + (0, 1) = (0, 3)$. Out-of-bounds ($3 \ge 3$). Halt simulation.
- Recorded answer: `ans[0] = 1`.

### Suffix $i = 1$: `"RDDLU"`
- Reset to $(0, 1)$, $t = 0$.
- Step 1: Instruction `'R'`. Candidate: $(0, 2)$. In-bounds. Position $\leftarrow (0, 2)$, $t = 1$.
- Step 2: Instruction `'D'`. Candidate: $(0, 2) + (1, 0) = (1, 2)$. In-bounds. Position $\leftarrow (1, 2)$, $t = 2$.
- Step 3: Instruction `'D'`. Candidate: $(1, 2) + (1, 0) = (2, 2)$. In-bounds. Position $\leftarrow (2, 2)$, $t = 3$.
- Step 4: Instruction `'L'`. Candidate: $(2, 2) + (0, -1) = (2, 1)$. In-bounds. Position $\leftarrow (2, 1)$, $t = 4$.
- Step 5: Instruction `'U'`. Candidate: $(2, 1) + (-1, 0) = (1, 1)$. In-bounds. Position $\leftarrow (1, 1)$, $t = 5$.
- Suffix exhausted. Recorded answer: `ans[1] = 5`.

### Suffix $i = 2$: `"DDLU"`
- Reset to $(0, 1)$, $t = 0$.
- Step 1: Instruction `'D'`. Candidate: $(1, 1)$. In-bounds. Position $\leftarrow (1, 1)$, $t = 1$.
- Step 2: Instruction `'D'`. Candidate: $(2, 1)$. In-bounds. Position $\leftarrow (2, 1)$, $t = 2$.
- Step 3: Instruction `'L'`. Candidate: $(2, 0)$. In-bounds. Position $\leftarrow (2, 0)$, $t = 3$.
- Step 4: Instruction `'U'`. Candidate: $(1, 0)$. In-bounds. Position $\leftarrow (1, 0)$, $t = 4$.
- Suffix exhausted. Recorded answer: `ans[2] = 4`.

### Suffix $i = 3$: `"DLU"`
- Reset to $(0, 1)$, $t = 0$.
- Step 1: Instruction `'D'`. Candidate: $(1, 1)$. In-bounds. Position $\leftarrow (1, 1)$, $t = 1$.
- Step 2: Instruction `'L'`. Candidate: $(1, 0)$. In-bounds. Position $\leftarrow (1, 0)$, $t = 2$.
- Step 3: Instruction `'U'`. Candidate: $(0, 0)$. In-bounds. Position $\leftarrow (0, 0)$, $t = 3$.
- Suffix exhausted. Recorded answer: `ans[3] = 3`.

### Suffix $i = 4$: `"LU"`
- Reset to $(0, 1)$, $t = 0$.
- Step 1: Instruction `'L'`. Candidate: $(0, 0)$. In-bounds. Position $\leftarrow (0, 0)$, $t = 1$.
- Step 2: Instruction `'U'`. Candidate: $(0, 0) + (-1, 0) = (-1, 0)$. Out-of-bounds ($-1 < 0$). Halt simulation.
- Recorded answer: `ans[4] = 1`.

### Suffix $i = 5$: `"U"`
- Reset to $(0, 1)$, $t = 0$.
- Step 1: Instruction `'U'`. Candidate: $(0, 1) + (-1, 0) = (-1, 1)$. Out-of-bounds ($-1 < 0$). Halt simulation.
- Recorded answer: `ans[5] = 0`.

---

## 4. Comprehensive State Trace

The full progression of states and boundary evaluations across all suffixes is detailed below:

| Suffix Index $i$ | Substring Evaluated | Sequence of Visited Cells | Halting Reason | Executed Moves ($ans[i]$) |
|---|---|---|---|---|
| $0$ | `"RRDDLU"` | $(0, 1) \to (0, 2) \to \text{Boundary Blocked at } (0, 3)$ | Column overflow ($c = 3 \ge n$) | $1$ |
| $1$ | `"RDDLU"` | $(0, 1) \to (0, 2) \to (1, 2) \to (2, 2) \to (2, 1) \to (1, 1)$ | Suffix completed | $5$ |
| $2$ | `"DDLU"` | $(0, 1) \to (1, 1) \to (2, 1) \to (2, 0) \to (1, 0)$ | Suffix completed | $4$ |
| $3$ | `"DLU"` | $(0, 1) \to (1, 1) \to (1, 0) \to (0, 0)$ | Suffix completed | $3$ |
| $4$ | `"LU"` | $(0, 1) \to (0, 0) \to \text{Boundary Blocked at } (-1, 0)$ | Row underflow ($r = -1 < 0$) | $1$ |
| $5$ | `"U"` | $(0, 1) \to \text{Boundary Blocked at } (-1, 1)$ | Row underflow ($r = -1 < 0$) | $0$ |

Combined output vector: `[1, 5, 4, 3, 1, 0]`.

---

## 5. Algorithmic Correctness & Soundness

**Soundness.** Each suffix execution is entirely decoupled from other suffixes. The robot coordinates are strictly initialized to $\text{startPos}$ before beginning each suffix traversal. Next-step coordinates are tested against the bounds $[0, n - 1]$ prior to updating the robot's coordinates or incrementing the step counter. Consequently, no invalid step is ever counted, and the robot never enters an invalid grid position.

**Completeness.** Every suffix index $i \in [0, m - 1]$ is simulated until either the boundary halts progress or the entire suffix is consumed. Because there are no cyclic traps (the trajectory length is bounded strictly by the suffix length $m - i$), the inner simulation terminates in finite steps for every suffix.

---

## 6. Edge Cases & Anti-Patterns

- **Immediate Out-of-Bounds:** If the initial instruction for a suffix directs the robot off the edge (e.g. Suffix 5 with `'U'` from row 0), the boundary check fails immediately on the first iteration and the count correctly remains $0$.
- **Complete In-Bounds Traversal:** If all $k = m - i$ instructions stay within bounds, the loop finishes normally, returning the full suffix length $k$.
- **$1 \times 1$ Grid ($n = 1$):** Starting at $(0, 0)$, any movement instruction immediately breaches the boundary, yielding $0$ for all suffixes.
- **Anti-Pattern — Stateful Carryover:** Failing to reinitialize the robot's position to $\text{startPos}$ at the beginning of each suffix simulation will corrupt subsequent trajectories by carrying over residual displacement from prior suffixes.

---

## 7. Complexity Analysis

- **Time Complexity:** $\mathcal{O}(m^2)$, where $m$ is the length of string $s$. There are $m$ suffixes, and suffix $i$ has length $m - i$. Evaluating each instruction involves $\mathcal{O}(1)$ coordinate addition and boundary checks, giving $\sum_{i=1}^m i = \frac{m(m+1)}{2} = \mathcal{O}(m^2)$ total steps.
- **Auxiliary Space Complexity:** $\mathcal{O}(1)$ auxiliary space beyond the output array of length $m$, as simulation requires only two coordinate variables and an iteration counter.
