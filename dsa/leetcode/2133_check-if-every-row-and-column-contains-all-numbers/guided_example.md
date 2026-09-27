# Guided Example: Check if Every Row and Column Contains All Numbers

We trace the step-by-step execution of the optimal distinctness-verification and matrix-transposition check on a representative problem instance:

- **Input Matrix (`matrix`):**
  $$\begin{pmatrix} 1 & 2 & 3 \\ 3 & 1 & 2 \\ 2 & 3 & 1 \end{pmatrix}$$
- **Expected Output:** `true`

This instance illustrates the equivalence between containing all numbers in $\{1, \dots, n\}$ and having zero duplicate entries across fixed-length rows and columns, demonstrating Latin square validation in quadratic time.

---

## 1. Problem Overview & Representative Instance

An $n \times n$ integer matrix is defined as valid if every row and every column contains all integers from $1$ to $n$ inclusive (a Latin square). Given an $n \times n$ matrix where each entry satisfies $1 \le \text{matrix}[i][j] \le n$, we must determine whether the matrix is valid.

Consider our representative $3 \times 3$ matrix:
- Row $0$: `[1, 2, 3]` contains $1, 2, 3$.
- Row $1$: `[3, 1, 2]` contains $1, 2, 3$.
- Row $2$: `[2, 3, 1]` contains $1, 2, 3$.
- Column $0$: `[1, 3, 2]` contains $1, 2, 3$.
- Column $1$: `[2, 1, 3]` contains $1, 2, 3$.
- Column $2$: `[3, 2, 1]` contains $1, 2, 3$.

Every line contains all three numbers without duplication, confirming validity.

---

## 2. Mathematical & Algorithmic Principles

### The Pigeonhole Bijective Equivalence
Let $S$ be a multiset of $n$ integers where each element $x \in \{1, 2, \dots, n\}$.
By the Pigeonhole Principle:
- The domain $\{1, \dots, n\}$ has cardinality $n$.
- The multiset $S$ has size $n$.
- A mapping from an $n$-element index set to an $n$-element target set is surjective (covers all elements) if and only if it is injective (contains no duplicates).

Therefore, testing whether a row or column contains every number from $1$ to $n$ is mathematically equivalent to verifying:

$$|\text{Distinct}(S)| = n$$

### Unified Row and Column Traversal
A matrix can be validated by inspecting $2n$ lines ($n$ rows and $n$ columns):
1. **Row Check:** For each row $i \in \{0, \dots, n-1\}$, insert all elements into a hash set or bitmask. If $|\text{set}| < n$, a duplicate exists, and the matrix is invalid.
2. **Column Check:** For each column $j \in \{0, \dots, n-1\}$, gather elements across all rows $\text{matrix}[0 \dots n-1][j]$. If $|\text{set}| < n$, the matrix is invalid.

If all $2n$ sets achieve size $n$, the matrix is unconditionally valid.

| Line Type | Index Range | Target Sequence | Distinct Target Condition |
|---|---|---|---|
| Rows | $i \in \{0, \dots, n-1\}$ | $\text{matrix}[i][0 \dots n-1]$ | $|\text{set}(\text{row}_i)| = n$ |
| Columns | $j \in \{0, \dots, n-1\}$ | $\text{matrix}[0 \dots n-1][j]$ | $|\text{set}(\text{col}_j)| = n$ |

---

## 3. Step-by-Step Walkthrough with Intermediate State

Matrix dimensions: $n = 3$. Target distinct count: $3$.

### Phase 1: Row Validations
- **Row 0: `[1, 2, 3]`**
  - Distinct set: $\{1, 2, 3\}$.
  - Cardinality: $3 = n$. Valid.
- **Row 1: `[3, 1, 2]`**
  - Distinct set: $\{1, 2, 3\}$.
  - Cardinality: $3 = n$. Valid.
- **Row 2: `[2, 3, 1]`**
  - Distinct set: $\{1, 2, 3\}$.
  - Cardinality: $3 = n$. Valid.

All rows pass the distinctness condition.

