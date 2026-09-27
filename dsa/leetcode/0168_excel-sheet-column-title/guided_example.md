# Guided Example: Excel Sheet Column Title

We trace the step-by-step 1-offset bijective base-26 reduction and ASCII character mapping on representative column number instances:

- **Input:** $\text{columnNumber} = 701$
- **Required output:** `"ZY"` ($26 \times 26 + 25 = 676 + 25 = 701$)
- **Two-Digit Carry Instance:** $\text{columnNumber} = 28 \implies \text{"AB"}$ ($1 \times 26 + 2 = 28$)
- **Single Letter Edge Instance:** $\text{columnNumber} = 26 \implies \text{"Z"}$
- **First Element Instance:** $\text{columnNumber} = 1 \implies \text{"A"}$

This instance demonstrates bijective base-26 numeral systems without a zero symbol, proves why decrementing the number by 1 prior to modulus ($\text{num} \leftarrow \text{num} - 1$) perfectly maps $[1, 26]$ onto standard $[0, 25]$ ASCII offsets, and operates in $O(\log_{26} N)$ logarithmic time.

---

## 1. Instance & Teaching Goal

Given a positive integer $\text{columnNumber} = 701$:
Find its corresponding Excel sheet column title:
$$
701 \implies \mathbf{\text{"ZY"}}
$$

Standard positional base-$B$ systems (like base 10 or base 2) use digits $\{0, 1, \dots, B-1\}$.
Excel column titles use **Bijective Base-26**:
- Digits are represented by $\{ \text{'A'}, \text{'B'}, \dots, \text{'Z'} \}$ with values $1 \dots 26$.
- There is **no symbol for zero**!
- After `'Z'` (26), the sequence transitions to `"AA"` (27), not `"A0"`.
- At column 26, standard modulo $26 \pmod{26} = 0$, which has no valid letter mapping.

To bridge 1-indexed bijective base-26 to standard 0-indexed modular arithmetic:
At each digit extraction, decrement `columnNumber` by 1:
$$
\text{rem} = (\text{columnNumber} - 1) \pmod{26} \in [0, 25]
$$
This shifts $\{1 \dots 26\}$ to $\{0 \dots 25\}$, mapping $0 \to \text{'A'}, \dots, 25 \to \text{'Z'}$.
The quotient $\lfloor (\text{columnNumber} - 1) / 26 \rfloor$ becomes the input for the next higher-order digit.

---

## 2. Conceptual Foundation & Invariants

### The Bijective Base-26 Shift Invariant
Let $N = \text{columnNumber}$.
Maintain a list of character tokens `title = []`.

While $N > 0$:
1. **Subtract Offset 1:**
   Adjust the current least significant digit from 1-indexed to 0-indexed:
   $$
   N \leftarrow N - 1
   $$
2. **Extract Character:**
   Compute remainder:
   $$
   \text{rem} = N \pmod{26}
   $$
   Convert to uppercase ASCII character:
   $$
   \text{char} = \text{chr}(\text{ord}(\text{'A'}) + \text{rem})
   $$
   Append to accumulator:
   $$
   \text{title.append}(\text{char})
   $$
3. **Integer Division for Higher Orders:**
   $$
   N \leftarrow \left\lfloor \frac{N}{26} \right\rfloor
   $$

After the loop, reverse `title` (since digits were extracted from least to most significant):
$$
\text{result} = \text{"".join}(\text{reversed}(\text{title}))
$$

> **Invariant.** After each iteration, the sequence in `title` represents the exact suffixes of the bijective base-26 representation, and $N$ represents the exact value of the remaining unexpressed higher-order prefixes.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $\text{columnNumber} = 701$:

### Iteration 1 (Least Significant Digit):
- Start value: $N = 701$.
- Shift offset:
  $$
  N \leftarrow 701 - 1 = \mathbf{700}
  $$
- Compute remainder:
  $$
  \text{rem} = 700 \pmod{26} = \mathbf{24}
  $$
- Map to ASCII:
  $$
  \text{ord}(\text{'A'}) + 24 = 65 + 24 = 89 \implies \text{chr}(89) = \mathbf{\text{'Y'}}
  $$
- Append: `title = ['Y']`.
- Update $N$:
  $$
  N \leftarrow \left\lfloor \frac{700}{26} \right\rfloor = \mathbf{26}
  $$
- $N = 26 > 0$. Continue loop.

---

### Iteration 2 (Next Significant Digit):
- Start value: $N = 26$.
- Shift offset:
  $$
  N \leftarrow 26 - 1 = \mathbf{25}
  $$
