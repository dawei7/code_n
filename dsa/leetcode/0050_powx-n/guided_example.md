# Guided Example: Pow(x, n)

We trace the step-by-step execution of binary exponentiation (exponentiation by squaring) on representative positive and negative exponent instances:

- **Positive Exponent:** $x = 2.0, n = 10 \implies 1024.0$
- **Negative Exponent:** $x = 2.0, n = -2 \implies 0.25$

This instance demonstrates binary exponent decomposition, repeated squaring of the base ($x^{2^k}$), bitwise shifting of the exponent ($n \gg 1$), handling negative exponents via reciprocals ($x \leftarrow 1/x$), and 32-bit signed integer boundary considerations.

---

## 1. Instance & Teaching Goal

Given a floating-point base $x = 2.0$ and an integer exponent $n = 10$, compute $x^n$.

A naive linear multiplication computes $2.0 \times 2.0 \times \dots \times 2.0$ in $O(n)$ time. When $n = 2^{31} - 1 \approx 2.14 \times 10^9$, a linear loop takes billions of operations and times out.

Binary exponentiation observes that any integer $n$ can be expressed uniquely as a sum of powers of two (its binary representation):
$$
10 = (1010)_2 = 2^3 + 2^1 = 8 + 2
$$
Therefore:
$$
x^{10} = x^8 \cdot x^2 = (2.0)^8 \cdot (2.0)^2 = 256.0 \cdot 4.0 = 1024.0
$$
By repeatedly squaring the base ($x, x^2, x^4, x^8, \dots$), we compute $x^n$ in only $O(\log n)$ multiplications.

---

## 2. Conceptual Foundation & Invariants

### Binary Exponentiation Recurrence
For any base $x$ and integer $n \ge 0$:
$$
x^n =
\begin{cases}
1.0 & \text{if } n = 0 \\
(x^2)^{n/2} & \text{if } n \text{ is even} \\
x \cdot (x^2)^{(n-1)/2} & \text{if } n \text{ is odd}
\end{cases}
$$

### Iterative Algorithm Formulation
1. **Handle Negative Powers:**
   If $n < 0$:
   $$
   x \leftarrow \frac{1.0}{x}, \quad n \leftarrow -n
   $$
2. **Bitwise Extraction:**
   Initialize accumulator $\text{res} = 1.0$ and base tracker $\text{base} = x$.
   While $n > 0$:
   - If the least significant bit is set ($n \ \& \ 1 == 1$):
     $$
     \text{res} \leftarrow \text{res} \cdot \text{base}
     $$
   - Square the base for the next bit position:
     $$
     \text{base} \leftarrow \text{base} \cdot \text{base}
     $$
   - Shift exponent right:
     $$
     n \leftarrow n \gg 1
     $$

> **Invariant.** At the start of each iteration, $\text{res} \cdot \text{base}^n = x^{n_{\text{initial}}}$. As $n \to 0$, $\text{res}$ converges to the exact value of $x^{n_{\text{initial}}}$.

---

## 3. Step-by-Step Worked Execution

We trace $x = 2.0, n = 10$:

### Initialization
- $\text{res} = 1.0$
- $\text{base} = 2.0$ ($x^{2^0} = x^1$)
- $n = 10 = (1010)_2$

---

### Step 1: Bit 0 ($n = 10$)
- Exponent binary status: $10 \ \& \ 1 = 0$ (Even).
- Action: Bit is 0; do not multiply into $\text{res}$. $\text{res} = 1.0$.
- Square base: $\text{base} \leftarrow 2.0 \times 2.0 = 4.0$ ($x^{2^1} = x^2$).
- Shift exponent: $n \leftarrow \lfloor 10 / 2 \rfloor = 5$.

---

### Step 2: Bit 1 ($n = 5$)
- Exponent binary status: $5 \ \& \ 1 = 1$ (Odd).
- Action: Bit is 1; include current base into accumulator:
  $$
  \text{res} \leftarrow \text{res} \cdot \text{base} = 1.0 \times 4.0 = 4.0
  $$
- Square base: $\text{base} \leftarrow 4.0 \times 4.0 = 16.0$ ($x^{2^2} = x^4$).
- Shift exponent: $n \leftarrow \lfloor 5 / 2 \rfloor = 2$.

---

