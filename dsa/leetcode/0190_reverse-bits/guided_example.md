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

### All 32 Iterations with the Positional Contribution

The prefix view above ends in an ellipsis because the accumulator's binary spelling is long. Writing the same run positionally removes the ellipsis and shows the mechanism exactly: each iteration extracts one bit and places it at the mirrored position $31 - i$, so the accumulator is a sum of distinct powers of two, one per set bit of the input.

| $i$ | Extracted $n \ \& \ 1$ | Destination position $31 - i$ | Contribution $(n \ \& \ 1) \ll (31 - i)$ | $\text{ans}$ afterwards |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 31 | 0 | 0 |
| 1 | 0 | 30 | 0 | 0 |
| 2 | 1 | 29 | 536870912 | 536870912 |
| 3 | 1 | 28 | 268435456 | 805306368 |
| 4 | 1 | 27 | 134217728 | 939524096 |
| 5 | 0 | 26 | 0 | 939524096 |
| 6 | 0 | 25 | 0 | 939524096 |
| 7 | 1 | 24 | 16777216 | 956301312 |
| 8 | 0 | 23 | 0 | 956301312 |
| 9 | 1 | 22 | 4194304 | 960495616 |
| 10 | 1 | 21 | 2097152 | 962592768 |
| 11 | 1 | 20 | 1048576 | 963641344 |
| 12 | 1 | 19 | 524288 | 964165632 |
| 13 | 0 | 18 | 0 | 964165632 |
| 14 | 0 | 17 | 0 | 964165632 |
| 15 | 0 | 16 | 0 | 964165632 |
| 16 | 0 | 15 | 0 | 964165632 |
| 17 | 0 | 14 | 0 | 964165632 |
| 18 | 1 | 13 | 8192 | 964173824 |
| 19 | 0 | 12 | 0 | 964173824 |
| 20 | 1 | 11 | 2048 | 964175872 |
| 21 | 0 | 10 | 0 | 964175872 |
| 22 | 0 | 9 | 0 | 964175872 |
| 23 | 1 | 8 | 256 | 964176128 |
| 24 | 0 | 7 | 0 | 964176128 |
| 25 | 1 | 6 | 64 | 964176192 |
| 26 | 0 | 5 | 0 | 964176192 |
| 27 | 0 | 4 | 0 | 964176192 |
| 28 | 0 | 3 | 0 | 964176192 |
| 29 | 0 | 2 | 0 | 964176192 |
| 30 | 0 | 1 | 0 | 964176192 |
| 31 | 0 | 0 | 0 | 964176192 |

Two facts stand out. First, the last set bit of the input is extracted at $i = 25$, and the six iterations $i = 26 \dots 31$ contribute nothing to the positional sum because they are exactly the six leading zeroes of $n$. In the shift-and-append formulation those same six iterations are the six left shifts that carry the accumulated bits into their final positions, so they are not free: an early-stopping variant that halts once $n$ reaches $0$ stops after $26$ iterations and returns $15065253$, which is the correct $964176192$ divided by $2^6 = 64$. The positional view and the shift-and-append view agree only when all 32 iterations run. Second, every nonzero contribution is a distinct power of two, so no two set bits of $n$ can ever collide in $\text{ans}$ — that distinctness is why the reversal is a bijection on 32-bit words rather than merely a mapping.

---

## 5. Algorithmic Correctness

**Soundness.** In bitwise positional arithmetic, each left-shift $(\text{ans} \ll 1)$ multiplies the current accumulated integer by 2. Over 32 iterations, a bit extracted at iteration $i$ is shifted left exactly $31 - i$ times. Thus, the original bit at position $i$ is mapped to destination bit $31 - i$, creating the exact mirror reversal.

**Completeness.** Fixed iteration bounds of exactly 32 ensure that all 32 bit slots are explicitly transferred, properly accounting for leading and trailing zeroes.

---

## 6. Traps This Instance Exposes

