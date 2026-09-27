# Guided Example: Divide Two Integers

We trace the step-by-step binary long division (exponential doubling via bit shifts) on a representative integer division instance:

- **Input:** $\text{dividend} = 10$, $\text{divisor} = 3$
- **Required output:** $3$

This instance demonstrates sign normalization, exponential doubling using bit shifts ($\text{divisor} \ll k$), subtracting powers-of-two multiples to compute the quotient in logarithmic time, and 32-bit overflow boundary clamping.

---

## 1. Instance & Teaching Goal

Given two signed 32-bit integers $\text{dividend}$ and $\text{divisor}$, we must compute the truncated integer quotient $\lfloor \text{dividend} / \text{divisor} \rfloor$ strictly **without** using multiplication, division, or modulo operators ($*$, $/$, $\%$).

For $\text{dividend} = 10$ and $\text{divisor} = 3$:
- Naive repeated subtraction ($10 - 3 - 3 - 3 = 1$) takes $O(\text{dividend})$ time. If $\text{dividend} = 2^{31}-1$ and $\text{divisor} = 1$, naive subtraction requires over $2$ billion operations, causing a Time Limit Exceeded error.
- Binary long division doubles the divisor exponentially using bit shifts ($3 \times 2^1 = 6 \le 10$), subtracting the largest power-of-two multiple at each step. This computes the quotient in $O(\log^2(\text{dividend}))$ or $O(32) = O(1)$ bit operations.

---

## 2. Conceptual Foundation & Invariants

### 32-Bit Overflow Edge Case
The signed 32-bit integer range is $[-2^{31}, 2^{31}-1] = [-2147483648, 2147483647]$.
There is exactly one case that overflows:
$$
\frac{-2^{31}}{-1} = 2^{31} = 2147483648 > 2^{31}-1
$$
This single edge case must be clamped to $2^{31}-1 = 2147483647$.

### Binary Exponential Subtraction
Any quotient $Q$ can be decomposed into a unique sum of powers of two:
$$
Q = \sum_{k} 2^k \implies \text{dividend} = \sum_{k} (2^k \cdot \text{divisor}) + \text{remainder}
$$
1. **Sign Resolution:** The quotient is negative if and only if exactly one of $\text{dividend}$ or $\text{divisor}$ is negative:
   $$
   \text{is\_negative} = (\text{dividend} < 0) \oplus (\text{divisor} < 0)
   $$
2. **Exponential Doubling:** While $\text{current\_divisor} \ll 1 \le \text{remainder}$, double $\text{current\_divisor}$ and the power-of-two contribution.
3. **Subtraction & Accumulation:** Subtract the largest doubled divisor from $\text{remainder}$ and add the power-of-two multiple to the quotient.
4. **Repeat:** Continue until $\text{remainder} < \text{divisor}$.

> **Invariant.** At each step, $\text{dividend} = \text{quotient} \cdot \text{divisor} + \text{remainder}$, where $\text{remainder} \ge 0$ strictly decreases.

---

## 3. Step-by-Step Worked Execution

We trace $\text{dividend} = 10$, $\text{divisor} = 3$:

### Step 0: Setup & Boundary Check
- Check overflow: Not $(-2^{31}, -1)$.
- Sign check: Both $10 > 0$ and $3 > 0 \implies \text{sign} = +1$.
- Work with positive absolute values: $\text{rem} = 10$, $D = 3$.
- Initial quotient: $Q = 0$.

---

### Step 1: First Doubling Phase
Find the largest multiple $D \cdot 2^k \le \text{rem} = 10$:
- $k = 0$: $3 \cdot 2^0 = 3 \le 10$
- $k = 1$: $3 \cdot 2^1 = 6 \le 10$
- $k = 2$: $3 \cdot 2^2 = 12 > 10$ (exceeds remainder)
- Largest fitting power: $k = 1$ with value $6$ ($3 \times 2^1$).
- **Update:**
  - Subtract chunk: $\text{rem} \leftarrow 10 - 6 = 4$.
  - Add to quotient: $Q \leftarrow 0 + 2^1 = 2$.

