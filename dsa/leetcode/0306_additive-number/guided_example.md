# Guided Example: Additive Number

We trace the step-by-step two-element boundary selection, leading zero rejection invariants, deterministic string addition propagation ($c = a + b$), and complete string consumption verification on representative numerical sequences:

- **Input:** $\text{num} = \text{"112358"}$
- **Required output:** `true` (Valid additive sequence $[1, 1, 2, 3, 5, 8]$ where each term after the first two is the exact sum of the previous two)
- **Variable Length Numbers:** $\text{num} = \text{"199100199"} \implies \text{true}$ (Sequence $[1, 99, 100, 199]$ where $1 + 99 = 100$ and $99 + 100 = 199$)
- **Zero Digit Handling:** $\text{num} = \text{"000"} \implies \text{true}$ ($[0, 0, 0]$ is valid; single zero digits are legal)
- **Leading Zero Rejection:** $\text{num} = \text{"1023"} \implies \text{false}$ (Candidate $[1, 02, 3]$ is rejected because multi-digit numbers cannot have leading zeros)
- **Minimum Length Requirement:** Length $< 3 \implies \text{false}$ (At least three numbers are required)

This instance demonstrates deterministic sequence propagation, proves why fixing only the first two numbers ($a$ and $b$) completely eliminates further branching, details strict leading-zero boundary rules, and executes in $O(N^3)$ time and $O(N)$ space without arbitrary-precision overflow hazards.

---

## 1. Instance & Teaching Goal

Given a digit string $\text{num} = \text{"112358"}$ ($N = 6$):
Determine whether it can be partitioned into at least 3 numbers forming an **additive sequence**:
$$
x_{k} = x_{k-1} + x_{k-2} \quad \text{for all } k \ge 2
$$
- No number in the sequence may contain leading zeros (except the single number $0$).

```text
String: "1 1 2 3 5 8"
Candidate partition:
x0 = 1
x1 = 1
x2 = 1 + 1 = 2 -> matches next digit "2"
x3 = 1 + 2 = 3 -> matches next digit "3"
x4 = 2 + 3 = 5 -> matches next digit "5"
x5 = 3 + 5 = 8 -> matches next digit "8"

Entire string consumed -> Output: true
```

### Determinism After Initial Choice
- In general string partitioning, searching all cuts creates an exponential $O(2^N)$ tree.
- In an additive sequence, **choosing the first two numbers ($a$ and $b$) completely fixes all subsequent numbers**:
  The third number must be $a + b$, the fourth must be $b + (a + b)$, and so on.
  Once the first two boundaries $(i, j)$ are chosen, the remainder of the verification is **100% deterministic with zero branching**!

---

## 2. Conceptual Foundation & Invariants

### First Two Term Boundaries $(i, j)$
Let $N = \text{len}(\text{num})$.
We iterate over all possible cut points for the first two numbers:
- First number: $a = \text{int}(\text{num}[0 : i])$ for $1 \le i \le N // 2$.
- Second number: $b = \text{int}(\text{num}[i : j])$ for $i + 1 \le j < N$.

### Leading Zero Constraints:
1. If $i > 1$ and $\text{num}[0] == \text{'0'}$: Invalid first term (e.g. `"05"` is forbidden). Break loop over $i$.
2. If $j - i > 1$ and $\text{num}[i] == \text{'0'}$: Invalid second term. Skip this $j$.

### Deterministic Verification `isValid(a, b, k)`:
Starting from index $k = j$:
While $k < N$:
1. Compute expected sum: $c = a + b$.
2. Convert sum to string: $s = \text{str}(c)$.
3. If the remaining substring does not start with $s$ (`not num.startswith(s, k)`):
   Return `False` (Additive property violated).
4. Advance deterministic pointers:
   $$
   k \leftarrow k + \text{len}(s)
   $$
   $$
   a \leftarrow b, \quad b \leftarrow c
   $$
If the loop reaches $k == N$ (all digits consumed): Return `True`!

> **Invariant.** For any pair $(i, j)$, `isValid(a, b, j)` simulates the unique Fibonacci-like trajectory. If any required sum does not match the string prefix, the branch is discarded immediately without sub-branching.

---

## 3. Step-by-Step Worked Execution

We trace the search on $\text{num} = \text{"112358"}$ ($N = 6$):

---

### Step 1: Evaluate First Candidate $(i = 1, j = 2)$
- Cut 1: $i = 1 \implies \text{num}[0:1] = \text{"1"}$, value $a = 1$.
- Cut 2: $j = 2 \implies \text{num}[1:2] = \text{"1"}$, value $b = 1$.
- Leading zero checks: Both are single digit `'1'` (Valid).
- Remaining string from $k = 2$: $\text{num}[2:] = \text{"2358"}$.

---

### Step 2: Deterministic Extension from $(a=1, b=1, k=2)$

- **Round 1 (Generate 3rd term):**
  - Expected sum: $c = a + b = 1 + 1 = \mathbf{2}$.
  - String representation: $s = \text{"2"}$. Length $= 1$.
  - Does $\text{"2358"}$ start with `"2"`? **Yes!**
  - Advance:
    $$
    k \leftarrow 2 + 1 = 3, \quad a \leftarrow 1, \quad b \leftarrow 2
    $$
  - Remaining string: $\text{num}[3:] = \text{"358"}$.

