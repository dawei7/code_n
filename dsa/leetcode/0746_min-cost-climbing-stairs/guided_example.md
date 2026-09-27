# Guided Example: Min Cost Climbing Stairs

We trace the step-by-step staircase elevation transitions, dual starting position alternatives (index $0$ or index $1$), one-step versus two-step stride optimization, forward Bellman state accumulation ($dp[i] = \min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])$), space-optimized rolling variables, and top-of-floor attainment on representative climbing cost profiles:

- **Input:** $cost = [10, 15, 20]$
- **Required output:** `15`
  - Staircase rules:
    - $cost[i]$ is the fee paid when departing from step $i$.
    - From step $i$, you can climb either **1 step** (to $i + 1$) or **2 steps** (to $i + 2$).
    - Free starting positions: You can begin your ascent directly on **step 0** or **step 1** at zero initial penalty.
    - **Top of the Floor Goal:**
      - The destination is reaching the top landing located at index $n = |cost| = 3$.
      - You do **not** pay any fee once you land on or pass index $n$.
    - Strategy comparison for $[10, 15, 20]$:
      - Option 1 (Start at step 0):
        - Pay 10 at step 0, jump 1 step to step 1.
        - Pay 15 at step 1, jump 2 steps to top (landing 3).
        - Total fee: $10 + 15 = 25$.
      - Option 2 (Start at step 0, leap over step 1):
        - Pay 10 at step 0, jump 2 steps to step 2.
        - Pay 20 at step 2, jump 1 step to top (landing 3).
        - Total fee: $10 + 20 = 30$.
      - Option 3 (Start directly at step 1):
        - Step 0 is completely bypassed.
        - Pay 15 at step 1, jump 2 steps directly to top (landing 3).
        - Total fee: **15**.
      - Minimum possible cost: **15**.
- **Forward Dynamic Programming State Invariant:**
  - **State Definition ($dp[i]$):**
    - Let $dp[i]$ represent the minimum cumulative cost required to reach landing / step $i$.
  - **Base Cases:**
    - Reaching step 0 costs 0 (free start): $dp[0] = 0$.
    - Reaching step 1 costs 0 (free start): $dp[1] = 0$.
  - **The Transition Equation for $i \ge 2$:**
    - To arrive at step $i$, you must arrive from either:
      1. Step $i - 1$, paying $cost[i - 1]$ to depart: $dp[i - 1] + cost[i - 1]$.
      2. Step $i - 2$, paying $cost[i - 2]$ to depart: $dp[i - 2] + cost[i - 2]$.
    - Bellman Optimality Principle:
      $$
      dp[i] = \min(dp[i - 1] + cost[i - 1], \; dp[i - 2] + cost[i - 2])
      $$
  - **Target Landing:**
    - The top of the staircase corresponds to index $n = |cost|$.
    - The answer is $dp[n]$.
- **Step-by-Step Worked Execution Trace on $cost = [10, 15, 20]$:**
  - Staircase length: $n = 3$. Array: $[cost[0]=10, \; cost[1]=15, \; cost[2]=20]$.
  - **Base States:**
    $$
    dp[0] = \mathbf{0}
    $$
    $$
    dp[1] = \mathbf{0}
    $$
  - **Step $i = 2$ (Arriving at Step 2):**
    - Transition paths:
      - Path A (from step 1):
        $$
        dp[1] + cost[1] = 0 + 15 = \mathbf{15}
        $$
      - Path B (from step 0):
        $$
        dp[0] + cost[0] = 0 + 10 = \mathbf{10}
        $$
    - Take the minimum:
      $$
      dp[2] = \min(15, \; 10) = \mathbf{10}
      $$
  - **Step $i = 3$ (Arriving at Top Landing $n = 3$):**
    - Transition paths:
      - Path A (from step 2):
        $$
        dp[2] + cost[2] = 10 + 20 = \mathbf{30}
        $$
      - Path B (from step 1):
        $$
        dp[1] + cost[1] = 0 + 15 = \mathbf{15}
        $$
    - Take the minimum:
      $$
      dp[3] = \min(30, \; 15) = \mathbf{15}
      $$
  - **Final Output:**
    $$
    ans = dp[3] = \mathbf{15}
    $$
- **Multi-Step Obstacle Course ($cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]$):**
  - Length $n = 10$.
  - Jump over every expensive step ($100$) by leaping 2 steps.
  - Path: Start at step 0 (pay 1) $\to$ step 2 (pay 1) $\to$ step 4 (pay 1) $\to$ step 6 (pay 1) $\to$ step 7 (pay 1) $\to$ step 9 (pay 1) $\to$ Top landing.
  - Sum of fees: $1 + 1 + 1 + 1 + 1 + 1 = \mathbf{6}$.
- **Two Steps Only ($cost = [10, 15]$):**
  - $n = 2$.
  - Can jump 2 steps from step 0 (cost 10) or 2 steps from step 1 (cost 15).
  - Returns $\min(10, 15) = \mathbf{10}$.

