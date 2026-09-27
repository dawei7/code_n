# Guided Example: Hamming Distance

We trace the step-by-step bitwise XOR difference extraction ($x \oplus y$), binary disparity mapping, Brian Kernighan's bit-clearing loop ($d \ \& \ (d - 1)$), and population count calculation on representative integer pairs:

- **Input:** $x = 1, \quad y = 4$
- **Required output:** `2`
  - Binary representations (aligned to 4 bits):
    $$
    x = 1 = 0001_2
    $$
    $$
    y = 4 = 0100_2
    $$
  - Bitwise XOR operation ($x \oplus y$):
    - Position 0 ($2^0$): $1 \oplus 0 = \mathbf{1}$ (Different)
    - Position 1 ($2^1$): $0 \oplus 0 = \mathbf{0}$ (Identical)
    - Position 2 ($2^2$): $0 \oplus 1 = \mathbf{1}$ (Different)
    - Position 3 ($2^3$): $0 \oplus 0 = \mathbf{0}$ (Identical)
    - Combined XOR value:
      $$
      d = x \oplus y = 0101_2 = 5
      $$
  - Count set bits (population count of $d = 5 = 0101_2$):
    - **Pass 1:** Least significant bit cleared via $d \ \& \ (d - 1)$:
      $$
      5 \ \& \ 4 = 0101_2 \ \& \ 0100_2 = 0100_2 = 4 \quad (\text{Count } = 1)
      $$
    - **Pass 2:** Next bit cleared:
      $$
      4 \ \& \ 3 = 0100_2 \ \& \ 0011_2 = 0000_2 = 0 \quad (\text{Count } = 2)
      $$
    - Value is now $0$. Loop halts.
  - Total differing bit positions: **`2`**.
- **Adjacent Numbers Instance:** $x = 3 (0011_2), y = 1 (0001_2) \implies x \oplus y = 0010_2 \implies \mathbf{1}$
- **Identical Numbers Instance:** $x = 0, y = 0 \implies x \oplus y = 0 \implies \mathbf{0}$ (Hamming distance is 0)

This instance demonstrates bitwise difference mapping, mathematically proves why bitwise XOR isolates exactly the positions of disagreement between binary vectors, and derives $O(1)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given two integers $x = 1$ and $y = 4$:
The **Hamming distance** between two integers is the number of positions at which the corresponding bits are different.
Calculate the Hamming distance between $x$ and $y$.

```text
Bitwise Comparison:
  x = 1:   0  0  0  1
  y = 4:   0  1  0  0
           ----------
  x ^ y:   0  1  0  1
              ^     ^
              Bit 2 Bit 0  (2 bits differ)

Hamming Distance: 2
```

### The Bitwise XOR Characterization
The exclusive OR (XOR, $\oplus$) truth table defines:
- $0 \oplus 0 = 0$
- $1 \oplus 1 = 0$
- $0 \oplus 1 = 1$
- $1 \oplus 0 = 1$
Thus, $(x \oplus y)_k = 1$ if and only if the $k$-th bit of $x$ differs from the $k$-th bit of $y$.
Therefore, the Hamming distance between $x$ and $y$ is mathematically equivalent to the **Hamming weight (population count)** of $x \oplus y$.

---

## 2. Conceptual Foundation & Invariants

### 1. XOR Difference Isolation:
Compute the difference integer:
$$
d = x \oplus y
$$

### 2. Brian Kernighan's Bit-Counting Algorithm:
To count the set bits in $d$:
- Subtracting 1 flips the rightmost set bit and all trailing zeros:
  $$
  d - 1 = (b_k \dots b_1 1 0 \dots 0) - 1 = (b_k \dots b_1 0 1 \dots 1)
  $$
- Computing the bitwise AND $d \ \& \ (d - 1)$ zeroes out the lowest set bit while keeping all higher bits unchanged:
  $$
  d \leftarrow d \ \& \ (d - 1)
  $$
