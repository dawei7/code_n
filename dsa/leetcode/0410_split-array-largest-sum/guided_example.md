# Guided Example: Split Array Largest Sum

We trace the step-by-step binary search on the answer space, monotonicity validation via greedy sequential packing, interval contraction, and optimal partition synthesis on representative problem instances:

- **Input:** $nums = [7, 2, 5, 10, 8], \quad k = 2$
- **Required output:** `18`
  - Domain lower bound: $L = \max(nums) = 10$
  - Domain upper bound: $R = \sum(nums) = 32$
  - Bisection trace:
    - Step 1: Probe $M = 21 \implies$ Greedy parts: $[7, 2, 5]$ (sum 14), $[10, 8]$ (sum 18) $\implies 2 \le k$ (Feasible) $\implies R \leftarrow 21$
    - Step 2: Probe $M = 15 \implies$ Greedy parts: $[7, 2, 5]$ (sum 14), $[10]$ (sum 10), $[8]$ (sum 8) $\implies 3 > k$ (Infeasible) $\implies L \leftarrow 16$
    - Step 3: Probe $M = 18 \implies$ Greedy parts: $[7, 2, 5]$ (sum 14), $[10, 8]$ (sum 18) $\implies 2 \le k$ (Feasible) $\implies R \leftarrow 18$
    - Step 4: Probe $M = 17 \implies$ Greedy parts: $[7, 2, 5]$ (sum 14), $[10]$ (sum 10), $[8]$ (sum 8) $\implies 3 > k$ (Infeasible) $\implies L \leftarrow 18$
  - Convergence: $L = R = 18 \implies$ Return `18`
- **Minimal Partition ($k = n$):** $nums = [1, 2, 3, 4], k = 4 \implies$ each element is its own part $\implies \max(nums) = \mathbf{4}$
- **Single Partition ($k = 1$):** $nums = [1, 2, 3, 4], k = 1 \implies$ whole array in one part $\implies \sum(nums) = \mathbf{10}$

This instance demonstrates inverting an optimization problem into a decision problem via predicate monotonicity, mathematically proves why greedy packing yields the minimal number of subarrays for any target maximum sum, and derives $O(N \log(\sum - \max))$ time and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $nums = [7, 2, 5, 10, 8]$ and an integer $k = 2$:
Split the array into $k$ non-empty contiguous subarrays such that the **largest sum** among these $k$ subarrays is **minimized**:

```text
Array: [7,  2,  5,  10,  8]

Possible 2-Partitions:
  [7] | [2, 5, 10, 8]       -> Subarray sums: 7 and 25  -> Max sum = 25
  [7, 2] | [5, 10, 8]       -> Subarray sums: 9 and 23  -> Max sum = 23
  [7, 2, 5] | [10, 8]       -> Subarray sums: 14 and 18 -> Max sum = 18  (Optimal!)
  [7, 2, 5, 10] | [8]       -> Subarray sums: 24 and 8  -> Max sum = 24

Optimal Maximum Subarray Sum: 18
```

### The Inversion Insight: From Search to Feasibility
Directly searching over all $\binom{N-1}{k-1}$ possible split points is computationally prohibitive.
Instead of trying to construct the optimal partition directly, we **invert the question**:
> *"Given a proposed maximum subarray sum $M$, can we partition $nums$ into $k$ or fewer contiguous subarrays such that no subarray exceeds $M$?"*

Because feasibility is strictly **monotonic** with respect to $M$:
- If a cap $M$ is feasible, any larger cap $M' > M$ is also feasible (relaxing the capacity cannot make packing impossible).
- If a cap $M$ is infeasible, any smaller cap $M' < M$ is also infeasible.

This monotonic step function allows us to use **binary search** over the range of possible answers $[L, R]$.

---

## 2. Conceptual Foundation & Invariants

### 1. The Search Space Range:
- **Lower Bound $L = \max(nums)$:** No subarray can contain less than a single element. If $M < \max(nums)$, the largest element cannot fit into any subarray. For $[7, 2, 5, 10, 8]$, $L = 10$.
- **Upper Bound $R = \sum(nums)$:** When $k = 1$, the entire array is placed into a single subarray with sum $\sum nums$. For $[7, 2, 5, 10, 8]$, $R = 7 + 2 + 5 + 10 + 8 = 32$.

Any feasible answer $M^*$ satisfies $10 \le M^* \le 32$.

