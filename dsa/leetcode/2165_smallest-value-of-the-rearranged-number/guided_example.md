# Guided Example: Smallest Value of the Rearranged Number

We analyze and execute the sign-conditioned digit rearrangement algorithm on a representative problem instance, establishing how the algebraic duality between positive minimization and negative maximization guides leading-zero handling and sorting directions.

- **Input:** `num = 310`
- **Output:** `103`

This instance illustrates sign bifurcation, ascending digit sorting, non-zero pivot extraction to prevent forbidden leading zeros, and numerical reconstruction.

---

## 1. Problem Overview & Representative Instance

Given an integer `num` within $[-10^{15}, 10^{15}]$, we must rearrange all its decimal digits to achieve the **algebraically smallest** possible numeric value. The rearrangement must obey two core constraints:
1. **Sign Invariance:** Positive numbers must remain positive, negative numbers must remain negative, and zero remains zero. The negative sign is a fixed algebraic prefix, not a moveable character.
2. **No Leading Zero:** The rearranged integer representation cannot begin with the digit `'0'`, unless the value itself is $0$.

In our representative instance:
- `num = 310`.
- The number is positive ($310 > 0$).
- Digits present: $\{0, 1, 3\}$.

If we strictly sorted digits ascending, we would obtain `"013"`, which violates the leading-zero rule. We must find the smallest valid positive arrangement.

---

## 2. Mathematical & Algorithmic Principles

### Sign Duality: Minimization vs. Maximization

Let $D$ be the multiset of decimal digits of $|num|$:
1. **Positive Case ($num > 0$):**
   To minimize the value of a positive number, we want the most significant digits (leftmost place values) to be as small as possible:
   - Sort the digits of $D$ in **ascending** order: $d_0 \le d_1 \le d_2 \le \dots \le d_{L-1}$.
   - If $d_0 = 0$, we cannot use $0$ as the leading digit. We find the smallest strictly positive digit $d_k > 0$ (the first non-zero digit) and swap it to position $0$. The remaining digits remain sorted in ascending order.
2. **Negative Case ($num < 0$):**
   Because $-A \le -B \iff A \ge B$, minimizing a negative number is equivalent to **maximizing its positive magnitude**:
   - Sort the digits of $D$ in **descending** order: $d_0 \ge d_1 \ge d_2 \ge \dots \ge d_{L-1}$.
   - Because $num \ne 0$, at least one digit is strictly positive. The largest digit $d_0 \ge 1$ is naturally non-zero, so a leading zero is mathematically impossible.
   - Prepend the negative sign: $-\text{integer}(d_0 d_1 \dots d_{L-1})$.
3. **Zero Case ($num = 0$):**
   Zero contains only the digit `'0'`; return $0$ immediately.

| Sign Regime | Target Objective on Magnitude $|num|$ | Sorting Order | Leading Zero Policy |
|---|---|---|---|
| Positive ($num > 0$) | Minimize magnitude | Ascending | Swap first non-zero digit to index $0$ |
| Negative ($num < 0$) | Maximize magnitude | Descending | Inherently non-zero leading digit |
| Zero ($num = 0$) | Identity | None | Preserved as $0$ |

---

## 3. Step-by-Step Walkthrough with Intermediate State

We trace `num = 310`.

```
Input: num = 310  (Positive)
Extracted digits: ['3', '1', '0']

Step 1: Sort ascending   => ['0', '1', '3']
Step 2: Check leading 0  => First non-zero is '1' at index 1
Step 3: Swap to front    => ['1', '0', '3']
Step 4: Parse to integer => 103
```

### Step 1: Sign Classification
- Evaluate: $310 > 0$.
- Regimen: Positive magnitude minimization.
- Target sorting direction: Ascending.

### Step 2: Extract and Sort Digits
- Digits of $|310|$: `['3', '1', '0']`.
- Sort characters ascending:
  $$D = ['0', '1', '3']$$
- Check index $0$: $D[0] = \text{'0'}$.
- Leading zero detected: illegal for standard decimal representations.

### Step 3: Locate Smallest Non-Zero Pivot
- Search for the first index $k > 0$ such that $D[k] \ne \text{'0'}$:
  - $D[1] = \text{'1'} \ne \text{'0'}$. Found at $k = 1$.
