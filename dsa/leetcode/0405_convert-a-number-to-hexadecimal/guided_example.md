# Guided Example: Convert a Number to Hexadecimal

We trace the step-by-step 32-bit two's complement nibble decomposition, high-to-low bit-shifting ($x = (num \gg (4 \times i)) \ \& \ 0\text{xF}$), leading-zero suppression (`if s or x != 0`), two's complement negative integer conversion, and base-16 character translation on representative numerical instances:

- **Input:** $num = 26$
- **Required output:** `"1a"`
  - 32-bit binary representation:
    $$
    26 = 0000\;0000\;0000\;0000\;0000\;0000\;0001\;1010_2
    $$
  - Total nibbles: $32 / 4 = 8$ (indices $i = 7 \dots 0$)
  - Step-by-step extraction:
    - $i = 7 \dots 2$: $x = 0$, list `s` empty $\implies$ skipped as leading zeros
    - $i = 1$ (bits 4-7): $(26 \gg 4) \ \& \ 0\text{xF} = 1 \ \& \ 15 = 1 \implies$ append `chars[1] = '1'`, `s = ['1']`
    - $i = 0$ (bits 0-3): $(26 \gg 0) \ \& \ 0\text{xF} = 26 \ \& \ 15 = 10 \implies$ append `chars[10] = 'a'`, `s = ['1', 'a']`
  - Concatenation: $\mathbf{\text{"1a"}}$
- **Two's Complement Negative Integer:** $num = -1$
  - In 32-bit two's complement, $-1 = 1111\dots 1111_2$ (all 32 bits are 1)
  - Every nibble $i \in [7 \dots 0]$ yields $( -1 \gg 4i ) \ \& \ 0\text{xF} = 15 \implies \text{'f'}$
  - Result: $\mathbf{\text{"ffffffff"}}$
- **Zero Input:** $num = 0 \implies \mathbf{\text{"0"}}$

This instance demonstrates bitwise extraction of discrete base-$2^k$ representations, mathematically proves why bit-shifting natively supports two's complement arithmetic without special-case sign branching, and confirms $O(1)$ constant runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a 32-bit signed integer $num = 26$:
Convert it to its lowercase hexadecimal representation without using built-in library functions:

```text
Decimal 26:
Binary (32-bit):  0000 0000 0000 0000 0000 0000 0001 1010
Nibble Index i:    7    6    5    4    3    2     1    0
Nibble Value:      0    0    0    0    0    0     1   10
Hex Digit:         -    -    -    -    -    -    '1'  'a'

Result: "1a"
```

### Why Nibbles Naturally Map to Hexadecimal
- In base 16, each hex digit spans values $[0, 15]$, which corresponds to exactly $4$ binary bits ($2^4 = 16$), called a **nibble**.
- A 32-bit integer is partitioned into exactly $32 / 4 = 8$ nibbles.
- To inspect nibble $i$ ($0 \le i \le 7$):
  1. Shift $num$ right by $4 \times i$ bits to move nibble $i$ to the lowest 4 positions.
  2. Mask with bitwise AND $0\text{xF} = 1111_2 = 15$ to isolate those 4 bits.
- Because Python represents negative numbers using infinite sign extension, right-shifting a negative integer and masking with `& 0xF` directly extracts the correct two's complement bits!

---

## 2. Conceptual Foundation & Invariants

### 1. Hex Alphabet Lookup:
$$
chars = \text{"0123456789abcdef"}
$$

### 2. Nibble Extraction Formula:
For $i$ descending from $7$ to $0$:
$$
x = (num \gg (4 \times i)) \ \& \ 0\text{xF}
$$
- If $s$ is empty and $x == 0$:
  This is a leading zero. Skip it.
- Else:
  Append $chars[x]$ to accumulator list $s$.

### 3. Edge Cases:
- $num == 0$: Loop would skip all 8 zeros. Explicit check returns `"0"`.
- $num < 0$: The most significant bit is 1, so nibble $i = 7$ is non-zero ($\ge 8$), immediately ending the leading-zero phase and outputting all 8 hex digits.

> **Invariant.** After processing nibble $i$, `s` contains the sequence of all non-trivial hexadecimal digits from nibble 7 down to nibble $i$ without any leading zeros.

---

## 3. Step-by-Step Worked Execution

We trace $num = 26$:
$chars = \text{"0123456789abcdef"}$. Initial: $s = []$.

---

### Step 1: Nibbles $i = 7$ Down to $i = 2$
For all $i \in \{7, 6, 5, 4, 3, 2\}$:
$$
x = (26 \gg (4 \times i)) \ \& \ 0\text{xF} = 0 \ \& \ 15 = \mathbf{0}
$$
- Guard check: `s` is empty and $x == 0$.
- Skip leading zero. `s` remains empty.

---

### Step 2: Nibble $i = 1$ (Bits 4 to 7)
- Shift right by $4 \times 1 = 4$ bits:
  $$
  26 \gg 4 = 1
  $$
