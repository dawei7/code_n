# Guided Example: Solve the Equation

We trace the step-by-step equality boundary partitioning (splitting at `'='`), signed polynomial token parsing (`+` and `-` delimiters), variable coefficient aggregation ($x$-terms) and scalar constant summation, linear canonical reduction ($(x_1 - x_2)x = (y_2 - y_1)$), singularity classification (zero coefficient with zero vs non-zero constant), and unique root isolation on representative linear algebraic equations:

- **Input:** $equation = \text{"x+5-3+x=6+x-2"}$
- **Required output:** `\text{"x=2"}`
  - Problem contract:
    - Solve for the single variable $x$.
    - If the equation has a unique integer solution $v$, return formatted as `"x=v"`.
    - If the equation is an identity valid for all $x$, return `"Infinite solutions"`.
    - If the equation produces a contradiction (e.g. $0 = 5$), return `"No solution"`.
- **Linear Canonical Reduction Architecture:**
  - Any linear equation in one variable reduces to the standard algebraic form:
    $$
    A x = B
    $$
  - **Parsing Subroutine ($f(side)$):**
    - Ensure a leading sign: if the expression does not begin with `'-'`, prepend `'+'`.
    - Parse tokens delimited by sign markers (`'+'` or `'-'`).
    - For each token of the form $\pm V$:
      - If $V$ ends with `'x'`:
        - If $V == \text{'x'}$, coefficient is $\pm 1$.
        - Otherwise, coefficient is $\pm int(V[:-1])$.
        - Accumulate into variable coefficient $x_{side}$.
      - If $V$ does not contain `'x'`:
        - Accumulate into constant sum $y_{side}$.
    - Each side transforms into a linear polynomial:
      $$
      \text{Left} = x_1 x + y_1, \quad \text{Right} = x_2 x + y_2
      $$
  - **Rearrangement and Classification:**
    $$
    (x_1 - x_2) x = y_2 - y_1
    $$
    - Let $\Delta x = x_1 - x_2$ and $\Delta y = y_2 - y_1$.
    - **Classification Rules:**
      1. If $\Delta x == 0$ and $\Delta y == 0$: Identity ($0 \cdot x = 0$) $\implies$ **`"Infinite solutions"`**.
      2. If $\Delta x == 0$ and $\Delta y \ne 0$: Contradiction ($0 \cdot x = \text{non-zero}$) $\implies$ **`"No solution"`**.
      3. If $\Delta x \ne 0$: Unique solution $\implies x = \frac{\Delta y}{\Delta x} \implies$ **`"x=" + str(x)`**.
- **Step-by-Step Worked Execution Trace on $\text{"x+5-3+x=6+x-2"}$:**
  - Split around `'='`:
    $$
    \text{Left} = \text{"x+5-3+x"}, \quad \text{Right} = \text{"6+x-2"}
    $$
  - **Step 1: Parse Left Side ($\text{"x+5-3+x"}$):**
    - Add leading `'+'`: `"+x+5-3+x"`.
    - Token 1: `+x` $\implies$ variable term with implicit coefficient $1$:
      $$
      x_1 \leftarrow 0 + 1 = \mathbf{1}
      $$
    - Token 2: `+5` $\implies$ constant term $+5$:
      $$
      y_1 \leftarrow 0 + 5 = \mathbf{5}
      $$
    - Token 3: `-3` $\implies$ constant term $-3$:
      $$
      y_1 \leftarrow 5 - 3 = \mathbf{2}
      $$
    - Token 4: `+x` $\implies$ variable term $+1$:
      $$
      x_1 \leftarrow 1 + 1 = \mathbf{2}
      $$
    - Result for Left:
      $$
      2x + 2 \quad (x_1 = 2, \; y_1 = 2)
      $$
  - **Step 2: Parse Right Side ($\text{"6+x-2"}$):**
    - Add leading `'+'`: `"+6+x-2"`.
    - Token 1: `+6` $\implies$ constant $+6$:
      $$
      y_2 \leftarrow 0 + 6 = \mathbf{6}
      $$
    - Token 2: `+x` $\implies$ variable term $+1$:
      $$
      x_2 \leftarrow 0 + 1 = \mathbf{1}
      $$
    - Token 3: `-2` $\implies$ constant $-2$:
      $$
      y_2 \leftarrow 6 - 2 = \mathbf{4}
      $$
    - Result for Right:
      $$
      1x + 4 \quad (x_2 = 1, \; y_2 = 4)
      $$
  - **Step 3: Collect Terms and Solve:**
    - Variable coefficient delta:
      $$
      \Delta x = x_1 - x_2 = 2 - 1 = \mathbf{1}
      $$
    - Constant value delta:
      $$
      \Delta y = y_2 - y_1 = 4 - 2 = \mathbf{2}
      $$
    - Equation in canonical form:
      $$
      1 \cdot x = 2
      $$
    - Check coefficient: $\Delta x = 1 \ne 0 \implies$ Unique root exists!
    - Solve for $x$:
      $$
      x = \frac{\Delta y}{\Delta x} = \frac{2}{1} = \mathbf{2}
      $$
    - Format output:
      $$
      \mathbf{\text{"x=2"}}
      $$
- **Identity Equation Instance ($equation = \text{"x=x"}$):**
  - Left: $1x + 0$. Right: $1x + 0$.
  - $\Delta x = 1 - 1 = 0$.
  - $\Delta y = 0 - 0 = 0$.
  - Both deltas are 0 $\implies$ Returns **`"Infinite solutions"`**.
- **Contradiction Instance ($equation = \text{"x=x+2"}$):**
  - Left: $1x + 0$. Right: $1x + 2$.
  - $\Delta x = 1 - 1 = 0$.
  - $\Delta y = 2 - 0 = 2 \ne 0$.
  - $0 \cdot x = 2$ is impossible $\implies$ Returns **`"No solution"`**.