- **Round 2 (Generate 4th term):**
  - Expected sum: $c = a + b = 1 + 2 = \mathbf{3}$.
  - String representation: $s = \text{"3"}$. Length $= 1$.
  - Does $\text{"358"}$ start with `"3"`? **Yes!**
  - Advance:
    $$
    k \leftarrow 3 + 1 = 4, \quad a \leftarrow 2, \quad b \leftarrow 3
    $$
  - Remaining string: $\text{num}[4:] = \text{"58"}$.

- **Round 3 (Generate 5th term):**
  - Expected sum: $c = a + b = 2 + 3 = \mathbf{5}$.
  - String representation: $s = \text{"5"}$. Length $= 1$.
  - Does $\text{"58"}$ start with `"5"`? **Yes!**
  - Advance:
    $$
    k \leftarrow 4 + 1 = 5, \quad a \leftarrow 3, \quad b \leftarrow 5
    $$
  - Remaining string: $\text{num}[5:] = \text{"8"}$.

- **Round 4 (Generate 6th term):**
  - Expected sum: $c = a + b = 3 + 5 = \mathbf{8}$.
  - String representation: $s = \text{"8"}$. Length $= 1$.
  - Does $\text{"8"}$ start with `"8"`? **Yes!**
  - Advance:
    $$
    k \leftarrow 5 + 1 = 6, \quad a \leftarrow 5, \quad b \leftarrow 8
    $$
  - Remaining string: Empty ($k == N == 6$).

---

### Step 3: Success Base Case Reached
$k == 6$ equals total string length $N = 6$.
Every digit in $\text{num}$ was consumed by exact mathematical additions.
Return **`true`**.

---

## 4. Complete Execution Trace

```text
num = "112358"

Try i = 1, j = 2: a = 1, b = 1, k = 2
  Round 1: 1 + 1 = 2 -> num[2:] starts with "2" -> k = 3, (a, b) = (1, 2)
  Round 2: 1 + 2 = 3 -> num[3:] starts with "3" -> k = 4, (a, b) = (2, 3)
  Round 3: 2 + 3 = 5 -> num[4:] starts with "5" -> k = 5, (a, b) = (3, 5)
  Round 4: 3 + 5 = 8 -> num[5:] starts with "8" -> k = 6, (a, b) = (5, 8)
  k == 6 == len(num) -> Entire string consumed!

Result: true
```

| Verification Step | Current $a$ | Current $b$ | Required Sum $c = a + b$ | Suffix Inspected | Suffix Starts With $c$? | Updated Index $k$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 1 | 1 | 2 | `"2358"` | **Yes** | $k = 3$ |
| 2 | 1 | 2 | 3 | `"358"` | **Yes** | $k = 4$ |
| 3 | 2 | 3 | 5 | `"58"` | **Yes** | $k = 5$ |
| 4 | 3 | 5 | 8 | `"8"` | **Yes** | $k = 6$ |
| **End** | 5 | 8 | - | `""` | **Complete Match** | **`true`** |

---

### Contrast: Failure Trace on `num = "1023"`
- Try $i = 1, j = 2$: $a = 1, b = 0$. Sum $c = 1$. Suffix `"23"` does not start with `"1"` $\implies$ Fails.
- Try $i = 1, j = 3$: $a = 1, b = \text{"02"}$. Mismatch: `"02"` has a leading zero! $\implies$ Disallowed.
- Try $i = 2, j = 3$: $a = \text{"10"}, b = 2$. Sum $c = 12$. Suffix `"3"` does not start with `"12"` $\implies$ Fails.
- All candidate pairs fail $\implies$ Returns `false`.

---

## 5. Algorithmic Correctness

**Soundness.** A string is declared additive only when an exact partition of at least 3 numbers is verified, where each number after the second is the exact numerical sum of its predecessors and no number contains illegal leading zeros. Every condition of the problem specification is strictly met.

**Completeness.** Any valid additive sequence must begin with some first number $\text{num}[0:i]$ and second number $\text{num}[i:j]$. The nested loops exhaustively enumerate all possible boundary splits $(i, j)$ with $i \le N/2$. Because subsequent terms are uniquely determined by addition, if any valid additive sequence exists, its initial pair $(i, j)$ will be tested and successfully verified.

---

## 6. Traps This Instance Exposes

- **Leading Zero Invalidation:** Strings like `"02"` or `"03"` cannot be treated as valid numbers in the sequence. Only single-digit `'0'` is permitted. Failing to prune leading zeros allows false positives like `"1023"` ($1, 02, 3$).
- **Stopping at 3 Numbers:** A sequence must consume the **entire** string. If $a + b$ matches a prefix of the remaining text but leftover characters remain that do not continue the sequence, the candidate is invalid.
- **Integer Overflow in Other Languages:** In languages like Java or C++, adding two 18-digit numbers can overflow standard 64-bit signed integers. Using string-based addition (or Python's arbitrary-precision integers) prevents arithmetic overflow.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^3)$, where $N = \text{len}(\text{num})$.
  - Choosing cut point $i$: $O(N)$ possibilities ($i \le N/2$).
  - Choosing cut point $j$: $O(N)$ possibilities.
  - Verifying the remaining string: advances by at least 1 digit per step, taking $O(N)$ total string slicing and addition operations.
  - Total time: $O(N) \times O(N) \times O(N) = O(N^3)$. With $N \le 35$, $N^3 \approx 42,875$ operations, running in under 2 milliseconds.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary memory for string slices and numerical conversion buffers.