- Mask with $0\text{xF}$:
  $$
  x = 1 \ \& \ 15 = \mathbf{1}
  $$
- Guard check: $x \ne 0$.
- Append $chars[1] = \text{'1'}$:
  $$
  s = [\text{'1'}]
  $$

---

### Step 3: Nibble $i = 0$ (Bits 0 to 3)
- Shift right by $4 \times 0 = 0$ bits:
  $$
  26 \gg 0 = 26
  $$
- Mask with $0\text{xF}$:
  $$
  x = 26 \ \& \ 15 = \mathbf{10}
  $$
- Guard check: `s` is non-empty (`len(s) == 1`).
- Append $chars[10] = \text{'a'}$:
  $$
  s = [\text{'1'}, \; \text{'a'}]
  $$

---

### Step 4: String Assembly
Join characters in $s$:
$$
\text{''.join}(s) = \mathbf{\text{"1a"}}
$$

---

## 4. Complete Execution Trace

```text
num = 26
i = 7: (26 >> 28) & 0xF = 0 -> s is empty -> skip
i = 6: (26 >> 24) & 0xF = 0 -> s is empty -> skip
i = 5: (26 >> 20) & 0xF = 0 -> s is empty -> skip
i = 4: (26 >> 16) & 0xF = 0 -> s is empty -> skip
i = 3: (26 >> 12) & 0xF = 0 -> s is empty -> skip
i = 2: (26 >>  8) & 0xF = 0 -> s is empty -> skip
i = 1: (26 >>  4) & 0xF = 1 -> x != 0     -> s.append('1')
i = 0: (26 >>  0) & 0xF = 10 -> s not empty -> s.append('a')

Output: "1a"
```

| Nibble Index $i$ | Bit Range $[4i, 4i+3]$ | Shifted Value $num \gg 4i$ | Masked Nibble $x$ | Hex Char $chars[x]$ | Leading Zero Skipped? | Accumulator $s$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 7 | [28, 31] | 0 | 0 | `'0'` | Yes (Leading) | `[]` |
| 6 | [24, 27] | 0 | 0 | `'0'` | Yes (Leading) | `[]` |
| 5 | [20, 23] | 0 | 0 | `'0'` | Yes (Leading) | `[]` |
| 4 | [16, 19] | 0 | 0 | `'0'` | Yes (Leading) | `[]` |
| 3 | [12, 15] | 0 | 0 | `'0'` | Yes (Leading) | `[]` |
| 2 | [8, 11] | 0 | 0 | `'0'` | Yes (Leading) | `[]` |
| **1** | **[4, 7]** | **1** | **1** | **`'1'`** | **No ($x \ne 0$)** | **`['1']`** |
| **0** | **[0, 3]** | **26** | **10** | **`'a'`** | **No ($s$ non-empty)**| **`['1', 'a']`** |
| **Exit** | - | - | - | - | - | **`"1a"`** |

---

### Negative Number Trace ($num = -1$)

```text
num = -1 (32-bit two's complement: 0xFFFFFFFF)
All 8 nibbles have x = 15:
i = 7: (-1 >> 28) & 0xF = 15 -> 'f'
i = 6: (-1 >> 24) & 0xF = 15 -> 'f'
...
i = 0: (-1 >>  0) & 0xF = 15 -> 'f'

Output: "ffffffff"
```

---

## 5. Algorithmic Correctness

**Soundness.** In any positional numeral system with base $B = 2^b$, every group of $b$ bits maps uniquely to one digit. For base 16, $b = 4$. Shifting by multiples of 4 and masking with $0\text{xF}$ extracts these exact independent coefficients without rounding errors. The condition `s or x != 0` ensures that no prefix of zeros is retained while guaranteeing that all legitimate internal zeros (e.g. in $16 = 0\text{x}10$) are preserved.

**Completeness.** All 8 nibbles of any 32-bit integer are inspected in descending significant order. Two's complement representation is preserved naturally under bitwise operations, ensuring accurate conversion for both positive and negative integers in $[-2^{31}, 2^{31} - 1]$.

---

## 6. Traps This Instance Exposes

- **Built-in `hex()` Disqualification:** Calling Python's built-in `hex(-1)` outputs `"-0x1"`, which violates both the prohibition of built-in helpers and the problem requirement to output two's complement hexadecimal without negative signs (`"ffffffff"`).
- **Internal Zeros Stripping:** Naively skipping all zeros would turn $16$ (`0x10`) into `"1"`. Checking `if s or x != 0` correctly differentiates leading zeros from internal zeros.
- **Zero Input Boundary:** When $num = 0$, all 8 nibbles are zero. Without the early guard `if num == 0: return '0'`, the function would return an empty string `""`.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$ constant time.
  - The loop iterates exactly 8 times (fixed for 32-bit integers).
  - Each iteration performs $O(1)$ constant-time bit shifts, bitwise ANDs, and lookups.
  - Overall time is $O(1)$, executing in $< 0.01$ ms.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary space, storing at most 8 characters in array $s$.
