# Guided Example: Bitwise AND of Numbers Range

We trace the step-by-step bitwise range reduction, common binary prefix extraction, and Brian Kernighan bit-clearing on representative numerical intervals:

- **Input:** $\text{left} = 5, \quad \text{right} = 7$
- **Required output:** $4$ ($5 \ \& \ 6 \ \& \ 7 = 101_2 \ \& \ 110_2 \ \& \ 111_2 = 100_2 = 4$)
- **Power-of-Two Span Instance:** $\text{left} = 1, \quad \text{right} = 2147483647 \implies 0$ (Crossing bit boundaries clears all bits)
- **Identical Boundaries Instance:** $\text{left} = 10, \quad \text{right} = 10 \implies 10$
- **Zero Boundary Instance:** $\text{left} = 0, \quad \text{right} = 5 \implies 0$

This instance demonstrates why bitwise range AND is mathematically equivalent to the **longest common binary prefix** of `left` and `right` padded with trailing zeroes, contrasts right-shift synchronization with Brian Kernighan bit-clearing ($R \leftarrow R \ \& \ (R - 1)$), and executes in $O(\log R)$ bitwise operations with $O(1)$ memory.

---

## 1. Instance & Teaching Goal

Given two integers $\text{left} = 5$ and $\text{right} = 7$:
Compute the cumulative bitwise AND of every integer in the inclusive range $[5, 7]$:
$$
\text{Result} = 5 \ \& \ 6 \ \& \ 7
$$
Examining the binary representation of each number in the interval:
$$
\begin{aligned}
5 &= 1 \ 0 \ 1_2 \\
6 &= 1 \ 1 \ 0_2 \\
7 &= 1 \ 1 \ 1_2 \\
\hline
5 \ \& \ 6 \ \& \ 7 &= \mathbf{1 \ 0 \ 0}_2 = \mathbf{4}_{10}
\end{aligned}
$$

Reading that interval column by column makes the elimination rule concrete. Bit position $k$ carries weight $2^k$, and a column survives only when **every** member of the range agrees on it:

| Bit position $k$ | Weight $2^k$ | Members of $[5,7]$ with $0$ at $k$ | Members with $1$ at $k$ | Is the column constant? | Surviving bit |
|:---:|:---:|:---|:---|:---|:---:|
| 2 | $4$ | none | $5, 6, 7$ | Yes, every member has $1$ | $1$ |
| 1 | $2$ | $5$ | $6, 7$ | No, both bit values occur | $0$ |
| 0 | $1$ | $6$ | $5, 7$ | No, both bit values occur | $0$ |

A single dissenting member kills a column: bit $1$ collapses because $5 = 101_2$ has a $0$ there, and bit $0$ collapses because $6 = 110_2$ has a $0$ there. Only bit $2$, where all three numbers agree, contributes, and the surviving column reassembles as $100_2 = 4$.

A naive linear loop `for x in range(left, right + 1)` takes $O(\text{right} - \text{left})$ time. When $\text{right} - \text{left} \approx 2 \times 10^9$, this results in an immediate Time Limit Exceeded (TLE).
A bitwise observation reveals that:
- For any bit position $k$, if the value varies anywhere between $\text{left}$ and $\text{right}$, at least one number in $[L, R]$ has a $0$ at bit $k$.
- Because $x \ \& \ 0 = 0$, that entire bit column is permanently zeroed out.
- Consequently, the only bits that survive are the **unvarying identical high-order prefix bits common to both $\text{left}$ and $\text{right}$**.

---

## 2. Conceptual Foundation & Invariants

### Theorem: Common Binary Prefix
Let $L$ and $R$ be represented in 32-bit binary.
The bitwise AND of all integers in $[L, R]$ equals the longest common prefix of $L$ and $R$, followed by zeroes for all differing lower bits:
$$
\bigwedge_{x=L}^{R} x = (L \ \& \ R \ \& \ \text{prefix\_mask})
$$