### Phase 2: Column Validations
- **Column 0: `[matrix[0][0], matrix[1][0], matrix[2][0]] = [1, 3, 2]`**
  - Distinct set: $\{1, 2, 3\}$.
  - Cardinality: $3 = n$. Valid.
- **Column 1: `[matrix[0][1], matrix[1][1], matrix[2][1]] = [2, 1, 3]`**
  - Distinct set: $\{1, 2, 3\}$.
  - Cardinality: $3 = n$. Valid.
- **Column 2: `[matrix[0][2], matrix[1][2], matrix[2][2]] = [3, 2, 1]`**
  - Distinct set: $\{1, 2, 3\}$.
  - Cardinality: $3 = n$. Valid.

All columns pass the distinctness condition.

### Verification Conclusion
All $3$ rows and all $3$ columns contain exactly $n = 3$ unique integers. Return `true`.

---

## 4. Comprehensive State Trace

The line-by-line verification trace is summarized below:

| Line Orientation | Line Index | Sequence Elements | Set Representation | Distinct Size | Satisfies Condition? | Early Abort Triggered? |
|---|---|---|---|---|---|---|
| Row | $0$ | `[1, 2, 3]` | $\{1, 2, 3\}$ | $3$ | Yes ($3 = 3$) | No |
| Row | $1$ | `[3, 1, 2]` | $\{1, 2, 3\}$ | $3$ | Yes ($3 = 3$) | No |
| Row | $2$ | `[2, 3, 1]` | $\{1, 2, 3\}$ | $3$ | Yes ($3 = 3$) | No |
| Column | $0$ | `[1, 3, 2]` | $\{1, 2, 3\}$ | $3$ | Yes ($3 = 3$) | No |
| Column | $1$ | `[2, 1, 3]` | $\{1, 2, 3\}$ | $3$ | Yes ($3 = 3$) | No |
| Column | $2$ | `[3, 2, 1]` | $\{1, 2, 3\}$ | $3$ | Yes ($3 = 3$) | No |

Final verdict: `true`.

---

## 5. Algorithmic Correctness & Soundness

**Soundness.** For any sequence $A$ of length $n$ with elements drawn from $\{1, \dots, n\}$, if $|\text{Distinct}(A)| = n$, then $A$ contains every integer from $1$ to $n$ exactly once without omission. If even a single line fails to achieve cardinality $n$, that line contains at least one duplicate, meaning by finite counting it must also omit at least one required value in $\{1, \dots, n\}$.

**Completeness.** The algorithm systematically evaluates all $n$ rows and all $n$ columns. Because both dimensions are checked independently, no orthogonal violation can slip through. Early short-circuiting guarantees immediate halting upon finding any defect.

---

## 6. Edge Cases & Anti-Patterns

- **Minimal Matrix ($n = 1$):** For `matrix = [[1]]`, the single row and single column each contain $\{1\}$ with cardinality $1$, correctly returning `true`.
- **Valid Rows but Invalid Columns:** In matrix `[[1, 2], [1, 2]]`, rows are valid (`{1, 2}`), but Column 0 contains `[1, 1]` (cardinality 1), correctly failing on the column check.
- **Values Exceeding Bound:** The problem constraint guarantees $1 \le \text{matrix}[i][j] \le n$, making cardinality comparison with $n$ strictly sufficient.
- **Anti-Pattern — Arithmetic Sum Only:** Testing whether $\sum = \frac{n(n+1)}{2}$ is insufficient because symmetric errors (e.g. replacing $2, 3$ with $1, 4$) preserve the sum while introducing duplicates. Explicit set distinctness or bitmask tracking is required.

---

## 7. Complexity Analysis

- **Time Complexity:** $\mathcal{O}(n^2)$, where $n$ is the number of rows/columns. There are $n^2$ entries in the matrix. Each entry is visited once during row inspection and once during column inspection, performing $\mathcal{O}(1)$ set or bitmask insertions.
- **Auxiliary Space Complexity:** $\mathcal{O}(n)$ to store the distinct element set or bitmask for the currently evaluated line.
