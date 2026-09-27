# Guided Example: Swap Adjacent in LR String

We trace the step-by-step non-passable particle kinematics (`'L'` and `'R'`), directional displacement constraints (`'L'` moves left $i \ge j$, `'R'` moves right $i \le j$), non-`'X'` invariant token projection ($s \setminus \{X\} == e \setminus \{X\}$), dual-pointer index synchronization ($i, j$), invalid movement rejection, and transformation reachability verification on representative string pairs:

- **Input:**
  $$
  start = \text{"RXXLRXRXL"}
  $$
  $$
  end = \text{"XRLXXRRLX"}
  $$
- **Required output:** `true`
  - Permissible transformation rules:
    - You can replace `"XL"` with `"LX"`.
      - **Physical meaning:** Character `'L'` can slide to the **left** into adjacent spaces (`'X'`).
      - An `'L'` can never move right. If an `'L'` in $start$ at index $i$ corresponds to an `'L'` in $end$ at index $j$, it must satisfy:
        $$
        i \ge j
        $$
    - You can replace `"RX"` with `"XR"`.
      - **Physical meaning:** Character `'R'` can slide to the **right** into adjacent spaces (`'X'`).
      - An `'R'` can never move left. If an `'R'` in $start$ at index $i$ corresponds to an `'R'` in $end$ at index $j$, it must satisfy:
        $$
        i \le j
        $$
    - **Particle Collision Rule:**
      - `'L'` and `'R'` can **never cross over each other** (neither `"LR"` nor `"RL"` can swap).
      - Consequently, the sequence of non-`'X'` characters must be **identically equal** in both strings!
    - For $\text{"RXXLRXRXL"}$ and $\text{"XRLXXRRLX"}$:
      - Non-`'X'` sequence in $start$: `['R', 'L', 'R', 'R', 'L']`.
      - Non-`'X'` sequence in $end$: `['R', 'L', 'R', 'R', 'L']`.
      - Order matches.
      - Indices comparison:
        - 1st `'R'`: from index 0 to index 1 ($0 \le 1$, valid rightward slide).
        - 1st `'L'`: from index 3 to index 2 ($3 \ge 2$, valid leftward slide).
        - 2nd `'R'`: from index 4 to index 5 ($4 \le 5$, valid rightward slide).
        - 3rd `'R'`: from index 6 to index 6 ($6 \le 6$, stationary).
        - 2nd `'L'`: from index 8 to index 8 ($8 \ge 8$, stationary).
      - All movements are physically valid $\implies$ return **`true`**.
- **Two-Pointer Particle Tracking Invariant:**
  - **The Relative Order Invariant:**
    - Because particles cannot jump over one another, the $k$-th non-`'X'` particle in $start$ must be matched with the $k$-th non-`'X'` particle in $end$.
  - **Dual Pointers ($i, j$):**
    - Skip all `'X'` characters in $start$ using pointer $i$.
    - Skip all `'X'` characters in $end$ using pointer $j$.
    - **Verification Conditions at Each Step:**
      1. If both $i$ and $j$ reach the end of their strings ($i \ge n \land j \ge n$): valid transformation completed $\implies$ return `true`.
      2. If one pointer reaches the end before the other ($i \ge n \lor j \ge n$): particle counts mismatch $\implies$ return `false`.
      3. If $start[i] \ne end[j]$: particle identities mismatch (e.g. `'L'` vs `'R'`) $\implies$ return `false`.
      4. If $start[i] == \text{'L'}$ and $i < j$: `'L'` attempted to move right $\implies$ return `false`.
      5. If $start[i] == \text{'R'}$ and $i > j$: `'R'` attempted to move left $\implies$ return `false`.
    - If all checks pass, advance $i \leftarrow i + 1, j \leftarrow j + 1$.
