# Guided Example: Excel Sheet Column Number

We trace the step-by-step left-to-right Horner's polynomial accumulation converting bijective base-26 titles to integers on representative string instances:

- **Input:** $\text{columnTitle} = \text{"ZY"}$
- **Required output:** $701$ ($26 \times 26 + 25 = 676 + 25 = 701$)
- **Two-Digit Example:** $\text{columnTitle} = \text{"AB"} \implies 28$ ($1 \times 26 + 2 = 28$)
- **Base Single Letter Instance:** $\text{columnTitle} = \text{"A"} \implies 1$
- **Full 32-Bit Max Column Instance:** $\text{columnTitle} = \text{"FXSHRXW"} \implies 2147483647$ ($2^{31} - 1$)

This instance demonstrates left-to-right positional digit accumulation using Horner's polynomial evaluation ($\text{ans} \times 26 + \text{digit}$), maps uppercase ASCII characters onto 1-indexed values $[1, 26]$, and executes in $O(L)$ time with strictly $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given a string representing an Excel sheet column title:
$$
\text{columnTitle} = \text{"ZY"}
$$
Compute its corresponding 1-indexed integer column number:
$$
\text{"ZY"} \implies \mathbf{701}
$$

In standard positional decimal representation, string `"35"` evaluates as $3 \times 10^1 + 5 \times 10^0 = 35$.
In Excel column notation:
- The base is $26$.
- The digit alphabet consists of $\{ \text{'A'} \dots \text{'Z'} \}$, mapped to $\{ 1 \dots 26 \}$ (there is no zero symbol).
- For a string of length $L$ with digit values $d_0, d_1, \dots, d_{L-1}$:
  $$
  \text{Value} = \sum_{i=0}^{L-1} d_i \cdot 26^{L - 1 - i}
  $$
Rather than computing powers of 26 from right to left, **Horner's Rule** accumulates the polynomial from left to right in a single pass: each incoming character shifts the current prefix by $\times 26$ and adds the new 1-indexed digit value.

---

## 2. Conceptual Foundation & Invariants

### Horner's Rule Protocol for Bijective Base-26
Initialize scalar accumulator:
$$
\text{ans} = 0
$$

For each character $c \in \text{columnTitle}$:
1. **Convert Character to 1-Indexed Digit:**
   $$
   d = \text{ord}(c) - \text{ord}(\text{'A'}) + 1 \in [1, 26]
   $$
2. **Shift and Accumulate:**
   Multiply existing prefix by base 26 and add digit $d$:
   $$
   \text{ans} \leftarrow \text{ans} \times 26 + d
   $$

Return `ans`.

> **Invariant.** After processing the prefix of length $k$, `ans` stores the exact column number corresponding to the substring $\text{columnTitle}[0 \dots k-1]$.

---

## 3. Step-by-Step Worked Execution

We trace the polynomial evaluation on $\text{columnTitle} = \text{"ZY"}$:

### Initialization
- $\text{ans} = 0$.

---

### Step 1: Character `'Z'` (Index 0)
- Compute 1-indexed digit value:
  $$
  d = \text{ord}(\text{'Z'}) - \text{ord}(\text{'A'}) + 1 = 90 - 65 + 1 = \mathbf{26}
  $$
- Shift and accumulate:
  $$
  \text{ans} \leftarrow 0 \times 26 + 26 = \mathbf{26}
  $$
- Current prefix `"Z"` represents column $26$.

---

### Step 2: Character `'Y'` (Index 1)
- Compute 1-indexed digit value:
  $$
  d = \text{ord}(\text{'Y'}) - \text{ord}(\text{'A'}) + 1 = 89 - 65 + 1 = \mathbf{25}
  $$
- Shift and accumulate:
  $$
  \text{ans} \leftarrow 26 \times 26 + 25 = 676 + 25 = \mathbf{701}
  $$
- Current prefix `"ZY"` represents column $701$.

---

### Termination
- End of string reached.
- Return $\text{ans} = \mathbf{701}$.

