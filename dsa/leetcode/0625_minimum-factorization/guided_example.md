# Guided Example: Minimum Factorization

We trace the step-by-step greedy prime-factor aggregation into maximal single decimal digits ($9 \to 2$), positional place-value assembly ($ans = mul \cdot d + ans$), prime factor impossibility verification ($num > 1 \implies 0$), 32-bit signed integer overflow bound checks ($ans \le 2^{31} - 1$), and minimal digit sequence construction on representative integer inputs:

- **Input:** $a = 48$
- **Required output:** `68`
  - Problem objective: Find the **smallest positive integer** whose digits multiply together to produce $a$:
    $$
    \prod_{k} \text{digit}_k = a
    $$
  - If no such integer exists, or if the integer exceeds the 32-bit signed integer limit ($2^{31} - 1 = 2{,}147{,}483{,}647$), return `0`.
- **Greedy Maximization & Positional Weight Invariants:**
  - To make an integer as small as possible:
    1. **Minimize the number of digits:** A 2-digit number is always smaller than a 3-digit number (e.g. $68 < 246$). To minimize total digits, we must combine smaller prime factors ($2$ and $3$) into the **largest possible single-digit factors** ($9, 8, 7, 6, \dots$).
    2. **Ascending digit order:** Place smaller digits in the most significant positions (e.g. $68 < 86$).
  - **Greedy Division Order ($9 \to 2$):**
    - Greedily test divisibility by digits $d$ starting from $9$ down to $2$.
    - The first (largest) factor extracted will become the **least significant digit** (units place).
    - Successive factors occupy tens, hundreds, thousands, etc., ensuring digits are assembled in **ascending order from left to right**!
  - **Impossibility & Overflow Conditions:**
    - If after testing all single-digit factors $9 \dots 2$, the remaining value of $num > 1$, then $a$ contains a prime factor $\ge 11$ (such as $11, 13, 17$). Since prime numbers $\ge 11$ cannot be represented as a single decimal digit, factorization is **impossible** $\implies$ return `0`.
    - If the resulting number $ans > 2^{31} - 1$, return `0`.
- **Step-by-Step Worked Execution Trace on $a = 48$:**
  - Initial state:
    $$
    num = 48, \quad ans = 0, \quad mul = 1
    $$
  - **Test $d = 9$:** $48 \pmod 9 = 3 \ne 0 \implies$ Skip.
  - **Test $d = 8$:**
    - $48 \pmod 8 == 0 \implies \mathbf{Divisible!}$
    - Divide:
      $$
      num \leftarrow \frac{48}{8} = \mathbf{6}
      $$
    - Place digit $8$ at active multiplier $mul = 1$:
      $$
      ans \leftarrow (1 \times 8) + 0 = \mathbf{8}
      $$
      $$
      mul \leftarrow 1 \times 10 = \mathbf{10}
      $$
    - Check remaining $num = 6$: $6 \pmod 8 \ne 0$. Move to next digit.
  - **Test $d = 7$:** $6 \pmod 7 \ne 0 \implies$ Skip.
  - **Test $d = 6$:**
    - $6 \pmod 6 == 0 \implies \mathbf{Divisible!}$
    - Divide:
      $$
      num \leftarrow \frac{6}{6} = \mathbf{1}
      $$
    - Place digit $6$ at active multiplier $mul = 10$:
      $$
      ans \leftarrow (10 \times 6) + 8 = \mathbf{68}
      $$
      $$
      mul \leftarrow 10 \times 10 = \mathbf{100}
      $$
    - Remaining $num = 1$. Loop finishes since $num < 2$.
  - **Step 4: Post-Loop Validation:**
    - Check remaining quotient:
      $$
      num = 1 \le 1 \implies \mathbf{Complete\ factorization!}
      $$
    - Check 32-bit integer bound:
      $$
      ans = 68 \le 2^{31} - 1 = 2147483647 \implies \mathbf{Valid!}
      $$
    - Return **`68`**.
    - Verification: Digits $6 \times 8 = 48$. No smaller number exists ($48$ has factors $2 \times 2 \times 2 \times 2 \times 3$; any other digit combinations like $246$ or $344$ are $\ge 3$ digits or larger).
- **Impossible Prime Factor Instance ($a = 22$):**
  - Prime factorization: $22 = 2 \times 11$.
  - Extract $2 \implies num = 11$.
  - No digits $2 \dots 9$ divide $11$.
  - Loop terminates with $num = 11 > 1 \implies$ Returns **`0`**.
- **32-Bit Integer Overflow Instance:**
  - $a = 18000000$: digits require $> 10$ places, producing a number $> 2^{31} - 1 \implies$ Returns **`0`**.
