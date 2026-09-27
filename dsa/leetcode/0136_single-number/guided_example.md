# Guided Example: Single Number

We trace the step-by-step bitwise XOR identity accumulation and duplicate cancellation on representative integer arrays:

- **Input:** $\text{nums} = [4, 1, 2, 1, 2]$
- **Required output:** $4$ (Duplicates $1$ and $2$ cancel to $0$, isolating singleton $4$)
- **Base Instances:** $\text{nums} = [2, 2, 1] \implies 1, \quad \text{nums} = [1] \implies 1$

This instance demonstrates the mathematical properties of bitwise Exclusive OR (commutativity, associativity, self-inverse $x \oplus x = 0$, and identity $x \oplus 0 = x$), proves why pair order is irrelevant to bit cancellation, and achieves linear $O(N)$ runtime with strictly $O(1)$ auxiliary space without hash sets.

---

## 1. Instance & Teaching Goal

Given a non-empty array of integers $\text{nums} = [4, 1, 2, 1, 2]$ where every element appears exactly twice except for one unique element, find that single element.
The problem requires an algorithm with linear $O(N)$ runtime complexity and strictly constant $O(1)$ extra space.

In this instance:
- Value $1$ appears twice (indices $1$ and $3$).
- Value $2$ appears twice (indices $2$ and $4$).
- Value $4$ appears exactly once (index $0$).
Result: $4$.

A hash set or frequency map takes $O(N)$ auxiliary space, violating the constant space requirement.
Sorting takes $O(N \log N)$ time, violating the linear time requirement.
Bitwise Exclusive OR ($\oplus$) operates at the bit level: because identical bits cancel to $0$ ($1 \oplus 1 = 0$ and $0 \oplus 0 = 0$), accumulating the running XOR of all array values eliminates every paired duplicate, leaving the exact unique value in $O(N)$ time and $O(1)$ space.

---

## 2. Conceptual Foundation & Invariants

### Mathematical Properties of XOR ($\oplus$)
Bitwise XOR satisfies four fundamental algebraic laws:
1. **Self-Inverse:** Any integer XORed with itself is zero:
   $$
   x \oplus x = 0
   $$
2. **Identity Element:** Any integer XORed with zero remains unchanged:
   $$
   x \oplus 0 = x
   $$
3. **Commutativity:** Operand order can be freely rearranged:
   $$
   a \oplus b = b \oplus a
   $$
4. **Associativity:** Grouping parentheses can be freely repositioned:
   $$
   (a \oplus b) \oplus c = a \oplus (b \oplus c)
   $$

### Global Cancellation Theorem
Let $u$ be the unique single element, and let $p_1, p_2, \dots, p_k$ be the duplicate pairs in the array:
$$
\text{Result} = \bigoplus_{x \in \text{nums}} x = u \oplus (p_1 \oplus p_1) \oplus (p_2 \oplus p_2) \oplus \dots \oplus (p_k \oplus p_k)
$$
Applying the self-inverse identity:
$$
\text{Result} = u \oplus 0 \oplus 0 \oplus \dots \oplus 0 = u
$$

> **Invariant.** After processing index $i$, the accumulator register $\text{acc} = \bigoplus_{j=0}^i \text{nums}[j]$ stores the XOR sum of all elements in the prefix, in which all complete pairs encountered so far cancel out bit-by-bit.

---

## 3. Step-by-Step Worked Execution

We trace the single-register accumulator on $\text{nums} = [4, 1, 2, 1, 2]$ in binary:

### Initial State
- $\text{acc} = 0$ ($000_2$)

---

### Step 1: Element $x = 4$ ($100_2$)
- Bitwise operation:
  $$
  \text{acc} \leftarrow 000_2 \oplus 100_2 = 100_2 = 4
  $$

---

### Step 2: Element $x = 1$ ($001_2$)
- Bitwise operation:
  $$
  \text{acc} \leftarrow 100_2 \oplus 001_2 = 101_2 = 5
  $$

---

### Step 3: Element $x = 2$ ($010_2$)
- Bitwise operation:
  $$
  \text{acc} \leftarrow 101_2 \oplus 010_2 = 111_2 = 7
  $$

---

### Step 4: Element $x = 1$ ($001_2$)
- Re-encountering $1$:
  $$
  \text{acc} \leftarrow 111_2 \oplus 001_2 = 110_2 = 6
  $$
- The lowest bit introduced by the first $1$ is now cancelled back to $0$!

---

### Step 5: Element $x = 2$ ($010_2$)
- Re-encountering $2$:
  $$
  \text{acc} \leftarrow 110_2 \oplus 010_2 = 100_2 = \mathbf{4}
  $$
- The middle bit introduced by the first $2$ is now cancelled back to $0$!

Stream ends. The final accumulator value is $\mathbf{4}$.

---

## 4. Complete Execution Trace

```text
Numbers:        4         1         2         1         2
Binary:      100_2     001_2     010_2     001_2     010_2
Acc:  000 -> 100 (4) -> 101 (5) -> 111 (7) -> 110 (6) -> 100 (4)
                                                ^         ^
                                            cancels 1  cancels 2
Final Isolated Value: 4
```

| Step $i$ | Visited Value $\text{nums}[i]$ | Binary Representation | Prior Accumulator | Bitwise XOR Equation | New Accumulator Value | Parity Note |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| Init | - | - | - | - | 0 ($000_2$) | Base |
| 1 | 4 | $100_2$ | 0 | $000_2 \oplus 100_2$ | 4 ($100_2$) | Singleton introduced |
| 2 | 1 | $001_2$ | 4 | $100_2 \oplus 001_2$ | 5 ($101_2$) | First copy of 1 |
| 3 | 2 | $010_2$ | 5 | $101_2 \oplus 010_2$ | 7 ($111_2$) | First copy of 2 |
| 4 | 1 | $001_2$ | 7 | $111_2 \oplus 001_2$ | 6 ($110_2$) | **Second copy cancels 1** |
| **5** | **2** | **$010_2$** | **6** | **$110_2 \oplus 010_2$** | **4 ($100_2$)** | **Second copy cancels 2** |
| Final | - | - | - | - | **4 (Result)** | Singleton remains |

---

## 5. Algorithmic Correctness

**Soundness.** For each bit position $b$, the $b$-th bit of the XOR sum equals the sum of the $b$-th bits of all numbers modulo 2. If a number appears twice, its bits contribute an even count ($2 \times 1 = 2 \equiv 0 \pmod 2$), contributing $0$ to the final sum. The unique number appears once, contributing an odd count ($1 \equiv 1 \pmod 2$). Thus, the final XOR sum exactly reconstructs the binary representation of the unique number.

**Completeness.** Every number in the array is included in the sequential XOR fold. No element is skipped, ensuring all duplicates cancel completely.

---

## 6. Traps This Instance Exposes

- **Negative Integers in Bitwise XOR:** Bitwise XOR functions identically for negative integers using two's complement arithmetic (e.g. $-3 \oplus -3 = 0$). The cancellation holds across all signed 32-bit integers.
- **Requiring Odd Multiplicities Greater Than 1:** The proof strictly relies on the guarantee that non-target numbers appear *exactly twice*. If another number appeared three times, two would cancel and one would remain, polluting the accumulator (see LeetCode 137 for three-copy variations).
- **Single Element Input:** If `nums = [1]`, the accumulator initialized with `nums[0]` terminates immediately with `1`.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of elements in `nums`. A single loop processes each element once, performing an $O(1)$ hardware bitwise operation.
- **Auxiliary Space Complexity:** $O(1)$ extra space, using only a single scalar accumulator register.
