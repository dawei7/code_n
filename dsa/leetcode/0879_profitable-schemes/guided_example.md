# Guided Example: Profitable Schemes

We trace the step-by-step multi-dimensional 0/1 knapsack dynamic programming, profit saturation bounding ($\min(k + p, minProfit)$), group member capacity tracking, subset enumeration, and modular combination counting on representative crime portfolios:

- **Input:**
  $$
  n = 5, \quad minProfit = 3, \quad group = [2, 2], \quad profit = [2, 3]
  $$
- **Required output:** `2`
  - Scheme rules & constraints:
    - We have a gang of $n = 5$ members.
    - There is a list of crimes available. The $i$-th crime requires $group[i]$ members and generates $profit[i]$ profit.
    - Each member can participate in at most one crime in any chosen scheme (i.e. total members committed to selected crimes must be $\le n$).
    - A scheme is **profitable** if:
      1. Total members used $\le n = 5$.
      2. Total profit generated $\ge minProfit = 3$.
    - Objective: Return the number of distinct profitable subsets of crimes, modulo $10^9 + 7$.
    - Evaluating all $2^2 = 4$ crime subsets:
      - $\emptyset$ (No crimes): members $0 \le 5$, profit $0 < 3$ (Invalid).
      - $\{\text{Crime } 0\}$: members $2 \le 5$, profit $2 < 3$ (Invalid).
      - $\{\text{Crime } 1\}$: members $2 \le 5$, profit $3 \ge 3$ (**Valid Scheme 1**).
      - $\{\text{Crime } 0, \text{Crime } 1\}$: members $2 + 2 = 4 \le 5$, profit $2 + 3 = 5 \ge 3$ (**Valid Scheme 2**).
    - Total profitable schemes: **`2`**.
- **Multi-Dimensional Knapsack & Profit Saturation Invariant:**
  - **The Dual-Constraint Knapsack:**
    - Unlike standard knapsack problems that optimize a single resource, this problem features:
      1. An **upper-bounded constraint**: total members $\le n$.
      2. A **lower-bounded constraint**: total profit $\ge minProfit$.
  - **The Profit Saturation Principle:**
    - Any scheme generating profit $\ge minProfit$ satisfies the condition identically.
    - Whether a scheme earns $minProfit$, $minProfit + 1$, or $10^6$ does not alter its validity.
    - Therefore, we clamp (saturate) the profit state dimension:
      $$
      k' = \min(k + profit[i], \; minProfit)
      $$
    - This limits the profit state coordinate strictly to the discrete range $[0, minProfit]$, shrinking the state space from unbounded integers to exactly $minProfit + 1$ values!
  - **State Definition & Transition:**
    - Let $dp[j][k]$ denote the number of schemes using exactly $j$ members with effective profit $k \in [0, minProfit]$.
    - Base state: $dp[0][0] = 1$ (the empty scheme using 0 members with 0 profit).
    - When considering crime $(g, p)$:
      $$
      dp[j][\min(minProfit, k + p)] \leftarrow dp[j][\min(minProfit, k + p)] + dp[j - g][k]
      $$
    - Total valid schemes is the sum of all schemes with saturated profit $minProfit$ across all member counts $j \in [0, n]$:
      $$
      ans = \sum_{j=0}^n dp[j][minProfit] \pmod{10^9 + 7}
      $$

---

## 1. Instance & Teaching Goal

Given $n = 5$ members, $minProfit = 3$, and crimes $(g_0=2, p_0=2)$ and $(g_1=2, p_1=3)$, track how the DP matrix accumulates qualifying schemes.

```text
Crimes:
  Crime 0: members = 2, profit = 2
  Crime 1: members = 2, profit = 3

Base State:
  dp[0 members][profit 0] = 1

After Crime 0 (g=2, p=2):
  dp[0][0] = 1
  dp[2][2] = 1

After Crime 1 (g=2, p=3):
  From dp[0][0]: adds to dp[2][min(3, 0+3)=3] -> dp[2][3] = 1 (Scheme: {Crime 1})
  From dp[2][2]: adds to dp[4][min(3, 2+3)=3] -> dp[4][3] = 1 (Scheme: {Crime 0, Crime 1})

Qualifying schemes with profit >= 3:
  dp[2][3] + dp[4][3] = 1 + 1 = 2
```

The teaching goal is to justify how profit clamping transforms an open-ended sum into a finite dynamic programming lattice.

---

## 2. Conceptual Foundation & Invariants

### 1. Clamped Profit Dimension:
For any current profit $k$ and new profit $p$:
$$
\text{clamp}(k, p) = \min(k + p, \; minProfit)
$$

### 2. Knapsack Recurrence:
Iterating through each crime $(g, p)$ in reverse member order ($j$ from $n$ down to $g$) and reverse profit order ($k$ from $minProfit$ down to $0$):
$$
dp[j][\text{clamp}(k, p)] = \left( dp[j][\text{clamp}(k, p)] + dp[j - g][k] \right) \pmod{10^9 + 7}
$$

---

## 3. Step-by-Step Worked Execution

Grid dimensions: $(n + 1) \times (minProfit + 1) = 6 \times 4$.
Initialize: $dp[0][0] = 1$, all other $dp[j][k] = 0$.

---

