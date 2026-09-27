# Guided Example: Remove All Ones With Row and Column Flips

We trace the step-by-step execution of the row equivalence and bitwise complement invariant verification on a representative problem instance:

- **Input Matrix (`grid`):**
  $$\begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix}$$
- **Expected Output:** `true`

This instance illustrates the algebraic structure of row and column flips over the Galois field $\mathbb{F}_2$, proving why reachability of the all-zero state requires every row to be either identical to or the exact bitwise complement of the reference row.

---

## 1. Problem Overview & Representative Instance

We are given an $m \times n$ binary matrix `grid`. In a single operation, we may choose any row or column and flip all of its bits ($0 \to 1$ and $1 \to 0$). We must determine whether any finite sequence of operations can transform the entire matrix into all zeros.

Consider our representative $3 \times 3$ matrix:
- Row $0$: `[0, 1, 0]`
- Row $1$: `[1, 0, 1]`
- Row $2$: `[0, 1, 0]`

Notice that flipping Row $1$ inverts its bits to `[0, 1, 0]`, making all three rows identical to `[0, 1, 0]`. Subsequently flipping Column $1$ clears the single remaining $1$ in every row, achieving an all-zero matrix.

---

## 2. Mathematical & Algorithmic Principles

### Linear Algebra Over $\mathbb{F}_2$
Let $r_i \in \{0, 1\}$ indicate whether row $i$ is flipped an odd number of times ($1$) or an even number of times ($0$).
Similarly, let $c_j \in \{0, 1\}$ indicate whether column $j$ is flipped an odd number of times.
The value of cell $(i, j)$ after applying all operations is:

$$\text{final}(i, j) = \text{grid}[i][j] \oplus r_i \oplus c_j$$

For the entire matrix to become zero, every cell must satisfy:

$$\text{grid}[i][j] \oplus r_i \oplus c_j = 0 \iff \text{grid}[i][j] = r_i \oplus c_j$$

### The Row Compatibility Theorem
**Theorem.** An all-zero configuration is reachable if and only if every row $i$ is either strictly identical to row $0$ or the exact bitwise complement of row $0$.

*Proof.*
Consider row $i$ and reference row $0$. For any column $j$:

$$\text{grid}[i][j] \oplus \text{grid}[0][j] = (r_i \oplus c_j) \oplus (r_0 \oplus c_j) = r_i \oplus r_0$$

The column term $c_j$ cancels out completely. Consequently, the differential bit $\text{grid}[i][j] \oplus \text{grid}[0][j]$ is a constant independent of column index $j$:
1. If $r_i \oplus r_0 = 0$, then $\text{grid}[i][j] = \text{grid}[0][j]$ for all $j \in \{0, \dots, n-1\}$. Row $i$ is identical to row $0$.
2. If $r_i \oplus r_0 = 1$, then $\text{grid}[i][j] = 1 \oplus \text{grid}[0][j]$ for all $j \in \{0, \dots, n-1\}$. Row $i$ is the exact bitwise complement of row $0$.

If any row contains some elements that match row $0$ and other elements that match its complement, no choice of row/column flips can ever zero out the matrix.

| Row Category Relative to Row 0 | Bitwise XOR with Row 0 | Action Required | Result After Row Flips |
|---|---|---|---|
| Identical | $(0, 0, \dots, 0)$ | Leave unflipped ($r_i = 0$) | Matches Row 0 |
| Bitwise Complement | $(1, 1, \dots, 1)$ | Flip row ($r_i = 1$) | Matches Row 0 |
| Incompatible Pattern | Mixed $0$s and $1$s | Impossible to align | Infeasible (`false`) |

---

## 3. Step-by-Step Walkthrough with Intermediate State

Input matrix:
- Row 0: `[0, 1, 0]`
- Row 1: `[1, 0, 1]`
- Row 2: `[0, 1, 0]`

### Step 1: Establish Reference Row and Complement
- Reference row $R_0$: `[0, 1, 0]`.
- Complement row $\overline{R_0}$: `[1, 0, 1]`.

### Step 2: Evaluate Row 0
- Row 0 matches reference $R_0$ identically.
- Classification: Compatible (Identical).

