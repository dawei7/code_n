# Guided Example: UTF-8 Validation

We trace the step-by-step bitwise UTF-8 finite-state machine (FSM), leading-byte header decoding via bit-shift prefix masking ($v \gg 7, v \gg 5, v \gg 4, v \gg 3$), continuation byte verification ($v \gg 6 == 0b10$), and trailing completeness verification ($cnt == 0$) on representative byte sequences:

- **Input:** $data = [197, 130, 1]$
- **Required output:** `true`
  - Binary representations (8-bit):
    - $197 = 11000101_2$
    - $130 = 10000010_2$
    - $1 = 00000001_2$
  - Step 1 ($v = 197$):
    - $cnt == 0$, test header prefixes:
      - $197 \gg 5 = 110_2 == 0b110 \implies$ Valid 2-byte sequence header!
      - Sets remaining continuation bytes required: $cnt = 1$
  - Step 2 ($v = 130$):
    - $cnt = 1 > 0$, continuation expected:
      - $130 \gg 6 = 10_2 == 0b10 \implies$ Valid continuation byte!
      - Decrement: $cnt = 1 - 1 = 0$
  - Step 3 ($v = 1$):
    - $cnt == 0$, test header prefixes:
      - $1 \gg 7 = 0_2 == 0b0 \implies$ Valid 1-byte ASCII character!
      - $cnt$ remains $0$
  - Stream completes with $cnt == 0 \implies$ Return `true`
- **Invalid Continuation Byte:** $data = [235, 140, 4] \implies \text{false}$
  - $235 = 11101011_2$ (3-byte header, needs 2 continuations, $cnt = 2$)
  - $140 = 10001100_2$ ($10xxxxxx_2$, valid continuation, $cnt = 1$)
  - $4 = 00000100_2$ ($00xxxxxx_2 \ne 10xxxxxx_2$, invalid continuation) $\implies$ Immediate return `false`
- **Truncated Sequence:** $data = [197] \implies$ ends with $cnt = 1 \ne 0 \implies \text{false}$

This instance demonstrates binary protocol decoding using bit-manipulation state machines, mathematically proves why prefix shifting cleanly isolates the RFC 3629 UTF-8 grammar rules without allocating string buffers, and derives $O(N)$ linear time and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an array of integers $data = [197, 130, 1]$ where each integer represents 1 byte (least significant 8 bits):
Determine whether it represents a valid UTF-8 encoded sequence:

```text
UTF-8 Grammar Rules (RFC 3629):
Number of Bytes | UTF-8 Octet Sequence (Binary)
----------------+------------------------------------------------
1 byte          | 0xxxxxxx
2 bytes         | 110xxxxx 10xxxxxx
3 bytes         | 1110xxxx 10xxxxxx 10xxxxxx
4 bytes         | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

Input Data: [197, 130, 1]
197 = 11000101  (Starts with 110 -> 2-byte header, expects 1 continuation)
130 = 10000010  (Starts with 10  -> Valid continuation byte!)
1   = 00000001  (Starts with 0   -> Valid 1-byte ASCII character)

Result: All bytes legally formatted -> Output: true
```

---

## 2. Conceptual Foundation & Invariants

### 1. The FSM State Variable:
Maintain integer counter `cnt = 0`:
- When `cnt == 0`: The current byte is the **header** of a new UTF-8 character.
- When `cnt > 0`: The current byte must be a **continuation byte** (`10xxxxxx`).

### 2. Prefix Inspection via Bit Shifts:
For an 8-bit integer $v$:
1. **Continuation Byte Check (`cnt > 0`):**
   - Shift right by 6 bits ($v \gg 6$): isolates the top 2 bits.
   - If $v \gg 6 \ne 0b10$ ($10_2 = 2$): **Invalid continuation**. Return `False`.
   - Else: consume continuation byte: $cnt \leftarrow cnt - 1$.

2. **Header Byte Check (`cnt == 0`):**
   - **1-byte char:** $v \gg 7 == 0b0 \implies cnt \leftarrow 0$.
   - **2-byte char:** $v \gg 5 == 0b110 \implies cnt \leftarrow 1$.
   - **3-byte char:** $v \gg 4 == 0b1110 \implies cnt \leftarrow 2$.
   - **4-byte char:** $v \gg 3 == 0b11110 \implies cnt \leftarrow 3$.
   - **Any other pattern:** (e.g. orphan continuation `10xxxxxx` or $> 4$ bytes `11111xxx`): Return `False`.

3. **Terminal Validity:**
   After the loop, return `cnt == 0` (ensuring no multi-byte character was left truncated).

> **Invariant.** After processing each byte, `cnt` represents the exact number of continuation bytes remaining before the current character is completely decoded.

---

## 3. Step-by-Step Worked Execution

We trace $data = [197, 130, 1]$:
Initial: $cnt = 0$.

---