### Method A: Right-Shift Synchronization (Prefix Alignment)
Shift both numbers right until they become identical, counting the number of shifts:
1. Initialize $\text{shift} = 0$.
2. While $\text{left} < \text{right}$:
   $$
   \text{left} \leftarrow \text{left} \gg 1, \quad \text{right} \leftarrow \text{right} \gg 1, \quad \text{shift} \leftarrow \text{shift} + 1
   $$
3. Restore common prefix to its original bit significance:
   $$
   \text{return } \text{left} \ll \text{shift}
   $$

### Method B: Brian Kernighan Right-Endpoint Reduction (Alternative)
Repeatedly clear the lowest set bit of `right` using $R \ \& \ (R - 1)$ until $R \le L$:
$$
\text{while right} > \text{left}: \quad \text{right} \leftarrow \text{right} \ \& \ (\text{right} - 1)
$$
$$
\text{return right}
$$

> **Invariant.** The bitwise AND of range $[L, R]$ is bounded above by $R$. Every cleared lowest set bit of $R$ corresponds to a column where numbers in $[L, R]$ fluctuate between 0 and 1.

---

## 3. Step-by-Step Worked Execution

We trace both methods on $\text{left} = 5$ ($101_2$) and $\text{right} = 7$ ($111_2$):

### Method A: Shift Synchronization
- **Shift 0:**
  - $\text{left} = 5 = 101_2$.
  - $\text{right} = 7 = 111_2$.
  - Are they equal? No ($5 \ne 7$).
  - Shift right: $\text{left} = 10_2 = 2, \quad \text{right} = 11_2 = 3, \quad \text{shift} = 1$.
- **Shift 1:**
  - $\text{left} = 2 = 10_2$.
  - $\text{right} = 3 = 11_2$.
  - Are they equal? No ($2 \ne 3$).
  - Shift right: $\text{left} = 1_2 = 1, \quad \text{right} = 1_2 = 1, \quad \text{shift} = 2$.
- **Shift 2:**
  - $\text{left} = 1, \quad \text{right} = 1$.
  - Are they equal? **Yes!** ($1 == 1$).
  - Common prefix identified: $1_2$.
  - Re-align with shift $= 2$:
    $$
    \text{Result} = 1_2 \ll 2 = \mathbf{100}_2 = \mathbf{4}
    $$

---

### Method B: Brian Kernighan Bit Clearing
- **Initial:** $\text{left} = 5 = 101_2, \quad \text{right} = 7 = 111_2$.
- **Iteration 1:**
  - Is $\text{right} > \text{left}$ ($7 > 5$)? Yes.
  - Compute $\text{right} \ \& \ (\text{right} - 1) = 7 \ \& \ 6 = 111_2 \ \& \ 110_2 = \mathbf{6}$ ($110_2$).
  - $\text{right} \leftarrow 6$.
- **Iteration 2:**
  - Is $\text{right} > \text{left}$ ($6 > 5$)? Yes.
  - Compute $\text{right} \ \& \ (\text{right} - 1) = 6 \ \& \ 5 = 110_2 \ \& \ 101_2 = \mathbf{4}$ ($100_2$).
  - $\text{right} \leftarrow 4$.
- **Iteration 3:**
  - Is $\text{right} > \text{left}$ ($4 > 5$)? No! ($4 \le 5$).
  - Loop terminates.
  - Return $\text{right} = \mathbf{4}$.

The reduction in tabular form, with the column that each cleared bit corresponds to:

| Kernighan iteration | `right` before | Lowest set bit cleared | Evaluation of $R \ \& \ (R - 1)$ | `right` after (binary) | Is `right > left`? |
|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | $7$ | bit $0$, weight $1$ | $7 \ \& \ 6 = 6$ | `110` ($6$) | Yes, $6 > 5$ — continue |
| 2 | $6$ | bit $1$, weight $2$ | $6 \ \& \ 5 = 4$ | `100` ($4$) | No, $4 \le 5$ — stop and return $4$ |

Each cleared bit is exactly one of the fluctuating columns identified in the section 1 table: bit $0$ varied because half the range is even, and bit $1$ varied because $5$ disagrees with $6$ and $7$ there. Once `right` has fallen to $100_2$, its remaining set bit is bit $2$, the one column the whole range agrees on, so nothing further may be cleared without destroying a correct answer bit.

