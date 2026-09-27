# Guided Example: Number Complement

We trace the step-by-step bit-length determination ($L = \lfloor \log_2(num) \rfloor + 1$), full-ones bitmask generation ($mask = (1 \ll L) - 1$), bitwise XOR inversion ($num \oplus mask$), and bitwise arithmetic cancellation on representative integers:

- **Input:** $num = 5$
- **Required output:** `2`
  - Binary representation:
    $$
    5 = 101_2
    $$
  - Significant bit length: $L = 3$ bits (from bit 0 to bit 2)
  - Generate a full mask of 1s of length $L$:
    $$
    mask = (1 \ll 3) - 1 = 8 - 1 = 7 = 111_2
    $$
  - Bitwise XOR inversion:
    $$
    \begin{aligned}
    num  &= 101_2 \\
    mask &= 111_2 \\
    \hline
    num \oplus mask &= 010_2 = 2
    \end{aligned}
    $$
  - The inverted value is $\mathbf{2}$.
- **Single-Bit Instance:** $num = 1$ ($1_2$)
  - $L = 1$, $mask = (1 \ll 1) - 1 = 1_2$
  - Inversion: $1 \oplus 1 = \mathbf{0}$
- **Four-Bit Alternating Pattern:** $num = 10$ ($1010_2$)
  - $L = 4$, $mask = (1 \ll 4) - 1 = 15 = 1111_2$
  - Inversion: $1010_2 \oplus 1111_2 = 0101_2 = \mathbf{5}$
- **All Ones Input:** $num = 7$ ($111_2$)
  - $L = 3$, $mask = 7$
  - Inversion: $7 \oplus 7 = \mathbf{0}$

This instance demonstrates bitwise mask synthesis, mathematically proves why XOR with an all-ones mask flips significant bits without introducing leading ones from two's complement sign extension, and derives $O(1)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a positive integer $num = 5$:
The **complement** of an integer is the integer you get when you flip all the `0`s to `1`s and all the `1`s to `0`s in its binary representation (ignoring leading zeros).
Find the complement number.

```text
Input: num = 5
Binary representation:      1  0  1
Flip every bit:             0  1  0

Decimal value of "010": 2
```

### The Two's Complement Hazard
In standard 32-bit two's complement computing:
- The bitwise NOT operator `~num` flips **all 32 bits**, including the 29 leading zeroes!
- For $num = 5$, `~5` becomes `...11111111111111111111111111111010` (which is $-6$).
- To flip *only* the significant bits without polluting the high-order bits with 1s:
  We must construct a **mask of 1s having the exact same bit-length** as $num$ and compute $num \oplus mask$.

---

## 2. Conceptual Foundation & Invariants

### 1. Significant Bit Length:
Let $L$ be the number of bits in the binary representation of $num$:
$$
L = \text{bit\_length}(num) = \lfloor \log_2(num) \rfloor + 1
$$
For $num = 5$, $L = 3$.

### 2. All-Ones Mask Construction:
Shifting $1$ to the left by $L$ places produces $2^L$ (a single 1 followed by $L$ zeroes).
Subtracting 1 yields exactly $L$ consecutive ones:
$$
mask = (1 \ll L) - 1 = \underbrace{11\dots 1}_{L \text{ bits}}
$$

### 3. Bitwise XOR Inversion:
XORing any bit with $1$ flips it:
- $0 \oplus 1 = 1$
- $1 \oplus 1 = 0$
Therefore:
$$
\text{Complement} = num \oplus mask
$$
Equivalently, since $num + \text{Complement} = mask$:
$$
\text{Complement} = mask - num
$$

> **Masking Invariant.** The mask $(1 \ll L) - 1$ isolates precisely the $L$ active bits of $num$, ensuring all bits in $[0, L - 1]$ invert while all bits $\ge L$ remain strictly zero.

---

## 3. Step-by-Step Worked Execution

We trace $num = 5$:

---

### Step 1: Calculate Bit Length $L$
- $num = 5$.
- Binary: $101_2$.
- Length:
  $$
  L = 3 \text{ bits}
  $$

---

### Step 2: Build the Bitmask
- Shift 1 by $L = 3$:
  $$
  1 \ll 3 = 1000_2 = 8
  $$
- Subtract 1:
  $$
  mask = 8 - 1 = 7 = 111_2
  $$

---

### Step 3: Compute Complement
- Perform bitwise XOR between $num$ and $mask$:
  $$
  5 \oplus 7 = 101_2 \oplus 111_2 = 010_2 = \mathbf{2}
  $$
- Or via subtraction:
  $$
  mask - num = 7 - 5 = \mathbf{2}
  $$
Output value: **`2`**.

---

## 4. Complete Execution Trace

| Decimal $num$ | Binary $num$ | Bit Length $L$ | Full-Ones Mask $(1 \ll L) - 1$ | Binary Inversion | Output Decimal |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **$1$** | $1_2$ | $1$ | $1_2 = 1$ | $1 \oplus 1 = 0_2$ | **$0$** |
| **$2$** | $10_2$ | $2$ | $11_2 = 3$ | $10_2 \oplus 11_2 = 01_2$ | **$1$** |
| **$5$** | $101_2$ | $3$ | $111_2 = 7$ | $101_2 \oplus 111_2 = 010_2$ | **$2$** |
| **$7$** | $111_2$ | $3$ | $111_2 = 7$ | $111_2 \oplus 111_2 = 000_2$ | **$0$** |
| **$10$** | $1010_2$ | $4$ | $1111_2 = 15$ | $1010_2 \oplus 1111_2 = 0101_2$ | **$5$** |

---

## 5. Boundary Cases & Failure Modes

- **Minimum Input ($num = 1$):** $L = 1 \implies mask = 1 \implies 1 \oplus 1 = \mathbf{0}$.
- **Powers of Two ($num = 8 = 1000_2$):** $L = 4 \implies mask = 15 = 1111_2 \implies 8 \oplus 15 = 7 = 0111_2$.
- **All Set Bits ($num = 2^{31} - 1$):** $L = 31 \implies mask = 2^{31} - 1 \implies \mathbf{0}$.
- **Large 32-Bit Overflow Avoidance:** Using unsigned 64-bit shifts or built-in arbitrary precision integers avoids 32-bit signed shift overflow when $L = 31$.

---

## 6. Traps & Common Anti-Patterns

- **Direct Bitwise NOT (`~num`):** Evaluating `~5` produces negative two's-complement numbers ($-6$) because all upper zero bits are flipped to 1. Masking with significant bits is mandatory.
- **String Conversion Roundtrips:** Converting to binary string via `bin(num)`, replacing `'1'` with `'0'` and `'0'` with `'1'`, and calling `int(..., 2)` works, but incurs heavy string heap allocation. CPU bitwise shifts execute in a single clock cycle.
- **Shift by 32 in 32-Bit Types:** In C/C++, shifting a 32-bit integer by 32 positions (`1 << 32`) is undefined behavior. Using `(1ULL << L) - 1` or handling the boundary safely prevents compiler UB.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Bit length calculation takes $O(1)$ time (via CPU instruction `clz` / `BSR`).
  - Bitwise shift and XOR take $O(1)$ time.
  - Total Time: $\mathcal{O}(1)$ machine operations.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ space using scalar CPU registers.
