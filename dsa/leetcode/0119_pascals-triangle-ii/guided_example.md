# Guided Example: Pascal's Triangle II

We trace the step-by-step $O(k)$ space backward DP update and direct combinatorial binomial multiplication on a representative row index:

- **Input:** $\text{rowIndex} = 3$
- **Required output:** `[1, 3, 3, 1]`
- **Row Zero Base:** $\text{rowIndex} = 0 \implies [1]$

This instance demonstrates space optimization from $O(k^2)$ matrix storage down to a single $O(k)$ buffer using backward in-place summation ($j$ from $i$ down to $1$), and derives the direct $O(k)$ closed-form multiplicative recurrence: $\binom{k}{i} = \binom{k}{i-1} \times \frac{k - i + 1}{i}$.

---

## 1. Instance & Teaching Goal

Given an integer $\text{rowIndex} = 3$, return the $3$-rd (0-indexed) row of Pascal's triangle:
- Row 0: `[1]`
- Row 1: `[1, 1]`
- Row 2: `[1, 2, 1]`
- Row 3: `[1, 3, 3, 1]`

The problem explicitly asks: *Could you optimize your algorithm to use only $O(k)$ extra space?*

Storing all previous rows wastes $O(k^2)$ space when only the single final row is required.
We analyze two distinct $O(k)$ space algorithms:
1. **In-Place Backward Summation ($O(k^2)$ Time, $O(k)$ Space):**
   Using a single array of length $k + 1$, each new level is accumulated by iterating backwards ($j = i \dots 1$) so that $row[j]$ consumes the prior row's $row[j-1]$ before $row[j-1]$ is modified.
2. **Direct Combinatorial Multiplicative Recurrence ($O(k)$ Time, $O(k)$ Space):**
   By recognizing that row $k$ contains $\binom{k}{0}, \binom{k}{1}, \dots, \binom{k}{k}$, successive terms can be computed directly in $O(1)$ arithmetic operations each without generating previous rows at all.

---

## 2. Conceptual Foundation & Invariants

### Method 1: In-Place Backward DP Protocol
Maintain an array `row = [1] + [0] * rowIndex`.
For each step $i$ from $1$ up to $\text{rowIndex}$:
Iterate $j$ **backwards** from $i$ down to $1$:
$$
\text{row}[j] \leftarrow \text{row}[j] + \text{row}[j - 1]
$$
Because $j$ decreases, computing $\text{row}[j]$ relies on $\text{row}[j-1]$ from the previous level $i-1$, preventing the newly written values from cascading forward.

### Method 2: Combinatorial Multiplicative Step
For a fixed row index $k$, let $C(k, i) = \binom{k}{i}$.
The ratio between adjacent binomial terms is:
$$
\frac{\binom{k}{i}}{\binom{k}{i-1}} = \frac{\frac{k!}{i!(k-i)!}}{\frac{k!}{(i-1)!(k-i+1)!}} = \frac{k - i + 1}{i}
$$
Therefore:
$$
C(k, 0) = 1
$$
$$
C(k, i) = C(k, i - 1) \times \frac{k - i + 1}{i} \quad \text{for } 1 \le i \le k
$$

> **Invariant.** Under backward iteration, at the end of step $i$, the prefix $\text{row}[0 \dots i]$ contains the exact entries of Pascal's triangle at row $i$.

---

## 3. Step-by-Step Worked Execution

### Execution via Method 1 (In-Place Backward DP)
Target $\text{rowIndex} = 3$.
Initialize buffer: `row = [1, 0, 0, 0]`.

#### Step $i = 1$:
- Iterate $j$ from $1$ down to $1$:
  - $j = 1$: $\text{row}[1] = \text{row}[1] + \text{row}[0] = 0 + 1 = 1$.
- Buffer state: `[1, 1, 0, 0]` (Represents Row 1).

#### Step $i = 2$:
- Iterate $j$ from $2$ down to $1$:
  - $j = 2$: $\text{row}[2] = \text{row}[2] + \text{row}[1] = 0 + 1 = 1$.
  - $j = 1$: $\text{row}[1] = \text{row}[1] + \text{row}[0] = 1 + 1 = 2$.
- Buffer state: `[1, 2, 1, 0]` (Represents Row 2).

#### Step $i = 3$:
- Iterate $j$ from $3$ down to $1$:
  - $j = 3$: $\text{row}[3] = \text{row}[3] + \text{row}[2] = 0 + 1 = 1$.
  - $j = 2$: $\text{row}[2] = \text{row}[2] + \text{row}[1] = 1 + 2 = 3$.
  - $j = 1$: $\text{row}[1] = \text{row}[1] + \text{row}[0] = 2 + 1 = 3$.
- Buffer state: `[1, 3, 3, 1]` (Represents Row 3).

Final answer: `[1, 3, 3, 1]`.

---

### Execution via Method 2 (Direct Combinatorial Multiplication)
Target $k = 3$:
1. $i = 0$: $C(3, 0) = \mathbf{1}$.
2. $i = 1$:
   $$
   C(3, 1) = 1 \times \frac{3 - 1 + 1}{1} = 1 \times \frac{3}{1} = \mathbf{3}
   $$
3. $i = 2$:
   $$
   C(3, 2) = 3 \times \frac{3 - 2 + 1}{2} = 3 \times \frac{2}{2} = \mathbf{3}
   $$