- **Zero Root Instance ($equation = \text{"2x=x"}$):**
  - $\Delta x = 2 - 1 = 1, \; \Delta y = 0 - 0 = 0$.
  - $x = 0 / 1 = 0 \implies$ Returns **`"x=0"`**.

This instance demonstrates tokenized lexical analysis and linear Diophantine canonical reduction, mathematically proves why coefficient degeneracy partitions solutions into empty vs affine subspaces, and derives $O(L)$ runtime and $O(L)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an equation string containing numbers, $x$, `+`, `-`, and `=`:
Solve for $x$.
Return `"x=value"`, `"Infinite solutions"`, or `"No solution"`.

```text
x + 5 - 3 + x = 6 + x - 2

Left side:
  x + x = 2x
  5 - 3 = 2
  Left = 2x + 2

Right side:
  x = 1x
  6 - 2 = 4
  Right = 1x + 4

Equation:
  2x + 2 = 1x + 4
  (2 - 1)x = 4 - 2
  1x = 2  ->  x = 2

Result: "x=2"
```

### The Invariant of the Linear Canonical Form
- Every valid linear equation reduces to:
  $$
  A \cdot x = B
  $$
- The solution space is completely determined by the pair $(A, B)$:
  - $A \ne 0 \implies$ exactly one solution $x = B / A$.
  - $A == 0$ and $B == 0 \implies$ infinitely many solutions.
  - $A == 0$ and $B \ne 0 \implies$ zero solutions (impossible).

---

## 2. Conceptual Foundation & Invariants

### 1. Token Sign Attachment:
Every term starts with an explicit sign `+` or `-`:
- `"+5"` $\implies$ scalar $+5$.
- `"+x"` $\implies$ variable $+1 \cdot x$.
- `"-3x"` $\implies$ variable $-3 \cdot x$.

### 2. Solving Form:
$$
\Delta x = x_{left} - x_{right}, \quad \Delta y = y_{right} - y_{left}
$$
$$
x = \frac{\Delta y}{\Delta x}
$$

> **Affine Rank Invariant.** A 1D affine map $T(x) = Ax - B$ has $\ker(T) = \mathbb{R}$ if and only if $\text{rank}([A \mid B]) = 0$, has $\ker(T) = \emptyset$ if $\text{rank}(A) = 0 < \text{rank}([A \mid B])$, and has $|\ker(T)| = 1$ when $\text{rank}(A) = 1$.

---

## 3. Step-by-Step Worked Execution

We trace $equation = \text{"x+5-3+x=6+x-2"}$:

---

### Step 1: Split Sides
- Left: `"x+5-3+x"`.
- Right: `"6+x-2"`.

---

### Step 2: Sum Left Side
- `+x`: $+1x$.
- `+5`: $+5$.
- `-3`: $-3$.
- `+x`: $+1x$.
- $x_1 = 2, y_1 = 2 \implies 2x + 2$.

---

### Step 3: Sum Right Side
- `+6`: $+6$.
- `+x`: $+1x$.
- `-2`: $-2$.
- $x_2 = 1, y_2 = 4 \implies 1x + 4$.

---

### Step 4: Solve
- $\Delta x = 2 - 1 = 1$.
- $\Delta y = 4 - 2 = 2$.
- $x = 2 / 1 = \mathbf{2}$.
- Output: **`"x=2"`**.

---

## 4. Complete Execution Trace

| Token Parsed | Side | Sign | Magnitude / Term | Variable Impact | Constant Impact | Running Polynomial |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `+x` | Left | $+$ | `x` | $+1$ | $0$ | $1x + 0$ |
| `+5` | Left | $+$ | `5` | $0$ | $+5$ | $1x + 5$ |
| `-3` | Left | $-$ | `3` | $0$ | $-3$ | $1x + 2$ |
| `+x` | Left | $+$ | `x` | $+1$ | $0$ | **$2x + 2$** |
| `+6` | Right | $+$ | `6` | $0$ | $+6$ | $0x + 6$ |
| `+x` | Right | $+$ | `x` | $+1$ | $0$ | $1x + 6$ |
| `-2` | Right | $-$ | `2` | $0$ | $-2$ | **$1x + 4$** |
| **System** | $(2 - 1)x = 4 - 2$ | — | $1x = 2$ | — | — | **`"x=2"`** |

---

## 5. Boundary Cases & Failure Modes

- **Implicit Coefficient (`"x"` or `"-x"`):** Magnitude defaults to $1$ (coefficient $+1$ or $-1$), not $0$.
- **Negative Answers (`"x+2=0"`):** Returns `"x=-2"`.
- **Zero Solution (`"2x=x"`):** Returns `"x=0"`.
- **Zero Coincident (`"0x=0"`):** Returns `"Infinite solutions"`.

---

## 6. Traps & Common Anti-Patterns

- **Parsing `"x"` as 0:** Missing the implicit coefficient $1$ when no number precedes `'x'` produces coefficient 0 instead of 1.
- **Handling Multi-Digit Coefficients (`"10x"`):** Slicing only one character before `'x'` fails on multi-digit numbers like `100x`. Slice $V[:-1]$ to capture all digits.
- **Integer Truncation on Division:** The problem guarantees integer solutions when a unique solution exists, so integer division `\Delta y // \Delta x` is exact.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Splitting and scanning string of length $L$: $\mathcal{O}(L)$ operations.
  - Linear equation arithmetic: $\mathcal{O}(1)$.
  - Total Time: strictly linear $\mathcal{O}(L)$. Completes in $< 1$ ms for $L \le 100$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(L)$ space to store tokens during parsing.
