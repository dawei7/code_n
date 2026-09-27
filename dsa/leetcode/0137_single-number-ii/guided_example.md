# Guided Example: Single Number II

We trace the step-by-step bit-level modulo-3 summation and two-bit digital logic finite state machine on representative triplicated element arrays:

- **Input:** $\text{nums} = [2, 2, 3, 2]$
- **Required output:** $3$ (Tripled $2$ cancels modulo 3, isolating singleton $3$)
- **Negative Number Instance:** $\text{nums} = [-2, -2, 1, 1, 4, 1, -2] \implies 4$

This instance demonstrates counting bit occurrences modulo 3 ($\sum \text{bit}_i \pmod 3$), proves why elements with multiplicity 3 vanish under modular arithmetic, contrasts the 32-pass bit counter with the single-pass 2-bit digital logic state machine (`ones`, `twos`), and addresses signed 32-bit two's complement reconstruction in $O(N)$ time and $O(1)$ space.

---

## 1. Instance & Teaching Goal

Given an integer array $\text{nums} = [2, 2, 3, 2]$ where every element appears exactly **three times** except for one unique element which appears **exactly once**, find that unique single element.
The problem requires an algorithm with linear $O(N)$ runtime complexity and strictly constant $O(1)$ extra space.

In LeetCode 136 (where duplicates appear twice), bitwise XOR solves the problem because $x \oplus x = 0$ is arithmetic addition modulo 2.
Here, duplicate elements appear three times ($3 \times 1 = 3$), so XORing them yields $x \oplus x \oplus x = x \ne 0$.
The modular arithmetic generalization:
For any bit position $k$, summing that bit across all numbers yields:
$$
\sum_{x \in \text{nums}} \text{bit}_k(x) = 3 \times (\text{triplets with bit set}) + 1 \times (\text{singleton bit})
$$
Taking the sum modulo 3:
$$
\left(\sum_{x \in \text{nums}} \text{bit}_k(x)\right) \bmod 3 = \text{bit}_k(\text{singleton})
$$
Every tripled number contributes $3 \equiv 0 \pmod 3$, cleanly isolating each bit of the singleton in $O(N)$ time and $O(1)$ space.

---

## 2. Conceptual Foundation & Invariants

### Method 1: 32-Bit Modulo-3 Bit Reconstruction
For each bit position $i \in [0, 31]$:
1. Count how many numbers in `nums` have their $i$-th bit set:
   $$
   \text{count}_i = \sum_{x \in \text{nums}} \left( (x \gg i) \ \& \ 1 \right)
   $$
2. If $\text{count}_i \bmod 3 == 1$:
   - The singleton has bit $i$ set.
   - For bits $0 \dots 30$: `ans |= (1 << i)`.
   - For sign bit 31: If set, convert from unsigned representation to signed two's complement: `ans -= (1 << 31)`.

### Method 2: Single-Pass Digital Logic FSM (`ones`, `twos`)
We maintain two 32-bit registers `ones` and `twos` that act as a ternary counter for each bit position:
- State 0 (seen 0 times mod 3): $\text{twos} = 0, \text{ones} = 0$
- State 1 (seen 1 time mod 3): $\text{twos} = 0, \text{ones} = 1$
- State 2 (seen 2 times mod 3): $\text{twos} = 1, \text{ones} = 0$
- State 3 (seen 3 times mod 3): resets back to State 0 ($\text{twos} = 0, \text{ones} = 0$).

Transition for each number $x$:
$$
\text{ones} \leftarrow (\text{ones} \oplus x) \ \& \ (\sim\text{twos})
$$
$$
\text{twos} \leftarrow (\text{twos} \oplus x) \ \& \ (\sim\text{ones})
$$
After processing all numbers, `ones` directly holds the bits of the unique number.

> **Invariant.** For each bit position $k$, the ternary counter cycles through $0 \to 1 \to 2 \to 0$ upon receiving ones. Tripled numbers complete an exact cycle back to 0, leaving the singleton in `ones`.

---

## 3. Step-by-Step Worked Execution

We trace Method 1 on $\text{nums} = [2, 2, 3, 2]$:
Binary representations:
- $2 = 010_2$
- $2 = 010_2$
- $3 = 011_2$
- $2 = 010_2$

### Position $i = 0$ (Least Significant Bit, $2^0 = 1$):
- Bit 0 of each number:
  - $2 \implies 0$
  - $2 \implies 0$
  - $3 \implies 1$
  - $2 \implies 0$
