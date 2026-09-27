# Guided Example: Sum of Square Numbers

We trace the step-by-step integer square search space initialization ($a = 0, \; b = \lfloor\sqrt{c}\rfloor$), quadratic polynomial monotonicity ($f(a, b) = a^2 + b^2$), two-pointer bilateral convergence, sum deficit advancement ($s < c \implies a \leftarrow a + 1$), sum excess reduction ($s > c \implies b \leftarrow b - 1$), and Diophantine representation validation on representative integer targets:

- **Input:** $c = 5$
- **Required output:** `true`
  - Problem objective: Determine whether there exist two non-negative integers $a$ and $b$ ($a, b \ge 0$) such that:
    $$
    a^2 + b^2 = c
    $$
  - The integers $a$ and $b$ can be identical (e.g. $0^2 + 0^2 = 0$, $2^2 + 2^2 = 8$).
- **Bilateral Monotonic Two-Pointer Invariant:**
  - Since $a, b \ge 0$, the smallest possible value for $a$ is $0$, and the largest possible value for either integer is:
    $$
    b_{max} = \lfloor\sqrt{c}\rfloor
    $$
    (Because if either $a$ or $b > \sqrt{c}$, their square alone exceeds $c$).
  - We can without loss of generality enforce the ordering $a \le b$.
  - **The Coordinate Grid & Monotonicity:**
    - Consider the function $s(a, b) = a^2 + b^2$.
    - $s(a, b)$ is **strictly increasing** with respect to both $a$ and $b$ on $\mathbb{N}_0$.
    - At any point in the search:
      - If $s(a, b) < c$: The current sum is too small. Because $b$ is already the largest valid candidate paired with $a$, no smaller choice of $b$ can reach $c$. Therefore, $a$ cannot be part of any solution with any integer $\le b$. We must increment $a$:
        $$
        a \leftarrow a + 1
        $$
      - If $s(a, b) > c$: The current sum is too large. Because $a$ is already the smallest non-negative candidate paired with $b$, no larger choice of $a$ can produce a smaller sum. Therefore, $b$ cannot be part of any solution. We must decrement $b$:
        $$
        b \leftarrow b - 1
        $$
      - If $s(a, b) == c$: We have found an exact Diophantine representation $\implies$ return **`true`**!
    - If the pointers cross ($a > b$) without finding a match, no valid integer pair exists $\implies$ return **`false`**.
- **Step-by-Step Worked Execution Trace on $c = 5$:**
  - Compute upper bound $b$:
    $$
    b = \lfloor\sqrt{5}\rfloor = \mathbf{2}
    $$
  - Initial pointer state:
    $$
    a = 0, \quad b = 2
    $$
  - **Iteration 1 ($a = 0, b = 2$):**
    - Compute sum of squares:
      $$
      s = 0^2 + 2^2 = 0 + 4 = \mathbf{4}
      $$
    - Compare with target $c = 5$:
      $$
      4 < 5 \implies \mathbf{Deficit\ detected!}
      $$
    - The pair $(0, 2)$ is too small. No $b' \le 2$ can make $0^2 + (b')^2 = 5$.
    - Advance lower pointer:
      $$
      a \leftarrow 0 + 1 = \mathbf{1}
      $$
  - **Iteration 2 ($a = 1, b = 2$):**
    - Pointers still valid: $a = 1 \le b = 2$.
    - Compute sum of squares:
      $$
      s = 1^2 + 2^2 = 1 + 4 = \mathbf{5}
      $$
    - Compare with target $c = 5$:
      $$
      5 == 5 \implies \mathbf{Exact\ match\ found!}
      $$
    - Return **`true`**.
- **Execution Trace on Impossible Input ($c = 3$):**
  - $b = \lfloor\sqrt{3}\rfloor = 1$.
  - Start: $a = 0, b = 1$.
    - $0^2 + 1^2 = 1 < 3 \implies a \leftarrow 1$.
  - State: $a = 1, b = 1$.
    - $1^2 + 1^2 = 2 < 3 \implies a \leftarrow 2$.
  - Pointers cross: $a = 2 > b = 1 \implies$ Loop terminates.
  - Return **`false`**.
- **Zero Input Boundary ($c = 0$):**
  - $b = \lfloor\sqrt{0}\rfloor = 0$.
  - $a = 0, b = 0 \implies 0^2 + 0^2 = 0 == 0 \implies$ Returns **`true`**.
- **Perfect Square Target ($c = 4$):**
  - $b = 2$.
  - $a = 0, b = 2 \implies 0^2 + 2^2 = 4 == 4 \implies$ Returns **`true`** on step 1.

This instance demonstrates Diophantine sum-of-squares verification via monotonic 2D grid walk, mathematically proves why eliminate-and-contract bounds prune candidate pairs without false negatives, and derives $O(\sqrt{c})$ execution time and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a non-negative integer $c$:
Determine if there exist integers $a, b \ge 0$ such that $a^2 + b^2 = c$.

