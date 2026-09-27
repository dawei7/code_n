# Guided Example: Non-negative Integers without Consecutive Ones

We trace the step-by-step binary digit dynamic programming state space ($dfs(i, pre, limit)$), most-significant-bit boundary decomposition ($n \gg i \ \& \ 1$), consecutive ones pruning ($pre == 1 \land j == 1$), Fibonacci word combinatorial transitions, prefix tightness relaxation, and valid integer counting on representative upper bounds:

- **Input:** $n = 5$
- **Required output:** `5`
  - Range evaluated: Integers $x \in [0, 5]$.
  - Constraint: The binary representation of $x$ must **not contain consecutive ones** (`"11"` substring).
  - Explicit binary inspection of integers in $[0, 5]$:
    - $0 = 0_2 \implies$ Valid
    - $1 = 1_2 \implies$ Valid
    - $2 = 10_2 \implies$ Valid
    - $3 = 11_2 \implies$ **Invalid (consecutive ones)**
    - $4 = 100_2 \implies$ Valid
    - $5 = 101_2 \implies$ Valid
  - Total valid integers: $\{0, 1, 2, 4, 5\} \implies \mathbf{5}$.
- **Digit Dynamic Programming Formulation ($dfs(i, pre, limit)$):**
  - Represent $n$ in binary: $5 = 101_2$ (bit length $L = 3$, bits $i \in [2, 1, 0]$).
  - Parameters:
    - $i$: Active bit position being chosen (from MSB $L - 1$ down to LSB $0$).
    - $pre \in \{0, 1\}$: The bit chosen at position $i + 1$.
    - $limit \in \{\text{True}, \text{False}\}$: True if all bits placed at positions $> i$ match the prefix of $n$; False if a strictly smaller bit was placed earlier (allowing free placement of $0$ or $1$).
  - **Pruning Rule:**
    - If $pre == 1$ and the current candidate bit $j == 1$:
      $$
      \text{Consecutive ones detected!} \implies \text{Prune branch immediately.}
      $$
  - **Upper Bound Bit ($up$):**
    $$
    up = \begin{cases} (n \gg i) \ \& \ 1 & \text{if } limit = \text{True} \\ 1 & \text{if } limit = \text{False} \end{cases}
    $$
  - **Base Case ($i < 0$):**
    - All $L$ bits have been successfully placed without violating the constraint:
      $$
      \text{return } 1
      $$
- **Step-by-Step Decision Tree Trace for $n = 5$ ($101_2$):**
  - **Level 1 ($i = 2$, MSB of $n$, $limit = \text{True}, pre = 0$):**
    - $up = (5 \gg 2) \ \& \ 1 = 1$.
    - Candidate bits $j \in \{0, 1\}$:
      - **Branch 1A ($j = 0$):**
        - Bit 0 is strictly smaller than $n$'s bit 1 $\implies limit$ becomes $\mathbf{False}$.
        - Transition to $dfs(1, \; pre=0, \; limit=\text{False})$.
      - **Branch 1B ($j = 1$):**
        - Bit 1 matches $n$'s bit 1 $\implies limit$ remains $\mathbf{True}$.
        - Transition to $dfs(1, \; pre=1, \; limit=\text{True})$.
  - **Level 2A (From Branch 1A: $dfs(1, pre=0, limit=\text{False})$):**
    - Free choice: $up = 1$.
    - Candidate bits $j \in \{0, 1\}$:
      - $j = 0$: $pre=0, j=0 \implies dfs(0, 0, \text{False})$.
        - At $i = 0$: choices $j=0 \implies 1$, $j=1 \implies 1$. (Numbers: $000_2 = 0$, $001_2 = 1$). Subtotal = $\mathbf{2}$.
      - $j = 1$: $pre=0, j=1 \implies dfs(0, 1, \text{False})$.
        - At $i = 0$: choices $j=0 \implies 1$, $j=1$ pruned ($pre=1 \land j=1$). (Number: $010_2 = 2$). Subtotal = $\mathbf{1}$.
      - Subtotal for Branch 1A: $2 + 1 = \mathbf{3}$ valid numbers ($0, 1, 2$).
  - **Level 2B (From Branch 1B: $dfs(1, pre=1, limit=\text{True})$):**
    - Tight bound: $n$'s bit 1 is $0 \implies up = (5 \gg 1) \ \& \ 1 = \mathbf{0}$.
    - Candidate bit only $j = 0$:
      - Place $j = 0$: $pre=1, j=0$ (Valid!).
      - $limit$ remains True (since $j == up == 0$).
      - Transition to $dfs(0, \; pre=0, \; limit=\text{True})$.
  - **Level 3 (From Branch 2B: $dfs(0, pre=0, limit=\text{True})$):**
    - $n$'s bit 0 is $1 \implies up = 1$.
    - Candidate bits $j \in \{0, 1\}$:
      - $j = 0$: $limit$ becomes False $\implies$ base case returns $\mathbf{1}$ (Number $100_2 = 4$).
      - $j = 1$: $pre=0, j=1$ (Valid!) $\implies$ base case returns $\mathbf{1}$ (Number $101_2 = 5$).
      - Subtotal for Branch 1B: $1 + 1 = \mathbf{2}$ valid numbers ($4, 5$).
  - **Summing All Subtrees:**
    $$
    \text{Total} = \text{Branch 1A} + \text{Branch 1B} = 3 + 2 = \mathbf{5}
    $$