---

## 4. Complete Execution Trace

```text
Input: "ZY"
Initial: ans = 0

Char 'Z': digit = 90 - 65 + 1 = 26.  ans = 0 * 26 + 26 = 26
Char 'Y': digit = 89 - 65 + 1 = 25.  ans = 26 * 26 + 25 = 676 + 25 = 701

Final Result: 701
```

| Step | Processed Prefix | Active Character | ASCII Difference $\text{ord}(c) - \text{ord}(\text{'A'})$ | Digit Value $d (+1)$ | Horner Calculation $\text{ans} \times 26 + d$ | Updated $\text{ans}$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Start | `""` | - | - | - | - | 0 |
| 1 | `"Z"` | `'Z'` | $90 - 65 = 25$ | 26 | $0 \times 26 + 26$ | 26 |
| **2** | **`"ZY"`** | **`'Y'`** | **$89 - 65 = 24$** | **25** | **$26 \times 26 + 25 = 676 + 25$** | **701 (Final)** |

### Contrast: Title `"AB"`
- Char 1 (`'A'`): $d = 1 \implies \text{ans} = 0 \times 26 + 1 = 1$.
- Char 2 (`'B'`): $d = 2 \implies \text{ans} = 1 \times 26 + 2 = \mathbf{28}$.

### Prefix-by-Prefix State for the Longest Valid Input

The invariant is easiest to believe when the input is long enough that no single step can be checked by inspection. Here is the full accumulation for $\text{columnTitle} = \text{"FXSHRXW"}$, the largest title that still fits a 32-bit signed integer:

| Index $i$ | Character | $\text{ord}(c) - \text{ord}(\text{'A'})$ | Digit Value $d$ | Prefix Read So Far | Horner Step $\text{ans} \times 26 + d$ | $\text{ans}$ after the step | Column number the prefix denotes |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | `'F'` | 5 | 6 | `"F"` | $0 \times 26 + 6$ | 6 | 6 |
| 1 | `'X'` | 23 | 24 | `"FX"` | $6 \times 26 + 24$ | 180 | 180 |
| 2 | `'S'` | 18 | 19 | `"FXS"` | $180 \times 26 + 19$ | 4699 | 4699 |
| 3 | `'H'` | 7 | 8 | `"FXSH"` | $4699 \times 26 + 8$ | 122182 | 122182 |
| 4 | `'R'` | 17 | 18 | `"FXSHR"` | $122182 \times 26 + 18$ | 3176750 | 3176750 |
| 5 | `'X'` | 23 | 24 | `"FXSHRX"` | $3176750 \times 26 + 24$ | 82595524 | 82595524 |
| 6 | `'W'` | 22 | 23 | `"FXSHRXW"` | $82595524 \times 26 + 23$ | **2147483647** | **$2^{31} - 1$** |

Two things are worth extracting from the last row. First, every prefix is itself a valid column number, which is exactly what the invariant asserts — the accumulator never holds a partial quantity, only the value of what has been read. Second, the growth factor per character is $26$, so after seven characters the value has grown by $26^{7} \approx 8.03 \times 10^{9}$; the fact that the true result stops at $2.14 \times 10^{9}$ is a property of which digits appear, not of the width of the accumulator.

---

## 5. Algorithmic Correctness

**Soundness.** Horner's rule evaluates polynomials of degree $L - 1$ iteratively without explicit exponentiation. By multiplying the running sum by 26 at each step, a digit processed at index $i$ is multiplied by $26$ exactly $(L - 1 - i)$ times by the end of the loop, matching the mathematical definition $\sum_{i=0}^{L-1} d_i \cdot 26^{L - 1 - i}$.

**Completeness.** Every character in the input string is visited in order from left to right. No powers or positions are skipped.

---

## 6. Traps This Instance Exposes

