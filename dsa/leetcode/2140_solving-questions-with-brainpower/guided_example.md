# Guided Example: Solving Questions With Brainpower

We trace the step-by-step derivation and execution of the backward Dynamic Programming algorithm on a representative problem instance, illustrating how backward optimal substructure resolves forward cooldown jump constraints.

- **Input:** `questions = [[3, 2], [4, 3], [4, 4], [2, 5]]`
- **Output:** `5`

This instance illustrates the trade-off between higher immediate points versus jumping past lucrative downstream questions.

---

## 1. Problem Overview & Representative Instance

An exam consists of $n$ ordered questions. For each question $i$, we are given:
- $\text{points}_i$: The score awarded for solving question $i$.
- $\text{brainpower}_i$: The mental cooldown required after solving question $i$.

When encountering question $i$, two mutually exclusive choices are available:
1. **Solve Question $i$:** Receive $\text{points}_i$, but skip the next $\text{brainpower}_i$ questions. The next reachable question index is $i + \text{brainpower}_i + 1$.
2. **Skip Question $i$:** Receive $0$ points, but remain eligible to solve question $i + 1$.

The objective is to determine the maximum total points achievable.

In our representative instance, $n = 4$:
- Question 0: $\text{points} = 3$, $\text{brainpower} = 2$. Next if solved: $0 + 2 + 1 = 3$.
- Question 1: $\text{points} = 4$, $\text{brainpower} = 3$. Next if solved: $1 + 3 + 1 = 5 \ge 4$ (out of bounds).
- Question 2: $\text{points} = 4$, $\text{brainpower} = 4$. Next if solved: $2 + 4 + 1 = 7 \ge 4$ (out of bounds).
- Question 3: $\text{points} = 2$, $\text{brainpower} = 5$. Next if solved: $3 + 5 + 1 = 9 \ge 4$ (out of bounds).

Evaluating from left to right creates forward dependency: solving question $0$ lands on question $3$, skipping questions $1$ and $2$. Conversely, skipping question $0$ allows answering question $1$ or $2$. A backward formulation eliminates this lookahead branching by resolving future subproblems first.

---

## 2. Mathematical & Algorithmic Principles

### Backward Dynamic Programming Formulation

Let $DP[i]$ denote the maximum points that can be collected from the suffix of questions starting at index $i$ through $n - 1$.

At each index $i \in [0, n - 1]$, exactly two decisions exist:
1. **Option A (Skip):** The score earned at index $i$ is $0$. The subsequent optimal payoff is $DP[i + 1]$.
   $$\text{Gain}_{\text{skip}} = DP[i + 1]$$
2. **Option B (Solve):** The score earned at index $i$ is $\text{points}_i$. The next question that may be attempted is at index $j = i + \text{brainpower}_i + 1$. If $j < n$, the maximum remaining payoff is $DP[j]$; if $j \ge n$, no further questions can be attempted, contributing $0$.
   $$\text{Gain}_{\text{solve}} = \text{points}_i + \begin{cases} DP[i + \text{brainpower}_i + 1] & \text{if } i + \text{brainpower}_i + 1 < n \\ 0 & \text{if } i + \text{brainpower}_i + 1 \ge n \end{cases}$$

The optimal value for suffix $i$ is the maximum of the two options:
$$DP[i] = \max\left(\text{Gain}_{\text{skip}}, \text{Gain}_{\text{solve}}\right)$$

### Base Case & Topological Order

- Base case: $DP[n] = 0$, representing an empty exam where no questions remain.
- Evaluation order: Compute backwards from $i = n - 1$ down to $i = 0$. Because each transition only queries indices strictly greater than $i$ ($i + 1$ and $i + \text{brainpower}_i + 1$), every dependency is already finalized when evaluating $DP[i]$.

| Parameter | Interpretation | Boundary / Evaluation Role |
|---|---|---|
| $DP[i]$ | Maximum points achievable from suffix $i \dots n-1$ | Primary dynamic programming state |
| $DP[n] = 0$ | Payoff beyond exam boundary | Base case anchoring recurrence |
| $i + 1$ | Target question index if skipped | Sequential backward neighbor |
| $i + \text{brainpower}_i + 1$ | Target question index if solved | Non-local forward jump target |
| $DP[0]$ | Maximum points achievable across full exam | Global terminal result |

