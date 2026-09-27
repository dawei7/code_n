# Guided Example: Single Number III

We trace the step-by-step bitwise XOR cancellation, lowest set-bit mask isolation ($x \ \& \ -x$), and two-group partition filtering on representative integer arrays:

- **Input:** $\text{nums} = [1, 2, 1, 3, 2, 5]$
- **Required output:** $[3, 5]$ (The two unique elements that appear exactly once; all other elements appear twice)
- **Two Elements Instance:** $\text{nums} = [-1, 0] \implies [-1, 0]$ (No duplicates; direct bit differentiation)
- **Minimal Positive Pair:** $\text{nums} = [0, 1] \implies [1, 0]$
- **Negative Integer Support:** Handles signed 32-bit integers seamlessly under two's-complement arithmetic

This instance demonstrates bit manipulation algebra on multisets, explains why XORing all elements yields the bitwise difference $a \oplus b$, proves how the lowest set bit isolates a bit where $a$ and $b$ differ, details two-group partitioning to cancel duplicate pairs, and runs in strictly $O(N)$ time with $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given an array where exactly two integers $a$ and $b$ appear once, and all other integers appear exactly twice:
$$
\text{nums} = [1, 2, 1, 3, 2, 5]
$$
Find $a$ and $b$ in $O(N)$ time and $O(1)$ auxiliary memory.

- A hash map frequency counter takes $O(N)$ time, but consumes $O(N)$ extra memory.
- Sorting takes $O(N \log N)$ time and modifies the input.
- **Bitwise XOR Properties:**
  1. $x \oplus x = 0$ (Self-inverse: duplicates annihilate each other).
  2. $x \oplus 0 = x$ (Identity).
  3. Commutative and associative: order of elements does not matter.
XORing the entire array eliminates all duplicate pairs, leaving the combined sum:
$$
\text{xor\_all} = a \oplus b = 3 \oplus 5 = 6
$$
Since $a \ne b$, $\text{xor\_all} \ne 0$. At least one bit in $\text{xor\_all}$ is $1$. That bit distinguishes $a$ from $b$, allowing us to partition the array into two separate subproblems.

---

## 2. Conceptual Foundation & Invariants

### 1. The Global XOR Invariant
XORing all elements in $\text{nums}$:
$$
\text{xor\_all} = \bigoplus_{x \in \text{nums}} x = (1 \oplus 1) \oplus (2 \oplus 2) \oplus (3 \oplus 5) = 0 \oplus 0 \oplus (3 \oplus 5) = 3 \oplus 5
$$
In binary:
$$
a = 3 = 011_2, \quad b = 5 = 101_2
$$
$$
a \oplus b = 011_2 \oplus 101_2 = 110_2 = 6
$$
A bit is $1$ in $a \oplus b$ **if and only if** $a$ and $b$ have different bits at that position!

### 2. Isolating the Differentiating Bit (`diff`)
Using two's-complement arithmetic, we isolate the lowest set bit of $\text{xor\_all}$:
$$
\text{diff} = \text{xor\_all} \ \& \ (-\text{xor\_all})
$$
For $\text{xor\_all} = 6 = 00000110_2$:
$$
-\text{xor\_all} = \sim 6 + 1 = 11111010_2
$$
$$
\text{diff} = 00000110_2 \ \& \ 11111010_2 = 00000010_2 = 2
$$
This mask isolates bit position 1. At this bit, one singleton has a $1$, and the other has a $0$!

### 3. Two-Partition XOR Sweep
Divide all elements in `nums` into two groups using the mask $\text{diff}$:
- **Group 1 ($x \ \& \ \text{diff} \ne 0$):** Contains numbers with bit 1 set.
- **Group 2 ($x \ \& \ \text{diff} == 0$):** Contains numbers with bit 1 clear.

Every duplicated number has identical bits, so both copies fall into the **exact same group**, canceling out to $0$!
Singleton $a$ falls into one group, and singleton $b$ falls into the other:
$$
a = \bigoplus_{x \in \text{Group 1}} x, \quad b = \text{xor\_all} \oplus a
$$

> **Invariant.** Both duplicate copies of any paired element always land in the same partition, leaving only the lone singleton after XOR reduction.

---

## 3. Step-by-Step Worked Execution

We trace $\text{nums} = [1, 2, 1, 3, 2, 5]$:

### Step 1: Compute Full Array XOR
Compute cumulative XOR across all 6 elements:
- $0 \oplus 1 = 1$
- $1 \oplus 2 = 3$
- $3 \oplus 1 = 2$
- $2 \oplus 3 = 1$
- $1 \oplus 2 = 3$
- $3 \oplus 5 = \mathbf{6}$
$\text{xor\_all} = 6$ ($0110_2$).

---

### Step 2: Extract Differentiating Bit Mask
$$
\text{diff} = 6 \ \& \ (-6) = 2 \quad (0010_2)
$$
Bit 1 (weight 2) is chosen to partition the elements.

---

