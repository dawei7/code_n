# Guided Example: Multiply Strings

We trace the step-by-step positional grade-school multiplication on a representative multi-digit string instance:

- **Input:** $\text{num1} = \text{"123"}$, $\text{num2} = \text{"456"}$
- **Required output:** $\text{"56088"}$

This instance demonstrates digit-by-digit convolution without big-integer conversion libraries, index positioning via power-of-ten alignments ($i + j + 1$), backward carry propagation, and stripping non-significant leading zeroes.

---

## 1. Instance & Teaching Goal

Given two non-negative integers $\text{num1}$ of length $M = 3$ and $\text{num2}$ of length $N = 3$ represented as strings, we must compute their product $\text{"123"} \times \text{"456"} = \text{"56088"}$ as a string without converting the input strings directly to built-in arbitrary-precision integers.

Mathematical Property:
The product of an $M$-digit number and an $N$-digit number has at most $M + N$ decimal digits:
$$
\text{Max Digits} = 3 + 3 = 6
$$
We allocate an integer array $\text{res}$ of length $M + N = 6$ initialized to zeroes. Each digit pair $(\text{num1}[i], \text{num2}[j])$ represents:
$$
(\text{num1}[i] \cdot 10^{M - 1 - i}) \times (\text{num2}[j] \cdot 10^{N - 1 - j}) = (\text{num1}[i] \cdot \text{num2}[j]) \cdot 10^{(M + N - 2) - (i + j)}
$$
In a 0-indexed array of length $M + N$, the positional weight $10^{(M + N - 2) - (i + j)}$ maps precisely to array index:
$$
\text{pos} = i + j + 1
$$
and its carry overflows into index $i + j$.

---

## 2. Conceptual Foundation & Invariants

### Two-Phase Multiplication Pipeline
1. **Convolution Phase (Accumulate Products):**
   For every pair $i \in [0, M-1]$ and $j \in [0, N-1]$:
   $$
   \text{res}[i + j + 1] \leftarrow \text{res}[i + j + 1] + (\text{num1}[i] - \text{'0'}) \times (\text{num2}[j] - \text{'0'})
   $$
   *(Products are summed into decimal power buckets without carrying immediately).*
2. **Carry Normalization Phase:**
   Iterate backwards from the least significant index $k = M + N - 1$ down to $1$:
   $$
   \text{carry} = \lfloor \text{res}[k] / 10 \rfloor
   $$
   $$
   \text{res}[k] \leftarrow \text{res}[k] \pmod{10}
   $$
   $$
   \text{res}[k - 1] \leftarrow \text{res}[k - 1] + \text{carry}
   $$
3. **Format & Strip Zeroes:**
   Convert $\text{res}$ to a string, skipping leading zeroes. If the result is entirely zeroes, return $\text{"0"}$.

> **Invariant.** After normalizing carry up to index $k$, every position from $k$ to $M + N - 1$ contains a single valid decimal digit in $[0, 9]$, and the numerical value of the array remains invariant.

---

## 3. Step-by-Step Worked Execution

We multiply $\text{num1} = \text{"123"}$ and $\text{num2} = \text{"456"}$ using array $\text{res}$ of length 6:

### Phase 1: Bucket Accumulation

The target slot of every one of the $M \times N = 9$ digit products can be read off directly, because
the slot index depends only on $i + j + 1$. Pairs sharing the same anti-diagonal $i + j$ therefore
share a bucket, which is exactly what makes the accumulation a convolution.

| $\text{num1}[i] \to$ | $j = 0$: $4$ (weight $10^{2}$) | $j = 1$: $5$ (weight $10^{1}$) | $j = 2$: $6$ (weight $10^{0}$) |
|:---|:---:|:---:|:---:|
| $i = 0$: $1$ (weight $10^{2}$) | $1 \times 4 = 4$ into slot $1$ | $1 \times 5 = 5$ into slot $2$ | $1 \times 6 = 6$ into slot $3$ |
| $i = 1$: $2$ (weight $10^{1}$) | $2 \times 4 = 8$ into slot $2$ | $2 \times 5 = 10$ into slot $3$ | $2 \times 6 = 12$ into slot $4$ |
| $i = 2$: $3$ (weight $10^{0}$) | $3 \times 4 = 12$ into slot $3$ | $3 \times 5 = 15$ into slot $4$ | $3 \times 6 = 18$ into slot $5$ |

