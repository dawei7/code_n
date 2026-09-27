# Guided Example: Largest Sum of Averages

We trace the step-by-step contiguous array partitioning into $k$ non-empty segments, prefix sum accelerated subarray average evaluation ($\frac{s[j] - s[i]}{j - i}$), memoized dynamic programming state recurrence ($dfs(i, k)$), partition cut-point search ($i < j < n$), and global maximum sum of averages maximization on representative integer sequences:

- **Input:**
  $$
  nums = [9, 1, 2, 3, 9], \quad k = 3
  $$
- **Required output:** `20.0`
  - Subarray partition rules:
    - We partition an array of length $n$ into at most $k$ contiguous, non-empty subarrays.
    - The score of a partition is the **sum of the averages** of each subarray.
    - Objective: Maximize this sum of averages.
    - Note: Because all numbers are positive, using the maximum allowed partitions (exactly $k$) is always optimal.
    - For $nums = [9, 1, 2, 3, 9]$ with $k = 3$:
      - Partition 1: $[9]$ (length 1) $\implies$ average is $9 / 1 = \mathbf{9.0}$.
      - Partition 2: $[1, 2, 3]$ (length 3) $\implies$ average is $(1 + 2 + 3) / 3 = 6 / 3 = \mathbf{2.0}$.
      - Partition 3: $[9]$ (length 1) $\implies$ average is $9 / 1 = \mathbf{9.0}$.
      - Total sum of averages:
        $$
        9.0 + 2.0 + 9.0 = \mathbf{20.0}
        $$
      - No other 3-partition achieves a sum $\ge 20.0$.
- **Prefix Sums & Dynamic Programming Invariant:**
  - **The $\mathcal{O}(1)$ Average Formula:**
    - Precompute prefix sums $s$ where $s[0] = 0$ and $s[i] = \sum_{t=0}^{i-1} nums[t]$.
    - For any subarray $nums[i \dots j - 1]$ spanning from index $i$ to $j - 1$:
      $$
      \text{avg}(i, j) = \frac{s[j] - s[i]}{j - i}
      $$
  - **The Optimal Substructure ($dfs(i, k)$):**
    - Let $dfs(i, k)$ be the maximum sum of averages partitioning the suffix $nums[i \dots n - 1]$ into $k$ non-empty subarrays.
    - **Base Case ($k = 1$):**
      - Only 1 subarray remaining; it must cover the entire remaining suffix from $i$ to $n$:
        $$
        dfs(i, 1) = \text{avg}(i, n) = \frac{s[n] - s[i]}{n - i}
        $$
    - **Transition ($k > 1$):**
      - Choose the cut point $j$ for the current subarray ($i < j < n$):
        $$
        dfs(i, k) = \max_{i < j < n} \left( \frac{s[j] - s[i]}{j - i} + dfs(j, k - 1) \right)
        $$
- **Step-by-Step Worked Execution Trace on $nums = [9, 1, 2, 3, 9], k = 3$:**
  - Length $n = 5$.
  - Prefix sums:
    $$
    s = [0, \; 9, \; 10, \; 12, \; 15, \; 24]
    $$
  - **Base Layer: Evaluate $dfs(j, 1)$ for all suffixes:**
    - $dfs(4, 1): nums[4:] = [9] \implies 9 / 1 = \mathbf{9.0}$
    - $dfs(3, 1): nums[3:] = [3, 9] \implies (3 + 9) / 2 = 12 / 2 = \mathbf{6.0}$
    - $dfs(2, 1): nums[2:] = [2, 3, 9] \implies 14 / 3 \approx \mathbf{4.667}$
    - $dfs(1, 1): nums[1:] = [1, 2, 3, 9] \implies 15 / 4 = \mathbf{3.75}$
    - $dfs(0, 1): nums[0:] = [9, 1, 2, 3, 9] \implies 24 / 5 = \mathbf{4.8}$
  - **Layer 2: Evaluate $dfs(i, 2)$ for suffixes:**
    - Suffix from index 1 ($nums[1:] = [1, 2, 3, 9]$) with $k = 2$:
      - Cut $j = 2$: $\text{avg}(1, 2) + dfs(2, 1) = 1.0 + 4.667 = 5.667$
      - Cut $j = 3$: $\text{avg}(1, 3) + dfs(3, 1) = 1.5 + 6.0 = 7.5$
      - Cut $j = 4$: $\text{avg}(1, 4) + dfs(4, 1) = \text{avg}([1, 2, 3]) + dfs(4, 1) = 2.0 + 9.0 = \mathbf{11.0}$
      - Best: $dfs(1, 2) = \max(5.667, 7.5, 11.0) = \mathbf{11.0}$.
  - **Layer 3: Top-Level Evaluation $dfs(0, 3)$:**
    - Test cut point $j$ for the first partition $nums[0 \dots j - 1]$:
      - **Cut $j = 1$ ($nums[0:1] = [9]$):**
        - Average: $9 / 1 = \mathbf{9.0}$.
        - Subproblem for remaining suffix $nums[1:]$ with $k = 2$:
          $$
          \text{avg}(0, 1) + dfs(1, 2) = 9.0 + 11.0 = \mathbf{20.0}
          $$
      - **Cut $j = 2$ ($nums[0:2] = [9, 1]$):**
        - Average: $(9 + 1) / 2 = 5.0$.
        - Subproblem $dfs(2, 2)$:
          - Cut at 3: $\text{avg}(2, 3) + dfs(3, 1) = 2.0 + 6.0 = 8.0$.
          - Cut at 4: $\text{avg}(2, 4) + dfs(4, 1) = 2.5 + 9.0 = 11.5$.
          - Best $dfs(2, 2) = 11.5$.
        - Total: $5.0 + 11.5 = 16.5$.
      - **Cut $j = 3$ ($nums[0:3] = [9, 1, 2]$):**
        - Average: $12 / 3 = 4.0$.
        - Subproblem $dfs(3, 2) = \text{avg}(3, 4) + dfs(4, 1) = 3.0 + 9.0 = 12.0$.
        - Total: $4.0 + 12.0 = 16.0$.
    - Compare all candidate first cuts:
      $$
      dfs(0, 3) = \max(20.0, \; 16.5, \; 16.0) = \mathbf{20.0}
      $$
