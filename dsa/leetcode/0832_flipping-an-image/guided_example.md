# Guided Example: Flipping an Image

We trace the step-by-step horizontal row reflection (mirror reversal across the vertical midline), boolean bit inversion ($x \oplus 1$), two-pointer symmetric pair simultaneous reduction, cancelation property on unequal bits ($x \ne y \implies \text{unchanged}$), center element toggle on odd row lengths ($i == j \implies row[i] \oplus 1$), and in-place binary image transformation on representative image matrices:

- **Input:**
  $$
  image = \begin{bmatrix}
  1 & 1 & 0 \\
  1 & 0 & 1 \\
  0 & 0 & 0
  \end{bmatrix}
  $$
- **Required output:**
  $$
  \begin{bmatrix}
  1 & 0 & 0 \\
  0 & 1 & 0 \\
  1 & 1 & 1
  \end{bmatrix}
  $$
  - Image transformation rules:
    - You are given an $n \times n$ binary matrix $image$.
    - **Operation 1 (Horizontal Flip):** Reverse the order of elements in each row independently:
      $$
      [x_0, x_1, \dots, x_{n-1}] \longrightarrow [x_{n-1}, \dots, x_1, x_0]
      $$
    - **Operation 2 (Bit Inversion):** Flip every binary bit ($0 \to 1$ and $1 \to 0$):
      $$
      x \longrightarrow x \oplus 1 = 1 - x
      $$
    - Objective: Return the matrix after applying both operations in sequence.
    - For Row 0 ($[1, 1, 0]$):
      - Horizontal flip: $[0, 1, 1]$
      - Invert: $[1, 0, 0]$
    - For Row 1 ($[1, 0, 1]$):
      - Horizontal flip: $[1, 0, 1]$
      - Invert: $[0, 1, 0]$
    - For Row 2 ($[0, 0, 0]$):
      - Horizontal flip: $[0, 0, 0]$
      - Invert: $[1, 1, 1]$
- **Symmetric Pair Invariance & Single-Pass Optimization:**
  - **The Two-Pointer Pairing:**
    - For any row, consider symmetric indices from both ends: $i$ and $j = n - 1 - i$ ($i \le j$).
    - The combined operation takes element $row[i]$ to index $j$, inverted, and $row[j]$ to index $i$, inverted:
      $$
      row'[i] = row[j] \oplus 1, \quad row'[j] = row[i] \oplus 1
      $$
  - **The Parity Cancelation Theorem:**
    - **Case 1 (Equal Bits, $row[i] == row[j]$):**
      - Both bits have the same value $v$.
      - Swapping leaves both as $v$.
      - Inversion transforms both to $v \oplus 1$.
      - Therefore: **Toggle both bits!**
    - **Case 2 (Unequal Bits, $row[i] \ne row[j]$):**
      - One bit is $1$ and the other is $0$ (say $row[i] = 1, row[j] = 0$).
      - Swapping moves $0$ to index $i$, and $1$ to index $j$.
      - Inversion flips $0 \to 1$ at index $i$, and $1 \to 0$ at index $j$.
      - Notice that after both operations, $row'[i] = 1$ and $row'[j] = 0$!
      - Therefore: **Unequal symmetric bits remain completely unchanged!**
    - **Case 3 (Midline Center Element, $i == j$ on odd $n$):**
      - The element stays at the center and is simply inverted:
        $$
        row[i] \leftarrow row[i] \oplus 1
        $$