- **Trivial Inputs ($a = 1$):**
  - Digits multiply to $1 \implies$ Returns **`1`**.

This instance demonstrates greedy base-10 radix compression over prime factor multisets, mathematically proves why maximal digit extraction minimizes positional string length, and derives $O(\log a)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an integer $a$:
Find the **smallest positive integer** $b$ whose digits multiply to $a$.
Return 0 if impossible or if $b$ exceeds the 32-bit signed integer limit.

```text
Target product a = 48

Candidate combinations of digits multiplying to 48:
  2 * 4 * 6 = 48  ->  246 (3 digits)
  3 * 4 * 4 = 48  ->  344 (3 digits)
  6 * 8     = 48  ->   68 (2 digits)  <-- SMALLEST!

Result: 68
```

### The Invariant of Greedy Digits
- To minimize the final integer:
  1. It must have the **fewest digits possible** (2 digits is always smaller than 3 digits).
  2. The smaller digits must appear in the **higher place-values** (leftmost).
- Both goals are simultaneously achieved by greedily extracting the **largest available single-digit factors** ($9, 8, \dots, 2$) from right to left!

---

## 2. Conceptual Foundation & Invariants

### 1. The Greedy Factoring Loop:
- From $d = 9$ down to $2$:
  - While $num \pmod d == 0$:
    - $num \leftarrow num / d$
    - $ans \leftarrow mul \cdot d + ans$
    - $mul \leftarrow mul \cdot 10$

### 2. The Verification Gate:
Return $ans$ if and only if:
$$
num == 1 \quad \text{AND} \quad ans \le 2^{31} - 1
$$
Otherwise return $0$.

> **Greedy Minimality Invariant.** Dividing by the largest available factor $d \in [2, 9]$ minimizes the total number of prime factors that must be partitioned into separate digits, strictly minimizing the decimal length of the integer.

---

## 3. Step-by-Step Worked Execution

We trace $a = 48$:

---

### Step 1: Initialize
- $num = 48, ans = 0, mul = 1$.

---

### Step 2: Try Digits 9 down to 2
- $d = 8$: $48 / 8 = 6$
  - $ans = 1 \cdot 8 + 0 = 8$.
  - $mul = 10$.
  - $num = 6$.
- $d = 6$: $6 / 6 = 1$
  - $ans = 10 \cdot 6 + 8 = 68$.
  - $mul = 100$.
  - $num = 1$.

---

### Step 3: Validate
- $num = 1 \le 1$.
- $ans = 68 \le 2^{31} - 1$.
- Return **`68`**.

---

## 4. Complete Execution Trace

| Tested Digit $d$ | Divisible? | Quotient $num$ After | Digit Position | Contribution $mul \cdot d$ | Value of $ans$ After |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $9$ | No ($48 \% 9 \ne 0$) | $48$ | — | — | $0$ |
| **$8$** | **Yes** | **$6$** | Units ($mul = 1$) | $8$ | **$8$** |
| $7$ | No | $6$ | — | — | $8$ |
| **$6$** | **Yes** | **$1$** | Tens ($mul = 10$) | $60$ | **`68`** |
| **End** | $num = 1$ | — | — | — | **`68`** |

---

## 5. Boundary Cases & Failure Modes

- **$a < 2$ (0 or 1):** Returns $a$ directly.
- **Prime Factors $\ge 11$ ($a = 22, 26, 33$):** Cannot be factored into single digits $\implies num > 1 \implies$ returns $0$.
- **Integer Overflow ($> 2^{31} - 1$):** Returns $0$.
- **Prime Target ($a = 7$):** Factors into single digit $7 \implies 7$.

---

## 6. Traps & Common Anti-Patterns

- **Extracting Factors From Small to Large ($2 \to 9$):** Extracting small factors first produces fragmented representations (e.g. $48 \to 2 \cdot 2 \cdot 2 \cdot 2 \cdot 3 \implies 22223$), which is vastly larger than $68$.
- **Forgetting the Remaining $num > 1$ Check:** If $a$ has a prime factor like 13, the loop finishes without dividing it. If you don't check $num == 1$, an invalid answer is returned.
- **32-Bit Signed Limit:** In Python, integers have arbitrary precision and do not automatically overflow. You must explicitly test $ans \le 2^{31} - 1$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Digits $9 \dots 2$ are checked in a fixed outer loop of at most 8 iterations.
  - The inner `while` divides $num$ by at least 2 at each step, running at most $\log_2 a \le 31$ times.
  - Total Time: $\mathcal{O}(\log a)$ operations. Completes in $< 0.1$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ auxiliary space (a few 64-bit integer variables).