- **Connection to Fibonacci Numbers:**
  - The number of $k$-bit binary strings without consecutive ones is the Fibonacci number $F_{k+2}$ ($F_1=1, F_2=1, F_3=2, F_4=3, F_5=5, \dots$).
  - For unconstrained 2-bit suffix, the count is $F_4 = 3$.
- **Power of Two Boundary ($n = 1$):**
  - $0_2$ and $1_2 \implies \mathbf{2}$.
- **Consecutive Ones in $n$ (e.g. $n = 3 = 11_2$):**
  - Placing $1$ at bit 1 and $1$ at bit 0 triggers pruning $\implies 3$ valid numbers ($0, 1, 2$).

This instance demonstrates binary digit dynamic programming with state-constrained bit placement, mathematically proves the Fibonacci recurrence governing non-adjacent binary words, and derives $O(\log N)$ runtime and $O(\log N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an integer $n$:
Find how many integers in $[0, n]$ have **no consecutive ones** in their binary representation.

```text
n = 5 (Binary: 101)

Integers 0 to 5:
  0 = 000_2 -> Valid
  1 = 001_2 -> Valid
  2 = 010_2 -> Valid
  3 = 011_2 -> INVALID (has "11")
  4 = 100_2 -> Valid
  5 = 101_2 -> Valid

Total Valid Integers = 5
```

### The Structure of Binary Digit DP
- Counting valid integers up to $10^9$ by checking each number one by one is impossible ($10^9$ takes seconds).
- Instead, we construct the binary representation bit by bit from the most significant bit (MSB) to the least significant bit (LSB):
  - State: $(i, pre, limit)$
  - $i$: current bit index ($29 \dots 0$).
  - $pre$: whether the previous bit was 1.
  - $limit$: whether we are restricted by the prefix of $n$.
- When $limit = \text{False}$, the state $(i, pre)$ repeats across multiple branches, allowing memoization.

---

## 2. Conceptual Foundation & Invariants

### 1. State Recurrence:
$$
dfs(i, pre, limit) = \sum_{j=0}^{up} dfs(i - 1, j, limit \land (j == up))
$$
subject to:
$$
\text{skip if } (pre == 1 \land j == 1)
$$

### 2. Base Case:
$$
dfs(-1, pre, limit) = 1
$$

### 3. Bit Length:
Start at $i = \lfloor \log_2 n \rfloor$ with $pre = 0, limit = \text{True}$.

> **Prefix Domination Invariant.** When $limit = \text{True}$, the digit choices cannot exceed the corresponding bit of $n$; once a strictly smaller bit is chosen, $limit$ becomes $\text{False}$ and all subsequent bits are bounded only by the algebraic constraint.

---

## 3. Step-by-Step Worked Execution

We trace $n = 5$ ($101_2$):

---

### Step 1: Bit 2 (MSB)
- $n$'s bit is 1. Choices for $j$: $0$ or $1$.
- Choice $j = 0$:
  - $limit$ drops to `False`.
  - Generates all valid 2-bit numbers: $\{00, 01, 10\} \implies \mathbf{3}$ paths ($0, 1, 2$).
- Choice $j = 1$:
  - $limit$ stays `True`.
  - Recurse into bit 1 with $pre = 1$.

---

### Step 2: Bit 1
- $n$'s bit is 0. Since $limit$ is `True`, upper bound is $0$.
- Choice $j = 0$:
  - Valid because $pre = 1, j = 0$.
  - Recurse into bit 0 with $pre = 0, limit = \text{True}$.

---

### Step 3: Bit 0
- $n$'s bit is 1. Choices: $j = 0$ or $j = 1$.
  - $j = 0 \implies$ yields number $100_2 = 4$ ($\mathbf{1}$ path).
  - $j = 1 \implies$ yields number $101_2 = 5$ ($\mathbf{1}$ path).
- Sum for choice $j = 1$: $1 + 1 = \mathbf{2}$ paths.

---

### Step 4: Total Sum
$$
3 + 2 = \mathbf{5}
$$

---

## 4. Complete Execution Trace

| Call $(i, pre, limit)$ | Bit Position | Max Bit $up$ | Choices Considered | Pruned? | Sub-Paths Returned |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $dfs(2, 0, \text{True})$ | Bit 2 | $1$ | $j = 0, 1$ | None | $3 + 2 = \mathbf{5}$ |
| $dfs(1, 0, \text{False})$ | Bit 1 | $1$ | $j = 0, 1$ | None | $2 + 1 = 3$ |
| $dfs(0, 0, \text{False})$ | Bit 0 | $1$ | $j = 0, 1$ | None | $1 + 1 = 2$ |
| $dfs(0, 1, \text{False})$ | Bit 0 | $1$ | $j = 0$ ($j=1$ pruned) | $j=1$ (11) | $1$ |
| $dfs(1, 1, \text{True})$ | Bit 1 | $0$ | $j = 0$ | None | $2$ |
| $dfs(0, 0, \text{True})$ | Bit 0 | $1$ | $j = 0, 1$ | None | $1 + 1 = 2$ |
| **Result** | — | — | — | — | **`5`** |

---

## 5. Boundary Cases & Failure Modes

- **$n = 0$:** Single valid number $0 \implies \mathbf{1}$.
- **$n = 1$:** Valid numbers $0, 1 \implies \mathbf{2}$.
- **$n = 2$ ($10_2$):** Valid numbers $0, 1, 2 \implies \mathbf{3}$.
- **$n = 10^9$:** Bit length is $30$; evaluates $\le 30 \times 2 \times 2 = 120$ states.

---

## 6. Traps & Common Anti-Patterns

- **Brute Force Counting ($O(N)$):** Looping from 0 to $N$ checking `x & (x >> 1) == 0` causes TLE for $N = 10^9$. Digit DP runs in $O(\log N)$ time.
- **Forgetting the Zero Option ($0$ is Non-Negative):** The problem statement asks for *non-negative* integers in $[0, n]$, so $0$ must be included.
- **Miscalculating Bit Length:** Starting at an arbitrary fixed bit size (like 32) without leading zero tracking can introduce spurious consecutive zero branches. Starting from `n.bit_length() - 1` cleanly isolates the significant bits.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - The number of bits is $B = \lfloor \log_2 n \rfloor + 1 \le 31$.
  - State space: $i \in [0, B-1]$, $pre \in \{0, 1\}$, $limit \in \{0, 1\}$.
  - Distinct states: $31 \times 2 \times 2 = 124$ states.
  - Each state iterates over at most 2 binary choices taking $\mathcal{O}(1)$ time.
  - Total Time: $\mathcal{O}(\log N)$. Completes in $< 1$ ms for any 32-bit integer.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(\log N)$ space for the memoization cache table and recursion stack.