---

### Step 2: Second Doubling Phase
Find the largest multiple $D \cdot 2^k \le \text{rem} = 4$:
- $k = 0$: $3 \cdot 2^0 = 3 \le 4$
- $k = 1$: $3 \cdot 2^1 = 6 > 4$ (exceeds remainder)
- Largest fitting power: $k = 0$ with value $3$ ($3 \times 2^0$).
- **Update:**
  - Subtract chunk: $\text{rem} \leftarrow 4 - 3 = 1$.
  - Add to quotient: $Q \leftarrow 2 + 2^0 = 3$.

---

### Step 3: Termination
- Remaining remainder $\text{rem} = 1 < D = 3$.
- No further multiples of $3$ can be subtracted.
- Apply sign: $+1 \cdot 3 = 3$.
- Bounds check: $-2147483648 \le 3 \le 2147483647$.
- Output: $3$.

---

## 4. Complete Execution Trace

| Phase | Remainder Before | Subtracted Power Chunk | Chunk Numerical Value | Power $2^k$ Added | Updated Quotient $Q$ | Remainder After |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 10 | $3 \ll 1$ | 6 | $2^1 = 2$ | 2 | 4 |
| 2 | 4 | $3 \ll 0$ | 3 | $2^0 = 1$ | **3** | 1 |
| Terminal | 1 | None ($1 < 3$) | - | - | 3 | 1 (Discarded) |

### Large Input Example: $\text{dividend} = 43, \text{divisor} = 3$

| Phase | Remainder | Largest Fitting Chunk | Power Added | Accumulated Quotient |
|:---:|:---:|:---:|:---:|:---:|
| 1 | 43 | $3 \ll 3 = 24$ | $2^3 = 8$ | 8 |
| 2 | $43 - 24 = 19$ | $3 \ll 2 = 12$ | $2^2 = 4$ | $8 + 4 = 12$ |
| 3 | $19 - 12 = 7$ | $3 \ll 1 = 6$ | $2^1 = 2$ | $12 + 2 = 14$ |
| 4 | $7 - 6 = 1$ | None ($1 < 3$) | - | **14** (Truncated) |

---

## 5. Algorithmic Correctness

**Soundness.** At every step, a quantity $2^k \cdot \text{divisor}$ is subtracted from the remainder, and $2^k$ is simultaneously added to the quotient. By distributive linearity, $\text{dividend} = Q \cdot \text{divisor} + \text{remainder}$. Because the loop halts when $0 \le \text{remainder} < \text{divisor}$, $Q$ is by definition the exact truncated quotient $\lfloor \text{dividend} / \text{divisor} \rfloor$.

**Completeness.** Each doubling phase subtracts at least half of the remaining dividend magnitude. The remainder strictly decreases toward $0$ in at most $32$ iterations, ensuring guaranteed termination for all 32-bit integers.

---

## 6. Traps This Instance Exposes

- **32-Bit Overflow Asymmetry:** In two's complement representation, the negative range $[-2^{31}]$ has one more value than the positive range $[2^{31}-1]$. Dividing $-2^{31}$ by $-1$ results in $2^{31}$, which cannot fit in a signed 32-bit integer. Explicit clamping to $2^{31}-1$ is required.
- **Divisor Equal to 1 or -1:** Dividing by $1$ or $-1$ can be checked early to bypass the bit-shift loop entirely.
- **Bit Shift Precedence:** In Python and C++, addition has higher precedence than bitwise shifts (`3 << 1 + 1` evaluates as `3 << 2 = 12`, not `(3 << 1) + 1 = 7`). Explicit parentheses around shifts are mandatory.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log^2(\text{dividend}))$ for nested doubling, or $O(\log(\text{dividend}))$ using a single decreasing shift from 31 down to 0. Since the input is bounded by 32 bits, the loop executes at most 32 times, running in strictly $O(1)$ constant time.
- **Auxiliary Space Complexity:** $O(1)$. Memory is limited to a few 64-bit integer registers for remainder and quotient tracking.
