# Guided Example: Champagne Tower

We trace the step-by-step triangular pyramid fluid cascade, glass capacity thresholding ($\max(0, f[i][j] - 1)$), symmetric bifurcation overflow routing ($half = (excess) / 2$), Pascal-like triangular grid propagation ($f[i+1][j]$ and $f[i+1][j+1]$), and saturation clamping ($\min(1.0, f)$) on representative champagne pour volumes:

- **Input:**
  - Champagne poured: $poured = 2$
  - Query coordinates: $query\_row = 1, \quad query\_glass = 1$
- **Required output:** `0.5`
  - Champagne pyramid architecture & fluid dynamics:
    - Glasses are arranged in a triangular pyramid:
      - Row 0: 1 glass ($(0, 0)$)
      - Row 1: 2 glasses ($(1, 0), (1, 1)$)
      - Row 2: 3 glasses ($(2, 0), (2, 1), (2, 2)$)
      - Row $i$: $i + 1$ glasses ($(i, 0) \dots (i, i)$)
    - Each glass has an exact capacity of **1 cup** of champagne.
    - When glass $(i, j)$ receives more than 1 cup, the excess liquid overflows and divides **equally into two streams**:
      - One half pours into the bottom-left glass: $(i + 1, j)$
      - One half pours into the bottom-right glass: $(i + 1, j + 1)$
    - Objective: Calculate how full the glass at $(query\_row, query\_glass)$ is after pouring. (Value in $[0.0, 1.0]$).
    - For $poured = 2$, query $(1, 1)$:
      - Glass $(0, 0)$ receives 2 cups.
      - Retains 1 cup (full capacity).
      - Excess of $2 - 1 = 1$ cup overflows.
      - Left glass $(1, 0)$ receives $1 / 2 = 0.5$ cup.
      - Right glass $(1, 1)$ receives $1 / 2 = 0.5$ cup.
      - Glass $(1, 1)$ is half full $\implies$ return **`0.5`**.
- **Pyramid Flow Conservation & Overflow Routing Invariant:**
  - **The Saturated Inflow Principle:**
    - Initialize the entire pour volume at the apex glass:
      $$
      f[0][0] = poured
      $$
    - All other glasses are initially empty ($0.0$).
  - **Layer-by-Layer Descent ($i = 0 \dots query\_row$):**
    - For each glass $(i, j)$ in row $i$:
      - If the liquid accumulated $f[i][j] > 1.0$:
        - The glass retains exactly $1.0$ cup:
          $$
          excess = f[i][j] - 1.0
          $$
          $$
          f[i][j] \leftarrow 1.0
          $$
        - The excess liquid splits equally:
          $$
          half = \frac{excess}{2}
          $$
        - Bottom-left child receives $half$:
          $$
          f[i + 1][j] \leftarrow f[i + 1][j] + half
          $$
        - Bottom-right child receives $half$:
          $$
          f[i + 1][j + 1] \leftarrow f[i + 1][j + 1] + half
          $$
  - **Termination & Clamping:**
    - After processing through row $query\_row$, the liquid level in the target glass is simply $f[query\_row][query\_glass]$ (clamped to at most $1.0$).
- **Step-by-Step Worked Execution Trace on $poured = 2, query\_row = 1, query\_glass = 1$:**
  - Initialize grid $f$ of dimension $101 \times 101$ with zeros.
  - Pour into apex:
    $$
    f[0][0] = 2.0
    $$
  - **Row 0 ($i = 0$):**
    - Process glass $(0, 0)$:
      - Inflow: $f[0][0] = 2.0 > 1.0 \implies \mathbf{Overflow!}$
      - Excess volume:
        $$
        excess = 2.0 - 1.0 = \mathbf{1.0}
        $$
      - Glass $(0, 0)$ retains:
        $$
        f[0][0] \leftarrow \mathbf{1.0}
        $$
      - Split excess equally:
        $$
        half = \frac{1.0}{2} = \mathbf{0.5}
        $$
      - Route to children in Row 1:
        $$
        f[1][0] \leftarrow 0.0 + 0.5 = \mathbf{0.5}
        $$
        $$
        f[1][1] \leftarrow 0.0 + 0.5 = \mathbf{0.5}
        $$
  - **Row 1 ($i = 1$, Query Row):**
    - Process glass $(1, 0)$:
      - $f[1][0] = 0.5 \le 1.0 \implies$ No overflow.
    - Process glass $(1, 1)$ (Target Glass):
      - $f[1][1] = 0.5 \le 1.0 \implies$ No overflow.
  - **Extract Target Value:**
    - Query coordinates: $(1, 1)$.
    - Liquid volume:
      $$
      ans = f[1][1] = \mathbf{0.5}
      $$
- **Deep Pyramid Cascading Trace ($poured = 10, query\_row = 2$):**
  - Row 0: $f[0][0] = 10 \implies$ retains 1.0, overflows 9.0 $\implies$ children receive 4.5 each:
    - Row 1: $f[1][0] = 4.5, \; f[1][1] = 4.5$.
  - Row 1:
    - Glass $(1, 0)$ retains 1.0, overflows $3.5 \implies$ sends 1.75 to $(2, 0)$ and 1.75 to $(2, 1)$.
    - Glass $(1, 1)$ retains 1.0, overflows $3.5 \implies$ sends 1.75 to $(2, 1)$ and 1.75 to $(2, 2)$.
  - Row 2:
    - Glass $(2, 0)$ receives $1.75$.
    - Glass $(2, 1)$ receives $1.75 + 1.75 = \mathbf{3.5}$ (center funneling concentration!).
    - Glass $(2, 2)$ receives $1.75$.
  - Glasses $(2, 0)$ and $(2, 2)$ are full ($1.0$), while $(2, 1)$ is completely saturated ($1.0$, with remaining excess continuing down).