4. $i = 3$:
   $$
   C(3, 3) = 3 \times \frac{3 - 3 + 1}{3} = 3 \times \frac{1}{3} = \mathbf{1}
   $$
Assembled in 4 steps: `[1, 3, 3, 1]`.

Each multiplicative step consumes one ratio and one already-known term, so the
whole row is a chain of $k$ divisions rather than a triangular sum:

| Step $i$ | Ratio $\frac{k-i+1}{i}$ for $k = 3$ | Previous term $C(3,i-1)$ | Product | New term $C(3,i)$ |
|:---:|:---:|:---:|:---:|:---:|
| $1$ | $\frac{3-1+1}{1} = 3$ | $1$ | $1 \times 3 = 3$ | $3$ |
| $2$ | $\frac{3-2+1}{2} = 1$ | $3$ | $3 \times 1 = 3$ | $3$ |
| $3$ | $\frac{3-3+1}{3} = \frac{1}{3}$ | $3$ | $3 \times \frac{1}{3} = 1$ | $1$ |

The third row is the informative one: the ratio is a proper fraction, yet the
product is never fractional, because $C(3,2) \cdot \frac{1}{3} = 3 \cdot
\frac{1}{3}$ clears exactly. Multiplying before dividing is what keeps every
intermediate value an integer.

---

## 4. Complete Execution Trace

### Buffer Mutations Across DP Passes

| Step $i$ | Inner Loop ($j$ from $i \dots 1$) | Calculation at Each Cell | Array State After Iteration |
|:---:|:---:|:---|:---|
| Init | - | Buffer allocation | `[1, 0, 0, 0]` |
| 1 | $j = 1$ | $\text{row}[1] = 0 + 1 = 1$ | `[1, 1, 0, 0]` |
| 2 | $j = 2, 1$ | $\text{row}[2] = 0 + 1 = 1$, $\text{row}[1] = 1 + 1 = 2$ | `[1, 2, 1, 0]` |
| 3 | $j = 3, 2, 1$ | $\text{row}[3] = 0 + 1 = 1$, $\text{row}[2] = 1 + 2 = 3$, $\text{row}[1] = 2 + 1 = 3$ | **`[1, 3, 3, 1]` (Result)** |

---

## 5. Algorithmic Correctness

**Soundness.** Under in-place backward DP, index $j$ only depends on indices $j$ and $j-1$. By updating from right to left, index $j-1$ remains untouched at its previous-tier value until after all indices $> j-1$ have read it. Under the multiplicative formula, integer division $\frac{(C(k, i-1) \cdot (k - i + 1))}{i}$ is always exact because the product of $i$ consecutive integers is divisible by $i!$.

**Completeness.** Both algorithms generate exactly $k + 1$ elements corresponding to $\binom{k}{0} \dots \binom{k}{k}$.

---

## 6. Traps This Instance Exposes

- **Forward Iteration Bug in Single Array:** If $j$ is iterated forward ($1 \dots i$), $\text{row}[1]$ becomes $2$ at step $i = 2$, and then $\text{row}[2] = \text{row}[2] + \text{row}[1]$ reads the *new* value $2$ instead of the previous-level value $1$. Carrying that order through every step corrupts the buffer into `[1, 3, 5, 5]` rather than the required `[1, 3, 3, 1]`. The two orders diverge exactly where a written cell is re-read:

| Step $i$ | Iteration order | Cells written, in order | Values actually read | Buffer after the step |
|:---:|:---|:---|:---|:---|
| $1$ | backward $j = 1 \dots 1$ | `row[1]` | `row[1] + row[0] = 0 + 1 = 1` | `[1, 1, 0, 0]` |
| $2$ | backward $j = 2 \dots 1$ (correct) | `row[2]`, then `row[1]` | `0 + 1 = 1`, then `1 + 1 = 2` | `[1, 2, 1, 0]` |
| $2$ | forward $j = 1 \dots 2$ (buggy) | `row[1]`, then `row[2]` | `1 + 1 = 2`, then `0 + 2 = 2` — the second read sees the freshly written $2$, not the previous-level $1$ | `[1, 2, 2, 0]` |
| $3$ | backward $j = 3 \dots 1$ (correct) | `row[3]`, `row[2]`, `row[1]` | `0 + 1 = 1`, `1 + 2 = 3`, `2 + 1 = 3` | `[1, 3, 3, 1]` |
| $3$ | forward $j = 1 \dots 3$ (buggy) | `row[1]`, `row[2]`, `row[3]` | `2 + 1 = 3`, then `2 + 3 = 5`, then `0 + 5 = 5` | `[1, 3, 5, 5]` |

  The divergence starts at step $2$ and compounds: by step $3$ the erroneous
  `row[2] = 2` has been added into `row[3]`, so a single read-order mistake
  changes three of the four entries.
- **Integer Division Truncation:** In languages where division truncates (e.g. `//`), writing `(C * (k - i + 1)) // i` must multiply before dividing, because `(k - i + 1) // i` might truncate to $0$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - **Backward DP:** $O(k^2)$, performing $\frac{k(k+1)}{2}$ additions.
  - **Combinatorial Multiplicative:** $O(k)$, performing exactly $k$ multiplications and divisions.
- **Auxiliary Space Complexity:** $O(k)$ extra space to store the output array of length $k + 1$.