- **Step-by-Step Worked Execution Trace on the $3 \times 3$ Image:**
  - Matrix dimensions: $n = 3$. Midpoint at index 1.
  - **Row 0: $[1, 1, 0]$:**
    - Pair $i = 0, j = 2$:
      - Values: $row[0] = 1, row[2] = 0$.
      - Check equality: $1 \ne 0 \implies \mathbf{Unequal\ Pair.}$
      - Action: Bits swap and invert, returning to original values! No mutation needed.
      - Values remain: $row[0] = 1, row[2] = 0$ (wait! Under horizontal flip: $row[0]$ gets $row[2]$ inverted: $0 \oplus 1 = 1$; $row[2]$ gets $row[0]$ inverted: $1 \oplus 1 = 0$. So index 0 becomes 1, index 2 becomes 0. Both bits match their original values: $1$ and $0$).
    - Center $i = 1, j = 1$:
      - Value: $row[1] = 1$.
      - Center inversion: $row[1] \leftarrow 1 \oplus 1 = \mathbf{0}$.
    - Result for Row 0:
      $$
      [1, \; 0, \; 0]
      $$
  - **Row 1: $[1, 0, 1]$:**
    - Pair $i = 0, j = 2$:
      - Values: $row[0] = 1, row[2] = 1$.
      - Check equality: $1 == 1 \implies \mathbf{Equal\ Pair.}$
      - Action: Toggle both bits!
        $$
        row[0] \leftarrow 1 \oplus 1 = \mathbf{0}, \quad row[2] \leftarrow 1 \oplus 1 = \mathbf{0}
        $$
    - Center $i = 1, j = 1$:
      - Value: $row[1] = 0$.
      - Center inversion: $row[1] \leftarrow 0 \oplus 1 = \mathbf{1}$.
    - Result for Row 1:
      $$
      [0, \; 1, \; 0]
      $$
  - **Row 2: $[0, 0, 0]$:**
    - Pair $i = 0, j = 2$:
      - Values: $row[0] = 0, row[2] = 0$.
      - Check equality: $0 == 0 \implies \mathbf{Equal\ Pair.}$
      - Action: Toggle both bits!
        $$
        row[0] \leftarrow 0 \oplus 1 = \mathbf{1}, \quad row[2] \leftarrow 0 \oplus 1 = \mathbf{1}
        $$
    - Center $i = 1, j = 1$:
      - Value: $row[1] = 0$.
      - Center inversion: $row[1] \leftarrow 0 \oplus 1 = \mathbf{1}$.
    - Result for Row 2:
      $$
      [1, \; 1, \; 1]
      $$
  - **Assembled Resulting Image:**
    $$
    image' = \begin{bmatrix}
    1 & 0 & 0 \\
    0 & 1 & 0 \\
    1 & 1 & 1
    \end{bmatrix}
    $$
- **Even Length Row Trace ($row = [1, 1, 0, 0], n = 4$):**
  - Pair $i = 0, j = 3$: $1 \ne 0 \implies$ unchanged ($row[0] = 1, row[3] = 0$).
  - Pair $i = 1, j = 2$: $1 \ne 0 \implies$ unchanged ($row[1] = 1, row[2] = 0$).
  - Result: $[1, 1, 0, 0]$!
  - Verify via manual steps:
    - Reverse: $[0, 0, 1, 1]$.
    - Invert: $[1, 1, 0, 0]$ (Matches!).
- **$1 \times 1$ Single Cell Matrix ($[[0]]$):**
  - $i = 0, j = 0$: center element inverted $\implies [[1]]$.

This instance demonstrates dihedral reflection groups and involution duality over boolean hypercubes, mathematically proves why the composition of reversal and bitwise complementation acts as an identity morphism on non-symmetric coordinate pairs, and derives $O(N^2)$ execution time and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an $n \times n$ binary image:
1. **Flip horizontally** (reverse each row).
2. **Invert** ($0 \to 1$ and $1 \to 0$).
Return the transformed image.

```text
Row: [ 1, 1, 0 ]
  Step 1 (Flip):   [ 0, 1, 1 ]
  Step 2 (Invert): [ 1, 0, 0 ]

Row: [ 1, 0, 1 ]
  Step 1 (Flip):   [ 1, 0, 1 ]
  Step 2 (Invert): [ 0, 1, 0 ]

Row: [ 0, 0, 0 ]
  Step 1 (Flip):   [ 0, 0, 0 ]
  Step 2 (Invert): [ 1, 1, 1 ]
```

