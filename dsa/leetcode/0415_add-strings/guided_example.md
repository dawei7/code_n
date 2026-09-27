# Guided Example: Add Strings

We trace the step-by-step column-by-column decimal full-adder addition, backward two-pointer traversal, base-10 digit splitting ($\text{divmod}(a + b + c, 10)$), and carry propagation on representative big-integer strings:

- **Input:** $num1 = \text{"456"}, \quad num2 = \text{"77"}$
- **Required output:** `"533"`
  - Pointers start at least significant digits:
    - $i = |num1| - 1 = 2 \quad (num1[2] = \text{'6'})$
    - $j = |num2| - 1 = 1 \quad (num2[1] = \text{'7'})$
    - Carry: $c = 0$
  - Column 0 ($10^0$, Units):
    - Digits: $a = 6, b = 7, c = 0$
    - Sum: $6 + 7 + 0 = 13$
    - Carry: $c \leftarrow \lfloor 13 / 10 \rfloor = 1$
    - Current digit: $v = 13 \bmod 10 = 3$
    - Emitted digit: `'3'`
  - Column 1 ($10^1$, Tens):
    - Digits: $a = 5, b = 7, c = 1$
    - Sum: $5 + 7 + 1 = 13$
    - Carry: $c \leftarrow \lfloor 13 / 10 \rfloor = 1$
    - Current digit: $v = 13 \bmod 10 = 3$
    - Emitted digit: `'3'`
  - Column 2 ($10^2$, Hundreds):
    - Digits: $a = 4, b = 0$ (exhausted), $c = 1$
    - Sum: $4 + 0 + 1 = 5$
    - Carry: $c \leftarrow \lfloor 5 / 10 \rfloor = 0$
    - Current digit: $v = 5 \bmod 10 = 5$
    - Emitted digit: `'5'`
  - Final assembly:
    - Reverse emitted digits: `'3', '3', '5'` reversed is `"533"`.
- **Leading Carry Expansion:** $num1 = \text{"99"}, num2 = \text{"1"} \implies 9+1=10 \to 9+1=10 \to$ final carry $1 \implies \text{"100"}$
- **Zero Addition:** $num1 = \text{"0"}, num2 = \text{"0"} \implies \text{"0"}$

This instance demonstrates simulating base-10 positional arithmetic on arbitrary-precision strings without using native big-integer conversions, deriving $O(\max(M, N))$ runtime and $O(\max(M, N))$ space bounds.

---

## 1. Instance & Teaching Goal

Given two non-negative integers represented as strings $num1 = \text{"456"}$ and $num2 = \text{"77"}$:
Calculate the sum of $num1$ and $num2$ as a string, without converting the inputs directly to integers or using built-in big-integer libraries:

```text
Align by Place Value (Right-to-Left):

       [Carry: 1  1  0]
  num1:        4  5  6
+ num2:           7  7
-----------------------
  Sum:         5  3  3
```

### The Big-Integer Addition Rule
Because integers in string form can be arbitrarily large (exceeding standard 64-bit primitive integer limits), addition must process the digits column by column from the least significant digit (rightmost) to the most significant digit (leftmost), maintaining a running **carry** bit $c \in \{0, 1\}$.

---

## 2. Conceptual Foundation & Invariants

### 1. The Decimal Full-Adder Equations:
At place value index $k$:
- Let $a$ be the digit from $num1$ (or $0$ if $num1$ is exhausted).
- Let $b$ be the digit from $num2$ (or $0$ if $num2$ is exhausted).
- Let $c_{in}$ be the incoming carry ($0$ or $1$).
The column sum is:
$$
S = a + b + c_{in}
$$
The value written to the current place is:
$$
v = S \bmod 10
$$
The outgoing carry to the next column is:
$$
c_{out} = \lfloor S / 10 \rfloor
$$

### 2. Termination Condition:
The addition loop continues as long as:
$$
(i \ge 0) \lor (j \ge 0) \lor (c > 0)
$$
Even if both strings have been completely traversed ($i < 0$ and $j < 0$), an outstanding carry ($c = 1$) must still be emitted as the most significant digit.

> **Invariant.** At the start of processing column $k$, the collected prefix of emitted digits represents the exact mathematical sum of the least-significant $k$ digits of $num1$ and $num2$, plus $c \times 10^k$.

---

## 3. Step-by-Step Worked Execution

We trace $num1 = \text{"456"}$ ($M = 3$), $num2 = \text{"77"}$ ($N = 2$):
Initialize pointers $i = 2, j = 1$, carry $c = 0$, buffer `digits = []`.

---

### Step 1: Units Column ($10^0$)
- Pointers: $i = 2 \implies num1[2] = \text{'6'}$, $j = 1 \implies num2[1] = \text{'7'}$.
- Digits: $a = 6, b = 7$.
- Calculate:
  $$
  S = 6 + 7 + 0 = \mathbf{13}
  $$
  $$
  v = 13 \bmod 10 = \mathbf{3}, \quad c \leftarrow \lfloor 13 / 10 \rfloor = \mathbf{1}
  $$
- Append `'3'` to buffer: `['3']`.
- Advance pointers: $i \leftarrow 1, j \leftarrow 0$.