### Step 3: Bit 2 ($n = 2$)
- Exponent binary status: $2 \ \& \ 1 = 0$ (Even).
- Action: Bit is 0; $\text{res}$ remains $4.0$.
- Square base: $\text{base} \leftarrow 16.0 \times 16.0 = 256.0$ ($x^{2^3} = x^8$).
- Shift exponent: $n \leftarrow \lfloor 2 / 2 \rfloor = 1$.

---

### Step 4: Bit 3 ($n = 1$)
- Exponent binary status: $1 \ \& \ 1 = 1$ (Odd).
- Action: Bit is 1; include current base:
  $$
  \text{res} \leftarrow \text{res} \cdot \text{base} = 4.0 \times 256.0 = 1024.0
  $$
- Square base: $\text{base} \leftarrow 256.0 \times 256.0 = 65536.0$.
- Shift exponent: $n \leftarrow \lfloor 1 / 2 \rfloor = 0$.

---

### Step 5: Termination
- $n = 0$. Loop terminates.
- Emitted output: $1024.0$.

---

## 4. Complete Execution Trace

| Iteration | Exponent $n$ (Decimal) | Exponent $n$ (Binary) | Low Bit $n \ \& \ 1$ | Current $\text{base}$ Value ($x^{2^k}$) | Action on Accumulator | Accumulator $\text{res}$ |
|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Start | 10 | `1010` | - | $2.0$ ($2^1$) | Initial state | $1.0$ |
| 1 | 10 | `1010` | 0 | $2.0$ | Bit is 0; skip multiply | $1.0$ |
| 2 | 5 | `101` | **1** | $4.0$ ($2^2$) | Multiply $\text{res} \times 4.0$ | **$4.0$** |
| 3 | 2 | `10` | 0 | $16.0$ ($2^4$) | Bit is 0; skip multiply | $4.0$ |
| 4 | 1 | `1` | **1** | $256.0$ ($2^8$) | Multiply $\text{res} \times 256.0$ | **$1024.0$** |
| End | 0 | `0` | - | - | $n = 0 \implies$ Exit loop | **$1024.0$** |

### Negative Exponent Trace ($x = 2.0, n = -2$)
1. Negative sign detected: $x \leftarrow 1 / 2.0 = 0.5$, $n \leftarrow -(-2) = 2$.
2. Step 1 ($n = 2$): low bit 0, $\text{base} \leftarrow 0.5^2 = 0.25$, $n \leftarrow 1$.
3. Step 2 ($n = 1$): low bit 1, $\text{res} \leftarrow 1.0 \times 0.25 = 0.25$, $n \leftarrow 0$.
4. Result: $0.25$.

### Negative Exponent Trace as a Table

The reciprocal is applied once, before the loop begins, so the negative-exponent run needs only two iterations. The exponent is now $|n| = 2$, whose binary form `10` has a single set bit, and that bit is not the lowest one.

| Iteration | Working base | Exponent $n$ | Low bit $n \ \& \ 1$ | $\text{base} = x^{2^k}$ | Accumulator $\text{res}$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Start | $0.5$ | 2 | - | $0.5$ | $1.0$ |
| 1 ($k = 0$) | $0.5$ | 2 (`10`) | 0 | $1.0 \to 0.5 \times 0.5 = 0.25$ after squaring | $1.0$ (bit is 0, so nothing is multiplied in) |
| 2 ($k = 1$) | $0.5$ | 1 (`1`) | **1** | $0.0625$ after squaring | $1.0 \times 0.25 = \mathbf{0.25}$ |
| End | - | 0 | - | - | $\mathbf{0.25}$ |

The mirror-image route — compute $2.0^{2} = 4.0$ first and divide once at the very end, $1.0 / 4.0$ — lands on the same $0.25$. Both routes are arithmetically equivalent, but they place the reciprocal at opposite ends of the computation: this lesson inverts the base first so that the loop body needs no post-processing at all.

---

## 5. Algorithmic Correctness

**Soundness.** Let $n = \sum_{k=0}^M b_k 2^k$ where $b_k \in \{0, 1\}$. By algebraic laws of exponents:
$$
x^n = x^{\sum b_k 2^k} = \prod_{k=0}^M (x^{2^k})^{b_k}
$$
The loop computes $x^{2^k}$ at step $k$ and multiplies it into $\text{res}$ if and only if $b_k = 1$. When the loop terminates, $\text{res}$ exactly equals $x^n$.

