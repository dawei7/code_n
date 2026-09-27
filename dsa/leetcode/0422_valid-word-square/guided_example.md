# Guided Example: Valid Word Square

We trace the step-by-step matrix transposition symmetry verification ($words[i][j] == words[j][i]$), ragged boundary existence checking ($j < m \land i < |words[j]|$), and coordinate alignment on representative word lists:

- **Input:** $words = [\text{"abcd"}, \text{"bnrt"}, \text{"crm"}, \text{"dt"}]$
- **Required output:** `true`
  - Row count: $m = 4$
  - Row lengths: $[4, 4, 3, 2]$
  - Symmetry verification by rows and columns:
    - **Row 0 ($i = 0$):** `"abcd"`
      - Col 0 ($j = 0$): $words[0][0] = \text{'a'} == words[0][0] = \text{'a'}$
      - Col 1 ($j = 1$): $words[0][1] = \text{'b'} == words[1][0] = \text{'b'}$
      - Col 2 ($j = 2$): $words[0][2] = \text{'c'} == words[2][0] = \text{'c'}$
      - Col 3 ($j = 3$): $words[0][3] = \text{'d'} == words[3][0] = \text{'d'}$
      - Column 0 reads `"abcd"` (**Matches Row 0**)
    - **Row 1 ($i = 1$):** `"bnrt"`
      - Col 0 ($j = 0$): $words[1][0] = \text{'b'} == words[0][1] = \text{'b'}$
      - Col 1 ($j = 1$): $words[1][1] = \text{'n'} == words[1][1] = \text{'n'}$
      - Col 2 ($j = 2$): $words[1][2] = \text{'r'} == words[2][1] = \text{'r'}$
      - Col 3 ($j = 3$): $words[1][3] = \text{'t'} == words[3][1] = \text{'t'}$
      - Column 1 reads `"bnrt"` (**Matches Row 1**)
    - **Row 2 ($i = 2$):** `"crm"`
      - Col 0 ($j = 0$): $words[2][0] = \text{'c'} == words[0][2] = \text{'c'}$
      - Col 1 ($j = 1$): $words[2][1] = \text{'r'} == words[1][2] = \text{'r'}$
      - Col 2 ($j = 2$): $words[2][2] = \text{'m'} == words[2][2] = \text{'m'}$
      - Column 2 reads `"crm"` (**Matches Row 2**)
    - **Row 3 ($i = 3$):** `"dt"`
      - Col 0 ($j = 0$): $words[3][0] = \text{'d'} == words[0][3] = \text{'d'}$
      - Col 1 ($j = 1$): $words[3][1] = \text{'t'} == words[1][3] = \text{'t'}$
      - Column 3 reads `"dt"` (**Matches Row 3**)
  - Every row $k$ matches column $k$ identically $\implies$ Return `true`
- **Character Mismatch Instance:** $words = [\text{"ball"}, \text{"area"}, \text{"read"}, \text{"lady"}] \implies words[0][2] = \text{'l'} \ne words[2][0] = \text{'r'} \implies \text{false}$
- **Single Character Instance:** $words = [\text{"z"}] \implies \text{true}$

This instance demonstrates ragged 2D matrix transposition symmetry, mathematically proves the dual boundary requirements preventing out-of-bounds ragged asymmetry, and derives $O(\sum |word|)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a list of strings $words = [\text{"abcd"}, \text{"bnrt"}, \text{"crm"}, \text{"dt"}]$:
Determine whether it forms a **valid word square**:
A sequence of words forms a valid word square if the $k$-th row and $k$-th column read the exact same string from left to right and top to bottom, for every $0 \le k < \max(m, \max |words|)$.

```text
Ragged Word Grid:
  Row 0:  a  b  c  d
  Row 1:  b  n  r  t
  Row 2:  c  r  m
  Row 3:  d  t

Transpose Check:
  Col 0: a-b-c-d  ==  Row 0: "abcd"  (Match)
  Col 1: b-n-r-t  ==  Row 1: "bnrt"  (Match)
  Col 2: c-r-m    ==  Row 2: "crm"   (Match)
  Col 3: d-t      ==  Row 3: "dt"    (Match)

All 4 rows and columns match -> true
```

