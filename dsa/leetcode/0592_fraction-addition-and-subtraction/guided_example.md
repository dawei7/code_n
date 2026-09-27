# Guided Example: Fraction Addition and Subtraction

We trace the step-by-step signed token stream parsing, common denominator scaling ($Y = \text{lcm}(1, \dots, 10) = 2520$), algebraic numerator accumulation ($x \leftarrow x \pm a \cdot (Y / b)$), Euclidean greatest common divisor reduction ($\gcd(|x|, y)$), and irreducible fractional representation ($x/y$) on representative arithmetic expressions:

- **Input:** $expression = \text{"-1/2+1/2+1/3"}$
- **Required output:** `"1/3"`
  - Arithmetic specification:
    - Input contains signed fractions of the form $\pm a/b$ where numerators and denominators are integers in $[1, 10]$.
    - Perform addition and subtraction from left to right.
    - Result must be returned as an **irreducible fraction** formatted as `"numerator/denominator"`.
    - If the answer is 0, the denominator must be 1: `"0/1"`.
- **Common Denominator Scaling & Exact Rational Arithmetic:**
  - Every denominator $b$ is an integer between $1$ and $10$.
  - The least common multiple (LCM) of all possible denominators $1, 2, \dots, 10$ is:
    $$
    Y = \text{lcm}(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) = 2520
    $$
    *(Or any common multiple such as $6 \times 7 \times 8 \times 9 \times 10 = 30240$)*.
  - By scaling all fractions to this shared universal denominator $Y$:
    $$
    \frac{a}{b} = \frac{a \cdot (Y / b)}{Y}
    $$
    Division is exact with zero fractional truncation!
  - Addition and subtraction reduce to **pure integer additions** on the numerator $x$.
- **Step-by-Step Worked Execution Trace:**
  - Let common denominator $Y = 2520$.
  - Initialize total numerator:
    $$
    x = 0
    $$
  - Normalize expression prefix: starts with `'-'`, so leading sign is preserved:
    $$
    expression = \text{"-1/2+1/2+1/3"}
    $$
  - **Term 1 (`-1/2`):**
    - Sign: $-1$.
    - Numerator $a = 1$, Denominator $b = 2$.
    - Scaling factor: $Y / b = 2520 / 2 = 1260$.
    - Contribution to $x$:
      $$
      \Delta x_1 = (-1) \cdot 1 \cdot 1260 = -1260
      $$
    - Running numerator:
      $$
      x = 0 - 1260 = -1260
      $$
  - **Term 2 (`+1/2`):**
    - Sign: $+1$.
    - Numerator $a = 1$, Denominator $b = 2$.
    - Scaling factor: $2520 / 2 = 1260$.
    - Contribution to $x$:
      $$
      \Delta x_2 = (+1) \cdot 1 \cdot 1260 = +1260
      $$
    - Running numerator:
      $$
      x = -1260 + 1260 = \mathbf{0}
      $$
  - **Term 3 (`+1/3`):**
    - Sign: $+1$.
    - Numerator $a = 1$, Denominator $b = 3$.
    - Scaling factor: $2520 / 3 = 840$.
    - Contribution to $x$:
      $$
      \Delta x_3 = (+1) \cdot 1 \cdot 840 = +840
      $$
    - Running numerator:
      $$
      x = 0 + 840 = \mathbf{840}
      $$
  - All terms processed!
  - Unsimplified fractional state:
    $$
    \frac{x}{Y} = \frac{840}{2520}
    $$
  - **Step 4: Reduce to Irreducible Form via Euclidean GCD:**
    - Calculate greatest common divisor:
      $$
      z = \gcd(|840|, \; 2520) = \mathbf{840}
      $$
    - Divide numerator and denominator by $z$:
      $$
      x_{final} = \frac{840}{840} = \mathbf{1}
      $$
      $$
      y_{final} = \frac{2520}{840} = \mathbf{3}
      $$
    - Format output string:
      $$
      \mathbf{\text{"1/3"}}
      $$
- **Cancellation to Zero Instance ($expression = \text{"-1/2+1/2"}$):**
  - Numerator sums to $x = 0$.
  - $z = \gcd(0, 2520) = 2520$.
  - $x_{final} = 0 / 2520 = 0$, $y_{final} = 2520 / 2520 = 1 \implies \mathbf{\text{"0/1"}}$.
- **Negative Reduced Result ($expression = \text{"1/3-1/2"}$):**
  - $Y = 6$.
  - $x = 2 - 3 = -1$.
  - $\gcd(|-1|, 6) = 1 \implies \mathbf{\text{"-1/6"}}$.

This instance demonstrates exact rational arithmetic via universal common denominator projections, mathematically proves why Euclidean GCD reduction guarantees canonical irreducible representation, and derives $O(N)$ runtime and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an arithmetic expression containing fraction additions and subtractions:
Evaluate the expression and return the result in **irreducible fraction format** (`"x/y"`).
If the result is 0, return `"0/1"`.

