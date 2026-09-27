# Guided Example: Regular Expression Matching

We trace the step-by-step execution of 2D dynamic programming grid matching with kleene-star pairs on a representative pattern instance:

- **Input:** $s = \text{"aab"}$, $p = \text{"c*a*b"}$
- **Required output:** $\text{True}$

This instance demonstrates coupling the kleene star `'*'` to its preceding token, matching zero occurrences via two-step pattern lookback ($DP[i][j-2]$), matching one or more occurrences via string reduction ($DP[i-1][j]$), and handling single-character wildcards (`'.'`).

---

## 1. Instance & Teaching Goal

Given an input string $s = \text{"aab"}$ of length $M = 3$ and a pattern $p = \text{"c*a*b"}$ of length $N = 5$:
- `'.'` matches any single character.
- `'*'` matches **zero or more of the preceding element**.

Matching breakdown:
- `"c*"` matches zero occurrences of `'c'`, consuming zero characters of $s$.
- `"a*"` matches two occurrences of `'a'`, consuming $\text{"aa"}$.
- `"b"` matches `'b'`, consuming $\text{"b"}$.
- The entire string is matched, returning $\text{True}$.

A naive recursive search without memoization branches on every `'*'`, causing exponential $O(2^{M+N})$ time. The optimal 2D dynamic programming approach constructs an $(M+1) \times (N+1)$ table $DP$, solving the matching decision in $O(M \cdot N)$ time.

---

## 2. Conceptual Foundation & Invariants

### 2D DP State Formulation
Let $DP[i][j]$ be a boolean indicating whether prefix $s[0 \dots i-1]$ matches pattern prefix $p[0 \dots j-1]$.

### Base Case Boundary Conditions
1. **Empty String & Empty Pattern:**
   $$
   DP[0][0] = \text{True}
   $$
2. **Non-Empty String & Empty Pattern ($i > 0$):**
   $$
   DP[i][0] = \text{False}
   $$
3. **Empty String & Pattern with Stars ($i = 0, j \ge 2$):**
   If $p[j-1] == \text{'*'},$ the star can eliminate the preceding character $p[j-2]$ by matching zero copies:
   $$
   DP[0][j] = DP[0][j-2]
   $$

