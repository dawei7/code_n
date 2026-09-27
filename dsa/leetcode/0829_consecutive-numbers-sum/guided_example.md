# Guided Example: Consecutive Numbers Sum

We trace the step-by-step arithmetic progression sum algebraic reduction ($n = k \cdot x + \frac{k(k-1)}{2}$), doubled product factorization ($2n = k(2x + k - 1)$), integer parity and positivity constraints ($2x = \frac{2n}{k} - k + 1$), $O(\sqrt{2n})$ bounded term enumeration ($k(k+1) \le 2n$), and valid consecutive partition tallying on representative integers:

- **Input:** $n = 9$
- **Required output:** `3`
  - Consecutive partition rules:
    - We want to express positive integer $n$ as the sum of $k$ consecutive positive integers starting at some base $x \ge 1$:
      $$
      n = x + (x + 1) + (x + 2) + \dots + (x + k - 1)
      $$
    - Objective: Count the number of pairs $(k, x)$ with $k \ge 1$ and $x \ge 1$ that satisfy this equation.
    - For $n = 9$:
      - Length $k = 1$: $[9] \implies 9$.
      - Length $k = 2$: $[4, 5] \implies 4 + 5 = 9$.
      - Length $k = 3$: $[2, 3, 4] \implies 2 + 3 + 4 = 9$.
      - Total valid representations: **3**.
- **Arithmetic Progression & Parity Invariant:**
  - **Algebraic Derivation of Base $x$:**
    - The sum of $k$ consecutive integers starting at $x$ is:
      $$
      n = k \cdot x + \sum_{j = 0}^{k - 1} j = k \cdot x + \frac{k(k - 1)}{2}
      $$
    - Multiply both sides by 2:
      $$
      2n = 2kx + k(k - 1) = k(2x + k - 1)
      $$
    - Solving for the initial integer $x$:
      $$
      2x = \frac{2n}{k} - k + 1 \implies x = \frac{\frac{2n}{k} - k + 1}{2}
      $$
  - **The Three Validity Criteria for a Chosen $k$:**
    1. **Divisibility:** $k$ must be a factor of $2n$:
       $$
       2n \bmod k == 0
       $$
    2. **Parity (Integrality of $x$):** The numerator must be even:
       $$
       \left( \frac{2n}{k} - k + 1 \right) \bmod 2 == 0
       $$
    3. **Positivity ($x \ge 1$):**
       $$
       2x \ge 2 \iff \frac{2n}{k} - k + 1 \ge 2 \iff \frac{k(k + 1)}{2} \le n
       $$
       $$
       k(k + 1) \le 2n
       $$
  - **The $O(\sqrt{2n})$ Upper Bound:**
    - The quadratic inequality $k^2 + k \le 2n$ bounds $k$ strictly by $\sqrt{2n}$:
      $$
      k \le \sqrt{2n}
      $$
    - For $n \le 10^9$, $\sqrt{2n} \le \sqrt{2 \times 10^9} \approx 44,721$.
    - Testing integers $k = 1, 2, \dots, \lfloor \sqrt{2n} \rfloor$ takes at most $45,000$ loop iterations ($< 5$ ms).
