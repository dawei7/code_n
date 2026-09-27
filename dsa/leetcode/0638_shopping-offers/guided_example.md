# Guided Example: Shopping Offers

We trace the step-by-step multidimensional knapsack state representation ($needs \in \mathbb{N}_0^n$), default direct-retail baseline pricing ($\sum price_i \cdot need_i$), special offer bundle feasibility filtering ($\forall j: offer[j] \le need_j$), memoized search tree branching ($dfs(next\_needs)$), exact inventory constraint enforcement (no over-purchasing), and minimum expenditure optimization on representative store catalog instances:

- **Input:**
  - Item unit retail prices: $price = [2, 5]$ (Item 0 costs $\$2$, Item 1 costs $\$5$)
  - Special bundles:
    - Bundle A: $[3, 0, 5]$ (Contains 3 of Item 0, 0 of Item 1 for $\$5$)
    - Bundle B: $[1, 2, 10]$ (Contains 1 of Item 0, 2 of Item 1 for $\$10$)
  - Required shopping target: $needs = [3, 2]$ (Need exactly 3 of Item 0, and 2 of Item 1)
- **Required output:** `14`
  - Purchasing constraints:
    1. You must buy **exactly** the quantities requested in $needs$.
    2. You are **not allowed to buy more items than requested**, even if an offer would be cheaper overall.
    3. You can use any combination of special bundles (repeating as many times as valid) and individual item retail purchases.