### 2. Greedy Feasibility Predicate $P(M)$:
To determine whether a cap $M$ can partition $nums$ into at most $k$ subarrays:
1. Initialize running subarray sum $S = 0$ and subarray count $cnt = 1$.
2. Iterate through each element $x \in nums$:
   - If $S + x \le M$: add $x$ to the current subarray ($S \leftarrow S + x$).
   - If $S + x > M$: the current subarray is full. Close it, start a new subarray with $x$, and increment $cnt \leftarrow cnt + 1$.
3. Return `true` if $cnt \le k$, otherwise `false`.

> **Greedy Exchange Invariant.** Greedily filling each subarray until adding the next element would exceed $M$ always minimizes the total number of subarrays needed. If an optimal packing exists that makes an earlier cut, pushing elements from the right subarray into the left subarray never increases the total count.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [7, 2, 5, 10, 8], k = 2$ with initial bounds $L = 10, R = 32$:

---

### Iteration 1: $L = 10, R = 32$
- Midpoint probe:
  $$
  M = 10 + \lfloor (32 - 10) / 2 \rfloor = \mathbf{21}
  $$
- Greedy packing check with cap $M = 21$:
  - Start subarray 1:
    - Add $7 \implies S = 7 \le 21$
    - Add $2 \implies S = 9 \le 21$
    - Add $5 \implies S = 14 \le 21$
    - Add $10 \implies S = 24 > 21 \implies$ **Cut!** Close subarray 1 ($[7, 2, 5]$, sum 14).
  - Start subarray 2:
    - Add $10 \implies S = 10 \le 21$
    - Add $8 \implies S = 18 \le 21$
  - End of array. Total subarrays used: $cnt = 2$.
  - Feasibility: $cnt = 2 \le k = 2 \implies$ **Feasible (`true`)**.
- Update search range:
  Since $M = 21$ is achievable, the optimal answer could be $21$ or smaller:
  $$
  R \leftarrow M = \mathbf{21}
  $$

---

### Iteration 2: $L = 10, R = 21$
- Midpoint probe:
  $$
  M = 10 + \lfloor (21 - 10) / 2 \rfloor = \mathbf{15}
  $$
- Greedy packing check with cap $M = 15$:
  - Start subarray 1:
    - Add $7 \implies S = 7 \le 15$
    - Add $2 \implies S = 9 \le 15$
    - Add $5 \implies S = 14 \le 15$
    - Add $10 \implies S = 24 > 15 \implies$ **Cut!** Close subarray 1 ($[7, 2, 5]$, sum 14).
  - Start subarray 2:
    - Add $10 \implies S = 10 \le 15$
    - Add $8 \implies S = 18 > 15 \implies$ **Cut!** Close subarray 2 ($[10]$, sum 10).
  - Start subarray 3:
    - Add $8 \implies S = 8 \le 15$
  - End of array. Total subarrays used: $cnt = 3$.
  - Feasibility: $cnt = 3 > k = 2 \implies$ **Infeasible (`false`)**.
- Update search range:
  Since $M = 15$ requires 3 subarrays, any cap $\le 15$ also requires $> 2$ subarrays.
  $$
  L \leftarrow M + 1 = \mathbf{16}
  $$

---

### Iteration 3: $L = 16, R = 21$
- Midpoint probe:
  $$
  M = 16 + \lfloor (21 - 16) / 2 \rfloor = \mathbf{18}
  $$
- Greedy packing check with cap $M = 18$:
  - Start subarray 1:
    - Add $7 \implies S = 7 \le 18$
    - Add $2 \implies S = 9 \le 18$
    - Add $5 \implies S = 14 \le 18$
    - Add $10 \implies S = 24 > 18 \implies$ **Cut!** Close subarray 1 ($[7, 2, 5]$, sum 14).
  - Start subarray 2:
    - Add $10 \implies S = 10 \le 18$
    - Add $8 \implies S = 18 \le 18$
  - End of array. Total subarrays used: $cnt = 2$.
  - Feasibility: $cnt = 2 \le k = 2 \implies$ **Feasible (`true`)**.
- Update search range:
  $$
  R \leftarrow M = \mathbf{18}
  $$

---

### Iteration 4: $L = 16, R = 18$
- Midpoint probe:
  $$
  M = 16 + \lfloor (18 - 16) / 2 \rfloor = \mathbf{17}
  $$