---

## 3. Step-by-Step Walkthrough with Intermediate State

We execute backward dynamic programming on `questions = [[3, 2], [4, 3], [4, 4], [2, 5]]` with $n = 4$.

```
Index:         0          1          2          3
Question:   [3, 2]     [4, 3]     [4, 4]     [2, 5]
Jump to:    index 3   out-of-bd  out-of-bd  out-of-bd
```

### Step 1: Initialize Base Boundary
- Array size: $n = 4$.
- Base state: $DP[4] = 0$.

### Step 2: Evaluate Index $i = 3$ (Question: $[2, 5]$)
- Points: $2$, Brainpower: $5$.
- Option A (Skip): $DP[4] = 0$.
- Option B (Solve):
  - Next index: $3 + 5 + 1 = 9 \ge 4$.
  - Additional payoff: $0$.
  - Total solve score: $2 + 0 = 2$.
- Optimal choice: $DP[3] = \max(0, 2) = 2$.
- State: Solving is strictly better than skipping.

### Step 3: Evaluate Index $i = 2$ (Question: $[4, 4]$)
- Points: $4$, Brainpower: $4$.
- Option A (Skip): $DP[3] = 2$.
- Option B (Solve):
  - Next index: $2 + 4 + 1 = 7 \ge 4$.
  - Additional payoff: $0$.
  - Total solve score: $4 + 0 = 4$.
- Optimal choice: $DP[2] = \max(2, 4) = 4$.
- State: Solving yields $4$, surpassing the skip payoff of $2$.

### Step 4: Evaluate Index $i = 1$ (Question: $[4, 3]$)
- Points: $4$, Brainpower: $3$.
- Option A (Skip): $DP[2] = 4$.
- Option B (Solve):
  - Next index: $1 + 3 + 1 = 5 \ge 4$.
  - Additional payoff: $0$.
  - Total solve score: $4 + 0 = 4$.
- Optimal choice: $DP[1] = \max(4, 4) = 4$.
- State: Both skipping and solving yield $4$. The optimal suffix value is $4$.

### Step 5: Evaluate Index $i = 0$ (Question: $[3, 2]$)
- Points: $3$, Brainpower: $2$.
- Option A (Skip): $DP[1] = 4$.
- Option B (Solve):
  - Next index: $0 + 2 + 1 = 3 < 4$.
  - Subsequent state is within bounds: look up $DP[3] = 2$.
  - Total solve score: $3 + DP[3] = 3 + 2 = 5$.
- Optimal choice: $DP[0] = \max(4, 5) = 5$.
- State: Solving question $0$ and then question $3$ yields $3 + 2 = 5$, strictly beating the skip path of $4$.

Global optimum found: $DP[0] = 5$.

---

## 4. Comprehensive State Trace

The table below summarizes the evaluation across all indices in backward order:

| Index $i$ | $[\text{points}_i, \text{brainpower}_i]$ | Next Index if Solved | Skip Value $DP[i+1]$ | Solve Value $\text{points}_i + DP[\text{next}]$ | Chosen Decision | Final $DP[i]$ |
|---|---|---|---|---|---|---|
| $4$ (Base) | Boundary | N/A | N/A | N/A | Base Definition | $0$ |
| $3$ | $[2, 5]$ | $9$ ($\ge 4$) | $0$ | $2 + 0 = 2$ | Solve | $2$ |
| $2$ | $[4, 4]$ | $7$ ($\ge 4$) | $2$ | $4 + 0 = 4$ | Solve | $4$ |
| $1$ | $[4, 3]$ | $5$ ($\ge 4$) | $4$ | $4 + 0 = 4$ | Tie (Either) | $4$ |
| $0$ | $[3, 2]$ | $3$ ($< 4$) | $4$ | $3 + DP[3] = 3 + 2 = 5$ | Solve | $5$ |

Reconstructed optimal choice path:
1. At index $0$: Solve question $0$ (earn $3$ points). Cooldown skips indices $1$ and $2$.
2. Next active index is $3$: Solve question $3$ (earn $2$ points).
3. Total score: $3 + 2 = 5$.

