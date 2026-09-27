# Guided Example: Sum of Two Integers

We trace the step-by-step half-adder bitwise simulation, carry-free addition via XOR (`a ^ b`), carry generation and left-shift propagation (`(a & b) << 1`), 32-bit two's complement masking (`& 0xFFFFFFFF`), and signed integer sign-restoration on representative integer instances:

- **Input:** $a = 1, \quad b = 2$
- **Required output:** $3$
  - Binary representations (4-bit slice):
    - $a = 1 = 0001_2$
    - $b = 2 = 0010_2$
  - Iteration 1:
    - Sum without carry: $a \oplus b = 0001_2 \oplus 0010_2 = 0011_2 = \mathbf{3}$
    - Carry generated: $(a \ \& \ b) \ll 1 = (0001_2 \ \& \ 0010_2) \ll 1 = 0 \ll 1 = \mathbf{0}$
    - New state: $a = 3, \; b = 0$
  - Carry $b = 0 \implies$ loop terminates
  - Positive sign verification: $3 < 2^{31} \implies \mathbf{3}$
- **Negative Arithmetic Instance:** $a = -2, \quad b = 3 \implies 1$
  - In two's complement: $-2 \equiv \texttt{0xFFFFFFFE}_{16}$
  - Sum ripples carries through bit 31, terminating at $a = 1$
- **Two Negative Integers:** $a = -1, \quad b = -1 \implies -2$
  - Bit 31 sign bit is set $\implies \sim(a \oplus \texttt{0xFFFFFFFF}) = -2$

This instance demonstrates digital logic full-adder circuit emulation in software, mathematically proves how XOR captures sum bits while AND left-shifted captures carry propagation, explains Python arbitrary-precision two's complement masking, and establishes $O(W) = O(1)$ time and $O(1)$ space complexity.

---

## 1. Instance & Teaching Goal

Given two signed integers $a = 1$ and $b = 2$:
Compute their sum $a + b$ **without using the arithmetic operators `+` or `-`**:

```text
Binary Bitwise Half-Adder Principles:
Bit A | Bit B | Sum (A ^ B) | Carry ((A & B) << 1)
  0   |   0   |      0      |          0
  0   |   1   |      1      |          0
  1   |   0   |      1      |          0
  1   |   1   |      0      |          1 (shifted left to next bit)

Example Trace (a = 1, b = 2):
a     = 0001
b     = 0010
a ^ b = 0011 (3)
(a & b) << 1 = 0000 (0, Carry is zero!)

Final Output: 3
```

### Emulating Hardware Adders
In digital hardware (ALUs), addition is implemented with logic gates:
1. **Sum Bit (without carry):** The exclusive-OR gate ($\text{XOR}$, $\oplus$) outputs $1$ if exactly one bit is $1$:
   $$
   \text{sum\_bits} = a \oplus b
   $$
2. **Carry Bit:** The logical-AND gate ($\text{AND}$, $\&$) outputs $1$ if both bits are $1$. Because a carry from bit $p$ must be added to bit $p+1$, it is shifted left by $1$:
   $$
   \text{carry} = (a \ \& \ b) \ll 1
   $$
3. By repeatedly replacing $a \leftarrow a \oplus b$ and $b \leftarrow carry$, the carry bits shift leftward until $carry = 0$.

---

## 2. Conceptual Foundation & Invariants

### 1. Python Two's Complement Simulation
Because Python integers have arbitrary precision (unlimited bits), negative numbers have an infinite sequence of leading $1$s. To emulate fixed 32-bit hardware integers and prevent infinite carry loops:
- Mask both operands to 32 bits:
  $$
  \text{MASK} = \texttt{0xFFFFFFFF} \quad (2^{32} - 1)
  $$
  $$
  a \leftarrow a \ \& \ \text{MASK}, \quad b \leftarrow b \ \& \ \text{MASK}
  $$

### 2. Adder Loop Protocol:
While $b \ne 0$:
1. Compute 32-bit carry:
   $$
   carry = \big((a \ \& \ b) \ll 1\big) \ \& \ \text{MASK}
   $$
2. Compute sum bits:
   $$
   a = a \oplus b
   $$
3. Advance:
   $$
   b = carry
   $$

### 3. Two's Complement Sign Restoration:
- The 32-bit sign bit is at $2^{31} = \texttt{0x80000000}$.
- If $a < \texttt{0x80000000}$: the number is positive $\implies$ return $a$.
- If $a \ge \texttt{0x80000000}$: the number is negative in two's complement.
  In Python, decode 32-bit negative integer:
  $$
  \text{result} = \sim(a \oplus \text{MASK})
  $$

> **Invariant.** At each step, $(a + b) \pmod{2^{32}}$ is strictly preserved. In each iteration, the lowest set bit in $b$ moves strictly to the left, guaranteeing termination within 32 steps.

---

## 3. Step-by-Step Worked Execution

We trace $a = 1, b = 2$:

---

### Step 1: 32-bit Mask Clamping
- $a = 1 \ \& \ \texttt{0xFFFFFFFF} = \mathbf{1}$.
- $b = 2 \ \& \ \texttt{0xFFFFFFFF} = \mathbf{2}$.