- Compute remainder:
  $$
  \text{rem} = 25 \pmod{26} = \mathbf{25}
  $$
- Map to ASCII:
  $$
  \text{ord}(\text{'A'}) + 25 = 65 + 25 = 90 \implies \text{chr}(90) = \mathbf{\text{'Z'}}
  $$
- Append: `title = ['Y', 'Z']`.
- Update $N$:
  $$
  N \leftarrow \left\lfloor \frac{25}{26} \right\rfloor = \mathbf{0}
  $$
- $N == 0$. Loop terminates.

---

### Assembly:
- Raw extracted digits (LSB to MSB): `['Y', 'Z']`.
- Reverse list: `['Z', 'Y']`.
- Output: $\mathbf{\text{"ZY"}}$.

---

## 4. Complete Execution Trace

```text
Input: 701

Iter 1: N = 701 -> N-1 = 700.  700 % 26 = 24 ('Y').  N = 700 // 26 = 26
Iter 2: N = 26  -> N-1 = 25.    25 % 26 = 25 ('Z').  N =  25 // 26 = 0
Reversed: "ZY"
```

| Iteration | Incoming $N$ | Decremented $N - 1$ | Remainder $(N - 1) \pmod{26}$ | Mapped Letter | New $N = \lfloor (N - 1) / 26 \rfloor$ | Cumulative `title` |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | 701 | 700 | 24 | `'Y'` | 26 | `['Y']` |
| **2** | **26** | **25** | **25** | **`'Z'`** | **0** | **`['Y', 'Z']`** |
| **Final** | - | - | - | - | - | **`reversed` $\implies$ `"ZY"`** |

### Contrast: Column 28
- Iter 1: $N = 28 \to 27$. $27 \pmod{26} = 1 \implies \text{'B'}$. $N = 27 // 26 = 1$.
- Iter 2: $N = 1 \to 0$. $0 \pmod{26} = 0 \implies \text{'A'}$. $N = 0 // 26 = 0$.
- Reversed: $\mathbf{\text{"AB"}}$ ($1 \times 26 + 2 = 28$).

### Boundary Scenarios This Instance Sits Next To

The interesting numbers are the ones where the offset decides an entire extra digit, because those are the columns where ordinary base-26 arithmetic breaks:

| $\text{columnNumber}$ | $N - 1$ on iteration 1 | Iteration 1 remainder | Iteration 1 quotient | Continuing quotients | Expected title | Why this value is a boundary |
|:---:|:---:|:---:|:---:|:---|:---:|:---|
| 1 | 0 | 0 $\to$ `'A'` | 0 | loop ends | `"A"` | Smallest legal input; the remaining prefix is already empty |
| 26 | 25 | 25 $\to$ `'Z'` | 0 | loop ends | `"Z"` | Last one-letter title; an ordinary modulo of $26$ would yield digit $0$ with no letter to map |
| 27 | 26 | 0 $\to$ `'A'` | 1 | $1 - 1 = 0 \to$ `'A'` $\to$ quotient $0$ | `"AA"` | First two-letter title, reached only because the offset turned $26$'s carry into a legal digit |
| 28 | 27 | 1 $\to$ `'B'` | 1 | $1 - 1 = 0 \to$ `'A'` $\to$ quotient $0$ | `"AB"` | Shows the carry is a separate digit rather than a change to the low digit |
| 52 | 51 | 25 $\to$ `'Z'` | 1 | $1 - 1 = 0 \to$ `'A'` $\to$ quotient $0$ | `"AZ"` | Last title beginning with `'A'`, closing the first block of $26$ |
| 676 | 675 | 25 $\to$ `'Z'` | 25 | $25 - 1 = 24 \to$ `'Y'` $\to$ quotient $0$ | `"YZ"` | Largest two-letter title with a nonzero leading digit below the final block |
| 701 | 700 | 24 $\to$ `'Y'` | 26 | $26 - 1 = 25 \to$ `'Z'` $\to$ quotient $0$ | `"ZY"` | The second iteration receives exactly $26$, so it needs the offset again to land on `'Z'` |
| 702 | 701 | 25 $\to$ `'Z'` | 26 | $26 - 1 = 25 \to$ `'Z'` $\to$ quotient $0$ | `"ZZ"` | Last two-letter title; both digits sit at the maximum value |
| 703 | 702 | 0 $\to$ `'A'` | 27 | $27 - 1 = 26$: remainder $0 \to$ `'A'`, quotient $1$; then $1 - 1 = 0 \to$ `'A'`, quotient $0$ | `"AAA"` | First three-letter title; two consecutive zero remainders prove the offset applies at every iteration, not once |

