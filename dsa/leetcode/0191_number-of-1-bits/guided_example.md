# Guided Example: Number of 1 Bits

We trace the step-by-step Brian Kernighan bitwise cancellation algorithm and Hamming weight evaluation on representative binary integers:

- **Input:** $n = 11$ (`00000000000000000000000000001011` in binary)
- **Required output:** $3$ ($11 = 2^3 + 2^1 + 2^0 \implies 3$ set bits)
- **Power of Two Instance:** $n = 128$ (`10000000` in binary) $\implies 1$ (Terminates in exactly 1 operation)
- **Dense Bit Instance:** $n = 2147483645$ $\implies 30$ ($30$ set bits out of $32$)
- **Zero Instance:** $n = 0 \implies 0$

This instance demonstrates Brian Kernighan's bit-clearing identity ($n \ \& \ (n - 1)$), proves why subtraction flips all trailing bits up to the lowest set bit, demonstrates skipping long runs of zeroes in $O(1)$ operations, and establishes $O(k)$ runtime where $k$ is the number of set bits.

---

## 1. Instance & Teaching Goal

Given a 32-bit positive integer $n = 11$:
Represented in binary:
$$
n = 11_{10} = \mathbf{1011}_2
$$
Count the number of set bits (1s) in its binary representation, known as the **Hamming weight**.
Here, the bits at positions 0, 1, and 3 are set:
$$
\text{Total 1-bits} = 1 + 1 + 1 = \mathbf{3}
$$

A naive approach tests all 32 bit positions with a right-shift loop (`for _ in range(32)`), requiring 32 operations regardless of how sparse the integer is.
**Brian Kernighan's Algorithm** executes in time proportional **only to the number of set bits**:
- For each step, the bitwise expression $n \ \& \ (n - 1)$ clears the **least significant set bit** of $n$.
- All intervening zeroes between set bits are skipped in a single operation.
- For a power of two (such as $128 = 10000000_2$), the algorithm terminates after just 1 iteration!

---

## 2. Conceptual Foundation & Invariants

### The Brian Kernighan Bit-Clearing Theorem
Let $n$ be an integer whose binary representation has its lowest set bit at position $p$:
$$
n = \dots 1 \underbrace{00\dots0}_{p \text{ zeroes}}
$$
When we subtract 1 from $n$, borrow propagation flips the 1 at position $p$ to 0, and all $p$ trailing zeroes flip to 1s:
$$
n - 1 = \dots 0 \underbrace{11\dots1}_{p \text{ ones}}
$$
Now compute the bitwise AND $n \ \& \ (n - 1)$:
1. Higher bits ($\dots$ to the left of position $p$) are identical in both operands, so they remain unchanged.
2. At position $p$, $1 \ \& \ 0 = 0$. The set bit is cleared!
3. Lower bits ($p$ trailing bits) have $0 \ \& \ 1 = 0$. All trailing bits become 0.

Therefore:
$$
n \ \& \ (n - 1)
$$
produces an integer identical to $n$, except that its **least significant 1-bit has been set to 0**.

### Algorithm Protocol:
Initialize $\text{count} = 0$.

While $n > 0$:
$$
n \leftarrow n \ \& \ (n - 1)
$$
$$
\text{count} \leftarrow \text{count} + 1
$$

Return $\text{count}$.

> **Invariant.** After each iteration, `count` increases by 1, and the number of set bits in $n$ decreases by exactly 1. When $n = 0$, all set bits have been counted.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $n = 11$ ($1011_2$):

### Initialization
- $n = 11 = 1011_2$.
- $\text{count} = 0$.

---

### Iteration 1: Clear Bit at Position 0
- Compute $n - 1$:
  $$
  n - 1 = 11 - 1 = 10 = 1010_2
  $$
- Bitwise AND:
  $$
  n \ \& \ (n - 1) = 1011_2 \ \& \ 1010_2 = \mathbf{1010}_2 = 10
  $$
  *(Bit at index 0 cleared!)*
- Update:
  $$
  n \leftarrow 10, \quad \text{count} \leftarrow 0 + 1 = \mathbf{1}
  $$

---