**Completeness.** Dividing $n$ by 2 strictly reduces the exponent. The loop executes exactly $\lfloor \log_2 n \rfloor + 1$ iterations, guaranteeing termination.

---

## 6. Traps This Instance Exposes

- **32-bit Integer Overflow for $n = -2^{31}$:** In systems with 32-bit signed integers (C++/Java), the range is $[-2147483648, 2147483647]$. Direct negation $-n$ of $-2^{31}$ overflows $2^{31}-1$. Casting $n$ to a 64-bit integer (`long long`) or using Python's arbitrary-precision integers avoids overflow.
- **Base Inversion vs Final Division:** Either invert the base at the start ($x \leftarrow 1/x, n \leftarrow -n$) or compute $x^{|n|}$ and return $1.0 / \text{res}$ at the end. Both are mathematically equivalent, but inverting upfront maintains identical loop logic.
- **Zero Base with Non-Positive Exponent:** $0^0$ is defined as $1.0$, while $0^{-k}$ would divide by zero. LeetCode constraints guarantee valid domain inputs ($x \ne 0$ when $n < 0$).

### Boundary Cases at the Exponent Limits

| Boundary scenario | Input | Required result | How the bit scan reaches it |
|:---|:---|:---|:---|
| Zero exponent | $x = -7.5$, $n = 0$ | $1.0$ | The loop condition fails on the first test, so no squaring and no multiplication happen and the initial accumulator is returned as the empty product. |
| Most negative exponent | $x = -1.0$, $n = -2147483648$ | $1.0$ | After inversion the working magnitude is $\lvert n \rvert = 2^{31}$, a single set bit followed by thirty-one zeros, so only the final iteration multiplies; the base has been squared an even number of times, leaving the sign positive. |
| Most positive exponent | $x = -1.0$, $n = 2147483647$ | $-1.0$ | $2^{31} - 1$ is thirty-one set bits, so the accumulator absorbs thirty-one factors; every one has magnitude $1$, and the odd count of factors leaves the sign negative. |
| Zero base | $x = 0.0$, $n = 5$ | $0.0$ | The first set bit multiplies $0.0$ into the accumulator, and every subsequent squaring keeps the base at $0.0$ as well. |
| Negative base, negative odd exponent | $x = -2.0$, $n = -3$ | $-0.125$ | Inversion gives a working base of $-0.5$ with $\lvert n \rvert = 3$; the accumulator becomes $(-0.5) \times (0.25) = -0.125$, an odd number of negative factors. |
| Unit exponent | $x = -99.999$, $n = 1$ | $-99.999$ | Exactly one set bit, so exactly one multiplication; the loop degenerates to a single scalar copy. |
| Fractional base | $x = 2.1$, $n = 3$ | $9.261$ | Set bits at $2^0$ and $2^1$ give $\text{res} = 2.1 \times 4.41 = 9.261$, so only two multiplications replace a three-step linear chain. |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log n)$. Each iteration performs a bitwise right-shift $n \gg 1$, cutting the exponent in half. At most $32$ iterations occur for any 32-bit signed integer.
- **Auxiliary Space Complexity:** $O(1)$. The iterative implementation requires only scalar floating-point and integer registers.

### Alternative Formulations

| Formulation | Mechanism | Time | Auxiliary space | Behaviour on $x = 2.0$, $n = 10$ |
|:---|:---|:---|:---|:---|
| Iterative bit scan (this lesson) | Keep a running squared base and shift the exponent right | $O(\log n)$ | $O(1)$ | Four iterations, accumulator finishing at $1024.0$. |
| Recursive halving | For even $n$, square the base and halve the exponent; for odd $n$, peel off one factor first | $O(\log n)$ | $O(\log n)$ call stack | The same $1024.0$, reached through four nested calls; at the exponent ceiling the depth is only about $31$ frames. |
| Compute $\lvert n \rvert$ first, then divide once | Build $x^{\lvert n \rvert}$ and take a single reciprocal at the end | $O(\log n)$ | $O(1)$ | Returns $4.0$ for $n = -2$ and then $0.25$, matching this lesson's result; the reciprocal simply lands at the other end of the pipeline. |
| Linear repeated multiplication | Multiply the base by itself $n$ times | $O(n)$ | $O(1)$ | Ten multiplications to reach $1024.0$ — indistinguishable here, but at $n = 2147483647$ it is roughly $2 \times 10^8$ times more work than the bit scan. |
