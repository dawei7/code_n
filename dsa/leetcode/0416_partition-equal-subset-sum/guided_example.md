# Guided Example: Partition Equal Subset Sum

We trace the step-by-step reduction to 0/1 knapsack subset-sum, parity feasibility gating, reverse-order 1D boolean state transitions ($DP[j] \leftarrow DP[j] \lor DP[j - x]$), and subset reconstruction on representative numerical arrays:

- **Input:** $nums = [1, 5, 11, 5]$
- **Required output:** `true`
  - Total array sum: $\sum nums = 1 + 5 + 11 + 5 = 22$
  - Parity check: $22 \bmod 2 = 0$ (Even $\implies$ Feasible target exists)
  - Target subset sum: $T = 22 / 2 = \mathbf{11}$
  - Step 1 (Element $x_1 = 1$):
    - Reachable sums: $\{0, 1\}$
  - Step 2 (Element $x_2 = 5$):
    - Reachable sums: $\{0, 1\} \cup \{5, 6\} = \{0, 1, 5, 6\}$
  - Step 3 (Element $x_3 = 11$):
    - New reachable sum: $0 + 11 = 11$
    - Target $T = 11$ achieved: subset $\{11\}$ has sum $11$, remaining $\{1, 5, 5\}$ has sum $11$
    - State $DP[11] \leftarrow \text{True}$
  - Step 4 (Element $x_4 = 5$):
    - Additional way to form $11$: $\{1, 5, 5\}$
  - Terminal check: $DP[11] == \text{True} \implies$ Return `true`
- **Odd Total Sum:** $nums = [1, 2, 3, 5] \implies \sum = 11$ (Odd $\implies 11 \bmod 2 \ne 0$) $\implies$ Return `false`
- **Dominant Element:** $nums = [1, 2, 9] \implies \sum = 12, T = 6$. Since $\max(nums) = 9 > 6$, no subset can balance $9 \implies$ Return `false`

This instance demonstrates reducing set bi-partitioning to the pseudo-polynomial 0/1 knapsack decision problem, mathematically proves why iterating backward in 1D prevents item reuse, and derives $O(N \cdot T)$ runtime and $O(T)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $nums = [1, 5, 11, 5]$:
Determine whether the array can be partitioned into two disjoint subsets $S_1$ and $S_2$ such that the sum of elements in both subsets is equal:
$$
S_1 \cup S_2 = nums, \quad S_1 \cap S_2 = \emptyset, \quad \sum_{x \in S_1} x = \sum_{y \in S_2} y
$$

```text
Array: [1,  5,  11,  5]   (Total Sum = 22)

Equal Partition:
  Subset 1: { 11 }        -> Sum = 11
  Subset 2: { 1, 5, 5 }   -> Sum = 1 + 5 + 5 = 11

Sum(Subset 1) == Sum(Subset 2) == 11 -> Partition Possible -> true
```

### The Reduction to 0/1 Knapsack
Let $S = \sum nums$. If two subsets have equal sum, each subset must sum to exactly:
$$
T = \frac{S}{2}
$$
1. If $S$ is odd ($S \bmod 2 \ne 0$), dividing $S$ into two equal integers is impossible. Return `false` immediately.
2. If any individual element $x > T$, placing $x$ in either subset forces its sum $> T$. Return `false` immediately.
3. Otherwise, the problem is equivalent to: **"Does there exist any subset of $nums$ whose elements sum to exactly $T$?"**

---

## 2. Conceptual Foundation & Invariants

### 1. Dynamic Programming State Definition:
Let $DP[j]$ be a boolean flag indicating whether a subset with sum $j$ can be formed using a subset of the elements processed so far ($0 \le j \le T$).
- **Base Case:** $DP[0] = \text{True}$ (an empty subset achieves sum 0). All other $DP[j] = \text{False}$ for $j \in [1, T]$.

### 2. Recurrence Relation for Element $x$:
For an element $x$, a sum $j$ can be achieved if:
- It was already achievable without $x$: $DP[j]$ was already `True`.
- It can be formed by adding $x$ to an existing sum $j - x$: $DP[j - x]$ was `True` ($j \ge x$).
$$
DP[j] \leftarrow DP[j] \lor DP[j - x] \quad \text{for } j = T, T-1, \dots, x
$$

### 3. The Reverse-Iteration Rule:
We must iterate $j$ from $T$ **downward to $x$**:
- In a 0/1 knapsack, each element can be chosen **at most once**.
- If we iterated $j$ forward ($x \dots T$), setting $DP[x] = \text{True}$ from $DP[0]$ would immediately allow $DP[2x]$ to read the updated $DP[x]$ within the same step, effectively reusing element $x$ multiple times (unbounded knapsack).
- Backward iteration ensures that $DP[j - x]$ represents the state from the *previous* element iteration.

> **Invariant.** After processing the first $i$ elements, $DP[j] == \text{True}$ if and only if some subset of the prefix $\{nums[0], \dots, nums[i-1]\}$ sums to exactly $j$.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [1, 5, 11, 5]$ with target $T = 22 / 2 = 11$:
Initialize array of size $T + 1 = 12$:
$$
DP = [\mathbf{T}, F, F, F, F, F, F, F, F, F, F, F] \quad (\text{Indices } 0 \dots 11)
$$

---

### Step 1: Process $x_1 = 1$
Loop $j$ from $11$ down to $1$:
- For $j = 1$: $DP[1] \leftarrow DP[1] \lor DP[0] = F \lor T = \mathbf{T}$.
- All other $j > 1$ have $DP[j - 1] = F$.
$$
DP = [T, \mathbf{T}, F, F, F, F, F, F, F, F, F, F]
$$
Reachable sums: $\{0, 1\}$.