### The Ragged Matrix Challenge
Unlike classical square matrices where every row has equal length $N$, word square inputs can be **ragged** (rows of differing lengths).
Symmetry requires two distinct guarantees for every character at coordinate $(i, j)$:
1. **Existence Symmetry:** If cell $(i, j)$ exists, the transposed cell $(j, i)$ must also exist (requiring $j < m$ and $i < |words[j]|$).
2. **Character Symmetry:** $words[i][j] == words[j][i]$.

---

## 2. Conceptual Foundation & Invariants

### 1. Coordinate Transposition Invariant:
For every pair $(i, j)$ where $0 \le i < m$ and $0 \le j < |words[i]|$:
- The transpose column index $j$ must refer to a valid existing row:
  $$
  j < m
  $$
- The transpose row $words[j]$ must have enough characters to contain column index $i$:
  $$
  i < |words[j]|
  $$
- The characters must match:
  $$
  words[i][j] == words[j][i]
  $$

### 2. Early-Exit Failure Predicate:
If any cell $(i, j)$ violates either existence or character equality:
$$
(j \ge m) \lor (i \ge |words[j]|) \lor (words[i][j] \ne words[j][i])
$$
Then the grid is asymmetric. Return `false` immediately.

> **Symmetry Invariant.** A word grid is a valid word square if and only if the matrix is completely symmetric across its main diagonal: $M = M^T$.

---

## 3. Step-by-Step Worked Execution

We trace $words = [\text{"abcd"}, \text{"bnrt"}, \text{"crm"}, \text{"dt"}]$ ($m = 4$):

---

### Row 0: `words[0] = "abcd"` ($|words[0]| = 4$)
- $j = 0$ (`'a'`): $j < 4$, $0 < |words[0]| (4)$, $words[0][0] == words[0][0] \implies$ Match `'a'`.
- $j = 1$ (`'b'`): $j < 4$, $0 < |words[1]| (4)$, $words[0][1] == words[1][0] \implies \text{'b'} == \text{'b'}$ (Match).
- $j = 2$ (`'c'`): $j < 4$, $0 < |words[2]| (3)$, $words[0][2] == words[2][0] \implies \text{'c'} == \text{'c'}$ (Match).
- $j = 3$ (`'d'`): $j < 4$, $0 < |words[3]| (2)$, $words[0][3] == words[3][0] \implies \text{'d'} == \text{'d'}$ (Match).

---

### Row 1: `words[1] = "bnrt"` ($|words[1]| = 4$)
- $j = 0$ (`'b'`): $j < 4$, $1 < |words[0]| (4)$, $words[1][0] == words[0][1] \implies \text{'b'} == \text{'b'}$ (Match).
- $j = 1$ (`'n'`): $j < 4$, $1 < |words[1]| (4)$, $words[1][1] == words[1][1] \implies \text{'n'} == \text{'n'}$ (Match).
- $j = 2$ (`'r'`): $j < 4$, $1 < |words[2]| (3)$, $words[1][2] == words[2][1] \implies \text{'r'} == \text{'r'}$ (Match).
- $j = 3$ (`'t'`): $j < 4$, $1 < |words[3]| (2)$, $words[1][3] == words[3][1] \implies \text{'t'} == \text{'t'}$ (Match).

---

### Row 2: `words[2] = "crm"` ($|words[2]| = 3$)
- $j = 0$ (`'c'`): $words[2][0] == words[0][2] \implies \text{'c'} == \text{'c'}$ (Match).
- $j = 1$ (`'r'`): $words[2][1] == words[1][2] \implies \text{'r'} == \text{'r'}$ (Match).
- $j = 2$ (`'m'`): $words[2][2] == words[2][2] \implies \text{'m'} == \text{'m'}$ (Match).

---

### Row 3: `words[3] = "dt"` ($|words[3]| = 2$)
- $j = 0$ (`'d'`): $words[3][0] == words[0][3] \implies \text{'d'} == \text{'d'}$ (Match).
- $j = 1$ (`'t'`): $words[3][1] == words[1][3] \implies \text{'t'} == \text{'t'}$ (Match).

---

### Termination:
All 13 character positions across all 4 words satisfied existence and transposition equality.
Return **`true`**.

---

## 4. Complete Execution Trace

