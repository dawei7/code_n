# Guided Example: Super Egg Drop

We trace the step-by-step worst-case minimax recurrence, monotonic function intersection bisection, building partition strategy, and minimal drop move derivation on representative egg and floor configurations:

- **Input:**
  $$
  k = 2, \quad n = 6
  $$
- **Required output:** `3`
  - Problem physics & rules:
    - We are given $k = 2$ identical eggs and a building with $n = 6$ floors (numbered $1$ to $6$).
    - There exists an unknown critical floor $F \in [0, 6]$ such that:
      - Any egg dropped from a floor $\le F$ **survives intact** and can be reused.
      - Any egg dropped from a floor $> F$ **breaks permanently**.
    - If an egg survives, it can be dropped again. If an egg breaks, we must continue testing with the remaining $k - 1$ eggs.
    - Objective: Find the **minimum number of moves** needed to determine $F$ with certainty in the worst case.
    - For $k = 2, n = 6$:
      - If we drop from floor $3$:
        - Case A (Breaks): $1$ egg left, $2$ floors below ($1, 2$). Testing them takes at most $2$ drops (floors 1 then 2) $\implies 1 + 2 = 3$ total drops.
        - Case B (Survives): $2$ eggs left, $3$ floors above ($4, 5, 6$). Next drop from floor $5$:
          - If breaks: test floor 4 ($1$ drop) $\implies 3$ drops.
          - If survives: test floor 6 ($1$ drop) $\implies 3$ drops.
      - In every branch, $F$ is uniquely identified within at most $3$ drops!
      - Can it be done in 2 drops? With 2 drops, the maximum floors testable is $2 + 1 = 3 < 6$.
      - Minimum moves required: **`3`**.
- **The Minimax Intersection & Convexity Invariant:**
  - **The Decision Recurrence:**
    - Suppose we have $j$ eggs and $i$ floors remaining to search.
    - If we drop an egg from the $x$-th floor of this range ($1 \le x \le i$):
      1. **Egg breaks:** We now have $j - 1$ eggs and must search the $x - 1$ floors below $\implies dp(x - 1, j - 1)$.
      2. **Egg survives:** We still have $j$ eggs and must search the $i - x$ floors above $\implies dp(i - x, j)$.
    - The worst-case outcome for this specific choice $x$ is:
      $$
      \text{cost}(x) = 1 + \max\left(dp(x - 1, j - 1), \; dp(i - x, j)\right)
      $$
    - An optimal player chooses the floor $x$ that minimizes the worst-case cost:
      $$
      dp(i, j) = 1 + \min_{1 \le x \le i} \max\left(dp(x - 1, j - 1), \; dp(i - x, j)\right)
      $$
  - **The Opposing Monotonicities (V-Shape Convexity):**
    - Regard $T_1(x) = dp(x - 1, j - 1)$ as a function of $x$: As $x$ increases, the number of floors below increases, so $T_1(x)$ is **strictly non-decreasing**.
    - Regard $T_2(x) = dp(i - x, j)$ as a function of $x$: As $x$ increases, the number of floors above decreases, so $T_2(x)$ is **strictly non-increasing**.
    - The maximum of an increasing function and a decreasing function forms a **V-shaped convex curve**.
    - The minimum occurs at or adjacent to their point of intersection:
      $$
      T_1(x) \approx T_2(x)
      $$
    - We can find the optimal floor $x$ using **Binary Search in $\mathcal{O}(\log i)$ time** instead of linear scanning!

---

## 1. Instance & Teaching Goal

Given $k = 2$ eggs and $n = 6$ floors, derive the optimal drop sequence and prove why $3$ drops are necessary and sufficient.

```text
Decision Tree for 2 Eggs, 6 Floors:
First Drop at Floor 3:
      [Drop at Floor 3]
       /             \
 (Egg Breaks)    (Egg Survives)
Search {1, 2}     Search {4, 5, 6}
1 Egg Left        2 Eggs Left
Drop 1:           Drop 5:
  F=0 or 1 or 2     /          \
  (<= 2 drops)  (Breaks)   (Survives)
                Check 4     Check 6
                (Total 3)   (Total 3)

Worst-case moves across all outcomes = 3
```

The teaching goal is to demonstrate how identifying opposing monotonic curves replaces linear DP searches with logarithmic bisections.

---

## 2. Conceptual Foundation & Invariants

### 1. Base Boundary Conditions:
- Zero floors: $dp(0, j) = 0$ (no search required).
- One floor: $dp(1, j) = 1$ (one drop identifies whether $F=0$ or $F=1$).
- One egg: $dp(i, 1) = i$ (must test sequentially from bottom to top $1, 2, \dots, i$).

### 2. Binary Search for Optimal Split:
For state $(i, j)$, search $x \in [1, i]$:
- Let $a = dp(mid - 1, j - 1)$ (cost if egg breaks).
- Let $b = dp(i - mid, j)$ (cost if egg survives).
- If $a \le b$: $mid$ is to the left of the intersection $\implies l \leftarrow mid$.
- If $a > b$: $mid$ is to the right of the intersection $\implies r \leftarrow mid - 1$.
- After convergence at $x^*$, compute:
  $$
  dp(i, j) = 1 + \max(dp(x^* - 1, j - 1), \; dp(i - x^*, j))
  $$

---

