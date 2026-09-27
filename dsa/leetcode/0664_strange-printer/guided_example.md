# Guided Example: Strange Printer

We trace the step-by-step interval dynamic programming formulation ($f[i][j]$ for substring $s[i \dots j]$), monochrome overwriting mechanics (layering color sweeps), endpoint matching absorption ($s[i] == s[j] \implies f[i][j] = f[i][j-1]$), interval split point minimization ($f[i][k] + f[k+1][j]$), and global minimal printing turn derivation on representative string targets:

- **Input:** $s = \text{"aba"}$
- **Required output:** `2`
  - Printer capabilities & constraints:
    - In each printing turn, the machine can print any contiguous sequence of identical characters (e.g. `"aaaa"`).
    - Later turns overwrite earlier turns across overlapping character segments.
    - Objective: Print the exact string $s$ in the **minimum total turns**.
- **Interval Dynamic Programming & Overwriting Invariant:**
  - **The Overwrite Advantage:**
    - To print `"aba"`, a naive approach might print `'a'` (turn 1), `'b'` (turn 2), and `'a'` (turn 3) $\implies 3$ turns.
    - However, because the machine can overwrite existing characters:
      - Turn 1: Print `"aaa"` across the entire span $0 \dots 2$.
      - Turn 2: Print `'b'` at index $1$.
      - Result: `"aba"` in only **2 turns**!
  - **The Matching Endpoints Invariant ($s[i] == s[j]$):**
    - Whenever the first character equals the last character of a substring ($s[i] == s[j]$):
      - We can imagine the turn that printed character $s[i]$ was simply extended all the way across to index $j$ at zero extra cost.
      - Any intermediate characters differing from $s[i]$ were subsequently stamped on top.
      - Therefore:
        $$
        f[i][j] = f[i][j - 1]
        $$
  - **General Interval Bipartition ($s[i] \ne s[j]$):**
    - When endpoints differ, we test all possible internal split points $k \in [i, \; j - 1]$:
      $$
      f[i][j] = \min_{i \le k < j} \left( f[i][k] + f[k + 1][j] \right)
      $$
- **Step-by-Step Worked Execution Trace on $s = \text{"aba"}$ ($n = 3$):**
  - Indices: $0 = \text{'a'}, \; 1 = \text{'b'}, \; 2 = \text{'a'}$.
  - Initialize $3 \times 3$ table $f$:
  - **Intervals of Length 1 ($j - i = 0$):**
    - Any single character requires exactly 1 turn:
      $$
      f[0][0] = 1 \quad (\text{"a"})
      $$
      $$
      f[1][1] = 1 \quad (\text{"b"})
      $$
      $$
      f[2][2] = 1 \quad (\text{"a"})
      $$
  - **Intervals of Length 2 ($j - i = 1$):**
    - **Substring $s[0 \dots 1] = \text{"ab"}$:**
      - Endpoints differ: $s[0] = \text{'a'} \ne s[1] = \text{'b'}$.
      - Split at $k = 0$:
        $$
        f[0][0] + f[1][1] = 1 + 1 = \mathbf{2}
        $$
      - $f[0][1] = \mathbf{2}$.
    - **Substring $s[1 \dots 2] = \text{"ba"}$:**
      - Endpoints differ: $s[1] = \text{'b'} \ne s[2] = \text{'a'}$.
      - Split at $k = 1$:
        $$
        f[1][1] + f[2][2] = 1 + 1 = \mathbf{2}
        $$
      - $f[1][2] = \mathbf{2}$.
  - **Interval of Length 3 ($j - i = 2$, Full String $s[0 \dots 2] = \text{"aba"}$):**
    - Check endpoints:
      $$
      s[0] = \text{'a'}, \quad s[2] = \text{'a'} \implies s[0] == s[2] \quad \mathbf{(Matching\ Endpoints!)}
      $$
    - Apply endpoint absorption:
      - The stroke covering index $0$ with `'a'` can simultaneously cover index $2$ with `'a'`.
      - Index $1$ (`'b'`) will be stamped over it later.
      - Therefore:
        $$
        f[0][2] = f[0][2 - 1] = f[0][1] = \mathbf{2}
        $$
    - Verify with split-point minimization:
      - Option $k = 0$ ($s[0 \dots 0] + s[1 \dots 2]$): $f[0][0] + f[1][2] = 1 + 2 = 3$.
      - Option $k = 1$ ($s[0 \dots 1] + s[2 \dots 2]$): $f[0][1] + f[2][2] = 2 + 1 = 3$.
      - Minimum between absorption (2) and splits (3):
        $$
        f[0][2] = \mathbf{2}
        $$
  - **Step 4: Emit Final Output:**
    $$
    ans = f[0][2] = \mathbf{2}
    $$
