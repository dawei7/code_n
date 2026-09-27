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

### Why Greedy Is Not Enough: A Second Instance ($\text{costs} = [[1, 2, 3], [1, 100, 100]]$)

On the primary instance the greedy walk reaches the optimum, so it takes a deliberately adversarial pair of houses to separate the two strategies. House 0 is cheapest in Red, but that cheap choice forces House 1 into a cost of $100$; choosing the slightly dearer Blue at House 0 unlocks the cost-$1$ Red at House 1.

| House $i$ | $\text{costs}[i]$ | $DP[i][R]$ | $DP[i][B]$ | $DP[i][G]$ | Row minimum | Greedy walk from the previous greedy color |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | $[1, 2, 3]$ | $1$ | $2$ | $3$ | $1$ (Red) | Red is the row minimum, so the walk commits to Red, running total $1$ |
| 1 | $[1, 100, 100]$ | $1 + \min(2, 3) = \mathbf{3}$ | $100 + \min(1, 3) = 101$ | $100 + \min(1, 2) = 101$ | $3$ (Red) | Red is barred by the previous choice, so the walk pays $100$, running total $101$ |

The DP answer is $\min(3, 101, 101) = \mathbf{3}$, realised by the coloring Blue then Red ($2 + 1$), while the greedy walk reports $101$. The difference is exactly $98$ and comes entirely from a decision made at House 0: the value $DP[1][R] = 3$ is reachable only through $DP[0][B] = 2$, and a strategy that keeps a single running best value instead of three has already discarded that prefix before House 1 is ever examined. This is the Markov property doing real work: the three scalars $r$, $b$, $g$ preserve all three prefix optima, so no future constraint can invalidate a prefix that the greedy walk would have thrown away.

---

## 5. Algorithmic Correctness

**Soundness.** For house $i$, painting it color $c$ restricts house $i-1$ to the two other colors $c_1, c_2$. Taking $\min(DP[i-1][c_1], DP[i-1][c_2])$ selects the cheapest valid coloring for all preceding houses that does not violate the adjacency rule.

**Completeness.** Every legal assignment of colors corresponds to a path in the state transition graph. Because the recurrence explores all three color possibilities at every stage, no valid combination is excluded, and the minimum of the three terminal values is guaranteed to be the global minimum.

---

## 6. Traps This Instance Exposes

- **Greedy Trap:** Choosing the minimum cost for each house independently (e.g. $[2, 5, 3] = 10$ worked here by coincidence) fails whenever an adjacent house forces a much more expensive color later. Dynamic Programming considers the global trade-off.
- **Simultaneous State Overwriting:** When updating `r, b, g` sequentially in-place without temporary variables, writing `r = cost[0] + min(b, g)` modifies `r` before it is used to compute `new_b` and `new_g`! Using a tuple assignment `r, b, g = new_r, new_b, new_g` prevents stale state corruption.
- **Modifying Input In-Place:** Overwriting `costs[i][c]` directly saves memory but mutates caller data. Maintaining three scalar variables achieves $O(1)$ space while keeping the input pristine.

### Boundary instances and what each one pins down

Every row is a separate input evaluated by the same three-scalar recurrence; the last column names the structural fact that the instance isolates.

| Instance | Houses | Optimal total | Boundary it pins down |
|:---|:---:|:---:|:---|
| `[[7, 6, 2]]` | 1 | 2 | with a single house there is no adjacency constraint, so the answer is exactly the row minimum |
| `[[20, 1, 20]]` | 1 | 1 | the two inclusive cost limits $20$ and $1$ coexist in one row without changing the rule |
| `[[1, 20, 20], [1, 20, 20]]` | 2 | 21 | the cheapest color cannot repeat, so the second house must pay the alternative price: $1 + 20$ |
| `[[1, 20, 20], [1, 20, 20], [1, 20, 20]]` | 3 | 22 | alternating Red, other, Red is forced: $1 + 20 + 1$, far above the illegal $3$ |
| `[[8, 5, 7], [6, 7, 1]]` | 2 | 6 | the optimum is Blue then Green ($5 + 1$), so the second row's cheapest cell decides the answer |
| `[[1, 20, 20], [20, 2, 20], [3, 20, 4], [20, 1, 20]]` | 4 | 7 | the best path alternates two colors ($1 + 2 + 3 + 1$) even though all three state values stay live in the table |
| `[[1, 1, 20], [20, 1, 1], [1, 20, 1]]` | 3 | 3 | tied cells mean several optimal prefixes exist, and the total is still uniquely minimal |
| one hundred rows of $[20, 20, 20]$ | 100 | 2000 | with all costs equal, alternation is always legal, so the answer is simply $20N$ |

The two- and three-house rows are the sharpest boundary: they show that the cheapest color *can* be used again, but never on consecutive houses, which is exactly the constraint that forces the second-best price into the total. The final row shows the opposite extreme, where the constraint costs nothing at all because the alternative color is equally cheap.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of houses. For each house, exactly 3 additions and 3 comparisons are performed. Total operations: $3N = O(N)$.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary space. Only three scalar variables (`r`, `b`, `g`) are retained.

### Cost of the alternatives on the three-house instance

The counts below are exact for `costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]`, so the price of each representation is concrete.

| Strategy | Mechanism | Work on this instance | Cost or failure mode |
|:---|:---|:---|:---|
| Full two-dimensional DP table | store every $DP[i][c]$ cell for all houses | 9 cells filled: rows $(17, 2, 17)$, $(18, 33, 7)$, $(21, 10, 37)$ | $O(N)$ memory, and $6$ of the $9$ cells are dead the moment the next row is written |
| Rolling three scalars (the method used) | overwrite $(r, b, g)$ from the previous triple in one simultaneous assignment | 3 live scalars, with $3$ additions and $3$ comparisons per house | $O(1)$ memory; sequential assignment would read already-updated values and corrupt two of the three states |
| In-place overwrite of `costs[i][c]` | reuse the input matrix as the DP table | same 9 cells, using the caller's memory | $O(1)$ extra memory but the input is destroyed, so the colouring can no longer be reconstructed from it |
| Exhaustive enumeration of colorings | try every legal colouring and keep the cheapest | $3 \times 2^{2} = 12$ colourings to price, each needing a legality check and a 3-term sum | $\Theta(3 \cdot 2^{N-1})$: correct but exponential, so the one-hundred-house input is out of reach |
| Greedy walk that keeps one running best value | always take the cheapest colour allowed by the previous greedy pick | $10$ here, reached by coincidence | no lookahead and no state diversity: on $[[1, 2, 3], [1, 100, 100]]$ it returns $101$ where the optimum is $3$, because it discarded the Blue prefix at House 0 |

The first three rows all produce the same answer of $10$ and differ only in what they keep; the last two rows show the two genuine failure modes, one of cost (exponential enumeration) and one of correctness (a single-valued greedy state). The recurrence's three states are what let the rolling version keep the correctness of the full table at constant memory.