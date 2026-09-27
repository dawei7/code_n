# Guided Example: 2 Keys Keyboard

We trace the step-by-step buffer multiplier mechanics (1 `Copy All` + $p - 1$ `Paste` operations $\implies p$ steps to scale by factor $p$), prime factor sum equivalence ($n = \prod p_i \implies \text{steps} = \sum p_i$), composite factorization sub-additivity proof ($a + b \le a \cdot b$), trial division prime factor extraction, and minimal operational step derivation on representative target character lengths:

- **Input:** $n = 12$
- **Required output:** `7`
  - Notepad rules:
    - Screen begins with exactly one character: `'A'`.
    - Operation 1 (`Copy All`): Copies the entire current text on the screen to clipboard.
    - Operation 2 (`Paste`): Pastes the clipboard text onto the screen.
    - Objective: Reach exactly $n$ characters on the screen in the **minimum total operations**.
- **Multiplication by Factor $p$ via Copy and Paste:**
  - Suppose we currently have $m$ characters on screen.
  - To multiply our character count from $m$ to $m \cdot p$:
    - Step 1: Execute `Copy All` (1 operation). Clipboard now holds $m$ characters.
    - Steps $2 \dots p$: Execute `Paste` exactly $p - 1$ times ($p - 1$ operations).
      - After 1 paste: $m + m = 2m$.
      - After 2 pastes: $2m + m = 3m$.
      - ...
      - After $p - 1$ pastes: $m + (p - 1)m = m \cdot p$.
    - Total operations consumed:
      $$
      1 + (p - 1) = \mathbf{p}
      $$
    - Multiplying the string length by factor $p$ costs exactly **$p$ operations**.
  - **Sub-Additivity & Prime Decomposition Theorem:**
    - Suppose a number can be factored as $n = a \cdot b$.
      - Factoring in one step by $a \cdot b$ costs $a \cdot b$ operations.
      - Factoring in two sequential steps (scale by $a$, then scale by $b$) costs $a + b$ operations.
    - For all integers $a, b \ge 2$:
      $$
      a \cdot b - (a + b) = (a - 1)(b - 1) - 1 \ge (2 - 1)(2 - 1) - 1 = 0 \implies a + b \le a \cdot b
      $$
    - Strict inequality holds whenever $a > 2$ or $b > 2$ (e.g. $2 \times 3 = 6$, but $2 + 3 = 5 < 6$).
    - Therefore, breaking any composite factor into its constituent **prime factors strictly reduces or maintains the total operation count**!
  - **Fundamental Result:**
    $$
    \text{Minimum Operations}(n) = \sum_{p \in \text{prime factors of } n} p \quad (\text{with } n = 1 \implies 0)
    $$
- **Step-by-Step Worked Execution Trace on $n = 12$:**
  - Target: $n = 12$.
  - **Step 1: Find Prime Factorization of $12$:**
    - Test smallest prime $p = 2$:
      $$
      12 \pmod 2 == 0 \implies 12 = 2 \times 6 \quad (\text{Factor: } 2)
      $$
    - Test factor $2$ on $6$:
      $$
      6 \pmod 2 == 0 \implies 6 = 2 \times 3 \quad (\text{Factor: } 2)
      $$
    - Remaining quotient is prime $3$:
      $$
      3 = 3 \times 1 \quad (\text{Factor: } 3)
      $$
    - Complete prime factorization multiset:
      $$
      12 = 2 \times 2 \times 3
      $$
  - **Step 2: Sum the Prime Factors:**
    $$
    ans = 2 + 2 + 3 = \mathbf{7}
    $$
  - **Step 3: Concrete Physical Keystroke Timeline:**
    - Start at $t = 0$: Screen has `'A'` (length 1).
    - **Phase 1 (Scale by $2$ $\implies 2$ operations):**
      - Op 1: `Copy All` (Clipboard = `'A'`, length 1)
      - Op 2: `Paste` (Screen = `'AA'`, length 2)
    - **Phase 2 (Scale by $2$ $\implies 2$ operations):**
      - Op 3: `Copy All` (Clipboard = `'AA'`, length 2)
      - Op 4: `Paste` (Screen = `'AAAA'`, length 4)
    - **Phase 3 (Scale by $3$ $\implies 3$ operations):**
      - Op 5: `Copy All` (Clipboard = `'AAAA'`, length 4)
      - Op 6: `Paste` (Screen = length $4 + 4 = 8$)
      - Op 7: `Paste` (Screen = length $8 + 4 = 12$)
    - Screen holds exactly $12$ characters `'A'` after $7$ operations.
    - No sequence of operations can reach 12 in fewer than 7 steps (e.g. scaling by 4 then 3 takes $4 + 3 = 7$; scaling by 6 then 2 takes $6 + 2 = 8$; copying 1 and pasting 11 times takes $1 + 11 = 12$).
