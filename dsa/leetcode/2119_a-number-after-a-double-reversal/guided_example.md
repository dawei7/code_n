# Guided Example: A Number After a Double Reversal

We trace the step-by-step execution of the optimal digit-loss invariance check on representative problem instances:

- **Representative Instance 1:** `num = 526` $\implies$ Expected Output: `true`
- **Representative Instance 2:** `num = 1800` $\implies$ Expected Output: `false`
- **Representative Instance 3:** `num = 0` $\implies$ Expected Output: `true`

This example demonstrates the digit-truncation mechanics of integer reversal, proving why trailing zeros are irrecoverably lost and why the result can be determined in $\mathcal{O}(1)$ time using modular arithmetic.

---

## 1. Problem Overview & Representative Instance

Reversing an integer means reversing the sequence of its decimal digits. However, because standard integers cannot have leading zeros, any leading zeros produced by the reversal are dropped.
We perform a double reversal:
1. Reverse $num$ to produce $R_1$.
2. Reverse $R_1$ to produce $R_2$.
We need to determine whether $R_2 = num$.

Consider our three contrasting instances:
- When $num = 526$:
  - First reversal: $526 \to 625$. No leading zeros were generated because the last digit $6 \ne 0$.
  - Second reversal: $625 \to 526$.
  - Result: $526 = 526 \implies$ `true`.
- When $num = 1800$:
  - First reversal: $1800 \to 0081$, which drops the leading zeros to become $81$.
  - Second reversal: $81 \to 18$.
  - Result: $18 \ne 1800 \implies$ `false`.
- When $num = 0$:
  - First reversal: $0 \to 0$.
  - Second reversal: $0 \to 0$.
  - Result: $0 = 0 \implies$ `true`.

---

## 2. Mathematical & Algorithmic Principles

### Information Loss via Trailing Zeros
Let a positive integer $num$ have decimal digit representation:

$$num = \sum_{j=0}^{k-1} d_j \cdot 10^j = (d_{k-1} d_{k-2} \dots d_1 d_0)_{10}$$

where $k \ge 1$ is the number of digits and $d_{k-1} \ne 0$.
Under digit reversal, the units digit $d_0$ becomes the most significant digit of the reversed value:
- If $d_0 \ne 0$, the reversed number has exactly $k$ digits with leading digit $d_0$. The second reversal maps the digits back to their original positions, preserving length and magnitude identically: $R_2 = num$.
- If $d_0 = 0$ and $num > 0$, the reversed representation begins with one or more zeros: $(0 \dots 0 d_m \dots d_{k-1})_{10}$. Truncating these leading zeros reduces the digit count from $k$ to $m < k$. Reversing this shortened integer yields a number with at most $m$ digits, strictly smaller than $num$:

$$R_2 \le 10^m - 1 < 10^{k-1} \le num \implies R_2 \ne num$$

### Closed-Form Criterion
Therefore, an integer preserves its identity across double reversal if and only if it has zero trailing zeros, with the single exception of $0$ itself:

$$R_2 = num \iff (num = 0) \lor (num \not\equiv 0 \pmod{10})$$

This condition can be evaluated via a single modulo operation and a zero equality test in $\mathcal{O}(1)$ time.

| Number Category | Least Significant Digit ($d_0$) | First Reversal Effect | Double Reversal Outcome |
|---|---|---|---|
| Zero ($num = 0$) | $0$ | $0 \to 0$ (identity) | `true` |
| Positive ending in non-zero | $d_0 \in \{1, \dots, 9\}$ | Full $k$ digits preserved | `true` |
| Positive ending in zero | $d_0 = 0$ | Leading zero(s) truncated ($< k$ digits) | `false` |

---

## 3. Step-by-Step Walkthrough with Intermediate State

We evaluate the decision logic across our representative test cases:

### Case 1: $num = 526$
- **Step 1 (Zero Check):** Does $num = 0$? No ($526 \ne 0$).
- **Step 2 (Modulo Check):** Compute $526 \pmod{10} = 6$.
- **Step 3 (Comparison):** Is $6 \ne 0$? Yes.
- **Conclusion:** No trailing zeros exist. Double reversal preserves the number. Output is `true`.

### Case 2: $num = 1800$
- **Step 1 (Zero Check):** Does $num = 0$? No ($1800 \ne 0$).
- **Step 2 (Modulo Check):** Compute $1800 \pmod{10} = 0$.
- **Step 3 (Comparison):** Is $0 \ne 0$? No.
- **Conclusion:** $num$ has trailing zeros that are lost during the initial reversal. Output is `false`.

### Case 3: $num = 0$
- **Step 1 (Zero Check):** Does $num = 0$? Yes.
- **Conclusion:** The special case $num = 0$ evaluates to `true` immediately via boolean short-circuiting.

---

## 4. Comprehensive State Trace

The evaluation metrics across several representative inputs are tabulated below:

| Candidate $num$ | Zero Condition ($num = 0$) | Modulo Residue ($num \pmod{10}$) | Non-Zero Check ($num \pmod{10} \ne 0$) | Final Boolean Decision |
|---|---|---|---|---|
| $526$ | False | $6$ | True | `true` |
| $1800$ | False | $0$ | False | `false` |
| $0$ | True | $0$ | False (short-circuited) | `true` |
| $4$ | False | $4$ | True | `true` |
| $100$ | False | $0$ | False | `false` |
| $102$ | False | $2$ | True | `true` |

Notice that intermediate zeros (as in $102 \to 201 \to 102$) do not cause truncation; only trailing zeros cause irreversibility.

---

## 5. Algorithmic Correctness & Soundness

**Soundness.** Suppose $num > 0$ and $num \pmod{10} = 0$. Then $num$ ends with at least one $0$. By integer literal semantics, converting the reversed digit sequence back into an integer discards all leading zeros. The length of the first reversal $R_1$ is strictly less than the length of $num$. Reversing $R_1$ can never recover the discarded digits because integer reversal preserves or decreases digit length, never increases it. Hence, $R_2 \ne num$ is guaranteed whenever $num > 0$ and $num \pmod{10} = 0$.

**Completeness.** If $num = 0$, both reversals produce $0$, so $R_2 = num$ holds. If $num > 0$ and $num \pmod{10} \ne 0$, the first digit of the reversed number is non-zero, meaning no leading zeros are truncated. Reversing a sequence of $k$ digits twice without truncation is the permutation involution $\tau \circ \tau = \text{id}$, restoring the exact initial number. Thus all cases are fully characterized.

---

## 6. Edge Cases & Anti-Patterns

- **Zero Boundary ($num = 0$):** $0 \pmod{10} = 0$, which would fail the non-zero test if evaluated in isolation. The explicit disjunction `num == 0` correctly handles this boundary.
- **Single-Digit Numbers ($1 \le num \le 9$):** Single non-zero digits have no trailing zeros and reverse to themselves.
- **Internal Zeros ($num = 105$):** $105 \to 501 \to 105$. The internal zero remains protected between non-zero digits and is never truncated.
- **Anti-Pattern — String Conversion and Dual Reversal:** Converting the number to a string, slicing backwards, parsing back to integer, converting to string again, and parsing once more requires multiple heap allocations and string parsing steps. The mathematical condition `num == 0 or num % 10 != 0` executes in $\mathcal{O}(1)$ time without memory allocation.

---

## 7. Complexity Analysis

- **Time Complexity:** $\mathcal{O}(1)$. The algorithm executes a single equality comparison and a single integer modulo operation on primitive hardware registers.
- **Auxiliary Space Complexity:** $\mathcal{O}(1)$. No auxiliary memory, strings, or intermediate data structures are allocated.
