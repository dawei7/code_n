# Guided Example: Count Numbers with Unique Digits

We trace the step-by-step digit dynamic programming memoization (`@cache`), bitmask digit availability tracking (`mask`), leading zero normalization (`lead`), and combinatorial counting ($0 \le x < 10^n$) on representative integer power instances:

- **Input:** $n = 2$
- **Required output:** $91$
  - Numbers in range $0 \le x < 10^2 = 100$:
    - 1-digit numbers ($0 \dots 9$): all $10$ have unique digits $\implies 10$
    - 2-digit numbers ($10 \dots 99$):
      - First digit $d_1 \in [1 \dots 9]$: $9$ choices (cannot be $0$)
      - Second digit $d_2 \in [0 \dots 9] \setminus \{d_1\}$: $9$ choices
      - Total 2-digit unique numbers: $9 \times 9 = 81$
    - Overall unique count: $10 + 81 = \mathbf{91}$
  - Non-unique numbers excluded: $11, 22, 33, 44, 55, 66, 77, 88, 99$ (9 numbers) $\implies 100 - 9 = 91$
- **Base Case $n = 0$:** $0 \le x < 1 \implies x = 0 \implies \mathbf{1}$
- **Base Case $n = 1$:** $0 \le x < 10 \implies 0 \dots 9 \implies \mathbf{10}$
- **Three Digits $n = 3$:** $91 + (9 \times 9 \times 8) = 91 + 648 = \mathbf{739}$
- **Pigeonhole Ceiling $n \ge 10$:** Any number with $> 10$ digits must repeat a digit (since only 10 distinct decimal digits exist)

This instance demonstrates digit dynamic programming with state compression, proves how leading zeros decouple prefix length from digit uniqueness constraints, and analyzes $O(n \cdot 2^{10})$ state space and $O(1)$ runtime bounds.

---

## 1. Instance & Teaching Goal

Given a non-negative integer $n = 2$:
Count all integers $x$ in the half-open interval $[0, 10^n)$ such that all digits of $x$ are strictly distinct:

```text
Interval: 0 <= x < 100

Partition by Number of Digits:
Length 1 (0 to 9):   All 10 numbers are valid: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
Length 2 (10 to 99): 10 to 99 has 90 total numbers.
                     Duplicates occur at {11, 22, 33, 44, 55, 66, 77, 88, 99} (9 numbers)
                     Valid 2-digit numbers: 90 - 9 = 81

Total Unique-Digit Numbers: 10 + 81 = 91
```

---

## 2. Conceptual Foundation & Invariants

### 1. Digit DP State Signature: `dfs(i, mask, lead)`
- `i`: Current digit position being placed, indexed from $n - 1$ down to $0$.
- `mask`: Integer bitmask in $[0, 2^{10} - 1]$ where bit $j$ is $1$ if digit $j$ has already been used.
- `lead`: Boolean flag indicating whether all preceding positions were leading zeros.

### 2. Transition Rules for Placing Digit $j \in [0 \dots 9]$:
1. **Duplicate Guard:**
   If $(mask \gg j) \ \& \ 1 == 1$: digit $j$ is already used, **skip**.
2. **Leading Zero Branch (`lead and j == 0`):**
   A leading zero does not form part of the number's actual digits. It does not occupy bit 0 in the mask:
   $$
   ans \mathrel{+}= dfs(i - 1, \; mask, \; \text{True})
   $$
3. **Active Digit Branch (`not lead or j != 0`):**
   Digit $j$ is consumed, marking bit $j$ in the mask:
   $$
   ans \mathrel{+}= dfs(i - 1, \; mask \mid (1 \ll j), \; \text{False})
   $$

### 3. Base Case:
When $i < 0$, all $n$ positions have been placed validly:
$$
\text{return } 1
$$

> **Invariant.** The bitmask `mask` records exactly the set of non-zero leading digits present in the current prefix, guaranteeing no digit is repeated.

---

## 3. Step-by-Step Worked Execution

We trace $n = 2$ starting at root call `dfs(i=1, mask=0, lead=True)`:

---

### Step 1: Evaluating Leading Zero at Position 1 ($j = 0$)
- Placed digit: $j = 0$. Since `lead` is True, this is a leading zero.
- Recurse into `dfs(i=0, mask=0, lead=True)`:
  - At position $i = 0$:
    - $j = 0$: `lead` is True $\implies dfs(-1, 0, True) = \mathbf{1}$ (Represents number $0$).
    - $j = 1 \dots 9$: `lead` becomes False $\implies dfs(-1, 1 \ll j, False) = \mathbf{1}$ each (Represents numbers $1 \dots 9$).
  - Total for 1-digit numbers: $1 + 9 = \mathbf{10}$.

