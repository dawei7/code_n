# Guided Example: Delete Operation for Two Strings

We trace the step-by-step longest common subsequence duality ($m + n - 2 \cdot \text{LCS}$), dynamic programming edit table initialization ($f[i][0] = i, \; f[0][j] = j$), matching character diagonal transfer ($f[i-1][j-1]$), mismatch deletion minimization ($\min(f[i-1][j], f[i][j-1]) + 1$), and minimal deletion step evaluation on representative string pairs:

- **Input:** $word1 = \text{"sea"}, \quad word2 = \text{"eat"}$
- **Required output:** `2`
  - Allowed operation: In one step, delete exactly one character from either string.
  - Goal: Find the minimum total deletion steps to reduce both strings to identical strings.
- **The Longest Common Subsequence (LCS) Duality:**
  - When two strings are made equal using only deletions, the resulting shared string must be a **common subsequence** of both $word1$ and $word2$.
  - To **minimize deletions**, we must **maximize the length of the preserved common subsequence**!
  - Let $L = \text{len}(\text{LCS}(word1, word2))$:
    - Number of deletions from $word1$: $m - L$
    - Number of deletions from $word2$: $n - L$
    - Total deletions required:
      $$
      \text{Steps} = (m - L) + (n - L) = m + n - 2L
      $$
  - For $word1 = \text{"sea"}$ ($m = 3$) and $word2 = \text{"eat"}$ ($n = 3$):
    - The longest common subsequence is $\text{"ea"}$ (length $L = 2$).
    - Total deletions: $3 + 3 - 2(2) = 6 - 4 = \mathbf{2}$.
- **2D Dynamic Programming Edit Table Trace ($f[i][j]$):**
  - Let $f[i][j]$ be the minimum deletion operations to make prefix $word1[0 \dots i-1]$ and prefix $word2[0 \dots j-1]$ equal.
  - **Base Cases (Empty Prefix):**
    - $f[i][0] = i$: To match an empty string, delete all $i$ characters from $word1$.
    - $f[0][j] = j$: Delete all $j$ characters from $word2$.
  - **State Transitions:**
    - If characters match ($word1[i-1] == word2[j-1]$):
      $$
      f[i][j] = f[i-1][j-1] \quad (\text{Preserve matching character for free!})
      $$
    - If characters differ ($word1[i-1] \ne word2[j-1]$):
      $$
      f[i][j] = \min(f[i-1][j], \; f[i][j-1]) + 1 \quad (\text{Delete one character})
      $$
- **Step-by-step table construction for $word1 = \text{"sea"}$, $word2 = \text{"eat"}$:**
  - **Row 0 (Empty $word1 = \text{""}$):**
    $$
    f[0] = [0, \; 1, \; 2, \; 3]
    $$
  - **Row 1 ($word1[0] = \text{'s'}$):**
    - $j = 1$ ($word2[0] = \text{'e'}$):
      - Differ: $\min(f[0][1], f[1][0]) + 1 = \min(1, 1) + 1 = \mathbf{2}$.
    - $j = 2$ ($word2[1] = \text{'a'}$):
      - Differ: $\min(f[0][2], f[1][1]) + 1 = \min(2, 2) + 1 = \mathbf{3}$.
    - $j = 3$ ($word2[2] = \text{'t'}$):
      - Differ: $\min(f[0][3], f[1][2]) + 1 = \min(3, 3) + 1 = \mathbf{4}$.
    - Row 1: $[1, 2, 3, 4]$.
  - **Row 2 ($word1[1] = \text{'e'}$):**
    - $j = 1$ ($word2[0] = \text{'e'}$):
      - **Match!** Both are `'e'`: $f[1][0] = \mathbf{1}$.
    - $j = 2$ ($word2[1] = \text{'a'}$):
      - Differ: $\min(f[1][2], f[2][1]) + 1 = \min(3, 1) + 1 = \mathbf{2}$.
    - $j = 3$ ($word2[2] = \text{'t'}$):
      - Differ: $\min(f[1][3], f[2][2]) + 1 = \min(4, 2) + 1 = \mathbf{3}$.
    - Row 2: $[2, 1, 2, 3]$.
  - **Row 3 ($word1[2] = \text{'a'}$):**
    - $j = 1$ ($word2[0] = \text{'e'}$):
      - Differ: $\min(f[2][1], f[3][0]) + 1 = \min(1, 3) + 1 = \mathbf{2}$.
    - $j = 2$ ($word2[1] = \text{'a'}$):
      - **Match!** Both are `'a'`: $f[2][1] = \mathbf{1}$.
    - $j = 3$ ($word2[2] = \text{'t'}$):
      - Differ: $\min(f[2][3], f[3][2]) + 1 = \min(3, 1) + 1 = \mathbf{2}$.
    - Row 3: $[3, 2, 1, \mathbf{2}]$.
  - **Result Extraction:**
    $$
    f[3][3] = \mathbf{2}
    $$
  - Transformation sequence:
    1. Delete `'s'` from `"sea"` $\to$ `"ea"`.
    2. Delete `'t'` from `"eat"` $\to$ `"ea"`.
    Both strings become `"ea"` in 2 deletions!
- **Subsequence Dominance Instance ($word1 = \text{"leetcode"}, word2 = \text{"etco"}$):**
  - All 4 characters of $word2$ appear in order in $word1$.
  - $L = 4 \implies 8 + 4 - 2(4) = \mathbf{4}$ deletions (deleting 'l', 'e', 'd', 'e' from "leetcode").