- **Step-by-Step Worked Execution Trace on $n = 9$:**
  - Compute target $2n$:
    $$
    2n = 2 \times 9 = \mathbf{18}
    $$
  - Loop while $k(k + 1) \le 18$:
  - **Term Length $k = 1$:**
    - Bound check: $1(2) = 2 \le 18 \implies \mathbf{Valid.}$
    - Divisibility check: $18 \bmod 1 = 0 \implies \mathbf{Pass.}$
    - Quotient: $18 / 1 = 18$.
    - Numerator: $18 - 1 + 1 = \mathbf{18}$.
    - Parity check: $18 \bmod 2 = 0 \implies \mathbf{Even\ (Pass)!}$
    - Starting integer:
      $$
      x = \frac{18}{2} = \mathbf{9} \quad (\text{Sequence: } [9])
      $$
    - Valid! $ans \leftarrow 0 + 1 = \mathbf{1}$.
  - **Term Length $k = 2$:**
    - Bound check: $2(3) = 6 \le 18 \implies \mathbf{Valid.}$
    - Divisibility check: $18 \bmod 2 = 0 \implies \mathbf{Pass.}$
    - Quotient: $18 / 2 = 9$.
    - Numerator: $9 - 2 + 1 = \mathbf{8}$.
    - Parity check: $8 \bmod 2 = 0 \implies \mathbf{Even\ (Pass)!}$
    - Starting integer:
      $$
      x = \frac{8}{2} = \mathbf{4} \quad (\text{Sequence: } [4, 5])
      $$
    - Valid! $ans \leftarrow 1 + 1 = \mathbf{2}$.
  - **Term Length $k = 3$:**
    - Bound check: $3(4) = 12 \le 18 \implies \mathbf{Valid.}$
    - Divisibility check: $18 \bmod 3 = 0 \implies \mathbf{Pass.}$
    - Quotient: $18 / 3 = 6$.
    - Numerator: $6 - 3 + 1 = \mathbf{4}$.
    - Parity check: $4 \bmod 2 = 0 \implies \mathbf{Even\ (Pass)!}$
    - Starting integer:
      $$
      x = \frac{4}{2} = \mathbf{2} \quad (\text{Sequence: } [2, 3, 4])
      $$
    - Valid! $ans \leftarrow 2 + 1 = \mathbf{3}$.
  - **Term Length $k = 4$:**
    - Bound check:
      $$
      k(k + 1) = 4 \times 5 = 20 > 18 \implies \mathbf{Upper\ Bound\ Exceeded!}
      $$
    - Loop terminates.
  - **Final Output:**
    $$
    ans = \mathbf{3}
    $$
- **Prime Number Trace ($n = 5$):**
  - $2n = 10$.
  - $k = 1$: $x = 5$ ($[5]$).
  - $k = 2$: $x = 2$ ($[2, 3]$).
  - $k = 3$: $3 \times 4 = 12 > 10$ (Stops).
  - All primes have exactly 2 representations ($n$ and $\frac{n-1}{2} + \frac{n+1}{2}$).
- **Power of Two Trace ($n = 8$):**
  - $2n = 16$.
  - $k = 1$: $x = 8$ ($[8]$).
  - $k = 2$: $16 / 2 = 8$, numerator $8 - 2 + 1 = 7$ (odd, fails parity!).
  - $k = 3$: $16 \bmod 3 \ne 0$.
  - $k = 4$: $4 \times 5 = 20 > 16$.
  - Powers of 2 have only $1$ representation ($[8]$).

This instance demonstrates arithmetic progression parameterization on Diophantine equations and quadratic constraint reduction, mathematically proves why valid sequence lengths correspond bijectively to odd divisors of $n$, and derives $O(\sqrt{N})$ execution time and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given integer $n$:
Count how many ways $n$ can be expressed as a sum of **consecutive positive integers**.

```text
n = 9

Ways to form 9:
  k = 1: [ 9 ]             -> 9
  k = 2: [ 4, 5 ]          -> 4 + 5 = 9
  k = 3: [ 2, 3, 4 ]       -> 2 + 3 + 4 = 9

Result: 3
```

### The Invariant of the $O(\sqrt{2n})$ Search
- The sum of $k$ consecutive integers starting at $x$ satisfies:
  $$
  2n = k(2x + k - 1)
  $$
- This yields $2x = \frac{2n}{k} - k + 1$.
- For $x \ge 1$ to be an integer, $k \mid 2n$ and $\frac{2n}{k} - k + 1$ must be positive and even.
- Because $k(k + 1) \le 2n$, we only need to test $k \le \sqrt{2n}$.

---

## 2. Conceptual Foundation & Invariants