Reading the table by anti-diagonal reproduces the bucket sums: slot $1$ collects $4$; slot $2$ collects
$5 + 8 = 13$; slot $3$ collects $6 + 10 + 12 = 28$; slot $4$ collects $12 + 15 = 27$; and slot $5$
collects $18$. Slot $0$ receives no product at all, which is why it is reserved for a final carry and
why the buffer must be $M + N$ long rather than $M + N - 1$.

- **Position 5 ($i + j + 1 = 5 \implies i = 2, j = 2$):**
  - $\text{num1}[2] \times \text{num2}[2] = 3 \times 6 = 18$.
  - $\text{res}[5] = 18$.
- **Position 4 ($i + j + 1 = 4$):**
  - $i = 2, j = 1: 3 \times 5 = 15$
  - $i = 1, j = 2: 2 \times 6 = 12$
  - $\text{res}[4] = 15 + 12 = 27$.
- **Position 3 ($i + j + 1 = 3$):**
  - $i = 2, j = 0: 3 \times 4 = 12$
  - $i = 1, j = 1: 2 \times 5 = 10$
  - $i = 0, j = 2: 1 \times 6 = 6$
  - $\text{res}[3] = 12 + 10 + 6 = 28$.
- **Position 2 ($i + j + 1 = 2$):**
  - $i = 1, j = 0: 2 \times 4 = 8$
  - $i = 0, j = 1: 1 \times 5 = 5$
  - $\text{res}[2] = 8 + 5 = 13$.
- **Position 1 ($i + j + 1 = 1$):**
  - $i = 0, j = 0: 1 \times 4 = 4$.
  - $\text{res}[1] = 4$.
- **Position 0:**
  - $\text{res}[0] = 0$.

Raw unnormalized array: $\text{res} = [0, 4, 13, 28, 27, 18]$.

---

### Phase 2: Right-to-Left Carry Propagation

- **Index 5 (Value 18):**
  - Digit: $18 \pmod{10} = 8$.
  - Carry: $\lfloor 18 / 10 \rfloor = 1$.
  - Update: $\text{res}[5] = 8$, $\text{res}[4] \leftarrow 27 + 1 = 28$.
- **Index 4 (Value 28):**
  - Digit: $28 \pmod{10} = 8$.
  - Carry: $\lfloor 28 / 10 \rfloor = 2$.
  - Update: $\text{res}[4] = 8$, $\text{res}[3] \leftarrow 28 + 2 = 30$.
- **Index 3 (Value 30):**
  - Digit: $30 \pmod{10} = 0$.
  - Carry: $\lfloor 30 / 10 \rfloor = 3$.
  - Update: $\text{res}[3] = 0$, $\text{res}[2] \leftarrow 13 + 3 = 16$.
- **Index 2 (Value 16):**
  - Digit: $16 \pmod{10} = 6$.
  - Carry: $\lfloor 16 / 10 \rfloor = 1$.
  - Update: $\text{res}[2] = 6$, $\text{res}[1] \leftarrow 4 + 1 = 5$.
- **Index 1 (Value 5):**
  - Digit: $5 \pmod{10} = 5$.
  - Carry: $0$.
  - Update: $\text{res}[1] = 5$, $\text{res}[0] \leftarrow 0 + 0 = 0$.

Normalized array: $[0, 5, 6, 0, 8, 8]$.

---

### Phase 3: Format Output
- Skip leading zero at index 0.
- Remaining digits: $[5, 6, 0, 8, 8]$.
- Emitted string: $\text{"56088"}$.

---

## 4. Complete Execution Trace

| Array Slot $k$ | Positional Weight | Contributing Digit Products $(i, j)$ | Raw Sum in Bucket | Incoming Carry | Resulting Digit ($k \pmod{10}$) | Outgoing Carry to $k-1$ |
|:---:|:---:|:---|:---:|:---:|:---:|:---:|
| 5 | $10^0$ | $3 \times 6 = 18$ | 18 | 0 | **8** | 1 |
| 4 | $10^1$ | $(3 \times 5) + (2 \times 6) = 27$ | 27 | 1 | **8** | 2 |
| 3 | $10^2$ | $(3 \times 4) + (2 \times 5) + (1 \times 6) = 28$ | 28 | 2 | **0** | 3 |
| 2 | $10^3$ | $(2 \times 4) + (1 \times 5) = 13$ | 13 | 3 | **6** | 1 |
| 1 | $10^4$ | $1 \times 4 = 4$ | 4 | 1 | **5** | 0 |
| 0 | $10^5$ | Leading overflow slot | 0 | 0 | **0** (Dropped) | 0 |

