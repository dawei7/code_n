# Guided Example: House Robber II

We trace the step-by-step circular graph boundary decomposition, linear dynamic programming recurrence, and rolling scalar state transitions on representative circular house neighborhoods:

- **Input:** $\text{nums} = [1, 2, 3, 1]$
- **Required output:** $4$ (Rob house 0 with value $1$ and house 2 with value $3$; $1 + 3 = 4$)
- **Circular Adjacency Conflict Instance:** $\text{nums} = [2, 3, 2] \implies 3$ (House 0 and House 2 cannot both be robbed because they touch in a circle; max is house 1 with value $3$)
- **Single House Instance:** $\text{nums} = [1] \implies 1$ (No circular conflict possible)
- **Three House Contrast:** $\text{nums} = [1, 2, 3] \implies 3$ ($\max(\text{rob}([1, 2]), \text{rob}([2, 3])) = \max(2, 3) = 3$)

This instance demonstrates breaking circular dependency cycles through domain decomposition into two linear subproblems ($\text{nums}[0:N-1]$ and $\text{nums}[1:N]$), proves why at least one boundary house must remain unrobbed, applies rolling memory DP, and runs in strictly $O(N)$ time and $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given houses arranged in a **circle** with values $\text{nums} = [1, 2, 3, 1]$ ($N = 4$):
- House 0 is adjacent to House 1 and House 3 (the last house).
- House 3 is adjacent to House 2 and House 0.
Robbing two adjacent houses triggers the security alarm.
Compute the maximum loot obtainable without triggering an alarm.

In the linear House Robber problem (LeetCode 198), House 0 and House $N - 1$ are independent and can both be chosen.
In the circular configuration, House 0 and House $N - 1$ are **adjacent neighbors**. They can never be robbed together!
This constraint forces a binary partition:
- **Case 1 (Do not rob House $N - 1$):** We may freely consider houses in the range $[0, N - 2]$.
- **Case 2 (Do not rob House $0$):** We may freely consider houses in the range $[1, N - 1]$.
Because any valid robbery plan cannot include both house $0$ and house $N - 1$, the global optimum is simply:
$$
\text{Global Maximum} = \max\Big(\text{rob\_linear}(\text{nums}[0 : N-1]), \; \text{rob\_linear}(\text{nums}[1 : N])\Big)
$$
Both subproblems are standard linear dynamic programs!

---

## 2. Conceptual Foundation & Invariants

### Linear Dynamic Programming Sub-Recurrence
For a linear subarray $H = [h_0, h_1, \dots, h_{k-1}]$:
Let $DP[i]$ be the maximum money robbed from prefix $H[0 \dots i]$:
$$
DP[i] = \max\big(DP[i-1], \; DP[i-2] + H[i]\big)
$$
- **Option A (Skip house $i$):** Total is $DP[i-1]$.
- **Option B (Rob house $i$):** Total is $DP[i-2] + H[i]$ (since house $i-1$ cannot be robbed).

### Space Optimization via Rolling Variables:
Maintain two scalar variables:
- `prev1`: represents $DP[i-1]$ (optimal answer up to previous house).
- `prev2`: represents $DP[i-2]$ (optimal answer up to two houses prior).

For each house $x$:
$$
\text{temp} = \max(\text{prev1}, \; \text{prev2} + x), \quad \text{prev2} \leftarrow \text{prev1}, \quad \text{prev1} \leftarrow \text{temp}
$$

> **Invariant.** For any circle of size $N \ge 2$, at least one of the boundary endpoints $\{0, N - 1\}$ must be excluded from the stolen subset. The union of Case 1 and Case 2 covers all valid subsets.

---

## 3. Step-by-Step Worked Execution

We evaluate $\text{nums} = [1, 2, 3, 1]$ ($N = 4$):

### Base Case Check:
$N = 4 > 1$. Decompose into two linear slices:
- **Slice 1 (Exclude House 3):** $H_1 = [1, 2, 3]$ (Indices $0 \dots 2$).
- **Slice 2 (Exclude House 0):** $H_2 = [2, 3, 1]$ (Indices $1 \dots 3$).

---

### Evaluating Slice 1: $H_1 = [1, 2, 3]$
Initialize $\text{prev1} = 0, \, \text{prev2} = 0$:

1. **Element $x = 1$:**
   - $\text{new\_val} = \max(0, \, 0 + 1) = 1$.
   - $\text{prev2} \leftarrow 0, \quad \text{prev1} \leftarrow 1$.
2. **Element $x = 2$:**
   - $\text{new\_val} = \max(1, \, 0 + 2) = 2$.
   - $\text{prev2} \leftarrow 1, \quad \text{prev1} \leftarrow 2$.
3. **Element $x = 3$:**
   - $\text{new\_val} = \max(2, \, 1 + 3) = \mathbf{4}$ *(Rob houses with values $1$ and $3$)*.
   - $\text{prev2} \leftarrow 2, \quad \text{prev1} \leftarrow 4$.