## 3. Step-by-Step Worked Execution

We compute $dp(6, 2)$ from base cases:

---

### Step 1: Base Case Subproblems
- 1 Egg on $m$ floors:
  - $dp(1, 1) = 1$
  - $dp(2, 1) = 2$
  - $dp(3, 1) = 3$
  - $dp(4, 1) = 4$
  - $dp(5, 1) = 5$
- 2 Eggs on small floors:
  - $dp(1, 2) = 1$
  - $dp(2, 2) = 2$ (drop at 1: breaks $\to 0$ left; survives $\to 1$ left)
  - $dp(3, 2) = 2$ (drop at 2: breaks $\to dp(1, 1)=1$; survives $\to dp(1, 2)=1 \implies 1 + 1 = 2$)

---

### Step 2: Evaluate 2 Eggs on 4 Floors ($dp(4, 2)$)
- Test drop floors $x \in [1, 4]$:
  - $x = 1: 1 + \max(dp(0, 1), dp(3, 2)) = 1 + \max(0, 2) = 3$.
  - $x = 2: 1 + \max(dp(1, 1), dp(2, 2)) = 1 + \max(1, 2) = 3$.
  - $x = 3: 1 + \max(dp(2, 1), dp(1, 2)) = 1 + \max(2, 1) = 3$.
- Optimal worst-case: $dp(4, 2) = \mathbf{3}$.

---

### Step 3: Evaluate 2 Eggs on 5 Floors ($dp(5, 2)$)
- Test $x = 3$:
  - Breaks: $dp(2, 1) = 2$.
  - Survives: $dp(2, 2) = 2$.
  - $1 + \max(2, 2) = 3$.
- Optimal worst-case: $dp(5, 2) = \mathbf{3}$.

---

### Step 4: Evaluate 2 Eggs on 6 Floors ($dp(6, 2)$)
- Binary search over $x \in [1, 6]$:
  - Candidate $x = 3$:
    - Breaks: $a = dp(3 - 1, 1) = dp(2, 1) = 2$.
    - Survives: $b = dp(6 - 3, 2) = dp(3, 2) = 2$.
    - Because $a = 2 == b = 2$, this point achieves the **exact intersection** where both branches balance perfectly!
    - Worst case cost:
      $$
      1 + \max(a, b) = 1 + \max(2, 2) = 1 + 2 = \mathbf{3}
      $$
- Minimal drops required: **`3`**.

---

## 4. Complete Execution Trace

| Building Floors $n$ | Eggs Available $k$ | Tested Drop Floor $x$ | Break Outcome ($dp(x-1, k-1)$) | Survive Outcome ($dp(n-x, k)$) | Worst-Case Moves ($1 + \max$) | Optimal $dp(n, k)$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | $2$ | $1$ | $dp(0, 1) = 0$ | $dp(0, 2) = 0$ | $1 + 0 = 1$ | $1$ |
| $2$ | $2$ | $1$ | $dp(0, 1) = 0$ | $dp(1, 2) = 1$ | $1 + 1 = 2$ | $2$ |
| $3$ | $2$ | $2$ | $dp(1, 1) = 1$ | $dp(1, 2) = 1$ | $1 + 1 = 2$ | $2$ |
| $4$ | $2$ | $2$ | $dp(1, 1) = 1$ | $dp(2, 2) = 2$ | $1 + 2 = 3$ | $3$ |
| $5$ | $2$ | $3$ | $dp(2, 1) = 2$ | $dp(2, 2) = 2$ | $1 + 2 = 3$ | $3$ |
| **$6$** | **$2$** | **$3$** | **$dp(2, 1) = 2$** | **$dp(3, 2) = 2$** | **$1 + 2 = 3$** | **`3`** |

---

## 5. Boundary Cases & Failure Modes

- **$k = 1$ (One Egg):** Must test floor by floor from 1 to $n$. Cannot risk breaking the only egg $\implies$ returns $n$.
- **$n = 1$ (One Floor):** Exactly one drop required $\implies$ returns $1$.
- **Large Number of Eggs ($k \ge \lceil \log_2(n + 1) \rceil$):** Can perform pure binary search without worrying about running out of eggs $\implies \lceil \log_2(n + 1) \rceil$.

---

## 6. Traps & Common Anti-Patterns

- **Naive Binary Search on Floors Without Considering Eggs:** Dropping from midpoint $n/2$ when $k=2$ and $n=100$ means if the egg breaks at floor 50, one egg must linearly scan 49 floors, resulting in 50 drops in the worst case! The optimal first drop for $k=2, n=100$ is floor 14, which balances worst-case paths evenly.
- **Linear Scan Over $x$ in DP:** Testing all $x \in [1, i]$ gives $\mathcal{O}(k \cdot n^2)$ time, which times out on $n = 10^4$. Binary search on $x$ reduces complexity to $\mathcal{O}(k \cdot n \log n)$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Number of DP states $(n, k)$: $k \times n$.
  - Each state transitions using binary search over $x \in [1, i]$: $\mathcal{O}(\log n)$.
  - Total Time: $\mathcal{O}(k \cdot n \log n)$. For $k \le 100, n \le 10^4$, executes in $< 80$ ms.
- **Auxiliary Space Complexity:**
  - Memoization cache storing at most $k \cdot n$ entries: $\mathcal{O}(k \cdot n)$ space.
