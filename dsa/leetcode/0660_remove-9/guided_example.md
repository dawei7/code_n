# Guided Example: Remove 9

We trace the step-by-step digit alphabet exclusion mapping (omitting `'9'` $\implies$ base-$9$ positional numeration), radix-$9$ change-of-base division algorithm ($n = 9q + r$), positional place-value assembly ($\sum d_i \cdot 10^i$), and $n$-th valid integer synthesis on representative rank queries:

- **Input:** $n = 9$
- **Required output:** `10`
  - Sequence generation rule:
    - Count positive integers starting from $1$, skipping any number that contains the digit `'9'`:
      $$
      1, \; 2, \; 3, \; 4, \; 5, \; 6, \; 7, \; 8, \; \mathbf{10}, \; 11, \; 12, \dots
      $$
    - Notice: $9$ is skipped, so the $9$-th integer in this sequence is **$10$**!
    - The $10$-th integer is $11$, and so on.
    - Objective: Find the $n$-th integer in this filtered sequence.
- **Base-9 Radix Isomorphism Invariant:**
  - **The Digit Restriction:**
    - In standard decimal (base 10), there are 10 distinct digit glyphs:
      $$
      \Sigma_{10} = \{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}
      $$
    - Completely removing the digit `'9'` restricts our allowable glyph alphabet to exactly 9 symbols:
      $$
      \Sigma_9 = \{0, 1, 2, 3, 4, 5, 6, 7, 8\}
      $$
  - **Natural Bijective Radix Equivalence:**
    - A number system with 9 digits $\{0 \dots 8\}$ where numbers count upwards $0, 1, 2, \dots, 8, 10, 11 \dots$ is precisely the **Base-9 (nonary) numeral system**!
    - In base 9:
      - Rank 1 is $(1)_9 = 1$
      - Rank 8 is $(8)_9 = 8$
      - Rank 9 is $1 \times 9^1 + 0 \times 9^0 = (10)_9$ (printed as `10`)
      - Rank 10 is $1 \times 9^1 + 1 \times 9^0 = (11)_9$ (printed as `11`)
      - Rank 18 is $2 \times 9^1 + 0 \times 9^0 = (20)_9$ (printed as `20`)
    - **Fundamental Insight:** The $n$-th integer that contains no digit 9 is simply the **number $n$ converted into base 9**, and then read as if it were a decimal number!
- **Step-by-Step Worked Execution Trace on $n = 9$:**
  - Convert $n = 9$ to base 9 via successive division:
  - **Iteration 1:**
    - Divide $n$ by $9$:
      $$
      n = 9 \implies \lfloor 9 / 9 \rfloor = 1, \quad 9 \pmod 9 = \mathbf{0}
      $$
    - Lowest significant digit: $d_0 = \mathbf{0}$.
    - Quotent remaining: $n = 1$.
  - **Iteration 2:**
    - Divide $n = 1$ by $9$:
      $$
      \lfloor 1 / 9 \rfloor = 0, \quad 1 \pmod 9 = \mathbf{1}
      $$
    - Next digit: $d_1 = \mathbf{1}$.
    - Quotient is now $0$ (Halts).
  - **Assemble Base-9 Digits into Decimal Place Values:**
    $$
    result = d_1 \times 10^1 + d_0 \times 10^0 = 1 \times 10 + 0 \times 1 = \mathbf{10}
    $$
    - Output: **`10`**.
- **Trace for Rank $n = 10$:**
  - $10 \pmod 9 = 1$, quotient $10 // 9 = 1$.
  - $1 \pmod 9 = 1$, quotient $1 // 9 = 0$.
  - Digits: $d_0 = 1, d_1 = 1 \implies \mathbf{11}$.
  - The 10th number without a 9 is indeed 11!
- **Trace for Rank $n = 80$:**
  - $80 \pmod 9 = 8$, quotient $80 // 9 = 8$.
  - $8 \pmod 9 = 8$, quotient $8 // 9 = 0$.
  - Digits: $d_0 = 8, d_1 = 8 \implies \mathbf{88}$.