Max for Slice 1: $\mathbf{4}$.

---

### Evaluating Slice 2: $H_2 = [2, 3, 1]$
Initialize $\text{prev1} = 0, \, \text{prev2} = 0$:

1. **Element $x = 2$:**
   - $\text{new\_val} = \max(0, \, 0 + 2) = 2$.
   - $\text{prev2} \leftarrow 0, \quad \text{prev1} \leftarrow 2$.
2. **Element $x = 3$:**
   - $\text{new\_val} = \max(2, \, 0 + 3) = 3$.
   - $\text{prev2} \leftarrow 2, \quad \text{prev1} \leftarrow 3$.
3. **Element $x = 1$:**
   - $\text{new\_val} = \max(3, \, 2 + 1) = \mathbf{3}$ *(Rob house with value $3$)*.
   - $\text{prev2} \leftarrow 3, \quad \text{prev1} \leftarrow 3$.

Max for Slice 2: $\mathbf{3}$.

---

### Combining Cases:
$$
\text{Total Maximum} = \max(4, 3) = \mathbf{4}
$$

---

## 4. Complete Execution Trace

```text
Circular Array: [1, 2, 3, 1]

Subproblem 1: nums[0:3] = [1, 2, 3] (Exclude last house)
  x = 1: max(0, 0+1) = 1 -> prev2=0, prev1=1
  x = 2: max(1, 0+2) = 2 -> prev2=1, prev1=2
  x = 3: max(2, 1+3) = 4 -> prev2=2, prev1=4
  Result 1 = 4

Subproblem 2: nums[1:4] = [2, 3, 1] (Exclude first house)
  x = 2: max(0, 0+2) = 2 -> prev2=0, prev1=2
  x = 3: max(2, 0+3) = 3 -> prev2=2, prev1=3
  x = 1: max(3, 2+1) = 3 -> prev2=3, prev1=3
  Result 2 = 3

Global Answer = max(4, 3) = 4
```

| Subproblem Domain | Subarray Elements | Step $i$ | Element $x$ | Candidate Choices $\max(\text{prev1}, \text{prev2} + x)$ | Updated `prev1` |
|:---|:---:|:---:|:---:|:---:|:---:|
| **Slice 1** ($0 \dots N-2$) | $[1, 2, 3]$ | 0 | 1 | $\max(0, 0 + 1)$ | 1 |
| | | 1 | 2 | $\max(1, 0 + 2)$ | 2 |
| | | 2 | 3 | $\max(2, 1 + 3)$ | **4 (Best Slice 1)** |
| **Slice 2** ($1 \dots N-1$) | $[2, 3, 1]$ | 0 | 2 | $\max(0, 0 + 2)$ | 2 |
| | | 1 | 3 | $\max(2, 0 + 3)$ | 3 |
| | | 2 | 1 | $\max(3, 2 + 1)$ | **3 (Best Slice 2)** |
| **Combined** | - | - | - | $\max(4, 3)$ | **4 (Global Optimal)** |

---

## 5. Algorithmic Correctness

**Soundness.** Any subset of houses chosen by Slice 1 does not contain house $N - 1$. Any subset chosen by Slice 2 does not contain house $0$. Therefore, no selected subset can simultaneously contain both house $0$ and house $N - 1$. Within each slice, the recurrence enforces non-adjacent selections, satisfying all alarm constraints.

**Completeness.** Any optimal valid robbery subset $S^*$ falls into at least one of three categories:
1. $S^*$ contains house $0$ (hence cannot contain house $N - 1$, subset of Slice 1).
2. $S^*$ contains house $N - 1$ (hence cannot contain house $0$, subset of Slice 2).
3. $S^*$ contains neither house $0$ nor house $N - 1$ (subset of both slices).
Because these three cases partition all possibilities, $\max(\text{Slice 1}, \text{Slice 2})$ is guaranteed to evaluate $S^*$.

---

## 6. Traps This Instance Exposes

- **Length 1 Array ($N = 1$):** When $N = 1$ (e.g. `nums = [1]`), slicing `nums[:-1]` and `nums[1:]` produces empty lists, returning $0$ instead of $1$! Guard with `if len(nums) == 1: return nums[0]`.
- **Length 2 Array ($N = 2$):** For `nums = [1, 2]`, the houses are adjacent. The algorithm evaluates $\max(\text{rob}([1]), \text{rob}([2])) = \max(1, 2) = 2$, correctly picking the larger single house.
- **Duplicate Memory Allocation:** Slicing creates two small subarrays of length $N - 1$. If $O(1)$ memory is strictly required, iterate over index ranges `range(0, n - 1)` and `range(1, n)` directly.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of houses. The linear robber function runs in $O(N)$ time and is executed exactly twice ($2 \times (N - 1) = O(N)$).
- **Auxiliary Space Complexity:** $O(1)$ auxiliary memory using rolling scalar variables.