- **Two Uniform Blocks ($s = \text{"aaabbb"}$):**
  - Block `"aaa"` takes 1 turn.
  - Block `"bbb"` takes 1 turn.
  - Total: $1 + 1 = \mathbf{2}$.
- **Consecutive Identical Characters:**
  - Repeated identical adjacent characters never increase turn count (e.g. `"a"` and `"aa"` both take 1 turn).

This instance demonstrates interval dynamic programming with non-local layer overwriting, mathematically proves why terminal equality allows contiguous background base-coating without additional operations, and derives $O(N^3)$ runtime and $O(N^2)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a string $s$:
The strange printer prints same-character sweeps and can overwrite previous turns.
Find the **minimum turns** to produce $s$.

```text
Target: "aba"

Strategy:
  Turn 1: Print "aaa"  (covers indices 0 to 2 with 'a')
  Turn 2: Print "b"    (overwrites index 1 with 'b')

Result: "aba" in 2 turns!
```

### The Invariant of Endpoint Absorption
- If $s[i] == s[j]$, printing $s[i]$ can span all the way to $j$ without consuming extra turns.
- Thus, whenever $s[i] == s[j]$:
  $$
  f[i][j] = f[i][j - 1]
  $$

---

## 2. Conceptual Foundation & Invariants

### 1. The Recurrence Relation:
For interval $[i, j]$:
$$
f[i][i] = 1
$$
If $s[i] == s[j]$:
$$
f[i][j] = f[i][j - 1]
$$
Else:
$$
f[i][j] = \min_{i \le k < j} \left( f[i][k] + f[k + 1][j] \right)
$$

### 2. Execution Order:
Iterate $i$ backwards from $n - 1$ down to 0, and $j$ from $i + 1$ to $n - 1$ (expanding interval length).

> **Monochrome Painting Dominance Invariant.** In any optimal paint sequence for substring $s[i \dots j]$ with $s[i] == s[j]$, the earliest operation covering either endpoint can be extended to an all-$s[i]$ base layer across the entire interval without increasing total turn count.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"aba"}$:

---

### Step 1: Base Table
- $f[0][0] = 1, f[1][1] = 1, f[2][2] = 1$.

---

### Step 2: Length 2
- $s[0 \dots 1] = \text{"ab"} \implies f[0][1] = 2$.
- $s[1 \dots 2] = \text{"ba"} \implies f[1][2] = 2$.

---

### Step 3: Length 3 ($s[0 \dots 2] = \text{"aba"}$)
- $s[0] == s[2] == \text{'a'}$.
- $f[0][2] = f[0][1] = \mathbf{2}$.

---

### Step 4: Final Output
$$
\mathbf{2}
$$

---

## 4. Complete Execution Trace

| Substring $s[i \dots j]$ | Left Endpoint $s[i]$ | Right Endpoint $s[j]$ | Endpoints Match? | Transition Applied | Computed $f[i][j]$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `"a"` ($i=0$) | `'a'` | `'a'` | Yes (Base) | Base case | $1$ |
| `"b"` ($i=1$) | `'b'` | `'b'` | Yes (Base) | Base case | $1$ |
| `"a"` ($i=2$) | `'a'` | `'a'` | Yes (Base) | Base case | $1$ |
| `"ab"` ($0 \dots 1$) | `'a'` | `'b'` | No | $f[0][0] + f[1][1] = 1 + 1$ | $2$ |
| `"ba"` ($1 \dots 2$) | `'b'` | `'a'` | No | $f[1][1] + f[2][2] = 1 + 1$ | $2$ |
| **`"aba"` ($0 \dots 2$)** | **`'a'`** | **`'a'`** | **Yes** | **$f[0][1] = 2$** | **`2`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Character ($N = 1$):** 1 turn.
- **All Same Characters ($s = \text{"aaaa"}$):** 1 turn.
- **All Distinct Characters ($s = \text{"abcdef"}$):** $N$ turns.
- **Palindromic String ($s = \text{"abacaba"}$):** Nested endpoint matches collapse turn counts efficiently.

---

## 6. Traps & Common Anti-Patterns

- **Greedy Printing Without Overwriting:** Greedily counting distinct blocks misses the opportunity to lay a base coat across matching distant endpoints.
- **Wrong Loop Ordering:** Evaluating longer intervals before their sub-intervals are computed leads to uninitialized table lookups.
- **Omitting Split Minimization When Characters Match:** While $f[i][j - 1]$ is optimal for matching endpoints, in some variations testing $f[i][k] + f[k+1][j]$ ensures consistency across all sub-splits.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Three nested loops: $i$ ($N$ values), $j$ ($N$ values), and split point $k$ ($N$ values).
  - Number of operations: $\approx \frac{N^3}{6}$.
  - For $N = 100$, executes $\approx 1.6 \times 10^5$ operations, completing in $< 10$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N^2)$ space for the dynamic programming table $f$.