# Guided Example: Interleaving String

We trace the step-by-step 2D dynamic programming grid matching and path verification on representative valid and invalid instances:

- **Valid Interleaved Instance:** $s_1 = \text{"aabcc"}, s_2 = \text{"dbbca"}, s_3 = \text{"aadbbcbcac"}$
- **Required output:** $\text{True}$
- **Failing Instance:** $s_1 = \text{"aabcc"}, s_2 = \text{"dbbca"}, s_3 = \text{"aadbbbaccc"} \implies \text{False}$

This instance demonstrates 2D grid lattice path formulation, prefix character matching from either $s_1$ (downward move) or $s_2$ (rightward move), total length compatibility filtering ($|s_1| + |s_2| == |s_3|$), and space compression to a 1D rolling row in $O(|s_2|)$ space.

---

## 1. Instance & Teaching Goal

Given strings $s_1 = \text{"aabcc"}$, $s_2 = \text{"dbbca"}$, and $s_3 = \text{"aadbbcbcac"}$, determine whether $s_3$ is formed by an interleaving of $s_1$ and $s_2$.

An interleaving divides $s_1$ and $s_2$ into substrings such that interleaving them preserves the internal relative order of characters from both sources:
- $s_1 = \mathbf{aa} \cdot \mathbf{b} \cdot \mathbf{c} \cdot \mathbf{c}$
- $s_2 = \underline{\text{d}} \cdot \underline{\text{bb}} \cdot \underline{\text{c}} \cdot \underline{\text{a}}$
- Interleaved: $\mathbf{aa} \underline{\text{d}} \underline{\text{bb}} \mathbf{b} \underline{\text{c}} \mathbf{c} \underline{\text{a}} \mathbf{c} = \text{"aadbbcbcac"}$.

A naive recursive exploration branches whenever both $s_1[i]$ and $s_2[j]$ match $s_3[i+j]$, leading to exponential $O(2^{M+N})$ worst-case branching.
By framing the problem as finding a path from $(0, 0)$ to $(M, N)$ in an $(M+1) \times (N+1)$ boolean DP grid, each subproblem $(i, j)$ is computed once in $O(M \cdot N)$ time.

---

## 2. Conceptual Foundation & Invariants

### 2D Grid Lattice Formulation
Let $M = |s_1|$ and $N = |s_2|$.
1. **Length Guard:**
   If $M + N \ne |s_3|$: return $\text{False}$ immediately.
2. **State Definition:**
   $DP[i][j]$ is `True` if prefix $s_1[0 \dots i-1]$ and prefix $s_2[0 \dots j-1]$ can interleave to form prefix $s_3[0 \dots i+j-1]$.
3. **Base Case:**
   $DP[0][0] = \text{True}$ (two empty strings trivially interleave into an empty string).
4. **Boundary Edges:**
   - Column 0 (matching $s_1$ alone):
     $$
     DP[i][0] = DP[i-1][0] \land (s_1[i-1] == s_3[i-1])
     $$
   - Row 0 (matching $s_2$ alone):
     $$
     DP[0][j] = DP[0][j-1] \land (s_2[j-1] == s_3[j-1])
     $$
5. **Transitions ($i \ge 1, j \ge 1$):**
   A cell $(i, j)$ is reachable if:
   - **From above (use $s_1[i-1]$):** $DP[i-1][j]$ is `True` and $s_1[i-1] == s_3[i+j-1]$
   - **From left (use $s_2[j-1]$):** $DP[i][j-1]$ is `True` and $s_2[j-1] == s_3[i+j-1]$
   $$
   DP[i][j] = (DP[i-1][j] \land s_1[i-1] == s_3[i+j-1]) \lor (DP[i][j-1] \land s_2[j-1] == s_3[i+j-1])
   $$

> **Invariant.** Cell $DP[i][j] = \text{True}$ if and only if there exists a valid interleaving sequence that consumes exactly $i$ characters from $s_1$ and $j$ characters from $s_2$ to match $s_3[0 \dots i+j-1]$.

---

## 3. Step-by-Step Worked Execution

We trace $s_1 = \text{"aabcc"}$ ($M = 5$), $s_2 = \text{"dbbca"}$ ($N = 5$), $s_3 = \text{"aadbbcbcac"}$ ($|s_3| = 10$):

### Successful Path Trajectory
We trace the sequence of coordinate steps from $(0, 0)$ to $(5, 5)$:

1. **At $(0, 0) \to$ Move Down to $(1, 0)$:**
   $s_1[0] = \text{'a'}, s_3[0] = \text{'a'}$. Match! $DP[1][0] = \text{True}$.
2. **At $(1, 0) \to$ Move Down to $(2, 0)$:**
   $s_1[1] = \text{'a'}, s_3[1] = \text{'a'}$. Match! $DP[2][0] = \text{True}$.
