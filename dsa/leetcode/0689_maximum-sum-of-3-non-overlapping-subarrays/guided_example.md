# Guided Example: Maximum Sum of 3 Non-Overlapping Subarrays

We trace the step-by-step staggered 3-window sliding summation ($s_1, s_2, s_3$ of length $k$), single-window prefix prefix-maximum tracking ($mx_1, idx_1$), dual-window coupled prefix-maximum accumulation ($mx_{12}, idx_{12}$), tri-window global total maximization ($s, ans$), strict inequality lexicographical tie-breaking, and index triplet derivation on representative integer sequences:

- **Input:** $nums = [1, 2, 1, 2, 6, 7, 5, 1], \quad k = 2$
- **Required output:** `[0, 3, 5]`
  - Subarray constraints:
    - Select exactly 3 subarrays, each of length $k = 2$.
    - Subarrays must be **strictly non-overlapping**:
      $$
      i_1 + k \le i_2 \quad \text{and} \quad i_2 + k \le i_3
      $$
    - Objective: Maximize the total sum of elements in the three subarrays:
      $$
      \text{Total Sum} = \sum_{p=i_1}^{i_1+k-1} nums[p] + \sum_{p=i_2}^{i_2+k-1} nums[p] + \sum_{p=i_3}^{i_3+k-1} nums[p]
      $$
    - Tie-breaking: If multiple index triplets achieve the same maximum sum, return the **lexicographically smallest** triplet $(i_1, i_2, i_3)$.
- **Triple-Window Staggered Sliding Invariant:**
  - **The Three-Phase Dynamic Programming Invariant:**
    - At any rightmost boundary $i \ge 3k - 1$, three non-overlapping windows of width $k$ slide synchronously:
      - **Window 3 (Rightmost):** covers $[i - k + 1, \; i]$ with sum $s_3$.
      - **Window 2 (Middle):** covers $[i - 2k + 1, \; i - k]$ with sum $s_2$.
      - **Window 1 (Leftmost):** covers $[i - 3k + 1, \; i - 2k]$ with sum $s_1$.
  - **Coupled Prefix Extremum Tracking:**
    1. **Single-Window Best ($mx_1, idx_1$):**
       - The best single window in the prefix ending at or before Window 1's position:
         $$
         s_1 > mx_1 \implies mx_1 \leftarrow s_1, \quad idx_1 \leftarrow i - 3k + 1
         $$
       - *Note on Lexicographical Ties:* By using strict inequality ($>$), an earlier index is preserved in case of equal sums.
    2. **Two-Window Best ($mx_{12}, idx_{12}$):**
       - The best pair of non-overlapping windows ending at or before Window 2's position:
         $$
         mx_1 + s_2 > mx_{12} \implies mx_{12} \leftarrow mx_1 + s_2, \quad idx_{12} \leftarrow (idx_1, \; i - 2k + 1)
         $$
    3. **Three-Window Best ($s, ans$):**
       - The best complete triplet combining $mx_{12}$ with the current Window 3:
         $$
         mx_{12} + s_3 > s \implies s \leftarrow mx_{12} + s_3, \quad ans \leftarrow [idx_{12}[0], \; idx_{12}[1], \; i - k + 1]
         $$
