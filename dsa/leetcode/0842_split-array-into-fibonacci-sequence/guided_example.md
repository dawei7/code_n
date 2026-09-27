# Guided Example: Split Array into Fibonacci Sequence

We trace the step-by-step backtracking search on digit split boundaries, leading zero rejection ($num[i] == \text{'0'} \land j > i$), 32-bit signed integer overflow ceiling ($x \le 2^{31} - 1$), additive recurrence validation ($F[k] = F[k-2] + F[k-1]$), early pruning on sum overshoot ($x > ans[-2] + ans[-1]$), and Fibonacci sequence reconstruction on representative digit strings:

- **Input:**
  $$
  num = \text{"1101111"}
  $$
- **Required output:**
  $$
  [11, 0, 11, 11]
  $$
  - Fibonacci sequence partition specifications:
    - We are given a numeric string $num$ of length $n$.
    - We seek to split $num$ into a sequence of at least 3 integers $[F_0, F_1, F_2, \dots, F_{m-1}]$ such that:
      1. **Cardinality:** $m \ge 3$.
      2. **Fibonacci Additive Law:** For all $k \ge 2$:
         $$
         F_k = F_{k-2} + F_{k-1}
         $$
      3. **32-Bit Signed Bounds:** Each integer satisfies $0 \le F_k \le 2^{31} - 1 = 2,147,483,647$.
      4. **No Leading Zeros:** A number cannot begin with `'0'` unless the number itself is the single digit $0$.
    - For $num = \text{"1101111"}$:
      - Split $F_0 = 11$ (digits `"11"`).
      - Split $F_1 = 0$ (digit `"0"`, valid single-digit zero).
      - Next required: $F_2 = 11 + 0 = 11$ (digits `"11"`).
      - Next required: $F_3 = 0 + 11 = 11$ (digits `"11"`).
      - Total concatenated digits: `"11" + "0" + "11" + "11" = "1101111"`.
      - Valid sequence: $[11, 0, 11, 11]$.
- **Prefix Branching & Monotone Determinism Invariant:**
  - **The Deterministic Extension Theorem:**
    - Notice that once the first two integers $F_0$ and $F_1$ are selected, **every subsequent term is uniquely and deterministically fixed**:
      $$
      F_2 = F_0 + F_1, \quad F_3 = F_1 + F_2, \quad \dots
      $$
    - Thus, the search tree branches **only** when choosing the initial pair $(F_0, F_1)$. All remaining digits must match the exact string representation of the expected sum!
  - **Pruning & Feasibility Invariants:**
    1. **Leading Zero Pruning:**
       - If $num[i] == \text{'0'}$, the only valid number starting at index $i$ is the single-digit $0$.
       - Any longer substring ($j > i$) starting with `'0'` is rejected immediately without recursion (`break`).
    2. **32-Bit Overflow Pruning:**
       - As soon as the parsed integer $x > 2^{31} - 1$, extending the substring further will only make $x$ larger. Terminate the inner loop (`break`).
    3. **Overshoot Pruning:**
       - Once $|ans| \ge 2$, the required next value is strictly $target = ans[-2] + ans[-1]$.
       - If the current parsed number $x > target$, extending the substring further can never equal $target$. Terminate the inner loop (`break`).