- **Completely Disjoint Strings ($word1 = \text{"a"}, word2 = \text{"b"}$):**
  - $L = 0 \implies 1 + 1 - 0 = \mathbf{2}$ deletions.
- **Identical Strings ($word1 = \text{"same"}, word2 = \text{"same"}$):**
  - $L = 4 \implies 4 + 4 - 2(4) = \mathbf{0}$ deletions.

This instance demonstrates distance metric symmetry over edit alphabets, mathematically proves why minimizing deletions is equivalent to finding the maximum common sub-structure, and derives $O(M \cdot N)$ runtime and $O(M \cdot N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given two strings $word1$ and $word2$:
Find the **minimum number of deletion steps** to make both strings equal.
In one step, you delete one character from either string.

```text
word1: "sea"
word2: "eat"

Step 1: Delete 's' from "sea" -> "ea"
Step 2: Delete 't' from "eat" -> "ea"

Both strings are now "ea"!
Minimum Steps = 2
```

### Connection to Longest Common Subsequence (LCS)
- Since the only operation allowed is deletion:
  Any final equal string must be a **common subsequence** of both original strings.
- To minimize the total characters removed, the final string must be as long as possible:
  $$
  \text{Final Length} = \text{len}(\text{LCS})
  $$
- Total deletions:
  $$
  \text{Deletions} = |word1| + |word2| - 2 \cdot \text{len}(\text{LCS})
  $$

---

## 2. Conceptual Foundation & Invariants

### 1. The Edit Distance Formulation $f[i][j]$:
- $f[i][j]$: minimum deletions to equalize $word1[0 \dots i-1]$ and $word2[0 \dots j-1]$.

### 2. Boundary Values:
$$
f[i][0] = i \quad (\forall i \in [0, m]), \quad f[0][j] = j \quad (\forall j \in [0, n])
$$

### 3. State Transitions:
$$
f[i][j] =
\begin{cases}
f[i-1][j-1] & \text{if } word1[i-1] == word2[j-1] \\
\min(f[i-1][j], \; f[i][j-1]) + 1 & \text{if } word1[i-1] \ne word2[j-1]
\end{cases}
$$

> **Optimal Preservation Invariant.** When two characters match, matching them consumes 0 deletion cost, which is strictly optimal compared to deleting either character.

---

## 3. Step-by-Step Worked Execution

We trace $word1 = \text{"sea"}$, $word2 = \text{"eat"}$:

---

### Step 1: Base Table Framing
$$
\begin{array}{c|cccc}
 & \epsilon & \text{e} & \text{a} & \text{t} \\
\hline
\epsilon & 0 & 1 & 2 & 3 \\
\text{s} & 1 & \cdot & \cdot & \cdot \\
\text{e} & 2 & \cdot & \cdot & \cdot \\
\text{a} & 3 & \cdot & \cdot & \cdot \\
\end{array}
$$

---

### Step 2: Row 1 (`'s'`)
- Against `'e'`: $\min(1, 1) + 1 = 2$.
- Against `'a'`: $\min(2, 2) + 1 = 3$.
- Against `'t'`: $\min(3, 3) + 1 = 4$.

---

### Step 3: Row 2 (`'e'`)
- Against `'e'`: Match! $f[1][0] = \mathbf{1}$.
- Against `'a'`: $\min(3, 1) + 1 = 2$.
- Against `'t'`: $\min(4, 2) + 1 = 3$.

---

### Step 4: Row 3 (`'a'`)
- Against `'e'`: $\min(1, 3) + 1 = 2$.
- Against `'a'`: Match! $f[2][1] = \mathbf{1}$.
- Against `'t'`: $\min(3, 1) + 1 = \mathbf{2}$.

---

### Step 5: Final Result
$$
f[3][3] = \mathbf{2}
$$

---

## 4. Complete Execution Trace

| DP Table | $\epsilon$ | `'e'` | `'a'` | `'t'` |
|:---:|:---:|:---:|:---:|:---:|
| $\epsilon$ | $0$ | $1$ | $2$ | $3$ |
| `'s'` | $1$ | $2$ | $3$ | $4$ |
| `'e'` | $2$ | **$1$** | $2$ | $3$ |
| `'a'` | $3$ | $2$ | **$1$** | **$2$** |

---

## 5. Boundary Cases & Failure Modes

- **One String Empty ($m = 0$):** $f[0][n] = n$ deletions.
- **Both Strings Identical:** All diagonal matches $\implies 0$ deletions.
- **No Shared Characters ($"a", "b"$):** $f[1][1] = \min(1, 1) + 1 = 2$.
- **String Length up to 500:** $500 \times 500 = 2.5 \times 10^5$ cells, completing in $< 15$ ms.

---

## 6. Traps & Common Anti-Patterns

- **Attempting Greedy Substring Matching:** Longest common *substring* is contiguous, whereas this problem permits non-contiguous *subsequences*. Greedily matching the longest contiguous block misses optimal scattered subsequences.
- **Initializing Base Cases to 0:** Setting $f[i][0] = 0$ implies that turning any prefix into an empty string costs 0 steps, destroying the deletion count.
- **Forgetting Diagonal Match Advantage:** If $a == b$, taking $\min(f[i-1][j], f[i][j-1]) + 1$ penalizes matching characters, failing to find the LCS.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Table dimensions: $(M + 1) \times (N + 1)$.
  - Each cell computes a comparison and at most one addition taking $\mathcal{O}(1)$ time.
  - Total Time: $\mathcal{O}(M \cdot N)$. For $M, N \le 500$, $2.5 \times 10^5$ operations finish in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(M \cdot N)$ space for the DP matrix (can be reduced to $O(N)$ with rolling row buffers).
