# Guided Example: Delete and Earn

We trace the step-by-step point potential aggregation ($total[x] \leftarrow x \times \text{count}(x)$), reduction to the canonical House Robber recurrence, adjacent numerical value exclusion constraints ($x-1$ and $x+1$), two-variable dynamic programming rolling state updates ($first, second$), non-adjacent selection optimization, and maximum points realization on representative integer multiset distributions:

- **Input:** $nums = [2, 2, 3, 3, 3, 4]$
- **Required output:** `9`
  - Game mechanics:
    - You can pick any number $x$ from the array to earn $x$ points.
    - However, picking $x$ forcibly deletes and destroys **every occurrence** of $x - 1$ and **every occurrence** of $x + 1$ without earning points from them.
    - Other copies of the same value $x$ are **not** destroyed by picking $x$.
    - **Greedy Multiplicity Observation:**
      - If you decide to pick the value $x$, there is no disadvantage to picking **all** available copies of $x$, since the penalty ($x-1$ and $x+1$ destroyed) is paid regardless.
      - Therefore, taking value $x$ yields a bundled payoff of:
        $$
        total[x] = x \times \text{count}(x)
        $$
    - For $[2, 2, 3, 3, 3, 4]$:
      - Value $2$ appears twice $\implies total[2] = 2 \times 2 = 4$.
      - Value $3$ appears three times $\implies total[3] = 3 \times 3 = 9$.
      - Value $4$ appears once $\implies total[4] = 4 \times 1 = 4$.
      - Strategy 1 (Take 2 and 4): destroys 3 $\implies$ earn $total[2] + total[4] = 4 + 4 = 8$.
      - Strategy 2 (Take 3): destroys 2 and 4 $\implies$ earn $total[3] = \mathbf{9}$.
      - Maximum points possible: **9**.
- **House Robber Reduction & Dynamic Programming Invariant:**
  - **The Structural Isomorphism:**
    - By transforming $nums$ into a frequency-weighted array $total$ indexed by integer values $0, 1, \dots, \max(nums)$:
      - Taking index $i$ yields $total[i]$ points, but prohibits taking adjacent indices $i - 1$ and $i + 1$.
      - This is mathematically isomorphic to the classic **House Robber** problem!
  - **State Formulation ($dp[i]$):**
    - Let $dp[i]$ denote the maximum points attainable considering only integer values in the range $0 \dots i$.
  - **Recurrence Transition for Value $i \ge 2$:**
    - **Choice A (Skip Value $i$):** Earn 0 from value $i$. Retain the best result from $i - 1$:
      $$
      \text{points} = dp[i - 1]
      $$
    - **Choice B (Take Value $i$):** Earn $total[i]$ points. Value $i - 1$ is prohibited, so combine with the best result from $i - 2$:
      $$
      \text{points} = dp[i - 2] + total[i]
      $$
    - Bellman Equation:
      $$
      dp[i] = \max(dp[i - 1], \; dp[i - 2] + total[i])
      $$
  - **Space Optimization ($O(1)$ Rolling Variables):**
    - To compute $dp[i]$, only the previous two states $dp[i-2]$ ($first$) and $dp[i-1]$ ($second$) are needed:
      $$
      cur = \max(second, \; first + total[i]), \quad first \leftarrow second, \quad second \leftarrow cur
      $$
- **Step-by-Step Worked Execution Trace on $nums = [2, 2, 3, 3, 3, 4]$:**
  - **Phase 0: Construct Total Value Payoff Table:**
    - Maximum element in array: $\max = 4$.
    - Table initialized for indices $0 \dots 4$:
      - $total[0] = 0$
      - $total[1] = 0$
      - $total[2] = 2 + 2 = \mathbf{4}$
      - $total[3] = 3 + 3 + 3 = \mathbf{9}$
      - $total[4] = 4 = \mathbf{4}$
      $$
      total = [0, \; 0, \; 4, \; 9, \; 4]
      $$
  - **Phase 1: Base Case Initialization:**
    - $first = dp[0] = total[0] = 0$.
    - $second = dp[1] = \max(total[0], total[1]) = \max(0, 0) = 0$.
  - **Phase 2: DP State Progression:**
    - **Value $i = 2$ ($total[2] = 4$):**
      - Choice: Skip vs Take:
        $$
        cur = \max(second, \; first + total[2]) = \max(0, \; 0 + 4) = \mathbf{4}
        $$
      - State shift: $first \leftarrow 0, \; second \leftarrow 4$.
    - **Value $i = 3$ ($total[3] = 9$):**
      - Choice: Skip ($second = 4$) vs Take ($first + total[3] = 0 + 9 = 9$):
        $$
        cur = \max(4, \; 0 + 9) = \mathbf{9}
        $$
        *(Taking the three 3s is strictly superior to retaining 2)*
      - State shift: $first \leftarrow 4, \; second \leftarrow 9$.
    - **Value $i = 4$ ($total[4] = 4$):**
      - Choice: Skip ($second = 9$) vs Take ($first + total[4] = 4 + 4 = 8$):
        $$
        cur = \max(9, \; 4 + 4) = \max(9, 8) = \mathbf{9}
        $$
        *(Skipping 4 preserves the 9 points from 3)*
      - State shift: $first \leftarrow 9, \; second \leftarrow 9$.
  - **Phase 3: Final Output:**
    $$
    ans = second = \mathbf{9}
    $$
