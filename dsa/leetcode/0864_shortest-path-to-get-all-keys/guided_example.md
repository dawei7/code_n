# Guided Example: Shortest Path to Get All Keys

We trace the step-by-step state space expansion, bitmask key representation, lock passage validation, visited state deduplication $(x, y, \text{mask})$, and breadth-first search wave propagation on representative grid labyrinths:

- **Input:**
  $$
  grid = \begin{bmatrix}
  \text{"@.a.."} \\
  \text{"\#\#\#.\#"} \\
  \text{"b.A.B"}
  \end{bmatrix}
  $$
- **Required output:** `8`
  - Labyrinth symbols & traversal rules:
    - `@`: Starting location of the explorer at $(0, 0)$.
    - `.`: Empty passable cell.
    - `#`: Impassable stone wall.
    - Lowercase letters (`'a'`, `'b'`, $\dots$): Keys that can be picked up.
    - Uppercase letters (`'A'`, `'B'`, $\dots$): Locks that require the corresponding lowercase key to open.
    - Moves: Up, Down, Left, Right ($1$ step per move).
    - Keys in this maze:
      - Key `'a'` at coordinate $(0, 2)$.
      - Key `'b'` at coordinate $(2, 0)$.
      - Total keys: $K = 2$.
    - Target completion condition:
      - Collect all $K = 2$ keys (target bitmask $2^2 - 1 = 3 = 11_2$).
    - Path trace:
      - Step 0: Start at $(0, 0)$ with $\text{mask} = 00_2$.
      - Step 1: Move East to $(0, 1)$.
      - Step 2: Move East to $(0, 2)$. Collect key `'a'`! New $\text{mask} = 01_2$.
      - Step 3: Move East to $(0, 3)$ (bypassing wall barrier at row 1).
      - Step 4: Move South to $(1, 3)$.
      - Step 5: Move South to $(2, 3)$.
      - Step 6: Move West to $(2, 2)$ (Lock `'A'`). We possess key `'a'`, so door opens!
      - Step 7: Move West to $(2, 1)$.
      - Step 8: Move West to $(2, 0)$. Collect key `'b'`! New $\text{mask} = 11_2$ (All keys collected!).
      - Minimum total steps: **`8`**.
- **State-Augmented Graph (Product Automaton) Invariant:**
  - **The Revisit Paradox:**
    - In standard BFS, a cell $(x, y)$ can only be visited once.
    - Here, an explorer may need to walk down a dead-end corridor to pick up a key, and then **walk back over the exact same cells**.
    - Furthermore, doors that were previously impassable become passable once a key is acquired.
  - **The 3D State Coordinate $(x, y, \text{mask})$:**
    - We augment the physical 2D plane with an orthogonal discrete dimension: the bitmask of collected keys.
    - If there are $K$ keys, there are $2^K$ discrete key configurations:
      $$
      \text{State} = (x, y, \text{mask}) \in [0, m-1] \times [0, n-1] \times [0, 2^K - 1]
      $$
    - Visiting cell $(x, y)$ with $\text{mask}_1$ does **not** block visiting $(x, y)$ with a richer $\text{mask}_2$.
    - Since every step has unit edge weight ($1$), standard BFS on the product graph guarantees the shortest path to any state with $\text{mask} = 2^K - 1$.

---

## 1. Instance & Teaching Goal

Given the maze with walls blocking row 1 except at column 3, find the minimum steps from `@` to collect keys `'a'` and `'b'`.

```text
Row 0:  @  .  a  .  .
Row 1:  #  #  #  .  #
Row 2:  b  .  A  .  B

Step 0: Start at (0, 0), keys = none (mask = 00)
Step 1: (0, 1), keys = none (mask = 00)
Step 2: (0, 2), collect key 'a' (mask = 01)
Step 3: (0, 3), keys = 'a' (mask = 01)
Step 4: (1, 3), keys = 'a' (mask = 01)
Step 5: (2, 3), keys = 'a' (mask = 01)
Step 6: (2, 2), unlock 'A' with key 'a' (mask = 01)
Step 7: (2, 1), keys = 'a' (mask = 01)
Step 8: (2, 0), collect key 'b' (mask = 11) -> ALL KEYS!

Shortest Path Length = 8
```

The teaching goal is to show how representing keys as bit flags turns a multi-agent inventory problem into single-source BFS on a layered graph.

---

## 2. Conceptual Foundation & Invariants

### 1. Bitmask Representation:
For $K$ keys labeled `'a'` through $\text{chr}(\text{ord}('a') + K - 1)$:
$$
\text{bit\_index}(c) = \text{ord}(c) - \text{ord}('a')
$$
$$
\text{target\_mask} = (1 \ll K) - 1
$$

### 2. Transition Rules:
From state $(x, y, \text{mask})$, moving to neighbor $(x', y')$:
- If $(x', y')$ is out of bounds or $grid[x'][y'] == \text{'\#'}$: **Invalid move**.
- If $grid[x'][y']$ is an uppercase lock $L$:
  $$
  \text{Can pass} \iff (\text{mask} \ \& \ (1 \ll (\text{ord}(L) - \text{ord}('A')))) \ne 0
  $$
- If $grid[x'][y']$ is a lowercase key $k$:
  $$
  \text{new\_mask} = \text{mask} \mid (1 \ll (\text{ord}(k) - \text{ord}('a')))
  $$
- Otherwise (empty cell `.` or `@`):
  $$
  \text{new\_mask} = \text{mask}
  $$

---

## 3. Step-by-Step Worked Execution

Total keys in maze: `'a'`, `'b'` $\implies K = 2$.
Target mask: $(1 \ll 2) - 1 = 3$ (binary `11`).
Start state: $(0, 0, 0)$, distance $0$.

---

