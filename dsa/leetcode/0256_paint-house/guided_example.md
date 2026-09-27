# Guided Example: Paint House

We trace the step-by-step three-color adjacent exclusion recurrence, rolling state transitions, and minimum total cost extraction on representative paint cost matrices:

- **Input:** $\text{costs} = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]$
- **Required output:** $10$ (Optimal coloring: House 0 Blue ($2$), House 1 Green ($5$), House 2 Blue ($3$) $\implies 2 + 5 + 3 = 10$)
- **Single House Instance:** $\text{costs} = [[7, 6, 2]] \implies 2$ (Select minimum cost among the three available colors)
- **Two Houses Inversion:** $\text{costs} = [[1, 100, 100], [1, 100, 100]] \implies 101$ (Cannot repeat the cheap Red color on consecutive houses)

This instance demonstrates dynamic programming under state adjacency constraints, explains why keeping the running optimal cost for each of the three ending colors ($r, b, g$) satisfies the Markov property, compresses the 2D DP table into three scalar variables for $O(1)$ auxiliary space, and evaluates in $O(N)$ time.

---

## 1. Instance & Teaching Goal

Given an $N \times 3$ cost matrix:
$$
\text{costs} = \begin{bmatrix}
17 & 2 & 17 \\
16 & 16 & 5 \\
14 & 3 & 19
\end{bmatrix}
$$
where columns $0, 1, 2$ represent Red, Blue, and Green respectively.
Paint all $N = 3$ houses such that **no two adjacent houses have the same color**, minimizing total cost.

- A greedy choice for House 0 is Blue ($2$).
- For House 1, the greedy choice without Blue is Green ($5$).
- For House 2, the greedy choice without Green is Blue ($3$).
- Total: $2 + 5 + 3 = \mathbf{10}$.
However, greedy strategies fail in general (e.g. choosing a slightly more expensive color now might unlock a vastly cheaper color later). Dynamic Programming explores all three color branches simultaneously, guaranteeing global optimality in $O(N)$ time.

---

## 2. Conceptual Foundation & Invariants

### State Formulation
Let $DP[i][c]$ denote the minimum cost to paint houses $0$ through $i$ such that house $i$ is painted color $c \in \{0, 1, 2\}$:
- $c = 0 \implies \text{Red}$
- $c = 1 \implies \text{Blue}$
- $c = 2 \implies \text{Green}$

### Transition Recurrence
Because house $i-1$ cannot share color $c$ with house $i$:
$$
DP[i][0] = \text{costs}[i][0] + \min\big(DP[i-1][1], \; DP[i-1][2]\big)
$$
$$
DP[i][1] = \text{costs}[i][1] + \min\big(DP[i-1][0], \; DP[i-1][2]\big)
$$
$$
DP[i][2] = \text{costs}[i][2] + \min\big(DP[i-1][0], \; DP[i-1][1]\big)
$$

### Rolling State Memory Compression
Notice that computing row $i$ depends strictly on row $i-1$. We only need three scalar variables $(r, b, g)$ tracking the optimal costs of the previous house:
$$
\text{new\_r} = \text{costs}[i][0] + \min(b, g)
$$
$$
\text{new\_b} = \text{costs}[i][1] + \min(r, g)
$$
$$
\text{new\_g} = \text{costs}[i][2] + \min(r, b)
$$
At the end, the global minimum cost is $\min(r, b, g)$.

> **Invariant.** After processing house $i$, $r$, $b$, and $g$ represent the exact minimum cumulative costs to legally paint the prefix of houses $[0 \dots i]$ ending in Red, Blue, and Green respectively.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $\text{costs} = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]$:

### Step 1: Base Case — House $i = 0$
For the first house, there is no previous house to conflict with:
$$
r = \text{costs}[0][0] = 17
$$
$$
b = \text{costs}[0][1] = 2
$$
$$
g = \text{costs}[0][2] = 17
$$
State after House 0: $(r = 17, \, b = 2, \, g = 17)$.

---

### Step 2: Transition — House $i = 1$ ($\text{costs}[1] = [16, 16, 5]$)
- **Paint Red ($c = 0$):**
  House 0 must be Blue or Green: $\min(b, g) = \min(2, 17) = 2$.
  $$
  \text{new\_r} = 16 + 2 = \mathbf{18}
  $$
- **Paint Blue ($c = 1$):**
  House 0 must be Red or Green: $\min(r, g) = \min(17, 17) = 17$.
  $$
  \text{new\_b} = 16 + 17 = \mathbf{33}
  $$
