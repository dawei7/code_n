# Guided Example: Falling Squares

We trace the step-by-step continuous interval projection ($[l, l + w - 1]$), open-boundary intersection modeling (shared boundary points do not stack), dynamic segment tree range-maximum querying ($base = \text{query}(l, r)$), square landing height calculation ($h = base + w$), range modification with lazy propagation, and running global peak elevation tracking on representative falling square drop events:

- **Input:** $positions = [[1, 2], [2, 3], [6, 1]]$
- **Required output:** `[2, 5, 5]`
  - Physics & geometry rules:
    - Each square drops straight down onto the horizontal X-axis or onto squares that have already landed.
    - Square dimensions: A square given as $[left, sideLength]$ occupies the horizontal interval:
      $$
      [left, \; left + sideLength]
      $$
    - Boundary intersection rule: Two squares must overlap along a **non-zero horizontal length** to rest on top of each other. Merely touching at a single point (e.g. $[1, 2]$ and $[2, 3]$ sharing point $2$) does NOT stack!
    - Discrete integer mapping: Stacking occurs across the integer interval:
      $$
      [l, \; r] = [left, \; left + sideLength - 1]
      $$
    - Objective: After each square drops, record the **maximum height** among all squares on the plane.
- **Dynamic Segment Tree & Range Maximum Invariant:**
  - **The Landing Base Height Invariant:**
    - When a square of width $w$ drops across interval $[l, r] = [left, left + w - 1]$:
      - It lands on whatever is highest underneath it within $[l, r]$.
      - The maximum surface height currently supporting that interval is:
        $$
        base = \max_{x \in [l, r]} \text{height}(x) = \text{query}(l, \; r)
        $$
      - If no squares lie beneath it, $base = 0$ (lands on the ground).
      - Its new top edge settles at height:
        $$
        h = base + w
        $$
  - **Range Assignment ($l \dots r \to h$):**
    - The new square covers the entire interval $[l, r]$ at uniform height $h$:
      $$
      \text{modify}(l, \; r, \; h)
      $$
  - **Running Peak Elevation:**
    - Maintain $mx = \max(mx, h)$.
    - Append $mx$ to the answer list after each drop.
- **Step-by-Step Worked Execution Trace on $[[1, 2], [2, 3], [6, 1]]$:**
  - Initialize Segment Tree spanning X-axis coordinate domain $[1, 10^9]$.
  - Global peak tracker: $mx = 0, \; ans = []$.
  - **Drop 1: Square $[1, 2]$ (left = 1, side = 2):**
    - Horizontal interval:
      $$
      [l, r] = [1, \; 1 + 2 - 1] = [1, \; 2]
      $$
    - Query supporting ground beneath $[1, 2]$:
      $$
      base = \text{query}(1, 2) = \mathbf{0}
      $$
    - Settle height:
      $$
      h = base + w = 0 + 2 = \mathbf{2}
      $$
    - Update interval $[1, 2]$ to height $2$:
      $$
      \text{modify}(1, 2, 2)
      $$
    - Update peak height:
      $$
      mx \leftarrow \max(0, 2) = \mathbf{2} \implies ans = [\mathbf{2}]
      $$
  - **Drop 2: Square $[2, 3]$ (left = 2, side = 3):**
    - Horizontal interval:
      $$
      [l, r] = [2, \; 2 + 3 - 1] = [2, \; 4]
      $$
    - Query supporting surface beneath $[2, 4]$:
      - Coordinate $2$ is covered by Square 1 (height 2).
      - Coordinates $3, 4$ are ground (height 0).
      - Maximum underlying height:
        $$
        base = \text{query}(2, 4) = \max(2, 0) = \mathbf{2}
        $$
    - Settle height:
      $$
      h = base + w = 2 + 3 = \mathbf{5}
      $$
      *(Square 2 lands on top of Square 1 at coordinate 2, elevating its top to 5)*
    - Update interval $[2, 4]$ to height $5$:
      $$
      \text{modify}(2, 4, 5)
      $$
    - Update peak height:
      $$
      mx \leftarrow \max(2, 5) = \mathbf{5} \implies ans = [2, \; \mathbf{5}]
      $$
  - **Drop 3: Square $[6, 1]$ (left = 6, side = 1):**
    - Horizontal interval:
      $$
      [l, r] = [6, \; 6 + 1 - 1] = [6, \; 6]
      $$
    - Query supporting surface beneath $[6, 6]$:
      $$
      base = \text{query}(6, 6) = \mathbf{0}
      $$
    - Settle height:
      $$
      h = base + w = 0 + 1 = \mathbf{1}
      $$
      *(Square 3 drops far away on empty ground at $x = 6$, settling at height 1)*
    - Update interval $[6, 6]$ to height $1$:
      $$
      \text{modify}(6, 6, 1)
      $$
    - Update peak height:
      $$
      mx \leftarrow \max(5, 1) = \mathbf{5} \implies ans = [2, \; 5, \; \mathbf{5}]
      $$
  - **Step 4: Output Trajectory:**
    $$
    ans = [\mathbf{2}, \; \mathbf{5}, \; \mathbf{5}]
    $$
