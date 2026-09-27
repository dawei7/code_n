# Guided Example: Add Binary

We trace the step-by-step full-adder binary bit addition on representative binary string instances:

- **Input:** $a = \text{"1010"}$, $b = \text{"1011"}$
- **Required output:** $\text{"10101"}$

This instance demonstrates two-pointer right-to-left traversal of unequal-length strings, binary full-adder truth table states ($\text{sum} \in \{0, 1, 2, 3\}$), bit extraction via modulo ($\text{sum} \pmod 2$), carry generation via integer division ($\lfloor \text{sum} / 2 \rfloor$), and reversing the accumulated bit buffer.

---

## 1. Instance & Teaching Goal

Given two binary strings $a$ and $b$, return their sum as a binary string.

For $a = \text{"1010"}$ ($10_{10}$) and $b = \text{"1011"}$ ($11_{10}$):
$$
10 + 11 = 21_{10} = (10101)_2
$$

Converting the strings to standard integers via `int(a, 2)` risks integer overflow in languages with fixed 32-bit or 64-bit integer limits when string lengths reach $10^4$. The optimal approach simulates hardware binary full-adders, processing bits from right to left in $O(\max(|a|, |b|))$ time and $O(1)$ auxiliary space.

---

## 2. Conceptual Foundation & Invariants

### Binary Full-Adder Mechanics
We initialize pointers $i = |a| - 1$, $j = |b| - 1$, and $\text{carry} = 0$.
While $i \ge 0$ or $j \ge 0$ or $\text{carry} > 0$:
1. Read available bit values:
   $$
   \text{bit}_a = (a[i] - \text{'0'}) \quad \text{if } i \ge 0 \text{ else } 0
   $$
   $$
   \text{bit}_b = (b[j] - \text{'0'}) \quad \text{if } j \ge 0 \text{ else } 0
   $$
2. Compute column sum:
   $$
   \text{total} = \text{bit}_a + \text{bit}_b + \text{carry}
   $$
3. Emit output bit and update carry:
   $$
   \text{output\_bit} = \text{total} \pmod 2
   $$
   $$
   \text{carry} = \lfloor \text{total} / 2 \rfloor
   $$
4. Decrement pointers: $i \leftarrow i - 1, j \leftarrow j - 1$.

### Full-Adder Truth Table

| Input $\text{bit}_a$ | Input $\text{bit}_b$ | Incoming $\text{carry}$ | Total Sum | Emitted Bit ($\text{total} \pmod 2$) | Outgoing $\text{carry}$ ($\lfloor \text{total}/2 \rfloor$) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 | **0** | 0 |
| 1 | 0 | 0 | 1 | **1** | 0 |
| 0 | 1 | 0 | 1 | **1** | 0 |
| 1 | 1 | 0 | 2 | **0** | **1** |
| 0 | 0 | 1 | 1 | **1** | 0 |
| 1 | 0 | 1 | 2 | **0** | **1** |
| 0 | 1 | 1 | 2 | **0** | **1** |
| 1 | 1 | 1 | 3 | **1** | **1** |

> **Invariant.** At each step, all lower-order bits have been correctly synthesized into the accumulator list, and $\text{carry} \in \{0, 1\}$ represents the overflow to the current position.

---

## 3. Step-by-Step Worked Execution

We add $a = \text{"1010"}$ and $b = \text{"1011"}$:

### Initialization
- Pointer $i = 3$ (points to $a[3] = \text{'0'}$).
- Pointer $j = 3$ (points to $b[3] = \text{'1'}$).
- $\text{carry} = 0$, $\text{buffer} = []$.

---

### Step 1 (Position $2^0$, Index $i=3, j=3$)
- $\text{bit}_a = 0, \text{bit}_b = 1, \text{carry} = 0$.
- $\text{total} = 0 + 1 + 0 = 1$.
- Emitted bit: $1 \pmod 2 = 1$. Append `'1'`.
- Next carry: $\lfloor 1 / 2 \rfloor = 0$.
- Decrement: $i \to 2, j \to 2$.

---

