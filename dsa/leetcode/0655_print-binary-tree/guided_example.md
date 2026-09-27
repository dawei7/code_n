# Guided Example: Print Binary Tree

We trace the step-by-step tree height computation ($h = \max(\text{depth})$), matrix dimension derivation ($m = h + 1, \; n = 2^{h+1} - 1$), top-level center anchoring ($[0, (n-1)/2]$), recursive dyadic coordinate bifurcation ($c \pm 2^{h - r - 1}$), sparse empty-string padding, and 2D formatted text grid layout on representative binary trees:

- **Input:**
  - Tree: $root = [1, 2, 3, \text{null}, 4]$
  - Tree structure:
    ```text
          1
        /   \
       2     3
        \
         4
    ```
- **Required output:**
  ```text
  [
    ["",  "",  "",  "1", "",  "",  ""],
    ["",  "2", "",  "",  "",  "3", ""],
    ["",  "",  "4", "",  "",  "",  ""]
  ]
  ```
  - Formatting layout rules:
    1. Let $h$ be the 0-indexed height of the tree (longest edge path from root to any leaf).
    2. Number of rows: $m = h + 1$.
    3. Number of columns: $n = 2^{h + 1} - 1$ (width of a full binary tree of depth $h$).
    4. Place the root at $[r, c] = [0, \; (n - 1) / 2]$.
    5. For any node placed at row $r$ and column $c$:
       - Left child is placed at row $r + 1$ and column $c - 2^{h - r - 1}$.
       - Right child is placed at row $r + 1$ and column $c + 2^{h - r - 1}$.
    6. All remaining cells must be empty strings `""`.
- **Dyadic Grid Geometry & Midpoint Bifurcation Invariant:**
  - **Grid Width ($2^{h+1} - 1$):**
    - A binary tree of height $h$ can have up to $2^h$ leaves at its bottom level.
    - Each leaf requires 1 cell, separated by alternating blank cells, producing exactly $2^{h+1} - 1$ columns.
  - **Dyadic Step Size ($2^{h - r - 1}$):**
    - At row $r$, the horizontal displacement between a parent and its children halves at each successive level:
      $$
      \Delta c(r) = 2^{h - r - 1}
      $$
    - At row $r = 0$: $\Delta c = 2^{h - 1}$
    - At row $r = h - 1$: $\Delta c = 2^0 = 1$
    - This exact power-of-two spacing guarantees that:
      - No two nodes ever share the same cell.
      - Left and right subtrees occupy completely disjoint column intervals $[L, c - 1]$ and $[c + 1, R]$.