- **Step-by-Step Worked Execution Trace on $num = \text{"1101111"}$ ($n = 7$):**
  - **Trial 1: Choose $F_0 = 1$ (index 0..0):**
    - $ans = [1]$. Recurse to index 1.
    - **Trial 1.1: Choose $F_1 = 1$ (index 1..1):**
      - $ans = [1, 1]$. Target $F_2 = 1 + 1 = \mathbf{2}$.
      - Next digit at index 2 is `'0'`. Single digit 0 fails $0 \ne 2$.
      - Backtrack.
    - **Trial 1.2: Choose $F_1 = 10$ (index 1..2):**
      - $ans = [1, 10]$. Target $F_2 = 1 + 10 = \mathbf{11}$.
      - Index 3..4: digits `"11"` parse to $11 == 11 \implies \mathbf{Match!}$
      - $ans = [1, 10, 11]$. Target $F_3 = 10 + 11 = \mathbf{21}$.
      - Remaining digits at index 5..6: `"11"` $\ne 21$.
      - Backtrack.
    - Backtrack all choices with $F_0 = 1$.
  - **Trial 2: Choose $F_0 = 11$ (index 0..1):**
    - Substring $num[0..1] = \text{"11"} \implies F_0 = \mathbf{11}$.
    - $ans = [11]$. Recurse to index 2.
    - **Trial 2.1: Choose $F_1$ starting at index 2 ($num[2] = \text{'0'}$):**
      - Since $num[2] = \text{'0'}$, the only valid number is length 1: $F_1 = \mathbf{0}$.
      - $ans = [11, 0]$.
      - Required target $F_2 = 11 + 0 = \mathbf{11}$.
      - Recurse to index 3.
      - **Trial 2.1.1: Search for $F_2 = 11$ starting at index 3:**
        - Index 3..3: digit `"1"` ($1 < 11 \implies$ continue loop).
        - Index 3..4: digits `"11"` $\implies x = 11 == target \implies \mathbf{Match!}$
        - $ans = [11, 0, 11]$.
        - Required target $F_3 = 0 + 11 = \mathbf{11}$.
        - Recurse to index 5.
        - **Trial 2.1.1.1: Search for $F_3 = 11$ starting at index 5:**
          - Index 5..5: digit `"1"` ($1 < 11 \implies$ continue).
          - Index 5..6: digits `"11"` $\implies x = 11 == target \implies \mathbf{Match!}$
          - $ans = [11, 0, 11, 11]$.
          - Recurse to index 7 ($i == n$).
          - Base case reached with $|ans| = 4 \ge 3 \implies \mathbf{Success!}$
  - **Return Winning Partition:**
    $$
    ans = [11, \; 0, \; 11, \; 11]
    $$
- **Unsplittable String Trace ($num = \text{"112358130"}$):**
  - Sequence $[1, 1, 2, 3, 5, 8]$ matches up to index 6.
  - Next required is $5 + 8 = 13$ (indices 6..7).
  - Then $8 + 13 = 21$, but remaining digit is `"0"`, which cannot equal 21 $\implies$ returns `[]`.
- **Large Fibonacci Sequence ($num = \text{"123456579"}$):**
  - Splits into $[123, 456, 579]$ since $123 + 456 = 579$.

This instance demonstrates recursive backtracking under Diophantine prefix constraints and deterministic forward propagation, mathematically proves why fixing the initial base coordinates collapses exponential split complexity into linear verification passes, and derives $O(N^2)$ runtime and $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a digit string $num$:
Split $num$ into a Fibonacci-like sequence $[F_0, F_1, F_2, \dots]$ where:
- Length $\ge 3$
- Each integer $\le 2^{31} - 1$
- No leading zeros (except $0$ itself)
- $F_k = F_{k-2} + F_{k-1}$

```text
num = "1101111"

Try F0 = 11, F1 = 0:
  Next must be 11 + 0 = 11 -> matches "11"!
  Next must be 0 + 11 = 11 -> matches "11"!
  All digits used!

Result: [ 11, 0, 11, 11 ]
```

### The Invariant of Deterministic Propagation
- The search tree only branches on the first two numbers $(F_0, F_1)$.
- Once $F_0$ and $F_1$ are chosen, every subsequent number is strictly determined: $F_k = F_{k-2} + F_{k-1}$.
- Break immediately if $x > target$, $x > 2^{31} - 1$, or a leading zero is extended.

---

## 2. Conceptual Foundation & Invariants

### 1. Fibonacci Recurrence:
$$
F_k = F_{k-2} + F_{k-1} \quad \text{for } k \ge 2
$$