### State Transitions ($i \ge 1, j \ge 1$)
1. **Normal Character or Dot ($p[j-1] \ne \text{'*'}'$):**
   If $p[j-1] == s[i-1]$ or $p[j-1] == \text{'.'}'$:
   $$
   DP[i][j] = DP[i-1][j-1]
   $$
2. **Kleene Star (`'*'`):**
   The star modifies token $p[j-2]$. It offers two choices:
   - **Zero Occurrences:** Discard the token pair $p[j-2 \dots j-1]$:
     $$
     \text{zero\_copies} = DP[i][j-2]
     $$
   - **One or More Occurrences:** If $s[i-1]$ matches $p[j-2]$ (either $s[i-1] == p[j-2]$ or $p[j-2] == \text{'.'}\,$), consume one character of $s$ while keeping the pattern active:
     $$
     \text{multiple\_copies} = DP[i-1][j]
     $$
   Combining both branches:
   $$
   DP[i][j] = DP[i][j-2] \lor \Big( (s[i-1] == p[j-2] \lor p[j-2] == \text{'.'}\,) \land DP[i-1][j] \Big)
   $$

> **Invariant.** Cell $DP[i][j] == \text{True}$ if and only if pattern prefix $p[0 \dots j-1]$ can generate string prefix $s[0 \dots i-1]$.

---

## 3. Step-by-Step Worked Execution

We construct the table for $s = \text{"aab"}$ ($M = 3$) and $p = \text{"c*a*b"}$ ($N = 5$):

### Step 0: Row 0 ($s = \text{""}$, Empty String)
- $DP[0][0] = \text{True}$.
- $j = 1$ ($p[0] = \text{'c'}$): $DP[0][1] = \text{False}$.
- $j = 2$ ($p[1] = \text{'*'}$): Lookback 2 steps $\implies DP[0][0] = \text{True}$ (`"c*"` can match empty).
- $j = 3$ ($p[2] = \text{'a'}$): $DP[0][3] = \text{False}$.
- $j = 4$ ($p[3] = \text{'*'}$): Lookback 2 steps $\implies DP[0][2] = \text{True}$ (`"a*"` can match empty).
- $j = 5$ ($p[4] = \text{'b'}$): $DP[0][5] = \text{False}$.

Row 0: `[T, F, T, F, T, F]`.

---

### Step 1: Row 1 ($s[0] = \text{'a'}$)
- $j = 1$ (`c`): Mismatch `'a' \ne 'c' \implies \text{False}$.
- $j = 2$ (`*` after `c`): Zero copies $\implies DP[1][0] = \text{False}$. Mismatch with `'c'` $\implies \text{False}$.
- $j = 3$ (`a`): Match! $s[0] == \text{'a'} \implies$ take diagonal $DP[0][2] = \text{True}$.
- $j = 4$ (`*` after `a`):
  - Zero copies: $DP[1][2] = \text{False}$.
  - One+ copies: $s[0] == \text{'a'}$ and $DP[0][4] = \text{True} \implies \text{True}$!
  - Result: $DP[1][4] = \text{True}$.
- $j = 5$ (`b`): Mismatch `'a' \ne 'b' \implies \text{False}$.

Row 1: `[F, F, F, T, T, F]`.

---

### Step 2: Row 2 ($s[1] = \text{'a'}$)
- $j \in [1, 3]$: All $\text{False}$.
- $j = 4$ (`*` after `a`):
  - Zero copies: $DP[2][2] = \text{False}$.
  - One+ copies: $s[1] == \text{'a'}$ and $DP[1][4] = \text{True} \implies \text{True}$!
  - Result: $DP[2][4] = \text{True}$ (second `'a'` absorbed by `"a*"`).
- $j = 5$ (`b`): Mismatch $\implies \text{False}$.

Row 2: `[F, F, F, F, T, F]`.

---

### Step 3: Row 3 ($s[2] = \text{'b'}$)
- $j \in [1, 4]$: All $\text{False}$ (neither `'c*'` nor `'a*'` can match `'b'`, and zero copies from $DP[3][2]$ is False).
- $j = 5$ ($p[4] = \text{'b'}$):
  - Exact match: $s[2] == \text{'b'}$.
  - Take diagonal: $DP[2][4] = \text{True}$!
  - Result: $DP[3][5] = \text{True}$.

Terminal entry $DP[3][5] = \text{True}$.

---

## 4. Complete Execution Trace

### 2D DP State Matrix ($4 \times 6$)

| String $\downarrow$ / Pattern $\to$ | $\epsilon$ (Col 0) | `c` (Col 1) | `*` (Col 2) | `a` (Col 3) | `*` (Col 4) | `b` (Col 5) |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| $\epsilon$ (Row 0) | **T** | F | **T** | F | **T** | F |
| `a` (Row 1) | F | F | F | **T** | **T** | F |
| `aa` (Row 2) | F | F | F | F | **T** | F |
| `aab` (Row 3) | F | F | F | F | F | **T (Result)** |

---

## 5. Algorithmic Correctness

**Soundness.** Because $p[j-1] == \text{'*'}$ checks both $DP[i][j-2]$ (token vanishes) and $DP[i-1][j]$ (token absorbs one character of $s$), the recurrence exhaustively mirrors the mathematical semantics of Kleene star in regular languages.

**Completeness.** Cell dependencies flow strictly to the left (same row) or to the top-left (prior row). Computing the matrix row by row ensures all subproblems are solved before their dependent states are queried, guaranteeing exact and deterministic discovery of valid matchings.

---

## 6. Traps This Instance Exposes

- **Regex `*` vs Wildcard `*`:** In LeetCode 44 (Wildcard Matching), `*` is a standalone wild sequence. In LeetCode 10 (Regex), `*` can never appear alone at the start of a pattern; it always qualifies the preceding token $p[j-2]$.
- **Zero-Occurrence Lookback:** When evaluating a star, forgetting to check $DP[i][j-2]$ makes it impossible to discard unused patterns like `"c*"`.
- **Dot-Star Pattern (`".*"`):** When $p[j-2] == \text{'.'}$, the star can match any sequence of arbitrary characters because $s[i-1]$ always satisfies the character match condition.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M \cdot N)$, where $M = |s|$ and $N = |p|$. The table has $(M + 1) \times (N + 1)$ cells, each evaluated in $O(1)$ transitions.
- **Auxiliary Space Complexity:** $O(M \cdot N)$ for the memoization grid, reducible to $O(N)$ by keeping two rows.