- **Step-by-Step Worked Execution Trace on $[1, 2, 1, 2, 6, 7, 5, 1]$ with $k = 2$:**
  - Array length $n = 8, \; k = 2$.
  - The loop index $i$ runs from $2k = 4$ up to $n - 1 = 7$.
  - Warm up sums:
    - Initial sliding window elements populate as $i$ approaches $3k - 1 = 5$.
  - **Window Evaluation at $i = 5$ (Right boundary = index 5):**
    - Window 1: indices $[0, 1] \implies nums[0 \dots 1] = [1, 2]$, sum $s_1 = 1 + 2 = \mathbf{3}$.
    - Window 2: indices $[2, 3] \implies nums[2 \dots 3] = [1, 2]$, sum $s_2 = 1 + 2 = \mathbf{3}$.
    - Window 3: indices $[4, 5] \implies nums[4 \dots 5] = [6, 7]$, sum $s_3 = 6 + 7 = \mathbf{13}$.
    - Update Single-Window Best:
      $$
      s_1 = 3 > mx_1 = 0 \implies mx_1 = 3, \quad idx_1 = 0
      $$
    - Update Dual-Window Best:
      $$
      mx_1 + s_2 = 3 + 3 = 6 > mx_{12} = 0 \implies mx_{12} = 6, \quad idx_{12} = (0, 2)
      $$
    - Update Tri-Window Best:
      $$
      mx_{12} + s_3 = 6 + 13 = 19 > s = 0 \implies s = 19, \quad ans = [0, 2, 4]
      $$
  - **Window Evaluation at $i = 6$ (Right boundary = index 6):**
    - Slide windows forward by 1:
    - Window 1: indices $[1, 2] \implies [2, 1]$, sum $s_1 = 2 + 1 = \mathbf{3}$.
    - Window 2: indices $[3, 4] \implies [2, 6]$, sum $s_2 = 2 + 6 = \mathbf{8}$.
    - Window 3: indices $[5, 6] \implies [7, 5]$, sum $s_3 = 7 + 5 = \mathbf{12}$.
    - Update Single-Window Best:
      - $s_1 = 3 \not> mx_1 = 3$ (Tie: keep earlier index $idx_1 = 0$).
    - Update Dual-Window Best:
      $$
      mx_1 + s_2 = 3 + 8 = \mathbf{11} > mx_{12} = 6 \implies mx_{12} = 11, \quad idx_{12} = (\mathbf{0}, \; \mathbf{3})
      $$
    - Update Tri-Window Best:
      $$
      mx_{12} + s_3 = 11 + 12 = \mathbf{23} > s = 19 \implies s = \mathbf{23}, \quad ans = [\mathbf{0}, \; \mathbf{3}, \; \mathbf{5}]
      $$
  - **Window Evaluation at $i = 7$ (Right boundary = index 7):**
    - Slide windows forward by 1:
    - Window 1: indices $[2, 3] \implies [1, 2]$, sum $s_1 = 3$.
    - Window 2: indices $[4, 5] \implies [6, 7]$, sum $s_2 = 13$.
    - Window 3: indices $[6, 7] \implies [5, 1]$, sum $s_3 = 6$.
    - Update Single-Window Best:
      - $s_1 = 3 \not> 3 \implies mx_1 = 3, idx_1 = 0$.
    - Update Dual-Window Best:
      $$
      mx_1 + s_2 = 3 + 13 = \mathbf{16} > mx_{12} = 11 \implies mx_{12} = 16, \quad idx_{12} = (0, 4)
      $$
    - Update Tri-Window Best:
      $$
      mx_{12} + s_3 = 16 + 6 = 22 \not> s = 23 \implies \text{No update!}
      $$
      - Current best triplet $[0, 3, 5]$ with sum $23$ remains undefeated!
  - **Step 4: Output Triplet:**
    $$
    ans = [\mathbf{0}, \; \mathbf{3}, \; \mathbf{5}]
    $$
    - Total sum achieved:
      $$
      (1 + 2) + (2 + 6) + (7 + 5) = 3 + 8 + 12 = \mathbf{23}
      $$

This instance demonstrates cascaded prefix dynamic programming over fixed-length interval packings, mathematically proves why strict inequalities guarantee lexicographical optimality under sliding window transitions, and derives $O(N)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given array $nums$ and window length $k$:
Find 3 non-overlapping subarrays of length $k$ with **maximum sum**.
If tied, return the **lexicographically smallest** starting indices.

```text
nums = [ 1, 2, 1, 2, 6, 7, 5, 1 ], k = 2

Subarray candidates of length 2:
  Index 0: [1, 2] -> sum 3
  Index 1: [2, 1] -> sum 3
  Index 2: [1, 2] -> sum 3
  Index 3: [2, 6] -> sum 8
  Index 4: [6, 7] -> sum 13
  Index 5: [7, 5] -> sum 12
  Index 6: [5, 1] -> sum 6

Best 3 non-overlapping windows:
  Window 1 at index 0: [1, 2] (sum 3)
  Window 2 at index 3: [2, 6] (sum 8)
  Window 3 at index 5: [7, 5] (sum 12)

Total Sum = 3 + 8 + 12 = 23
Starting indices: [ 0, 3, 5 ]
```

### The Invariant of the 3 Synchronized Windows
- As the rightmost window slides, we maintain:
  1. The best 1-window sum in the past ($mx_1$).
  2. The best 2-window sum in the past ($mx_{12} = mx_1 + s_2$).
  3. The best 3-window sum ($s = mx_{12} + s_3$).
- Using strict inequality ($>$) ensures that on equal sums, earlier indices are preserved, guaranteeing lexicographical minimization.

---

## 2. Conceptual Foundation & Invariants

### 1. Sliding Window Updates:
At step $i$:
$$
mx_1 = \max(mx_1, \; s_1)
$$
$$
mx_{12} = \max(mx_{12}, \; mx_1 + s_2)
$$
$$
s = \max(s, \; mx_{12} + s_3)
$$