- **Edge-Touching Without Stacking Trace ($positions = [[1, 5], [6, 2]]$):**
  - Square 1 occupies $[1, 1 + 5 - 1] = [1, 5]$ with height 5.
  - Square 2 occupies $[6, 6 + 2 - 1] = [6, 7]$.
  - The interval $[6, 7]$ does **not** overlap with $[1, 5]$!
  - Underlying base for $[6, 7]$ is $0$.
  - Square 2 lands on the ground at height 2.
  - Peaks: `[5, 5]`.
  - Stacking did not occur because they only share point 6 without positive area overlap.

This instance demonstrates dynamic range assignment and range maximum queries on continuous 1D spatial boundaries, mathematically proves why subtracting 1 from the upper endpoint correctly enforces interior open-interval stacking semantics, and derives $O(N \log X)$ runtime and $O(N \log X)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given squares falling on the X-axis:
Each square $[left, sideLength]$ drops until it hits another square or the ground.
After each square drops, record the **maximum height** on the entire board.

```text
Drops: [ [1, 2], [2, 3], [6, 1] ]

Drop 1: [1, 2] -> lands on ground [1, 2], top = 2
  Max height = 2

Drop 2: [2, 3] -> interval [2, 4], hits square 1 at x = 2 (height 2)
  Top = 2 + 3 = 5
  Max height = 5

Drop 3: [6, 1] -> lands on ground at [6, 6], top = 1
  Max height = max(5, 1) = 5

Result: [ 2, 5, 5 ]
```

### The Invariant of Open-Interval Boundary Contact
- Two squares only overlap in 2D space if they share an interior horizontal segment.
- Contact at a single boundary point (e.g. $[1, 2]$ and $[2, 5]$ meeting at $x = 2$) does NOT stack.
- Mapping each square to the discrete integer interval $[left, left + sideLength - 1]$ enforces this open-interval intersection naturally.

---

## 2. Conceptual Foundation & Invariants

### 1. Landing Height Query:
For square with parameters $(l, w)$:
$$
base = \text{query}(l, \; l + w - 1)
$$
$$
h = base + w
$$

### 2. Segment Tree Range Update:
$$
\text{modify}(l, \; l + w - 1, \; h)
$$
$$
mx \leftarrow \max(mx, \; h)
$$

> **Skyline Profile Monotonicity Invariant.** The upper boundary of the union of axis-aligned orthogonal squares forms a piecewise-constant step function whose point evaluations are strictly non-decreasing under sequential square additions.

---

## 3. Step-by-Step Worked Execution

We trace the sample drops:

---

### Step 1: Drop $[1, 2]$
- Range $[1, 2]$. $base = 0$.
- $h = 0 + 2 = 2$.
- Update $[1, 2] \to 2$.
- $mx = 2$.

---

### Step 2: Drop $[2, 3]$
- Range $[2, 4]$. $base = \text{query}(2, 4) = 2$.
- $h = 2 + 3 = 5$.
- Update $[2, 4] \to 5$.
- $mx = \max(2, 5) = \mathbf{5}$.

---

### Step 3: Drop $[6, 1]$
- Range $[6, 6]$. $base = 0$.
- $h = 0 + 1 = 1$.
- Update $[6, 6] \to 1$.
- $mx = \max(5, 1) = \mathbf{5}$.

---

### Step 4: Output
$$
[\mathbf{2}, \; \mathbf{5}, \; \mathbf{5}]
$$

---

## 4. Complete Execution Trace

| Drop Event $i$ | Square $[l, w]$ | Discrete Range $[l, r]$ | Queried Base Height | Settle Height $h = base + w$ | Updated Profile | System Peak $mx$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | $[1, 2]$ | $[1, 2]$ | $0$ (Ground) | $2$ | $[1, 2] \to 2$ | **`2`** |
| $2$ | $[2, 3]$ | $[2, 4]$ | $2$ (Hits sq 1) | $5$ | $[2, 4] \to 5$ | **`5`** |
| **$3$** | **$[6, 1]$** | **$[6, 6]$** | **$0$ (Ground)** | **$1$** | **$[6, 6] \to 1$** | **`5`** |

---

## 5. Boundary Cases & Failure Modes

- **Direct Vertical Stacking ($[[1, 2], [1, 2]]$):** Base of square 2 is 2 $\implies$ new top is $2 + 2 = 4$.
- **Edge Touching ($[1, 5]$ and $[6, 2]$):** Discrete intervals $[1, 5]$ and $[6, 7]$ are disjoint $\implies$ base is 0.
- **Large Coordinates ($left \le 10^8$):** Dynamic segment tree allocates nodes on-demand up to $10^9$ without memory blowup.
- **Single Drop ($N = 1$):** Returns `[w]`.

---

## 6. Traps & Common Anti-Patterns

- **Using Closed Intervals $[l, l + w]$:** Using $l + w$ without subtracting 1 causes adjacent squares that merely touch boundaries to falsely stack on top of each other!
- **Coordinate Array of Size $10^9$:** Trying to allocate an array of size $10^9$ causes Out Of Memory. Use either a dynamic node-based segment tree or coordinate compression.
- **$O(N^2)$ Pairwise Comparison:** Comparing each new square against all previous squares is $O(N^2)$; a segment tree reduces queries and updates to $O(\log C)$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - $N$ square drops.
  - Each drop performs 1 query and 1 range update in a dynamic segment tree of height $\approx 30$ ($\log_2 10^9$): $\mathcal{O}(\log C)$.
  - Total Time: $\mathcal{O}(N \log C)$. For $N = 1000$, executes in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N \log C)$ nodes allocated dynamically in the tree.