---

### Step 2: Process $x_2 = 5$
Loop $j$ from $11$ down to $5$:
- $j = 6$: $DP[6] \leftarrow DP[6] \lor DP[6 - 5] = DP[6] \lor DP[1] = F \lor T = \mathbf{T}$.
- $j = 5$: $DP[5] \leftarrow DP[5] \lor DP[5 - 5] = DP[5] \lor DP[0] = F \lor T = \mathbf{T}$.
$$
DP = [T, T, F, F, F, \mathbf{T}, \mathbf{T}, F, F, F, F, F]
$$
Reachable sums: $\{0, 1, 5, 6\}$.

---

### Step 3: Process $x_3 = 11$
Loop $j$ from $11$ down to $11$:
- $j = 11$:
  $$
  DP[11] \leftarrow DP[11] \lor DP[11 - 11] = DP[11] \lor DP[0] = F \lor T = \mathbf{T}
  $$
$$
DP = [T, T, F, F, F, T, T, F, F, F, F, \mathbf{T}]
$$
Reachable sums: $\{0, 1, 5, 6, 11\}$.
Notice that $DP[11]$ is now `True`. Target $T = 11$ is already reached!

---

### Step 4: Process $x_4 = 5$
Loop $j$ from $11$ down to $5$:
- $j = 11$: $DP[11] \leftarrow DP[11] \lor DP[11 - 5] = DP[11] \lor DP[6] = T \lor T = \mathbf{T}$.
  *(Confirms alternative subset $\{1, 5, 5\}$ sums to $11$.)*
- $j = 10$: $DP[10] \leftarrow DP[10] \lor DP[5] = F \lor T = \mathbf{T}$.
$$
DP = [T, T, F, F, F, T, T, F, F, F, \mathbf{T}, \mathbf{T}]
$$
Final evaluation: $DP[11] == \mathbf{True}$.

---

## 4. Complete Execution Trace

| Step | Element $x$ | Loop Range $j = 11 \dots x$ | Active Transitions $DP[j - x] == \text{True}$ | Newly Reached Sums $j$ | Complete Set of Reachable Sums | Target Reached ($DP[11]$)? |
|:---:|:---:|:---:|:---|:---:|:---|:---:|
| **Init** | — | — | Base case $DP[0] = T$ | $\{0\}$ | $\{0\}$ | False |
| **1** | $1$ | $11 \dots 1$ | $j = 1 \ (DP[0])$ | $\{1\}$ | $\{0, 1\}$ | False |
| **2** | $5$ | $11 \dots 5$ | $j = 6 \ (DP[1]), \; j = 5 \ (DP[0])$ | $\{5, 6\}$ | $\{0, 1, 5, 6\}$ | False |
| **3** | **$11$** | $11 \dots 11$ | **$j = 11 \ (DP[0])$** | **$\{11\}$** | $\{0, 1, 5, 6, 11\}$ | **True** |
| **4** | $5$ | $11 \dots 5$ | $j = 11 \ (DP[6]), \; j = 10 \ (DP[5])$ | $\{10, 11\}$ | $\{0, 1, 5, 6, 10, 11\}$ | **True** |

---

## 5. Boundary Cases & Failure Modes

- **Odd Total Sum ($nums = [1, 2, 5]$):** Sum is $8$ (even, $T=4$), but $nums = [1, 2, 3, 5] \implies \sum = 11$ (odd). Parity test $11 \bmod 2 = 1$ returns `false` without computing DP table.
- **Single Element Array ($nums = [2]$):** Length is $< 2$. Cannot partition into two non-empty subsets.
- **Identical Pair ($nums = [3, 3]$):** $\sum = 6, T = 3$. Element 1 sets $DP[3] = \text{True}$, returns `true`.
- **Target Sum Exceeded by Single Element ($nums = [1, 2, 20]$):** $\sum = 23$ is odd. If $nums = [1, 1, 10] \implies \sum = 12, T = 6$. Element $10 > 6$ cannot be placed in either half without exceeding $6$.

---

## 6. Traps & Common Anti-Patterns

- **Forward DP Iteration:** Writing `for j in range(x, target + 1)` allows an element to be added to itself repeatedly. For example, with $nums = [2]$ and target $4$, forward iteration sets $DP[2]=T$, then uses $DP[2]$ to set $DP[4]=T$, falsely declaring that a single $2$ can sum to $4$. Backward iteration strictly enforces the 0/1 knapsack constraint.
- **Omission of Parity Gate:** Failing to check `sum % 2 == 0` causes floating point target values ($T = 5.5$) or integer division truncation ($11 // 2 = 5$) that produces incorrect positive matches.
- **Full 2D Matrix Memory Allocation:** Using an $N \times T$ 2D matrix consumes $O(N \cdot T)$ auxiliary memory. Rolling backward in a 1D array of size $T+1$ reduces memory to $O(T)$ with zero performance penalty.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $N$ be the number of elements and $T = \frac{1}{2} \sum nums$.
  - Outer loop runs $N$ times.
  - Inner loop runs at most $T + 1$ times.
  - Total Time: $\mathcal{O}(N \cdot T)$ pseudo-polynomial time. For $N \le 200$ and $nums[i] \le 100$, $T \le 10000$, resulting in at most $2 \times 10^6$ operations (executes in $\approx 20$ ms).
- **Auxiliary Space Complexity:**
  - The 1D boolean table requires $T + 1$ entries.
  - Total Auxiliary Space: $\mathcal{O}(T) = \mathcal{O}(\sum nums)$.
