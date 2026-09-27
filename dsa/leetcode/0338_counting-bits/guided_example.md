# Guided Example: Counting Bits

We trace the step-by-step binary representation bit counting, bitwise right-shift recurrence ($ans[i] = ans[i \gg 1] + (i \ \& \ 1)$), lowest set-bit elimination ($ans[i] = ans[i \ \& \ (i - 1)] + 1$), and built-in popcount vector generation on representative integer ranges:

- **Input:** $n = 5$
- **Required output:** $[0, 1, 1, 2, 1, 2]$
  - Binary representations:
    - $0 = 000_2 \implies 0$ ones
    - $1 = 001_2 \implies 1$ one
    - $2 = 010_2 \implies 1$ one
    - $3 = 011_2 \implies 2$ ones
    - $4 = 100_2 \implies 1$ one
    - $5 = 101_2 \implies 2$ ones
  - Output array: $[0, 1, 1, 2, 1, 2]$ (Length $n + 1 = 6$)
- **Base Case $n = 2$:** $n = 2 \implies [0, 1, 1]$
- **Zero Base Case:** $n = 0 \implies [0]$
- **Power of Two Instances:** Any power of two $2^k$ has exactly $1$ set bit ($[1, 2, 4, 8, 16] \implies 1$)

This instance demonstrates bit manipulation dynamic programming recurrences, mathematically proves why shifting right drops the least significant bit while preserving higher-order popcount, contrasts naive $O(N \log N)$ independent bit checks with optimal $O(N)$ single-pass transitions, and analyzes $O(N)$ return array space bounds.

---

## 1. Instance & Teaching Goal

Given an integer $n = 5$:
Return an array $ans$ of length $n + 1 = 6$ such that for each $i \in [0, 5]$, $ans[i]$ is the number of $1$'s in the binary representation of $i$:

```text
Integers 0 through 5:
i = 0:  000_2 -> Popcount: 0
i = 1:  001_2 -> Popcount: 1
i = 2:  010_2 -> Popcount: 1
i = 3:  011_2 -> Popcount: 2
i = 4:  100_2 -> Popcount: 1
i = 5:  101_2 -> Popcount: 2

Result Array: [0, 1, 1, 2, 1, 2]
```

### The Inefficiencies of Naive Loop Counting
- Checking each bit of each number $i$ individually takes $O(\log i) = O(\log N)$ work per number, totaling $O(N \log N)$ across the range.
- Python's optimized `int.bit_count()` performs hardware-accelerated population count instructions (such as `POPCNT` on x86-64) in $O(1)$ operations per integer, computing the entire array in $O(N)$ time.

---

## 2. Conceptual Foundation & Invariants

### 1. The Right-Shift Bit Recurrence
For any positive integer $i$:
- $i \gg 1$ divides $i$ by 2 (dropping its least significant bit).
- $i \ \& \ 1$ extracts the least significant bit ($1$ if $i$ is odd, $0$ if $i$ is even).
- Therefore, the total number of set bits in $i$ is:
  $$
  ans[i] = ans[i \gg 1] + (i \ \& \ 1)
  $$
- Base case: $ans[0] = 0$.

### 2. Alternative Brian Kernighan Recurrence
Clearing the lowest set bit using $i \ \& \ (i - 1)$:
$$
ans[i] = ans[i \ \& \ (i - 1)] + 1
$$
Both recurrences compute $ans[i]$ in $O(1)$ time by referencing an already computed smaller subproblem!

> **Invariant.** For every integer $i \in [0, n]$, $ans[i]$ stores the exact Hamming weight (number of active set bits) of $i$.

---

## 3. Step-by-Step Worked Execution

We trace the recurrence $ans[i] = ans[i \gg 1] + (i \ \& \ 1)$ on $n = 5$:

---

### Step 1: Base Case $i = 0$
- Binary: $0_2$.
- $ans[0] = \mathbf{0}$.

---

### Step 2: $i = 1$
- Shift: $1 \gg 1 = 0$.
- Parity: $1 \ \& \ 1 = 1$.
- Transition:
  $$
  ans[1] = ans[0] + 1 = 0 + 1 = \mathbf{1}
  $$

---