### Iteration 2: Clear Bit at Position 1
- Compute $n - 1$:
  $$
  n - 1 = 10 - 1 = 9 = 1001_2
  $$
- Bitwise AND:
  $$
  n \ \& \ (n - 1) = 1010_2 \ \& \ 1001_2 = \mathbf{1000}_2 = 8
  $$
  *(Bit at index 1 cleared!)*
- Update:
  $$
  n \leftarrow 8, \quad \text{count} \leftarrow 1 + 1 = \mathbf{2}
  $$

---

### Iteration 3: Clear Bit at Position 3
- Compute $n - 1$:
  $$
  n - 1 = 8 - 1 = 7 = 0111_2
  $$
- Bitwise AND:
  $$
  n \ \& \ (n - 1) = 1000_2 \ \& \ 0111_2 = \mathbf{0000}_2 = 0
  $$
  *(Bit at index 3 cleared!)*
- Update:
  $$
  n \leftarrow 0, \quad \text{count} \leftarrow 2 + 1 = \mathbf{3}
  $$

---

### Termination
- $n == 0$. Loop terminates.
- Final set bit count: $\mathbf{3}$.

---

## 4. Complete Execution Trace

```text
n = 11 (binary: 1011)

Iter 1: n = 1011 & 1010 = 1010 (10).  Cleared bit 0. count = 1
Iter 2: n = 1010 & 1001 = 1000 ( 8).  Cleared bit 1. count = 2
Iter 3: n = 1000 & 0111 = 0000 ( 0).  Cleared bit 3. count = 3

Loop ends (n == 0). Total 1-bits: 3
```

| Iteration | Binary State of $n$ | Binary of $n - 1$ | $n \ \& \ (n - 1)$ | Cleared Bit Position | Updated $\text{count}$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Start | `1011` ($11$) | - | - | - | 0 |
| 1 | `1011` ($11$) | `1010` ($10$) | `1010` ($10$) | Bit 0 | 1 |
| 2 | `1010` ($10$) | `1001` ($9$) | `1000` ($8$) | Bit 1 | 2 |
| **3** | **`1000` ($8$)** | **`0111` ($7$)** | **`0000` ($0$)** | **Bit 3** | **3 (Final)** |

### Contrast: Power of Two ($n = 128$)
- $n = 128 = 10000000_2$.
- $n - 1 = 127 = 01111111_2$.
- $128 \ \& \ 127 = 00000000_2 = 0$.
- Count increments to **1** and loop terminates immediately!

---

## 5. Algorithmic Correctness

**Soundness.** Let $n > 0$. The lowest set bit of $n$ is at position $p = \log_2(n \ \& \ (-n))$. In $n - 1$, bit $p$ is cleared and bits $0 \dots p-1$ are set to 1. Since bits $0 \dots p-1$ are 0 in $n$, bitwise AND produces 0 at all positions $\le p$, while bits $> p$ remain identical. Thus, $n \ \& \ (n - 1)$ strictly eliminates the lowest set bit without modifying higher set bits.

**Completeness.** Each step decreases the number of set bits by exactly 1. Since any 32-bit positive integer has a finite number of set bits $k \le 32$, $n$ strictly decreases and reaches $0$ in exactly $k$ iterations.

---

## 6. Traps This Instance Exposes

- **Unnecessary 32-Bit Scans:** Scanning all 32 bits with `n & 1` and `n >>= 1` always takes 32 iterations, whereas Brian Kernighan takes only $k$ iterations (where $k \ll 32$ for sparse numbers).
- **Signed Integer Underflow:** In languages with signed integers, bit 31 set to 1 can represent negative values. In Python, integers have arbitrary precision, but for 32-bit contracts, inputs are treated as unsigned integers in $[0, 2^{32} - 1]$.
- **Built-in `bin(n).count('1')`:** While correct and $O(1)$, string conversion allocates memory and hides bitwise principles in interviews.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(k)$, where $k$ is the number of set bits (Hamming weight) of $n$. In the worst case (all bits set), $k = 32$. On average, $k \approx 16$. For powers of two, $k = 1$.
- **Auxiliary Space Complexity:** $O(1)$ constant auxiliary memory, using only the scalar integer `count`.
