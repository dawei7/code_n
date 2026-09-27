# Guided Example: Longest Palindromic Substring

We trace the step-by-step dynamic programming evaluation on a representative string instance:

- **Input:** $s = \text{"babad"}$
- **Required output:** $\text{"bab"}$ (or $\text{"aba"}$)

This instance is selected because it demonstrates both essential dynamic programming behaviors: decomposing an outer interval into an inner subproblem, and rejecting candidates where outer characters match but inner substrings fail or vice versa.

---

## 1. Instance & Teaching Goal

Given a string $s$, we seek the longest contiguous substring that reads identically forward and backward. 

For $s = \text{"babad"}$, the indices are:

| Index | 0 | 1 | 2 | 3 | 4 |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Character | `b` | `a` | `b` | `a` | `d` |

A naive approach checks all $O(N^2)$ candidate substrings, verifying each in $O(N)$ time for an overall $O(N^3)$ complexity. The optimal dynamic programming method reuses truth values of smaller inner substrings, verifying each interval in $O(1)$ time and reducing the overall complexity to $O(N^2)$.

---

## 2. Conceptual Foundation & Invariants

Let $f[i][j]$ denote whether the substring $s[i \dots j]$ (from index $i$ to $j$ inclusive) is a palindrome.

A substring $s[i \dots j]$ is palindromic if and only if:
1. The boundary characters match: $s[i] = s[j]$; and
2. The remaining interior $s[i+1 \dots j-1]$ is also palindromic (or has length $\le 1$).

This gives the recurrence relation:

$$
f[i][j] = (s[i] = s[j]) \land \big(j - i < 2 \lor f[i+1][j-1]\big)
$$

### Base Cases
- **Length 1:** Every single character $s[i \dots i]$ is vacuously a palindrome: $f[i][i] = \text{True}$.
- **Length 2:** Two adjacent characters $s[i \dots i+1]$ form a palindrome if and only if $s[i] = s[i+1]$.
- **Empty interior:** When $j - i < 2$, there is no inner substring to check.

> **Invariant.** Before evaluating any interval of length $L = j - i + 1$, all sub-intervals of length strictly less than $L$ have been computed and stored in $f$.

---

## 3. Step-by-Step Worked Execution

We systematically evaluate candidate substrings ordered by increasing length $L = 1, 2, 3, 4, 5$.

### Length $L = 1$ (Single Characters)
Every single character is inherently a palindrome:
- $s[0 \dots 0] = \text{"b"} \implies f[0][0] = \text{True}$
- $s[1 \dots 1] = \text{"a"} \implies f[1][1] = \text{True}$
- $s[2 \dots 2] = \text{"b"} \implies f[2][2] = \text{True}$
- $s[3 \dots 3] = \text{"a"} \implies f[3][3] = \text{True}$
- $s[4 \dots 4] = \text{"d"} \implies f[4][4] = \text{True}$

Current best palindrome: $\text{"b"}$ (length 1).

---

### Length $L = 2$ (Adjacent Pairs)
For length 2, $j = i + 1$. We only need to check if $s[i] = s[j]$:
- $s[0 \dots 1] = \text{"ba"}$: $s[0] = \text{'b'} \ne s[1] = \text{'a'} \implies f[0][1] = \text{False}$
- $s[1 \dots 2] = \text{"ab"}$: $s[1] = \text{'a'} \ne s[2] = \text{'b'} \implies f[1][2] = \text{False}$
- $s[2 \dots 3] = \text{"ba"}$: $s[2] = \text{'b'} \ne s[3] = \text{'a'} \implies f[2][3] = \text{False}$
- $s[3 \dots 4] = \text{"ad"}$: $s[3] = \text{'a'} \ne s[4] = \text{'d'} \implies f[3][4] = \text{False}$

No length 2 palindromes exist in this instance. Current best remains $\text{"b"}$ (length 1).

---

### Length $L = 3$ (Three-Character Windows)
For length 3, $j = i + 2$. We check $s[i] = s[j]$ and consult the inner single character $f[i+1][j-1]$:
- $s[0 \dots 2] = \text{"bab"}$:
  - Outer check: $s[0] = \text{'b'}$ and $s[2] = \text{'b'}$ (match).
  - Inner check: $f[1][1] = \text{True}$ (center $\text{"a"}$).
  - Result: $f[0][2] = \text{True}$.
  - Update best: $\text{"bab"}$ (length 3).
- $s[1 \dots 3] = \text{"aba"}$:
  - Outer check: $s[1] = \text{'a'}$ and $s[3] = \text{'a'}$ (match).
  - Inner check: $f[2][2] = \text{True}$ (center $\text{"b"}$).
  - Result: $f[1][3] = \text{True}$.
  - Both $\text{"bab"}$ and $\text{"aba"}$ have maximal length 3.
- $s[2 \dots 4] = \text{"bad"}$:
  - Outer check: $s[2] = \text{'b'} \ne s[4] = \text{'d'}$ (mismatch).
  - Result: $f[2][4] = \text{False}$.

---

### Length $L = 4$ (Four-Character Windows)
For length 4, $j = i + 3$:
- $s[0 \dots 3] = \text{"baba"}$: $s[0] = \text{'b'} \ne s[3] = \text{'a'} \implies f[0][3] = \text{False}$.
- $s[1 \dots 4] = \text{"abad"}$: $s[1] = \text{'a'} \ne s[4] = \text{'d'} \implies f[1][4] = \text{False}$.

---

### Length $L = 5$ (Full String)
For the full string $s[0 \dots 4] = \text{"babad"}$:
- Outer check: $s[0] = \text{'b'} \ne s[4] = \text{'d'} \implies f[0][4] = \text{False}$.

