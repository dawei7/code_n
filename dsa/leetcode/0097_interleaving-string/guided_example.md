# Guided Example: Interleaving String

We trace the step-by-step 2D dynamic programming grid matching and path verification on representative valid and invalid instances:

- **Valid Interleaved Instance:** $s_1 = \text{"aabcc"}, s_2 = \text{"dbbca"}, s_3 = \text{"aadbbcbcac"}$
- **Required output:** $\text{True}$
- **Failing Instance:** $s_1 = \text{"aabcc"}, s_2 = \text{"dbbca"}, s_3 = \text{"aadbbbaccc"} \implies \text{False}$

This instance demonstrates 2D grid lattice path formulation, prefix character matching from either $s_1$ (downward move) or $s_2$ (rightward move), total length compatibility filtering ($|s_1| + |s_2| == |s_3|$), and space compression to a 1D rolling row in $O(|s_2|)$ space.

---

## 1. Instance & Teaching Goal

Given strings $s_1 = \text{"aabcc"}$, $s_2 = \text{"dbbca"}$, and $s_3 = \text{"aadbbcbcac"}$, determine whether $s_3$ is formed by an interleaving of $s_1$ and $s_2$.

An interleaving divides $s_1$ and $s_2$ into substrings such that interleaving them preserves the internal relative order of characters from both sources. One such split is:
- $s_1 = \mathbf{aa} \cdot \mathbf{bc} \cdot \mathbf{c}$
- $s_2 = \underline{\text{d}} \cdot \underline{\text{b}} \cdot \underline{\text{bca}}$
- Interleaved: $\mathbf{aa} \underline{\text{d}} \underline{\text{b}} \mathbf{bc} \underline{\text{bca}} \mathbf{c} = \text{"aadbbcbcac"}$.

Note that $s_1$ contributes `'a'`, `'a'`, `'b'`, `'c'`, `'c'` in that order and $s_2$ contributes `'d'`, `'b'`, `'b'`, `'c'`, `'a'` in that order; the split above is one of several that obey both orders, which is exactly why a greedy choice between the two heads is unsafe.

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
6. **At $(3, 2) \to$ Move Down to $(4, 2)$:**
   $s_1[3] = \text{'c'}, s_3[5] = \text{'c'}$. Match! $DP[4][2] = \text{True}$.
7. **At $(4, 2) \to$ Move Right to $(4, 3)$:**
   $s_2[2] = \text{'b'}, s_3[6] = \text{'b'}$. Match! $DP[4][3] = \text{True}$.
8. **At $(4, 3) \to$ Move Right to $(4, 4)$:**
   $s_2[3] = \text{'c'}, s_3[7] = \text{'c'}$. Match! $DP[4][4] = \text{True}$.
9. **At $(4, 4) \to$ Move Right to $(4, 5)$:**
   $s_2[4] = \text{'a'}, s_3[8] = \text{'a'}$. Match! $DP[4][5] = \text{True}$.
10. **At $(4, 5) \to$ Move Down to $(5, 5)$:**
    $s_1[4] = \text{'c'}, s_3[9] = \text{'c'}$. Match! $DP[5][5] = \text{True}$.

Ten moves are exactly right: five downward moves consume all five characters of $s_1$ and five rightward moves consume all five characters of $s_2$. The same path is written out as a move table so that each comparison can be checked against the target index $i + j - 1$:

| Step | From $(i, j)$ | To $(i, j)$ | Move and source index | Character consumed | Target index $i + j - 1$ | Required $s_3$ character | Match |
|:---:|:---:|:---:|:---|:---:|:---:|:---:|:---:|
| 1 | $(0, 0)$ | $(1, 0)$ | Down, $s_1[0]$ | `'a'` | 0 | `'a'` | Yes |
| 2 | $(1, 0)$ | $(2, 0)$ | Down, $s_1[1]$ | `'a'` | 1 | `'a'` | Yes |
| 3 | $(2, 0)$ | $(2, 1)$ | Right, $s_2[0]$ | `'d'` | 2 | `'d'` | Yes |
| 4 | $(2, 1)$ | $(2, 2)$ | Right, $s_2[1]$ | `'b'` | 3 | `'b'` | Yes |
| 5 | $(2, 2)$ | $(3, 2)$ | Down, $s_1[2]$ | `'b'` | 4 | `'b'` | Yes |
| 6 | $(3, 2)$ | $(4, 2)$ | Down, $s_1[3]$ | `'c'` | 5 | `'c'` | Yes |
| 7 | $(4, 2)$ | $(4, 3)$ | Right, $s_2[2]$ | `'b'` | 6 | `'b'` | Yes |
| 8 | $(4, 3)$ | $(4, 4)$ | Right, $s_2[3]$ | `'c'` | 7 | `'c'` | Yes |
| 9 | $(4, 4)$ | $(4, 5)$ | Right, $s_2[4]$ | `'a'` | 8 | `'a'` | Yes |
| 10 | $(4, 5)$ | $(5, 5)$ | Down, $s_1[4]$ | `'c'` | 9 | `'c'` | Yes |

