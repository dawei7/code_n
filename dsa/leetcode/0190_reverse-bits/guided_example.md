# Guided Example: Reverse Bits

We trace the step-by-step 32-bit fixed-width bitwise extraction, left-accumulator shifting, and divide-and-conquer parallel mask swaps on representative binary integers:

- **Input:** $n = 43261596$ (`00000010100101000001111010011100` in 32-bit binary)
- **Required output:** $964176192$ (`00111001011110000010100101000000` in 32-bit binary)
- **All-Ones Instance:** $n = 4294967295$ (`111...111` in binary) $\implies 4294967295$
- **Unit Bit Instance:** $n = 1$ (`...0001` in binary) $\implies 2147483648$ ($2^{31}$, bit 0 shifts to bit 31)

This instance demonstrates fixed-width 32-bit register manipulation, explains why leading zeroes must be preserved as trailing zeroes, constructs the single-pass shift-and-accumulate loop ($(\text{ans} \ll 1) \mid (n \ \& \ 1)$), and derives the $O(1)$ divide-and-conquer mask optimization for high-throughput calls.

---

## 1. Instance & Teaching Goal

Given a 32-bit unsigned integer $n = 43261596$:
Represented in binary with leading zeroes:
$$
n = \mathbf{00000010100101000001111010011100}_2
$$
Reverse the order of all 32 bits from left to right:
$$
\text{reversed} = \mathbf{00111001011110000010100101000000}_2 = \mathbf{964176192}_{10}
$$

A critical requirement is that the reversal is defined strictly over **all 32 bit positions**, including leading zeroes:
- The 6 leading zeroes of $n$ must become the 6 trailing zeroes of the result.
- Stopping early when $n$ reaches $0$ fails because missing bits are not shifted into higher significance.
The loop must execute exactly 32 times.

---

## 2. Conceptual Foundation & Invariants

### Method A: Shift-and-Accumulate Protocol (32 Iterations)
Initialize $\text{ans} = 0$.

Repeat exactly 32 times:
1. **Shift Accumulator Left:**
   Make room at the least significant position:
   $$
   \text{ans} \leftarrow \text{ans} \ll 1
   $$
2. **Inject Extracted Bit:**
   Extract bit 0 of $n$ and bitwise-OR it into $\text{ans}$:
   $$
   \text{ans} \leftarrow \text{ans} \mid (n \ \& \ 1)
   $$
3. **Shift Input Right:**
   Drop the processed bit from $n$:
   $$
   n \leftarrow n \gg 1
   $$

Return $\text{ans}$.

### Method B: Divide-and-Conquer Parallel Mask Swaps ($O(1)$, 5 Operations)
When called millions of times, bit-by-bit loops can be replaced by parallel bit swaps using precomputed bitmasks:
1. Swap 16-bit halves:
   $$
   n = (n \gg 16) \mid (n \ll 16)
   $$
2. Swap 8-bit bytes:
   $$
   n = ((n \ \& \ \text{0xFF00FF00}) \gg 8) \mid ((n \ \& \ \text{0x00FF00FF}) \ll 8)
   $$
3. Swap 4-bit nibbles:
   $$
   n = ((n \ \& \ \text{0xF0F0F0F0}) \gg 4) \mid ((n \ \& \ \text{0x0F0F0F0F}) \ll 4)
   $$
4. Swap 2-bit pairs:
   $$
   n = ((n \ \& \ \text{0xCCCCCCCC}) \gg 2) \mid ((n \ \& \ \text{0x33333333}) \ll 2)
   $$
5. Swap adjacent bits:
   $$
   n = ((n \ \& \ \text{0xAAAAAAAA}) \gg 1) \mid ((n \ \& \ \text{0x55555555}) \ll 1)
   $$

> **Invariant.** After $k$ iterations of Method A, the first $k$ least significant bits of the original $n$ occupy the $k$ lowest positions of $\text{ans}$ in reversed order. After 32 iterations, all bits reach their exact mirrored positions.

---

## 3. Step-by-Step Worked Execution

We trace the shift accumulation for $n = 43261596$:
Binary suffix of $n$: $\dots \mathbf{11100}_2$.

### Iterations 0 to 4 (Trailing bits of $n$):
- **Iter 0 ($i = 0$):**
  - Bit 0 of $n$: $n \ \& \ 1 = 0$.
  - $\text{ans} = (0 \ll 1) \mid 0 = \mathbf{0}$.
  - $n \leftarrow n \gg 1$.
