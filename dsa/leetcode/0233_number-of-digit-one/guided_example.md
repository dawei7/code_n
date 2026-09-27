# Guided Example: Number of Digit One

We trace the step-by-step place-value decomposition, quotient-remainder cycle counting, and partial-prefix boundary clamping on representative positive integers:

- **Input:** $n = 13$
- **Required output:** $6$ (Numbers $\le 13$ containing digit 1: $1, 10, 11, 12, 13$; total count of '1's is $1 + 1 + 2 + 1 + 1 = 6$)
- **Zero Input Boundary:** $n = 0 \implies 0$
- **Power of Ten Instance:** $n = 20 \implies 12$ (Units contribute 2, tens contribute 10; $2 + 10 = 12$)
- **Large Composite Instance:** $n = 100 \implies 21$ (Units: 10, Tens: 10, Hundreds: 1; $10 + 10 + 1 = 21$)

This instance demonstrates mathematical positional combinatorics (place-value digit induction), explains why counting occurrences column-by-column ($m = 1, 10, 100, \dots$) eliminates exhaustive $O(N)$ string formatting, and derives the closed-form boundary formula in $O(\log_{10} n)$ time with $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given a positive integer $n = 13$, count the total number of times the digit `'1'` appears across all integers from $1$ to $13$:
```text
 1 -> "1"      (1 one)
 2 -> "2"
 ...
 9 -> "9"
10 -> "10"     (1 one)
11 -> "11"     (2 ones)
12 -> "12"     (1 one)
13 -> "13"     (1 one)
Total = 1 + 1 + 2 + 1 + 1 = 6
```

A brute-force loop checks every number from $1$ to $n$ and converts to string, taking $O(n \log_{10} n)$ time. For $n = 10^9$, that would take over $10^{10}$ operations and time out.
Instead of counting by number, we count **by positional column** (units, tens, hundreds, ...):
- How many times does digit `1` appear in the **units** place?
- How many times does digit `1` appear in the **tens** place?
- How many times does digit `1` appear in the **hundreds** place?
Summing the contributions of all columns yields the exact total in at most $10$ steps ($O(\log_{10} n)$ time).

---

## 2. Conceptual Foundation & Invariants

### Place-Value Column Decomposition
Let $m$ be the current place value ($m = 1, 10, 100, 1000, \dots$).
At each place value $m$, partition $n$ into three components:
1. **Higher Digits:**
   $$
   a = n // (m \cdot 10)
   $$
