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

The signed instance from the opening is the harder one, because its value is negative and every high bit position sees sign-extended ones. Counting its columns explicitly:

| Bit position $i$ | Values contributing a $1$ | Count | Count mod 3 | Singleton bit | Note |
|:---:|:---|:---:|:---:|:---:|:---|
| 0 | the three copies of $1$ | 3 | 0 | 0 | The three $1$s cancel; neither $-2$ nor $-4$ sets bit 0 |
| 1 | the three copies of $-2$ | 3 | 0 | 0 | Only $-2$ sets bit 1, and it appears exactly three times |
| 2 | three copies of $-2$, three copies of $4$, one $-4$ | 7 | 1 | 1 | $3 + 3 \equiv 0$, so only the single contribution of $-4$ survives |
| $3 \dots 30$ | three copies of $-2$, one $-4$ | 4 | 1 | 1 | Sign extension repeats the high bits of both negatives, and $3 + 1 \equiv 1$ |
| 31 (Sign) | three copies of $-2$, one $-4$ | 4 | 1 | 1 | The set sign bit means the assembly below must be read as a negative value |

Assembling the marked bits gives the unsigned pattern $\text{0xFFFFFFFC}$, and reducing it to a signed 32-bit integer yields $-4$. The lesson of the table is that the tripled negatives contribute high ones in complete groups of three: they vanish at every position above bit 1 as well, so no special branch is needed while counting.

---

## 5. Algorithmic Correctness

**Soundness.** Let $S$ be the singleton integer and $T_1, \dots, T_k$ be the integers appearing three times. For each bit position $i$, the sum of bits is $\text{count}_i = \text{bit}_i(S) + 3 \sum_{j=1}^k \text{bit}_i(T_j)$. Because $3 \sum \equiv 0 \pmod 3$, the remainder $\text{count}_i \bmod 3$ is mathematically equal to $\text{bit}_i(S)$.

**Completeness.** Evaluating all 32 bits covers the entire domain of 32-bit signed integers $[-2^{31}, 2^{31}-1]$, reconstructing the unique value bit-for-bit without loss.

---

## 6. Traps This Instance Exposes

- **Sign Bit in Python Two's Complement:** In Python, integers have arbitrary precision. If bit 31 is 1, a positive number $\ge 2^{31}$ will be constructed rather than a negative number! For bit 31, using `ans -= (1 << 31)` or `ans if ans < (1 << 31) else ans - (1 << 32)` properly converts the bit pattern into a negative signed integer.
- **Negative Tripled Numbers:** A negative number repeated three times contributes three sign-extended $1$s at higher bit positions. These sum to $3$, which also vanishes modulo 3 ($3 \equiv 0$). Negative numbers require no special branching during bit counting.
- **Generalizing to Multiplicity $K$:** This modulo-counting approach generalizes to any multiplicity $K$: if every non-target element appears $K$ times, taking $\text{count}_i \bmod K$ isolates the singleton.

The authored cases cover the sign bit, the all-zero answer, and the degenerate short arrays:

| Authored case | `nums` | Values appearing three times | Singleton | Decisive detail | Returned |
|:---|:---|:---|:---:|:---|:---:|
| `sample-1` | $[2, 2, 3, 2]$ | $2$ | 3 | Bit 0 counts $1$ and bit 1 counts $4$, so both remainders are $1$ | 3 |
| `sample-2` | $[0, 1, 0, 1, 0, 1, 99]$ | $0$ and $1$ | 99 | Only bits of $99 = 1100011_2$ survive; the triples of $0$ and $1$ contribute multiples of three at every position | 99 |
| `trial-negative-single` | $[-2, -2, 1, 1, 4, 1, 4, 4, -4, -2]$ | $-2$, $1$, $4$ | $-4$ | Every position from 2 to 31 counts $4$, and the sign bit turns the unsigned pattern into $-4$ | $-4$ |
| `trial-zero-single` | $[5, 5, 5, 7, 7, 7, 0]$ | $5$ and $7$ | 0 | The bit counts are $6$, $3$ and $6$ at positions 0, 1 and 2, so every remainder is $0$ and no bit is ever set | 0 |
| `trial-boundary-5` | $[2]$ | none | 2 | Bit 1 counts $1$, so the remainder is $1$ and the value is reconstructed | 2 |
| `trial-boundary-6` | $[2, 2]$ | none | 2 | Bit 1 counts $2$, and the remainder $2$ is still non-zero, so bit 1 is set | 2 |

The zero row is the sharpest one: the correct answer is an integer whose every bit remainder is $0$, so no position ever marks a bit. An implementation that treats "no bit was marked" as a failure would be wrong here, and an implementation that tests the remainder for equality with $1$ rather than for being non-zero would disagree with the last row.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(32 \cdot N) = O(N)$, where $N$ is the number of elements in `nums`. The bit-counting loop evaluates 32 fixed positions, each iterating over $N$ numbers. Method 2 (the digital logic FSM) evaluates in a single pass of $N$ operations.
- **Auxiliary Space Complexity:** $O(1)$ constant memory, utilizing only a few integer registers (`ans`, `count`).

The two methods taught above are complemented by three alternatives, and only two of them stay within constant space:

| Strategy | Idea | Time | Auxiliary space | Behavior on the signed instance |
|:---|:---|:---:|:---:|:---|
| Modulo-3 bit counting over 32 positions | Sum each bit column and keep the remainder | $O(32N)$ | $O(1)$ | Recovers $\text{0xFFFFFFFC}$, which needs the explicit sign-bit correction to become $-4$ |
| Two-register FSM (`ones`, `twos`) | A ternary counter per bit driven by XOR and masks | $O(N)$ | $O(1)$ | Produces $-4$ directly in one pass, with no separate sign step |
| Frequency map | Count occurrences and report the value seen once | $O(N)$ expected | $O(N)$ | Correct, but stores every distinct value and violates the constant-space requirement |
| Sort and scan runs of three | Order the array and look for a run of length one | $O(N \log N)$ | $O(N)$ for a copy, $O(1)$ if the caller's array may be reordered | Correct, but violates the linear-time requirement |
| XOR fold as in the two-copy problem | Reuse $x \oplus x = 0$ | $O(N)$ | $O(1)$ | Fails here: $x \oplus x \oplus x = x \ne 0$, so triples do not cancel and the result is $2 \oplus 3 = 1$ for `sample-1` |

For `sample-1` the naive XOR fold leaves $2 \oplus 2 \oplus 3 \oplus 2 = 1$ instead of $3$, which is exactly the gap the modulo-3 argument closes.

---