This instance demonstrates linear shortest path DAG computation over topological step spaces, mathematically proves why local optimal choices in the Fibonacci-type recurrence preserve global minimum energy paths, and derives $O(N)$ execution time and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an array $cost$:
Paying $cost[i]$ lets you climb 1 or 2 steps.
You can start at step 0 or step 1.
Find the **minimum cost to reach the top landing** (index $n = |cost|$).

```text
cost = [ 10, 15, 20 ]

Option 1: Start at step 0 (10) -> step 1 (15) -> top (landing 3) -> cost 25
Option 2: Start at step 0 (10) -> step 2 (20) -> top (landing 3) -> cost 30
Option 3: Start at step 1 (15) -> jump 2 steps to top (landing 3) -> cost 15!

Best choice is Option 3!
Result: 15
```

### The Invariant of the Landing State
- Let $dp[i]$ be the minimum cost to reach step $i$.
- To arrive at step $i$, you either departed from $i-1$ (paying $cost[i-1]$) or departed from $i-2$ (paying $cost[i-2]$).
- Recurrence: $dp[i] = \min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])$.

---

## 2. Conceptual Foundation & Invariants

### 1. Base Cases:
$$
dp[0] = 0, \quad dp[1] = 0
$$

### 2. Forward Recurrence:
$$
dp[i] = \min(dp[i - 1] + cost[i - 1], \; dp[i - 2] + cost[i - 2]) \quad \forall i \in [2, n]
$$
$$
ans = dp[n]
$$

> **Step DAG Geodesic Invariant.** The staircase graph $(V, E)$ with vertices $\{0, \dots, n\}$ and directed edges $(i, i+1)$ and $(i, i+2)$ of weights $cost[i]$ is an acyclic DAG, whose single-pair shortest path from $\{0, 1\}$ to $n$ satisfies the Bellman functional equation.

---

## 3. Step-by-Step Worked Execution

We trace $cost = [10, 15, 20]$:

---

### Step 1: Base
- $dp[0] = 0, dp[1] = 0$.

---

### Step 2: Step 2
- From 1: $dp[1] + cost[1] = 0 + 15 = 15$.
- From 0: $dp[0] + cost[0] = 0 + 10 = 10$.
- $dp[2] = \min(15, 10) = 10$.

---

### Step 3: Top Landing 3
- From 2: $dp[2] + cost[2] = 10 + 20 = 30$.
- From 1: $dp[1] + cost[1] = 0 + 15 = 15$.
- $dp[3] = \min(30, 15) = \mathbf{15}$.

---

### Step 4: Output
$$
\mathbf{15}
$$

---

## 4. Complete Execution Trace

| Step $i$ Reached | Arrival from $i-1$ Cost | Arrival from $i-2$ Cost | Optimal Choice | Accumulated Minimum Cost $dp[i]$ |
|:---:|:---:|:---:|:---:|:---:|
| $0$ | — | — | Free start | $0$ |
| $1$ | — | — | Free start | $0$ |
| $2$ | $dp[1] + cost[1] = 15$ | $dp[0] + cost[0] = 10$ | From step 0 | $10$ |
| **$3$ (Top)** | **$dp[2] + cost[2] = 30$** | **$dp[1] + cost[1] = 15$** | **From step 1** | **`15`** |

---

## 5. Boundary Cases & Failure Modes

- **Length 2 Array ($[10, 15]$):** Jump directly from step 0 (10) or step 1 (15) to top landing $2 \implies \min(10, 15) = 10$.
- **All Identical Costs ($[5, 5, 5, 5]$):** Leaps 2 steps at each stride: $5 + 5 = 10$.
- **Zero Cost Steps ($[0, 0, 0, 0]$):** Cost is 0 throughout.
- **Large Unequal Jumps ($[1, 100, 1]$):** Always steps through the 1s, bypassing 100.

---

## 6. Traps & Common Anti-Patterns

- **Paying for Landing on Top:** The top of the staircase is index $n$, **not** index $n - 1$. Reaching index $n$ does not incur an additional cost.
- **Greedy Stride Selection:** Choosing the cheaper immediate step can trap you into paying a huge cost later (e.g. $[0, 2, 2, 1]$). DP explores both options and guarantees global minimum.
- **Overwriting Variables in $O(1)$ Space:** When rolling $first$ and $second$, compute $cur = \min(first + cost[i-2], second + cost[i-1])$ before updating $first = second, second = cur$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - A single linear loop from $i = 2$ to $n$: $\mathcal{O}(N)$.
  - Each step performs basic arithmetic and comparison: $\mathcal{O}(1)$.
  - Total Time: strictly linear $\mathcal{O}(N)$. Completes in $< 0.1$ ms for $N = 1000$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ space using two rolling variables $first$ and $second$.