---

### Step 2: Iteration 1
- **Evaluate Carry:**
  $$
  a \ \& \ b = 1 \ \& \ 2 = 0b0001 \ \& \ 0b0010 = \mathbf{0}
  $$
  $$
  carry = ((0 \ll 1) \ \& \ \texttt{0xFFFFFFFF}) = \mathbf{0}
  $$
- **Evaluate Sum Bits:**
  $$
  a \leftarrow a \oplus b = 1 \oplus 2 = 0b0001 \oplus 0b0010 = 0b0011 = \mathbf{3}
  $$
- **Update $b$:**
  $$
  b \leftarrow carry = \mathbf{0}
  $$

---

### Step 3: Loop Termination
- Condition `while b:` evaluates to False ($b = 0$).
- No further carries remain to propagate.

---

### Step 4: Sign Check and Return
- Check sign bit:
  $$
  a = 3 < \texttt{0x80000000} \implies \text{Positive integer}
  $$
- Return:
  $$
  \mathbf{3}
  $$

---

### Walkthrough: Signed Negative Example ($a = -2, b = 3$)
1. **Masking:**
   - $a = -2 \ \& \ \texttt{0xFFFFFFFF} = \texttt{0xFFFFFFFE}$
   - $b = 3 \ \& \ \texttt{0xFFFFFFFF} = \texttt{0x00000003}$
2. **Iteration 1:**
   - $a \ \& \ b = \texttt{0xFFFFFFFE} \ \& \ \texttt{3} = \texttt{2}$
   - $carry = (2 \ll 1) = \mathbf{4}$
   - $a = \texttt{0xFFFFFFFE} \oplus 3 = \mathbf{\texttt{0xFFFFFFFD}}$
   - $b = 4$
3. **Subsequent Iterations:**
   - Carries propagate leftward until $b$ becomes $0$ and $a = \mathbf{1}$.
4. **Sign Check:**
   - $1 < \texttt{0x80000000} \implies$ returns $\mathbf{1}$!

---

## 4. Complete Execution Trace

```text
a = 1, b = 2

Initial Masking:
a = 1 & 0xFFFFFFFF = 0b...0001
b = 2 & 0xFFFFFFFF = 0b...0010

Iteration 1:
  carry = ((a & b) << 1) & 0xFFFFFFFF = (0 << 1) = 0
  a = a ^ b = 1 ^ 2 = 3
  b = carry = 0

Loop Exit (b == 0)
Sign check: 3 < 0x80000000 -> Return 3
```

| Iteration | Variable $a$ (Hex / Binary) | Variable $b$ (Hex / Binary) | Bitwise AND $a \ \& \ b$ | Carry $((a \ \& \ b) \ll 1)$ | New Sum $a \oplus b$ | Loop Status |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Init | `0x00000001` ($0001_2$) | `0x00000002` ($0010_2$) | - | - | - | Active |
| **1** | **`0x00000001`** | **`0x00000002`** | **`0`** | **`0`** | **`0x00000003` ($0011_2$)** | **$b \to 0$ (Exit)** |
| **Final** | **`3`** | **`0`** | - | - | - | **Terminated** |

---

## 5. Algorithmic Correctness

**Soundness.** For any bit position $p$, adding bits $a_p$ and $b_p$ produces a value in $\{0, 1, 2\}$. The low bit is $a_p \oplus b_p$ (sum bit at position $p$), and the high bit is $a_p \land b_p$ (carry bit into position $p+1$). Thus, the arithmetic value $(a \oplus b) + ((a \land b) \ll 1)$ is identically equal to $a + b$. Replacing $(a, b)$ with this pair preserves the mathematical sum at every iteration.

**Completeness.** Each time a carry is shifted left, the lowest position containing a carry increases strictly by at least $1$. In a 32-bit register, carries can shift at most 32 times before spilling out of the 32nd bit. Hence, $b$ is guaranteed to reach $0$ in at most 32 iterations, at which point $a$ holds the exact sum.

---

## 6. Traps This Instance Exposes

- **Infinite Loop in Python on Negative Numbers:** In Python, `-1 << 1` shifts negative numbers infinitely without dropping high bits. Applying `& 0xFFFFFFFF` to clamp calculations to 32 bits is strictly required.
- **Signed Representation Decoding:** A 32-bit value like `0xFFFFFFFF` represents $-1$ in signed two's complement. If returned directly, Python treats it as the positive number $4,294,967,295$. The conditional `~(a ^ 0xFFFFFFFF)` correctly restores negative signs.
- **Precedence of Operators:** Bitwise shift `<<` has lower precedence than bitwise AND `&` in some languages, and bitwise XOR `^` has lower precedence than addition. Using explicit parentheses around `((a & b) << 1)` prevents precedence bugs.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(W)$, where $W = 32$ is the bit width of the integer data type. Carries shift left by at least one bit per iteration, guaranteeing at most 32 loop iterations. Overall time is strictly $O(1)$.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary space, using only three local 32-bit scalar integer variables (`a`, `b`, `carry`).