- **Step-by-Step Worked Execution Trace:**
  - **Step 1: Compute Tree Height ($h$):**
    - Leaf Node 3: depth 1.
    - Leaf Node 4: depth 2 (path: $1 \to 2 \to 4$).
    - Longest path has 2 edges:
      $$
      h = 2
      $$
  - **Step 2: Calculate Grid Dimensions:**
    - Rows:
      $$
      m = h + 1 = 2 + 1 = \mathbf{3}
      $$
    - Columns:
      $$
      n = 2^{h + 1} - 1 = 2^{3} - 1 = 8 - 1 = \mathbf{7}
      $$
    - Initialize $3 \times 7$ matrix filled with `""`:
      $$
      ans = \begin{bmatrix}
      \text{""} & \text{""} & \text{""} & \text{""} & \text{""} & \text{""} & \text{""} \\
      \text{""} & \text{""} & \text{""} & \text{""} & \text{""} & \text{""} & \text{""} \\
      \text{""} & \text{""} & \text{""} & \text{""} & \text{""} & \text{""} & \text{""}
      \end{bmatrix}
      $$
  - **Step 3: Place Root (Node 1):**
    - Row $r = 0$.
    - Column:
      $$
      c = \frac{n - 1}{2} = \frac{7 - 1}{2} = \frac{6}{2} = \mathbf{3}
      $$
    - Assign: $ans[0][3] = \text{"1"}$.
    - Horizontal displacement for children ($r = 0$):
      $$
      \Delta c = 2^{h - r - 1} = 2^{2 - 0 - 1} = 2^1 = \mathbf{2}
      $$
  - **Step 4: Place Left Child of 1 (Node 2):**
    - Row: $r = 0 + 1 = \mathbf{1}$.
    - Column:
      $$
      c = 3 - \Delta c = 3 - 2 = \mathbf{1}
      $$
    - Assign: $ans[1][1] = \text{"2"}$.
    - Horizontal displacement for children of 2 ($r = 1$):
      $$
      \Delta c = 2^{h - r - 1} = 2^{2 - 1 - 1} = 2^0 = \mathbf{1}
      $$
    - Node 2 has no left child $\implies \mathbf{null}$.
  - **Step 5: Place Right Child of 2 (Node 4):**
    - Row: $r = 1 + 1 = \mathbf{2}$.
    - Column:
      $$
      c = 1 + \Delta c = 1 + 1 = \mathbf{2}
      $$
    - Assign: $ans[2][2] = \text{"4"}$.
    - Node 4 is a leaf (halts).
  - **Step 6: Place Right Child of 1 (Node 3):**
    - Row: $r = 0 + 1 = \mathbf{1}$.
    - Column:
      $$
      c = 3 + \Delta c = 3 + 2 = \mathbf{5}
      $$
    - Assign: $ans[1][5] = \text{"3"}$.
    - Node 3 has no children $\implies \mathbf{null}$ (halts).
  - **Step 7: Final Formatted Grid:**
    $$
    \begin{bmatrix}
    \text{""} & \text{""} & \text{""} & \mathbf{\text{"1"}} & \text{""} & \text{""} & \text{""} \\
    \text{""} & \mathbf{\text{"2"}} & \text{""} & \text{""} & \text{""} & \mathbf{\text{"3"}} & \text{""} \\
    \text{""} & \text{""} & \mathbf{\text{"4"}} & \text{""} & \text{""} & \text{""} & \text{""}
    \end{bmatrix}
    $$
- **Two-Node Tree ($root = [1, 2]$):**
  - Height $h = 1$. Rows $m = 2$, Columns $n = 2^2 - 1 = 3$.
  - Root 1 at $[0, 1]$.
  - Left child 2 at $[1, 1 - 2^0] = [1, 0]$.
  - Result:
    $$
    \begin{bmatrix}
    \text{""} & \mathbf{\text{"1"}} & \text{""} \\
    \mathbf{\text{"2"}} & \text{""} & \text{""}
    \end{bmatrix}
    $$
- **Single Root Node ($root = [1]$):**
  - Height $h = 0 \implies m = 1, n = 1$.
  - Grid: `[["1"]]`.

This instance demonstrates dyadic fractional subdivision and recursive grid embedding, mathematically proves why power-of-two displacements guarantee zero-overlap spatial projection, and derives $O(h \cdot 2^h)$ runtime and $O(h \cdot 2^h)$ output matrix space bounds.

---

## 1. Instance & Teaching Goal

Given the root of a binary tree:
Format and print the tree in a 2D string grid of size $m \times n$:
- Height $h$, rows $m = h + 1$, columns $n = 2^{h+1} - 1$.
- Root at $[0, (n - 1) / 2]$.
- Children offset horizontally by $2^{h - r - 1}$.

```text
Tree:
      1
    /   \
   2     3
    \
     4

Height h = 2 -> Rows m = 3, Cols n = 2^(2+1) - 1 = 7

Row 0: [ "",  "",  "", "1",  "",  "",  "" ]  (root at col 3)
Row 1: [ "", "2",  "",  "",  "", "3",  "" ]  (col 3-2=1, 3+2=5)
Row 2: [ "",  "", "4",  "",  "",  "",  "" ]  (col 1+1=2)
```

### The Invariant of Dyadic Halving
- At each successive level downwards ($r \to r + 1$), the branch separation shrinks by a factor of 2:
  $$
  \Delta c = 2^{h - r - 1}
  $$
- This fractal division ensures that left and right subtrees never collide.