2. **Current Digit:**
   $$
   b = (n // m) \% 10
   $$
3. **Lower Digits:**
   $$
   c = n \% m
   $$

### Contribution Formula for Column $m$:
Every full cycle of $10 \cdot m$ numbers contains exactly $m$ occurrences of digit `1` at place value $m$.
The higher digits $a$ represent $a$ complete cycles, contributing:
$$
\text{Full Cycle Ones} = a \cdot m
$$
The remaining partial cycle depends on the current digit $b$:
- **Case 1 ($b == 0$):**
  The current column has not yet reached digit `1` in the final partial block.
  $$
  \text{Partial Contribution} = 0
  $$
- **Case 2 ($b == 1$):**
  The current column is partially through its run of `1`s, starting from $10\dots0$ up to $1c$.
  $$
  \text{Partial Contribution} = c + 1
  $$
- **Case 3 ($b > 1$):**
  The current column has completely finished its run of `1`s (all $m$ occurrences from $10\dots0$ through $19\dots9$ have occurred).
  $$
  \text{Partial Contribution} = m
  $$

Total contribution at place value $m$:
$$
\text{count}(m) = a \cdot m + \begin{cases}
0, & b = 0 \\
c + 1, & b = 1 \\
m, & b > 1
\end{cases}
$$

> **Invariant.** For each place value $m$, $\text{count}(m)$ is strictly equal to the number of integers $x \in [1, n]$ whose $m$-position digit is equal to `1`.

---

## 3. Step-by-Step Worked Execution

We trace the column evaluations for $n = 13$:

### Iteration 1: Units Place ($m = 1$)
- Higher digits: $a = 13 // (1 \cdot 10) = 1$.
- Current digit: $b = (13 // 1) \% 10 = 3$.
- Lower digits: $c = 13 \% 1 = 0$.
- Evaluate contribution:
  - Higher cycles: $a \cdot m = 1 \cdot 1 = 1$.
  - Since $b = 3 > 1$, Case 3 triggers: partial contribution is $m = 1$.
  $$
  \text{count}(1) = a \cdot m + m = 1 + 1 = \mathbf{2}
  $$
  *(Verification: Units digit is 1 at integers $1$ and $11 \implies 2$ times)*.

---

### Iteration 2: Tens Place ($m = 10$)
- Higher digits: $a = 13 // (10 \cdot 10) = 0$.
- Current digit: $b = (13 // 10) \% 10 = 1$.
- Lower digits: $c = 13 \% 10 = 3$.
- Evaluate contribution:
  - Higher cycles: $a \cdot m = 0 \cdot 10 = 0$.
  - Since $b = 1 == 1$, Case 2 triggers: partial contribution is $c + 1 = 3 + 1 = 4$.
  $$
  \text{count}(10) = a \cdot m + (c + 1) = 0 + 4 = \mathbf{4}
  $$
  *(Verification: Tens digit is 1 at integers $10, 11, 12, 13 \implies 4$ times)*.

---

### Iteration 3: Hundreds Place ($m = 100$)
- Since $m = 100 > n$ ($100 > 13$), the loop terminates.

---

### Step 4: Total Accumulation
$$
\text{Total} = \text{count}(1) + \text{count}(10) = 2 + 4 = \mathbf{6}
$$
The result is $\mathbf{6}$.

---

## 4. Complete Execution Trace

```text
n = 13

m = 1 (Units):
  a = 1, b = 3, c = 0
  b > 1 -> count = 1 * 1 + 1 = 2 (numbers: 1, 11)

m = 10 (Tens):
  a = 0, b = 1, c = 3
  b == 1 -> count = 0 * 10 + (3 + 1) = 4 (numbers: 10, 11, 12, 13)

m = 100 > 13 -> Stop

Total Ones = 2 + 4 = 6
```

| Place Value $m$ | Higher $a$ | Digit $b$ | Lower $c$ | Case Evaluated | Full Cycle $(a \cdot m)$ | Partial Cycle | Column Total | Running Total |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **$1$ (Units)** | 1 | 3 | 0 | $b > 1$ | $1 \cdot 1 = 1$ | $1$ | $2$ | **2** |
| **$10$ (Tens)** | 0 | 1 | 3 | $b == 1$ | $0 \cdot 10 = 0$ | $3 + 1 = 4$ | $4$ | **6** |
| **$100$** | - | - | - | $m > n$ | - | - | - | **6 (Final Answer)** |

### 4.1 Reconciling Column Totals Against Explicit Enumerations

The formula produces two numbers and the answer is their sum. Nothing in the
derivation spells out *which* numbers each column counted, so the table below
reconstructs the enumeration that each column total represents and checks it
against the column value.

| Place value $m$ | Digit $b$ of $n$ | Case applied | Formula value | Numbers in $[1, n]$ with a `1` at this place value | How many | Agree? |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|
| $1$ (units) | 3 | $b > 1$ | $a \cdot m + m = 1 + 1 = 2$ | 1, 11 | 2 | Yes |
| $10$ (tens) | 1 | $b == 1$ | $a \cdot m + (c + 1) = 0 + 4 = 4$ | 10, 11, 12, 13 | 4 | Yes |
| $100$ | beyond $n$ | loop terminates | not evaluated | none, since $100 > 13$ | 0 | Yes |

Number 11 appears in two rows, which is the mechanism the whole method depends
on. It is counted once as a units `1` and once as a tens `1`, and the sum over
columns is therefore the total number of `1` characters rather than the number of
integers containing at least one `1`. Any approach that counts integers instead
of characters would report 5 for this input.

### 4.2 Positional Reconciliation for the Larger Trials

The authored trials push the same accounting further, and each one stresses a
different part of the three-way case split.

| Trial input | Place value $m$ | Digit $b$ | Case applied | Numbers contributing at this place value | Column count | Running total |
|:---|:---:|:---:|:---:|:---|:---:|:---:|
| $n = 20$ | $1$ | 0 | $b == 0$ | 1, 11 | 2 | 2 |
| $n = 20$ | $10$ | 2 | $b > 1$ | 10 through 19 | 10 | 12 |
| $n = 99$ | $1$ | 9 | $b > 1$ | 1, 11, 21, 31, 41, 51, 61, 71, 81, 91 | 10 | 10 |
| $n = 99$ | $10$ | 9 | $b > 1$ | 10 through 19 | 10 | 20 |
| $n = 101$ | $1$ | 1 | $b == 1$ | 1, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101 | 11 | 11 |
| $n = 101$ | $10$ | 0 | $b == 0$ | 10 through 19 | 10 | 21 |
| $n = 101$ | $100$ | 1 | $b == 1$ | 100, 101 | 2 | 23 |

The first two rows expose the most counterintuitive case in the whole formula.
For $n = 20$ the final incomplete block of ten is 20 through 29, and the only two
numbers of that block that are present are 20 and 21 — too few to reach the 21
that would carry a units `1`. The two occurrences the formula reports are
therefore the leftovers of the completed cycle 0 through 19, namely 1 and 11,
which is why the $b == 0$ branch still yields a non-zero column total rather than
nothing at all. The $n = 99$ pair are both complete cycles, so each column
contributes exactly its full $m$. The $n = 101$ rows show the opposite extreme: a
tens column whose digit is 0 contributes 10 through its completed cycle while the
hundreds column contributes the partial run $c + 1 = 2$.

---

## 5. Algorithmic Correctness

**Soundness.** Every integer's base-10 representation has a unique digit at position $m$. Counting the occurrences of `1` in position $m$ independently across all integers and summing across all valid positions $m \le n$ partitions the count of all `'1'` characters without duplication or omission.

**Completeness.** Since $m$ scales by $10$ until $m > n$, all digit positions present in $n$ are evaluated. Because $a, b, c$ form the standard division identity $n = a \cdot 10m + b \cdot m + c$, the full and partial cycle counts account for every integer from $1$ to $n$.

---

## 6. Traps This Instance Exposes

- **Double-Counting Multi-One Numbers:** Number $11$ contains two `'1'`s. The column-based method counts the units `'1'` in iteration $m = 1$, and counts the tens `'1'` in iteration $m = 10$. Both are counted naturally with zero special-case logic.
- **Off-by-One on Partial Block ($c + 1$):** When $b == 1$, the partial block runs from $10\dots0$ to $1c$. Because $0$ is included in the suffix range $[0, c]$, there are $c + 1$ numbers, not $c$.
- **Integer Overflow on $m \cdot 10$:** In 32-bit typed languages like C++, if $n \approx 10^9$, multiplying $m = 10^9$ by $10$ overflows a 32-bit signed integer. Using a 64-bit integer (`long long`) or writing `n // m // 10` prevents overflow.

### 6.1 Boundary Probes for the Three Cases

The three branches of the contribution formula are best separated by working at a
single place value and moving only the digit that governs the partial cycle. All
probes below use $m = 10$, so the components are the hundreds digit $a$, the tens
digit $b$, and the units suffix $c = n \% 10$.

| Probe input $n$ | $a$ | $b$ | $c$ | Branch taken | Full cycles $a \cdot m$ | Partial contribution | Column total for $m = 10$ | Numbers the column counts |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 105 | 1 | 0 | 5 | $b == 0$ | $1 \cdot 10 = 10$ | 0 | 10 | 10 through 19 only; the tens digit of 105 is 0, so nothing partial exists |
| 113 | 1 | 1 | 3 | $b == 1$ | $1 \cdot 10 = 10$ | $c + 1 = 4$ | 14 | 10 through 19 and 110 through 113 |
| 123 | 1 | 2 | 3 | $b > 1$ | $1 \cdot 10 = 10$ | $m = 10$ | 20 | 10 through 19 and 110 through 119 |
| 13 | 0 | 1 | 3 | $b == 1$ | $0 \cdot 10 = 0$ | $c + 1 = 4$ | 4 | 10 through 13; there is no completed cycle to contribute |

Reading the rows downward shows the entire case split: at $b = 0$ the partial term
vanishes while the completed cycles remain, at $b = 1$ the partial term grows with
the suffix, and at $b > 1$ the partial term saturates at $m$ because every suffix
from 0 through 9 has already carried a `1` in that position. Row 4 is the input
actually traced in Section 3, and it is the one case where $a = 0$: the full-cycle
term contributes nothing at all, so the answer rests entirely on the partial run.

The $c + 1$ term also deserves a boundary check of its own. At $n = 119$ the suffix
is $c = 9$, so the partial block covers 110 through 119, which is ten numbers, and
$c + 1 = 10$ rather than 9. Writing the term as $c$ instead would understate every
column whose current digit is exactly 1.

### 6.2 Alternatives Compared on This Instance

| Approach | How the count is obtained | Time | Auxiliary space | Tradeoff or failure mode |
|:---|:---|:---:|:---:|:---|
| Column-by-column cycle counting (traced above) | Evaluate a closed form once per place value | $O(\log_{10} n)$ | $O(1)$ | Chosen. At most ten iterations for the problem's range, and every case is arithmetic |
| Enumerate every integer and count characters | Convert each value to a decimal string and scan it | $O(n \log_{10} n)$ | $O(\log_{10} n)$ per conversion | Correct but hopeless at the upper limit, where $n$ can approach $2 \times 10^9$ |
| Digit DP with memoization on position, count, and tightness | Enumerate digit choices and memoize the remaining suffix states | $O(\log_{10} n)$ states, with a bounded branching factor | $O(\log_{10} n)$ memo entries | Also linear in the digit count and easier to generalize to other digit-counting constraints, yet it carries more state than a closed form needs |
| Arithmetic progression on complete blocks only | Count only the fully completed cycles and ignore the partial block | $O(\log_{10} n)$ | $O(1)$ | Understates the answer by the partial contribution; for $n = 13$ it reports 1 instead of 6 |
| Counting integers that contain at least one `1` | Deduplicate each integer before adding it | $O(\log_{10} n)$ per value | $O(1)$ | Wrong by construction: 11 contributes two characters but one integer, which is exactly the distinction Section 4.1 makes |

The first and third rows are both logarithmic, and the difference between them is
one of form rather than of asymptotic class. The last two rows are the errors the
instance is chosen to expose: dropping the partial block loses most of the
answer, and counting integers rather than digit characters loses exactly the
multiplicity that number 11 supplies.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log_{10} n)$. In each step, $m$ is multiplied by $10$. For $n \le 2 \times 10^9$, the loop executes at most $\approx 10$ times. Each iteration takes $O(1)$ arithmetic operations. Total runtime is practically instantaneous ($< 10$ CPU cycles).
- **Auxiliary Space Complexity:** $O(1)$ constant auxiliary memory.