Notice that $27$, $52$, $676$, $702$, and $703$ are all values where the low remainder is $0$ or the low digit sits at $25$. Those are precisely the positions where the decrement is load-bearing; the remaining values decode correctly even by coincidence, which is why a single hand-checked example is not enough evidence that the offset is applied correctly.

### How Many Iterations the Value Buys

Each iteration strips exactly one base-26 digit, so the loop count is the title length. Under the stated input ceiling the count is capped at seven:

| Value range | Base-26 digits | Iterations | Example |
|:---|:---:|:---:|:---|
| $1 \le N \le 26$ | 1 | 1 | $26 \to \text{"Z"}$ |
| $27 \le N \le 26^{2} = 676$ | 2 | 2 | $701$ is outside this band, but $676 \to \text{"YZ"}$ takes 2 |
| $677 \le N \le 26^{3} = 17576$ | 3 | 3 | $703 \to \text{"AAA"}$ |
| $26^{6} + 1 \le N \le 26^{7} \approx 8.03 \times 10^{9}$ | 7 | 7 | Any $N$ up to $2^{31} - 1 \approx 2.14 \times 10^{9}$ still fits |

---

## 5. Algorithmic Correctness

**Soundness.** Any positive integer in bijective base-26 can be represented uniquely as $\sum_{i=0}^{k-1} c_i \cdot 26^i$, where $c_i \in \{1, \dots, 26\}$. Subtracting 1 yields $(c_0 - 1) + 26 \sum_{i=1}^{k-1} c_i \cdot 26^{i-1}$, where $c_0 - 1 \in \{0, \dots, 25\}$. Taking modulo 26 isolates $(c_0 - 1)$ exactly, producing the correct ASCII character offset. Dividing by 26 removes $c_0$ and exposes $c_1$.

**Completeness.** Since $N$ decreases by a factor of 26 on each step, $N$ strictly decreases to 0 in $\lceil \log_{26} N \rceil$ iterations, guaranteeing termination for all integers up to $2^{31} - 1$.

---

## 6. Traps This Instance Exposes

- **Failing to Decrement by 1 ($N \pmod{26}$):** If $N = 26$, $26 \pmod{26} = 0$. Without decrementing, 0 maps before `'A'` or requires an awkward special-case check. Decrementing $N - 1$ unifies all numbers uniformly.
- **Decrementing Only Once:** The subtraction $N - 1$ must be performed **at every iteration**, not just before the while loop! Higher-order digits also participate in bijective base-26.
- **Order of Letters:** Modulus extracts the least significant character first. Forgetting to reverse `title` at the end produces inverted output `"YZ"` instead of `"ZY"`.

### Alternative Approaches on These Instances

| Approach | $26$ | $28$ | $701$ | $703$ | Why it breaks or costs more |
|:---|:---:|:---:|:---:|:---:|:---|
| Plain base-26 with `'A'` mapped to $0$ and no offset | `"A0"` (no letter for digit $0$) | `"AB"` | `"ZY"` | `"A0A"` | There is no zero symbol to emit; the failures at $26$ and $703$ are exactly the wrap points, while the two middle columns happen to agree |
| Decrement the input once, then convert in plain base-26 | `"Z"` | `"AB"` | `"ZY"` | `"BBA"` | Correct only while the input has one digit; from $703$ on, the higher-order digits keep their own $1$-offset and the title gains a phantom leading letter |
| Decrement once and repair the result with a manual carry | `"Z"` | `"AB"` | `"ZY"` | Carry propagation cascades through two positions | The repair is the per-iteration offset written badly: every zero digit forces a borrow, so the loop is both simpler and provably uniform |
| Per-iteration offset with `divmod`-style extraction | `"Z"` | `"AB"` | `"ZY"` | `"AAA"` | Matches every boundary in the table because each digit is converted in the same $1$-indexed frame |
| Precomputed lookup table over all columns | `"Z"` | `"AB"` | `"ZY"` | `"AAA"` | The legal input reaches $2^{31} - 1$, so enumerating titles is far larger than the $7$ arithmetic steps the loop needs |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log_{26} N)$, where $N$ is `columnNumber`. For a 32-bit signed integer ($N \le 2^{31} - 1 \approx 2.14 \times 10^9$), the loop runs at most $\lceil \log_{26}(2 \times 10^9) \rceil = 7$ iterations.
- **Auxiliary Space Complexity:** $O(\log_{26} N) \le 7$ characters to store the title output array.