---

## 2. Conceptual Foundation & Invariants

### 1. Dimension Formulas:
$$
h = \text{height}(root)
$$
$$
m = h + 1, \quad n = 2^{h+1} - 1
$$

### 2. Recursive Child Coordinates:
If parent is at $(r, c)$:
$$
\text{left} = (r + 1, \; c - 2^{h - r - 1})
$$
$$
\text{right} = (r + 1, \; c + 2^{h - r - 1})
$$

> **Dyadic Interval Splitting Invariant.** Placing node $u$ at midpoint $(L + R)/2$ divides column interval $[L, R]$ into two open sub-intervals of length $(R - L)/2$, mapping the binary tree topology homeomorphically onto a 1D Cantor-like coordinate set.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Compute Dimensions
- $h = 2 \implies m = 3, n = 7$.

---

### Step 2: Place Root 1
- $r = 0, c = (7 - 1) / 2 = 3$.
- $ans[0][3] = \text{"1"}$.
- Step $\Delta = 2^{2 - 0 - 1} = 2$.

---

### Step 3: Place Left Child 2
- $r = 1, c = 3 - 2 = 1$.
- $ans[1][1] = \text{"2"}$.
- Step $\Delta = 2^{2 - 1 - 1} = 1$.

---

### Step 4: Place Right Child 4 of Node 2
- $r = 2, c = 1 + 1 = 2$.
- $ans[2][2] = \text{"4"}$.

---

### Step 5: Place Right Child 3 of Node 1
- $r = 1, c = 3 + 2 = 5$.
- $ans[1][5] = \text{"3"}$.

---

## 4. Complete Execution Trace

| Node Visited | Node Value | Current Row $r$ | Current Column $c$ | Offset $\Delta c$ | Placement |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Node 1 | `1` | $0$ | $3$ | $2^1 = 2$ | $ans[0][3] = \text{"1"}$ |
| Node 2 | `2` | $1$ | $3 - 2 = 1$ | $2^0 = 1$ | $ans[1][1] = \text{"2"}$ |
| **Node 4** | **`4`** | **$2$** | **$1 + 1 = 2$** | — | **$ans[2][2] = \text{"4"}$** |
| Node 3 | `3` | $1$ | $3 + 2 = 5$ | $2^0 = 1$ | $ans[1][5] = \text{"3"}$ |

---

## 5. Boundary Cases & Failure Modes

- **Single Node ($root = [1]$):** $h = 0 \implies 1 \times 1$ matrix `[["1"]]`.
- **Complete Balanced Tree:** Symmetrically fills the grid.
- **Skewed Tree (Linear chain of depth 5):** Matrix width expands to $2^5 - 1 = 31$; placements remain accurate without index collisions.
- **Maximum Height ($h = 10$):** $n = 2^{11} - 1 = 2047$ columns; easily fits within standard memory budgets.

---

## 6. Traps & Common Anti-Patterns

- **Using 1-Indexed Height ($h = \text{number of levels}$):** The problem defines height as the number of edges ($h = 0$ for single node). If you use $h = 1$ for a single node, the matrix dimensions become $2 \times 3$ instead of $1 \times 1$.
- **Bit Shift Precedence in C++/Python:** In Python, `2 ** h - r - 1` without parentheses evaluates as `(2**h) - r - 1` instead of `2**(h - r - 1)`. Always parenthesize the exponent!
- **Filling with Spaces Instead of Empty Strings:** The problem requires empty strings `""`, not space characters `" "`.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Finding tree height: $\mathcal{O}(N)$ where $N$ is number of nodes.
  - Initializing $m \times n$ matrix: $\mathcal{O}(m \cdot n) = \mathcal{O}(h \cdot 2^h)$.
  - Traversing tree and filling cells: $\mathcal{O}(N)$.
  - Total Time: $\mathcal{O}(h \cdot 2^h)$. Since $h \le 10$, $h \cdot 2^h \le 10 \times 1024 \approx 10^4$ operations, executing in $< 2$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(h \cdot 2^h)$ space to store the output grid.