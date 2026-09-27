# Guided Example: Self Dividing Numbers

We trace the step-by-step arithmetic digit extraction ($d = y \pmod{10}$), zero-digit disqualification ($d == 0 \implies \text{false}$), individual digit divisibility evaluation ($x \pmod d \ne 0 \implies \text{false}$), base-10 right-shift reduction ($y \leftarrow \lfloor y / 10 \rfloor$), range iteration ($x \in [left, right]$), and valid self-dividing sequence compilation on representative integer intervals:

- **Input:** $left = 1, \quad right = 22$
- **Required output:**
  $$
  [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
  $$
  - Self-dividing criteria:
    - An integer $x$ is **self-dividing** if and only if $x$ is divisible by **every single digit** it contains:
      $$
      \forall d \in \text{digits}(x): \quad d \ne 0 \ \land \ x \equiv 0 \pmod d
      $$
    - Crucial constraint: A self-dividing number **cannot contain the digit 0** (division by zero is undefined).
    - Collect all self-dividing numbers in the closed interval $[left, right]$ in ascending order.
    - For $[1, 22]$:
      - Numbers $1 \dots 9$: Every non-zero single-digit number trivially divides itself ($x \pmod x = 0$). All 9 are valid.
      - $10$: Contains digit $0 \implies$ invalid.
      - $11$: Digits are $\{1\}$; $11 \pmod 1 = 0 \implies$ valid.
      - $12$: $12 \pmod 1 = 0$ and $12 \pmod 2 = 0 \implies$ valid.
      - $13$: $13 \pmod 3 = 1 \ne 0 \implies$ invalid.
      - $14$: $14 \pmod 4 = 2 \ne 0 \implies$ invalid.
      - $15$: $15 \pmod 1 = 0$ and $15 \pmod 5 = 0 \implies$ valid.
      - $16 \dots 21$: Fail divisibility on at least one digit.
      - $22$: $22 \pmod 2 = 0 \implies$ valid.
- **Digit Extraction & Arithmetic Predicate Invariant:**
  - **Base-10 Arithmetic Decomposition:**
    - To inspect all digits of a number $x$ without string conversion:
      1. Initialize a working copy $y = x$.
      2. While $y > 0$:
         - Isolate the least significant decimal digit:
           $$
           d = y \pmod{10}
           $$
         - **Zero Trap Check:** If $d == 0$, $x$ is disqualified immediately:
           $$
           \text{return false}
           $$
         - **Divisibility Check:** If $x$ is not evenly divisible by $d$:
           $$
           x \pmod d \ne 0 \implies \text{return false}
           $$
         - Truncate the evaluated digit via integer division:
           $$
           y \leftarrow \lfloor y / 10 \rfloor
           $$
      3. If all digits are exhausted and all tests pass, $x$ is self-dividing.
  - **Linear Range Filter:**
    - Test each candidate $x \in [left, right]$ independently.
    - Yields an ordered list in natural sorted order.
- **Step-by-Step Worked Execution Trace on Range $[1, 22]$:**
  - **Single-Digit Numbers ($x \in [1, 9]$):**
    - For each $x \in [1, 9]$: $d = x$, $d \ne 0$, and $x \pmod x = 0$.
    - All 9 numbers pass: $[1, 2, 3, 4, 5, 6, 7, 8, 9]$.
  - **Testing $x = 10$:**
    - $y = 10 \implies d = 10 \pmod{10} = \mathbf{0}$.
    - Zero digit encountered! Disqualified immediately.
  - **Testing $x = 11$:**
    - $y = 11 \implies d = 1$. $11 \pmod 1 = 0$. $y \leftarrow 1$.
    - $y = 1 \implies d = 1$. $11 \pmod 1 = 0$. $y \leftarrow 0$.
    - All digits valid $\implies \mathbf{Retain\ 11}$.
  - **Testing $x = 12$:**
    - $y = 12 \implies d = 2$. $12 \pmod 2 = 0$ (Pass). $y \leftarrow 1$.
    - $y = 1 \implies d = 1$. $12 \pmod 1 = 0$ (Pass). $y \leftarrow 0$.
    - All digits valid $\implies \mathbf{Retain\ 12}$.
  - **Testing $x = 13$:**
    - $y = 13 \implies d = 3$. $13 \pmod 3 = 1 \ne 0 \implies \mathbf{Failed!}$
    - Discarded.
  - **Testing $x = 14$:**
    - $y = 14 \implies d = 4$. $14 \pmod 4 = 2 \ne 0 \implies \mathbf{Failed!}$
    - Discarded.
  - **Testing $x = 15$:**
    - $y = 15 \implies d = 5$. $15 \pmod 5 = 0$ (Pass). $y \leftarrow 1$.
    - $y = 1 \implies d = 1$. $15 \pmod 1 = 0$ (Pass). $y \leftarrow 0$.
    - All digits valid $\implies \mathbf{Retain\ 15}$.
  - **Testing $x = 16 \dots 21$:**
    - $16 \pmod 6 = 4 \ne 0 \implies$ Failed.
    - $17 \pmod 7 = 3 \ne 0 \implies$ Failed.
    - $18 \pmod 8 = 2 \ne 0 \implies$ Failed.
    - $19 \pmod 9 = 1 \ne 0 \implies$ Failed.
    - $20$: contains 0 $\implies$ Disqualified.
    - $21 \pmod 2 = 1 \ne 0 \implies$ Failed.
  - **Testing $x = 22$:**
    - $y = 22 \implies d = 2$. $22 \pmod 2 = 0$.
    - $y = 2 \implies d = 2$. $22 \pmod 2 = 0$.
    - All digits valid $\implies \mathbf{Retain\ 22}$.
  - **Final Collected Output:**
    $$
    ans = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    $$
- **Larger Three-Digit Number ($x = 128$):**
  - $d = 8$: $128 \pmod 8 = 0$ (Pass).
  - $d = 2$: $128 \pmod 2 = 0$ (Pass).
  - $d = 1$: $128 \pmod 1 = 0$ (Pass).
  - 128 is valid.
- **Interval with No Valid Numbers ($left = 19, right = 21$):**
  - 19, 20, 21 all fail.
  - Returns empty list `[]`.

This instance demonstrates modular arithmetic digit extraction and composite integer divisibility filtering, mathematically proves why zero-digit exclusion guarantees well-defined congruence relations, and derives $O((R - L) \log_{10} R)$ runtime and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given range $[left, right]$:
Find all **self-dividing numbers** (divisible by every digit they contain).
No self-dividing number may contain the digit 0.

```text
Check range [1, 22]:
  1..9: all valid (single digits divide themselves)
  10: has digit 0 -> INVALID
  11: 11 % 1 == 0 -> VALID
  12: 12 % 2 == 0 and 12 % 1 == 0 -> VALID
  13: 13 % 3 != 0 -> INVALID
  14: 14 % 4 != 0 -> INVALID
  15: 15 % 5 == 0 and 15 % 1 == 0 -> VALID
  16..21: all fail on at least one digit
  22: 22 % 2 == 0 -> VALID

Result: [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22 ]
```

### The Invariant of Digit Extraction
- While $y > 0$: extract $d = y \pmod{10}$, test $d \ne 0$ and $x \pmod d == 0$, then shift $y //= 10$.
- Pure arithmetic runs significantly faster than string conversions and avoids memory allocations.

---

## 2. Conceptual Foundation & Invariants

### 1. The Divisibility Predicate:
$$
\text{check}(x) \iff \forall d \in \text{digits}(x): \quad d \ne 0 \ \land \ (x \bmod d == 0)
$$

### 2. Modulo-Division Loop:
$$
y = x; \quad \text{while } y > 0: \quad d = y \bmod 10; \quad \text{if } (d == 0 \lor x \bmod d \ne 0) \implies \mathbf{False}; \quad y \leftarrow \lfloor y / 10 \rfloor
$$

> **Decimal Factorization Invariant.** An integer $n \in \mathbb{N}$ is self-dividing if and only if its prime valuation satisfies $v_p(n) \ge \max_{d \in \mathcal{D}_{10}(n)} v_p(d)$ for all primes $p$, where $\mathcal{D}_{10}(n) \subset \{1, \dots, 9\}$ is the non-zero decimal digit set.

---

## 3. Step-by-Step Worked Execution

We trace key numbers in $[1, 22]$:

---

### Step 1: $1 \dots 9$
- All pass.

---

### Step 2: 10
- $10 \pmod{10} = 0 \implies$ Reject.

---

### Step 3: 11, 12
- 11: $11 \% 1 == 0 \implies$ Keep.
- 12: $12 \% 2 == 0, 12 \% 1 == 0 \implies$ Keep.

---

### Step 4: 15
- 15: $15 \% 5 == 0, 15 \% 1 == 0 \implies$ Keep.

---

### Step 5: 22
- 22: $22 \% 2 == 0 \implies$ Keep.

---

### Step 6: Output
$$
[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
$$

---

## 4. Complete Execution Trace

| Number $x$ | Digits Tested | Contains 0? | Digit Divisibility Evaluated | Decision | Added to Result? |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $1 \dots 9$ | $\{x\}$ | No | $x \pmod x == 0$ | Pass | Yes ($1 \dots 9$) |
| $10$ | $\{0, 1\}$ | **Yes ($d=0$)**| Division by zero forbidden | Fail | No |
| $11$ | $\{1, 1\}$ | No | $11 \pmod 1 = 0$ | Pass | Yes ($11$) |
| $12$ | $\{2, 1\}$ | No | $12 \pmod 2 = 0, 12 \pmod 1 = 0$ | Pass | Yes ($12$) |
| $13$ | $\{3, 1\}$ | No | $13 \pmod 3 = 1 \ne 0$ | Fail | No |
| $15$ | $\{5, 1\}$ | No | $15 \pmod 5 = 0, 15 \pmod 1 = 0$ | Pass | Yes ($15$) |
| $20$ | $\{0, 2\}$ | **Yes ($d=0$)**| Division by zero forbidden | Fail | No |
| **$22$** | **$\{2, 2\}$** | **No** | **$22 \pmod 2 = 0$** | **Pass** | **Yes ($22$)** |

---

## 5. Boundary Cases & Failure Modes

- **Single Number Range ($left = right$):** Evaluates single number, returns `[left]` or `[]`.
- **Numbers Containing 0 ($10, 20, 105$):** Caught immediately by $y \pmod{10} == 0$.
- **Maximum Bound ($right = 10^4$):** At most 4 digits per number $\implies \le 4$ operations per candidate.
- **Repeated Digits ($11, 222$):** Both digits divide the number evenly.

---

## 6. Traps & Common Anti-Patterns

- **Division by Zero Exception:** Forgetting `if d == 0: return False` before computing `x % d` throws a ZeroDivisionError in any runtime.
- **String Conversion Overhead:** Converting numbers to strings `str(x)` and iterating through characters is $5\times$ to $10\times$ slower than simple modulo-division loops.
- **Modifying the Original $x$:** Modifying $x$ directly in the while loop prevents computing `x % d` against the original number. Always use a copy $y = x$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Evaluates each number in the interval $[left, right]$: $N = right - left + 1$.
  - Each number has at most $\lfloor \log_{10}(right) \rfloor + 1$ digits (at most 4 digits for $right \le 10^4$).
  - Total Time: strictly $\mathcal{O}((right - left + 1) \log_{10}(right))$. Completes in $< 3$ ms for range size $10^4$.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space beyond the output array.