### 1. Diophantine Factorization:
$$
2x = \frac{2n}{k} - k + 1
$$

### 2. Valid Progression Predicate:
$$
\text{Valid}(k) \iff \Big( 2n \equiv 0 \pmod k \Big) \;\land\; \left( \frac{2n}{k} - k + 1 \equiv 0 \pmod 2 \right) \;\land\; \Big( k(k + 1) \le 2n \Big)
$$
$$
ans = \sum_{k = 1}^{\lfloor \sqrt{2n} \rfloor} \mathbb{I}[\text{Valid}(k)]
$$

> **Odd Divisor Theorem Invariant.** Every representation of $n$ as a sum of consecutive positive integers corresponds bijectively to an odd divisor of $n$. The number of solutions equals $d(n_{\text{odd}})$, the number of divisors of the maximal odd factor of $n$.

---

## 3. Step-by-Step Worked Execution

We trace $n = 9$ ($2n = 18$):

---

### Step 1: $k = 1$
- $18 / 1 = 18$. Numerator: $18 - 1 + 1 = 18$ (even) $\implies x = 9$ ($[9]$). Valid!

---

### Step 2: $k = 2$
- $18 / 2 = 9$. Numerator: $9 - 2 + 1 = 8$ (even) $\implies x = 4$ ($[4, 5]$). Valid!

---

### Step 3: $k = 3$
- $18 / 3 = 6$. Numerator: $6 - 3 + 1 = 4$ (even) $\implies x = 2$ ($[2, 3, 4]$). Valid!

---

### Step 4: $k = 4$
- $4 \times 5 = 20 > 18 \implies$ terminate loop!

---

### Step 5: Output
$$
\mathbf{3}
$$

---

## 4. Complete Execution Trace

| Length $k$ | Quadratic Bound $k(k + 1) \le 2n$ | Divisor Check ($2n \bmod k == 0$) | Quotient $2n / k$ | Numerator $2x$ | Is Even? | Starting Integer $x$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | $2 \le 18$ | Yes | $18$ | $18$ | **Yes** | $9$ |
| $2$ | $6 \le 18$ | Yes | $9$ | $8$ | **Yes** | $4$ |
| $3$ | $12 \le 18$ | Yes | $6$ | $4$ | **Yes** | $2$ |
| **$4$** | **$20 > 18$ (Exceeded)** | — | — | — | — | **Stop** |
| **Total** | — | — | — | — | — | **`3`** |

---

## 5. Boundary Cases & Failure Modes

- **$n = 1$:** Only $[1] \implies 1$.
- **Powers of 2 ($n = 2^p$):** No odd divisors $> 1$; only $k = 1$ succeeds $\implies 1$.
- **Maximum $n = 10^9$:** Loop executes at most $44,721$ steps ($< 5$ ms).
- **Parity Check Missing:** Omitting the even-parity check will falsely accept fractional start points (e.g. $k = 2$ for $n = 8$ yields $x = 3.5$).

---

## 6. Traps & Common Anti-Patterns

- **Checking All $k$ up to $n$ ($O(N)$):** For $n = 10^9$, a linear loop causes Time Limit Exceeded. The bound $k(k + 1) \le 2n$ guarantees termination at $\sqrt{2n}$.
- **Simulating the Sequences:** Never sum elements in an inner loop. Closed-form algebra solves $x$ directly in $O(1)$.
- **Division Truncation Confusion:** Always verify $2n \bmod k == 0$ before computing the quotient to prevent integer division truncation errors.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Loop iterates while $k(k + 1) \le 2n$, which terminates at $k \approx \sqrt{2n}$.
  - Constant-time scalar arithmetic per iteration: $\mathcal{O}(1)$.
  - Total Time: strictly $\mathcal{O}(\sqrt{N})$ where $N \le 10^9 \implies \le 4.5 \times 10^4$ steps. Completes in $< 3$ ms.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space.
