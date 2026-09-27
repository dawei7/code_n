# Guided Example: Length of Longest Fibonacci Subsequence

We trace the step-by-step pair-state dynamic programming formulation, hash table index lookups, transition recurrence $dp[i][j] = dp[j][k] + 1$, and longest sequence extraction on representative strictly increasing integer arrays:

- **Input:**
  $$
  arr = [1, 2, 3, 4, 5, 6, 7, 8]
  $$
- **Required output:** `5`
  - Fibonacci-like subsequence rules:
    - A sequence $x_1, x_2, \dots, x_m$ with $m \ge 3$ is Fibonacci-like if:
      $$
      x_{p} + x_{p+1} = x_{p+2} \quad \text{for all } 1 \le p \le m - 2
      $$
    - The elements must form a subsequence of $arr$ (preserving relative order).
    - Objective: Find the maximum length of such a subsequence, or $0$ if no valid sequence of length $\ge 3$ exists.
    - For $arr = [1, 2, 3, 4, 5, 6, 7, 8]$:
      - Valid sequence: $[1, 2, 3, 5, 8]$:
        - $1 + 2 = 3$
        - $2 + 3 = 5$
        - $3 + 5 = 8$
        - Length is $5$.
      - Other sequences: $[1, 3, 4, 7]$ (len 4), $[2, 3, 5, 8]$ (len 4), $[2, 4, 6]$ (len 3).
      - Longest length: **`5`**.
- **The Pair-State Dynamic Programming Invariant:**
  - **The Two-Term Determinism Property:**
    - A single number does not determine a Fibonacci sequence; the recurrence requires the **two previous numbers** ($x_{m-1}$ and $x_{m-2}$).
    - Therefore, the state cannot be indexed by a single element $i$.
    - We index the state by the **ordered pair of its last two elements**: $(arr[j], arr[i])$ where $j < i$.
  - **Predecessor Inversion:**
    - If a Fibonacci-like subsequence ends with $(\dots, arr[k], arr[j], arr[i])$, then by definition:
      $$
      arr[k] + arr[j] = arr[i] \iff arr[k] = arr[i] - arr[j]
      $$
    - Because $arr$ is strictly increasing, $arr[k]$ (if it exists) must satisfy $arr[k] < arr[j]$, which implies index $k < j$.
    - Using a hash map $d[\text{val}] \to \text{index}$, we look up $k = d[arr[i] - arr[j]]$ in $\mathcal{O}(1)$ time.
    - If $k$ exists and $k < j$:
      $$
      dp[i][j] = dp[j][k] + 1
      $$
    - If no such $k < j$ exists, any pair $(arr[j], arr[i])$ has base length $2$.

---

## 1. Instance & Teaching Goal

Given $arr = [1, 2, 3, 4, 5, 6, 7, 8]$, track how the DP matrix discovers and extends the 5-element sequence ending at $(5, 8)$.

```text
Array: [1, 2, 3, 4, 5, 6, 7, 8]
Indices:0  1  2  3  4  5  6  7

Tracing the optimal sequence:
Pair (1, 2) at indices (0, 1): base length = 2
Pair (2, 3) at indices (1, 2): predecessor 3 - 2 = 1 (idx 0). dp[2][1] = dp[1][0] + 1 = 3  [1, 2, 3]
Pair (3, 5) at indices (2, 4): predecessor 5 - 3 = 2 (idx 1). dp[4][2] = dp[2][1] + 1 = 4  [1, 2, 3, 5]
Pair (5, 8) at indices (4, 7): predecessor 8 - 5 = 3 (idx 2). dp[7][4] = dp[4][2] + 1 = 5  [1, 2, 3, 5, 8]

Maximum length = 5
```

The teaching goal is to justify why expanding the state space from $N$ to $N^2$ captures optimal substructure for multi-step recurrences.

---

## 2. Conceptual Foundation & Invariants

### 1. State Space:
Let $dp[i][j]$ be the length of the longest Fibonacci-like subsequence whose final two elements are $arr[j]$ and $arr[i]$ (with $0 \le j < i < n$).
Base state:
$$
dp[i][j] = 2 \quad \forall 0 \le j < i < n
$$

### 2. State Transition:
For each pair $(j, i)$ with $j < i$:
Let $\Delta = arr[i] - arr[j]$.
$$
\text{If } \Delta \in arr \land \text{index}(\Delta) < j:
$$
$$
k = \text{index}(\Delta)
$$
$$
dp[i][j] = \max(dp[i][j], dp[j][k] + 1)
$$
$$
ans = \max(ans, dp[i][j])
$$

### 3. Threshold Guard:
Because a valid Fibonacci-like subsequence must have length at least $3$:
$$
\text{Final Answer} = \begin{cases}
ans & \text{if } ans \ge 3 \\
0 & \text{if } ans < 3
\end{cases}
$$

---

## 3. Step-by-Step Worked Execution

We trace $arr = [1, 2, 3, 4, 5, 6, 7, 8]$:
Hash map: $\{1:0, 2:1, 3:2, 4:3, 5:4, 6:5, 7:6, 8:7\}$.
Initialize $dp[i][j] = 2$ for all pairs. $ans = 0$.

---