### 2. Strict Inequality Tie-Breaker:
$$
s_1 > mx_1 \implies idx_1 \leftarrow i - 3k + 1
$$
$$
mx_1 + s_2 > mx_{12} \implies idx_{12} \leftarrow (idx_1, \; i - 2k + 1)
$$
$$
mx_{12} + s_3 > s \implies ans \leftarrow [*idx_{12}, \; i - k + 1]
$$

> **Cascaded Monotone Packing Invariant.** The optimal $m$-interval packing over a prefix decomposes into the maximum packing of $m-1$ intervals prior to the final interval position, maintaining strict left-to-right optimal substructure.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: $i = 5$ (Indices $[0, 1], [2, 3], [4, 5]$)
- $s_1 = 3, s_2 = 3, s_3 = 13$.
- $mx_1 = 3$ ($idx_1 = 0$).
- $mx_{12} = 3 + 3 = 6$ ($idx_{12} = (0, 2)$).
- $s = 6 + 13 = 19$ ($ans = [0, 2, 4]$).

---

### Step 2: $i = 6$ (Indices $[1, 2], [3, 4], [5, 6]$)
- $s_1 = 3, s_2 = 8, s_3 = 12$.
- $mx_1 = 3$ ($idx_1 = 0$).
- $mx_{12} = 3 + 8 = 11$ ($idx_{12} = (0, 3)$).
- $s = 11 + 12 = \mathbf{23} > 19 \implies ans = [\mathbf{0}, \mathbf{3}, \mathbf{5}]$.

---

### Step 3: $i = 7$ (Indices $[2, 3], [4, 5], [6, 7]$)
- $s_1 = 3, s_2 = 13, s_3 = 6$.
- $mx_1 = 3, mx_{12} = 3 + 13 = 16$.
- $mx_{12} + s_3 = 16 + 6 = 22 < 23$ (No update).

---

### Step 4: Output
$$
[\mathbf{0}, \; \mathbf{3}, \; \mathbf{5}]
$$

---

## 4. Complete Execution Trace

| Step $i$ | Window 1 $([idx], s_1)$ | Window 2 $([idx], s_2)$ | Window 3 $([idx], s_3)$ | Best 1-Window $mx_1$ | Best 2-Window $mx_{12}$ | Total 3-Window Sum $s$ | Active Best $ans$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $5$ | $[0 \dots 1]: 3$ | $[2 \dots 3]: 3$ | $[4 \dots 5]: 13$ | $3$ (at $0$) | $6$ (at $0, 2$) | $19$ | `[0, 2, 4]` |
| **$6$** | $[1 \dots 2]: 3$ | $[3 \dots 4]: 8$ | $[5 \dots 6]: 12$ | $3$ (at $0$) | **$11$ (at $0, 3$)** | **`23`** | **`[0, 3, 5]`** |
| $7$ | $[2 \dots 3]: 3$ | $[4 \dots 5]: 13$ | $[6 \dots 7]: 6$ | $3$ (at $0$) | $16$ (at $0, 4$) | $22$ | `[0, 3, 5]` |

---

## 5. Boundary Cases & Failure Modes

- **Minimum Length ($N = 3k$):** Exactly one choice for all 3 windows $\implies$ returns $[0, k, 2k]$.
- **All Identical Elements ($nums = [1, 1, \dots, 1]$):** Lexicographical tie-breaking returns the earliest possible indices $[0, k, 2k]$.
- **Large Values ($N = 2 \times 10^4, k = 1000$):** Sliding windows maintain running totals with integer arithmetic without overflow.

---

## 6. Traps & Common Anti-Patterns

- **Using $\ge$ Instead of $>$ for Maximum:** Using $\ge$ replaces earlier indices with later indices on ties, violating the requirement to return the **lexicographically smallest** triplet.
- **Three Nested Loops ($O(N^3)$):** Testing all triples of starting indices takes $O(N^3)$ time (TLE). Cascaded sliding window DP runs in strictly linear $O(N)$ time.
- **Off-By-One Index Offsets:** Carefully calculate window start indices: $i - 3k + 1$, $i - 2k + 1$, and $i - k + 1$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Single loop from $2k$ to $N - 1$: $\mathcal{O}(N)$ iterations.
  - In each iteration, performs constant number of additions and scalar comparisons: $\mathcal{O}(1)$.
  - Total Time: strictly linear $\mathcal{O}(N)$. Completes in $< 5$ ms for $N = 2 \times 10^4$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ auxiliary space (only scalar running sums and index tuples).
