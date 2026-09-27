# Guided Example: Target Sum

We trace the step-by-step algebraic partition reduction ($\sum P - \sum N = target \implies \sum N = (S - target) / 2$), parity feasibility validation ($(S - target) \pmod 2 == 0$), 0-1 Knapsack subset-sum DP table construction ($f[j] += f[j - x]$), zero-element multiplicity handling, and combination counting on representative signed arrays:

- **Input:** $nums = [1, 1, 1, 1, 1], \quad target = 3$
- **Required output:** `5`
  - Array sum:
    $$
    S = 1 + 1 + 1 + 1 + 1 = 5
    $$
  - Feasibility checks:
    - $S \ge target \implies 5 \ge 3$ (Pass)
    - Parity check: $(S - target) \pmod 2 = (5 - 3) \pmod 2 = 2 \pmod 2 = 0$ (Pass)
  - **Algebraic Reduction to 0-1 Subset Sum:**
    - Let $P$ be elements assigned `+`, and $N$ be elements assigned `-`:
      $$
      \begin{aligned}
      \text{Sum}(P) - \text{Sum}(N) &= target = 3 \\
      \text{Sum}(P) + \text{Sum}(N) &= S = 5
      \end{aligned}
      $$
    - Subtracting the top from the bottom:
      $$
      2 \times \text{Sum}(N) = S - target = 5 - 3 = 2 \implies \text{Sum}(N) = \mathbf{1}
      $$
    - The problem is equivalent to: **Find the number of subsets of $nums$ whose sum equals $1$**.
  - **Dynamic Programming Trace for Target Sum $1$:**
    - Initialize table $f[0 \dots 1] = [1, 0]$ (1 way to form sum 0: empty subset $\emptyset$)
    - **Item 1 ($x = 1$):**
      - $f[1] \leftarrow f[1] + f[0] = 0 + 1 = \mathbf{1}$. State: $[1, 1]$.
    - **Item 2 ($x = 1$):**
      - $f[1] \leftarrow f[1] + f[0] = 1 + 1 = \mathbf{2}$. State: $[1, 2]$.
    - **Item 3 ($x = 1$):**
      - $f[1] \leftarrow f[1] + f[0] = 2 + 1 = \mathbf{3}$. State: $[1, 3]$.
    - **Item 4 ($x = 1$):**
      - $f[1] \leftarrow f[1] + f[0] = 3 + 1 = \mathbf{4}$. State: $[1, 4]$.
    - **Item 5 ($x = 1$):**
      - $f[1] \leftarrow f[1] + f[0] = 4 + 1 = \mathbf{5}$. State: $[1, 5]$.
  - Number of ways to choose elements that sum to $1$ is $\mathbf{5}$.
  - The 5 corresponding sign configurations:
    1. $-1 + 1 + 1 + 1 + 1 = 3$
    2. $+1 - 1 + 1 + 1 + 1 = 3$
    3. $+1 + 1 - 1 + 1 + 1 = 3$
    4. $+1 + 1 + 1 - 1 + 1 = 3$
    5. $+1 + 1 + 1 + 1 - 1 = 3$
  - Result: **`5`**.
- **Impossible Parity Instance ($nums = [1, 2], target = 2$):**
  - $S = 3$. $S - target = 3 - 2 = 1$ (Odd!).
  - $(S - target) \pmod 2 \ne 0 \implies$ No assignment can equal $2 \implies \mathbf{0}$
- **Target Exceeds Sum ($nums = [1, 2], target = 5$):**
  - Maximum possible sum is $3 < 5 \implies \mathbf{0}$
- **Zero Values Present ($nums = [0, 0, 1], target = 1$):**
  - Each zero doubles the number of valid sign assignments ($+0$ vs $-0$) $\implies 2^2 \times 1 = \mathbf{4}$

This instance demonstrates linear algebraic reduction of sign assignment games to canonical knapsack counting, mathematically proves why parity mismatch forbids any solution, and derives $O(N \cdot \text{target})$ runtime and $O(\text{target})$ space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $nums = [1, 1, 1, 1, 1]$ and an integer $target = 3$:
Build an expression by adding either a `'+'` or `'-'` before each integer in $nums$.
Return the **number of different expressions** that evaluate to $target$.

```text
Input: nums = [1, 1, 1, 1, 1], target = 3

Sign Configurations:
  -1 + 1 + 1 + 1 + 1 = 3
  +1 - 1 + 1 + 1 + 1 = 3
  +1 + 1 - 1 + 1 + 1 = 3
  +1 + 1 + 1 - 1 + 1 = 3
  +1 + 1 + 1 + 1 - 1 = 3

Total Valid Expressions = 5
```

### The Algebraic Reduction
Instead of exploring a branching tree of $2^N$ signs:
Partition $nums$ into two disjoint subsets:
- $P$: elements given a positive sign (`+`)
- $N$: elements given a negative sign (`-`)

We must satisfy two simultaneous equations:
$$
\sum(P) - \sum(N) = target
$$
$$
\sum(P) + \sum(N) = \sum(nums) = S
$$
Subtracting the top equation from the bottom:
$$
2 \sum(N) = S - target \implies \sum(N) = \frac{S - target}{2}
$$
This transforms the problem into a classic **0-1 Knapsack Subset Sum Problem**:
Count the number of subsets of $nums$ whose elements sum to exactly $K = \frac{S - target}{2}$.

---

## 2. Conceptual Foundation & Invariants

### 1. Necessary Feasibility Filters:
1. **Magnitude Bound:** $S \ge |target|$. If the sum of all absolute numbers cannot reach $target$, no configuration exists $\implies$ Return $0$.
2. **Parity Match:** $S - target$ must be non-negative and **even**:
   $$
   (S - target) \pmod 2 == 0
   $$
   If $S - target$ is odd, dividing by 2 yields a fraction, but all elements in $nums$ are integers $\implies$ Return $0$.