3. **At $(2, 0) \to$ Move Right to $(2, 1)$:**
   $s_2[0] = \text{'d'}, s_3[2] = \text{'d'}$. Match! $DP[2][1] = \text{True}$.
4. **At $(2, 1) \to$ Move Right to $(2, 2)$:**
   $s_2[1] = \text{'b'}, s_3[3] = \text{'b'}$. Match! $DP[2][2] = \text{True}$.
5. **At $(2, 2) \to$ Move Down to $(3, 2)$:**
   $s_1[2] = \text{'b'}, s_3[4] = \text{'b'}$. Match! $DP[3][2] = \text{True}$.
6. **At $(3, 2) \to$ Move Right to $(3, 3)$:**
   $s_2[2] = \text{'b'}, s_3[5] = \text{'b'}$. Match! $DP[3][3] = \text{True}$.
7. **At $(3, 3) \to$ Move Down to $(4, 3)$:**
   $s_1[3] = \text{'c'}, s_3[6] = \text{'c'}$. Match! $DP[4][3] = \text{True}$.
8. **At $(4, 3) \to$ Move Right to $(4, 4)$:**
   $s_2[3] = \text{'c'}, s_3[7] = \text{'c'}$. Match! $DP[4][4] = \text{True}$.
9. **At $(4, 4) \to$ Move Down to $(5, 4)$:**
   $s_1[4] = \text{'c'}, s_3[8] = \text{'c'}$. Match! $DP[5][4] = \text{True}$.
10. **At $(5, 4) \to$ Move Right to $(5, 5)$:**
    $s_2[4] = \text{'a'}, s_3[9] = \text{'a'}$. Match! $DP[5][5] = \text{True}$.

Terminal cell $DP[5][5]$ is reachable $\implies$ returns $\mathbf{True}$.

---

## 4. Complete Execution Trace

### 2D DP Reachability Matrix ($DP[i][j]$)

Columns correspond to $s_2 = \text{"dbbca"}$ ($j = 0 \dots 5$), Rows to $s_1 = \text{"aabcc"}$ ($i = 0 \dots 5$):

| $s_1 \backslash s_2$ | $\emptyset$ ($j=0$) | `'d'` ($j=1$) | `'b'` ($j=2$) | `'b'` ($j=3$) | `'c'` ($j=4$) | `'a'` ($j=5$) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **$\emptyset$ ($i=0$)** | **T** | F | F | F | F | F |
| **`'a'` ($i=1$)** | **T** | F | F | F | F | F |
| **`'a'` ($i=2$)** | **T** | **T** | **T** | F | F | F |
| **`'b'` ($i=3$)** | F | **T** | **T** | **T** | F | F |
| **`'c'` ($i=4$)** | F | F | **T** | **T** | **T** | F |
| **`'c'` ($i=5$)** | F | F | F | **T** | **T** | **T (Result)** |

### Failing Comparison: $s_3 = \text{"aadbbbaccc"}$
At index 6, the required character is `'b'`, but from all valid states at length 6, both available heads are `'c'`. The frontier becomes empty (all false), safely returning $\text{False}$.

---

## 5. Algorithmic Correctness

**Soundness.** A cell $(i, j)$ is set to `True` only if an already confirmed valid prefix $(i-1, j)$ or $(i, j-1)$ can be extended by a matching character from $s_1$ or $s_2$ respectively. Thus, every reachable cell corresponds to a provably correct prefix interleaving.

**Completeness.** By evaluating every cell $(i, j)$ in row-major topological order, all possible combination paths through the grid are explored simultaneously. If any interleaving path exists, cell $(M, N)$ is guaranteed to evaluate to `True`.

---

## 6. Traps This Instance Exposes

- **Initial Length Mismatch:** If $|s_1| + |s_2| \ne |s_3|$, no interleaving is possible. Checking this up front avoids running the entire $O(M \cdot N)$ table for invalid inputs.
- **Empty String Inputs:** If $s_1 = \text{""}, s_2 = \text{""}, s_3 = \text{""}$, $M = N = 0$. The base case $DP[0][0] = \text{True}$ handles empty inputs seamlessly without crashes.
- **Greedy Matching Fallacy:** If both $s_1[i]$ and $s_2[j]$ equal $s_3[i+j]$, choosing greedily from one string can lead to a dead end later. Dynamic programming maintains both possibilities in parallel.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M \cdot N)$, where $M = |s_1|$ and $N = |s_2|$. The 2D DP grid contains $(M + 1) \times (N + 1)$ cells, each computed in $O(1)$ operations.
- **Auxiliary Space Complexity:** $O(N)$ when compressed to a 1D rolling array, or $O(M \cdot N)$ for the full 2D table.