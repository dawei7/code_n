# Guided Example: Ones and Zeroes

We trace the step-by-step two-dimensional 0-1 Knapsack formulation, dual-resource budget tracking ($m$ zeros, $n$ ones), item cost vector extraction ($(a, b)$), reverse capacity table transitions ($f[j][k] = \max(f[j][k], f[j-a][k-b] + 1)$), and maximum subset size maximization on representative binary string inputs:

- **Input:**
  - $strs = [\text{"10"}, \text{"0001"}, \text{"111001"}, \text{"1"}, \text{"0"}]$
  - Zero budget: $m = 5$
  - One budget: $n = 3$
- **Required output:** `4`
  - Item cost decomposition $(zeros, ones)$:
    - Item 1 (`"10"`): cost $(1, 1)$, value $1$
    - Item 2 (`"0001"`): cost $(3, 1)$, value $1$
    - Item 3 (`"111001"`): cost $(2, 4)$, value $1$ (requires 4 ones $> n=3$, impossible!)
    - Item 4 (`"1"`): cost $(0, 1)$, value $1$
    - Item 5 (`"0"`): cost $(1, 0)$, value $1$
  - **Knapsack Selection:**
    - Choose items $\{ \text{"10"}, \text{"0001"}, \text{"1"}, \text{"0"} \}$:
      - Zeros consumed: $1 + 3 + 0 + 1 = \mathbf{5} \le 5$ (Within zero budget $m$)
      - Ones consumed: $1 + 1 + 1 + 0 = \mathbf{3} \le 3$ (Within one budget $n$)
      - Subset cardinality: $1 + 1 + 1 + 1 = \mathbf{4}$
    - Excluded item: `"111001"` (alone requires $4$ ones, exceeding the budget of $3$)
  - Maximum possible subset size: $\mathbf{4}$.
- **Small Budget Instance:** $strs = [\text{"10"}, \text{"0"}, \text{"1"}], m = 1, n = 1$
  - Option A: Pick `{"10"}` $\implies$ cost $(1, 1)$, size $1$
  - Option B: Pick `{"0", "1"}` $\implies$ cost $(1, 0) + (0, 1) = (1, 1)$, size $\mathbf{2}$
  - Optimal size is $\mathbf{2}$.
- **Zero Budget Allocation:** $m = 0, n = 0 \implies \mathbf{0}$ (no string can be chosen)

This instance demonstrates multi-dimensional 0-1 Knapsack optimization, mathematically proves why reverse grid iteration prevents reusing the same item, and derives $O(|strs| \times m \times n)$ runtime and $O(m \times n)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an array of binary strings $strs$ and two budget integers $m$ (maximum zeroes) and $n$ (maximum ones):
Find the **maximum size of a subset** of $strs$ such that the total number of `0`s in the subset is $\le m$ and the total number of `1`s is $\le n$.

```text
Resource Limits:  m = 5 zeroes,  n = 3 ones

Item Costs:
  "10"     -> 1 zero,  1 one
  "0001"   -> 3 zeroes, 1 one
  "111001" -> 2 zeroes, 4 ones (Exceeds n = 3 immediately!)
  "1"      -> 0 zeroes, 1 one
  "0"      -> 1 zero,  0 ones

Optimal Selection: {"10", "0001", "1", "0"}
  Total Zeroes: 1 + 3 + 0 + 1 = 5 <= 5
  Total Ones:   1 + 1 + 1 + 0 = 3 <= 3
Subset Size: 4
```

### The 2D 0-1 Knapsack Analogy
- In standard 0-1 knapsack, each item has a weight $w$ and a value $v$, and there is a single capacity $W$.
- Here, each item has **two simultaneous weights**:
  1. Count of `'0'`s: $a$
  2. Count of `'1'`s: $b$
- Every chosen item contributes **exactly $+1$** to the objective (subset size).
- The knapsack has a **two-dimensional capacity**: $(m, n)$.

---

## 2. Conceptual Foundation & Invariants

### 1. The 2D Dynamic Programming State:
Let $f[j][k]$ represent the maximum number of binary strings that can be selected using at most $j$ zeroes and at most $k$ ones.

### 2. State Transition Formula:
For each string $s \in strs$ with costs $a = \text{count}('0')$ and $b = \text{count}('1')$:
We iterate capacities **in reverse** from $m$ down to $a$ and from $n$ down to $b$:
$$
f[j][k] = \max(f[j][k], \; f[j - a][k - b] + 1)
$$
- If we do not pick string $s$: the capacity remains $f[j][k]$.
- If we pick string $s$: we add $1$ to the optimal subset from residual capacity $f[j - a][k - b]$.

### 3. The Reverse Traversal Invariant:
Iterating $j$ and $k$ in **decreasing order** ($m \to a$, $n \to b$) guarantees that $f[j - a][k - b]$ comes from the **previous** item state, preventing the current string from being selected multiple times (0-1 knapsack property).

> **Capacity Invariant.** At all stages, $f[j][k]$ is the exact maximum number of items chosen from the processed prefix of strings satisfying the joint budget constraints $\sum zeros \le j$ and $\sum ones \le k$.

---

## 3. Step-by-Step Worked Execution

We trace $strs = [\text{"10"}, \text{"0001"}, \text{"111001"}, \text{"1"}, \text{"0"}]$ with $m = 5, n = 3$:
Initialize table $f[0 \dots 5][0 \dots 3] = 0$.

---