- **Failing to Add 1 for 1-Indexed Digits:** Calculating `ord(c) - ord('A')` yields $0$ for `'A'`, which is standard base-26 but incorrect for Excel! `'A'` must map to $1$, `'B'` to $2$, and `'Z'` to $26$.
- **Right-to-Left Exponentiation Overhead:** Calculating powers $26^0, 26^1, \dots$ from the right requires keeping track of an exponent or calling power functions, which introduces unnecessary arithmetic overhead compared to Horner's left-to-right multiplication.
- **32-Bit Overflow Considerations:** The maximum input `"FXSHRXW"` corresponds to $2^{31} - 1 = 2147483647$, fitting cleanly inside a 32-bit signed integer.

### Boundary Scenarios This Instance Sits Next To

| Title | Length $L$ | Digit values | Expected | Accumulation | Why the boundary matters |
|:---|:---:|:---|:---:|:---|:---|
| `"A"` | 1 | 1 | 1 | $0 \times 26 + 1$ | Smallest legal title; the 1-index offset is the only reason the answer is not $0$ |
| `"Z"` | 1 | 26 | 26 | $0 \times 26 + 26$ | Largest single-character title; a 0-indexed alphabet would report $25$ here |
| `"AA"` | 2 | 1, 1 | 27 | $1 \times 26 + 1$ | First two-character title; the leading `'A'` contributes a full $26$, not nothing |
| `"AB"` | 2 | 1, 2 | 28 | $1 \times 26 + 2$ | Shows the low digit advances while the high digit stays fixed |
| `"ZY"` | 2 | 26, 25 | 701 | $26 \times 26 + 25$ | Largest two-character title below the final block; both digits sit near their maximum |
| `"ZZ"` | 2 | 26, 26 | 702 | $26 \times 26 + 26$ | Last two-character title; the entire two-character range is exactly $[1, 702]$ |
| `"AAA"` | 3 | 1, 1, 1 | 703 | $(1 \times 26 + 1) \times 26 + 1$ | First three-character title, proving the third position is worth $26^{2} = 676$ |
| `"FXSHRXW"` | 7 | 6, 24, 19, 8, 18, 24, 23 | 2147483647 | Seven Horner steps ending at $2^{31} - 1$ | Largest title the input contract allows; any longer string would exceed the 32-bit column range |

### Alternative Approaches on These Titles

| Approach | `"ZY"` | `"FXSHRXW"` | Time | Auxiliary space | Why it is worse or wrong |
|:---|:---:|:---:|:---:|:---:|:---|
| 0-indexed alphabet with $26^{L-1-i}$ weights | 675 | 2147483646 (one short) | $O(L)$ | $O(1)$ | Off by one on every title, because Excel's alphabet has $26$ digits with no zero symbol |
| Left-to-right Horner accumulation | 701 | 2147483647 | $O(L)$ | $O(1)$ | Correct and never forms a power of 26 explicitly |
| Right-to-left accumulation with a running power | 701 | 2147483647 | $O(L)$ | $O(1)$ | Correct, but it must maintain and re-multiply a separate $26^{k}$ variable that Horner's shift already provides |
| Explicit power calls per position | 701 | 2147483647 | $O(L^{2})$ with repeated squaring-by-multiplication | $O(1)$ | Recomputes each $26^{L-1-i}$ from scratch, doing asymptotically more arithmetic than Horner's single running multiply |
| Lookup table over all valid titles | 701 | 2147483647 | $O(L)$ to look up the whole string | $O(26^{7})$ to store every title | The title space reaches $2^{31} - 1$ entries, so enumeration is not a feasible substitute for seven multiplications |
| Recursive prefix evaluation | 701 | 2147483647 | $O(L)$ | $O(L)$ call stack | Same arithmetic with a stack that the iterative accumulator avoids entirely |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(L)$, where $L$ is the length of `columnTitle`. For 32-bit valid inputs, $L \le 7$. The loop runs at most 7 times, performing $O(1)$ arithmetic operations per step.
- **Auxiliary Space Complexity:** $O(1)$ strictly constant extra space, utilizing only scalar integer accumulator `ans`.