### Step 3: Evaluate Row 1 (`[1, 0, 1]`)
- Compare with $R_0 = [0, 1, 0]$:
  - Column 0: $1 \ne 0$
  - Column 1: $0 \ne 1$
  - Column 2: $1 \ne 0$
- Every bit differs from $R_0$.
- Compare with $\overline{R_0} = [1, 0, 1]$:
  - Matches $\overline{R_0}$ across all columns!
- Classification: Compatible (Complement).

### Step 4: Evaluate Row 2 (`[0, 1, 0]`)
- Compare with $R_0 = [0, 1, 0]$:
  - Column 0: $0 = 0$
  - Column 1: $1 = 1$
  - Column 2: $0 = 0$
- Matches $R_0$ across all columns!
- Classification: Compatible (Identical).

### Conclusion
Every row is either identical or complementary to row $0$.
The condition holds across all rows. Output is `true`.

---

## 4. Comprehensive State Trace

The row comparison metrics and alignment states are detailed below:

| Row Index ($i$) | Vector Content $\text{grid}[i]$ | Matches Row 0? | Matches Complement $\overline{\text{Row 0}}$? | Compatibility Status | Required Row Flip $r_i$ | State After Row Normalization |
|---|---|---|---|---|---|---|
| $0$ | `[0, 1, 0]` | Yes | No | Valid | $0$ (No) | `[0, 1, 0]` |
| $1$ | `[1, 0, 1]` | No | Yes | Valid | $1$ (Yes) | `[0, 1, 0]` |
| $2$ | `[0, 1, 0]` | Yes | No | Valid | $0$ (No) | `[0, 1, 0]` |

After row flips, all rows become `[0, 1, 0]`.
Applying column flip $c_1 = 1$ inverts column 1, transforming every row into `[0, 0, 0]`.

---

## 5. Algorithmic Correctness & Soundness

**Soundness.** Suppose every row $i$ satisfies $\text{grid}[i] \in \{R_0, \overline{R_0}\}$. We can set $r_i = 1$ for every row that equals $\overline{R_0}$ and $r_i = 0$ for every row that equals $R_0$. After these row operations, all $m$ rows are identical to $R_0$. For any column $j$ where $R_0[j] = 1$, we flip column $j$ ($c_j = 1$); for any column where $R_0[j] = 0$, we set $c_j = 0$. Every cell in the matrix now evaluates to $0$. Hence, the condition is sufficient.

**Completeness.** Suppose an all-zero matrix is reachable. Then there exist binary vectors $\mathbf{r}$ and $\mathbf{c}$ such that $\text{grid}[i][j] = r_i \oplus c_j$. Then $\text{grid}[i][j] \oplus \text{grid}[0][j] = r_i \oplus r_0$, which is constant across all columns $j$. If $r_i \oplus r_0 = 0$, row $i$ equals row $0$. If $r_i \oplus r_0 = 1$, row $i$ equals the complement of row $0$. No other row profile can satisfy the system. Hence, the condition is strictly necessary.

---

## 6. Edge Cases & Anti-Patterns

- **Single Row ($m = 1$):** A matrix with $1$ row is always solvable; flipping columns corresponding to $1$s immediately yields an all-zero matrix.
- **Single Column ($n = 1$):** Any binary vector of length $1$ is either $0$ or $1$, which trivially matches $R_0$ or $\overline{R_0}$, always returning `true`.
- **Incompatible Matrix:** For `grid = [[1, 1, 0], [0, 0, 0]]`, row 1 matches row 0 at index 2 (both are 0) but differs at index 0 and 1, producing an incompatible row and returning `false`.
- **Anti-Pattern — Exponential Search:** Attempting all $2^{m+n}$ subsets of row and column flips leads to exponential time $\mathcal{O}(2^{m+n})$. The XOR cancellation theorem allows verifying solvability in a single $\mathcal{O}(m \cdot n)$ pass.

---

## 7. Complexity Analysis

- **Time Complexity:** $\mathcal{O}(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns. We compare each row against row 0 in $\mathcal{O}(n)$ steps, giving $\mathcal{O}(m \cdot n)$ total time with immediate early termination on the first incompatible row.
- **Auxiliary Space Complexity:** $\mathcal{O}(1)$ beyond the input matrix if comparing cells in-place, or $\mathcal{O}(n)$ to store the normalized reference row.