### 2. Subset Sum DP Recurrence:
Let $f[j]$ be the number of subsets from the processed prefix of $nums$ that sum to $j$:
- Base case: $f[0] = 1$ (the empty subset sums to 0).
- For each number $x \in nums$:
  Iterate capacity $j$ **in reverse** from $K$ down to $x$:
  $$
  f[j] \leftarrow f[j] + f[j - x]
  $$
- Answer: $f[K]$.

> **Reverse Iteration Invariant.** Traversing $j$ downwards from $K$ to $x$ ensures that each element $x$ is included in any subset at most once (0-1 knapsack invariant).

---

## 3. Step-by-Step Worked Execution

We trace $nums = [1, 1, 1, 1, 1]$ with $target = 3$:

---

### Step 1: Compute Parameters & Feasibility
- Total sum: $S = 5$.
- Check $S \ge target \iff 5 \ge 3$ (Pass).
- Check parity: $(5 - 3) \pmod 2 = 2 \pmod 2 = 0$ (Pass).
- Target subset sum:
  $$
  K = \frac{5 - 3}{2} = \mathbf{1}
  $$

---

### Step 2: Initialize Table
- Array $f$ of size $K + 1 = 2$:
  $$
  f = [1, \; 0]
  $$
  ($f[0] = 1$: 1 way to make sum 0; $f[1] = 0$: 0 ways to make sum 1).

---

### Step 3: Sequential Item Processing
For each $x = 1$ (repeated 5 times):
We update in reverse: $j = 1 \dots 1$:
$$
f[1] \leftarrow f[1] + f[1 - 1] = f[1] + f[0]
$$

- **Item 1 ($x = 1$):** $f[1] \leftarrow 0 + 1 = \mathbf{1}$. Table: $[1, 1]$.
- **Item 2 ($x = 1$):** $f[1] \leftarrow 1 + 1 = \mathbf{2}$. Table: $[1, 2]$.
- **Item 3 ($x = 1$):** $f[1] \leftarrow 2 + 1 = \mathbf{3}$. Table: $[1, 3]$.
- **Item 4 ($x = 1$):** $f[1] \leftarrow 3 + 1 = \mathbf{4}$. Table: $[1, 4]$.
- **Item 5 ($x = 1$):** $f[1] \leftarrow 4 + 1 = \mathbf{5}$. Table: $[1, 5]$.

---

### Step 4: Final Count
The number of ways to form subset sum $K = 1$ is:
$$
f[1] = \mathbf{5}
$$

---

## 4. Complete Execution Trace

| Processing Step | Element $x$ | Capacity $j$ Target | Transition: $f[j] \leftarrow f[j] + f[j-x]$ | Table State $f[0 \dots 1]$ | Valid Subsets Represented |
|:---:|:---:|:---:|:---:|:---:|:---|
| **Init** | — | — | — | `[1, 0]` | $\emptyset$ |
| **$1$** | $1$ | $1$ | $f[1] = 0 + 1 = 1$ | `[1, 1]` | $\{idx_0\}$ |
| **$2$** | $1$ | $1$ | $f[1] = 1 + 1 = 2$ | `[1, 2]` | $\{idx_0\}, \{idx_1\}$ |
| **$3$** | $1$ | $1$ | $f[1] = 2 + 1 = 3$ | `[1, 3]` | $\{idx_0\}, \{idx_1\}, \{idx_2\}$ |
| **$4$** | $1$ | $1$ | $f[1] = 3 + 1 = 4$ | `[1, 4]` | 4 singletons |
| **$5$** | $1$ | $1$ | $f[1] = 4 + 1 = \mathbf{5}$ | `[1, 5]` | **5 distinct singletons** |

---

## 5. Boundary Cases & Failure Modes

- **$target$ Exceeds Total Sum ($target = 10, S = 5$):** $S < target \implies \mathbf{0}$.
- **Negative Target ($target = -3, S = 5$):**
  $$
  K = \frac{5 - (-3)}{2} = \frac{8}{2} = 4
  $$
  Subsets summing to 4: $\binom{5}{4} = \mathbf{5}$. Fully symmetric.
- **Zeros in Array ($nums = [0, 0, 0, 1], target = 1$):**
  - For each zero, $f[j] += f[j - 0] = f[j] + f[j] = 2 \cdot f[j]$.
  - Each zero doubles the number of expressions ($+0$ vs $-0$) $\implies 2^3 \times 1 = \mathbf{8}$.

---

## 6. Traps & Common Anti-Patterns

- **Direct Recursive DFS ($O(2^N)$):** A naive branching recursion without memoization explores all $2^{20} \approx 10^6$ combinations on every query. The DP reduction runs in $O(N \cdot \text{target})$ time.
- **Forgetting Parity Check:** Dividing $(S - target)$ by 2 using integer division `//` without checking `(s - target) % 2 == 0` truncates fractional targets, returning false positive counts on impossible configurations.
- **Forward Traversal in 1D DP Array:** Iterating $j$ ascending from $x$ to $K$ allows the same number to be reused multiple times (unbounded knapsack), corrupting counts. Reverse iteration ($K \to x$) is mandatory for 0-1 subset sums.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $N = |nums|$ and $K = \frac{S - target}{2} \le 1000$.
  - The outer loop runs $N$ times.
  - The inner loop iterates $K$ times.
  - Total Time: $\mathcal{O}(N \cdot K)$. For $N \le 20$ and $K \le 1000$, $20 \times 1000 = 2 \times 10^4$ operations, completing in $< 2$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(K)$ space using a 1D DP array of length $K + 1$.