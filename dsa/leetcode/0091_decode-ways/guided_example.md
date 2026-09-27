# Guided Example: Decode Ways

We trace the step-by-step 1D dynamic programming prefix decoding recurrence on representative valid and trapped string instances:

- **Valid Multi-Path Instance:** $s = \text{"226"} \implies 3$ (`"BZ"`, `"VF"`, `"BBF"`)
- **Valid Embedded Zero:** $s = \text{"10"} \implies 1$ (`"J"`)
- **Invalid Leading Zero Trap:** $s = \text{"06"} \implies 0$
- **Invalid Trapped Zero:** $s = \text{"30"} \implies 0$

This instance demonstrates decomposing choices into 1-digit ($1 \dots 9$) and 2-digit ($10 \dots 26$) decodings, handling zero digit constraints, state compression to two scalar variables, and early pruning upon encountering unmatchable zeroes.

---

## 1. Instance & Teaching Goal

A message containing letters from A-Z is encoded using the mapping:
- `'A'` $\to \text{"1"}$
- `'B'` $\to \text{"2"}$
- $\dots$
- `'Z'` $\to \text{"26"}$

Given a string $s = \text{"226"}$, return the number of ways to decode it.

For $s = \text{"226"}$, there are 3 distinct valid groupings:
1. $(2, 2, 6) \implies \text{"BBF"}$
2. $(22, 6) \implies \text{"VF"}$
3. $(2, 26) \implies \text{"BZ"}$

Notice that the digit `'0'` cannot map to any letter by itself; it can only appear as the second digit of `"10"` (`'J'`) or `"20"` (`'T'`).
A naive recursion branches into two choices at each index, causing exponential $O(2^N)$ time.
Dynamic programming computes the number of decodings for prefix lengths $0 \dots N$ in a single $O(N)$ pass with $O(1)$ space.

---

## 2. Conceptual Foundation & Invariants

### 1D Prefix Recurrence
Let $DP[i]$ be the number of valid decodings for prefix $s[0 \dots i-1]$ (of length $i$).

1. **Base Cases:**
   - Empty prefix: $DP[0] = 1$.
   - If the first character is `'0'` ($s[0] == \text{'0'}$): return $0$ immediately (leading zero is invalid).
2. **Transitions for $i \in [1, N]$:**
   Initialize $DP[i] = 0$.
   - **Single-Digit Decode ($s[i-1]$):**
     If $s[i-1] \ne \text{'0'}$:
     $$
     DP[i] \leftarrow DP[i] + DP[i-1]
     $$
     *(Digits $1 \dots 9$ map to `'A'` $\dots$ `'I'`)*.
   - **Two-Digit Decode ($s[i-2 \dots i-1]$):**
     If $i \ge 2$ and $10 \le \text{int}(s[i-2 \dots i-1]) \le 26$:
     $$
     DP[i] \leftarrow DP[i] + DP[i-2]
     $$
     *(Pairs $10 \dots 26$ map to `'J'` $\dots$ `'Z'`)*.

### Space Optimization
Since $DP[i]$ depends only on $DP[i-1]$ and $DP[i-2]$, the computation can be performed with two scalar variables (`prev1`, `prev2`) in $O(1)$ auxiliary space.

> **Invariant.** Entry $DP[i]$ contains the exact number of legal character partitions of the prefix string $s[0 \dots i-1]$.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"226"}$ ($N = 3$):

### Base Initialization
- $DP[0] = 1$ (Empty string base).

---

### Step 1: Prefix Length $i = 1$ (Char $s[0] = \text{'2'}$)
- **1-Digit:** $s[0] = \text{'2'} \ne \text{'0'}$.
  - Valid! Can decode `'2'` as `'B'`.
  - Contribution: $DP[1] += DP[0] \implies DP[1] = 1$.
- **2-Digit:** Not applicable ($i < 2$).
- State: $DP[1] = 1$. Decodings: `{"B"}`.

---

### Step 2: Prefix Length $i = 2$ (Chars $s[0 \dots 1] = \text{"22"}$)
- **1-Digit:** $s[1] = \text{'2'} \ne \text{'0'}$.
  - Valid! Can append `'2'` (`'B'`) to all previous decodings.
  - Contribution: $DP[2] += DP[1] = 1$.