---

### Step 2: Tens Column ($10^1$)
- Pointers: $i = 1 \implies num1[1] = \text{'5'}$, $j = 0 \implies num2[0] = \text{'7'}$.
- Digits: $a = 5, b = 7$, incoming carry $c = 1$.
- Calculate:
  $$
  S = 5 + 7 + 1 = \mathbf{13}
  $$
  $$
  v = 13 \bmod 10 = \mathbf{3}, \quad c \leftarrow \lfloor 13 / 10 \rfloor = \mathbf{1}
  $$
- Append `'3'` to buffer: `['3', '3']`.
- Advance pointers: $i \leftarrow 0, j \leftarrow -1$.

---

### Step 3: Hundreds Column ($10^2$)
- Pointers: $i = 0 \implies num1[0] = \text{'4'}$, $j = -1 \implies$ string exhausted, $b = 0$.
- Digits: $a = 4, b = 0$, incoming carry $c = 1$.
- Calculate:
  $$
  S = 4 + 0 + 1 = \mathbf{5}
  $$
  $$
  v = 5 \bmod 10 = \mathbf{5}, \quad c \leftarrow \lfloor 5 / 10 \rfloor = \mathbf{0}
  $$
- Append `'5'` to buffer: `['3', '3', '5']`.
- Advance pointers: $i \leftarrow -1, j \leftarrow -2$.

---

### Step 4: Loop Exit & Reversal
- Check condition: $i = -1 < 0$, $j = -2 < 0$, $c = 0$.
- Loop terminates.
- Reverse buffer:
  $$
  [\text{'3'}, \text{'3'}, \text{'5'}] \xrightarrow{\text{Reverse}} [\text{'5'}, \text{'3'}, \text{'3'}] \implies \text{"533"}
  $$

---

## 4. Complete Execution Trace

| Column | Place Value | Pointer $i$ ($num1[i]$) | Pointer $j$ ($num2[j]$) | Incoming Carry $c$ | Column Sum $S = a + b + c$ | Written Digit $S \bmod 10$ | Outgoing Carry $\lfloor S/10 \rfloor$ | Accumulated Reversed Buffer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **Init** | — | $2$ | $1$ | $0$ | — | — | — | `[]` |
| **1** | $10^0$ (Units) | $2$ (`'6'`) | $1$ (`'7'`) | $0$ | $6 + 7 + 0 = 13$ | **`3`** | **`1`** | `['3']` |
| **2** | $10^1$ (Tens) | $1$ (`'5'`) | $0$ (`'7'`) | $1$ | $5 + 7 + 1 = 13$ | **`3`** | **`1`** | `['3', '3']` |
| **3** | $10^2$ (Hundreds) | $0$ (`'4'`) | $-1$ (`0`) | $1$ | $4 + 0 + 1 = 5$ | **`5`** | **`0`** | `['3', '3', '5']` |
| **Done** | — | $-1$ | $-2$ | $0$ | — | — | — | **Reversed: `"533"`** |

---

## 5. Boundary Cases & Failure Modes

- **Unequal Lengths ($num1 = \text{"11"}, num2 = \text{"123"}$):** Shorter string exhausts earlier. Safe fallback evaluates missing digits as $0$ without null-pointer exceptions. Result: `"134"`.
- **Final Carry Overflow ($num1 = \text{"99"}, num2 = \text{"1"}$):** Both $i$ and $j$ reach $-1$, but $c = 1$. The loop condition `c > 0` triggers an extra iteration, emitting `'1'` and expanding output length to 3 digits (`"100"`).
- **Both Zeroes ($num1 = \text{"0"}, num2 = \text{"0"}$):** Single iteration evaluates $0 + 0 + 0 = 0$, emitting `"0"`. No invalid empty string or multiple leading zeros.
- **Large Inputs ($|num1|, |num2| \le 10^4$):** Because addition operates in linear time and appends to a mutable list, performance is instantaneous and does not suffer from quadratic string reallocation costs.

---

## 6. Traps & Common Anti-Patterns

- **Direct String Prepends:** Writing `ans = str(v) + ans` inside the loop causes $O(K^2)$ quadratic runtime due to repeated memory allocations for strings of length $1, 2, \dots, K$. Appending to a list and reversing once at the end guarantees strict $O(K)$ linear time.
- **Premature Loop Termination:** Writing `while i >= 0 and j >= 0` terminates as soon as the shorter string runs out, dropping the higher place values of the longer number.
- **Dropping the Final Carry:** Omitting `or c` from the loop condition misses the overflow digit in cases like `"99" + "1"`, yielding `"00"` instead of `"100"`.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $M = |num1|$ and $N = |num2|$.
  - The loop runs for $\max(M, N) + 1$ iterations.
  - In each iteration, digit lookup, modular arithmetic, and list appending take $O(1)$ time.
  - Final array reversal takes $O(\max(M, N))$ time.
  - Total Time: $\mathcal{O}(\max(M, N))$.
- **Auxiliary Space Complexity:**
  - The list buffer stores $\max(M, N) + 1$ characters.
  - Total Auxiliary Space: $\mathcal{O}(\max(M, N))$ to construct the resulting string.
