# Guided Example: Maximum Subarray

We trace the step-by-step execution of Kadane's dynamic programming algorithm on a representative integer array:

- **Input:** $\text{nums} = [-2, 1, -3, 4, -1, 2, 1, -5, 4]$
- **Required output:** $6$

This instance demonstrates local prefix restart decisions ($\max(\text{nums}[i], \text{cur} + \text{nums}[i])$), tracking the contiguous subarray interval, updating the global maximum, and avoiding the all-negative number initialization pitfall.

---

## 1. Instance & Teaching Goal

Given an integer array $\text{nums}$ of length $N = 9$:
$$
[-2, 1, -3, 4, -1, 2, 1, -5, 4]
$$
we must find the contiguous subarray (containing at least one number) which has the largest sum, and return its sum.

A naive algorithm checks all $\frac{N(N+1)}{2}$ subarrays in $O(N^2)$ time. Kadane's algorithm computes the maximum contiguous subarray in a single pass ($O(N)$ time, $O(1)$ space) by recognizing that a prefix with a negative running sum can never contribute positively to any subsequent subarray.

For this instance, the optimal contiguous subarray is:
$$
[4, -1, 2, 1] \implies 4 + (-1) + 2 + 1 = 6
$$
spanning indices $3$ through $6$.

---

## 2. Conceptual Foundation & Invariants

### Kadane's Recurrence Relation
Let $DP[i]$ be the maximum subarray sum that **ends exactly at index $i$**.
At each index $i$, we have two choices:
1. **Extend:** Append $\text{nums}[i]$ to the best subarray ending at $i - 1$ ($\implies DP[i-1] + \text{nums}[i]$).
2. **Restart:** Start a brand-new subarray at index $i$ ($\implies \text{nums}[i]$).

Combining both:
$$
DP[i] = \max(\text{nums}[i], \, DP[i-1] + \text{nums}[i]) = \text{nums}[i] + \max(0, \, DP[i-1])
$$

The global maximum across all possible ending positions is:
$$
\text{max\_so\_far} = \max_{0 \le i < N} DP[i]
$$

### Space Optimization ($O(1)$ Auxiliary Memory)
Because $DP[i]$ depends only on $DP[i-1]$, we maintain a single scalar variable `current_sum`:
$$
\text{current\_sum} \leftarrow \max(\text{nums}[i], \, \text{current\_sum} + \text{nums}[i])
$$
$$
\text{max\_sum} \leftarrow \max(\text{max\_sum}, \, \text{current\_sum})
$$

> **Invariant.** At the end of iteration $i$, `current_sum` holds the maximum sum of any contiguous subarray ending at $i$, and `max_sum` holds the maximum sum among all subarrays within $\text{nums}[0 \dots i]$.

---

## 3. Step-by-Step Worked Execution

We trace $\text{nums} = [-2, 1, -3, 4, -1, 2, 1, -5, 4]$:

### Initialization
- $\text{current\_sum} = \text{nums}[0] = -2$
- $\text{max\_sum} = \text{nums}[0] = -2$

---

### Iteration Trace

- **Index 0 ($\text{nums}[0] = -2$):** Base value: $\text{current\_sum} = -2$, $\text{max\_sum} = -2$.
- **Index 1 ($\text{nums}[1] = 1$):**
  - Extend vs Restart: $\max(1, -2 + 1) = \max(1, -1) = 1$.
  - Decision: Prior sum was negative; restart at index 1!
  - $\text{current\_sum} = 1$, $\text{max\_sum} = \max(-2, 1) = 1$.
- **Index 2 ($\text{nums}[2] = -3$):**
  - $\max(-3, 1 - 3) = \max(-3, -2) = -2$.
  - $\text{current\_sum} = -2$, $\text{max\_sum} = 1$.
- **Index 3 ($\text{nums}[3] = 4$):**
  - $\max(4, -2 + 4) = \max(4, 2) = 4$.
  - Decision: Prior sum was negative; restart at index 3!
  - Subarray starting anchor set to index 3.
  - $\text{current\_sum} = 4$, $\text{max\_sum} = \max(1, 4) = 4$.
