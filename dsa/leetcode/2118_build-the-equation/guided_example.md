# Guided Example: Build the Equation

We trace the step-by-step execution of the optimal relational string assembly approach on a representative problem instance:

- **Input Table (`Terms`):**
  - Row 1: `power = 2`, `factor = 1`
  - Row 2: `power = 1`, `factor = -4`
  - Row 3: `power = 0`, `factor = 2`
- **Expected Output Table:**
  - Row: `equation = "+1X^2-4X+2=0"`

This instance illustrates how individual polynomial monomials are formatted based on their degree, sorted in descending exponent order, and concatenated into a well-formed equation string ending with `=0`.

---

## 1. Problem Overview & Representative Instance

We are given a database table `Terms` with schema:
- `power` (integer): The non-negative exponent of the polynomial term (primary key).
- `factor` (integer): The non-zero integer coefficient.

Our objective is to construct the mathematical equation formed by these terms. The output must satisfy the following grammatical rules:
1. Every term must explicitly display its sign (`+` for positive factors, `-` for negative factors).
2. The coefficient (absolute value) must be included even if it equals $1$.
3. If `power > 1`, the variable fragment is formatted as `X^<power>`.
4. If `power = 1`, the variable fragment is formatted as `X` (no exponent marker).
5. If `power = 0`, the variable is omitted entirely (constant term only).
6. Terms must be ordered in strictly descending order of `power`.
7. The complete left-hand side string must be terminated with `=0`.

In our representative dataset:
- Exponent $2$ with coefficient $1$ produces `+1X^2`.
- Exponent $1$ with coefficient $-4$ produces `-4X`.
- Exponent $0$ with coefficient $2$ produces `+2`.
Combining them in descending order yields `+1X^2-4X+2=0`.

---

## 2. Mathematical & Algorithmic Principles

### Monomial String Mapping
Each relational tuple $(\text{power}, \text{factor})$ maps deterministically to a text token $T(\text{power}, \text{factor})$.
1. **Sign and Magnitude Representation:**
   - If $\text{factor} > 0$, prefix with `'+'` and append the factor: `CONCAT('+', factor)`.
   - If $\text{factor} < 0$, the negative integer automatically formats with its leading minus sign `'-'`: `factor`.
2. **Variable Segment Formatting:**
   - Case $\text{power} = 0$: empty suffix `""`.
   - Case $\text{power} = 1$: linear variable `"X"`.
   - Case $\text{power} > 1$: exponential term `CONCAT("X^", power)`.

### Ordered Relational Aggregation
Relational tables are unordered multisets by definition. To guarantee standard polynomial canonical form (descending order of powers), the fragments must be concatenated under an explicit ordering clause:

$$\text{LHS} = \sum_{\text{power descending}} T(\text{power}, \text{factor})$$

In SQL syntax, this is achieved via string aggregation with an empty delimiter and an internal ordering directive: `GROUP_CONCAT(term ORDER BY power DESC SEPARATOR '')`.

| Degree ($\text{power}$) | Coefficient ($\text{factor}$) | Formatted Sign & Factor | Variable Suffix | Complete Monomial Fragment |
|---|---|---|---|---|
| $0$ | $c > 0$ | `+c` | None | `+c` |
| $0$ | $c < 0$ | `-c` | None | `-c` |
| $1$ | $c > 0$ | `+c` | `X` | `+cX` |
| $1$ | $c < 0$ | `-c` | `X` | `-cX` |
| $k > 1$ | $c > 0$ | `+c` | `X^k` | `+cX^k` |
| $k > 1$ | $c < 0$ | `-c` | `X^k` | `-cX^k` |

---

## 3. Step-by-Step Walkthrough with Intermediate State

### Step 1: Evaluating Row 1 (`power = 2, factor = 1`)
- Factor classification: $1 > 0 \implies$ sign prefix `'+'`, magnitude `'1'` $\to$ `"+1"`.
- Power classification: $2 > 1 \implies$ variable suffix `"X^2"`.
- Concatenated monomial fragment: `"+1X^2"`.