Every move consumes exactly one character of the target, so after step $t$ the prefix of length $t$ is accounted for by $i + j = t$ consumed source characters — the diagonal that the reachability matrix is indexed by.

Terminal cell $DP[5][5]$ is reachable $\implies$ returns $\mathbf{True}$.

---

## 4. Complete Execution Trace

### 2D DP Reachability Matrix ($DP[i][j]$)

Columns correspond to $s_2 = \text{"dbbca"}$ ($j = 0 \dots 5$), Rows to $s_1 = \text{"aabcc"}$ ($i = 0 \dots 5$):

| $s_1 \backslash s_2$ | $\emptyset$ ($j=0$) | `'d'` ($j=1$) | `'b'` ($j=2$) | `'b'` ($j=3$) | `'c'` ($j=4$) | `'a'` ($j=5$) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **$\emptyset$ ($i=0$)** | **T** | F | F | F | F | F |
| **`'a'` ($i=1$)** | **T** | F | F | F | F | F |
| **`'a'` ($i=2$)** | **T** | **T** | **T** | **T** | **T** | F |
| **`'b'` ($i=3$)** | F | **T** | **T** | F | **T** | F |
| **`'c'` ($i=4$)** | F | F | **T** | **T** | **T** | **T** |
| **`'c'` ($i=5$)** | F | F | F | **T** | F | **T (Result)** |

Reading the matrix as diagonals confirms the move table: the reachable cells on the diagonal $i + j = 5$ are $(2, 3)$ and $(3, 2)$, so two distinct prefixes of the same length are alive at once. Only $(5, 5)$ matters at the end, and it is reached from $(4, 5)$ by a downward move.

### Failing Comparison: $s_3 = \text{"aadbbbaccc"}$

The table below lists, for each prefix length $t$, the set of cells $(i, j)$ on the diagonal $i + j = t$ that survive. It is the frontier of a breadth-first reading of the same recurrence:

| $t$ | Required character $s_3[t-1]$ | Surviving states $(i, j)$ | What the next move requires |
|:---:|:---:|:---|:---|
| 0 | — | $(0, 0)$ | Start state. |
| 1 | `'a'` | $(1, 0)$ | Only $s_1[0]$ matches, because $s_2[0] = \text{'d'}$. |
| 2 | `'a'` | $(2, 0)$ | Again only the $s_1$ head matches. |
| 3 | `'d'` | $(2, 1)$ | Only $s_2[0]$ matches here. |
| 4 | `'b'` | $(2, 2)$, $(3, 1)$ | Both heads match, so the frontier widens for the first time. |
| 5 | `'b'` | $(2, 3)$, $(3, 2)$ | Two survivors again, reached by different orderings. |
| 6 | `'b'` | $(3, 3)$ | The two branches reconverge on a single state. |
| 7 | `'a'` | none | The heads are $s_1[3] = \text{'c'}$ and $s_2[3] = \text{'c'}$, and neither equals `'a'`, so no successor cell exists. |

Once the frontier is empty it can never refill, because every later cell depends on a cell on the previous diagonal. The answer is therefore $\text{False}$, and the check is complete after $7$ of the $10$ target characters rather than at the end.

---

## 5. Algorithmic Correctness

**Soundness.** A cell $(i, j)$ is set to `True` only if an already confirmed valid prefix $(i-1, j)$ or $(i, j-1)$ can be extended by a matching character from $s_1$ or $s_2$ respectively. Thus, every reachable cell corresponds to a provably correct prefix interleaving.