- **No Overflow Base Trace ($poured = 1, query\_row = 1, query\_glass = 1$):**
  - $f[0][0] = 1.0 \le 1.0 \implies$ Zero overflow.
  - Row 1 glasses receive 0.0 $\implies$ returns **`0.0`**.

This instance demonstrates fluid percolation on directed acyclic simplicial complexes and discrete nonlinear diffusion with capacity constraints, mathematically proves why downward conservation laws with threshold truncation converge stably in topological order, and derives $O(R^2)$ runtime and $O(R^2)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given $poured$ cups of champagne poured into the top glass of a pyramid:
Each glass holds 1 cup; excess splits equally to bottom-left and bottom-right children.
Find **how full** glass $(query\_row, query\_glass)$ is.

```text
poured = 2, query = (row 1, glass 1)

Row 0:
  Glass (0, 0) receives 2.0 cups.
  Holds 1.0 cup -> Overflows 1.0 cup!

Row 1:
  Left glass (1, 0) gets 1.0 / 2 = 0.5 cup.
  Right glass (1, 1) gets 1.0 / 2 = 0.5 cup.

Result for (1, 1): 0.5
```

### The Invariant of the Saturated Overflow Split
- Simulate layer by layer from row 0 down to $query\_row$.
- If glass $(i, j)$ has $f[i][j] > 1$:
  - Excess $e = f[i][j] - 1$.
  - Glass caps at 1: $f[i][j] = 1$.
  - Half $e/2$ flows to $(i + 1, j)$, and $e/2$ flows to $(i + 1, j + 1)$.

---

## 2. Conceptual Foundation & Invariants

### 1. Fluid Mass Conservation:
$$
\text{excess}(i, j) = \max(0.0, \; f[i][j] - 1.0)
$$
$$
f[i + 1][j] \mathrel{+}= \frac{\text{excess}(i, j)}{2}, \quad f[i + 1][j + 1] \mathrel{+}= \frac{\text{excess}(i, j)}{2}
$$

### 2. Output Saturation Clamp:
$$
ans = \min(1.0, \; f[query\_row][query\_glass])
$$

> **Nonlinear Diffusion Flow Invariant.** The liquid volume satisfies a discrete conservation law on the Pascal lattice with saturation threshold $\theta = 1.0$. The triangular topological DAG ordering enables exact forward integration without back-coupling.

---

## 3. Step-by-Step Worked Execution

We trace $poured = 2, (1, 1)$:

---

### Step 1: Initialize
- $f[0][0] = 2.0$.

---

### Step 2: Row 0
- $f[0][0] = 2.0 > 1.0 \implies excess = 1.0$.
- $f[0][0] = 1.0$.
- $f[1][0] += 0.5$.
- $f[1][1] += 0.5$.

---

### Step 3: Row 1
- Target glass $f[1][1] = 0.5$.

---

### Step 4: Output
$$
\mathbf{0.5}
$$

---

## 4. Complete Execution Trace

| Pyramid Row $i$ | Glass $(i, j)$ | Total Inflow $f[i][j]$ | Retained Volume | Excess Liquid | Split to Left $(i+1, j)$ | Split to Right $(i+1, j+1)$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | $(0, 0)$ | $2.0$ | $1.0$ | $1.0$ | $0.5$ | $0.5$ |
| $1$ | $(1, 0)$ | $0.5$ | $0.5$ | $0.0$ | $0.0$ | $0.0$ |
| **$1$** | **$(1, 1)$** | **$0.5$** | **$0.5$** | **$0.0$** | **—** | **—** |
| **Final** | — | — | — | — | — | **Result: `0.5`** |

---

## 5. Boundary Cases & Failure Modes

- **$poured = 0$:** All glasses remain $0.0$.
- **$poured = 1$:** Top glass fills to $1.0$; zero overflow to lower rows $\implies 0.0$.
- **Massive Pours ($poured = 10^9$):** Glasses in query row cap at $1.0$; clamping $\min(1.0, f)$ ensures output never exceeds 1.0.
- **Apex Query ($(0, 0)$):** Returns $\min(1.0, poured)$.

---

## 6. Traps & Common Anti-Patterns

- **Attempting Pure Combinatorics / Pascal's Formula:** Because glasses cap at 1.0 and do not overflow until full, liquid propagation is non-linear and cannot be computed with simple binomial coefficients $\binom{n}{k}$. Layer-by-layer simulation is mandatory.
- **Simulating Beyond Query Row:** There is no need to simulate down to row 100 if $query\_row = 5$; simulating up to $query\_row$ saves time.
- **Overwriting Fluid Values:** When adding overflow, use addition `+= half`, because interior glasses receive liquid from **two** parent glasses above them!

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Row $i$ contains $i + 1$ glasses.
  - Summing glasses up to $R = query\_row$: $\sum_{i = 0}^R (i + 1) = \frac{(R + 1)(R + 2)}{2} = \mathcal{O}(R^2)$.
  - Total Time: strictly quadratic in row index $\mathcal{O}(R^2)$ where $R \le 100 \implies \le 5050$ operations. Completes in $< 0.5$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(R^2)$ memory for the triangular grid (or $\mathcal{O}(R)$ with 1D rolling array).