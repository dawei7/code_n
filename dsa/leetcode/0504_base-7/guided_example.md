# Guided Example: Base 7

We trace the step-by-step radix-7 positional numeral division, remainder collection ($num \pmod 7$), quotient reduction ($num // 7$), sign prefix handling ($num < 0$), and digit reversal on representative integers:

- **Input:** $num = 100$
- **Required output:** `"202"`
  - Objective: Express decimal integer $100$ in base 7 notation:
    $$
    100_{10} = \sum_{i=0}^k d_i \cdot 7^i \quad \text{where } d_i \in \{0, 1, 2, 3, 4, 5, 6\}
    $$
- **Repeated division by 7 execution trace:**
  - Initial value: $num = 100$
  - **Iteration 1 (Least Significant Digit $7^0$):**
    - Compute remainder:
      $$
      d_0 = 100 \pmod 7 = \mathbf{2}
      $$
    - Compute quotient:
      $$
      num \leftarrow \lfloor 100 / 7 \rfloor = \mathbf{14}
      $$
    - Recorded digits: `[2]`
  - **Iteration 2 (Digit $7^1$):**
    - Compute remainder:
      $$
      d_1 = 14 \pmod 7 = \mathbf{0}
      $$
    - Compute quotient:
      $$
      num \leftarrow \lfloor 14 / 7 \rfloor = \mathbf{2}
      $$
    - Recorded digits: `[2, 0]`
  - **Iteration 3 (Most Significant Digit $7^2$):**
    - Compute remainder:
      $$
      d_2 = 2 \pmod 7 = \mathbf{2}
      $$
    - Compute quotient:
      $$
      num \leftarrow \lfloor 2 / 7 \rfloor = \mathbf{0}
      $$
    - Recorded digits: `[2, 0, 2]`
  - Division terminates since $num = 0$.
  - **Reverse to Most-Significant-Digit-First:**
    $$
    [2, 0, 2] \xrightarrow{\text{reverse}} \mathbf{\text{"202"}}
    $$
  - Verification:
    $$
    2 \cdot 7^2 + 0 \cdot 7^1 + 2 \cdot 7^0 = 2(49) + 0 + 2(1) = 98 + 2 = \mathbf{100}
    $$
- **Negative Value Instance ($num = -7$):**
  - Sign check: $-7 < 0 \implies$ prepend `'-'` to result of $+7$.
  - Positive $7$:
    - $7 \pmod 7 = 0$, $num = 1$
    - $1 \pmod 7 = 1$, $num = 0$
    - Reversed: `"10"`
  - Combined: $\mathbf{\text{"-10"}}$
- **Zero Input Instance ($num = 0$):**
  - Division loop would not execute $\implies$ Handled directly by base check: $\mathbf{\text{"0"}}$

This instance demonstrates positional numeral radix conversions, mathematically proves why successive modular remainders yield polynomial coefficients, and derives $O(\log_7 |num|)$ runtime and $O(\log_7 |num|)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an integer $num = 100$:
Return a string of its **base 7 representation**.

```text
Positional Representation in Base 7:
  100 = 2 * (7^2) + 0 * (7^1) + 2 * (7^0)
      = 2 * 49    + 0 * 7     + 2 * 1
      = 98 + 2 = 100

Base 7 String: "202"
```

### The Division-Remainder Algorithm
Any integer $N$ can be expressed in base $B$ as:
$$
N = d_k B^k + d_{k-1} B^{k-1} + \dots + d_1 B^1 + d_0 B^0
$$
- Taking $N \pmod B$ extracts the lowest coefficient $d_0$.
- Dividing $N \leftarrow \lfloor N / B \rfloor$ shifts all powers down by 1.
- Repeating this extracts digits from least significant ($7^0$) to most significant ($7^k$).
- Reversing the collected list gives the standard human-readable string.

---

## 2. Conceptual Foundation & Invariants

### 1. Radix Transition Steps:
For a positive integer $num$:
1. $d = num \pmod 7$ (Digit in $\{0, 1, 2, 3, 4, 5, 6\}$).
2. $num \leftarrow \lfloor num / 7 \rfloor$.
3. Repeat until $num == 0$.
4. Reverse the digit sequence.

### 2. Sign Invariance:
For negative inputs ($num < 0$):
Base conversion is applied to the absolute value $|num|$, and a negative sign `'-'` is prepended:
$$
\text{convertToBase7}(num) = \text{"-"} + \text{convertToBase7}(-num)
$$

### 3. Zero Handling:
$0$ has 0 quotient iterations in a `while num > 0` loop; it must return `"0"` as a base case.

> **Positional Invariant.** At step $i$, the remainder $num \pmod 7$ represents the exact coefficient of $7^i$ in the canonical base-7 expansion of the input.

---

## 3. Step-by-Step Worked Execution

We trace $num = 100$:

---

### Step 1: Base Case & Sign Checks
- $num \ne 0$.
- $num > 0$ (no sign prepending needed).

---

### Step 2: Division Steps
Initialize digit list: $ans = []$.

1. **Step 1 ($num = 100$):**
   - Remainder: $100 \pmod 7 = \mathbf{2}$.
   - Quotient: $\lfloor 100 / 7 \rfloor = \mathbf{14}$.
   - $ans = [2]$.
2. **Step 2 ($num = 14$):**
   - Remainder: $14 \pmod 7 = \mathbf{0}$.
   - Quotient: $\lfloor 14 / 7 \rfloor = \mathbf{2}$.
   - $ans = [2, 0]$.
3. **Step 3 ($num = 2$):**
   - Remainder: $2 \pmod 7 = \mathbf{2}$.
   - Quotient: $\lfloor 2 / 7 \rfloor = \mathbf{0}$.
   - $ans = [2, 0, 2]$.

---

### Step 3: Reverse & Join
- Reverse list: $[2, 0, 2] \to [2, 0, 2]$.
- Join to string:
  $$
  \mathbf{\text{"202"}}
  $$

---

## 4. Complete Execution Trace

| Step | Current Value $num$ | Quotient $\lfloor num / 7 \rfloor$ | Remainder $num \pmod 7$ | Digit Power | Digit Array $ans$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **$1$** | $100$ | $14$ | **$2$** | $7^0 = 1$ | `['2']` |
| **$2$** | $14$ | $2$ | **$0$** | $7^1 = 7$ | `['2', '0']` |
| **$3$** | $2$ | $0$ | **$2$** | $7^2 = 49$ | `['2', '0', '2']` |
| **Done** | $0$ | — | — | — | **Reversed: `"202"`** |

---

## 5. Boundary Cases & Failure Modes

- **Zero ($num = 0$):** Handled directly by `if num == 0: return '0'`.
- **Negative Power of Seven ($num = -7$):** Yields $\mathbf{\text{"-10"}}$.
- **Large Values ($num = 10^7$):** $\log_7(10^7) \approx 8.28 \implies$ generates at most 9 digits.
- **Numbers Less than Seven ($num \in [1, 6]$):** 1 division step $\implies$ returns the digit directly.

---

## 6. Traps & Common Anti-Patterns

- **Negative Modulo in Different Languages:** In C/C++, `-7 % 7` evaluates differently than in Python. Converting to positive $-num$ first avoids all implementation-specific negative modulo issues.
- **Missing Reversal:** Appending remainders produces least-significant digits first (`"202"` is symmetric, but $num = 8$ produces remainders `[1, 1]`, while $num = 15$ produces `[1, 2]`). Forgetting to reverse produces `"12"` instead of `"21"`.
- **Omitting Zero Base Case:** If $num = 0$ enters `while num:`, the loop terminates with an empty string `""` instead of `"0"`.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - In each step, $num$ is divided by 7.
  - Number of iterations is $\lfloor\log_7 |num|\rfloor + 1$.
  - For $|num| \le 10^7$, $\log_7(10^7) \le 9$ operations.
  - Total Time: $\mathcal{O}(\log_7 |num|)$. Completes in $< 1$ microsecond.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(\log_7 |num|)$ to store the character list buffer.
