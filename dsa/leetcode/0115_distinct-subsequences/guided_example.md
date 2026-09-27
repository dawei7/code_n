# Guided Example: Distinct Subsequences

We trace the step-by-step 2D dynamic programming grid recurrence and backward 1D rolling array optimization on representative string instances:

- **Input:** $s = \text{"rabbbit"}$, $t = \text{"rabbit"}$
- **Required output:** $3$
- **Multi-Branching Instance:** $s = \text{"babgbag"}$, $t = \text{"bag"} \implies 5$

This instance demonstrates formulating substring match decisions (ignoring $s[i-1]$ vs pairing $s[i-1]$ with $t[j-1]$), establishing the sum recurrence $DP[i][j] = DP[i-1][j] + (s[i-1] == t[j-1] \ ? \ DP[i-1][j-1] : 0)$, constructing the 2D state matrix, and compressing to a 1D backward array in $O(|t|)$ space.

---

## 1. Instance & Teaching Goal

Given two strings $s = \text{"rabbbit"}$ and $t = \text{"rabbit"}$, return the number of distinct subsequences of $s$ which equal $t$.

A subsequence of a string is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.

In $s = \text{"rabbbit"}$ ($|s| = 7$) and $t = \text{"rabbit"}$ ($|t| = 6$):
- Character `'b'` appears $3$ times in $s$ (indices $2, 3, 4$), but only $2$ times in $t$.
- We can form $t$ by choosing any $2$ of the $3$ `'b'`s:
  1. Drop the 3rd `'b'` (index 4): $\text{ra} \mathbf{bb} \text{it} \implies \text{"rabbit"}$
  2. Drop the 2nd `'b'` (index 3): $\text{ra} \mathbf{b} \_ \mathbf{b} \text{it} \implies \text{"rabbit"}$
  3. Drop the 1st `'b'` (index 2): $\text{ra} \_ \mathbf{bb} \text{it} \implies \text{"rabbit"}$
Total ways: $\binom{3}{2} = 3$.

A naive recursive search branches on every duplicate character, causing exponential $O(2^{|s|})$ explosion.
Dynamic programming evaluates prefix matches $(i, j)$ in topological order, running in $O(|s| \cdot |t|)$ time.

---

## 2. Conceptual Foundation & Invariants

### 2D DP State Recurrence
Let $M = |s|$ and $N = |t|$.
Let $DP[i][j]$ be the number of distinct subsequences of $s[0 \dots i-1]$ that equal $t[0 \dots j-1]$.

1. **Base Cases:**
   - $DP[i][0] = 1$ for all $0 \le i \le M$:
     An empty target string $t = \text{""}$ can always be formed by deleting all characters in $s$ (exactly $1$ empty subsequence).
   - $DP[0][j] = 0$ for all $1 \le j \le N$:
     A non-empty target $t$ cannot be formed from an empty source $s$.
2. **Transition Rules ($i \in [1, M], j \in [1, N]$):**
   - **Always Available Option (Skip $s[i-1]$):**
     We can always choose to ignore character $s[i-1]$, keeping all solutions formed from earlier characters:
     $$
     DP[i][j] = DP[i-1][j]
     $$
   - **Matching Option (Use $s[i-1]$ to match $t[j-1]$):**
     If $s[i-1] == t[j-1]$, we can additionally pair $s[i-1]$ with $t[j-1]$. The number of ways to complete the preceding prefix $t[0 \dots j-2]$ is $DP[i-1][j-1]$:
     $$
     DP[i][j] = DP[i-1][j] + DP[i-1][j-1]
     $$

### 1D Space Compression
Maintain a 1D array `dp` of size $N + 1$, initialized with `dp[0] = 1` and `dp[1...N] = 0`.
For each character $c$ in $s$:
Iterate $j$ **backwards** from $N$ down to $1$:
$$
\text{if } c == t[j - 1]: \quad dp[j] \leftarrow dp[j] + dp[j - 1]
$$
Iterating backwards ensures $dp[j - 1]$ reflects the state before character $c$ was introduced.

> **Invariant.** Entry $DP[i][j]$ stores the exact count of unique index tuples $0 \le k_1 < k_2 < \dots < k_j < i$ such that $s[k_r] = t[r-1]$ for all $1 \le r \le j$.

---

## 3. Step-by-Step Worked Execution

We trace the 1D rolling array on $s = \text{"rabbbit"}$ and $t = \text{"rabbit"}$ ($N = 6$):

### Initial State
Target characters: $t = [\,\text{'r'}, \, \text{'a'}, \, \text{'b'}, \, \text{'b'}, \, \text{'i'}, \, \text{'t'}\,]$.
`dp = [1, 0, 0, 0, 0, 0, 0]` (indices $0 \dots 6$).

---

### Process $s[0] = \text{'r'}$
- Matches $t[0]$ ($j = 1$):
  $$
  dp[1] \leftarrow dp[1] + dp[0] = 0 + 1 = 1
  $$
