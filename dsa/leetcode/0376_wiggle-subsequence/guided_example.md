# Guided Example: Wiggle Subsequence

We trace the step-by-step dual-state dynamic programming formulation ($f[i]$ for upward-ending wiggles, $g[i]$ for downward-ending wiggles), alternating sign transition conditions ($nums[j] < nums[i] \implies g[j] + 1$, $nums[j] > nums[i] \implies f[j] + 1$), and peak/valley counting on representative integer sequences:

- **Input:** $nums = [1, 7, 4, 9, 2, 5]$
- **Required output:** $6$
  - Step-by-step difference signs between adjacent elements:
    - $1 \to 7$: $+6$ (Upward)
    - $7 \to 4$: $-3$ (Downward)
    - $4 \to 9$: $+5$ (Upward)
    - $9 \to 2$: $-7$ (Downward)
    - $2 \to 5$: $+3$ (Upward)
  - Sign sequence: $[+, -, +, -, +]$ alternates strictly at every step!
  - Entire array of length 6 forms a valid wiggle sequence
  - Dual-state DP evolution:
    - At $i = 1$ ($nums[1] = 7$): $f[1] = g[0] + 1 = 2$
    - At $i = 2$ ($nums[2] = 4$): $g[2] = f[1] + 1 = 3$
    - At $i = 3$ ($nums[3] = 9$): $f[3] = g[2] + 1 = 4$
    - At $i = 4$ ($nums[4] = 2$): $g[4] = f[3] + 1 = 5$
    - At $i = 5$ ($nums[5] = 5$): $f[5] = g[4] + 1 = \mathbf{6}$
  - Longest wiggle subsequence length: $\mathbf{6}$
- **Plateau / Monotonic Run:** $nums = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8] \implies 7$
- **All Identical Elements:** $nums = [3, 3, 3, 3] \implies 1$
- **Two Elements:** $nums = [1, 2] \implies 2$

This instance demonstrates alternating parity / polarity dynamic programming, mathematically proves why tracking the last transition direction decouples alternating subproblems, explores the connection to greedy local extrema extraction, and derives $O(N^2)$ and $O(N)$ complexity models.

---

## 1. Instance & Teaching Goal

Given an integer array $nums = [1, 7, 4, 9, 2, 5]$:
A **wiggle sequence** is a sequence where the differences between successive numbers strictly alternate between strictly positive and strictly negative.
Find the length of the longest subsequence that forms a wiggle sequence:

```text
Sequence: [ 1,   7,   4,   9,   2,   5 ]
Diffs:       +6   -3   +5   -7   +3
Signs:       +    -    +    -    +  (Strictly Alternating!)

Visual Contour:
      9
     / \
    7   \       5
   /     4     /
  1       \   /
           2

Every turning point (peak/valley) can be included.
Max Wiggle Subsequence Length: 6
```

---

## 2. Conceptual Foundation & Invariants

### 1. Dual DP State Definitions:
For each index $i \in [0, n - 1]$:
- $f[i]$: Length of the longest wiggle subsequence ending at $nums[i]$ where the **last transition was upward** ($nums[j] < nums[i]$).
- $g[i]$: Length of the longest wiggle subsequence ending at $nums[i]$ where the **last transition was downward** ($nums[j] > nums[i]$).

### 2. Base Initialization:
Every individual element is trivially a wiggle sequence of length 1:
$$
f[i] = 1, \quad g[i] = 1 \quad \text{for all } i \in [0, n - 1]
$$

### 3. Transition Recurrence:
For each $i \ge 1$ and every predecessor $j < i$:
1. If $nums[j] < nums[i]$ (Upward step):
   To alternate, the predecessor at $j$ must have ended with a **downward** step:
   $$
   f[i] = \max(f[i], \; g[j] + 1)
   $$
2. If $nums[j] > nums[i]$ (Downward step):
   To alternate, the predecessor at $j$ must have ended with an **upward** step:
   $$
   g[i] = \max(g[i], \; f[j] + 1)
   $$
3. If $nums[j] == nums[i]$: difference is zero, no valid transition.

Global maximum:
$$
ans = \max_{0 \le i < n} \big(\max(f[i], g[i])\big)
$$

> **Invariant.** For all $i$, $f[i]$ and $g[i]$ accurately represent the maximum alternating sequence lengths terminating at $nums[i]$ with positive and negative slope respectively.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [1, 7, 4, 9, 2, 5]$ ($n = 6$):
Initial: $f = [1, 1, 1, 1, 1, 1], g = [1, 1, 1, 1, 1, 1], ans = 1$.

---

### Step 1: Index $i = 1$ ($nums[1] = 7$)
- Compare with $j = 0$ ($nums[0] = 1$):
  $$
  1 < 7 \implies \text{Upward step}
  $$
  $$
  f[1] = \max(1, \; g[0] + 1) = \max(1, \; 1 + 1) = \mathbf{2}
  $$
- States at $i = 1$: $f[1] = 2, g[1] = 1$.
- Best so far: $ans = \max(1, 2, 1) = \mathbf{2}$.

---

### Step 2: Index $i = 2$ ($nums[2] = 4$)
- Compare with $j = 0$ ($nums[0] = 1$):
  - $1 < 4 \implies f[2] = \max(1, g[0] + 1) = 2$.
