# Guided Example: Coin Change II

We trace the step-by-step complete/unbounded knapsack dynamic programming formulation ($f[j] \mathrel{+}= f[j - x]$), coin-outer loop sequencing (enforcing combinations instead of permutations), forward capacity iteration ($x \to amount$), base zero-amount grounding ($f[0] = 1$), and combination enumeration on representative monetary amounts:

- **Input:** $amount = 5, \quad coins = [1, 2, 5]$
- **Required output:** `4`
  - Target amount: $5$
  - Coin denominations: $1, 2, 5$ (infinite supply of each)
  - Combinations requirement: Order does not matter (e.g. $1 + 2 + 2$ and $2 + 1 + 2$ are the exact same combination).
- **Unbounded Knapsack DP execution trace:**
  - Table array $f$ of size $amount + 1 = 6$ ($j \in [0, 5]$).
  - $f[j]$ represents the number of distinct combinations using the processed coins that sum to $j$.
  - **Base Case:**
    $$
    f[0] = 1, \quad f[1 \dots 5] = [0, 0, 0, 0, 0]
    $$
    (There is exactly 1 way to form an amount of 0: using zero coins).
  - **Stage 1: Introduce Coin Denomination $x = 1$:**
    - Iterate $j$ forward from $1$ to $5$:
      - $j = 1: f[1] \leftarrow f[1] + f[0] = 0 + 1 = \mathbf{1}$
      - $j = 2: f[2] \leftarrow f[2] + f[1] = 0 + 1 = \mathbf{1}$
      - $j = 3: f[3] \leftarrow f[3] + f[2] = 0 + 1 = \mathbf{1}$
      - $j = 4: f[4] \leftarrow f[4] + f[3] = 0 + 1 = \mathbf{1}$
      - $j = 5: f[5] \leftarrow f[5] + f[4] = 0 + 1 = \mathbf{1}$
    - Table state after coin $1$:
      $$
      f = [1, \; 1, \; 1, \; 1, \; 1, \; 1]
      $$
  - **Stage 2: Introduce Coin Denomination $x = 2$:**
    - Iterate $j$ forward from $2$ to $5$:
      - $j = 2: f[2] \leftarrow f[2] + f[0] = 1 + 1 = \mathbf{2}$ (combinations: $\{1+1\}, \{2\}$)
      - $j = 3: f[3] \leftarrow f[3] + f[1] = 1 + 1 = \mathbf{2}$ (combinations: $\{1+1+1\}, \{1+2\}$)
      - $j = 4: f[4] \leftarrow f[4] + f[2] = 1 + 2 = \mathbf{3}$ (combinations: $\{1+1+1+1\}, \{1+1+2\}, \{2+2\}$)
      - $j = 5: f[5] \leftarrow f[5] + f[3] = 1 + 2 = \mathbf{3}$ (combinations: $\{1\times 5\}, \{1\times 3 + 2\}, \{1 + 2 + 2\}$)
    - Table state after coins $\{1, 2\}$:
      $$
      f = [1, \; 1, \; 2, \; 2, \; 3, \; 3]
      $$
  - **Stage 3: Introduce Coin Denomination $x = 5$:**
    - Iterate $j$ forward from $5$ to $5$:
      - $j = 5: f[5] \leftarrow f[5] + f[0] = 3 + 1 = \mathbf{4}$
        (new combination: $\{5\}$)
    - Table state after all coins $\{1, 2, 5\}$:
      $$
      f = [1, \; 1, \; 2, \; 2, \; 3, \; \mathbf{4}]
      $$
  - Final total combinations: **`4`**.
  - The 4 unique combinations:
    1. $5 = 5$
    2. $5 = 2 + 2 + 1$
    3. $5 = 2 + 1 + 1 + 1$
    4. $5 = 1 + 1 + 1 + 1 + 1$
- **Unreachable Amount Instance ($amount = 3, coins = [2]$):**
  - Odd amount cannot be formed with even coins $\implies f[3] = \mathbf{0}$.
- **Zero Amount Target ($amount = 0$):**
  - Returns base case $f[0] = \mathbf{1}$ (empty set).
- **Single Denomination ($amount = 10, coins = [10]$):** Returns $\mathbf{1}$.

This instance demonstrates complete knapsack dynamic programming with combination order constraints, mathematically proves why outer coin iteration prevents permutation overcounting, and derives $O(N \cdot amount)$ runtime and $O(amount)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $coins$ and an integer $amount$:
Return the **number of combinations** that make up that amount.
Each coin can be chosen an infinite number of times.
If the amount cannot be made up, return `0`.

```text
Amount = 5, Coins = [1, 2, 5]

Valid Combinations:
  1. 5
  2. 2 + 2 + 1
  3. 2 + 1 + 1 + 1
  4. 1 + 1 + 1 + 1 + 1

Total Combinations = 4
```

### The Difference Between Combinations and Permutations
- If we loop over **amounts first** and coins second:
  $f[3]$ would count both $(1 + 2)$ and $(2 + 1)$ as distinct ways ($2$ permutations).
- By looping over **coins first** and amounts second:
  We decide how many copies of coin 1 to use, then how many copies of coin 2 to use, etc.
  Because coins are considered in a fixed non-decreasing sequence, **each multiset combination is counted exactly once**.

---

## 2. Conceptual Foundation & Invariants