Alternative candidate comparison:
- Skip question $0$, solve question $1$: Points $= 4$ (skips rest of exam).
- Skip question $0$, skip question $1$, solve question $2$: Points $= 4$ (skips rest of exam).
- Maximum across all possible strategies is indeed $5$.

---

## 5. Algorithmic Correctness & Soundness

### Principle of Optimality
The problem exhibits optimal substructure. The decisions available at question $i$ depend solely on the maximum points achievable on future suffix subproblems, independent of what prior decisions were made before index $i$:
- If question $i$ is skipped, the remaining subproblem is questions $i+1 \dots n-1$.
- If question $i$ is solved, the remaining subproblem is questions $j \dots n-1$ where $j = i + \text{brainpower}_i + 1$.

Because neither choice imposes backward constraints on questions already resolved, the recurrence $DP[i] = \max(\text{Gain}_{\text{skip}}, \text{Gain}_{\text{solve}})$ is both sound and complete.

### Finite Acyclicity
Every valid transition moves to an index strictly greater than $i$. The subproblem dependency graph is a directed acyclic graph (DAG) whose topological sort is precisely the reverse index order $n-1, n-2, \dots, 0$. Evaluating in this order guarantees no cycle can exist and every subproblem is queried only after being fully resolved.

---

## 6. Edge Cases & Anti-Patterns

### Edge Cases
1. **Single Question Exam ($n = 1$):** With only one question available, skipping gives $0$ and solving gives $\text{points}_0$. The algorithm correctly returns $\max(0, \text{points}_0) = \text{points}_0$ since points are strictly positive.
2. **Brainpower Exceeds Remaining Exam Length:** When $i + \text{brainpower}_i + 1 \ge n$, the subsequent state is out of bounds. Clamping or boundary testing guards against index-out-of-bounds exceptions, safely treating the downstream contribution as $0$.
3. **Zero Brainpower ($\text{brainpower}_i = 0$):** Solving question $i$ advances directly to $i + 1$. In this case, both solving and skipping look at $DP[i+1]$, and solving always dominates because $\text{points}_i > 0$.
4. **Large Cumulative Points:** With $n \le 10^5$ and each question worth up to $10^9$ points, total points can reach $10^{14}$. State values must use 64-bit integer types to prevent arithmetic overflow.

### Common Anti-Patterns
- **Greedy Selection by Highest Points:** Question $1$ and $2$ offer $4$ points each, whereas question $0$ offers only $3$ points. A greedy choice might pick question $1$ or $2$ for an immediate gain of $4$, missing the combined total of $3 + 2 = 5$ obtained by choosing question $0$ followed by question $3$.
- **Greedy Selection by Efficiency Ratio ($\text{points} / \text{brainpower}$):** Ratio heuristics fail because brainpower costs only apply when within bounds, and discrete skipping patterns create non-linear packing interactions.
- **Top-Down Recursion Without Memoization:** Unmemoized branch exploration creates an $O(2^n)$ call tree that times out for $n > 30$.
- **Forward DP with Dynamic Sparse State Updates:** Updating future states from the front requires scattered writes and range-lookup data structures. Backward DP simplifies the problem to two static reads per cell.

---

## 7. Complexity Analysis

### Time Complexity
- The backward loop iterates exactly $n$ times, from $i = n - 1$ down to $0$.
- In each iteration:
  - Reading $DP[i + 1]$ requires $O(1)$ time.
  - Computing the jump index $j = i + \text{brainpower}_i + 1$ and conditionally reading $DP[j]$ requires $O(1)$ time.
  - Taking the maximum of the two candidate values requires $O(1)$ time.
- Total time complexity is strictly $O(n)$, which comfortably handles the upper bound of $n = 10^5$ within a few milliseconds.

### Auxiliary Space Complexity
- A 1D array of size $n + 1$ stores the suffix optimal scores $DP[0 \dots n]$.
- Total auxiliary space complexity is $O(n)$.
- Note: Because jump targets $i + \text{brainpower}_i + 1$ can point arbitrarily far ahead into the array, the DP state cannot be reduced to a small sliding window of $O(1)$ variables without retaining prior values.