| Coordinate $(i, j)$ | Char $words[i][j]$ | Transposed Row $j$ Valid? ($j < m$) | Transposed Col $i$ Valid? ($i < |words[j]|$) | Transposed Char $words[j][i]$ | Symmetry Match? |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $(0, 0)$ | `'a'` | Yes ($0 < 4$) | Yes ($0 < 4$) | `'a'` | **True** |
| $(0, 1)$ | `'b'` | Yes ($1 < 4$) | Yes ($0 < 4$) | `'b'` | **True** |
| $(0, 2)$ | `'c'` | Yes ($2 < 4$) | Yes ($0 < 3$) | `'c'` | **True** |
| $(0, 3)$ | `'d'` | Yes ($3 < 4$) | Yes ($0 < 2$) | `'d'` | **True** |
| $(1, 0)$ | `'b'` | Yes ($0 < 4$) | Yes ($1 < 4$) | `'b'` | **True** |
| $(1, 1)$ | `'n'` | Yes ($1 < 4$) | Yes ($1 < 4$) | `'n'` | **True** |
| $(1, 2)$ | `'r'` | Yes ($2 < 4$) | Yes ($1 < 3$) | `'r'` | **True** |
| $(1, 3)$ | `'t'` | Yes ($3 < 4$) | Yes ($1 < 2$) | `'t'` | **True** |
| $(2, 0)$ | `'c'` | Yes ($0 < 4$) | Yes ($2 < 4$) | `'c'` | **True** |
| $(2, 1)$ | `'r'` | Yes ($1 < 4$) | Yes ($2 < 4$) | `'r'` | **True** |
| $(2, 2)$ | `'m'` | Yes ($2 < 4$) | Yes ($2 < 3$) | `'m'` | **True** |
| $(3, 0)$ | `'d'` | Yes ($0 < 4$) | Yes ($3 < 4$) | `'d'` | **True** |
| $(3, 1)$ | `'t'` | Yes ($1 < 4$) | Yes ($3 < 4$) | `'t'` | **True** |

---

## 5. Boundary Cases & Failure Modes

- **Width Exceeds Total Rows ($words = [\text{"abc"}] \implies m = 1, |words[0]| = 3$):** Cell $(0, 2)$ has $j = 2 \ge m (1)$. Transpose row does not exist $\implies$ returns `false`.
- **Ragged Row Missing Transpose ($words = [\text{"ab"}, \text{"b"}] \implies m = 2$):** Cell $(0, 1)$ exists (`'b'`), but row $1$ has length 1. Transposed cell $(1, 0)$ exists, but what if $words = [\text{"abc"}, \text{"b"}]$? Cell $(0, 2)$ has $j=2 \ge m \implies$ `false`.
- **Character Mismatch ($words = [\text{"ball"}, \text{"area"}, \text{"read"}, \text{"lady"}] $):** $(0, 2) = \text{'l'}$, but $(2, 0) = \text{'r'}$. Transposition mismatch $\implies$ returns `false`.
- **Single Character ($words = [\text{"a"}]$):** $1 \times 1$ matrix is trivially symmetric $\implies$ returns `true`.

---

## 6. Traps & Common Anti-Patterns

- **Assuming Uniform Square Grid ($N \times N$):** Assuming every row has the same length causes `IndexOutOfBoundsException` on ragged word squares like `["abcd", "bnrt", "crm", "dt"]`.
- **Forgetting Row Boundary Check ($j < m$):** Accessing `words[j]` before checking if $j$ is within $[0, m-1]$ crashes when a word's length exceeds the total number of rows.
- **Transposing Full Strings:** Constructing all column strings in memory uses $O(\sum |word|)$ extra space. In-place index comparison $words[i][j] == words[j][i]$ runs in $O(1)$ auxiliary space.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $K = \sum_{i=0}^{m-1} |words[i]|$ be the total number of characters across all words.
  - The nested loops visit each character $(i, j)$ exactly once.
  - Boundary checks and array indexing take $O(1)$ time per character.
  - Total Time: $\mathcal{O}(K)$. For $K \le 500 \times 500 = 2.5 \times 10^5$, execution completes in under 2 ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$. Memory is strictly bounded to loop indices and length variables.