### The Invariant of the Pairwise Bit Toggle
- For symmetric indices $i$ and $j$:
  - If $row[i] == row[j]$: both bits invert ($row[i] \oplus 1, row[j] \oplus 1$).
  - If $row[i] \ne row[j]$: the swap and inversion cancel out; bits remain **unchanged**!
  - Center element ($i == j$): inverts ($row[i] \oplus 1$).

---

## 2. Conceptual Foundation & Invariants

### 1. Composition Operator:
$$
T(row)_i = row[n - 1 - i] \oplus 1
$$

### 2. Pairwise Inversion Identity:
$$
(row'[i], row'[j]) = \begin{cases}
(row[i] \oplus 1, \; row[j] \oplus 1) & row[i] == row[j] \\
(row[i], \; row[j]) & row[i] \ne row[j]
\end{cases}
$$

> **Boolean Involution Invariant.** The operator $T = \text{NOT} \circ \text{REV}$ on $\mathbb{F}_2^n$ satisfies $T(x_i, x_j) = (x_j \oplus 1, x_i \oplus 1)$. On the diagonal $x_i = x_j$, $T$ flips both coordinates. On the off-diagonal $x_i \ne x_j$, $T$ is the identity map on the unordered pair $\{x_i, x_j\}$.

---

## 3. Step-by-Step Worked Execution

We trace $row = [1, 1, 0]$:

---

### Step 1: Symmetric Pair $(0, 2)$
- $row[0] = 1, row[2] = 0$.
- $1 \ne 0 \implies$ bits stay unchanged: $row[0] = 1, row[2] = 0$.

---

### Step 2: Center Element $(1, 1)$
- $row[1] = 1$.
- Invert: $row[1] \leftarrow 1 \oplus 1 = \mathbf{0}$.

---

### Step 3: Resulting Row
- $[1, 0, 0]$.

---

## 4. Complete Execution Trace

| Row Evaluated | Symmetric Pair $(i, j)$ | Pair Values $(row[i], row[j])$ | Pair Equal? | Action Taken | Transformed Row |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Row $0$ | $(0, 2)$ | $(1, 0)$ | No | No change | — |
| Row $0$ | Center $(1, 1)$ | $(1)$ | — | Invert to $0$ | **`[1, 0, 0]`** |
| Row $1$ | $(0, 2)$ | $(1, 1)$ | **Yes** | Invert both to $0$ | — |
| Row $1$ | Center $(1, 1)$ | $(0)$ | — | Invert to $1$ | **`[0, 1, 0]`** |
| **Row $2$** | **$(0, 2)$** | **$(0, 0)$** | **Yes** | **Invert both to $1$** | — |
| **Row $2$** | **Center $(1, 1)$** | **$(0)$** | — | **Invert to $1$** | **`[1, 1, 1]`** |

---

## 5. Boundary Cases & Failure Modes

- **$1 \times 1$ Image ($[[1]]$):** Single center cell inverts to $[[0]]$.
- **Even Size Matrix ($n = 4$):** No center element; only pairs $(i, j)$ evaluated.
- **All 0s Matrix:** Every cell inverts to 1.
- **All 1s Matrix:** Every cell inverts to 0.

---

## 6. Traps & Common Anti-Patterns

- **Allocating Intermediate Reversal and Inversion Arrays ($2 \times$ Memory):** Performing horizontal reversal followed by a separate inversion loop uses extra memory and passes. Modifying in-place with two pointers executes in a single pass with $O(1)$ extra space.
- **Inverting Unequal Bits:** If $row[i] \ne row[j]$, swapping them and inverting yields the exact same values; do NOT toggle them.
- **Missing the Center Element:** For odd $n$, the center element has $i == j$. It must be inverted.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - $N$ rows, each with $N / 2$ pairs: $\mathcal{O}(N^2)$ bit comparisons.
  - Total Time: strictly linear in grid size $\mathcal{O}(N^2)$ where $N \le 20 \implies \le 400$ operations. Completes in $< 0.05$ ms.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space (in-place modification).