- Repeating this operation until $d == 0$ requires exactly as many iterations as there are set bits in $d$.

> **Bit Invariance.** Every application of $d \ \& \ (d - 1)$ strictly reduces the Hamming weight of $d$ by exactly 1 without altering higher-order bits.

---

## 3. Step-by-Step Worked Execution

We trace $x = 1$ and $y = 4$:

---

### Step 1: Compute XOR Difference
- $x = 1 = 0001_2$.
- $y = 4 = 0100_2$.
- Compute bitwise XOR:
  $$
  d = x \oplus y = 0001_2 \oplus 0100_2 = 0101_2 = \mathbf{5}
  $$

---

### Step 2: Clear Bits Sequentially (Brian Kernighan)
Initialize $count = 0$.

1. **Iteration 1 ($d = 5 = 0101_2$):**
   - $d - 1 = 4 = 0100_2$.
   - $d \ \& \ (d - 1) = 0101_2 \ \& \ 0100_2 = 0100_2 = \mathbf{4}$.
   - $count \leftarrow 0 + 1 = \mathbf{1}$.
   - New value: $d = 4$.

2. **Iteration 2 ($d = 4 = 0100_2$):**
   - $d - 1 = 3 = 0011_2$.
   - $d \ \& \ (d - 1) = 0100_2 \ \& \ 0011_2 = 0000_2 = \mathbf{0}$.
   - $count \leftarrow 1 + 1 = \mathbf{2}$.
   - New value: $d = 0$.

---

### Step 3: Termination
- Value $d = 0$. Loop halts.
- Resulting Hamming distance: **`2`**.

---

## 4. Complete Execution Trace

| Step | Current Value $d$ | Binary Form | Subtract 1 ($d - 1$) | Bitwise AND ($d \ \& \ (d-1)$) | Bit Cleared | Total Count |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Init** | $5$ | $0101_2$ | — | — | — | $0$ |
| **1** | $5$ | $0101_2$ | $4$ ($0100_2$) | $4$ ($0100_2$) | Bit $0$ ($2^0$) | **$1$** |
| **2** | $4$ | $0100_2$ | $3$ ($0011_2$) | $0$ ($0000_2$) | Bit $2$ ($2^2$) | **$2$** |
| **End** | $0$ | $0000_2$ | — | — | — | **Result: $2$** |

---

## 5. Boundary Cases & Failure Modes

- **Equal Numbers ($x == y$):** $x \oplus x = 0 \implies 0$ set bits $\implies \mathbf{0}$.
- **Opposite Bits Across All Positions ($x = 0, y = 2^{31} - 1$):** $x \oplus y$ has all 31 bits set $\implies \mathbf{31}$.
- **Single Bit Difference ($x = 0, y = 1$):** $0 \oplus 1 = 1 \implies \mathbf{1}$.
- **Power of Two Numbers ($x = 2, y = 8$):** Disjoint single bits $\implies 2$ bits set $\implies \mathbf{2}$.

---

## 6. Traps & Common Anti-Patterns

- **Shifting 32 Times Unconditionally:** Iterating through all 32 bits with `d & 1` and `d >>= 1` always takes 32 iterations. Brian Kernighan's algorithm takes only $K$ iterations where $K \le 32$ is the number of set bits.
- **Negative Integer Sign Extension:** In languages with signed bitwise shift operators (like Java `>>`), shifting negative numbers fills leading bits with 1. Using logical right shift `>>>` or bitwise AND with unsigned masks prevents infinite loops.
- **Floating-Point Conversion:** Converting to floating-point strings or base-2 strings with string search (`bin(x ^ y).count('1')`) incurs string heap allocation overhead. Direct CPU bitwise instructions execute in a single machine cycle.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - The XOR operation takes $O(1)$ time.
  - The bit-clearing loop executes at most $K \le 31$ times, where $K$ is the number of differing bits.
  - Total Time: $\mathcal{O}(1)$ bounded by 31 steps (or 1 hardware popcount CPU instruction).
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ using a single scalar register.