- **Iter 1 ($i = 1$):**
  - Bit 0 of $n$: $n \ \& \ 1 = 0$.
  - $\text{ans} = (0 \ll 1) \mid 0 = \mathbf{0}$.
  - $n \leftarrow n \gg 1$.
- **Iter 2 ($i = 2$):**
  - Bit 0 of $n$: $n \ \& \ 1 = 1$.
  - $\text{ans} = (0 \ll 1) \mid 1 = \mathbf{1}_2 = 1$.
  - $n \leftarrow n \gg 1$.
- **Iter 3 ($i = 3$):**
  - Bit 0 of $n$: $n \ \& \ 1 = 1$.
  - $\text{ans} = (1 \ll 1) \mid 1 = \mathbf{11}_2 = 3$.
  - $n \leftarrow n \gg 1$.
- **Iter 4 ($i = 4$):**
  - Bit 0 of $n$: $n \ \& \ 1 = 1$.
  - $\text{ans} = (11_2 \ll 1) \mid 1 = \mathbf{111}_2 = 7$.
  - $n \leftarrow n \gg 1$.

*(Notice: The trailing bits `...11100` of $n$ are emerging as the leading bits `00111...` of $\text{ans}$!)*

---

### Continuing Through Iteration 31:
- As iterations continue, each bit is shifted left by 1.
- At iteration 31, the original bit 0 (which was $0$) has been shifted left 31 times to bit position 31.
- The 6 leading zeroes of $n$ are processed in the final 6 iterations ($i = 26 \dots 31$), shifting zeroes into $\text{ans}$ and positioning all bits precisely.

Final value of $\text{ans}$:
$$
\mathbf{00111001011110000010100101000000}_2 = \mathbf{964176192}
$$

---

## 4. Complete Execution Trace

```text
Original n:  00000010100101000001111010011100 (43261596)

Bit Traversal:
  Bits  0- 4: 0, 0, 1, 1, 1 -> ans prefix starts with 00111...
  Bits  5- 9: 0, 1, 0, 0, 1
  Bits 10-14: 1, 1, 1, 1, 0
  ...
  Bits 26-31: 0, 0, 0, 0, 0, 0 -> shifts 6 zeros into ans suffix

Reversed:    00111001011110000010100101000000 (964176192)
```

| Iteration Window | Extracted Bit from $n$ | $\text{ans} \ll 1$ | Injected Bit | Cumulative $\text{ans}$ (Binary Prefix) |
|:---:|:---:|:---:|:---:|:---|
| 0 | 0 | `0` | 0 | `0` |
| 1 | 0 | `00` | 0 | `00` |
| 2 | 1 | `000` | 1 | `001` |
| 3 | 1 | `0010` | 1 | `0011` |
| 4 | 1 | `00110` | 1 | `00111` |
| ... | ... | ... | ... | ... |
| **31** | **0** | - | - | **`00111001011110000010100101000000` (964176192)** |

---

## 5. Algorithmic Correctness

**Soundness.** In bitwise positional arithmetic, each left-shift $(\text{ans} \ll 1)$ multiplies the current accumulated integer by 2. Over 32 iterations, a bit extracted at iteration $i$ is shifted left exactly $31 - i$ times. Thus, the original bit at position $i$ is mapped to destination bit $31 - i$, creating the exact mirror reversal.

**Completeness.** Fixed iteration bounds of exactly 32 ensure that all 32 bit slots are explicitly transferred, properly accounting for leading and trailing zeroes.

---

## 6. Traps This Instance Exposes

- **Terminating When $n == 0$:** If a while loop terminates when $n$ reaches 0 (`while n > 0:`), leading zeroes are omitted, resulting in an incomplete shift and a wrong answer. The loop must iterate exactly 32 times.
- **Signed Integer Sign Extension:** In languages with signed 32-bit integers (e.g. Java), bit 31 set to 1 makes the integer negative. Using logical unsigned right shift (`>>>`) in Java or treating values as 64-bit unsigned integers avoids arithmetic sign preservation bugs.
- **Repeated Optimization:** Calling the function millions of times benefits from the divide-and-conquer parallel mask swap or a 256-entry byte lookup table.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The loop runs for exactly 32 steps, performing $O(1)$ bitwise operations per step. The parallel mask method runs in 5 bitwise operations.
- **Auxiliary Space Complexity:** $O(1)$ constant memory, storing only the scalar integer `ans`.