```text
Expression: "-1/2 + 1/2 + 1/3"

Term 1: -1/2 ->  -1260 / 2520
Term 2: +1/2 ->  +1260 / 2520
Term 3: +1/3 ->   +840 / 2520

Sum = 840 / 2520
Reduce by gcd(840, 2520) = 840:
  840 / 840  = 1
  2520 / 840 = 3

Result: "1/3"
```

### The Universal Precomputed Denominator Advantage
- Rather than computing least common multiples dynamically at every addition step, we observe that the problem constrains denominators to $b \in [1, 10]$.
- The least common multiple of all integers $1 \dots 10$ is:
  $$
  Y = 2520 \quad (\text{or any multiple like } 30240)
  $$
- Every denominator $b \le 10$ divides $Y$ evenly without remainder ($Y \pmod b == 0$).
- This converts the entire fraction evaluation into simple integer addition.

---

## 2. Conceptual Foundation & Invariants

### 1. Universal Scaling:
For any term $\pm a/b$:
$$
x \leftarrow x + \text{sign} \cdot a \cdot \left( \frac{Y}{b} \right)
$$

### 2. Irreducible Reduction:
After summing all terms:
$$
z = \gcd(|x|, \; Y)
$$
$$
x_{reduced} = \frac{x}{z}, \quad y_{reduced} = \frac{Y}{z}
$$

> **Rational Invariance.** Multiplying numerators by exact quotient weights $Y/b$ preserves fractional proportionality over integer arithmetic without floating-point rounding errors.

---

## 3. Step-by-Step Worked Execution

We trace $expression = \text{"-1/2+1/2+1/3"}$:

---

### Step 1: Initialize
- Universal denominator $Y = 2520$.
- Running numerator $x = 0$.

---

### Step 2: Parse and Accumulate Terms
1. `-1/2`:
   - $sign = -1, a = 1, b = 2$.
   - $x \leftarrow 0 + (-1) \cdot 1 \cdot (2520 / 2) = -1260$.
2. `+1/2`:
   - $sign = +1, a = 1, b = 2$.
   - $x \leftarrow -1260 + (+1) \cdot 1 \cdot (2520 / 2) = 0$.
3. `+1/3`:
   - $sign = +1, a = 1, b = 3$.
   - $x \leftarrow 0 + (+1) \cdot 1 \cdot (2520 / 3) = \mathbf{840}$.

---

### Step 3: Simplify via GCD
$$
z = \gcd(|840|, 2520) = 840
$$
$$
x_{final} = 840 // 840 = 1, \quad y_{final} = 2520 // 840 = 3
$$

---

### Step 4: Format String
$$
\mathbf{\text{"1/3"}}
$$

---

## 4. Complete Execution Trace

| Term Scanned | Sign | $a/b$ | Scale $Y / b$ | Delta $x$ | Cumulative $x$ | Fractional Form $x / Y$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `"-1/2"` | $-1$ | $1/2$ | $1260$ | $-1260$ | $-1260$ | $-1260 / 2520$ |
| `"+1/2"` | $+1$ | $1/2$ | $1260$ | $+1260$ | $0$ | $0 / 2520$ |
| `"+1/3"` | $+1$ | $1/3$ | $840$ | $+840$ | **$840$** | $840 / 2520$ |
| **Reduction** | — | — | $\gcd = 840$ | — | — | **`"1/3"`** |

---

## 5. Boundary Cases & Failure Modes

- **Zero Result (`-1/2+1/2`):** $x = 0 \implies \gcd(0, Y) = Y \implies 0 / 1 \implies \mathbf{\text{"0/1"}}$.
- **Negative Result (`1/3-1/2`):** Preserves negative sign on numerator: $\mathbf{\text{"-1/6"}}$.
- **Denominator 10 (`1/10+1/10`):** Handled with integer division $2520 / 10 = 252$.
- **No Leading Sign (`1/2+1/3`):** Prepending `+` standardizes tokenization.

---

## 6. Traps & Common Anti-Patterns

- **Using Floating-Point Numbers (`float`):** Floating-point arithmetic introduces rounding inaccuracies (e.g. $1/3 \approx 0.3333333333333333$), preventing exact rational reduction.
- **Forgetting `abs()` on GCD:** In some languages, $\gcd(-x, y)$ returns a negative number, which can invert signs. Always take $\gcd(|x|, y)$ so the denominator remains strictly positive.
- **Forgetting to Reduce 0 to `"0/1"`:** If the numerator is 0, returning `0/2520` is incorrect; dividing by $\gcd(0, 2520) = 2520$ produces the required `0/1`.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Parsing the expression of length $N$ takes $\mathcal{O}(N)$ linear scan.
  - Number of fractions $K \le N / 3$.
  - Computing GCD of two integers $\le 10^6$ takes $\mathcal{O}(\log(\min(|x|, Y)))$ Euclidean steps ($< 10$ iterations).
  - Total Time: strictly linear $\mathcal{O}(N)$. For $N \le 100$, completes in $< 1$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ auxiliary memory (only integer variables $x, Y, z$).