### Step 3: Partition and XOR Accumulation
Initialize $a = 0$:
We filter elements with bit 1 set ($x \ \& \ 2 \ne 0$):
1. Element $x = 1$ ($0001_2$): $1 \ \& \ 2 = 0$. Group 2 (Ignored).
2. Element $x = 2$ ($0010_2$): $2 \ \& \ 2 = 2 \ne 0$. Group 1:
   $$
   a \leftarrow 0 \oplus 2 = 2
   $$
3. Element $x = 1$ ($0001_2$): $1 \ \& \ 2 = 0$. Group 2 (Ignored).
4. Element $x = 3$ ($0011_2$): $3 \ \& \ 2 = 2 \ne 0$. Group 1:
   $$
   a \leftarrow 2 \oplus 3 = 1
   $$
5. Element $x = 2$ ($0010_2$): $2 \ \& \ 2 = 2 \ne 0$. Group 1:
   $$
   a \leftarrow 1 \oplus 2 = \mathbf{3}
   $$
   *(The duplicate 2 canceled out: $2 \oplus 3 \oplus 2 = 3$)*.
6. Element $x = 5$ ($0101_2$): $5 \ \& \ 2 = 0$. Group 2 (Ignored).

First singleton isolated: $a = \mathbf{3}$.

---

### Step 4: Extract Second Singleton
Recover $b$ using the total XOR:
$$
b = \text{xor\_all} \oplus a = 6 \oplus 3 = 0110_2 \oplus 0011_2 = 0101_2 = \mathbf{5}
$$

Output: $[3, 5]$.

---

## 4. Complete Execution Trace

```text
nums = [1, 2, 1, 3, 2, 5]

Pass 1: Total XOR
  1 ^ 2 ^ 1 ^ 3 ^ 2 ^ 5 = 6 (0110 in binary)

Mask: diff = 6 & (-6) = 2 (0010 in binary)

Pass 2: Partition by bit 1 (x & 2 != 0)
  x = 1: 1 & 2 == 0 -> Group 2
  x = 2: 2 & 2 != 0 -> a = 0 ^ 2 = 2
  x = 1: 1 & 2 == 0 -> Group 2
  x = 3: 3 & 2 != 0 -> a = 2 ^ 3 = 1
  x = 2: 2 & 2 != 0 -> a = 1 ^ 2 = 3
  x = 5: 5 & 2 == 0 -> Group 2

Singletons: a = 3, b = 6 ^ 3 = 5
Result: [3, 5]
```

| Element $x$ | Binary Representation | $x \ \& \ \text{diff}$ ($x \ \& \ 2$) | Assigned Partition | Group 1 Cumulative XOR ($a$) | Group 2 Cumulative XOR ($b$) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | $001_2$ | 0 | Group 2 | 0 | 1 |
| 2 | $010_2$ | 2 | Group 1 | 2 | 1 |
| 1 | $001_2$ | 0 | Group 2 | 2 | $1 \oplus 1 = 0$ |
| **3** | $011_2$ | 2 | **Group 1** | $2 \oplus 3 = 1$ | 0 |
| 2 | $010_2$ | 2 | Group 1 | $1 \oplus 2 = \mathbf{3}$ | 0 |
| **5** | $101_2$ | 0 | **Group 2** | 3 | $0 \oplus 5 = \mathbf{5}$ |
| **Output** | - | - | - | **3** | **5** |

---

## 5. Algorithmic Correctness

**Soundness.** Because $a \ne b$, $a \oplus b \ne 0$, which ensures $\text{diff} \ne 0$. For any identical pair $(v, v)$, both instances share the exact same bits, so both are either in Group 1 or Group 2. In each group, $v \oplus v = 0$. Since $a$ and $b$ have opposite bits at the position represented by $\text{diff}$, exactly one falls into Group 1 and the other into Group 2. Thus, the XOR accumulator for each group isolates the single unique element without interference.

**Completeness.** Every element in `nums` is examined, and the bitwise properties of XOR operate universally across all 32-bit signed integers.

---

## 6. Traps This Instance Exposes

- **Integer Overflow in Two's Complement ($-\text{xor\_all}$):** In languages like C/C++ or Java with fixed 32-bit signed integers, if $\text{xor\_all} = -2^{31}$ (`INT_MIN`), computing $-\text{xor\_all}$ causes undefined signed integer overflow. Casting to an unsigned integer (`(unsigned int)xor_all`) before negation prevents overflow bugs.
- **Operator Precedence Trap:** In Python and C++, bitwise AND (`&`) has lower precedence than equality comparison (`!=` or `==`). Writing `if x & diff != 0` is parsed as `if x & (diff != 0)`! Parentheses are mandatory: `if (x & diff) != 0:`.
- **Assuming Fixed Bit Index:** Rather than looping through bits $0 \dots 31$ with shift operations, the identity `diff = x & -x` extracts the lowest set bit in a single CPU instruction ($O(1)$).

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of elements in `nums`. Pass 1 reads all $N$ elements to compute `xor_all`. Pass 2 reads all $N$ elements to compute the partitioned XOR sum $a$. Total runtime is $2N = O(N)$ linear time.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary space. Only scalar variables (`xor_all`, `diff`, `a`, `b`) are stored.
