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

### 4.1 What the Clearing Formula Returns for Every Small Input

The three traced cases are isolated points. Sweeping the first sixteen positive
integers shows that the formula is never ambiguous: the AND result after clearing
is exactly $n$ with its lowest set bit removed, which is a power of two precisely
when nothing remains.

| $n$ | $n - 1$ | $n \ \& \ (n - 1)$ | Lowest set bit value in $n$ | Set bits in $n$ | Is the AND result 0? | Decision |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 0 | 0 | 1 | 1 | Yes | `true` |
| 2 | 1 | 0 | 2 | 1 | Yes | `true` |
| 3 | 2 | 2 | 1 | 2 | No | `false` |
| 4 | 3 | 0 | 4 | 1 | Yes | `true` |
| 5 | 4 | 4 | 1 | 2 | No | `false` |
| 6 | 5 | 4 | 2 | 2 | No | `false` |
| 7 | 6 | 6 | 1 | 3 | No | `false` |
| 8 | 7 | 0 | 8 | 1 | Yes | `true` |
| 9 | 8 | 8 | 1 | 2 | No | `false` |
| 10 | 9 | 8 | 2 | 2 | No | `false` |
| 11 | 10 | 10 | 1 | 3 | No | `false` |
| 12 | 11 | 8 | 4 | 2 | No | `false` |
| 13 | 12 | 12 | 1 | 3 | No | `false` |
| 14 | 13 | 12 | 2 | 3 | No | `false` |
| 15 | 14 | 14 | 1 | 4 | No | `false` |
| 16 | 15 | 0 | 16 | 1 | Yes | `true` |

The rows with a single set bit are exactly the rows whose AND result is zero, and
they are exactly the powers of two. Row 12 is the instructive non-power: its
lowest set bit is worth 4, so clearing it leaves 8 rather than 0. Two claims from
the derivation are visible here at once. The cleared value is always
$n - (\text{lowest set bit})$, so the result is smaller than $n$ but never
negative for positive input, and the operation never touches any bit above the
lowest one.

### 4.2 Negative and Composite Boundaries

The positivity guard is a separate decision from the bit test, and this table
separates the two so that neither can be mistaken for the other.

| Input $n$ | Two's complement or binary form | $n - 1$ | $n \ \& \ (n - 1)$ | Bit test alone would say | Positivity guard says | Final decision |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | $(00000)_2$ | -1 | 0 | Accept, which is wrong: $2^x$ is never 0 | Reject | `false` |
| -16 | $(11110000)_2$ | -17 | -32 | Reject, since the result is non-zero | Reject | `false` |
| -2147483648 | $(1\underbrace{00\ldots0}_{31})_2$ | -2147483649 | -2147483648 | Reject, since the result is non-zero | Reject | `false` |
| 3 | $(00011)_2$ | 2 | 2 | Reject: two set bits | Accept | `false` |
| 48 | $(110000)_2$ | 47 | 32 | Reject: two set bits | Accept | `false` |

Row 1 is the single case where the bit test alone gives the wrong answer: zero
survives it because subtracting one produces an all-ones value whose AND with
zero is zero. The negative rows are not rescued by the bit test, because a
negative integer's lowest set bit is not its only set bit; only the guard
excludes them on principle. Rows 4 and 5 show the converse situation, where the
guard passes and the bit test is the one that rejects. Reading the table by
column, no single condition accepts every power of two and rejects everything
else, which is exactly why the answer is a conjunction rather than either test.

---

## 5. Algorithmic Correctness

**Soundness.** Let $n > 0$. Any positive integer $n$ can be expressed uniquely as $\sum_{i=0}^k b_i 2^i$ where $b_i \in \{0, 1\}$. $n$ is a power of two if and only if $\sum b_i = 1$. The operation $n \ \& \ (n - 1)$ clears the least significant 1-bit. If $\sum b_i = 1$, clearing it yields 0. If $\sum b_i \ge 2$, at least one 1-bit remains, yielding a non-zero value. Thus, $n > 0 \text{ and } (n \ \& \ (n - 1)) == 0 \iff n = 2^x$.

**Completeness.** Every 32-bit signed integer is tested. The condition strictly accepts all powers of two in $[1, 2^{30}]$ and rejects all non-powers, zero, and negative values.

---

## 6. Traps This Instance Exposes

- **Missing Positivity Check ($n = 0$):** In binary, $0 - 1 = -1 = (1111\dots 1)_2$. Computing $0 \ \& \ (-1) = 0$. Without `n > 0`, $n = 0$ would falsely return `true`!
- **Negative Powers Fallacy:** In two's complement, $-2147483648 = -2^{31}$ has binary representation `0x80000000`. Subtracting 1 in 32-bit unsigned arithmetic wraps, so without `n > 0`, negative numbers could produce false positives.
- **Operator Precedence in C/C++/Python:** Bitwise AND (`&`) has lower precedence than equality comparison (`==`). Writing `n & n - 1 == 0` evaluates as `n & (n - 1 == 0)`. Parentheses are mandatory: `(n & (n - 1)) == 0`.

### 6.1 Alternatives Compared on This Instance

| Approach | How it decides | Time | Auxiliary space | Tradeoff or failure mode |
|:---|:---|:---:|:---:|:---|
| Clear the lowest set bit and test for zero (traced above) | One subtraction and one AND | $O(1)$ | $O(1)$ | Chosen. No loop, no recursion, and no conversion; the positivity guard supplies the only case the bit test misses |
| Repeated halving while the remainder is zero | Divide by 2 until the value becomes odd | $O(\log n)$ | $O(1)$ | Correct, but it performs up to 31 iterations on this problem's domain and needs its own zero handling, since 0 is even forever |
| Popcount equals one | Count set bits and test the count | $O(1)$ to $O(\log n)$ | $O(1)$ | Equivalent in meaning, but a hardware popcount is not available in every target language, and a manual loop reintroduces the iteration cost |
| Isolate the lowest set bit with two's complement and compare with $n$ | Test whether $n \ \& \ -n$ equals $n$ | $O(1)$ | $O(1)$ | Correct for positive $n$, and the positivity guard is still required because the identity holds trivially at zero |
| Test the decimal last digit | Accept values ending in 2, 4, 6, or 8, plus 1 | $O(1)$ | $O(1)$ | Wrong. The last digit is not a function of the exponent: $2^{10} = 1024$ ends in 4 and $2^{12} = 4096$ ends in 6, so the pattern breaks after single digits |
| Floating-point logarithm | Test whether $\log_2 n$ is an integer | $O(1)$ | $O(1)$ | Wrong near the domain limits, where the logarithm of a large power of two rounds to a non-integer and rejects a valid input |

The first row is the only one that is simultaneously constant time, constant
space, integer-exact, and free of loop-boundary cases. The last two rows are the
traps: both look like constant-time arithmetic, and both fail because they reason
about a decimal or real-valued representation instead of the binary one that
actually defines the property.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$ constant time. A single subtraction, bitwise AND, and comparison are executed in 1 CPU cycle.
- **Auxiliary Space Complexity:** $O(1)$ constant memory.