- **2-Digit:** Substring $s[0 \dots 1] = \text{"22"}$.
  - Value is $22$. Since $10 \le 22 \le 26$, this is valid (`'V'`).
  - Contribution: $DP[2] += DP[0] = 1$.
- State: $DP[2] = 1 + 1 = 2$. Decodings: `{"BB", "V"}`.

---

### Step 3: Prefix Length $i = 3$ (Chars $s[0 \dots 2] = \text{"226"}$)
- **1-Digit:** $s[2] = \text{'6'} \ne \text{'0'}$.
  - Valid! Can append `'6'` (`'F'`) to all decodings of length 2.
  - Contribution: $DP[3] += DP[2] = 2$.
- **2-Digit:** Substring $s[1 \dots 2] = \text{"26"}$.
  - Value is $26$. Since $10 \le 26 \le 26$, this is valid (`'Z'`).
  - Contribution: $DP[3] += DP[1] = 1$.
- State: $DP[3] = 2 + 1 = \mathbf{3}$. Decodings: `{"BBF", "VF", "BZ"}`.

Termination. Final answer is $DP[3] = 3$.

---

## 4. Complete Execution Trace

### DP State Progression for $s = \text{"226"}$

| Prefix Length $i$ | Suffix Inspected | 1-Digit Valid? ($s[i-1] \ne \text{'0'}$) | 2-Digit Valid? ($10 \le \text{pair} \le 26$) | Sum Formula ($DP[i-1] + DP[i-2]$) | Computed $DP[i]$ | Decoded Candidates |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | $\emptyset$ | - | - | Base condition | 1 | `""` |
| 1 | `'2'` | Yes (`'2'`) | N/A ($i < 2$) | $1$ | 1 | `"B"` |
| 2 | `'2'` (`"22"`) | Yes (`'2'`) | Yes (`"22"`) | $1 + 1$ | 2 | `"BB"`, `"V"` |
| 3 | `'6'` (`"26"`) | Yes (`'6'`) | Yes (`"26"`) | $2 + 1$ | **3** | **`"BBF"`, `"VF"`, `"BZ"`** |

### Zero Handling Comparison

| String Instance | 1-Digit Step | 2-Digit Step | Outcome $DP$ | Explanation |
|:---:|:---:|:---:|:---:|:---|
| `"06"` | $s[0] == \text{'0'}$ (Invalid) | - | **0** | Leading zero is not a valid encoding |
| `"10"` | $s[1] == \text{'0'}$ (0) | $10 \in [10, 26]$ ($+1$) | **1** | Only valid as two-digit `"10"` (`'J'`) |
| `"30"` | $s[1] == \text{'0'}$ (0) | $30 > 26$ (0) | **0** | `'0'` cannot stand alone; `"30"` exceeds alphabet |

---

## 5. Algorithmic Correctness

**Soundness.** Every valid decoding of prefix $s[0 \dots i-1]$ must either end in a 1-digit code (valid if $s[i-1] \in [1, 9]$) or a 2-digit code (valid if $s[i-2 \dots i-1] \in [10, 26]$). Because these two cases end in distinct token lengths (1 vs 2), their decoding sets are disjoint. By the sum rule of combinatorics, $DP[i] = DP[i-1] + DP[i-2]$.

**Completeness.** Computing values monotonically from $i = 1$ to $N$ guarantees that all valid decodings are counted. If an impassable zero (like `"30"`) occurs, $DP[i] = 0 + 0 = 0$, propagating $0$ to all subsequent states.

---

## 6. Traps This Instance Exposes

- **Leading Zeroes (`"0"`, `"06"`):** Strings beginning with `'0'` have zero valid interpretations. A check `if not s or s[0] == '0': return 0` handles this immediately.
- **Embedded Zero Pairs (`"10"`, `"20"`):** When $s[i-1] == \text{'0'}$, the single-digit branch contributes $0$. It can only receive decodings from the 2-digit branch if $s[i-2] \in \{\text{'1'}, \text{'2'}\}$.
- **Illegal Zero Pairs (`"30"`, `"00"`):** Neither single-digit nor two-digit branches are valid, setting $DP[i] = 0$.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N = |s|$. The loop executes $N$ times, each iteration performing $O(1)$ arithmetic and string slice comparisons.
- **Auxiliary Space Complexity:** $O(1)$. Memory is compressed to two scalar integer variables.