- Greedy packing check with cap $M = 17$:
  - Start subarray 1:
    - Add $7 \implies S = 7 \le 17$
    - Add $2 \implies S = 9 \le 17$
    - Add $5 \implies S = 14 \le 17$
    - Add $10 \implies S = 24 > 17 \implies$ **Cut!** Close subarray 1 ($[7, 2, 5]$, sum 14).
  - Start subarray 2:
    - Add $10 \implies S = 10 \le 17$
    - Add $8 \implies S = 18 > 17 \implies$ **Cut!** Close subarray 2 ($[10]$, sum 10).
  - Start subarray 3:
    - Add $8 \implies S = 8 \le 17$
  - End of array. Total subarrays used: $cnt = 3$.
  - Feasibility: $cnt = 3 > k = 2 \implies$ **Infeasible (`false`)**.
- Update search range:
  $$
  L \leftarrow M + 1 = \mathbf{18}
  $$

---

### Convergence: $L = 18, R = 18$
The search interval collapsed to a single point:
$$
L = R = 18
$$
The minimal largest subarray sum is **18**.

---

## 4. Complete Execution Trace

| Iteration | Active Range $[L, R]$ | Midpoint Probe $M$ | Subarrays Formed | Subarray Count $cnt$ | Feasibility ($cnt \le 2$) | Next Range |
|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| **Init** | $[10, 32]$ | — | — | — | — | $[10, 32]$ |
| **1** | $[10, 32]$ | $21$ | $[7, 2, 5]$, $[10, 8]$ | $2$ | **True** (Feasible) | $[10, 21]$ |
| **2** | $[10, 21]$ | $15$ | $[7, 2, 5]$, $[10]$, $[8]$ | $3$ | **False** (Too tight) | $[16, 21]$ |
| **3** | $[16, 21]$ | $18$ | $[7, 2, 5]$, $[10, 8]$ | $2$ | **True** (Feasible) | $[16, 18]$ |
| **4** | $[16, 18]$ | $17$ | $[7, 2, 5]$, $[10]$, $[8]$ | $3$ | **False** (Too tight) | $[18, 18]$ |
| **Done** | $[18, 18]$ | — | Optimal partition: $[7, 2, 5]$ and $[10, 8]$ | — | **Converged** | **Result = 18** |

---

## 5. Boundary Cases & Failure Modes

- **$k = 1$:** The whole array must remain contiguous. Search range initializes with $L = \max(nums), R = \sum(nums)$. $L$ converges directly to $\sum(nums)$.
- **$k = N$:** Every element is its own subarray. The maximum subarray sum is simply $\max(nums)$. Feasibility check passes for all $M \ge \max(nums)$, converging to $L = \max(nums)$.
- **All Equal Elements ($[5, 5, 5, 5], k = 2$):** $L = 5, R = 20$. Pairs cleanly into $[5, 5]$ and $[5, 5]$ with max sum $10$.
- **Single Dominant Element ($[1, 1, 100, 1], k = 2$):** $L = 100$. Any cut requires 100 to be in one subarray, yielding $[1, 1, 100]$ or $[100, 1]$, with sum $102$ or $101$.

---

## 6. Traps & Common Anti-Patterns

- **Setting $L = 0$ instead of $\max(nums)$:** If $L < \max(nums)$, a probe $M$ could be smaller than an individual element. An element $x > M$ can never fit into any subarray, causing an infinite loop or incorrect count unless explicitly checked. Setting $L = \max(nums)$ guarantees every single element fits.
- **Attempting 2D Dynamic Programming ($O(k \cdot N^2)$):** Classic DP $DP[i][j] = \min_p (\max(DP[i-1][p], \text{sum}(p\dots j)))$ exceeds time limits when $N = 1000, k = 50$. Binary search reduces time to $O(N \log(\sum nums))$.
- **Off-By-One Boundary Contraction:** When $P(M)$ is true, $M$ could be the answer, so $R = M$. When $P(M)$ is false, $M$ cannot be the answer, so $L = M + 1$. Using $R = M - 1$ when true drops the valid answer.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - The search domain has size $W = \sum(nums) - \max(nums)$.
  - Binary search performs $\lceil \log_2 W \rceil$ iterations.
  - In each iteration, the greedy feasibility check scans the array of $N$ elements once in $O(N)$ time.
  - Total Time: $\mathcal{O}(N \log(\sum nums))$. For $N = 1000$ and $\sum nums = 10^9$, $\log_2(10^9) \approx 30$ iterations, requiring at most $3 \times 10^4$ operations.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$. The algorithm maintains only boundary variables $L, R, M$, and greedy running accumulators $S, cnt$. No heap allocations or recursive call stacks are required.