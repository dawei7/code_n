# Guided Example: Wildcard Matching

We trace the step-by-step execution of 2D dynamic programming grid matching on a representative pattern instance:

- **Input:** $s = \text{"adceb"}$, $p = \text{"*a*b"}$
- **Required output:** $\text{True}$

This instance demonstrates wildcard wildcard expansions, handling `'?'` (single character wildcard) versus `'*'` (arbitrary sequence wildcard including empty sequence), base row empty-string matching, and the two-way transition rule for `'*'`.

---

## 1. Instance & Teaching Goal

Given an input string $s$ of length $M = 5$ and a pattern $p$ of length $N = 4$ containing wildcards `'?'` and `'*'`:
- `'?'` matches any single character.
- `'*'` matches any sequence of characters (including the empty sequence).

For $s = \text{"adceb"}$ and $p = \text{"*a*b"}$:
- The first `'*'` matches the empty sequence `""`.
- `'a'` matches `'a'`.
- The second `'*'` matches substring $\text{"dce"}$.
- `'b'` matches `'b'`.
- The entire string matches the pattern, yielding $\text{True}$.

A naive recursive search without memoization branches on every `'*'`, causing worst-case exponential time $O(2^{M+N})$. The optimal dynamic programming approach constructs an $(M+1) \times (N+1)$ boolean table $DP$, solving the matching problem in $O(M \cdot N)$ time.

---

## 2. Conceptual Foundation & Invariants

### 2D DP State Definition
Let $DP[i][j]$ be a boolean value indicating whether the prefix $s[0 \dots i-1]$ matches the pattern prefix $p[0 \dots j-1]$.

### Boundary Base Cases
1. **Empty String & Empty Pattern:**
   $$
   DP[0][0] = \text{True}
   $$
2. **Non-Empty String & Empty Pattern ($i > 0$):**
   $$
   DP[i][0] = \text{False}
   $$
3. **Empty String & Pattern with Leading Stars ($i = 0, j > 0$):**
   $$
   DP[0][j] = DP[0][j-1] \quad \text{if } p[j-1] == \text{'*'} \text{ else False}
   $$

### Recurrence Transitions
For $i \ge 1$ and $j \ge 1$:
1. **Exact Character Match or `'?'`:**
   If $p[j-1] == s[i-1]$ or $p[j-1] == \text{'?'}$:
   $$
   DP[i][j] = DP[i-1][j-1]
   $$
2. **Star Wildcard (`'*'`):**
   A star can either:
   - Match **empty sequence**: matches $s[0 \dots i-1]$ if $p[0 \dots j-2]$ matched $\implies DP[i][j-1]$.
   - Match **one or more characters**: matches $s[0 \dots i-1]$ if $p[0 \dots j-1]$ already matched $s[0 \dots i-2] \implies DP[i-1][j]$.
   Combining both possibilities:
   $$
   DP[i][j] = DP[i][j-1] \lor DP[i-1][j]
   $$

> **Invariant.** For any cell $(i, j)$, $DP[i][j] == \text{True}$ if and only if there exists a valid sequence of wildcard substitutions that transforms $p[0 \dots j-1]$ into $s[0 \dots i-1]$.

---

## 3. Step-by-Step Worked Execution

We build the DP table for $s = \text{"adceb"}$ ($M = 5$) and $p = \text{"*a*b"}$ ($N = 4$):

### Step 0: Row 0 (Empty String $s = \text{""}$)
- $DP[0][0] = \text{True}$ (empty matches empty).
- $j = 1$ ($p[0] = \text{'*'}$): $DP[0][1] = DP[0][0] = \text{True}$ (star matches empty).
- $j = 2$ ($p[1] = \text{'a'}$): $DP[0][2] = \text{False}$.
- $j = 3$ ($p[2] = \text{'*'}$): $DP[0][3] = DP[0][2] = \text{False}$.
- $j = 4$ ($p[3] = \text{'b'}$): $DP[0][4] = \text{False}$.

---