---

### Step 2: Evaluating First Non-Zero Digit at Position 1 ($j \in [1 \dots 9]$)
- For each non-zero choice $j \in \{1, 2, 3, 4, 5, 6, 7, 8, 9\}$:
  - $j$ sets bit $j$: `mask` becomes $1 \ll j$, `lead` becomes False.
  - Recurse into `dfs(i=0, mask = 1 << j, lead=False)`:
    - At position $i = 0$, iterate candidates $k \in [0 \dots 9]$:
      - If $k == j$: Bit $k$ is set in `mask` $\implies$ **Skipped (Duplicate!)**.
      - For all other 9 choices of $k \in [0 \dots 9] \setminus \{j\}$:
        Bit $k$ is clear $\implies dfs(-1, \dots) = 1$.
    - Total valid second digits for each initial digit $j$: $\mathbf{9}$ choices.
- Total 2-digit numbers:
  $$
  9 \times 9 = \mathbf{81}
  $$

---

### Step 3: Total Sum Aggregation
Combine leading zero branch (1-digit numbers) and active branches (2-digit numbers):
$$
\text{Total} = 10 + 81 = \mathbf{91}
$$

---

## 4. Complete Execution Trace

```text
dfs(i=1, mask=0, lead=True)
├── j=0 (leading zero) -> dfs(0, 0, True)
│   ├── j=0 -> dfs(-1, 0, True) = 1 (number 0)
│   └── j=1..9 -> 9 branches each returning 1 (numbers 1..9)
│   Subtotal = 10
└── j=1..9 (9 choices for tens digit):
    ├── For j=1 (tens digit 1): ones digit can be {0, 2, 3, 4, 5, 6, 7, 8, 9} (9 choices)
    ├── For j=2 (tens digit 2): ones digit can be {0, 1, 3, 4, 5, 6, 7, 8, 9} (9 choices)
    └── ... (9 choices each for j=1..9)
    Subtotal = 9 * 9 = 81

Final Answer: 10 + 81 = 91
```

| Traversal Frame | Digit $j$ Placed | Leading Zero? | Updated Mask | Candidate Count at $i = 0$ | Contribution | Running Total |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Root $i = 1$ | 0 | Yes | $0$ | 10 ($0 \dots 9$) | 10 | 10 |
| Root $i = 1$ | 1 | No | $10_2$ | 9 ($0, 2 \dots 9$) | 9 | 19 |
| Root $i = 1$ | 2 | No | $100_2$ | 9 ($0, 1, 3 \dots 9$) | 9 | 28 |
| Root $i = 1$ | $3 \dots 9$ | No | $1 \ll j$ | 9 each ($7 \times 9$) | 63 | **91 (Final)** |

---

## 5. Algorithmic Correctness

**Soundness.** The check `mask >> j & 1` explicitly forbids selecting any digit already present in the active prefix, preventing duplicate digits. Differentiating leading zeros via `lead` ensures that numbers with fewer than $n$ digits (e.g. $007$ representing $7$) are not penalized for multiple leading zeros.

**Completeness.** The recursion branches over all ten possible digits $0 \dots 9$ at every position from $n - 1$ down to $0$. Since every decimal representation of an integer $< 10^n$ corresponds to an assignment of $n$ digits with optional leading zeros, all non-repeating numbers are exhaustively enumerated.

---

## 6. Traps This Instance Exposes

- **Counting Zero Twice or Omitting Zero:** The number $0$ is explicitly in the range $[0, 10^n)$ and has 1 unique digit. The leading zero path naturally counts $0$ when all digits are zero.
- **Pigeonhole Principle ($n > 10$):** Since there are only 10 distinct decimal digits ($0 \dots 9$), any number with 11 or more digits must have at least one repeated digit. For $n \ge 10$, the number of unique-digit numbers is capped at the count for $n = 10$.
- **Leading Zeros in Mask:** If a leading zero were placed in the mask, then the digit 0 could never appear later in the number (e.g. $050$ would be blocked, but $05$ would also prevent $50$ from being formed). Preserving `mask = 0` while `lead` is True avoids this bug.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n \cdot 2^{10} \cdot 10) = O(n)$, since $2^{10} = 1024$ and the alphabet size $10$ are constants. With $n \le 8$, the search explores only a few thousand states, executing in less than 1 millisecond.
- **Auxiliary Space Complexity:** $O(n \cdot 2^{10}) = O(1)$ bounded auxiliary memory for memoization table cache.