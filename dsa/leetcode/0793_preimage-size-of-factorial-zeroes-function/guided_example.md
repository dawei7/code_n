# Guided Example: Preimage Size of Factorial Zeroes Function

We trace the step-by-step 5-adic valuation of factorials, Legendre's trailing zero formula ($f(x) = \sum \lfloor x/5^p \rfloor$), non-decreasing step function geometry, block multiplicity theorem ($|f^{-1}(k)| \in \{0, 5\}$), monotonic binary search bounds ($g(k) = \text{bisect\_left}(f \ge k)$), discontinuous gap detection ($v_5(x) \ge 2$), and exact preimage fiber size derivation on representative zero counts:

- **Input:** $k = 0$
- **Required output:** `5`
  - Problem specifications & Legendre's formula:
    - Let $f(x)$ denote the number of trailing zeroes in $x!$.
    - A trailing zero is produced by each factor of $10 = 2 \times 5$. Since factors of 2 are strictly more abundant than factors of 5 in any factorial, $f(x)$ equals the 5-adic valuation of $x!$:
      $$
      f(x) = \sum_{p=1}^{\infty} \left\lfloor \frac{x}{5^p} \right\rfloor = \left\lfloor \frac{x}{5} \right\rfloor + \left\lfloor \frac{x}{25} \right\rfloor + \left\lfloor \frac{x}{125} \right\rfloor + \dots
      $$
    - Objective: Given $k$, determine how many non-negative integers $x$ satisfy $f(x) = k$.
    - For $k = 0$:
      - $0! = 1 \implies 0$ zeroes ($f(0) = 0$)
      - $1! = 1 \implies 0$ zeroes ($f(1) = 0$)
      - $2! = 2 \implies 0$ zeroes ($f(2) = 0$)
      - $3! = 6 \implies 0$ zeroes ($f(3) = 0$)
      - $4! = 24 \implies 0$ zeroes ($f(4) = 0$)
      - $5! = 120 \implies 1$ zero ($f(5) = 1$)
      - Exactly 5 integers $\{0, 1, 2, 3, 4\}$ have $f(x) = 0$.
      - Preimage size is **5**.
- **The Binary Dichotomy Theorem ($|f^{-1}(k)| \in \{0, 5\}$):**
  - **The Step-Plateau Property:**
    - Notice that between any multiple of 5, say $5m$, and $5m + 4$:
      $$
      \left\lfloor \frac{5m}{5^p} \right\rfloor = \left\lfloor \frac{5m + 1}{5^p} \right\rfloor = \dots = \left\lfloor \frac{5m + 4}{5^p} \right\rfloor
      $$
    - No factor of 5 enters during the integers $5m + 1, 5m + 2, 5m + 3, 5m + 4$.
    - Therefore, $f(x)$ is **constant across every 5-integer interval**:
      $$
      f(5m) = f(5m + 1) = f(5m + 2) = f(5m + 3) = f(5m + 4)
      $$
  - **The Step Jumps:**
    - When transitioning from $5m - 1$ to $5m$, $f(x)$ increases by the number of factors of 5 in $5m$:
      $$
      f(5m) - f(5m - 1) = v_5(5m) \ge 1
      $$
    - If $5m$ is a multiple of 25 ($5^2$), 125 ($5^3$), etc., $v_5(5m) \ge 2$.
    - When $v_5(5m) \ge 2$, the value of $f(x)$ jumps by 2 or more, **completely skipping one or more integer values of $k$**!
  - **Preimage Cardinality Conclusion:**
    - If a target $k$ is attained, it is attained by an entire 5-integer block: $|f^{-1}(k)| = 5$.
    - If $k$ falls in a jump gap, it is never attained: $|f^{-1}(k)| = 0$.
    - Preimage size is **always either 0 or 5**!
  - **Binary Search Formulation:**
    - Let $g(k)$ be the smallest integer $x$ such that $f(x) \ge k$.
    - Because $f(x)$ is monotonically non-decreasing, find $g(k)$ and $g(k + 1)$ via binary search over $[0, 5k]$.
    - Preimage size is directly:
      $$
      |f^{-1}(k)| = g(k + 1) - g(k)
      $$
- **Step-by-Step Worked Execution Trace on $k = 0$:**
  - Compute $g(0)$:
    - Smallest $x \ge 0$ such that $f(x) \ge 0$ is $x = \mathbf{0}$.
  - Compute $g(1)$:
    - Smallest $x$ such that $f(x) \ge 1$:
    - Test $x = 4$: $f(4) = 0 < 1$.
    - Test $x = 5$: $f(5) = \lfloor 5/5 \rfloor = 1 \ge 1$.
    - Thus, $g(1) = \mathbf{5}$.
  - Preimage fiber size:
    $$
    ans = g(1) - g(0) = 5 - 0 = \mathbf{5}
    $$
- **Skipped Value Discontinuous Gap Trace on $k = 5$:**
  - Let's check $x = 24$:
    $$
    f(24) = \left\lfloor \frac{24}{5} \right\rfloor = \mathbf{4}
    $$
  - Let's check $x = 25$:
    $$
    f(25) = \left\lfloor \frac{25}{5} \right\rfloor + \left\lfloor \frac{25}{25} \right\rfloor = 5 + 1 = \mathbf{6}
    $$
  - Notice the jump:
    $$
    f(24) = 4 \quad \longrightarrow \quad f(25) = 6
    $$
  - The function jumps directly from 4 to 6!
  - Value $k = 5$ is **never produced** by any integer factorial in mathematics.
  - Binary search results:
    - $g(5) = 25$ (first $x$ with $f(x) \ge 5$).
    - $g(6) = 25$ (first $x$ with $f(x) \ge 6$).
  - Preimage size:
    $$
    ans = g(6) - g(5) = 25 - 25 = \mathbf{0}
    $$