### Step 1: Row 1 ($s[0] = \text{'a'}$)
- $j = 1$ (`*`): $DP[1][0] \lor DP[0][1] = \text{False} \lor \text{True} = \text{True}$.
- $j = 2$ (`a`): Matches $s[0] = \text{'a'}$. Take diagonal $DP[0][1] = \text{True}$.
- $j = 3$ (`*`): $DP[1][2] \lor DP[0][3] = \text{True} \lor \text{False} = \text{True}$.
- $j = 4$ (`b`): Mismatch `'a' \ne 'b' \implies \text{False}$.

---

### Step 2: Row 2 ($s[1] = \text{'d'}$)
- $j = 1$ (`*`): $DP[2][0] \lor DP[1][1] = \text{False} \lor \text{True} = \text{True}$.
- $j = 2$ (`a`): Mismatch `'d' \ne 'a' \implies \text{False}$.
- $j = 3$ (`*`): $DP[2][2] \lor DP[1][3] = \text{False} \lor \text{True} = \text{True}$.
- $j = 4$ (`b`): Mismatch $\implies \text{False}$.

---

### Step 3 & 4: Rows 3 and 4 ($s[2] = \text{'c'}$, $s[3] = \text{'e'}$)
Both characters match the second `'*'` at $j = 3$:
- In Row 3: $DP[3][3] = DP[3][2] \lor DP[2][3] = \text{False} \lor \text{True} = \text{True}$.
- In Row 4: $DP[4][3] = DP[4][2] \lor DP[3][3] = \text{False} \lor \text{True} = \text{True}$.
- All $j = 4$ cells remain $\text{False}$ because neither `'c'` nor `'e'` equals `'b'`.

---

### Step 5: Row 5 ($s[4] = \text{'b'}$)
- $j = 1$ (`*`): $\text{True}$.
- $j = 2$ (`a`): $\text{False}$.
- $j = 3$ (`*`): $DP[5][2] \lor DP[4][3] = \text{False} \lor \text{True} = \text{True}$.
- $j = 4$ (`b`): $s[4] == \text{'b'}$. Take diagonal $DP[4][3] = \text{True}$!
- Terminal state: $DP[5][4] = \text{True}$.

---

## 4. Complete Execution Trace

### 2D DP State Matrix ($M \times N$)

| String Prefix $\downarrow$ / Pattern $\to$ | $\epsilon$ (Col 0) | `*` (Col 1) | `a` (Col 2) | `*` (Col 3) | `b` (Col 4) |
|:---|:---:|:---:|:---:|:---:|:---:|
| $\epsilon$ (Row 0) | **T** | **T** | F | F | F |
| `a` (Row 1) | F | **T** | **T** | **T** | F |
| `ad` (Row 2) | F | **T** | F | **T** | F |
| `adc` (Row 3) | F | **T** | F | **T** | F |
| `adce` (Row 4) | F | **T** | F | **T** | F |
| `adceb` (Row 5) | F | **T** | F | **T** | **T (Result)** |

---

## 5. Algorithmic Correctness

**Soundness.** Every cell in the DP table satisfies the inductive definition of wildcard matching. When $p[j-1] == \text{'*'},$ setting $DP[i][j] = DP[i][j-1] \lor DP[i-1][j]$ strictly accounts for all possibilities: either the star consumes zero characters (looking left to $j-1$) or it consumes at least one character (looking up to $i-1$).

**Completeness.** The table evaluates every prefix pair $(i, j)$ in topological order. Because dynamic programming considers both branches of `'*'` without greedy premature commitment, no viable matching derivation can be overlooked.

---

## 6. Traps This Instance Exposes

- **Wildcard Difference from Regex:** In LeetCode 10 (Regular Expression Matching), `*` modifies the *preceding* element (`a*`). In Wildcard Matching (LeetCode 44), `*` is a standalone token that matches any sequence of characters independently.
- **Consecutive Stars:** A pattern with consecutive stars like `****` is equivalent to a single `*`. Collapsing consecutive stars into one star reduces redundant table columns.
- **Empty String Matches:** Leading stars can match the empty string (e.g. $s = \text{""}, p = \text{"*"}$). Row 0 initialization must correctly propagate `True` across all consecutive leading stars.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M \cdot N)$, where $M = |s|$ and $N = |p|$. The table contains $(M + 1) \times (N + 1)$ cells, each computed in $O(1)$ time.
- **Auxiliary Space Complexity:** $O(M \cdot N)$ for the full 2D table, which can be optimized to $O(N)$ space by maintaining only the previous and current rows.