### Step 1: Base State
- Empty set $\emptyset$: $0$ members, $0$ profit.
- Matrix has a single $1$ at $(j=0, k=0)$.

---

### Step 2: Incorporate Crime 0 ($g = 2, p = 2$)
- Existing state: $(j=0, k=0)$ with count $1$.
- New member count: $j' = 0 + 2 = 2 \le 5$.
- New clamped profit: $k' = \min(0 + 2, 3) = 2$.
- Update:
  $$
  dp[2][2] \leftarrow dp[2][2] + dp[0][0] = 0 + 1 = \mathbf{1}
  $$
- Active states after Crime 0:
  - $dp[0][0] = 1$ ($\emptyset$)
  - $dp[2][2] = 1$ ($\{\text{Crime } 0\}$)

---

### Step 3: Incorporate Crime 1 ($g = 2, p = 3$)
- **Transition from $(j=0, k=0)$:**
  - Member count: $j' = 0 + 2 = 2 \le 5$.
  - Clamped profit: $k' = \min(0 + 3, 3) = \mathbf{3}$.
  - Update:
    $$
    dp[2][3] \leftarrow dp[2][3] + dp[0][0] = 0 + 1 = \mathbf{1}
    $$
    *(Represents scheme $\{\text{Crime } 1\}$)*.
- **Transition from $(j=2, k=2)$:**
  - Member count: $j' = 2 + 2 = 4 \le 5$.
  - Clamped profit: $k' = \min(2 + 3, 3) = \min(5, 3) = \mathbf{3}$.
  - Update:
    $$
    dp[4][3] \leftarrow dp[4][3] + dp[2][2] = 0 + 1 = \mathbf{1}
    $$
    *(Represents scheme $\{\text{Crime } 0, \text{Crime } 1\}$)*.

---

### Step 4: Sum Qualifying Saturated States
We sum all schemes achieving profit level $k = minProfit = 3$:
$$
ans = \sum_{j=0}^{5} dp[j][3]
$$
- $j = 0: dp[0][3] = 0$
- $j = 1: dp[1][3] = 0$
- $j = 2: dp[2][3] = 1$
- $j = 3: dp[3][3] = 0$
- $j = 4: dp[4][3] = 1$
- $j = 5: dp[5][3] = 0$
$$
ans = 0 + 0 + 1 + 0 + 1 + 0 = \mathbf{2}
$$

---

## 4. Complete Execution Trace

| Crime Evaluated | Source State $(j, k)$ | Crime Cost $(g, p)$ | Destination State $(j+g, \min(3, k+p))$ | Schemes Added | Active DP Entries $(j, k) \to \text{count}$ |
|:---:|:---:|:---:|:---:|:---:|:---|
| Init | — | — | $(0, 0)$ | $1$ | $(0, 0): 1$ |
| Crime 0 | $(0, 0)$ | $(2, 2)$ | $(2, 2)$ | $1$ | $(0, 0): 1, \; (2, 2): 1$ |
| Crime 1 | $(0, 0)$ | $(2, 3)$ | **$(2, 3)$** | **$1$** | $(0, 0): 1, \; (2, 2): 1, \; \mathbf{(2, 3): 1}$ |
| Crime 1 | $(2, 2)$ | $(2, 3)$ | **$(4, 3)$** | **$1$** | $(0, 0): 1, \; (2, 2): 1, \; \mathbf{(2, 3): 1}, \; \mathbf{(4, 3): 1}$ |
| **Sum** | **Target $k = 3$** | — | — | — | **$dp[2][3] + dp[4][3] = 1 + 1 = \mathbf{2}$** |

---

## 5. Boundary Cases & Failure Modes

- **$minProfit = 0$:** Any scheme within $n$ members is valid (including empty set $\emptyset$). Clamping at $0$ reduces the profit dimension to a single column, counting all subsets with $\le n$ members.
- **Crime Requires More Members Than $n$ ($group[i] > n$):** Branch $j + group[i] \le n$ is skipped; crime cannot be part of any scheme.
- **No Crime Can Reach $minProfit$:** Final column $dp[\cdot][minProfit]$ remains $0 \implies$ returns $0$.

---

## 6. Traps & Common Anti-Patterns

- **Unbounded Profit Array:** Tracking raw profit amounts up to $\sum profit = 10^4$ blows up memory and time to $\mathcal{O}(M \cdot N \cdot \sum P)$. Clamping at $minProfit \le 100$ keeps the profit dimension tiny ($\le 101$).
- **Forward Iteration Without Copy:** Iterating $j$ ascending causes the same crime to be reused multiple times (unbounded knapsack). Iterating $j$ and $k$ descending guarantees each crime is chosen at most once.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $M$ be the number of crimes ($M \le 100$).
  - For each crime, we iterate over $j \in [0, n]$ and $k \in [0, minProfit]$.
  - Total operations: $M \times (n + 1) \times (minProfit + 1) \le 100 \times 101 \times 101 \approx 10^6$ operations.
  - Total Time: strictly $\mathcal{O}(M \cdot n \cdot minProfit)$, executing in $< 35$ ms.
- **Auxiliary Space Complexity:**
  - 2D DP array of size $(n + 1) \times (minProfit + 1) \le 101 \times 101$: $\mathcal{O}(n \cdot minProfit)$ space ($\approx 10$ KB).