### Step 2 (Position $2^1$, Index $i=2, j=2$)
- $\text{bit}_a = 1, \text{bit}_b = 1, \text{carry} = 0$.
- $\text{total} = 1 + 1 + 0 = 2$.
- Emitted bit: $2 \pmod 2 = 0$. Append `'0'`.
- Next carry: $\lfloor 2 / 2 \rfloor = 1$.
- Decrement: $i \to 1, j \to 1$.

---

### Step 3 (Position $2^2$, Index $i=1, j=1$)
- $\text{bit}_a = 0, \text{bit}_b = 0, \text{carry} = 1$.
- $\text{total} = 0 + 0 + 1 = 1$.
- Emitted bit: $1 \pmod 2 = 1$. Append `'1'`.
- Next carry: $\lfloor 1 / 2 \rfloor = 0$.
- Decrement: $i \to 0, j \to 0$.

---

### Step 4 (Position $2^3$, Index $i=0, j=0$)
- $\text{bit}_a = 1, \text{bit}_b = 1, \text{carry} = 0$.
- $\text{total} = 1 + 1 + 0 = 2$.
- Emitted bit: $2 \pmod 2 = 0$. Append `'0'`.
- Next carry: $\lfloor 2 / 2 \rfloor = 1$.
- Decrement: $i \to -1, j \to -1$.

---

### Step 5 (Final Overflow Carry, Position $2^4$)
- $i < 0$ and $j < 0$, but $\text{carry} = 1 > 0$.
- $\text{total} = 0 + 0 + 1 = 1$.
- Emitted bit: $1 \pmod 2 = 1$. Append `'1'`.
- Next carry: $\lfloor 1 / 2 \rfloor = 0$.
- Loop halts.

Buffer of collected bits (LSB to MSB): `['1', '0', '1', '0', '1']`.
Reverse buffer: $\text{"10101"}$.

---

## 4. Complete Execution Trace

| Column Added | $a[i]$ | $b[j]$ | Incoming $\text{carry}$ | Column Total | Emitted Bit ($\text{total} \pmod 2$) | Outgoing $\text{carry}$ | Buffer (LSB $\to$ MSB) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| $2^0$ | `'0'` | `'1'` | 0 | 1 | **1** | 0 | `['1']` |
| $2^1$ | `'1'` | `'1'` | 0 | 2 | **0** | 1 | `['1', '0']` |
| $2^2$ | `'0'` | `'0'` | 1 | 1 | **1** | 0 | `['1', '0', '1']` |
| $2^3$ | `'1'` | `'1'` | 0 | 2 | **0** | 1 | `['1', '0', '1', '0']` |
| $2^4$ (Carry) | - | - | 1 | 1 | **1** | 0 | `['1', '0', '1', '0', '1']` |

Reversed final binary string: $\text{"10101"}$.

---

## 5. Algorithmic Correctness

**Soundness.** Binary addition is defined modulo 2 with carry propagation into base 2 powers. Computing $\text{total} \pmod 2$ and $\lfloor \text{total} / 2 \rfloor$ precisely implements the boolean equations of a ripple-carry full adder.

**Completeness.** The while-loop condition `i >= 0 or j >= 0 or carry` guarantees that all bits from both strings, as well as any final overflow carry, are fully processed.

---

## 6. Traps This Instance Exposes

- **Unequal String Lengths:** One string may be much longer than the other (e.g. `"1"` and `"1111"`). Testing $i \ge 0$ and $j \ge 0$ independently treats missing digits as $0$ without allocating padded strings.
- **Unprocessed Final Carry:** Forgetting the `or carry` check causes sums like `"1" + "1"` to emit `"0"` instead of `"10"`.
- **String Reversal:** Appending bits to a list and joining reversed at the end (`"".join(reversed(buffer))`) is $O(N)$ linear time, avoiding quadratic string copying overhead.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\max(M, N))$, where $M = |a|$ and $N = |b|$. The loop runs $\max(M, N) + 1$ times.
- **Auxiliary Space Complexity:** $O(\max(M, N))$ to store the output character list.