The search terminates having evaluated all valid substrings.

---

## 4. Complete Execution Trace

### Step-by-Step Substring Evaluation

| Window Length $L$ | Substring $s[i \dots j]$ | Outer Match ($s[i] = s[j]$) | Interior State $f[i+1][j-1]$ | Is Palindrome $f[i][j]$ | Longest Found |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | $s[0 \dots 0] = \text{"b"}$ | Identical (Base Case) | - | **True** | $\text{"b"}$ ($L=1$) |
| 1 | $s[1 \dots 1] = \text{"a"}$ | Identical (Base Case) | - | **True** | $\text{"b"}$ ($L=1$) |
| 1 | $s[2 \dots 2] = \text{"b"}$ | Identical (Base Case) | - | **True** | $\text{"b"}$ ($L=1$) |
| 1 | $s[3 \dots 3] = \text{"a"}$ | Identical (Base Case) | - | **True** | $\text{"b"}$ ($L=1$) |
| 1 | $s[4 \dots 4] = \text{"d"}$ | Identical (Base Case) | - | **True** | $\text{"b"}$ ($L=1$) |
| 2 | $s[0 \dots 1] = \text{"ba"}$ | $\text{'b'} \ne \text{'a'}$ | - | **False** | $\text{"b"}$ ($L=1$) |
| 2 | $s[1 \dots 2] = \text{"ab"}$ | $\text{'a'} \ne \text{'b'}$ | - | **False** | $\text{"b"}$ ($L=1$) |
| 2 | $s[2 \dots 3] = \text{"ba"}$ | $\text{'b'} \ne \text{'a'}$ | - | **False** | $\text{"b"}$ ($L=1$) |
| 2 | $s[3 \dots 4] = \text{"ad"}$ | $\text{'a'} \ne \text{'d'}$ | - | **False** | $\text{"b"}$ ($L=1$) |
| 3 | $s[0 \dots 2] = \text{"bab"}$ | $\text{'b'} = \text{'b'}$ | $f[1][1] = \text{True}$ | **True** | $\text{"bab"}$ ($L=3$) |
| 3 | $s[1 \dots 3] = \text{"aba"}$ | $\text{'a'} = \text{'a'}$ | $f[2][2] = \text{True}$ | **True** | $\text{"bab"}$ ($L=3$) |
| 3 | $s[2 \dots 4] = \text{"bad"}$ | $\text{'b'} \ne \text{'d'}$ | - | **False** | $\text{"bab"}$ ($L=3$) |
| 4 | $s[0 \dots 3] = \text{"baba"}$ | $\text{'b'} \ne \text{'a'}$ | - | **False** | $\text{"bab"}$ ($L=3$) |
| 4 | $s[1 \dots 4] = \text{"abad"}$ | $\text{'a'} \ne \text{'d'}$ | - | **False** | $\text{"bab"}$ ($L=3$) |
| 5 | $s[0 \dots 4] = \text{"babad"}$ | $\text{'b'} \ne \text{'d'}$ | - | **False** | $\text{"bab"}$ ($L=3$) |

### Final 2D Dynamic Programming Table

The resulting truth table $f[i][j]$ for all $0 \le i \le j < 5$:

| $i \backslash j$ | 0 (`b`) | 1 (`a`) | 2 (`b`) | 3 (`a`) | 4 (`d`) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **0 (`b`)** | **True** | False | **True** | False | False |
| **1 (`a`)** | - | **True** | False | **True** | False |
| **2 (`b`)** | - | - | **True** | False | False |
| **3 (`a`)** | - | - | - | **True** | False |
| **4 (`d`)** | - | - | - | - | **True** |

---

## 5. Algorithmic Correctness

**Soundness.** A substring $s[i \dots j]$ is declared a palindrome if and only if its boundary characters match ($s[i] = s[j]$) and its strictly smaller interior is already verified as palindromic ($f[i+1][j-1] = \text{True}$). Since base cases of length $1$ and length $2$ are exact, induction guarantees that no non-palindromic substring can be marked $\text{True}$.

**Completeness.** Every contiguous substring corresponds to a unique pair of indices $(i, j)$ with $0 \le i \le j < N$. By iterating through all lengths $L$ from $1$ to $N$, the algorithm evaluates all $\frac{N(N+1)}{2}$ substrings without omission. Thus, the global maximum length palindrome is guaranteed to be identified.

---

## 6. Traps This Instance Exposes

- **Inner Palindrome Dependency:** Outer character agreement alone is insufficient. For instance, in $s[0 \dots 3] = \text{"baba"}$, testing only matching characters at alternating positions would fail; checking strict boundary equality and recursive interior truth is essential.
- **Order of Subproblem Resolution:** Computing $f[i][j]$ requires that $f[i+1][j-1]$ already be populated. Iterating by window length $L$ guarantees that shorter subproblems are always finalized before longer ones.
- **Multiple Optimal Answers:** Both $\text{"bab"}$ and $\text{"aba"}$ are valid length-3 palindromes. Problem contracts permitting any valid maximal palindrome accept either choice.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^2)$. There are $\frac{N(N+1)}{2}$ substring pairs $(i, j)$. For each pair, checking boundary characters and querying the memoized interior takes $O(1)$ operations. Thus, the total time is $O(N^2)$, where $N = |s|$.
- **Auxiliary Space Complexity:** $O(N^2)$. An $N \times N$ boolean table stores the truth values for all subproblems. (Expanding around centers can reduce auxiliary space to $O(1)$ while retaining $O(N^2)$ time).
