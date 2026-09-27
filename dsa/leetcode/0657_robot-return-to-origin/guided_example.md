# Guided Example: Robot Return to Origin

We trace the step-by-step 2D Cartesian coordinate tracking ($(x, y)$), orthogonal vector displacement accumulation ($R \to (+1, 0), L \to (-1, 0), U \to (0, +1), D \to (0, -1)$), independent axis cancellation ($\Delta x = 0 \land \Delta y = 0$), and origin return verification on representative robot navigation move sequences:

- **Input:** $moves = \text{"URDL"}$
- **Required output:** `true`
  - Robot kinematics:
    - Robot begins at the Cartesian origin: $(x, y) = (0, 0)$.
    - Move instructions:
      - `'U'` (Up): Increments vertical position ($y \leftarrow y + 1$).
      - `'D'` (Down): Decrements vertical position ($y \leftarrow y - 1$).
      - `'R'` (Right): Increments horizontal position ($x \leftarrow x + 1$).
      - `'L'` (Left): Decrements horizontal position ($x \leftarrow x - 1$).
    - Objective: Return `true` if and only if the robot finishes all moves at the exact starting location $(0, 0)$.
- **Orthogonal Vector Invariance & Equilibrium Condition:**
  - **Axis Independence:**
    - The horizontal axis ($x$) and vertical axis ($y$) are mutually orthogonal:
      - Moves `'U'` and `'D'` have zero projection onto $x$ ($\Delta x = 0$).
      - Moves `'L'` and `'R'` have zero projection onto $y$ ($\Delta y = 0$).
    - Therefore, the total net displacement along each axis is simply the arithmetic difference of opposing directional move counts:
      $$
      \Delta x = \text{count}('R') - \text{count}('L')
      $$
      $$
      \Delta y = \text{count}('U') - \text{count}('D')
      $$
  - **Origin Return Condition:**
    - The robot concludes at the origin if and only if:
      $$
      \Delta x = 0 \quad \land \quad \Delta y = 0
      $$
    - Equivalently:
      $$
      \text{count}('R') = \text{count}('L') \quad \land \quad \text{count}('U') = \text{count}('D')
      $$
- **Step-by-Step Worked Execution Trace on $\text{"URDL"}$:**
  - Initialize origin state:
    $$
    x = 0, \quad y = 0
    $$
  - **Move 1 ($c = \text{'U'}$):**
    - Step vertical position:
      $$
      y \leftarrow 0 + 1 = \mathbf{1}
      $$
    - Position: $(x, y) = (0, 1)$.
  - **Move 2 ($c = \text{'R'}$):**
    - Step horizontal position:
      $$
      x \leftarrow 0 + 1 = \mathbf{1}
      $$
    - Position: $(x, y) = (1, 1)$.
  - **Move 3 ($c = \text{'D'}$):**
    - Step vertical position:
      $$
      y \leftarrow 1 - 1 = \mathbf{0}
      $$
    - Position: $(x, y) = (1, 0)$.
  - **Move 4 ($c = \text{'L'}$):**
    - Step horizontal position:
      $$
      x \leftarrow 1 - 1 = \mathbf{0}
      $$
    - Position: $(x, y) = (0, 0)$.
  - **Step 5: Origin Check:**
    - Final coordinates:
      $$
      x = 0, \quad y = 0
      $$
    - Verification:
      $$
      (x == 0) \land (y == 0) \implies \mathbf{True!}
      $$
    - Return **`true`**.
- **Vertical Cancellation Only ($moves = \text{"UD"}$):**
  - $t = 1$ (`'U'`): $(0, 1)$
  - $t = 2$ (`'D'`): $(0, 0)$
  - Result: **`true`**.
- **Horizontal Drift Failure ($moves = \text{"LL"}$):**
  - $t = 1$ (`'L'`): $(-1, 0)$
  - $t = 2$ (`'L'`): $(-2, 0)$
  - $x = -2 \ne 0 \implies$ Return **`false`**.
- **Odd Total Length Invariant:**
  - If $|moves|$ is odd (e.g. $|moves| = 3$), the robot can **never** return to origin because each step changes the $L_1$ taxicab distance by $\pm 1$ ($x + y \pmod 2 \ne 0$).