- **Single Partition Limit ($k = 1$):**
  - No cuts permitted $\implies$ returns entire array average $\sum nums / n$.
- **Full Partition Limit ($k = n$):**
  - Each element forms its own singleton $\implies$ returns sum of all elements $\sum nums$.

This instance demonstrates optimal contiguous 1D partition DP and Bellman additive reward decomposition over non-linear segment functionals, mathematically proves why dynamic programming handles fractional segment averages through sequential cut enumeration, and derives $O(K \cdot N^2)$ runtime and $O(K \cdot N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given array $nums$ and maximum partitions $k$:
Partition $nums$ into at most $k$ contiguous subarrays to maximize the **sum of their averages**.

```text
nums = [ 9, 1, 2, 3, 9 ],  k = 3

Optimal partition into 3 subarrays:
  Subarray 1: [ 9 ]       -> average = 9.0
  Subarray 2: [ 1, 2, 3 ] -> average = 6 / 3 = 2.0
  Subarray 3: [ 9 ]       -> average = 9.0

Total score = 9.0 + 2.0 + 9.0 = 20.0
Result: 20.0
```

### The Invariant of the Partition Recurrence
- Precompute prefix sums so any subarray average $\text{avg}(i, j)$ takes $O(1)$ time.
- $dfs(i, k)$ partitions suffix $nums[i:]$ into $k$ pieces:
  $$
  dfs(i, k) = \max_{i < j < n} \Big( \text{avg}(i, j) + dfs(j, k - 1) \Big)
  $$

---

## 2. Conceptual Foundation & Invariants

### 1. Fast Subarray Average:
$$
\text{avg}(i, j) = \frac{s[j] - s[i]}{j - i}
$$

### 2. Bellman Recurrence Relation:
$$
dfs(i, k) = \begin{cases}
\text{avg}(i, n) & k = 1 \\
\max_{i < j < n} \left( \text{avg}(i, j) + dfs(j, k - 1) \right) & k > 1
\end{cases}
$$

> **Non-Concave Objective Invariant.** Although the average function is not additive, the optimal partition satisfies the principle of optimality because the future reward depends only on the suffix start index $j$ and remaining budget $k - 1$.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [9, 1, 2, 3, 9], k = 3$:

---

### Step 1: Prefix Sums
- $s = [0, 9, 10, 12, 15, 24]$.

---

### Step 2: Evaluate $dfs(1, 2)$
- Cut at $j = 4 \implies [1, 2, 3]$ (avg 2.0) and $[9]$ (avg 9.0) $\implies 11.0$.

---

### Step 3: Top Level $dfs(0, 3)$
- Cut at $j = 1 \implies [9]$ (avg 9.0) $+ dfs(1, 2) (11.0) = \mathbf{20.0}$.
- Other cuts ($j = 2, 3$) give $16.5$ and $16.0$.
- Maximum is $20.0$.

---

### Step 4: Output
$$
\mathbf{20.0}
$$

---

## 4. Complete Execution Trace

| Cut Point $j$ | Subarray 1 ($0 \dots j-1$) | Average 1 | Remaining Suffix | Subproblem Score ($k=2$) | Total Partition Score |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **$1$** | **`[9]`** | **$9.0$** | **`[1, 2, 3, 9]`** | **$11.0$** | **`20.0` (Max!)** |
| $2$ | `[9, 1]` | $5.0$ | `[2, 3, 9]` | $11.5$ | $16.5$ |
| $3$ | `[9, 1, 2]` | $4.0$ | `[3, 9]` | $12.0$ | $16.0$ |

---

## 5. Boundary Cases & Failure Modes

- **$k = 1$:** Single group $\implies \sum nums / n$.
- **$k = n$:** Every number is its own partition $\implies \sum nums$.
- **All Elements Equal ($[5, 5, 5]$):** Every partition yields average 5 $\implies k \times 5$.
- **Small Array ($N = 1$):** Returns $nums[0]$.

---

## 6. Traps & Common Anti-Patterns

- **Greedy Partitioning by Local Average:** Grouping elements greedily to maximize local averages ignores the negative impacts on remaining suffixes. Global DP is required.
- **Recomputing Subarray Sums ($O(N)$ inside loop):** Using `sum(nums[i:j])` inside the nested loops degrades time complexity to $O(K \cdot N^3)$. Prefix sums keep each transition strictly $O(1)$.
- **Floating Point Imprecision in Memoization Keys:** Always memoize on integer indices $(i, k)$, never on floating-point values.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Number of DP states: $N \times K$.
  - Each state iterates over at most $N$ cut points: $\mathcal{O}(N)$.
  - Total Time: strictly $\mathcal{O}(K \cdot N^2)$ where $N \le 100, K \le 100 \implies \le 10^6$ operations. Completes in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(K \cdot N)$ memory for memoization table and $\mathcal{O}(N)$ for prefix sums.