- **Attained Value Trace on $k = 3$:**
  - $f(14) = 2$.
  - $f(15) = 3$. Values $\{15, 16, 17, 18, 19\}$ all have $f(x) = 3$.
  - $f(20) = 4$.
  - $g(3) = 15, g(4) = 20 \implies ans = 20 - 15 = \mathbf{5}$.

This instance demonstrates arithmetic p-adic valuation analysis and monotone step function discretization, mathematically proves why the preimage fibers of Legendre's trailing zero map partition into empty sets or 5-element intervals, and derives $O(\log^2 K)$ execution time and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Let $f(x)$ be the number of trailing zeroes in $x!$.
Given $k$, find how many integers $x$ have $f(x) = k$.

```text
Legendre's formula:
  f(x) = x // 5 + x // 25 + x // 125 + ...

Values of f(x):
  x = 0..4:   f(x) = 0  (5 values)
  x = 5..9:   f(x) = 1  (5 values)
  x = 10..14: f(x) = 2  (5 values)
  x = 15..19: f(x) = 3  (5 values)
  x = 20..24: f(x) = 4  (5 values)
  x = 25..29: f(x) = 6  (5 values, skipped 5!)

Preimage size is ALWAYS either 5 (if attained) or 0 (if skipped)!
```

### The Invariant of the 5-Integer Step Plateau
- $f(x)$ is constant on every block $[5m, 5m + 4]$.
- At multiples of 25 ($5^2$), $f(x)$ jumps by $\ge 2$, skipping some values of $k$.
- By binary searching for the first $x$ with $f(x) \ge k$, the answer is simply $g(k + 1) - g(k) \in \{0, 5\}$.

---

## 2. Conceptual Foundation & Invariants

### 1. Legendre's Summation:
$$
f(x) = \sum_{i = 1}^\infty \left\lfloor \frac{x}{5^i} \right\rfloor
$$

### 2. Fiber Cardinality Bound:
$$
|f^{-1}(k)| = g(k + 1) - g(k) \in \{0, 5\}
$$
where $g(k) = \min \{ x \ge 0 \mid f(x) \ge k \}$.

> **5-Adic Step Discontinuity Invariant.** The function $f: \mathbb{N} \to \mathbb{N}$ has forward difference $\Delta f(x) = v_5(x + 1)$. Because $\Delta f(x) = 0$ whenever $x + 1 \not\equiv 0 \pmod 5$, non-empty fibers $f^{-1}(k)$ are translate invariant congruence classes modulo 5 of exact measure 5.

---

## 3. Step-by-Step Worked Execution

We trace $k = 0$:

---

### Step 1: Find $g(0)$
- Smallest $x$ with $f(x) \ge 0$ is $x = 0$.

---

### Step 2: Find $g(1)$
- Smallest $x$ with $f(x) \ge 1$ is $x = 5$ ($f(5) = 1$).

---

### Step 3: Compute Difference
- $g(1) - g(0) = 5 - 0 = \mathbf{5}$.

---

### Step 4: Output
$$
\mathbf{5}
$$

---

## 4. Complete Execution Trace

| Target $k$ | First $x$ with $f(x) \ge k$ ($g(k)$) | First $x$ with $f(x) \ge k + 1$ ($g(k+1)$) | Difference $g(k+1) - g(k)$ | Preimage Size |
|:---:|:---:|:---:|:---:|:---:|
| $0$ | $0$ | $5$ | $5 - 0 = 5$ | **$5$** |
| $1$ | $5$ | $10$ | $10 - 5 = 5$ | **$5$** |
| $4$ | $20$ | $25$ | $25 - 20 = 5$ | **$5$** |
| **$5$ (Skipped)** | **$25$** | **$25$** | **$25 - 25 = 0$** | **`0`** |

---

## 5. Boundary Cases & Failure Modes

- **$k = 0$:** Evaluates $x \in [0, 4] \implies 5$.
- **Skipped Values ($k = 5, 11, 17, 23, 29, 30$):** Jumps skip these values entirely $\implies 0$.
- **Large Values ($k = 10^9$):** $x$ is at most $5k \le 5 \times 10^9$; binary search converges in $\le 33$ iterations.
- **Factorial Zero Overflow:** Legendre's loop divides by 5 at each step, running in $\le 15$ operations for any 64-bit integer.

---

## 6. Traps & Common Anti-Patterns

- **Computing Factorials Explicitly ($x!$):** For $x = 25$, $25! \approx 1.55 \times 10^{25}$. For $k = 10^9$, $x \approx 4 \times 10^9$, which has millions of digits and cannot be stored. Legendre's formula computes zeroes directly in $O(\log_5 x)$ without calculating factorials.
- **Searching for All $x$ Linearly:** Searching through numbers one by one takes $O(k)$ time, which TLEs when $k = 10^9$. Monotonic binary search evaluates the boundary in $\approx 33$ steps.
- **Upper Bound of Binary Search:** $f(5k) = k + \lfloor k/5 \rfloor + \dots \ge k$. Thus $5k$ is always a safe upper bound for the binary search.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Legendre function $f(x)$ takes $\mathcal{O}(\log_5 x)$ divisions.
  - Binary search over range $[0, 5k]$ takes $\mathcal{O}(\log(5k))$ iterations.
  - Total Time: strictly $\mathcal{O}(\log_5 k \cdot \log(5k))$ where $k \le 10^9 \implies \le 33 \times 14 \approx 460$ arithmetic operations. Completes in $< 0.05$ ms.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space.
