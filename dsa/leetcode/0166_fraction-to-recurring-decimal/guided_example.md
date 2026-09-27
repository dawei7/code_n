# Guided Example: Fraction to Recurring Decimal

We trace the step-by-step simulated long division, remainder cycle detection via hash map, and parenthesis enclosing on representative rational fraction instances:

- **Input:** $\text{numerator} = 4, \quad \text{denominator} = 333$
- **Required output:** `"0.(012)"` (Fractional part $012$ recurs indefinitely)
- **Terminating Decimal Instance:** $\text{numerator} = 1, \quad \text{denominator} = 2 \implies \text{"0.5"}$
- **Whole Integer Instance:** $\text{numerator} = 2, \quad \text{denominator} = 1 \implies \text{"2"}$
- **Negative Fraction Instance:** $\text{numerator} = -50, \quad \text{denominator} = 8 \implies \text{"-6.25"}$

This instance demonstrates separating integer parts from fractional decimal digits, simulating positional long division with remainder tracking, identifying repeating repeating cycles via pigeonhole remainder recurrence, and formatting recurring decimals in $O(D)$ time.

---

## 1. Instance & Teaching Goal

Given two integers representing a fraction:
$$
\frac{\text{numerator}}{\text{denominator}} = \frac{4}{333}
$$
Convert the rational number into its exact decimal string representation. If the fractional part repeats, enclose the repeating sequence in parentheses:
$$
\frac{4}{333} = 0.012012012\dots \implies \mathbf{\text{"0.(012)"}}
$$

Directly using floating-point types (`float(4) / 333`) introduces IEEE-754 precision loss and cannot detect cycle lengths or boundary repetitions.
In grade-school long division:
- At each decimal place, the remainder $R$ is multiplied by 10, producing quotient digit $\lfloor (R \times 10) / D \rfloor$ and new remainder $(R \times 10) \pmod D$.
- Because $D$ is finite, the non-zero remainder must be an integer in $[1, D - 1]$.
- By the **Pigeonhole Principle**, after at most $D$ divisions, a previously observed remainder **must repeat**!
Recording each remainder's first appearance index in a hash map allows exact, $O(1)$ cycle identification and parenthesis placement.

---

## 2. Conceptual Foundation & Invariants

### Long Division State Machine Protocol
Let $N = |\text{numerator}|$ and $D = |\text{denominator}|$.

#### 1. Zero and Sign Pre-processing:
- If $\text{numerator} == 0$, return `"0"`.
- Determine sign:
  $$
  \text{sign} = \text{"-"} \quad \text{if } (\text{numerator} < 0) \oplus (\text{denominator} < 0) \quad \text{else } \text{""}
  $$

#### 2. Integer Part Extraction:
$$
Q = \lfloor N / D \rfloor, \quad R = N \pmod D
$$
Initialize string tokens: `ans = [sign, str(Q)]`.
If $R == 0$: return `"".join(ans)` (Whole number, no decimal point needed).

#### 3. Fractional Long Division:
Append `"."` to `ans`.
Maintain `seen = {}` mapping remainder $R \to$ index in `ans` where its quotient digit will be placed.

While $R \ne 0$:
- **Cycle Check:**
  If $R \in \text{seen}$:
  - The cycle starts at index $\text{seen}[R]$.
  - Insert `"("` at index $\text{seen}[R]$.
  - Append `")"` at the end of `ans`.
  - Break out of loop.
- **Record Position:**
  $$
  \text{seen}[R] = |\text{ans}|
  $$
- **Compute Next Decimal Digit:**
  $$
  R \leftarrow R \times 10
  $$
  $$
  \text{digit} = \lfloor R / D \rfloor
  $$
  $$
  R \leftarrow R \pmod D
  $$
  $$
  \text{ans.append}(\text{str}(\text{digit}))
  $$

Return `"".join(ans)`.

> **Invariant.** If remainder $R$ reappears, every subsequent quotient digit and remainder will repeat identically. The slice from $\text{seen}[R]$ to the end constitutes the exact minimal repeating period.

---

## 3. Step-by-Step Worked Execution

We trace $\text{numerator} = 4, \text{denominator} = 333$:
$N = 4, D = 333$. Both positive $\implies \text{sign} = \text{""}$.

### Step 1: Integer Part
- $Q = \lfloor 4 / 333 \rfloor = 0$.
- $R = 4 \pmod{333} = 4$.
- `ans = ["0", "."]`. Initial length $= 2$.

---

### Step 2: Remainder $R = 4$
- Check: $4 \notin \text{seen}$.
- Record: $\text{seen}[4] = |\text{ans}| = 2$.
- Shift remainder: $4 \times 10 = 40$.
- Division:
  - Digit: $\lfloor 40 / 333 \rfloor = \mathbf{0}$.
  - Remainder: $40 \pmod{333} = \mathbf{40}$.