- $\text{count}_0 = 0 + 0 + 1 + 0 = 1$.
- Modulo 3: $1 \bmod 3 = \mathbf{1}$.
- Bit 0 of singleton is $1$.
- Cumulative answer: $\text{ans} = 1$ ($001_2$).

---

### Position $i = 1$ (Middle Bit, $2^1 = 2$):
- Bit 1 of each number:
  - $2 \implies 1$
  - $2 \implies 1$
  - $3 \implies 1$
  - $2 \implies 1$
- $\text{count}_1 = 1 + 1 + 1 + 1 = 4$.
- Modulo 3: $4 \bmod 3 = \mathbf{1}$ (The three $2$s contribute $3 \equiv 0$; $3$ contributes $1$).
- Bit 1 of singleton is $1$.
- Cumulative answer: $\text{ans} = 1 | (1 \ll 1) = 1 | 2 = 3$ ($011_2$).

---

### Position $i = 2$ through $31$:
- Bit values for all numbers are $0$.
- $\text{count}_i = 0 \implies 0 \bmod 3 = 0$.
- No higher bits set.

Sign bit 31 is $0 \implies$ positive integer.
Final reconstructed answer: $\mathbf{3}$.

---

## 4. Complete Execution Trace

### Bit Column Count Table on $[2, 2, 3, 2]$

```text
Number        Bit 2 (4s)    Bit 1 (2s)    Bit 0 (1s)
  2               0             1             0
  2               0             1             0
  3               0             1             1
  2               0             1             0
------------------------------------------------
Sum:              0             4             1
Sum % 3:          0             1             1
Reconstructed:    0             1             1  => 3
```

| Bit Position $i$ | Binary Weight $2^i$ | Bit Sum $\sum \text{bit}_i$ | $\text{count}_i \bmod 3$ | Singleton Bit | Cumulative `ans` |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 1 | $0 + 0 + 1 + 0 = 1$ | 1 | **1** | 1 ($001_2$) |
| 1 | 2 | $1 + 1 + 1 + 1 = 4$ | 1 | **1** | **3 ($011_2$)** |
| 2 | 4 | $0 + 0 + 0 + 0 = 0$ | 0 | 0 | 3 |
| $3 \dots 30$ | - | 0 | 0 | 0 | 3 |
| 31 (Sign) | $-2^{31}$ | 0 | 0 | 0 | **3 (Result)** |

---

## 5. Algorithmic Correctness

**Soundness.** Let $S$ be the singleton integer and $T_1, \dots, T_k$ be the integers appearing three times. For each bit position $i$, the sum of bits is $\text{count}_i = \text{bit}_i(S) + 3 \sum_{j=1}^k \text{bit}_i(T_j)$. Because $3 \sum \equiv 0 \pmod 3$, the remainder $\text{count}_i \bmod 3$ is mathematically equal to $\text{bit}_i(S)$.

**Completeness.** Evaluating all 32 bits covers the entire domain of 32-bit signed integers $[-2^{31}, 2^{31}-1]$, reconstructing the unique value bit-for-bit without loss.

---

## 6. Traps This Instance Exposes

- **Sign Bit in Python Two's Complement:** In Python, integers have arbitrary precision. If bit 31 is 1, a positive number $\ge 2^{31}$ will be constructed rather than a negative number! For bit 31, using `ans -= (1 << 31)` or `ans if ans < (1 << 31) else ans - (1 << 32)` properly converts the bit pattern into a negative signed integer.
- **Negative Tripled Numbers:** A negative number repeated three times contributes three sign-extended $1$s at higher bit positions. These sum to $3$, which also vanishes modulo 3 ($3 \equiv 0$). Negative numbers require no special branching during bit counting.
- **Generalizing to Multiplicity $K$:** This modulo-counting approach generalizes to any multiplicity $K$: if every non-target element appears $K$ times, taking $\text{count}_i \bmod K$ isolates the singleton.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(32 \cdot N) = O(N)$, where $N$ is the number of elements in `nums`. The bit-counting loop evaluates 32 fixed positions, each iterating over $N$ numbers. Method 2 (the digital logic FSM) evaluates in a single pass of $N$ operations.
- **Auxiliary Space Complexity:** $O(1)$ constant memory, utilizing only a few integer registers (`ans`, `count`).