---

## 5. Algorithmic Correctness

**Soundness.** Multiplication of two polynomials $A(x) = \sum a_i x^i$ and $B(x) = \sum b_j x^j$ at base $x = 10$ evaluates the product as the discrete convolution of their coefficients. Accumulating digit products into index $i + j + 1$ followed by carry propagation exactly reproduces multi-precision positional decimal arithmetic.

**Completeness.** Every pair of digits $(a, b)$ is multiplied and accumulated into its mathematically corresponding power-of-ten slot. Carry propagation moves strictly right to left, terminating at the most significant digit without dropping any value.

---

## 6. Traps This Instance Exposes

- **Multiplying by Zero:** If either input is $\text{"0"}$ (e.g. $\text{"0"} \times \text{"456"}$), all array buckets remain $0$. Failing to handle the all-zero case would emit an empty string `""` instead of $\text{"0"}$.
- **Leading Zeros in Buffer:** A product of length $M + N$ may have $M + N - 1$ digits (e.g. $10 \times 10 = 100$, occupying 3 digits in a 4-slot array). Stripping leading zeros before joining prevents outputs like $\text{"056088"}$.
- **Index Arithmetic Confusion:** Placing products directly at $i + j$ without allocating $M + N$ slots causes index out-of-bounds or misaligned place values. Slot $i + j + 1$ correctly reserves slot 0 for the final carry.

### Boundary instances and what each one measures

The buffer length below is $M + N$, and the raw bucket column is the largest unnormalized value any single slot ever holds — the quantity the carry pass must reduce to a digit.

| $\text{num1}$ | $\text{num2}$ | $M + N$ | Largest raw bucket | Slots that carry | Product digits | Result | Why it is handled |
|:---|:---|:---:|:---:|:---:|:---:|:---|:---|
| `"2"` | `"3"` | $2$ | $6$ | $0$ | $1$ | `"6"` | A single product already below $10$ needs no carry; slot $0$ stays zero and is stripped |
| `"1002"` | `"304"` | $7$ | $8$ | $0$ | $6$ | `"304608"` | Interior zero digits still contribute $0$ into their slots, so place value is preserved without any special handling |
| `"123"` | `"456"` | $6$ | $28$ | $4$ | $5$ | `"56088"` | Four slots exceed $9$; the buffer still fits because slot $0$ is only needed for a leading carry that never arrives |
| `"999"` | `"999"` | $6$ | $243$ | $5$ | $6$ | `"998001"` | The heaviest accumulation in a three-digit case: a single bucket reaches $243$, and the carry ripples through every remaining slot |
| `"123456789"` | `"98765"` | $14$ | $255$ | $13$ | $14$ | `"12193209765585"` | Unequal lengths do not change the mapping; the product occupies all $M + N$ slots, so no leading zero is stripped |
| `"0"` | `"999"` | $4$ | $0$ | $0$ | $1$ | `"0"` | Every bucket stays $0$, so reading the buffer literally would emit `"000"`; the all-zero case must collapse to a single `"0"` |
| `"999"` | `"0"` | $4$ | $0$ | $0$ | $1$ | `"0"` | The mirror of the previous row, confirming that the zero rule cannot depend on operand order |
| $200$ nines | $200$ nines | $400$ | $16200$ | $399$ | $400$ | $199$ nines, then $8$, then $199$ zeros, then $1$ | The maximum legal case: one bucket reaches $16200$, and the carry chain runs through almost the whole buffer |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M \cdot N)$, where $M = |\text{num1}|$ and $N = |\text{num2}|$. The nested loops perform $M \times N$ digit multiplications. The carry propagation pass takes $O(M + N)$ time.
- **Auxiliary Space Complexity:** $O(M + N)$ to store the intermediate integer array of length $M + N$.