- Append digit: `ans = ["0", ".", "0"]`.

---

### Step 3: Remainder $R = 40$
- Check: $40 \notin \text{seen}$.
- Record: $\text{seen}[40] = |\text{ans}| = 3$.
- Shift remainder: $40 \times 10 = 400$.
- Division:
  - Digit: $\lfloor 400 / 333 \rfloor = \mathbf{1}$.
  - Remainder: $400 \pmod{333} = 400 - 333 = \mathbf{67}$.
- Append digit: `ans = ["0", ".", "0", "1"]`.

---

### Step 4: Remainder $R = 67$
- Check: $67 \notin \text{seen}$.
- Record: $\text{seen}[67] = |\text{ans}| = 4$.
- Shift remainder: $67 \times 10 = 670$.
- Division:
  - Digit: $\lfloor 670 / 333 \rfloor = \mathbf{2}$.
  - Remainder: $670 \pmod{333} = 670 - 666 = \mathbf{4}$.
- Append digit: `ans = ["0", ".", "0", "1", "2"]`.

---

### Step 5: Remainder $R = 4$ (Cycle Detected!)
- Check: $4 \in \text{seen}$!
  $$
  \text{seen}[4] = \mathbf{2}
  $$
- The repeating sequence starts at index $2$ (where the first `'0'` was written).
- Insert `"("` at index 2:
  `ans` $\implies$ `["0", ".", "(", "0", "1", "2"]`.
- Append `")"`:
  `ans` $\implies$ `["0", ".", "(", "0", "1", "2", ")"]`.
- Break loop.

Assemble result: $\mathbf{\text{"0.(012)"}}$.

---

## 4. Complete Execution Trace

```text
Fraction: 4 / 333
Integer part: 0, Remainder: 4. ans = ["0", "."]

Step 1: Remainder = 4.  seen[4] = 2.  40 / 333  = 0 rem 40.  ans = ["0", ".", "0"]
Step 2: Remainder = 40. seen[40] = 3. 400 / 333 = 1 rem 67.  ans = ["0", ".", "0", "1"]
Step 3: Remainder = 67. seen[67] = 4. 670 / 333 = 2 rem 4.   ans = ["0", ".", "0", "1", "2"]
Step 4: Remainder = 4 -> Already seen at index 2!
        Insert '(' at index 2, append ')' at end:
        Result: "0.(012)"
```

| Step | Remainder In $R$ | Recorded Index $\text{seen}[R]$ | Multiplied $R \times 10$ | Quotient Digit | New Remainder | Tokens in `ans` |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| Init | 4 | - | - | - | 4 | `["0", "."]` |
| 1 | 4 | 2 | 40 | 0 | 40 | `["0", ".", "0"]` |
| 2 | 40 | 3 | 400 | 1 | 67 | `["0", ".", "0", "1"]` |
| 3 | 67 | 4 | 670 | 2 | 4 | `["0", ".", "0", "1", "2"]` |
| **4** | **4** | **Found at 2** | - | - | - | **`"0.(012)"` (Enclosed)** |

---

## 5. Algorithmic Correctness

**Soundness.** Long division produces the exact base-10 expansion of $N/D$. At any step, the next digit and new remainder depend solely on the current remainder $R$ and divisor $D$. Therefore, encountering an identical remainder guarantees that the subsequent string of digits will repeat in an identical sequence.

**Completeness.** Since $0 \le R < D$, there are at most $D$ possible remainders. If $R$ never becomes $0$, a remainder must repeat in at most $D$ steps by Dirichlet's Box (Pigeonhole) Principle. The algorithm terminates for all rational fractions.

---

## 6. Traps This Instance Exposes

- **32-Bit Overflow on Integer Negation:** In languages like C++, negating $-2^{31}$ causes integer overflow! Casting to 64-bit integer (`long long`) before taking absolute values prevents overflow crashes.
- **Zero Numerator Sign:** When `numerator = 0` and `denominator = -5`, returning `"-0"` is incorrect. Check `if numerator == 0: return "0"` first.
- **Zero Digits in Quotient:** In $\frac{4}{333}$, $40 < 333$, generating digit $0$. Omitting the zero would yield wrong answer `"0.(12)"` instead of `"0.(012)"`.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(D)$, where $D$ is the denominator. The number of unique remainders cannot exceed $D$. In practice, repeating cycles for 32-bit test inputs are limited to at most $10^4$ characters.
- **Auxiliary Space Complexity:** $O(D)$ auxiliary memory for the remainder hash map and output string tokens.
