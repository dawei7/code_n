# Guided Example: Reverse Integer

We trace the step-by-step mathematical digit reversal and 32-bit overflow boundary checks on a representative signed instance:

- **Input:** $x = -123$
- **Required output:** $-321$

This instance demonstrates signed decimal digit extraction, truncation toward zero, arithmetic digit accumulation, and overflow prevention within the signed 32-bit integer range $[-2^{31}, 2^{31} - 1] = [-2147483648, 2147483647]$.

---

## 1. Instance & Teaching Goal

Given a 32-bit signed integer $x$, we must reverse its decimal digits. If the reversed value exceeds the 32-bit signed bounds $[-2^{31}, 2^{31} - 1]$, the algorithm must detect this condition and return $0$.

For $x = -123$:
- The negative sign is preserved.
- The digits $\{1, 2, 3\}$ from right to left become $\{3, 2, 1\}$.
- The resulting integer is $-321$.

A naive approach converts the integer to an intermediate string representation. However, in low-level and interview environments, standard 32-bit integers must be processed numerically without allocating extra string buffers, while guarding against intermediate overflow at every step.

---

## 2. Conceptual Foundation & Invariants

### Mathematical Digit Extraction
At each step, we extract the least significant decimal digit $y$ from $x$ using truncation toward zero:
$$
y = \text{sgn}(x) \cdot (|x| \pmod{10})
$$
The remaining integer is updated by discarding the least significant digit:
$$
x_{\text{next}} = \text{trunc}(x / 10)
$$
The reversed accumulator $\text{ans}$ is updated by shifting left one decimal position and adding $y$:
$$
\text{ans}_{\text{next}} = \text{ans} \cdot 10 + y
$$

### 32-Bit Overflow Prevention
Before executing the multiplication $\text{ans} \cdot 10$, we must verify that $\text{ans}_{\text{next}}$ will not exceed the 32-bit signed limits:
- $\text{INT\_MAX} = 2^{31} - 1 = 2147483647$
- $\text{INT\_MIN} = -2^{31} = -2147483648$

The lookahead boundary conditions are:
1. **Positive Overflow:**
   $$
   \text{ans} > \left\lfloor \frac{2147483647}{10} \right\rfloor = 214748364 \quad \lor \quad (\text{ans} = 214748364 \land y > 7)
   $$
2. **Negative Overflow:**
   $$
   \text{ans} < \left\lceil \frac{-2147483648}{10} \right\rceil = -214748364 \quad \lor \quad (\text{ans} = -214748364 \land y < -8)
   $$

If either condition is triggered, continuing would overflow 32-bit representation, so the algorithm immediately halts and returns $0$.

> **Invariant.** At iteration $k$, the accumulator $\text{ans}$ represents exactly the first $k$ extracted digits of $x$ reversed with the correct sign, and $\text{ans} \in [-2^{31}, 2^{31}-1]$.

---

## 3. Step-by-Step Worked Execution

We trace $x = -123$ with initial accumulator $\text{ans} = 0$:

### Iteration 1: Extract Units Digit
- **Current state:** $x = -123$, $\text{ans} = 0$.
- **Digit extraction:**
  $$
  y = - (123 \pmod{10}) = -3
  $$
- **Remaining $x$:**
  $$
  x = \text{trunc}(-123 / 10) = -12
  $$
- **Overflow check:** $\text{ans} = 0$, which is well within $[-214748364, 214748364]$. Safe.
- **Update accumulator:**
  $$
  \text{ans} = 0 \cdot 10 + (-3) = -3
  $$

---

### Iteration 2: Extract Tens Digit
- **Current state:** $x = -12$, $\text{ans} = -3$.
- **Digit extraction:**
  $$
  y = - (12 \pmod{10}) = -2
  $$
- **Remaining $x$:**
  $$
  x = \text{trunc}(-12 / 10) = -1
  $$
- **Overflow check:** $\text{ans} = -3$, well within bounds. Safe.
- **Update accumulator:**
  $$
  \text{ans} = -3 \cdot 10 + (-2) = -30 - 2 = -32
  $$