- **Step-by-Step Worked Execution Trace on the Sample Strings:**
  - Length $n = 9$.
  - **Pair 1 (1st Particle):**
    - Advance $i$ to first non-`'X'` in $start$: $i = 0$ ($start[0] = \text{'R'}$).
    - Advance $j$ to first non-`'X'` in $end$: $end[0] = \text{'X'}$, so $j = 1$ ($end[1] = \text{'R'}$).
    - Compare tokens: $start[0] == end[1] == \text{'R'} \implies \mathbf{Match.}$
    - Directional check: Particle `'R'` moves from $i = 0$ to $j = 1$.
      $$
      i \le j \iff 0 \le 1 \implies \mathbf{Valid\ Rightward\ Shift!}
      $$
    - Advance: $i = 1, j = 2$.
  - **Pair 2 (2nd Particle):**
    - Advance $i$ past `'X'`s in $start$: $start[1]=\text{'X'}, start[2]=\text{'X'}, start[3]=\text{'L'} \implies i = 3$.
    - Advance $j$ past `'X'`s in $end$: $end[2] = \text{'L'} \implies j = 2$.
    - Compare tokens: $start[3] == end[2] == \text{'L'} \implies \mathbf{Match.}$
    - Directional check: Particle `'L'` moves from $i = 3$ to $j = 2$.
      $$
      i \ge j \iff 3 \ge 2 \implies \mathbf{Valid\ Leftward\ Shift!}
      $$
    - Advance: $i = 4, j = 3$.
  - **Pair 3 (3rd Particle):**
    - Advance $i$: $start[4] = \text{'R'} \implies i = 4$.
    - Advance $j$: $end[3]=\text{'X'}, end[4]=\text{'X'}, end[5]=\text{'R'} \implies j = 5$.
    - Compare tokens: $start[4] == end[5] == \text{'R'} \implies \mathbf{Match.}$
    - Directional check: Particle `'R'` moves from $i = 4$ to $j = 5$.
      $$
      i \le j \iff 4 \le 5 \implies \mathbf{Valid\ Rightward\ Shift!}
      $$
    - Advance: $i = 5, j = 6$.
  - **Pair 4 (4th Particle):**
    - Advance $i$: $start[5]=\text{'X'}, start[6]=\text{'R'} \implies i = 6$.
    - Advance $j$: $end[6] = \text{'R'} \implies j = 6$.
    - Compare tokens: $start[6] == end[6] == \text{'R'} \implies \mathbf{Match.}$
    - Directional check: $i \le j \iff 6 \le 6 \implies \mathbf{Valid.}$
    - Advance: $i = 7, j = 7$.
  - **Pair 5 (5th Particle):**
    - Advance $i$: $start[7]=\text{'X'}, start[8]=\text{'L'} \implies i = 8$.
    - Advance $j$: $end[7]=\text{'X'}, end[8]=\text{'L'} \implies j = 8$.
    - Compare tokens: $start[8] == end[8] == \text{'L'} \implies \mathbf{Match.}$
    - Directional check: $i \ge j \iff 8 \ge 8 \implies \mathbf{Valid.}$
    - Advance: $i = 9, j = 9$.
  - **Termination:**
    - Both $i \ge 9$ and $j \ge 9$.
    - Output:
      $$
      ans = \mathbf{true}
      $$
- **Particle Direction Violation Trace ($start = \text{"LLR"}, end = \text{"RRL"}$):**
  - First particle in $start$ is `'L'`, but first particle in $end$ is `'R'`.
  - $start[i] \ne end[j]$ $\implies$ returns **`false`**.
- **Illegal Forward Slide Trace ($start = \text{"LXX"}, end = \text{"XXL"}$):**
  - Particle `'L'` at $i = 0$ needs to reach $j = 2$.
  - Since $start[i] == \text{'L'}$ and $i < j$ ($0 < 2$), `'L'` cannot slide right!
  - Returns **`false`**.

This instance demonstrates 1D unidirectional particle kinetics and monotonic coordinate projection, mathematically proves why conservation of non-empty symbol order coupled with partial order inequalities forms the necessary and sufficient reachability condition, and derives $O(N)$ execution time and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given two strings $start$ and $end$ of `'L'`, `'R'`, and `'X'`:
Can $start$ transform into $end$ by moving `'L'` left into `'X'` (`"XL" -> "LX"`) and `'R'` right into `'X'` (`"RX" -> "XR"`)?

```text
start = "RXXLRXRXL"
end   = "XRLXXRRLX"

Non-'X' sequence in start: [ 'R', 'L', 'R', 'R', 'L' ]
Non-'X' sequence in end:   [ 'R', 'L', 'R', 'R', 'L' ] (Identical!)

Movement checks:
  'R' moves from 0 to 1: 0 <= 1 -> OK (moves right)
  'L' moves from 3 to 2: 3 >= 2 -> OK (moves left)
  'R' moves from 4 to 5: 4 <= 5 -> OK (moves right)
  'R' moves from 6 to 6: 6 <= 6 -> OK (stationary)
  'L' moves from 8 to 8: 8 >= 8 -> OK (stationary)

Result: true
```