- **Prime Number Target ($n = 3$):**
  - $3$ is prime $\implies$ prime factor is $3$.
  - 1 `Copy All` + 2 `Paste` $\implies \mathbf{3}$ operations.
- **Base Case ($n = 1$):**
  - Screen already starts with 1 `'A'`.
  - Zero operations required $\implies \mathbf{0}$.
- **Power of Two ($n = 8$):**
  - $8 = 2 \times 2 \times 2 \implies 2 + 2 + 2 = \mathbf{6}$ operations.

This instance demonstrates prime factorization arithmetic and sub-additive state transitions, mathematically proves why complete prime decomposition achieves the absolute operational infimum, and derives $O(\sqrt{n})$ execution time and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an integer $n$:
Starting with 1 `'A'`, find the **minimum operations** (`Copy All` or `Paste`) to produce exactly $n$ `'A'`s.

```text
Target n = 12

Prime factorization: 12 = 2 * 2 * 3

Phase 1 (x2): Copy, Paste                -> length 2  (2 ops)
Phase 2 (x2): Copy, Paste                -> length 4  (2 ops)
Phase 3 (x3): Copy, Paste, Paste         -> length 12 (3 ops)

Total Operations = 2 + 2 + 3 = 7
```

### The Invariant of Prime Factorization
- Scaling the text length by a factor $p$ requires 1 copy and $p - 1$ pastes, costing $1 + (p - 1) = p$ operations.
- Because $a + b \le a \cdot b$ for all integers $\ge 2$, factoring into primes always costs less than or equal to factoring into composite numbers.
- The answer is strictly the **sum of the prime factors of $n$**.

---

## 2. Conceptual Foundation & Invariants

### 1. The Sub-Additivity Identity:
For $a, b \ge 2$:
$$
a + b \le a \cdot b
$$
Proof: $a \cdot b - a - b = (a - 1)(b - 1) - 1 \ge (1)(1) - 1 = 0$.

### 2. Recurrence Relation:
$$
ans(n) = \begin{cases} 0 & \text{if } n = 1 \\ \min_{d \mid n, d > 1} (d + ans(n / d)) & \text{if } n > 1 \end{cases}
$$

> **Arithmetic Additivity Invariant.** The minimum keystroke function $\kappa: \mathbb{N} \to \mathbb{N}_0$ is completely additive over the multiplicative semigroup of positive integers, satisfying $\kappa(a \cdot b) = \kappa(a) + \kappa(b)$ with $\kappa(p) = p$ for prime $p$.

---

## 3. Step-by-Step Worked Execution

We trace $n = 12$:

---

### Step 1: Trial Division by Smallest Primes
- $n = 12$.
- $12 \pmod 2 == 0 \implies$ factor 2. $n \leftarrow 6$, ops $= 2$.
- $6 \pmod 2 == 0 \implies$ factor 2. $n \leftarrow 3$, ops $= 2 + 2 = 4$.
- $3 \pmod 3 == 0 \implies$ factor 3. $n \leftarrow 1$, ops $= 4 + 3 = 7$.

---

### Step 2: Sum
$$
2 + 2 + 3 = \mathbf{7}
$$

---

## 4. Complete Execution Trace

| Step | Current Quotient $n$ | Extracted Factor $p$ | Action Sequence | Operations Added | Cumulative Steps |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | $12$ | $2$ | `Copy All`, `Paste` | $2$ | $2$ |
| $2$ | $6$ | $2$ | `Copy All`, `Paste` | $2$ | $4$ |
| $3$ | $3$ | $3$ | `Copy All`, `Paste`, `Paste` | $3$ | **`7`** |
| **End** | $1$ | — | Target reached | — | **`7`** |

---

## 5. Boundary Cases & Failure Modes

- **$n = 1$:** 0 operations (already at 1).
- **$n$ is Prime ($n = 7$):** Single factor $7 \implies 7$ operations.
- **Large Prime ($n = 997$):** Returns $997$.
- **Powers of Two ($n = 16$):** $2 + 2 + 2 + 2 = 8$.

---

## 6. Traps & Common Anti-Patterns

- **Searching Beyond $\sqrt{n}$ on Factoring:** When $n$ has no prime factors $\le \sqrt{n}$, $n$ itself is prime and can be added directly.
- **Off-by-One Base Case ($n = 1$):** Returning 1 instead of 0 fails because no copy or paste is needed when target is already 1.
- **Attempting BFS Simulation:** A breadth-first search simulating screen and clipboard states explores an unnecessarily large state space, whereas prime factorization solves it in $O(\sqrt{n})$ time.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Trial division runs up to $i \le \sqrt{n}$.
  - In each step where $n \pmod i == 0$, $n$ is divided by $i$.
  - Total Time: $\mathcal{O}(\sqrt{n})$. For $n = 1000$, $\sqrt{n} \approx 31$ steps, completing in $< 0.1$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ auxiliary space (only a few integer variables).
