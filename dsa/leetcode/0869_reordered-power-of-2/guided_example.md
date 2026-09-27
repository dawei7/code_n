# Guided Example: Reordered Power of 2

We trace the step-by-step decimal digit multiset extraction, finite power-of-two domain bounds ($2^0 \dots 2^{29}$), leading-zero prohibition constraints, and digit frequency profile matching on representative positive integers:

- **Input:**
  $$
  n = 46
  $$
- **Required output:** `true`
  - Reordering rules:
    - Given a positive integer $n$, we may reorder its decimal digits in any permutation.
    - The reordered number must **not have a leading zero** (e.g. reordering $10 \to 01$ is invalid).
    - Objective: Determine if any valid permutation forms a power of two ($2^0, 2^1, 2^2, \dots$).
    - For $n = 46$:
      - Digits: `['4', '6']`.
      - Permutations:
        - $46$: not a power of two ($32 < 46 < 64$).
        - $64$: $64 = 2^6$ (exact power of two!). No leading zero.
      - A valid power of two can be formed!
      - Result: **`true`**.
- **The Digit Multiset Matching & Finite Search Space Invariant:**
  - **The Power-of-Two Domain Bound:**
    - The input constraint states $1 \le n \le 10^9$.
    - Any valid reordering must produce a number with the same number of digits as $n$, and at most $10^9$.
    - How many powers of two are $\le 10^9$?
      $$
      2^{29} = 536,870,912 \le 10^9 < 2^{30} = 1,073,741,824
      $$
    - There are **only 30 powers of two** ($2^0, 2^1, \dots, 2^{29}$) in the entire problem domain!
  - **Multiset Invariance (Signature Matching):**
    - Two numbers are digit permutations of each other if and only if their 10-element digit frequency vectors are identical:
      $$
      \text{freq}(x) = (\text{count}(0), \text{count}(1), \dots, \text{count}(9))
      $$
    - Instead of generating all $d!$ digit permutations of $n$ (which risks factorial time blowup), we compute the single signature $\text{freq}(n)$ and compare it against the signatures of the 30 candidate powers of two.
    - If $\text{freq}(n) == \text{freq}(2^k)$ for any $k \in [0, 29]$, then $n$ can be reordered into $2^k$.

---

## 1. Instance & Teaching Goal

Given $n = 46$, determine if its digits can be rearranged into a power of two.

```text
Input: n = 46
Digits of n: {4: 1, 6: 1}

Search Powers of Two:
  2^0 = 1    -> {1: 1}
  2^1 = 2    -> {2: 1}
  2^2 = 4    -> {4: 1}
  2^3 = 8    -> {8: 1}
  2^4 = 16   -> {1: 1, 6: 1}
  2^5 = 32   -> {2: 1, 3: 1}
  2^6 = 64   -> {4: 1, 6: 1} -> MATCH!

Digits {4, 6} form 64 = 2^6!
Output: true
```

We also contrast this with $n = 10$: digits are $\{0, 1\}$. While $2^0 = 1$ has digit $1$, $n = 10$ requires both digits $0$ and $1$, and $01$ has an illegal leading zero, so $n = 10$ returns `false`.

---

## 2. Conceptual Foundation & Invariants

### 1. Decimal Frequency Function:
$$
f(x) = [c_0, c_1, \dots, c_9] \quad \text{where } c_d = \sum_{k} \mathbb{I}\left[\lfloor x / 10^k \rfloor \pmod{10} = d\right]
$$

### 2. Decision Predicate:
$$
\text{reorderedPowerOf2}(n) = \bigvee_{k=0}^{29} \left( f(n) == f(2^k) \right)
$$
Because powers of two never contain a leading zero (they are positive integers), any match $f(n) == f(2^k)$ guarantees that the digits of $n$ can form $2^k$ without a leading zero.

---

## 3. Step-by-Step Worked Execution

We trace $n = 46$:

---