- **Terminating When $n == 0$:** If a while loop terminates when $n$ reaches 0 (`while n > 0:`), leading zeroes are omitted, resulting in an incomplete shift and a wrong answer. The loop must iterate exactly 32 times.
- **Signed Integer Sign Extension:** In languages with signed 32-bit integers (e.g. Java), bit 31 set to 1 makes the integer negative. Using logical unsigned right shift (`>>>`) in Java or treating values as 64-bit unsigned integers avoids arithmetic sign preservation bugs.
- **Repeated Optimization:** Calling the function millions of times benefits from the divide-and-conquer parallel mask swap or a 256-entry byte lookup table.

### Boundary Words and the Fixed-Width Contract

Every boundary value here is decided by the same 32-iteration count, and each row isolates one consequence of that contract:

| Input $n$ | 32-bit pattern | Required result | What the instance settles |
|:---|:---|:---:|:---|
| 0 | `00000000000000000000000000000000` | 0 | all 32 extracted bits are zero, so the reversal of an all-zero word is the same word |
| 1 | `00000000000000000000000000000001` | 2147483648 | the single set bit travels from position 0 to position 31; an early-stopping method returns 1 instead, because it performs one iteration rather than 32 |
| 2 | `00000000000000000000000000000010` | 1073741824 | the same bit one position higher lands at position 30, confirming that the shift amount is exactly $31 - i$ |
| 2147483648 | `10000000000000000000000000000000` | 1 | this word is the previous case reversed, so applying the reversal twice restores the input |
| 4294967295 | `11111111111111111111111111111111` | 4294967295 | with every bit set, the reversed pattern is identical to the original: the all-ones word is a fixed point |
| 65535 | `00000000000000001111111111111111` | 4294901760 | the 16 low bits become the 16 high bits while the 16 leading zeroes become 16 trailing zeroes, which is the half-swap stage in isolation |
| 2147483644 | `01111111111111111111111111111100` | 1073741822 | the second authored sample: its two trailing zeroes move to the leading edge and its two leading zeroes to the trailing edge |
| 43261596 via early stop | `00000010100101000001111010011100` | 15065253 instead of 964176192 | $n$ reaches $0$ after 26 iterations because its bit length is 26, so the six skipped iterations divide the answer by $2^6$ |

The last row is the trap in numeric form. The wrong answer $15065253$ is not garbage — it is the reversal of the *significant* bits only, and it is exactly the correct answer shifted down by the six leading zeroes the early stop ignored. That is why the loop bound is a constant 32 and not a function of the input's magnitude.

### Methods for the Same Reversal

| Method | Work per call | Auxiliary space | Where it wins | Failure mode it invites |
|:---|:---|:---|:---|:---|
| Bit-by-bit loop (Method A) | 32 iterations, each extracting a bit, shifting the accumulator and shifting the input | $O(1)$ | clarity and any call count where 32 steps are irrelevant | it always pays all 32 steps, and terminating on $n = 0$ silently drops the leading zeroes |
| Divide-and-conquer masks (Method B) | exactly 5 mask-and-shift stages, independent of the data | $O(1)$, masks held in registers | millions of calls, or library code where a constant stage count matters | a mistyped mask, or a missing 32-bit truncation after the half-swap stage, corrupts only some inputs, so a few spot checks still pass |
| Byte lookup table | 4 lookups plus 3 shifts and 3 masks | 256 entries, roughly 1 KB | repeated calls when a shared table already exists | the table must be built or shipped before the first call, adding a data dependency the register-only methods avoid |
| Text round trip (format, reverse the characters, parse back) | work proportional to the 32 printed characters plus allocation | temporary text of length 32 | scripting a one-off verification of an expected value | it is not a bitwise method, and the fixed 32-character width must be supplied explicitly or it fails exactly like the early-stopping loop |

The first three rows are all exact; they differ only in constant factors and in the shape of their mistakes. Method B's five stages are the reason it is the method of choice when the reversal is called per-pixel or per-packet: its cost does not depend on the input at all, while the loop's 32 steps do not shrink even for a word with a single set bit.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The loop runs for exactly 32 steps, performing $O(1)$ bitwise operations per step. The parallel mask method runs in 5 bitwise operations.
- **Auxiliary Space Complexity:** $O(1)$ constant memory, storing only the scalar integer `ans`.
