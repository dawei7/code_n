# Guided Example: House Robber

We trace the step-by-step non-adjacent dynamic programming recurrence and constant-space rolling variables on representative street loot arrays:

- **Input:** $\text{nums} = [2, 7, 9, 3, 1]$
- **Required output:** $12$ (Rob house 0 [$2$], house 2 [$9$], and house 4 [$1$] $\implies 2 + 9 + 1 = 12$)
- **Alternating Equality Instance:** $\text{nums} = [1, 2, 3, 1] \implies 4$ (Rob house 0 and house 2 $\implies 1 + 3 = 4$)
- **Two House Instance:** $\text{nums} = [2, 1] \implies 2$ (Take maximum of the two)
- **Single House Instance:** $\text{nums} = [5] \implies 5$

This instance demonstrates the foundational non-adjacent selection optimal substructure ($DP[i] = \max(DP[i-1], DP[i-2] + x)$), proves why rolling state variables reduce memory from $O(N)$ to $O(1)$, and executes in strictly $O(N)$ linear time.

---

## 1. Instance & Teaching Goal

Given an integer array representing the amount of money stored in a row of houses along a street:
$$
\text{nums} = [2, 7, 9, 3, 1]
$$
Determine the maximum cash you can rob tonight, subject to the security constraint that **adjacent houses cannot be robbed on the same night**.

Exploring feasible non-adjacent combinations:
- Rob houses $0, 2, 4$: money $= 2 + 9 + 1 = \mathbf{12}$.
- Rob houses $1, 3$: money $= 7 + 3 = 10$.
- Rob houses $0, 3$: money $= 2 + 3 = 5$.
- Rob houses $1, 4$: money $= 7 + 1 = 8$.
The global maximum is $12$.

Evaluating all $2^N$ subsets takes exponential time.
However, deciding whether to rob house $i$ depends only on the optimal answers of smaller prefixes, demonstrating **optimal substructure**.

---

## 2. Conceptual Foundation & Invariants

### State Formulation & Recurrence
Let $DP[i]$ be the maximum money that can be robbed from the prefix of houses $\text{nums}[0 \dots i]$.

At house $i$ with loot $x = \text{nums}[i]$, there are strictly two mutually exclusive choices:
1. **Skip House $i$:**
   No money is taken from house $i$. The optimal yield is simply the maximum loot attainable from the prefix ending at house $i-1$:
   $$
   \text{gain}_{\text{skip}} = DP[i-1]
   $$
2. **Rob House $i$:**
   We gain $\text{nums}[i]$. Because adjacent houses trigger alarms, house $i-1$ must not be robbed. We add $\text{nums}[i]$ to the optimal loot attainable from the prefix ending at house $i-2$:
   $$
   \text{gain}_{\text{rob}} = DP[i-2] + \text{nums}[i]
   $$

Taking the optimal choice:
$$
DP[i] = \max(DP[i-1], \, DP[i-2] + \text{nums}[i])
$$

### Rolling Space Optimization ($O(1)$ Auxiliary Space)
Notice that computing $DP[i]$ requires only the two immediately preceding values, $DP[i-1]$ and $DP[i-2]$.
We replace the $O(N)$ array with two scalar variables:
- `prev2` $\equiv DP[i-2]$ (initialized to $0$)
- `prev1` $\equiv DP[i-1]$ (initialized to $0$)

For each house $x \in \text{nums}$:
$$
\text{current} = \max(\text{prev1}, \, \text{prev2} + x)
$$
$$
\text{prev2} \leftarrow \text{prev1}, \quad \text{prev1} \leftarrow \text{current}
$$

> **Invariant.** At the start of processing house $i$, `prev1` holds the exact optimal answer for prefix $0 \dots i-1$, and `prev2` holds the optimal answer for prefix $0 \dots i-2$.

---

## 3. Step-by-Step Worked Execution

We trace the rolling variables across $\text{nums} = [2, 7, 9, 3, 1]$:

### Initialization:
- $\text{prev2} = 0$
- $\text{prev1} = 0$

---

### House 0 ($x = 2$):
- Choice 1 (Skip): $\text{prev1} = 0$.
- Choice 2 (Rob): $\text{prev2} + x = 0 + 2 = 2$.
- $\text{current} = \max(0, 2) = \mathbf{2}$.
- State shift: $\text{prev2} \leftarrow 0, \quad \text{prev1} \leftarrow 2$.

---

### House 1 ($x = 7$):
- Choice 1 (Skip): $\text{prev1} = 2$.
- Choice 2 (Rob): $\text{prev2} + x = 0 + 7 = 7$.
- $\text{current} = \max(2, 7) = \mathbf{7}$.
- State shift: $\text{prev2} \leftarrow 2, \quad \text{prev1} \leftarrow 7$.