This instance demonstrates discrete vector summation over orthogonal basis dimensions, mathematically proves why conservation of directional counts is both necessary and sufficient for closed-loop path closure, and derives $O(N)$ execution time and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a sequence of robot moves (`'U'`, `'D'`, `'L'`, `'R'`):
Starting at $(0, 0)$, determine if the robot **ends up at the origin $(0, 0)$**.

```text
moves = "URDL"

Start at: (0, 0)
  1. 'U' -> ( 0,  1)
  2. 'R' -> ( 1,  1)
  3. 'D' -> ( 1,  0)
  4. 'L' -> ( 0,  0)  <-- Returned to origin!

Result: true
```

### The Invariant of Direct Cancellation
- For the robot to return to the origin:
  - Every upward step must be cancelled by a downward step: $\text{count}(U) = \text{count}(D)$.
  - Every rightward step must be cancelled by a leftward step: $\text{count}(R) = \text{count}(L)$.
- Order of execution is completely irrelevant to the final coordinate.

---

## 2. Conceptual Foundation & Invariants

### 1. The Vector Summation:
$$
(x_{final}, \; y_{final}) = \sum_{c \in moves} \vec{v}(c)
$$
where:
$$
\vec{v}(U) = (0, 1), \quad \vec{v}(D) = (0, -1), \quad \vec{v}(R) = (1, 0), \quad \vec{v}(L) = (-1, 0)
$$

### 2. The Equilibrium Predicate:
$$
\text{returnCircle} \iff (x_{final} == 0 \land y_{final} == 0)
$$

> **Abelian Path Homology Invariant.** The total displacement group homomorphism $\Phi: \Sigma^* \to \mathbb{Z}^2$ is abelian, rendering the final coordinates invariant under any permutation of the movement instructions.

---

## 3. Step-by-Step Worked Execution

We trace $moves = \text{"URDL"}$:

---

### Step 1: Initialize
- $x = 0, y = 0$.

---

### Step 2: Step 'U'
- $y \leftarrow 1$. Pos: $(0, 1)$.

---

### Step 3: Step 'R'
- $x \leftarrow 1$. Pos: $(1, 1)$.

---

### Step 4: Step 'D'
- $y \leftarrow 0$. Pos: $(1, 0)$.

---

### Step 5: Step 'L'
- $x \leftarrow 0$. Pos: $(0, 0)$.

---

### Step 6: Verify
- $x = 0$ and $y = 0 \implies \mathbf{true}$.

---

## 4. Complete Execution Trace

| Move Index $t$ | Move Command $c$ | Axis Affected | Coordinate Update | Current Position $(x, y)$ |
|:---:|:---:|:---:|:---:|:---:|
| $0$ | — | — | Initial state | $(0, 0)$ |
| $1$ | `'U'` | $+y$ | $y \leftarrow 0 + 1 = 1$ | $(0, 1)$ |
| $2$ | `'R'` | $+x$ | $x \leftarrow 0 + 1 = 1$ | $(1, 1)$ |
| $3$ | `'D'` | $-y$ | $y \leftarrow 1 - 1 = 0$ | $(1, 0)$ |
| $4$ | `'L'` | $-x$ | $x \leftarrow 1 - 1 = 0$ | **$(0, 0)$** |
| **Conclusion** | — | — | Final coordinates $(0, 0)$ | **`true`** |

---

## 5. Boundary Cases & Failure Modes

- **Odd Length ($|moves| = 2k + 1$):** Mathematically impossible to return to origin $\implies$ always `false`.
- **Empty Moves ($moves = \text{""}$):** Remains at $(0, 0) \implies$ `true`.
- **Large Loop ($10^5$ moves of $\text{"UD"}$):** Accumulators stay at 0 $\implies$ `true`.
- **Pure Drift ($\text{"RRRRR"}$):** $x = 5, y = 0 \implies$ `false`.

---

## 6. Traps & Common Anti-Patterns

- **Checking Intermittent Origin Visits:** The problem only asks if the robot ends up at the origin **after all moves are finished**, not whether it touched the origin midway through.
- **Using 2D Matrix Grids:** Simulating a physical 2D grid array causes memory overflows for long move sequences. Use simple scalar integer counters $x$ and $y$.
- **Ignoring Parity Pre-Check:** An odd-length string cannot possibly be balanced; while simulating it works, recognizing the parity invariant provides deep structural clarity.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - A single linear pass through the $N$ move characters: $\mathcal{O}(N)$.
  - For $N = 2 \times 10^4$, executes in $< 1$ ms.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space (only two integer accumulators $x$ and $y$).
