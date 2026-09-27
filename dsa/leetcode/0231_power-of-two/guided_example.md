# Guided Example: Power of Two

We trace the step-by-step bitwise low-bit clearing, binary representation invariants, and non-positive boundary guards on representative integer inputs:

- **Input:** $n = 1$
- **Required output:** `true` ($1 = 2^0$, binary $(0001)_2$)
- **Positive Power of Two:** $n = 16 \implies \text{true}$ ($16 = 2^4$, binary $(10000)_2$)
- **Composite Non-Power of Two:** $n = 12 \implies \text{false}$ (Binary $(1100)_2$; has 2 set bits)
- **Zero Input Boundary:** $n = 0 \implies \text{false}$ (Guards against $0 \ \& \ -1 = 0$)
- **Negative Extreme Boundary:** $n = -2147483648 \implies \text{false}$ (Negative minimum has single sign-bit in 2's complement)

This instance demonstrates constant-time arithmetic verification without loops or recursion ($O(1)$ time), proves the lowest-set-bit elimination identity ($n \ \& \ (n - 1) == 0$), explains why the positivity guard ($n > 0$) is mathematically essential, and compares bitwise AND with two's complement isolation ($n \ \& \ -n == n$).

---

## 1. Instance & Teaching Goal

Given a 32-bit signed integer $n$, determine whether there exists an integer $x \ge 0$ such that:
$$
n = 2^x
$$
A loop-based approach repeatedly divides $n$ by 2 while $n \% 2 == 0$, taking $O(\log n)$ iterations.
The optimal bit manipulation approach evaluates the mathematical truth in **a single processor instruction ($O(1)$ time)** without loops, recursion, or floating-point conversions.

### Binary Structure of Powers of Two
In base-2 binary positional notation:
- $2^0 = 1 = (00001)_2$ (Bit 0 set)
- $2^1 = 2 = (00010)_2$ (Bit 1 set)
- $2^2 = 4 = (00100)_2$ (Bit 2 set)
- $2^3 = 8 = (01000)_2$ (Bit 3 set)
- $2^4 = 16 = (10000)_2$ (Bit 4 set)

**Fundamental Theorem:** A positive integer $n$ is an exact power of two **if and only if its binary representation contains exactly one set bit (`1`)**!

---

## 2. Conceptual Foundation & Invariants

### The Lowest-Set-Bit Clearing Formula: $n \ \& \ (n - 1)$
Consider any positive binary integer $n$:
Let the position of the least significant set bit be $k$.
All bits to the right of $k$ are `0`.
When subtracting $1$ from $n$:
- Borrowing cascades down to position $k$.
- The bit at position $k$ flips from `1` to `0`.
- All bits to the right of position $k$ flip from `0` to `1`.
- All bits to the left of position $k$ remain unchanged.

When we perform bitwise AND:
$$
n \ \& \ (n - 1)
$$
- Bits to the left of $k$ are unchanged in both $\implies$ preserved.
- Bit $k$ is `1` in $n$ and `0` in $n - 1 \implies$ becomes `0`.
- Bits to the right of $k$ are `0` in $n$ and `1` in $n - 1 \implies$ become `0`.

**Result:** The expression $n \ \& \ (n - 1)$ **clears precisely the lowest set bit of $n$**, leaving all other bits intact!

### The Power-of-Two Invariant:
1. If $n$ is a positive power of two, it has **only one set bit**. Clearing that bit leaves **all zeroes**:
   $$
   n \ \& \ (n - 1) == 0
   $$
2. If $n$ is not a power of two, it has **at least two set bits**. Clearing the lowest bit leaves the higher set bit(s) intact:
   $$
   n \ \& \ (n - 1) \ne 0
   $$
3. **The Positivity Guard:**
   If $n = 0$: $0 \ \& \ (-1) = 0$, but $0$ is not a power of two!
   If $n \le 0$: $n$ cannot be a positive power of two.
   Therefore, the full necessary and sufficient condition is:
   $$
   n > 0 \quad \text{and} \quad (n \ \& \ (n - 1)) == 0
   $$

---

## 3. Step-by-Step Worked Execution

We trace the evaluation across three representative numbers:

### Case 1: $n = 1$ ($2^0$)
1. Positivity check:
   $$
   n > 0 \implies 1 > 0 \quad (\text{True})
   $$
2. Binary representation:
   $$
   n = 1 = (0001)_2
   $$
   $$
   n - 1 = 0 = (0000)_2
   $$
3. Bitwise AND:
   $$
   n \ \& \ (n - 1) = (0001)_2 \ \& \ (0000)_2 = (0000)_2 = 0
   $$
4. Check equality with 0: $0 == 0$ ($\text{True}$).
5. Both conditions hold $\implies \mathbf{\text{true}}$.

---

### Case 2: $n = 16$ ($2^4$)
1. Positivity check: $16 > 0$ ($\text{True}$).
2. Binary representations:
   $$
   n = 16 = (10000)_2
   $$
   $$
   n - 1 = 15 = (01111)_2
   $$
3. Bitwise AND:
   $$
   \begin{aligned}
   16 &= 1 \ 0 \ 0 \ 0 \ 0_2 \\
   15 &= 0 \ 1 \ 1 \ 1 \ 1_2 \\
   \hline
   16 \ \& \ 15 &= 0 \ 0 \ 0 \ 0 \ 0_2 = 0
   \end{aligned}
   $$
4. $0 == 0$ ($\text{True}$) $\implies \mathbf{\text{true}}$.

---

### Case 3: $n = 12$ ($2^3 + 2^2$, Not a Power of Two)
1. Positivity check: $12 > 0$ ($\text{True}$).
2. Binary representations:
   $$
   n = 12 = (1100)_2
   $$
   $$
   n - 1 = 11 = (1011)_2
   $$
3. Bitwise AND:
   $$
   \begin{aligned}
   12 &= 1 \ 1 \ 0 \ 0_2 \\
   11 &= 1 \ 0 \ 1 \ 1_2 \\
   \hline
   12 \ \& \ 11 &= 1 \ 0 \ 0 \ 0_2 = 8 \ne 0
   \end{aligned}
   $$
4. Check equality: $8 == 0$ ($\text{False}$).
5. Condition fails $\implies \mathbf{\text{false}}$.

---

## 4. Complete Execution Trace

```text
n = 1:  1 > 0 (T), 1 & 0 = 0 == 0 (T)  -> TRUE
n = 16: 16 > 0 (T), 16 & 15 = 0 == 0 (T) -> TRUE
n = 12: 12 > 0 (T), 12 & 11 = 8 != 0 (F) -> FALSE
n = 0:  0 > 0 (F)                      -> FALSE
n = -16: -16 > 0 (F)                   -> FALSE
```

| Input $n$ | Positivity Check $n > 0$ | Binary of $n$ | Binary of $n - 1$ | Bitwise $n \ \& \ (n - 1)$ | Equal to 0? | Final Decision |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | **True** ($1 > 0$) | $(00001)_2$ | $(00000)_2$ | $0$ | **Yes** | **`true`** |
| **16** | **True** ($16 > 0$) | $(10000)_2$ | $(01111)_2$ | $0$ | **Yes** | **`true`** |
| **12** | **True** ($12 > 0$) | $(01100)_2$ | $(01011)_2$ | $8 = (01000)_2$ | No | **`false`** |
| **0** | **False** ($0 \not> 0$) | $(00000)_2$ | - | - | - | **`false`** |
| **-16** | **False** ($-16 \not> 0$) | $(10000)_2$ | - | - | - | **`false`** |

---

## 5. Algorithmic Correctness

**Soundness.** Let $n > 0$. Any positive integer $n$ can be expressed uniquely as $\sum_{i=0}^k b_i 2^i$ where $b_i \in \{0, 1\}$. $n$ is a power of two if and only if $\sum b_i = 1$. The operation $n \ \& \ (n - 1)$ clears the least significant 1-bit. If $\sum b_i = 1$, clearing it yields 0. If $\sum b_i \ge 2$, at least one 1-bit remains, yielding a non-zero value. Thus, $n > 0 \text{ and } (n \ \& \ (n - 1)) == 0 \iff n = 2^x$.

**Completeness.** Every 32-bit signed integer is tested. The condition strictly accepts all powers of two in $[1, 2^{30}]$ and rejects all non-powers, zero, and negative values.

---

## 6. Traps This Instance Exposes

- **Missing Positivity Check ($n = 0$):** In binary, $0 - 1 = -1 = (1111\dots 1)_2$. Computing $0 \ \& \ (-1) = 0$. Without `n > 0`, $n = 0$ would falsely return `true`!
- **Negative Powers Fallacy:** In two's complement, $-2147483648 = -2^{31}$ has binary representation `0x80000000`. Subtracting 1 in 32-bit unsigned arithmetic wraps, so without `n > 0`, negative numbers could produce false positives.
- **Operator Precedence in C/C++/Python:** Bitwise AND (`&`) has lower precedence than equality comparison (`==`). Writing `n & n - 1 == 0` evaluates as `n & (n - 1 == 0)`. Parentheses are mandatory: `(n & (n - 1)) == 0`.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$ constant time. A single subtraction, bitwise AND, and comparison are executed in 1 CPU cycle.
- **Auxiliary Space Complexity:** $O(1)$ constant memory.