### 1. Unbounded Knapsack Transition:
Let $f[j]$ be the number of ways to form amount $j$ using coins processed so far:
- Base case: $f[0] = 1$.
- For each coin $x \in coins$:
  Iterate capacity $j$ **forward** from $x$ to $amount$:
  $$
  f[j] \leftarrow f[j] + f[j - x]
  $$
- Why forward?
  Traversing $j$ in increasing order allows the same coin $x$ to be used multiple times in the same sum (since $f[j - x]$ already includes the possibility of having used coin $x$).

> **Combination Invariant.** Processing one denomination at a time ensures that any combination $(c_1, c_2, \dots, c_k)$ is assembled in monotonic denomination order, strictly prohibiting permutation duplicates.

---

## 3. Step-by-Step Worked Execution

We trace $amount = 5, coins = [1, 2, 5]$:

---

### Step 1: Initialize 1D Array
Array of size 6 ($0 \dots 5$):
$$
f = [1, \; 0, \; 0, \; 0, \; 0, \; 0]
$$

---

### Step 2: Process Coin $x = 1$
Loop $j$ from $1$ to $5$:
- $j=1: f[1] \leftarrow 0 + f[0] = 1$
- $j=2: f[2] \leftarrow 0 + f[1] = 1$
- $j=3: f[3] \leftarrow 0 + f[2] = 1$
- $j=4: f[4] \leftarrow 0 + f[3] = 1$
- $j=5: f[5] \leftarrow 0 + f[4] = 1$
State: `[1, 1, 1, 1, 1, 1]`.

---

### Step 3: Process Coin $x = 2$
Loop $j$ from $2$ to $5$:
- $j=2: f[2] \leftarrow 1 + f[0] = 1 + 1 = \mathbf{2}$
- $j=3: f[3] \leftarrow 1 + f[1] = 1 + 1 = \mathbf{2}$
- $j=4: f[4] \leftarrow 1 + f[2] = 1 + 2 = \mathbf{3}$
- $j=5: f[5] \leftarrow 1 + f[3] = 1 + 2 = \mathbf{3}$
State: `[1, 1, 2, 2, 3, 3]`.

---

### Step 4: Process Coin $x = 5$
Loop $j$ from $5$ to $5$:
- $j=5: f[5] \leftarrow 3 + f[0] = 3 + 1 = \mathbf{4}$
State: `[1, 1, 2, 2, 3, 4]`.

---

### Step 5: Final Count
$$
f[5] = \mathbf{4}
$$

---

## 4. Complete Execution Trace

| Coin $x$ | Capacity $j$ Evaluated | Prior $f[j]$ | Complement $f[j - x]$ | New $f[j] = \text{Prior} + \text{Comp}$ | Full Table $f[0 \dots 5]$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **Init** | — | — | — | — | `[1, 0, 0, 0, 0, 0]` |
| **$1$** | $1 \to 5$ | $0$ | $1$ | $0 + 1 = 1$ | `[1, 1, 1, 1, 1, 1]` |
| **$2$** | $2$ | $1$ | $f[0] = 1$ | $1 + 1 = 2$ | `[1, 1, 2, 1, 1, 1]` |
| **$2$** | $3$ | $1$ | $f[1] = 1$ | $1 + 1 = 2$ | `[1, 1, 2, 2, 1, 1]` |
| **$2$** | $4$ | $1$ | $f[2] = 2$ | $1 + 2 = 3$ | `[1, 1, 2, 2, 3, 1]` |
| **$2$** | $5$ | $1$ | $f[3] = 2$ | $1 + 2 = 3$ | `[1, 1, 2, 2, 3, 3]` |
| **$5$** | $5$ | $3$ | $f[0] = 1$ | $3 + 1 = \mathbf{4}$ | `[1, 1, 2, 2, 3, 4]` |

---

## 5. Boundary Cases & Failure Modes

- **Target $amount = 0$:** Always exactly 1 combination (choose no coins) $\implies \mathbf{1}$.
- **Target Cannot Be Formed ($amount = 3, coins = [2]$):** No odd numbers can be formed $\implies \mathbf{0}$.
- **Large Amounts ($amount = 5000$):** Combinations can exceed $2^{31} - 1$. Python handles arbitrary-precision integers automatically; C++ requires `unsigned long long` or checking constraints.
- **Empty Coin List ($coins = [], amount > 0$):** Cannot form amount $\implies \mathbf{0}$.

---

## 6. Traps & Common Anti-Patterns

- **Inverting the Nested Loops (Amounts Outer, Coins Inner):**
  Swapping the loop order calculates **permutations** (e.g. $[1, 2]$ and $[2, 1]$ counted separately), yielding 9 instead of 4 for $amount = 5$. Coins MUST be the outer loop for combinations.
- **Reverse Iteration in Inner Loop:**
  Iterating $j$ in reverse ($amount \to x$) is the rule for **0-1 Knapsack** (at most 1 coin of each type). Here, each coin is available in infinite supply, requiring **forward iteration** ($x \to amount$).
- **Initializing $f[0] = 0$:** If $f[0] = 0$, no combination can ever start, leaving the entire array as all zeros. $f[0] = 1$ is the foundational base case.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $N = |coins|$ and $A = amount$.
  - The outer loop runs $N$ times.
  - The inner loop iterates from $x$ up to $A$ (at most $A$ times).
  - Total Time: $\mathcal{O}(N \cdot A)$. For $N = 300, A = 5000$, $300 \times 5000 = 1.5 \times 10^6$ operations, completing in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(A)$ space using a single 1D rolling array of size $amount + 1$.