- **Index 4 ($\text{nums}[4] = -1$):**
  - $\max(-1, 4 - 1) = \max(-1, 3) = 3$.
  - Decision: Running sum remains positive ($3 > 0$); absorb the $-1$ penalty.
  - $\text{current\_sum} = 3$, $\text{max\_sum} = 4$.
- **Index 5 ($\text{nums}[5] = 2$):**
  - $\max(2, 3 + 2) = \max(2, 5) = 5$.
  - $\text{current\_sum} = 5$, $\text{max\_sum} = \max(4, 5) = 5$.
- **Index 6 ($\text{nums}[6] = 1$):**
  - $\max(1, 5 + 1) = \max(1, 6) = 6$.
  - $\text{current\_sum} = 6$, $\text{max\_sum} = \max(5, 6) = \mathbf{6}$!
  - *(Peak subarray achieved: $[4, -1, 2, 1]$)*.
- **Index 7 ($\text{nums}[7] = -5$):**
  - $\max(-5, 6 - 5) = \max(-5, 1) = 1$.
  - $\text{current\_sum} = 1$, $\text{max\_sum} = 6$.
- **Index 8 ($\text{nums}[8] = 4$):**
  - $\max(4, 1 + 4) = \max(4, 5) = 5$.
  - $\text{current\_sum} = 5$, $\text{max\_sum} = 6$.

Termination. Final maximum subarray sum is $6$.

---

## 4. Complete Execution Trace

| Index $i$ | Value $\text{nums}[i]$ | Extension ($\text{cur} + \text{val}$) | Restart ($\text{val}$) | New $\text{current\_sum}$ | Active Subarray Window | New $\text{max\_sum}$ |
|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| 0 | -2 | - | -2 | -2 | `[-2]` | -2 |
| 1 | 1 | -1 | 1 | 1 | `[1]` | 1 |
| 2 | -3 | -2 | -3 | -2 | `[1, -3]` | 1 |
| 3 | 4 | 2 | 4 | 4 | `[4]` | 4 |
| 4 | -1 | 3 | -1 | 3 | `[4, -1]` | 4 |
| 5 | 2 | 5 | 2 | 5 | `[4, -1, 2]` | 5 |
| 6 | 1 | 6 | 1 | **6** | `[4, -1, 2, 1]` | **6 (Max)** |
| 7 | -5 | 1 | -5 | 1 | `[4, -1, 2, 1, -5]` | 6 |
| 8 | 4 | 5 | 4 | 5 | `[4, -1, 2, 1, -5, 4]` | 6 |

---

## 5. Algorithmic Correctness

**Soundness.** Let $S[j \dots i]$ be the optimal subarray ending at $i$. If $j < i$, the prefix $S[j \dots i-1]$ must have a strictly positive sum; otherwise, dropping that prefix would produce a larger sum $S[i]$, contradicting optimality. Hence, dropping negative prefixes via $\max(\text{nums}[i], \text{cur} + \text{nums}[i])$ provably maintains the maximal sum ending at every index.

**Completeness.** Every valid non-empty subarray ends at some index $i \in [0, N - 1]$. By computing the maximal subarray sum for each possible ending index and taking their global maximum, no subarray can exceed the returned result.

---

## 6. Traps This Instance Exposes

- **All-Negative Array Pitfall:** If $\text{nums} = [-3, -1, -5]$ and $\text{max\_sum}$ is initialized to $0$, the algorithm will return $0$, which is wrong because an empty subarray is not allowed. Initializing $\text{current\_sum} = \text{nums}[0]$ and $\text{max\_sum} = \text{nums}[0]$ handles all-negative inputs correctly (returning $-1$).
- **Divide-and-Conquer Alternative:** The problem can also be solved in $O(N)$ time via divide-and-conquer by maintaining four metrics for each segment: total sum, max prefix sum, max suffix sum, and max contiguous sum. Kadane's algorithm achieves the same result iteratively with far simpler code.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N = |\text{nums}|$. The algorithm inspects each element exactly once in a single linear loop.
- **Auxiliary Space Complexity:** $O(1)$. Kadane's algorithm requires only two scalar variables (`current_sum` and `max_sum`).