### The Invariant of Non-Crossing Particles
1. `'L'` and `'R'` cannot cross $\implies$ sequence of non-`'X'` characters must be identical.
2. `'L'` can only move **left** $\implies$ start index $i \ge$ end index $j$.
3. `'R'` can only move **right** $\implies$ start index $i \le$ end index $j$.

---

## 2. Conceptual Foundation & Invariants

### 1. Particle Sequence Congruence:
$$
\text{filter}(start, \ne \text{'X'}) = \text{filter}(end, \ne \text{'X'})
$$

### 2. Kinematic Direction Inequalities:
For the $k$-th particle at index $i$ in $start$ and index $j$ in $end$:
$$
\text{if } token == \text{'L'} \implies i \ge j
$$
$$
\text{if } token == \text{'R'} \implies i \le j
$$

> **Poset Path Reachability Invariant.** The string rewrite rules induce a distributive lattice of configurations where particles preserve their total ordering. Reachability is characterized by component-wise dominance relations on the coordinates $(x_1, \dots, x_k) \le (y_1, \dots, y_k)$.

---

## 3. Step-by-Step Worked Execution

We trace $start = \text{"RXXLRXRXL"}, end = \text{"XRLXXRRLX"}$:

---

### Step 1: Particle 1 `'R'`
- $start$ at 0, $end$ at 1 $\implies 0 \le 1$ (Valid right move).

---

### Step 2: Particle 2 `'L'`
- $start$ at 3, $end$ at 2 $\implies 3 \ge 2$ (Valid left move).

---

### Step 3: Particle 3 `'R'`
- $start$ at 4, $end$ at 5 $\implies 4 \le 5$ (Valid right move).

---

### Step 4: Particles 4 and 5
- `'R'` at 6 to 6 $\implies 6 \le 6$ (Valid).
- `'L'` at 8 to 8 $\implies 8 \ge 8$ (Valid).

---

### Step 5: Output
$$
\mathbf{true}
$$

---

## 4. Complete Execution Trace

| Particle # | Token Type | Start Index $i$ | End Index $j$ | Direction Inequality | Physically Valid? |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | `'R'` | $0$ | $1$ | $i \le j$ ($0 \le 1$) | Yes |
| $2$ | `'L'` | $3$ | $2$ | $i \ge j$ ($3 \ge 2$) | Yes |
| $3$ | `'R'` | $4$ | $5$ | $i \le j$ ($4 \le 5$) | Yes |
| $4$ | `'R'` | $6$ | $6$ | $i \le j$ ($6 \le 6$) | Yes |
| **$5$** | **`'L'`** | **$8$** | **$8$** | **$i \ge j$ ($8 \ge 8$)** | **Yes** |
| **Final** | — | — | — | — | **Result: `true`** |

---

## 5. Boundary Cases & Failure Modes

- **Token Type Mismatch ($start = \text{"X"}, end = \text{"L"}$):** One string has more particles than the other $\implies$ returns `false`.
- **Wrong Order ($start = \text{"LR"}, end = \text{"RL"}$):** Particles cannot cross $\implies$ returns `false`.
- **All Spaces ($start = \text{"XXX"}, end = \text{"XXX"}$):** Both pointers reach end with 0 particles $\implies$ returns `true`.
- **Backward Shift of `'R'` ($start = \text{"XR"}, end = \text{"RX"}$):** $i = 1 > j = 0 \implies$ `'R'` cannot slide left, returns `false`.

---

## 6. Traps & Common Anti-Patterns

- **Simulating Swaps Explicitly ($O(N^2)$ or BFS):** Simulating string replacements is exponential or quadratic. The invariant formulation allows determining reachability in a single linear scan!
- **Filtering Strings into Separate Lists:** Creating `[c for c in start if c != 'X']` uses extra memory and still requires index tracking. Two pointers $i, j$ iterate directly in $O(1)$ memory.
- **Forgetting End Bounds on Both Pointers:** When checking if one string ran out of particles early, ensure both pointers are tested for reaching length $N$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Both pointers $i$ and $j$ only advance forward from 0 to $N$: $\mathcal{O}(N)$.
  - Total Time: strictly linear $\mathcal{O}(N)$ where $N \le 10^4$. Completes in $< 1$ ms.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space (only index pointers $i, j$).