### Step 1: Evaluating $i = 2$ ($arr[2] = 3$)
- $j = 1$ ($arr[1] = 2$):
  - Predecessor $\Delta = 3 - 2 = 1$.
  - Index of $1$ is $k = 0 < j = 1$.
  - Transition:
    $$
    dp[2][1] = dp[1][0] + 1 = 2 + 1 = \mathbf{3}
    $$
  - Subsequence: $[1, 2, 3]$. Update $ans = \max(0, 3) = \mathbf{3}$.

---

### Step 2: Evaluating $i = 4$ ($arr[4] = 5$)
- $j = 2$ ($arr[2] = 3$):
  - Predecessor $\Delta = 5 - 3 = 2$.
  - Index of $2$ is $k = 1 < j = 2$.
  - Transition:
    $$
    dp[4][2] = dp[2][1] + 1 = 3 + 1 = \mathbf{4}
    $$
  - Subsequence: $[1, 2, 3, 5]$. Update $ans = \max(3, 4) = \mathbf{4}$.
- $j = 3$ ($arr[3] = 4$):
  - Predecessor $\Delta = 5 - 4 = 1$.
  - Index of $1$ is $k = 0 < 3$.
  - Transition: $dp[4][3] = dp[3][0] + 1 = 2 + 1 = 3$.

---

### Step 3: Evaluating $i = 6$ ($arr[6] = 7$)
- $j = 3$ ($arr[3] = 4$):
  - Predecessor $\Delta = 7 - 4 = 3$.
  - Index of $3$ is $k = 2 < 3$.
  - Transition: $dp[6][3] = dp[3][2] + 1 = 3 + 1 = 4$ ($[1, 3, 4, 7]$).

---

### Step 4: Evaluating $i = 7$ ($arr[7] = 8$)
- $j = 4$ ($arr[4] = 5$):
  - Predecessor $\Delta = 8 - 5 = 3$.
  - Index of $3$ is $k = 2 < j = 4$.
  - Transition:
    $$
    dp[7][4] = dp[4][2] + 1 = 4 + 1 = \mathbf{5}
    $$
  - Subsequence: $[1, 2, 3, 5, 8]$.
  - Update: $ans = \max(4, 5) = \mathbf{5}$.

---

### Termination:
All pairs evaluated. Maximum sequence length found:
$$
ans = \mathbf{5}
$$

---

## 4. Complete Execution Trace

| End Index $i$ | Prev Index $j$ | End Value $arr[i]$ | Prev Value $arr[j]$ | Predecessor $\Delta = arr[i] - arr[j]$ | Predecessor Index $k$ | Valid ($k < j$)? | Prior Length $dp[j][k]$ | New Length $dp[i][j]$ | Running Max $ans$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $2$ | $1$ | $3$ | $2$ | $1$ | $0$ | Yes | $2$ | $3$ | $3$ |
| $3$ | $2$ | $4$ | $3$ | $1$ | $0$ | Yes | $2$ | $3$ | $3$ |
| $4$ | $2$ | $5$ | $3$ | $2$ | $1$ | Yes | $3$ | **$4$** | $4$ |
| $4$ | $3$ | $5$ | $4$ | $1$ | $0$ | Yes | $2$ | $3$ | $4$ |
| $5$ | $3$ | $6$ | $4$ | $2$ | $1$ | Yes | $2$ | $3$ | $4$ |
| $6$ | $3$ | $7$ | $4$ | $3$ | $2$ | Yes | $3$ | **$4$** | $4$ |
| **$7$** | **$4$** | **$8$** | **$5$** | **$3$** | **$2$** | **Yes** | **$4$** | **`5`** | **`5`** |

---

## 5. Boundary Cases & Failure Modes

- **No Valid Triplet (e.g. $[1, 2, 4, 8]$):** All differences fail to produce a previous element $\implies ans$ remains $0 \implies$ returns $0$.
- **Short Array ($N < 3$):** Impossible to have a Fibonacci sequence of length $\ge 3 \implies$ returns $0$.
- **Predecessor Exceeds $arr[j]$ ($k \ge j$):** Condition $k < j$ prevents cyclic or inverted ordering.

---

## 6. Traps & Common Anti-Patterns

- **1D Dynamic Programming ($DP[i]$):** A single state $DP[i]$ cannot determine which specific predecessor created the sequence, leading to false transitions and incorrect chains.
- **Linear Search for Predecessor:** Scanning linearly for $arr[k]$ takes $\mathcal{O}(N)$ per pair, degrading total time to $\mathcal{O}(N^3)$. Precomputing a hash map or two pointers reduces lookup to $\mathcal{O}(1)$, achieving $\mathcal{O}(N^2)$ overall time.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Hash map construction: $\mathcal{O}(N)$.
  - Nested loops over all pairs $(i, j)$ with $j < i$: $\frac{N(N - 1)}{2} = \mathcal{O}(N^2)$ pairs.
  - Predecessor lookup and transition: $\mathcal{O}(1)$ per pair.
  - Total Time: strictly $\mathcal{O}(N^2)$, completing in $< 120$ ms for $N = 1000$.
- **Auxiliary Space Complexity:**
  - 2D DP matrix of dimension $N \times N$: $\mathcal{O}(N^2)$ space (or $\mathcal{O}(N^2)$ sparse hash table).