- **Separated Values Trace ($nums = [3, 4, 2]$):**
  - $total = [0, 0, 2, 3, 4]$.
  - At $i = 2$: $dp[2] = 2$.
  - At $i = 3$: $dp[3] = \max(2, 0 + 3) = 3$.
  - At $i = 4$: $dp[4] = \max(3, 2 + 4) = \mathbf{6}$.
  - Returns **`6`** (taking 2 and 4).
- **Single Element Array ($nums = [10]$):**
  - $total[10] = 10$.
  - Returns **`10`**.

This instance demonstrates problem reduction to maximum-weight independent set on path graphs, mathematically proves why bundling identical elements optimizes reward under local deletion constraints, and derives $O(N + M)$ runtime and $O(M)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $nums$:
Pick number $x$ to earn $x$ points, but all copies of $x-1$ and $x+1$ are deleted.
Maximize total points.

```text
nums = [ 2, 2, 3, 3, 3, 4 ]

Aggregate totals by value:
  value 2: appears 2 times -> total = 4
  value 3: appears 3 times -> total = 9
  value 4: appears 1 time  -> total = 4

Adjacent values conflict!
  Option A: take 2 and 4 -> earn 4 + 4 = 8 (destroys 3)
  Option B: take 3       -> earn 9         (destroys 2 and 4)

Best choice is Option B!
Result: 9
```

### The Invariant of the House Robber Reduction
- If you take any copy of $x$, take ALL copies of $x$ since $x-1$ and $x+1$ are destroyed anyway.
- Map $total[x] = x \times \text{count}(x)$.
- Since adjacent values $x$ and $x+1$ cannot both be picked, this is identical to House Robber: $dp[i] = \max(dp[i-1], dp[i-2] + total[i])$.

---

## 2. Conceptual Foundation & Invariants

### 1. Payoff Aggregation:
$$
total[x] = \sum_{v \in nums, v = x} v = x \cdot \text{count}(x)
$$

### 2. The Recurrence:
$$
dp[i] = \max(dp[i - 1], \; dp[i - 2] + total[i])
$$

> **Independent Set Isomorphism Invariant.** The conflict hypergraph on values $\{v\}$ with edge set $\{ \{u, v\} \mid |u - v| = 1 \}$ is isomorphic to a linear path graph $P_M$, whose maximum-weight independent set is solvable by forward Dynamic Programming.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [2, 2, 3, 3, 3, 4]$:

---

### Step 1: Bucket Totals
- $total = [0, 0, 4, 9, 4]$.

---

### Step 2: Forward DP
- $i = 2$: $\max(0, 0 + 4) = 4$.
- $i = 3$: $\max(4, 0 + 9) = \mathbf{9}$.
- $i = 4$: $\max(9, 4 + 4) = \max(9, 8) = \mathbf{9}$.

---

### Step 3: Output
$$
\mathbf{9}
$$

---

## 4. Complete Execution Trace

| Value $i$ | Aggregated Value $total[i]$ | Skip Choice ($dp[i-1]$) | Take Choice ($dp[i-2] + total[i]$) | Winning Choice | Optimal Prefix Points $dp[i]$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | $0$ | — | — | Base | $0$ |
| $1$ | $0$ | $0$ | $0 + 0 = 0$ | Either | $0$ |
| $2$ | $4$ | $0$ | $0 + 4 = 4$ | Take | $4$ |
| $3$ | $9$ | $4$ | $0 + 9 = 9$ | **Take** | **`9`** |
| **$4$** | **$4$** | **$9$** | **$4 + 4 = 8$** | **Skip** | **`9`** |

---

## 5. Boundary Cases & Failure Modes

- **Disjoint Numbers ($[2, 5, 8]$):** None are adjacent $\implies$ can take all of them: $2 + 5 + 8 = 15$.
- **All Identical Elements ($[3, 3, 3, 3]$):** Takes all four 3s $\implies 12$.
- **Single Element ($[5]$):** Returns 5.
- **Large Range Gap ($[1, 10000]$):** Zero-filled buckets bridge the gap naturally without penalties.

---

## 6. Traps & Common Anti-Patterns

- **Greedy Selection by Highest Total:** A greedy choice of highest element can block two neighbors whose combined sum is larger (e.g. $[3, 4, 2]$ has 4 vs $2+3=5$; greedy picks 4 and loses 5). DP guarantees global optimality.
- **Taking Only One Copy of a Number:** Taking only one copy of $x$ still destroys $x-1$ and $x+1$. Always take all copies of $x$.
- **Allocating Full Array if Memory Limited:** If $\max(nums)$ is huge but sparse, compress values into unique sorted numbers and check if $nums[i] == nums[i-1] + 1$. Here $\max(nums) \le 10^4$, so direct indexing is optimal.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - One pass to find $\max(nums) = M$ and build $total$: $\mathcal{O}(N)$.
  - One pass from $0$ to $M$ to compute DP values: $\mathcal{O}(M)$.
  - Total Time: strictly linear $\mathcal{O}(N + M)$ where $N \le 2 \times 10^4, M \le 10^4$. Completes in $< 3$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(M)$ space for the $total$ array, with $O(1)$ space for the DP transition scalars.