- **Paint Green ($c = 2$):**
  House 0 must be Red or Blue: $\min(r, b) = \min(17, 2) = 2$.
  $$
  \text{new\_g} = 5 + 2 = \mathbf{7}
  $$
Update state: $(r = 18, \, b = 33, \, g = 7)$.

---

### Step 3: Transition — House $i = 2$ ($\text{costs}[2] = [14, 3, 19]$)
- **Paint Red ($c = 0$):**
  House 1 must be Blue or Green: $\min(b, g) = \min(33, 7) = 7$.
  $$
  \text{new\_r} = 14 + 7 = \mathbf{21}
  $$
- **Paint Blue ($c = 1$):**
  House 1 must be Red or Green: $\min(r, g) = \min(18, 7) = 7$.
  $$
  \text{new\_b} = 3 + 7 = \mathbf{10}
  $$
- **Paint Green ($c = 2$):**
  House 1 must be Red or Blue: $\min(r, b) = \min(18, 33) = 18$.
  $$
  \text{new\_g} = 19 + 18 = \mathbf{37}
  $$
Update state: $(r = 21, \, b = 10, \, g = 37)$.

---

### Step 4: Terminal Resolution
All 3 houses are painted. Find the minimum among all three final color choices:
$$
\text{Total Minimum Cost} = \min(r, b, g) = \min(21, 10, 37) = \mathbf{10}
$$

---

## 4. Complete Execution Trace

```text
House 0: costs = [17, 2, 17] -> r=17, b=2,  g=17
House 1: costs = [16, 16, 5]
  new_r = 16 + min(2, 17)  = 18
  new_b = 16 + min(17, 17) = 33
  new_g =  5 + min(17, 2)  = 7   -> r=18, b=33, g=7
House 2: costs = [14, 3, 19]
  new_r = 14 + min(33, 7)  = 21
  new_b =  3 + min(18, 7)  = 10
  new_g = 19 + min(18, 33) = 37  -> r=21, b=10, g=37

Global Minimum: min(21, 10, 37) = 10
```

| House Index $i$ | Given Costs $[R, B, G]$ | Red Option ($+ \min(B, G)$) | Blue Option ($+ \min(R, G)$) | Green Option ($+ \min(R, B)$) | Cumulative $[r, b, g]$ | Current Minimum |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | $[17, 2, 17]$ | Base: $17$ | Base: $2$ | Base: $17$ | $[17, 2, 17]$ | 2 |
| 1 | $[16, 16, 5]$ | $16 + 2 = 18$ | $16 + 17 = 33$ | $5 + 2 = 7$ | $[18, 33, 7]$ | 7 |
| **2** | $[14, 3, 19]$ | $14 + 7 = 21$ | $3 + 7 = \mathbf{10}$ | $19 + 18 = 37$ | $[21, \mathbf{10}, 37]$ | **$\mathbf{10}$ (Optimal)** |

---

## 5. Algorithmic Correctness

**Soundness.** For house $i$, painting it color $c$ restricts house $i-1$ to the two other colors $c_1, c_2$. Taking $\min(DP[i-1][c_1], DP[i-1][c_2])$ selects the cheapest valid coloring for all preceding houses that does not violate the adjacency rule.

**Completeness.** Every legal assignment of colors corresponds to a path in the state transition graph. Because the recurrence explores all three color possibilities at every stage, no valid combination is excluded, and the minimum of the three terminal values is guaranteed to be the global minimum.

---

## 6. Traps This Instance Exposes

- **Greedy Trap:** Choosing the minimum cost for each house independently (e.g. $[2, 5, 3] = 10$ worked here by coincidence) fails whenever an adjacent house forces a much more expensive color later. Dynamic Programming considers the global trade-off.
- **Simultaneous State Overwriting:** When updating `r, b, g` sequentially in-place without temporary variables, writing `r = cost[0] + min(b, g)` modifies `r` before it is used to compute `new_b` and `new_g`! Using a tuple assignment `r, b, g = new_r, new_b, new_g` prevents stale state corruption.
- **Modifying Input In-Place:** Overwriting `costs[i][c]` directly saves memory but mutates caller data. Maintaining three scalar variables achieves $O(1)$ space while keeping the input pristine.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of houses. For each house, exactly 3 additions and 3 comparisons are performed. Total operations: $3N = O(N)$.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary space. Only three scalar variables (`r`, `b`, `g`) are retained.