---

### Iteration 3: Extract Hundreds Digit
- **Current state:** $x = -1$, $\text{ans} = -32$.
- **Digit extraction:**
  $$
  y = - (1 \pmod{10}) = -1
  $$
- **Remaining $x$:**
  $$
  x = \text{trunc}(-1 / 10) = 0
  $$
- **Overflow check:** $\text{ans} = -32$, well within bounds. Safe.
- **Update accumulator:**
  $$
  \text{ans} = -32 \cdot 10 + (-1) = -320 - 1 = -321
  $$

### Termination
- $x = 0$. The loop terminates.
- Final returned value: $-321$.

---

## 4. Complete Execution Trace

### Step-by-Step Numeric State Table

| Iteration | Remaining $x$ Before | Extracted Digit $y$ | Overflow Check Status | Update Formula | Remaining $x$ After | New Accumulator $\text{ans}$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 (Init) | -123 | - | Initialized | - | -123 | 0 |
| 1 | -123 | $-3$ | Safe ($0 \in [-2.14 \cdot 10^8, 2.14 \cdot 10^8]$) | $0 \cdot 10 + (-3)$ | -12 | -3 |
| 2 | -12 | $-2$ | Safe ($-3 \in [-2.14 \cdot 10^8, 2.14 \cdot 10^8]$) | $-3 \cdot 10 + (-2)$ | -1 | -32 |
| 3 | -1 | $-1$ | Safe ($-32 \in [-2.14 \cdot 10^8, 2.14 \cdot 10^8]$) | $-32 \cdot 10 + (-1)$ | 0 | **-321** |

### Overflow Contrast Example: $x = 1534236469$

To demonstrate how the lookahead guard prevents overflow, consider $x = 1534236469$:

| Step | State Before | Next Digit $y$ | Accumulator $\text{ans}$ | Threshold Test | Outcome |
|:---:|:---:|:---:|:---:|:---:|:---|
| Steps 1–9 | Digits processed: $9, 6, 4, 6, 3, 2, 4, 3, 5$ | - | $964632435$ | - | Normal progress |
| Step 10 | Final digit $y = 1$ | 1 | $964632435$ | $\text{ans} = 964632435 > 214748364$ | **Overflow detected**; abort and return **0** |

---

## 5. Algorithmic Correctness

**Soundness.** Digits are extracted from lowest to highest decimal power and inserted into the accumulator with increasing decimal weight. By mathematical induction, reversing the sequence of base-10 digits reconstructs the mirrored decimal integer. The strict lookahead check guarantees that no operation will evaluate to a value outside $[-2^{31}, 2^{31}-1]$.

**Completeness.** Dividing $x$ by 10 truncates exactly one decimal digit per step. Because $|x|$ decreases strictly monotonically, $x$ must reach $0$ in at most $\lfloor \log_{10} |x| \rfloor + 1$ iterations. Every decimal digit is accounted for.

---

## 6. Traps This Instance Exposes

- **Truncation vs Euclidean Floor Division:** In Python, standard `//` floors toward $-\infty$ (e.g. $-123 // 10 = -13$) and `%` returns a positive remainder ($-123 \% 10 = 7$). When implementing numerical reversal, one must either use absolute values with a preserved sign or explicitly adjust negative remainders ($y = y - 10$ if $y > 0$).
- **Asymmetric 32-Bit Range:** $|-2^{31}| = 2147483648$, which exceeds the maximum positive signed integer $2^{31}-1 = 2147483647$. Performing operations on absolute values must handle this asymmetry without attempting to represent $+2147483648$.
- **Trailing Zeroes:** An input such as $120$ should produce $21$, not $021$. Numerical accumulation naturally eliminates leading zeroes because $0 \cdot 10 + 2 = 2$.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log_{10} |x|)$. A 32-bit signed integer has at most 10 decimal digits. The algorithm executes at most 10 iterations of constant-time arithmetic operations, making the runtime $O(1)$ in practice.
- **Auxiliary Space Complexity:** $O(1)$. All operations are performed using a constant number of scalar integer variables without allocating strings or heap memory.