**Completeness.** By evaluating every cell $(i, j)$ in row-major topological order, all possible combination paths through the grid are explored simultaneously. If any interleaving path exists, cell $(M, N)$ is guaranteed to evaluate to `True`.

---

## 6. Traps This Instance Exposes

The boundary cases below are the ones a submitted solution actually meets, and each answer follows directly from the recurrence rather than from a special branch:

| Boundary | Instance | Answer | Why that answer is forced |
|:---|:---|:---|:---|
| Both sources empty | $s_1 = \text{""}$, $s_2 = \text{""}$, $s_3 = \text{""}$ | True | $M + N = 0 = \lvert s_3 \rvert$, and the start cell is already the terminal cell. |
| One source empty | $s_1 = \text{"abc"}$, $s_2 = \text{""}$, $s_3 = \text{"abc"}$ | True | Every target character must then come from $s_1$ in order, which is exactly the column-0 edge recurrence $DP[i][0] = DP[i-1][0] \land s_1[i-1] = s_3[i-1]$. |
| Total length mismatch | $s_1 = \text{"abc"}$, $s_2 = \text{"def"}$, $s_3 = \text{"abcdefg"}$ | False | $3 + 3 = 6 \ne 7$; one target character could never be consumed by any move, so the guard rejects the input before any grid work. |
| Ambiguity that fails late | $s_1 = \text{"aaaa"}$, $s_2 = \text{"aaaa"}$, $s_3 = \text{"aaaaaaab"}$ | False | The sources contribute eight `'a'` characters and no `'b'`, so the frontier survives the first seven diagonals and dies on the final character. |
| Lengths swapped | $s_1 = \text{"dbbca"}$, $s_2 = \text{"aabcc"}$, $s_3 = \text{"aadbbcbcac"}$ | True | Interleaving is symmetric in the two sources; only the assignment of the $i$ and $j$ axes changes, not reachability. |

- **Initial Length Mismatch:** If $|s_1| + |s_2| \ne |s_3|$, no interleaving is possible. Checking this up front avoids running the entire $O(M \cdot N)$ table for invalid inputs.
- **Empty String Inputs:** If $s_1 = \text{""}, s_2 = \text{""}, s_3 = \text{""}$, $M = N = 0$. The base case $DP[0][0] = \text{True}$ handles empty inputs seamlessly without crashes.
- **Greedy Matching Fallacy:** If both $s_1[i]$ and $s_2[j]$ equal $s_3[i+j]$, choosing greedily from one string can lead to a dead end later. Dynamic programming maintains both possibilities in parallel.

---

## 7. Complexity Derivation

All four implementations below compute the same recurrence; they differ only in how much of it is remembered at once:

| Strategy | State that is stored | Time | Space | Tradeoff or failure mode |
|:---|:---|:---|:---|:---|
| Plain recursion on $(i, j)$ | Only the current index pair on the call stack | $O(2^{M+N})$ worst case | $O(M + N)$ stack | Whenever both heads match the target character the same pair $(i, j)$ is re-entered and re-solved, which is the exponential blow-up this lesson's grid removes. |
| Memoised recursion | One boolean per cell, filled on demand | $O(M \cdot N)$ | $O(M \cdot N)$ plus $O(M + N)$ stack | Same asymptotics as the grid, but the recursion depth still grows with $M + N$, so a strictly iterative order is usually preferred. |
| Iterative 2D grid | One boolean per cell, filled in row-major order | $O(M \cdot N)$ | $O(M \cdot N)$ | The matrix doubles as the reachability witness, which makes auditing easy; the full grid is the price. |
| Iterative rolling row | One boolean per column $j$, overwritten in place | $O(M \cdot N)$ | $O(N)$ | The row must be filled left to right so that the value to the left already belongs to the current row; reading it before it is updated mixes two different $i$ values and silently loses paths. |

- **Time Complexity:** $O(M \cdot N)$, where $M = |s_1|$ and $N = |s_2|$. The 2D DP grid contains $(M + 1) \times (N + 1)$ cells, each computed in $O(1)$ operations.
- **Auxiliary Space Complexity:** $O(N)$ when compressed to a 1D rolling array, or $O(M \cdot N)$ for the full 2D table.