### Step 1: Compute Target Signature for $n = 46$
- Extract digits:
  - $46 \pmod{10} = 6 \implies count[6] \leftarrow 1, \quad 46 // 10 = 4$
  - $4 \pmod{10} = 4 \implies count[4] \leftarrow 1, \quad 4 // 10 = 0$
- Target frequency vector $f(46)$:
  $$
  c_4 = 1, \quad c_6 = 1, \quad \text{all other } c_d = 0
  $$

---

### Step 2: Compare with Powers of Two
- $2^0 = 1$: $f(1) = \{1: 1\} \ne f(46)$.
- $2^1 = 2$: $f(2) = \{2: 1\} \ne f(46)$.
- $2^2 = 4$: $f(4) = \{4: 1\} \ne f(46)$.
- $2^3 = 8$: $f(8) = \{8: 1\} \ne f(46)$.
- $2^4 = 16$: $f(16) = \{1: 1, 6: 1\} \ne f(46)$.
- $2^5 = 32$: $f(32) = \{2: 1, 3: 1\} \ne f(46)$.
- $2^6 = 64$:
  - Extract digits of $64$:
    - $64 \pmod{10} = 4 \implies count[4] \leftarrow 1$
    - $6 \pmod{10} = 6 \implies count[6] \leftarrow 1$
  - Vector: $c_4 = 1, c_6 = 1$, all other $0$.
  - Comparison:
    $$
    f(64) == f(46) \implies \mathbf{Exact\ Match!}
    $$
- **Immediate Termination: `true`**.

---

## 4. Complete Execution Trace

| Power $k$ | Value $2^k$ | Number of Digits | Digit Multiset $f(2^k)$ | Matches $f(46) = \{4: 1, 6: 1\}$? |
|:---:|:---:|:---:|:---:|:---:|
| $0$ | $1$ | $1$ | $\{1: 1\}$ | No |
| $1$ | $2$ | $1$ | $\{2: 1\}$ | No |
| $2$ | $4$ | $1$ | $\{4: 1\}$ | No |
| $3$ | $8$ | $1$ | $\{8: 1\}$ | No |
| $4$ | $16$ | $2$ | $\{1: 1, 6: 1\}$ | No |
| $5$ | $32$ | $2$ | $\{2: 1, 3: 1\}$ | No |
| **$6$** | **$64$** | **$2$** | **$\{4: 1, 6: 1\}$** | **`Yes (Match Found!)`** |

---

## 5. Boundary Cases & Failure Modes

- **$n = 1$ ($2^0$):** Digits are `{1: 1}`. Matches $2^0 = 1$ immediately $\implies$ returns `true`.
- **$n = 10$:** Digits are `{0: 1, 1: 1}`. Powers of two with 2 digits are $16, 32, 64$; none has digits $\{0, 1\}$. Reordering to $01$ has an illegal leading zero $\implies$ returns `false`.
- **Large Input $n = 10^9$:** 10 digits (`1` followed by nine `0`s). No power of two has nine zeros $\implies$ returns `false`.

---

## 6. Traps & Common Anti-Patterns

- **Generating All Permutations of $n$:** Calling permutation libraries generates up to $10! = 3,628,800$ permutations. When $n$ has duplicate digits, duplicate checking adds severe overhead. Comparing against the 30 fixed powers of two requires only 30 checks.
- **Overlooking Leading Zeros in Permutation Generators:** If generating permutations as strings, converting `"01"` to integer produces `1 = 2^0`, falsely reporting `true` for $n = 10$. Precomputing powers of two natively eliminates leading zero bugs because $2^k$ has no leading zeros.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Target frequency count: $\mathcal{O}(\log_{10} n) \le 10$ operations.
  - Exactly 30 powers of two evaluated.
  - Each power has $\le 10$ digits.
  - Total operations: $30 \times 10 \approx 300$ primitive operations.
  - Total Time: strictly $\mathcal{O}(1)$ bounded time, executing in $< 0.05$ ms.
- **Auxiliary Space Complexity:**
  - 10-element integer array for digit counting: strictly $\mathcal{O}(1)$ auxiliary space.