### Step 1: Byte 0 ($v = 197$)
- Value: $197 = 11000101_2$.
- State: $cnt == 0$ (Expects header).
- Evaluate prefix shifts:
  - $197 \gg 7 = 00000001_2 \ne 0$.
  - $197 \gg 5$:
    $$
    11000101_2 \gg 5 = 110_2 = \mathbf{0b110}
    $$
- Match: **2-byte character header**!
- Set required continuations:
  $$
  cnt \leftarrow \mathbf{1}
  $$

---

### Step 2: Byte 1 ($v = 130$)
- Value: $130 = 10000010_2$.
- State: $cnt = 1 > 0$ (Expects continuation).
- Evaluate continuation prefix:
  $$
  130 \gg 6 = 10000010_2 \gg 6 = 10_2 = \mathbf{0b10}
  $$
- Check: matches $0b10$ (**True**).
- Consume continuation byte:
  $$
  cnt \leftarrow 1 - 1 = \mathbf{0}
  $$
- 2-byte character successfully completed!

---

### Step 3: Byte 2 ($v = 1$)
- Value: $1 = 00000001_2$.
- State: $cnt == 0$ (Expects header).
- Evaluate prefix shift:
  $$
  1 \gg 7 = 00000001_2 \gg 7 = 0_2 = \mathbf{0b0}
  $$
- Match: **1-byte ASCII character**!
- Set required continuations:
  $$
  cnt \leftarrow \mathbf{0}
  $$
- 1-byte character successfully completed!

---

### Step 4: Stream Termination
All bytes processed. Check final state:
$$
cnt == 0 \iff 0 == 0 \quad (\mathbf{True})
$$
Return:
$$
\mathbf{\text{True}}
$$

---

## 4. Complete Execution Trace

```text
data = [197, 130, 1]

Byte 0: v = 197 (11000101)
  cnt == 0 -> v >> 5 == 0b110 -> 2-byte header -> cnt = 1

Byte 1: v = 130 (10000010)
  cnt > 0  -> v >> 6 == 0b10  -> valid continuation -> cnt = 0

Byte 2: v = 1   (00000001)
  cnt == 0 -> v >> 7 == 0b0   -> 1-byte header -> cnt = 0

Stream end: cnt == 0 -> Return True
```

| Step | Byte Decimal | Byte Binary (8-bit) | State $cnt$ Before | Bitwise Operation | Resulting Prefix | Character Role | State $cnt$ After |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| 1 | 197 | $11000101_2$ | 0 | $197 \gg 5$ | $110_2$ | 2-byte Header | **1** |
| 2 | 130 | $10000010_2$ | 1 | $130 \gg 6$ | $10_2$ | Continuation Byte | **0** |
| **3** | **1** | **$00000001_2$** | **0** | **$1 \gg 7$** | **$0_2$** | **1-byte ASCII** | **0** |
| **Exit**| - | - | 0 | - | - | Complete ($cnt == 0$) | **`true`** |

---

### Malformed Counterexample ($data = [235, 140, 4]$)

```text
Byte 0: 235 (11101011) -> 235 >> 4 == 0b1110 -> 3-byte header -> cnt = 2
Byte 1: 140 (10001100) -> 140 >> 6 == 0b10   -> valid continuation -> cnt = 1
Byte 2: 4   (00000100) -> 4 >> 6 == 0b00 != 0b10 -> MALFORMED! -> Return False
```

---

## 5. Algorithmic Correctness

**Soundness.** Every valid UTF-8 character must start with a header containing $k$ leading ones ($k \in \{0, 2, 3, 4\}$) followed by a zero, and must be followed by exactly $\max(0, k - 1)$ continuation bytes with prefix `10`. Any departure—such as an invalid header bit pattern, an unexpected continuation byte when $cnt == 0$, an invalid prefix when $cnt > 0$, or an unclosed character at end of stream ($cnt > 0$)—violates the standard and is immediately rejected.

**Completeness.** All legal character lengths (1, 2, 3, 4 bytes) are checked in strictly exhaustive order. By scanning the stream byte-by-byte, any valid sequence of UTF-8 characters leaves $cnt = 0$ at each character boundary, ensuring that all valid inputs return `True`.

---

## 6. Traps This Instance Exposes

- **Orphan Continuation Bytes:** If a byte begins with `10xxxxxx` while $cnt == 0$, it is an illegal orphan continuation byte without a preceding header. The `else: return False` branch correctly catches this.
- **5-byte and 6-byte Sequences:** The original 1993 UTF-8 standard allowed up to 6 bytes, but RFC 3629 permanently restricted UTF-8 to at most 4 bytes. Any byte starting with `11111xxx` is invalid.
- **Truncated Input Streams:** An input like `[197]` has a valid 2-byte header, but ends without its continuation byte. Checking `return cnt == 0` at the end prevents truncated inputs from falsely returning `True`.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of integers in `data`. Each integer is processed once with $O(1)$ constant-time bit shifts and comparisons.
- **Auxiliary Space Complexity:** $O(1)$ strict constant memory, using only the single scalar counter `cnt`.