- **Trace for Rank $n = 81$ ($9^2$):**
  - $81 \pmod 9 = 0$, $81 // 9 = 9$.
  - $9 \pmod 9 = 0$, $9 // 9 = 1$.
  - $1 \pmod 9 = 1$, $1 // 9 = 0$.
  - Digits: $d_0 = 0, d_1 = 0, d_2 = 1 \implies \mathbf{100}$.
  - Check: Numbers from 1 to 100 contain exactly 19 numbers with digit 9 ($9, 19, \dots 89, 90 \dots 99$). $100 - 19 = 81$! Rank 81 is indeed 100!

This instance demonstrates radix representation isomorphisms between restricted alphabet languages and positional base systems, mathematically proves why decimal numeral exclusion maps bijectively onto nonary positional coefficients, and derives $O(\log_9 n)$ execution time and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an integer $n$:
Count positive integers omitting any number containing digit `'9'`.
Find the **$n$-th integer** in this sequence.

```text
Sequence without digit '9':
  Rank 1 -> 1
  Rank 2 -> 2
  ...
  Rank 8 -> 8
  Rank 9 -> 10  (skips 9!)
  Rank 10 -> 11

Observation:
  These are exactly numbers written in Base 9!
  9 in base 10 = (10)_9
  10 in base 10 = (11)_9
  81 in base 10 = (100)_9
```

### The Invariant of the Radix Isomorphism
- Removing digit `'9'` leaves 9 available symbols: $0, 1, 2, 3, 4, 5, 6, 7, 8$.
- Counting without `'9'` is identical to counting in **base 9**.
- The answer is the base-9 representation of $n$ formatted as a decimal integer.

---

## 2. Conceptual Foundation & Invariants

### 1. Base-9 Expansion:
For integer $n$:
$$
n = \sum_{i=0}^k d_i \cdot 9^i \quad \text{where } d_i \in \{0, 1, \dots, 8\}
$$

### 2. Decimal Projection:
$$
\text{Answer} = \sum_{i=0}^k d_i \cdot 10^i
$$

> **Positional Radix Homomorphism Invariant.** The canonical digit projection $\pi: \mathbb{Z}_9 \to \Sigma_9$ is a strictly order-preserving bijective embedding of $\mathbb{N}$ into the decimal integers excluding the symbol `'9'`.

---

## 3. Step-by-Step Worked Execution

We trace $n = 9$:

---

### Step 1: Divide by 9
- $9 \div 9 = 1$, remainder $0$.
- Place $10^0$: digit 0.

---

### Step 2: Divide by 9
- $1 \div 9 = 0$, remainder $1$.
- Place $10^1$: digit 1.

---

### Step 3: Combine Place Values
$$
result = 1 \times 10 + 0 = \mathbf{10}
$$

---

## 4. Complete Execution Trace

| Division Step | Current $n$ | Remainder $d = n \pmod 9$ | Next $n = n // 9$ | Place Value Multiplier | Contribution to Output | Running Result |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | $9$ | $0$ | $1$ | $1$ | $0 \times 1 = 0$ | $0$ |
| $2$ | $1$ | $1$ | $0$ | $10$ | $1 \times 10 = 10$ | **`10`** |
| **Halt** | $0$ | — | — | — | Target reached | **`10`** |

---

## 5. Boundary Cases & Failure Modes

- **$n \le 8$:** Remainder is $n$, quotient is $0 \implies$ returns $n$ unchanged.
- **Power of 9 ($n = 9, 81, 729$):** Produces round decimal-looking numbers $10, 100, 1000$.
- **Large Input ($n = 10^9$):** Base-9 representation has $\approx \log_9(10^9) \approx 10$ digits; fits easily within 64-bit integer limits without overflow.

---

## 6. Traps & Common Anti-Patterns

- **Brute Force Counting ($O(N)$ with string search):** Iterating $1, 2, 3 \dots$ and checking `'9' in str(i)` times out catastrophically for $n = 10^9$.
- **Digit DP Search:** While digit DP can count valid numbers, it is unnecessarily complicated; converting $n$ directly to base 9 solves it in 10 operations.
- **Off-by-One with 0-Indexing:** The problem is 1-indexed, which aligns directly with counting positive integers in base 9.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - The loop divides $n$ by 9 at each step.
  - Number of iterations: $\lfloor \log_9(n) \rfloor + 1$.
  - For $n = 10^9$, at most $10$ loop iterations.
  - Total Time: strictly $\mathcal{O}(\log_9 n)$. Executes in $< 0.01$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ auxiliary space (only a few integer scalar variables).