- **Multidimensional State Space & Memoized DFS Architecture:**
  - State definition: The tuple of remaining unmet needs:
    $$
    S = (need_0, need_1, \dots, need_{n-1})
    $$
  - Since $n \le 6$ and $need_i \le 10$, each component can be represented as an integer coordinate or packed into a bitmask (4 bits per dimension).
  - **Upper Bound Baseline (No Bundles):**
    - The most basic valid option is to purchase all remaining items individually at standard shelf prices:
      $$
      cost_{retail}(S) = \sum_{i=0}^{n-1} price[i] \times S[i]
      $$
  - **Bundle Exploration:**
    - For each special bundle $offer = [c_0, c_1, \dots, c_{n-1}, \; P_{offer}]$:
      - Feasibility check: Can we take this bundle without exceeding our quota?
        $$
        \forall j \in [0, n - 1]: \quad c_j \le S[j]
        $$
      - If feasible, compute next state:
        $$
        S' = (S[0] - c_0, \; S[1] - c_1, \; \dots, \; S[n-1] - c_{n-1})
        $$
      - Explore cost:
        $$
        P_{offer} + dfs(S')
        $$
    - Minimization recurrence:
      $$
      dfs(S) = \min\left( cost_{retail}(S), \; \min_{feasible\ offers} \left( P_{offer} + dfs(S') \right) \right)
      $$
- **Step-by-Step Worked Execution Trace on $needs = [3, 2]$:**
  - Initial state: $S_0 = [3, 2]$.
  - **Baseline Retail Cost for $[3, 2]$:**
    $$
    cost_{retail} = 3 \times 2 + 2 \times 5 = 6 + 10 = \mathbf{16}
    $$
  - **Branch 1: Test Bundle A ($[3, 0, 5]$):**
    - Compare with $S_0 = [3, 2]$:
      - Item 0: $3 \le 3 \implies$ OK.
      - Item 1: $0 \le 2 \implies$ OK.
    - Bundle A is feasible!
    - New remaining needs:
      $$
      S_A = [3 - 3, \; 2 - 0] = [\mathbf{0}, \; \mathbf{2}]
      $$
    - **Subproblem $dfs([0, 2])$:**
      - Baseline retail cost for $[0, 2]$:
        $$
        0 \times 2 + 2 \times 5 = \mathbf{10}
        $$
      - Test Bundle A on $[0, 2]$: requires 3 of Item 0, but we have 0 ($3 > 0$) $\implies$ Infeasible.
      - Test Bundle B on $[0, 2]$: requires 1 of Item 0, but we have 0 ($1 > 0$) $\implies$ Infeasible.
      - No bundles feasible for $[0, 2] \implies dfs([0, 2]) = 10$.
    - Total cost via Branch 1:
      $$
      cost(A) = P_A + dfs([0, 2]) = 5 + 10 = \mathbf{15}
      $$
  - **Branch 2: Test Bundle B ($[1, 2, 10]$):**
    - Compare with $S_0 = [3, 2]$:
      - Item 0: $1 \le 3 \implies$ OK.
      - Item 1: $2 \le 2 \implies$ OK.
    - Bundle B is feasible!
    - New remaining needs:
      $$
      S_B = [3 - 1, \; 2 - 2] = [\mathbf{2}, \; \mathbf{0}]
      $$
    - **Subproblem $dfs([2, 0])$:**
      - Baseline retail cost for $[2, 0]$:
        $$
        2 \times 2 + 0 \times 5 = \mathbf{4}
        $$
      - Test Bundle A on $[2, 0]$: requires 3 of Item 0, but we have only 2 ($3 > 2$) $\implies$ Infeasible.
      - Test Bundle B on $[2, 0]$: requires 2 of Item 1, but we have 0 ($2 > 0$) $\implies$ Infeasible.
      - No bundles feasible for $[2, 0] \implies dfs([2, 0]) = 4$.
    - Total cost via Branch 2:
      $$
      cost(B) = P_B + dfs([2, 0]) = 10 + 4 = \mathbf{14}
      $$
  - **Step 4: Global Minimum Comparison:**
    $$
    ans = \min(\text{Retail}: 16, \; \text{Bundle A}: 15, \; \text{Bundle B}: 14) = \mathbf{14}
    $$
  - Return **`14`**.
- **Over-Purchasing Disqualification Instance:**
  - Suppose there was a mega bundle $[4, 4, 8]$ (4 of each for only $\$8$).
  - Although $\$8 < \$14$, buying it would leave us with 4 of Item 0 and 4 of Item 1, exceeding $needs = [3, 2]$.
  - The feasibility check $4 \le 3$ fails, correctly preventing this illegal purchase.
- **Useless Bundle Pruning:**
  - If a bundle $[1, 1, 10]$ costs $\$10$, but buying 1 of each individually costs $2 + 5 = \$7$, the baseline $cost_{retail}$ automatically beats the bundle.

This instance demonstrates exact-fit multidimensional knapsack optimization, mathematically proves why strict component-wise inequalities ensure zero excess inventory, and derives $O(M \cdot \prod (needs_i + 1))$ memoized runtime and state bounds.

---

## 1. Instance & Teaching Goal

Given item prices, special bundle offers, and exact customer needs:
Find the **lowest cost** to buy the exact quantities requested.
You cannot buy more items than requested.

```text
Prices: Item 0 = $2, Item 1 = $5
Needs:  3 of Item 0, 2 of Item 1

Option 1 (Retail only):
  3 * $2 + 2 * $5 = $16

Option 2 (Use Bundle A: [3, 0] for $5):
  Bundle A ($5) + Remaining [0, 2] retail ($10) = $15

Option 3 (Use Bundle B: [1, 2] for $10):
  Bundle B ($10) + Remaining [2, 0] retail ($4) = $14  <-- CHEAPEST!

Result: 14
```

### The Invariant of Exact-Inventory Transitions
- We can view this as moving from $needs = [3, 2]$ towards target $[0, 0]$ in a discrete grid.
- Each valid step subtracts a non-negative vector $\vec{c}$ corresponding to a special offer such that all coordinates remain $\ge 0$.
- Unused items at any point can always be bought at individual retail rates.

---

## 2. Conceptual Foundation & Invariants

### 1. The Dynamic Recurrence:
$$
dfs(\vec{S}) = \min \left( \sum_{i} price[i] \cdot S[i], \quad \min_{offer \le \vec{S}} \left( price_{offer} + dfs(\vec{S} - \vec{offer}) \right) \right)
$$

### 2. Base Case:
$$
dfs(\vec{0}) = 0
$$

> **Sub-Additive Lattice Invariant.** The price function on the multi-commodity inventory lattice $\mathbb{N}_0^n$ is bounded above by the linear inner product $\langle \vec{price}, \vec{needs} \rangle$, with concave infima attained along valid bundle combinations.

---

## 3. Step-by-Step Worked Execution

We trace $needs = [3, 2]$:

---

### Step 1: Evaluate Baseline
- Retail cost: $3(2) + 2(5) = 16$.

---

### Step 2: Try Bundle A $[3, 0, 5]$
- Feasible: $3 \le 3, 0 \le 2$.
- Remainder: $[0, 2]$.
- $dfs([0, 2]) = 0(2) + 2(5) = 10$.
- Total via A: $5 + 10 = 15$.

---

### Step 3: Try Bundle B $[1, 2, 10]$
- Feasible: $1 \le 3, 2 \le 2$.
- Remainder: $[2, 0]$.
- $dfs([2, 0]) = 2(2) + 0(5) = 4$.
- Total via B: $10 + 4 = 14$.

---

### Step 4: Minimum
$$
\min(16, 15, 14) = \mathbf{14}
$$

---

## 4. Complete Execution Trace

| State $\vec{S}$ | Candidate Choice | Feasible? | Remainder $\vec{S}'$ | Transition Cost | Total Branch Cost | Best for State |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $[3, 2]$ | Retail | **Yes** | — | $3(2) + 2(5) = 16$ | $16$ | $16$ |
| $[3, 2]$ | Bundle A ($[3, 0]$) | **Yes** | $[0, 2]$ | $\$5 + dfs([0, 2])$ | $5 + 10 = 15$ | $15$ |
| $[3, 2]$ | Bundle B ($[1, 2]$) | **Yes** | $[2, 0]$ | $\$10 + dfs([2, 0])$ | $10 + 4 = \mathbf{14}$ | **`14`** |
| **Output** | — | — | — | — | — | **`14`** |

---

## 5. Boundary Cases & Failure Modes

- **$needs = [0, \dots, 0]$:** Cost is 0.
- **No Special Offers Feasible:** Falls back to pure retail cost.
- **Overpriced Special Offers:** If an offer costs more than retail, baseline retail check automatically dominates and discards it.
- **Offers with 0 Quantities:** Handled naturally by vector subtraction.

---

## 6. Traps & Common Anti-Patterns

- **Greedy Selection of "Best Discount" Offer:** Choosing the bundle with the highest percentage savings can trap you into an unfavorable remainder that forces expensive retail purchases. Global DP/DFS is mandatory.
- **Allowing Negative Remainder (Over-Purchasing):** If an offer has 4 items and you only need 3, taking it is strictly illegal. The condition $c_j \le S[j]$ must hold for **every** item $j$.
- **Not Memoizing States:** Without `@cache` or a lookup table, overlapping paths (e.g. taking Offer 1 then Offer 2 vs Offer 2 then Offer 1) re-evaluate the same state exponentially.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $n$ be the number of distinct items ($n \le 6$) and $N_i$ be $needs[i]$ ($N_i \le 10$).
  - Total reachable states: $\le \prod_{i=0}^{n-1} (N_i + 1) \le 11^6$.
  - In practice, valid states reachable from $[3, 2]$ are $< 100$.
  - At each state, we iterate through $M$ special offers ($M \le 100$).
  - Total Time: $\mathcal{O}(M \cdot \prod (N_i + 1))$. Completes in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(\prod (N_i + 1))$ for the memoization cache and call stack.