### Item 1: `"10"` (Cost: $a = 1, b = 1$)
- Loop $j = 5 \dots 1$, $k = 3 \dots 1$:
  $$
  f[j][k] = \max(0, \; f[j - 1][k - 1] + 1) = \mathbf{1} \quad \forall j \ge 1, k \ge 1
  $$
- Capacity $(5, 3)$ reaches size $1$.

---

### Item 2: `"0001"` (Cost: $a = 3, b = 1$)
- Loop $j = 5 \dots 3$, $k = 3 \dots 1$:
  - At $(j=4, k=2)$: $f[4 - 3][2 - 1] + 1 = f[1][1] + 1 = 1 + 1 = \mathbf{2}$.
  - At $(j=5, k=3)$: $f[5 - 3][3 - 1] + 1 = f[2][2] + 1 = 1 + 1 = \mathbf{2}$.
- Now pairs with $\ge 4$ zeroes and $\ge 2$ ones hold size $2$ (e.g. `{"10", "0001"}`).

---

### Item 3: `"111001"` (Cost: $a = 2, b = 4$)
- Requires $b = 4$ ones.
- Since maximum capacity is $n = 3 < 4$, the condition $k \ge b$ is never met.
- Item 3 is completely skipped; table remains unchanged.

---

### Item 4: `"1"` (Cost: $a = 0, b = 1$)
- Requires $0$ zeroes, $1$ one.
- Loop $j = 5 \dots 0$, $k = 3 \dots 1$:
  - At $(j=4, k=3)$: $f[4 - 0][3 - 1] + 1 = f[4][2] + 1 = 2 + 1 = \mathbf{3}$.
  - At $(j=5, k=3)$: $f[5 - 0][3 - 1] + 1 = f[5][2] + 1 = 2 + 1 = \mathbf{3}$.
- Subsets of size 3 formed: `{"10", "0001", "1"}` (uses 4 zeroes, 3 ones).

---

### Item 5: `"0"` (Cost: $a = 1, b = 0$)
- Requires $1$ zero, $0$ ones.
- Loop $j = 5 \dots 1$, $k = 3 \dots 0$:
  - At $(j=5, k=3)$:
    $$
    f[5 - 1][3 - 0] + 1 = f[4][3] + 1 = 3 + 1 = \mathbf{4}
    $$
- Subsets of size 4 formed: `{"10", "0001", "1", "0"}` (uses 5 zeroes, 3 ones).

---

### Final Result:
Maximum subset size: $f[5][3] = \mathbf{4}$.

---

## 4. Complete Execution Trace

| Item $s$ | Cost $(a, b)$ | Target Budget $(j, k)$ | Residual Lookup $f[j-a][k-b]$ | Transition Value $+1$ | New Optimal $f[5][3]$ | Subset Represented |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **Init** | — | $(5, 3)$ | — | — | $0$ | $\emptyset$ |
| `"10"` | $(1, 1)$ | $(5, 3)$ | $f[4][2] = 0$ | $0 + 1 = 1$ | $1$ | `{"10"}` |
| `"0001"` | $(3, 1)$ | $(5, 3)$ | $f[2][2] = 1$ | $1 + 1 = 2$ | $2$ | `{"10", "0001"}` |
| `"111001"`| $(2, 4)$ | $(5, 3)$ | Exceeds $n=3$ | Skipped | $2$ | Unchanged |
| `"1"` | $(0, 1)$ | $(5, 3)$ | $f[5][2] = 2$ | $2 + 1 = 3$ | $3$ | `{"10", "0001", "1"}` |
| `"0"` | $(1, 0)$ | $(5, 3)$ | $f[4][3] = 3$ | $3 + 1 = 4$ | **$4$** | `{"10", "0001", "1", "0"}` |

---

## 5. Boundary Cases & Failure Modes

- **Zero Budget for Both ($m = 0, n = 0$):** Only empty strings could be accepted $\implies \mathbf{0}$.
- **Only Zeroes Budget ($m = 5, n = 0$):** Can only pick pure zero strings (`"0"`, `"00"`); any string with `'1'` cannot be accommodated.
- **Single Character Options ($strs = [\text{"0"}, \text{"1"}], m=1, n=1$):** Picks both $\implies \mathbf{2}$.
- **All Strings Exceed Budget:** $f[m][n]$ remains $0$.

---

## 6. Traps & Common Anti-Patterns

- **Forward Capacity Loops ($j = 0 \dots m$):** Forward loops allow the same string to be added multiple times into the knapsack (Unbounded Knapsack behavior), producing incorrect counts. Reverse loops ($m \to a, n \to b$) are strictly required for 0-1 knapsack.
- **Greedy Length Heuristics:** Picking the shortest strings first is a greedy heuristic that fails when a slightly longer string with better zero/one proportions fits tighter into the remaining budget. Only dynamic programming guarantees global optimality.
- **Allocating 3D Arrays in Memory ($O(|strs| \cdot m \cdot n)$):** Using a full 3D array `f[sz][m][n]` wastes memory. Compressing to a 2D rolling array `f[m][n]` reduces memory to a tiny $100 \times 100$ matrix.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $L = |strs|$.
  - Counting zeroes and ones for all strings takes $\sum |s_i| \le 600 \times 100 = 6 \times 10^4$ operations.
  - The DP loop runs $L$ times with two nested loops of size $(m + 1) \times (n + 1)$.
  - Total Time: $\mathcal{O}(L \times m \times n)$. For $L = 600, m = 100, n = 100$, $600 \times 10^4 = 6 \times 10^6$ operations, executing in $< 50$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(m \times n)$ to store the 2D DP grid of size $(m+1) \times (n+1)$.