### Step 1: Distance 0 to 1
- Pop $(0, 0, 00_2)$.
- Valid neighbor:
  - $(0, 1)$ is `.`: enqueue $(0, 1, 00_2)$.
- South neighbor $(1, 0)$ is `#` (blocked).
- Distance: $1$.

---

### Step 2: Distance 1 to 2
- Pop $(0, 1, 00_2)$.
- Valid neighbor:
  - $(0, 2)$ has key `'a'`.
  - Update mask: $00_2 \mid (1 \ll 0) = 01_2$.
  - Enqueue $(0, 2, 01_2)$.
- South neighbor $(1, 1)$ is `#` (blocked).
- Distance: $2$.

---

### Step 3: Distance 2 to 3
- Pop $(0, 2, 01_2)$.
- Valid neighbors:
  - $(0, 3)$ is `.`: enqueue $(0, 3, 01_2)$.
  - $(0, 1)$ is `.`: can revisit $(0, 1, 01_2)$ because mask is now $01_2$ (different state layer!).
- South neighbor $(1, 2)$ is `#` (blocked).
- Distance: $3$.

---

### Step 4: Distance 3 to 4
- From $(0, 3, 01_2)$, move South to $(1, 3, 01_2)$ (passable gap in wall).
- Enqueue $(1, 3, 01_2)$.
- Distance: $4$.

---

### Step 5: Distance 4 to 5
- From $(1, 3, 01_2)$, move South to $(2, 3, 01_2)$.
- Enqueue $(2, 3, 01_2)$.
- Distance: $5$.

---

### Step 6: Distance 5 to 6
- From $(2, 3, 01_2)$, inspect West neighbor $(2, 2)$:
  - Cell contains lock `'A'`.
  - Required key bit: $\text{ord}('A') - \text{ord}('A') = 0$.
  - Mask check: $01_2 \ \& \ (1 \ll 0) = 1 \ne 0 \implies$ **Lock Opened!**
  - Enqueue $(2, 2, 01_2)$.
- Distance: $6$.

---

### Step 7: Distance 6 to 7
- From $(2, 2, 01_2)$, move West to $(2, 1, 01_2)$.
- Enqueue $(2, 1, 01_2)$.
- Distance: $7$.

---

### Step 8: Distance 7 to 8
- From $(2, 1, 01_2)$, move West to $(2, 0)$:
  - Cell contains key `'b'`.
  - Update mask: $01_2 \mid (1 \ll 1) = 11_2 = 3$.
  - Check target: $11_2 == \text{target\_mask}$!
  - **All keys acquired!**
- **Return: `8`**.

---

## 4. Complete Execution Trace

| Step (Distance) | Position $(x, y)$ | Cell Type | Keys Held | Bitmask | Action / Decision | Target Mask ($11_2$) Met? |
|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| $0$ | $(0, 0)$ | `@` (Start) | None | $00_2$ | Enqueue initial state | No |
| $1$ | $(0, 1)$ | `.` | None | $00_2$ | Move East | No |
| $2$ | $(0, 2)$ | `'a'` (Key) | `{'a'}` | $01_2$ | **Acquire key `'a'`** | No |
| $3$ | $(0, 3)$ | `.` | `{'a'}` | $01_2$ | Move East around wall | No |
| $4$ | $(1, 3)$ | `.` | `{'a'}` | $01_2$ | Move South through gap | No |
| $5$ | $(2, 3)$ | `.` | `{'a'}` | $01_2$ | Move South to bottom row | No |
| $6$ | $(2, 2)$ | `'A'` (Lock) | `{'a'}` | $01_2$ | **Unlock door `'A'`** | No |
| $7$ | $(2, 1)$ | `.` | `{'a'}` | $01_2$ | Move West towards `'b'` | No |
| **$8$** | **$(2, 0)$** | **`'b'` (Key)** | **`{'a', 'b'}`** | **$11_2$** | **Acquire key `'b'`** | **`Yes (Return 8)`** |

---

## 5. Boundary Cases & Failure Modes

- **Unreachable Keys Behind Walls:** If a key is completely surrounded by `#`, the queue exhausts without reaching target mask $\implies$ returns $-1$.
- **Cyclic Dependency (Key Locked Behind Its Own Door):** If key `'a'` is locked behind door `'A'` and no other path exists, the door check permanently fails $\implies$ returns $-1$.
- **Zero Keys ($K = 0$):** Target mask is $0$; initial state matches immediately $\implies$ returns $0$.
- **Maximum Keys ($K = 6$):** State space has $2^6 = 64$ layers, perfectly bounded.

---

## 6. Traps & Common Anti-Patterns

- **Standard 2D Visited Array:** Marking $(x, y)$ as visited without the mask prevents backtracking out of dead ends after collecting a key.
- **Dijkstra Overkill:** Because every step has edge weight $1$, standard FIFO queue BFS runs in $\mathcal{O}(V)$ time, whereas Dijkstra adds an unnecessary $\mathcal{O}(\log V)$ priority queue overhead.
- **Using String Sets for Key Storage:** Representing key sets as strings or tuples creates heavy hash hashing overhead; an integer bitmask uses single-cycle bitwise registers.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Grid has $m \times n$ cells ($m, n \le 30$).
  - Maximum keys $K \le 6 \implies 2^K \le 64$ layers.
  - State space vertices: $|V| = m \cdot n \cdot 2^K \le 30 \times 30 \times 64 = 57,600$.
  - Each state has at most 4 edges: $|E| \le 4 \cdot |V| \approx 230,400$.
  - Breadth-first search runs in $\mathcal{O}(|V| + |E|)$ time, completing in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - Visited hash table and BFS queue store at most $|V|$ states: $\mathcal{O}(m \cdot n \cdot 2^K)$ space.