- Compare with $j = 1$ ($nums[1] = 7$):
  - $7 > 4 \implies \text{Downward step}$.
  $$
  g[2] = \max(1, \; f[1] + 1) = \max(1, \; 2 + 1) = \mathbf{3}
  $$
- States at $i = 2$: $f[2] = 2, g[2] = 3$.
- Subsequence represented by $g[2]$: $[1, 7, 4]$ (Length 3).
- Best so far: $ans = \max(2, 2, 3) = \mathbf{3}$.

---

### Step 3: Index $i = 3$ ($nums[3] = 9$)
- Predecessors tested:
  - From $j = 2$ ($nums[2] = 4$): $4 < 9 \implies$ upward step.
  $$
  f[3] = \max(1, \; g[2] + 1) = \max(1, \; 3 + 1) = \mathbf{4}
  $$
- States at $i = 3$: $f[3] = 4, g[3] = 1$.
- Subsequence: $[1, 7, 4, 9]$ (Length 4).
- Best so far: $ans = \mathbf{4}$.

---

### Step 4: Index $i = 4$ ($nums[4] = 2$)
- Predecessors tested:
  - From $j = 3$ ($nums[3] = 9$): $9 > 2 \implies$ downward step.
  $$
  g[4] = \max(1, \; f[3] + 1) = \max(1, \; 4 + 1) = \mathbf{5}
  $$
- States at $i = 4$: $f[4] = 2, g[4] = 5$.
- Subsequence: $[1, 7, 4, 9, 2]$ (Length 5).
- Best so far: $ans = \mathbf{5}$.

---

### Step 5: Index $i = 5$ ($nums[5] = 5$)
- Predecessors tested:
  - From $j = 4$ ($nums[4] = 2$): $2 < 5 \implies$ upward step.
  $$
  f[5] = \max(1, \; g[4] + 1) = \max(1, \; 5 + 1) = \mathbf{6}
  $$
- States at $i = 5$: $f[5] = 6, g[5] = 1$.
- Subsequence: $[1, 7, 4, 9, 2, 5]$ (Length 6).
- Best so far: $ans = \mathbf{6}$.

---

### Step 6: Final Result
Loop completes across all elements. Maximum wiggle length:
$$
\mathbf{6}
$$

---

## 4. Complete Execution Trace

```text
nums = [1, 7, 4, 9, 2, 5]

i=1 (val=7): j=0 (val=1): 1 < 7 -> f[1] = g[0] + 1 = 2
i=2 (val=4): j=1 (val=7): 7 > 4 -> g[2] = f[1] + 1 = 3
i=3 (val=9): j=2 (val=4): 4 < 9 -> f[3] = g[2] + 1 = 4
i=4 (val=2): j=3 (val=9): 9 > 2 -> g[4] = f[3] + 1 = 5
i=5 (val=5): j=4 (val=2): 2 < 5 -> f[5] = g[4] + 1 = 6

Final Max Wiggle Length: 6
```

| Index $i$ | Value $nums[i]$ | Dominant Transition From $j$ | Step Direction | Upward State $f[i]$ | Downward State $g[i]$ | Global Max $ans$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 1 | Base | - | 1 | 1 | 1 |
| 1 | 7 | $j = 0$ ($1 < 7$) | Upward | $\mathbf{2}$ | 1 | 2 |
| 2 | 4 | $j = 1$ ($7 > 4$) | Downward | 2 | $\mathbf{3}$ | 3 |
| 3 | 9 | $j = 2$ ($4 < 9$) | Upward | $\mathbf{4}$ | 1 | 4 |
| 4 | 2 | $j = 3$ ($9 > 2$) | Downward | 2 | $\mathbf{5}$ | 5 |
| **5** | **5** | **$j = 4$ ($2 < 5$)** | **Upward** | **$\mathbf{6}$** | **1** | **$\mathbf{6}$ (Final)** |

---

## 5. Algorithmic Correctness

**Soundness.** A wiggle sequence requires strictly alternating differences. By maintaining separate states for upward and downward endings, an upward step to $nums[i]$ can only transition from a subsequence ending with a downward step ($g[j]$), guaranteeing that the difference signs alternate at every position.

**Completeness.** For every index $i$, all previous positions $j < i$ are evaluated. Since dynamic programming exhaustively tests all valid predecessors for both upward and downward transitions, no longer alternating subsequence can exist.

---

## 6. Traps This Instance Exposes

- **Flat Consecutive Equal Values:** When $nums[j] == nums[i]$, the difference is $0$, which is neither positive nor negative. These steps must be strictly ignored and cannot contribute to either $f[i]$ or $g[i]$.
- **Greedy Equivalence:** A wiggle sequence corresponds to picking all local extrema (peaks and valleys). This allows a linear $O(N)$ space-optimized greedy algorithm (`up` and `down` variables updated on each adjacent step).
- **Single Element Base Case:** If $\text{len}(nums) = 1$, the loops do not run and the function directly returns $ans = 1$, as required by the definition.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^2)$, where $N$ is the length of `nums`. The outer loop runs $N$ times, and the inner loop runs $i$ times, executing $\frac{N(N-1)}{2}$ constant-time comparisons. (Can be optimized to $O(N)$ with greedy peak/valley counting).
- **Auxiliary Space Complexity:** $O(N)$ auxiliary space for arrays $f$ and $g$.