### 2. State Feasibility Predicate:
$$
\text{ValidNext}(x) \iff (x \le 2^{31} - 1) \;\land\; \Big( |ans| < 2 \;\lor\; x = ans[-2] + ans[-1] \Big)
$$

> **Fiber Degeneracy Invariant.** The Fibonacci recurrence is a linear difference equation of order 2. The solution space over $\mathbb{Z}$ is an affine plane parameterized solely by the initial conditions $(F_0, F_1)$. For a string of length $n$, testing all pairs $(F_0, F_1)$ takes at most $\mathcal{O}(n^2)$ configurations, after which forward validation is completely deterministic.

---

## 3. Step-by-Step Worked Execution

We trace $num = \text{"1101111"}$:

---

### Step 1: Pick $F_0 = 11$
- Substring `"11"`. $ans = [11]$.

---

### Step 2: Pick $F_1 = 0$
- Next digit is `'0'`. Only length 1 valid.
- $ans = [11, 0]$. Target $= 11$.

---

### Step 3: Match $F_2 = 11$
- Substring `"11"` equals 11.
- $ans = [11, 0, 11]$. Target $= 11$.

---

### Step 4: Match $F_3 = 11$
- Substring `"11"` equals 11.
- $ans = [11, 0, 11, 11]$.
- End of string reached with length 4 $\ge 3$!

---

### Step 5: Output
$$
[11, \; 0, \; 11, \; 11]
$$

---

## 4. Complete Execution Trace

| Backtrack Step | Current Position $i$ | Substring Selected | Parsed Value $x$ | Target Expected | Action Taken | Current $ans$ Stack |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Root | $0$ | `"11"` | $11$ | Any ($F_0$) | Push $11$ | $[11]$ |
| Branch 1 | $2$ | `"0"` | $0$ | Any ($F_1$) | Push $0$ | $[11, 0]$ |
| Branch 2 | $3$ | `"11"` | $11$ | $11 + 0 = 11$ | **Match $\to$ Push** | $[11, 0, 11]$ |
| **Branch 3** | **$5$** | **`"11"`** | **$11$** | **$0 + 11 = 11$** | **Match $\to$ Push** | **`[11, 0, 11, 11]`** |
| **Complete** | **$7 == n$** | **End** | — | — | **Success Return** | **`[11, 0, 11, 11]`** |

---

## 5. Boundary Cases & Failure Modes

- **Leading Zero Handling ($num = \text{"0123"}$):** Substring `"01"` is immediately blocked; only `"0"` can be chosen as $F_0$, then $F_1 = 1 \implies 0 + 1 = 1 \ne 2 \implies []$.
- **Overflowing $2^{31} - 1$:** When integer exceeds $2,147,483,647$, stop the inner loop immediately.
- **Minimum Cardinality ($|ans| \ge 3$):** Reaching string end with only 2 numbers returns `False` (must have at least 3 numbers).
- **String Cannot Form Sequence:** Returns empty list `[]`.

---

## 6. Traps & Common Anti-Patterns

- **Permitting Multi-Digit Numbers with Leading Zeros:** Substrings like `"03"` or `"00"` are strictly forbidden. When `num[i] == '0'`, break the loop after length 1.
- **Exploring Substrings After $x > target$:** Since $x$ grows monotonically with substring length, once $x > ans[-2] + ans[-1]$, no longer substring starting at $i$ can match $target$. Break early.
- **Integer Overflow in Other Languages:** Use 64-bit integer types during accumulation to check $x > 2^{31} - 1$ safely.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - First two numbers have at most $\min(n/2, 10)$ digits each due to the $2^{31} - 1$ bound.
  - Number of pairs $(F_0, F_1)$ is bounded by $10 \times 10 = 100$.
  - Once a pair is chosen, remaining string validation takes $\mathcal{O}(N)$ comparisons.
  - Total Time: strictly bounded $\mathcal{O}(N^2)$ where $N \le 35 \implies \le 1200$ operations. Completes in $< 1$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ memory for the recursion stack and sequence accumulator.