### Step 3: $i = 2$
- Shift: $2 \gg 1 = 1$.
- Parity: $2 \ \& \ 1 = 0$.
- Transition:
  $$
  ans[2] = ans[1] + 0 = 1 + 0 = \mathbf{1}
  $$

---

### Step 4: $i = 3$
- Shift: $3 \gg 1 = 1$.
- Parity: $3 \ \& \ 1 = 1$.
- Transition:
  $$
  ans[3] = ans[1] + 1 = 1 + 1 = \mathbf{2}
  $$

---

### Step 5: $i = 4$
- Shift: $4 \gg 1 = 2$.
- Parity: $4 \ \& \ 1 = 0$.
- Transition:
  $$
  ans[4] = ans[2] + 0 = 1 + 0 = \mathbf{1}
  $$

---

### Step 6: $i = 5$
- Shift: $5 \gg 1 = 2$.
- Parity: $5 \ \& \ 1 = 1$.
- Transition:
  $$
  ans[5] = ans[2] + 1 = 1 + 1 = \mathbf{2}
  $$

---

### Final Array
$$
ans = \mathbf{[0, 1, 1, 2, 1, 2]}
$$

---

## 4. Complete Execution Trace

```text
n = 5
ans = [0, 0, 0, 0, 0, 0]

ans[0] = 0
ans[1] = ans[0] + 1 = 0 + 1 = 1
ans[2] = ans[1] + 0 = 1 + 0 = 1
ans[3] = ans[1] + 1 = 1 + 1 = 2
ans[4] = ans[2] + 0 = 1 + 0 = 1
ans[5] = ans[2] + 1 = 1 + 1 = 2

Output: [0, 1, 1, 2, 1, 2]
```

| Integer $i$ | Binary Representation | Shifted Integer $i \gg 1$ | Prior Count $ans[i \gg 1]$ | Parity Bit $i \ \& \ 1$ | Recurrence: $ans[i \gg 1] + (i \ \& \ 1)$ | Output $ans[i]$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | $0_2$ | - | - | - | Base Case | 0 |
| 1 | $1_2$ | 0 | 0 | 1 | $0 + 1$ | 1 |
| 2 | $10_2$ | 1 | 1 | 0 | $1 + 0$ | 1 |
| 3 | $11_2$ | 1 | 1 | 1 | $1 + 1$ | 2 |
| 4 | $100_2$ | 2 | 1 | 0 | $1 + 0$ | 1 |
| 5 | $101_2$ | 2 | 1 | 1 | $1 + 1$ | 2 |

---

## 5. Algorithmic Correctness

**Soundness.** Any non-negative integer $i$ has binary representation $b_k b_{k-1} \dots b_1 b_0$. Shifting right by 1 bit removes $b_0$, yielding integer $i \gg 1$ with binary representation $b_k \dots b_1$. The number of set bits in $i$ is precisely the number of set bits in $i \gg 1$ plus $b_0 = i \ \& \ 1$. Because $i \gg 1 < i$ for all $i \ge 1$, the dependency is always precomputed.

**Completeness.** The evaluation iterates through all integers from $0$ to $n$ inclusive in strictly ascending order. Every index in the return array of length $n + 1$ is populated with its mathematically proven set-bit count.

---

## 6. Traps This Instance Exposes

- **Array Sizing Off-By-One:** The range requires values from $0$ up to $n$ inclusive. The output array must have length $n + 1$, not $n$.
- **Bitwise Precedence Trap:** In Python, addition has higher precedence than bitwise AND (`+` precedes `&`). Expressions like `ans[i >> 1] + i & 1` evaluate as `(ans[i >> 1] + i) & 1`, producing incorrect results unless parenthesized as `ans[i >> 1] + (i & 1)`.
- **Topological Evaluation Order:** Recurrences referencing $i \gg 1$ or $i \ \& \ (i - 1)$ require that smaller integers are computed before larger integers, which is satisfied by linear iteration $0 \to n$.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N = n$. Each of the $N + 1$ entries is computed in $O(1)$ bitwise and arithmetic operations (or single hardware `POPCNT` instruction).
- **Auxiliary Space Complexity:** $O(1)$ auxiliary space beyond the required $O(N)$ output array.