- `dp = [1, 1, 0, 0, 0, 0, 0]`

---

### Process $s[1] = \text{'a'}$
- Matches $t[1]$ ($j = 2$):
  $$
  dp[2] \leftarrow dp[2] + dp[1] = 0 + 1 = 1
  $$
- `dp = [1, 1, 1, 0, 0, 0, 0]`

---

### Process $s[2] = \text{'b'}$ (First 'b' in $s$)
- Matches $t[3]$ ($j = 4$, second 'b' in $t$): $dp[4] += dp[3] = 0 + 0 = 0$.
- Matches $t[2]$ ($j = 3$, first 'b' in $t$):
  $$
  dp[3] \leftarrow dp[3] + dp[2] = 0 + 1 = 1
  $$
- `dp = [1, 1, 1, 1, 0, 0, 0]`

---

### Process $s[3] = \text{'b'}$ (Second 'b' in $s$)
- Matches $t[3]$ ($j = 4$):
  $$
  dp[4] \leftarrow dp[4] + dp[3] = 0 + 1 = 1
  $$
- Matches $t[2]$ ($j = 3$):
  $$
  dp[3] \leftarrow dp[3] + dp[2] = 1 + 1 = 2
  $$
- `dp = [1, 1, 1, 2, 1, 0, 0]`

---

### Process $s[4] = \text{'b'}$ (Third 'b' in $s$)
- Matches $t[3]$ ($j = 4$):
  $$
  dp[4] \leftarrow dp[4] + dp[3] = 1 + 2 = \mathbf{3}
  $$
- Matches $t[2]$ ($j = 3$):
  $$
  dp[3] \leftarrow dp[3] + dp[2] = 2 + 1 = 3
  $$
- `dp = [1, 1, 1, 3, 3, 0, 0]`

---

### Process $s[5] = \text{'i'}$
- Matches $t[4]$ ($j = 5$):
  $$
  dp[5] \leftarrow dp[5] + dp[4] = 0 + 3 = 3
  $$
- `dp = [1, 1, 1, 3, 3, 3, 0]`

---

### Process $s[6] = \text{'t'}$
- Matches $t[5]$ ($j = 6$):
  $$
  dp[6] \leftarrow dp[6] + dp[5] = 0 + 3 = \mathbf{3}
  $$
- `dp = [1, 1, 1, 3, 3, 3, 3]`

Termination. The answer is $dp[6] = \mathbf{3}$.

---

## 4. Complete Execution Trace

### 2D Matrix Evolution ($DP[i][j]$)

Columns represent prefixes of $t = \text{"rabbit"}$ ($j = 0 \dots 6$), Rows represent prefixes of $s = \text{"rabbbit"}$ ($i = 0 \dots 7$):

| $s \backslash t$ | $\emptyset$ | `'r'` | `'a'` | `'b'` | `'b'` | `'i'` | `'t'` |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $\emptyset$ | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| `'r'` | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| `'a'` | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| `'b'` | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| `'b'` | 1 | 1 | 1 | 2 | 1 | 0 | 0 |
| `'b'` | 1 | 1 | 1 | 3 | **3** | 0 | 0 |
| `'i'` | 1 | 1 | 1 | 3 | 3 | **3** | 0 |
| `'t'` | 1 | 1 | 1 | 3 | 3 | 3 | **3 (Result)** |

---

## 5. Algorithmic Correctness

**Soundness.** Subsequences of $s[0 \dots i-1]$ matching $t[0 \dots j-1]$ partition into two mutually exclusive sets: those that do not use $s[i-1]$ (counted by $DP[i-1][j]$) and those that do use $s[i-1]$ (valid only when $s[i-1] == t[j-1]$, counted by $DP[i-1][j-1]$). Summing these disjoint counts guarantees no double counting.

**Completeness.** Computing entries in topological order ensures that all combinations of character deletions are accounted for. The base cases accurately initialize empty string matching.

---

## 6. Traps This Instance Exposes

- **Forward Iteration Collision in 1D DP:** When using a 1D array, iterating $j$ forwards from $1 \dots N$ causes $dp[j]$ to use the updated value of $dp[j-1]$ from the *current* character, equivalent to allowing a single character in $s$ to match multiple characters in $t$! Iterating $j$ strictly backwards ($N$ down to $1$) prevents this corruption.
- **Base Column Invariant:** $DP[i][0]$ must remain $1$ for all $i$, because there is always exactly one way to form an empty target (by deleting all characters of $s$).
- **Length Filtering:** If $|s| < |t|$, a subsequence is impossible; return $0$ immediately.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M \cdot N)$, where $M = |s|$ and $N = |t|$. The nested loop performs $M \times N$ constant-time addition operations.
- **Auxiliary Space Complexity:** $O(N)$ using the backward 1D rolling array (or $O(M \cdot N)$ for the full 2D matrix).