```text
c = 5:
  sqrt(5) ~ 2.236 -> b starts at 2, a starts at 0

Step 1: a = 0, b = 2 -> 0^2 + 2^2 = 4 < 5 -> sum too small, a increases to 1
Step 2: a = 1, b = 2 -> 1^2 + 2^2 = 5 == 5 -> MATCH!

Result: true
```

### The Invariant of Monotonic Search Space Elimination
- The search space consists of integer pairs in $[0, \lfloor\sqrt{c}\rfloor] \times [0, \lfloor\sqrt{c}\rfloor]$.
- Because $f(a, b) = a^2 + b^2$ is monotonically increasing in each variable:
  - If $a^2 + b^2 < c$, then $a^2 + (b')^2 < c$ for all $b' \le b$. The entire row $a$ is eliminated.
  - If $a^2 + b^2 > c$, then $(a')^2 + b^2 > c$ for all $a' \ge a$. The entire column $b$ is eliminated.
- Every step permanently eliminates one row or one column.

---

## 2. Conceptual Foundation & Invariants

### 1. Two-Pointer Convergent Loop:
Initialize:
$$
a = 0, \quad b = \lfloor\sqrt{c}\rfloor
$$
While $a \le b$:
- $s = a^2 + b^2$
- If $s == c \implies$ return `true`
- If $s < c \implies a \leftarrow a + 1$
- If $s > c \implies b \leftarrow b - 1$
Return `false`.

### 2. Number Theoretic Connection (Fermat's Theorem):
- An integer $c$ can be written as the sum of two squares if and only if in its prime factorization, every prime factor of the form $4k + 3$ appears with an **even exponent**.
- The two-pointer search achieves the same test in $\mathcal{O}(\sqrt{c})$ without requiring full prime factorization.

> **Bilateral Pruning Invariant.** For any pair $(a, b)$, the sign of $a^2 + b^2 - c$ determines a non-invertible hyperplane separating the remaining valid Diophantine solutions from the eliminated half-plane.

---

## 3. Step-by-Step Worked Execution

We trace $c = 5$:

---

### Step 1: Initialize Boundaries
- $a = 0$.
- $b = \lfloor\sqrt{5}\rfloor = 2$.

---

### Step 2: Step 1
- $s = 0^2 + 2^2 = 4$.
- $4 < 5 \implies a$ increases to 1.

---

### Step 3: Step 2
- $s = 1^2 + 2^2 = 5$.
- $5 == 5 \implies$ Match! Return **`true`**.

---

## 4. Complete Execution Trace

| Iteration | Left Pointer $a$ | Right Pointer $b$ | Evaluated Sum $a^2 + b^2$ | Comparison with $c = 5$ | Action Taken | Next State $(a, b)$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | $0$ | $2$ | $0 + 4 = 4$ | $4 < 5$ (Too small) | Increment $a$ | $(1, 2)$ |
| **$2$** | **$1$** | **$2$** | **$1 + 4 = 5$** | **$5 == 5$ (Match)** | **Return `true`** | **Terminated** |

---

## 5. Boundary Cases & Failure Modes

- **$c = 0$:** $0^2 + 0^2 = 0 \implies$ returns `true`.
- **$c = 1$:** $0^2 + 1^2 = 1 \implies$ returns `true`.
- **$c = 2$:** $1^2 + 1^2 = 2 \implies$ returns `true`.
- **$c = 3$:** $a > b \implies$ returns `false`.
- **Large Prime of Form $4k+1$ ($c = 13$):** $2^2 + 3^2 = 13 \implies$ `true`.
- **Large Target ($c = 2^{31} - 1$):** $\sqrt{c} \approx 46340$, finishes in $< 1$ ms.

---

## 6. Traps & Common Anti-Patterns

- **Searching Up to $c$ Instead of $\sqrt{c}$:** Setting $b = c$ turns an $O(\sqrt{c})$ algorithm into $O(c)$ (running $2 \cdot 10^9$ operations), leading to Time Limit Exceeded.
- **Strict Inequality on Pointer Loop ($a < b$):** Using $a < b$ fails when $c$ is twice a square (e.g. $c = 8 = 2^2 + 2^2$, or $c = 0 = 0^2 + 0^2$). The condition must be $a \le b$.
- **Integer Overflow in Other Languages:** In C/C++, $b^2$ for $b \approx 46340$ approaches $2 \cdot 10^9$. If $c = 2^{31} - 1$, $a^2 + b^2$ can overflow a signed 32-bit integer; use 64-bit integers (`long long`).

---

## 7. Complexity Derivation

- **Time Complexity:**
  - $a$ starts at 0 and increments at most $\lfloor\sqrt{c}\rfloor$ times.
  - $b$ starts at $\lfloor\sqrt{c}\rfloor$ and decrements at most $\lfloor\sqrt{c}\rfloor$ times.
  - Total iterations: at most $2\sqrt{c}$.
  - Total Time: $\mathcal{O}(\sqrt{c})$. For $c = 2^{31} - 1$, $\sqrt{c} \approx 46{,}340$ steps, completing in $< 1$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ auxiliary space.