- Swap $D[0]$ and $D[1]$:
  - Before swap: `['0', '1', '3']`.
  - After swap: `['1', '0', '3']`.

### Step 4: Reconstruct Final Integer
- String representation: `"103"`.
- Convert to signed 64-bit integer: $103$.
- Output: $103$.

---

## 4. Comprehensive State Trace

The table below contrasts the execution across different sign profiles and digit configurations:

| Input `num` | Sign Condition | Extracted Digits | Sorted Digits | Pivot Swap Applied | Final Digit Sequence | Evaluated Return Value |
|---|---|---|---|---|---|---|
| **$310$** | **Positive** | `['3', '1', '0']` | `['0', '1', '3']` | Swap index 0 and 1 | `['1', '0', '3']` | **$103$** |
| $-7605$ | Negative | `['7', '6', '0', '5']` | `['7', '6', '5', '0']` | None (already descending) | `['7', '6', '5', '0']` | **$-7650$** |
| $0$ | Zero | `['0']` | `['0']` | None | `['0']` | **$0$** |
| $4009$ | Positive | `['4', '0', '0', '9']` | `['0', '0', '4', '9']` | Swap index 0 and 2 (`'4'`) | `['4', '0', '0', '9']` | **$4009$** |

### Mathematical Optimality Verification for $310$

All possible valid non-leading-zero permutations of $\{0, 1, 3\}$:
- $103$: valid, value $= 103$.
- $130$: valid, value $= 130$.
- $301$: valid, value $= 301$.
- $310$: valid, value $= 310$.

The minimum valid positive number is strictly $103$.

---

## 5. Algorithmic Correctness & Soundness

### Lexicographical Minimization with Leading Constraint
Let $S$ be a multiset of digits containing at least one non-zero digit.
1. Any valid number has representation $x = d_0 d_1 \dots d_{L-1}$ with $d_0 > 0$.
2. To minimize $\sum_{j=0}^{L-1} d_j \cdot 10^{L-1-j}$, we must choose the smallest possible non-zero digit for $d_0$.
3. Once $d_0$ is fixed to the minimum non-zero element, the remaining digits $S \setminus \{d_0\}$ have unconstrained positional choices.
4. By the rearrangement inequality, the remaining digits must be ordered in non-decreasing order $d_1 \le d_2 \le \dots \le d_{L-1}$ (which naturally places all zeros immediately after $d_0$).
5. Swapping the first non-zero digit with $d_0$ in an ascending sorted array achieves this exact sequence, proving strict global optimality.

---

## 6. Edge Cases & Anti-Patterns

### Edge Cases
1. **Zero (`num = 0`):** Has no sign and only one digit; returns $0$.
2. **Multiple Zeros in Positive Number:** E.g., `num = 4009`. Sorted: `0, 0, 4, 9`. First non-zero is $4$ at index $2$. Swapping with index $0$ yields `4, 0, 0, 9` $\implies 4009$.
3. **Negative Number with Zeros:** E.g., `num = -7605`. Descending sort puts zeros at the end: `7650`. With negative sign: $-7650$, which is the most negative possible value.
4. **All Digits Identical:** E.g., `num = -555` $\to -555$; `num = 777` $\to 777$.

### Common Anti-Patterns
- **Ascending Sort for Negative Numbers:** Sorting digits of a negative number ascending yields $-567$ instead of $-765$. Since $-765 < -567$, descending magnitude sort is required for negative numbers.
- **Dropping Leading Zeros as Integers:** Parsing `"013"` as integer $13$ drops the `'0'` digit, failing the rule that every digit occurrence must be used.
- **Permutation Generation ($O(L!)$):** Generating all permutations is unnecessary when string sorting runs in $O(L \log L)$ for length $L \le 16$.

---

## 7. Complexity Analysis

### Time Complexity
- The number of decimal digits $L$ for $|num| \le 10^{15}$ is at most $16$.
- Converting integer to string of digits: $O(L)$.
- Sorting $L \le 16$ characters: $O(L \log L) \le 16 \log_2(16) \approx 64$ operations.
- Finding the first non-zero digit and swapping: $O(L)$.
- Total time complexity is strictly $O(L) = O(\log_{10} |num|)$, executing in under $1$ microsecond.

### Auxiliary Space Complexity
- Character array of length at most $16$.
- Total auxiliary space complexity is $O(L) = O(1)$ fixed memory.