---

## 4. Complete Execution Trace

```text
Range: [ 5, 7 ] (binary 101 to 111)

Method A (Shift Alignment):
  Shift 0: L = 101 (5), R = 111 (7) -> Not equal
  Shift 1: L =  10 (2), R =  11 (3) -> Not equal
  Shift 2: L =   1 (1), R =   1 (1) -> EQUAL! Prefix = 1
  Re-align: 1 << 2 = 100 (4)

Method B (Kernighan Clear):
  Iter 1: R = 7 & 6 = 6 (110) > 5
  Iter 2: R = 6 & 5 = 4 (100) <= 5 -> TERMINATE

Final Bitwise AND: 4
```

| Step | Method A: $\text{left}$ (Binary) | Method A: $\text{right}$ (Binary) | Current `shift` | Method B: $\text{right}$ State | Invariant Condition |
|:---:|:---:|:---:|:---:|:---:|:---|
| Init | `101` ($5$) | `111` ($7$) | 0 | `111` ($7$) | Search active |
| 1 | `10` ($2$) | `11` ($3$) | 1 | `110` ($6$) | Bits differing at position 0 cleared |
| **2** | **`1` ($1$)** | **`1` ($1$)** | **2** | **`100` ($4$)** | **Common prefix found $\implies$ Emits $4$** |

---

## 5. Algorithmic Correctness

**Soundness.** Let $p$ be the most significant bit where $L$ and $R$ differ. Since $L < R$, bit $p$ must be $0$ in $L$ and $1$ in $R$. In the numerical range $[L, R]$, the integer $2^p$ (or $R$ truncated at bit $p$) lies within the interval, flipping bit $p$ to $0$. Furthermore, every lower bit $k < p$ alternates between 0 and 1 within the range of size $\ge 2^p$. Thus, all bits $\le p$ must be $0$ in the cumulative AND. Bits $> p$ never change throughout $[L, R]$, so they are preserved in full.

**Completeness.** Both the shift algorithm and the bit-clearing algorithm strip away all bits from position $p$ downward, leaving precisely the common prefix.

---

## 6. Traps This Instance Exposes

- **Linear Range Iteration:** Running an iterative loop `for x in range(left, right + 1)` crashes with TLE when the range spans up to $2 \times 10^9$ numbers.
- **Interval Spanning Power of Two:** If $\text{left} = 1$ and $\text{right} = 2$, their binary representations are $01_2$ and $10_2$. They have no common prefix $\implies \text{shift}$ reaches the MSB, returning $0$.
- **Integer Overflow in 32-bit Signed Environments:** In C++/Java, `1 << 31` with signed integers causes signed overflow. Using unsigned 32-bit integers or Python's arbitrary-precision integers avoids overflow.

The boundary scenarios below are the ones worth rehearsing, because each one probes a different reason for the common prefix to be short, empty, or the whole number:

| Scenario | `left` | `right` | Binary endpoints | Longest common prefix | Result |
|:---|:---:|:---:|:---|:---|:---:|
| Single-point range | $12$ | $12$ | `1100`, `1100` | `1100` (the entire number) | $12$ |
| Range touching zero | $0$ | $1$ | `0`, `1` | the all-zero 32-bit prefix | $0$ |
| Shared high prefix | $49$ | $62$ | `110001`, `111110` | `11` | $48$ |
| Full 31-bit span | $1$ | $2147483647$ | `1`, `1111111111111111111111111111111` | none | $0$ |

The single-point range is the degenerate case where the two endpoints are already identical, so no shift and no bit-clearing ever happens and the endpoint itself is returned. The range touching zero is the opposite extreme: because $0$ has a $0$ in every column, every column of the AND is forced to $0$ the moment the interval includes it.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log \text{right})$, bounded by at most $31$ bit shifts or at most $31$ bit-clearing operations for standard 32-bit non-negative integers.
- **Auxiliary Space Complexity:** $O(1)$ constant auxiliary memory, requiring only two scalar tracking variables.