---

### House 2 ($x = 9$):
- Choice 1 (Skip): $\text{prev1} = 7$.
- Choice 2 (Rob): $\text{prev2} + x = 2 + 9 = 11$ *(Robbing house 0 and house 2)*.
- $\text{current} = \max(7, 11) = \mathbf{11}$.
- State shift: $\text{prev2} \leftarrow 7, \quad \text{prev1} \leftarrow 11$.

---

### House 3 ($x = 3$):
- Choice 1 (Skip): $\text{prev1} = 11$.
- Choice 2 (Rob): $\text{prev2} + x = 7 + 3 = 10$.
- $\text{current} = \max(11, 10) = \mathbf{11}$ *(Skipping house 3 is better than taking it)*.
- State shift: $\text{prev2} \leftarrow 11, \quad \text{prev1} \leftarrow 11$.

---

### House 4 ($x = 1$):
- Choice 1 (Skip): $\text{prev1} = 11$.
- Choice 2 (Rob): $\text{prev2} + x = 11 + 1 = 12$ *(Robbing house 4 adds to loot 11 from house 2)*.
- $\text{current} = \max(11, 12) = \mathbf{12}$.
- State shift: $\text{prev2} \leftarrow 11, \quad \text{prev1} \leftarrow 12$.

Loop completes. The final maximum cash robbed is $\mathbf{12}$.

---

## 4. Complete Execution Trace

```text
Houses: [ 2,  7,  9,  3,  1 ]

House 0 (val=2): max(0,  0+2) =  2  -> prev2=0,  prev1=2
House 1 (val=7): max(2,  0+7) =  7  -> prev2=2,  prev1=7
House 2 (val=9): max(7,  2+9) = 11  -> prev2=7,  prev1=11
House 3 (val=3): max(11, 7+3) = 11  -> prev2=11, prev1=11
House 4 (val=1): max(11, 11+1)= 12  -> prev2=11, prev1=12

Final Max Loot: 12
```

| House Index $i$ | House Cash $\text{nums}[i]$ | $\text{prev2}$ ($DP[i-2]$) | $\text{prev1}$ ($DP[i-1]$) | Rob Option ($\text{prev2} + x$) | Optimal Choice $\text{current}$ | Decision Made |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| Init | - | 0 | 0 | - | 0 | Base configuration |
| 0 | 2 | 0 | 0 | $0 + 2 = 2$ | 2 | Rob House 0 |
| 1 | 7 | 0 | 2 | $0 + 7 = 7$ | 7 | Rob House 1 |
| 2 | 9 | 2 | 7 | $2 + 9 = 11$ | 11 | Rob House 2 |
| 3 | 3 | 7 | 11 | $7 + 3 = 10$ | 11 | Skip House 3 |
| **4** | **1** | **11** | **11** | **$11 + 1 = 12$** | **12** | **Rob House 4 $\implies$ Final: 12** |

---

## 5. Algorithmic Correctness

**Soundness.** Any valid robbery schedule is a subset of indices containing no two adjacent integers. In any optimal subset for prefix $i$, house $i$ is either included or excluded. If excluded, the subset restricted to prefix $i-1$ is valid and optimal for $i-1$. If included, house $i-1$ is omitted, making the subset restricted to prefix $i-2$ valid and optimal for $i-2$. Therefore, taking $\max(DP[i-1], DP[i-2] + \text{nums}[i])$ strictly computes the optimum.

**Completeness.** The induction advances through all houses $0 \dots N-1$ topologically, exploring both inclusion and exclusion at every step.

---

## 6. Traps This Instance Exposes

- **Greedy Alternation Trap:** Picking all even indices ($2 + 9 + 1 = 12$) or all odd indices ($7 + 3 = 10$) fails on inputs like `[2, 1, 1, 2]`. The optimal schedule robs index 0 and index 3 (loot $= 2 + 2 = 4$), which requires skipping *two* consecutive houses (indices 1 and 2). The DP handles arbitrary gap sizes naturally.
- **Empty or Single House Input:** If $N = 1$, the loop executes once and returns $\text{nums}[0]$, requiring no special boundary branching.
- **Negative Values:** Problem constraints guarantee non-negative cash ($\text{nums}[i] \ge 0$), meaning robbing a house never decreases total cash.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of houses. The algorithm evaluates each house exactly once, performing constant-time arithmetic and comparisons.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary memory, storing only the scalar rolling variables `prev1`, `prev2`, and `current`.