### Step 2: Evaluating Row 2 (`power = 1, factor = -4`)
- Factor classification: $-4 < 0 \implies$ inherits leading minus $\to$ `"-4"`.
- Power classification: $1 = 1 \implies$ variable suffix `"X"` (no caret).
- Concatenated monomial fragment: `"-4X"`.

### Step 3: Evaluating Row 3 (`power = 0, factor = 2`)
- Factor classification: $2 > 0 \implies$ sign prefix `'+'`, magnitude `'2'` $\to$ `"+2"`.
- Power classification: $0 = 0 \implies$ constant term, variable omitted.
- Concatenated monomial fragment: `"+2"`.

### Step 4: Sorting by Descending Exponent
We order the generated monomial fragments by their corresponding `power` values descending:
1. Degree $2$: `"+1X^2"`
2. Degree $1$: `"-4X"`
3. Degree $0$: `"+2"`

### Step 5: String Aggregation and Suffix Attachment
- Aggregate without delimiter: `"+1X^2"` $+$ `"-4X"` $+$ `"+2"` $=$ `"+1X^2-4X+2"`.
- Append required terminal marker `=0`: `"+1X^2-4X+2=0"`.
- Resulting column value: `"+1X^2-4X+2=0"`.

---

## 4. Comprehensive State Trace

The table below traces the per-row formatting transitions and the final concatenated aggregate.

| Input Row ID | Attribute `power` | Attribute `factor` | Conditional Monomial Rule | Produced String Fragment | Ordered Sequence Position |
|---|---|---|---|---|---|
| Row 1 | $2$ | $1$ | Positive factor, degree $> 1$ | `"+1X^2"` | Position 1 |
| Row 2 | $1$ | $-4$ | Negative factor, degree $= 1$ | `"-4X"` | Position 2 |
| Row 3 | $0$ | $2$ | Positive factor, degree $= 0$ | `"+2"` | Position 3 |

Aggregated Expression: `CONCAT("+1X^2", "-4X", "+2", "=0")` $\to$ `"+1X^2-4X+2=0"`.

---

## 5. Algorithmic Correctness & Soundness

**Soundness.** Every polynomial term is generated according to mutually exclusive, collectively exhaustive degree branches ($\text{power} = 0$, $\text{power} = 1$, or $\text{power} > 1$). Because `power` is unique across rows (the primary key), no duplicate degrees exist to merge. The explicit `ORDER BY power DESC` inside the string aggregation guarantees that algebraic canonical ordering is preserved regardless of how the underlying storage engine retrieves rows. Appending `=0` guarantees exact adherence to the specified equation grammar.

**Completeness.** Every record in the table is visited and formatted. In relational databases where strings are aggregated across all matching rows, using `GROUP_CONCAT` without an explicit `GROUP BY` collapses the entire relation into a single scalar row representing the full equation.

---

## 6. Edge Cases & Anti-Patterns

- **Single Constant Term:** If the table contains only `power = 0, factor = -100`, the algorithm produces `"-100=0"` without inserting unwanted variable symbols.
- **Unit Coefficients ($1$ and $-1$):** Unlike standard mathematical shorthand where $1X$ is written as $X$, the problem specification explicitly mandates retaining the coefficient digit: `+1X` or `-1X`.
- **Negative Leading Term:** If the highest degree monomial has a negative coefficient, the equation begins with `-`, e.g., `-4X^4+1X^2-1X=0`.
- **Anti-Pattern — Missing Order Clause:** Using `GROUP_CONCAT` without `ORDER BY power DESC` relies on physical storage order, which can cause arbitrary reordering of terms across database engine restarts or index scans.

---

## 7. Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \log N)$, where $N$ is the number of rows in the `Terms` table. Evaluating the `CASE` statement takes $\mathcal{O}(1)$ per row ($\mathcal{O}(N)$ total), and sorting the fragments by `power DESC` takes $\mathcal{O}(N \log N)$ sorting time.
- **Auxiliary Space Complexity:** $\mathcal{O}(N)$ buffer memory in the query execution engine to store the formatted fragments prior to concatenation.
