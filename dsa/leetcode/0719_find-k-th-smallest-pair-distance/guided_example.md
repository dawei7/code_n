# Guided Example: Find K-th Smallest Pair Distance

We trace the step-by-step array pre-sorting ($nums \to \text{sorted}$), answer-space binary search over distance domain $[0, \max - \min]$, monotonic pair counting predicate ($\text{count}(dist) = |\{(i, j) \mid nums[j] - nums[i] \le dist\}|$), two-pointer / binary search left-bound location ($a = b - dist$), monotonic step convergence, and $k$-th order statistic isolation on representative pair collections:

- **Input:** $nums = [1, 3, 1], \quad k = 1$
- **Required output:** `0`
  - Distance definition:
    - The distance between an index pair $(i, j)$ with $i < j$ is defined as the absolute difference:
      $$
      \text{dist}(i, j) = |nums[i] - nums[j]|
      $$
    - Total pairs in an array of size $n$:
      $$
      \binom{n}{2} = \frac{n(n - 1)}{2}
      $$
    - For $nums = [1, 3, 1]$ ($n = 3$), there are $\binom{3}{2} = 3$ pairs:
      1. Pair $(nums[0], nums[1]) = (1, 3) \implies \text{dist} = |1 - 3| = 2$.
      2. Pair $(nums[0], nums[2]) = (1, 1) \implies \text{dist} = |1 - 1| = 0$.
      3. Pair $(nums[1], nums[2]) = (3, 1) \implies \text{dist} = |3 - 1| = 2$.
    - Distances sorted in ascending order:
      $$
      [0, \; 2, \; 2]
      $$
    - The $k = 1$-st smallest distance is **0**.
- **Binary Search on the Answer & Monotonic Counting Invariant:**
  - **The Search Range:**
    - The pair distance cannot be smaller than $0$ or larger than $\max(nums) - \min(nums)$:
      $$
      dist \in [0, \; nums[n-1] - nums[0]]
      $$
  - **The Monotonic Counting Predicate $\text{count}(dist)$:**
    - Define $\text{count}(dist)$ as the number of pairs $(j, i)$ with $j < i$ such that $nums[i] - nums[j] \le dist$.
    - As $dist$ increases, the number of satisfying pairs weakly increases:
      $$
      dist_1 \le dist_2 \implies \text{count}(dist_1) \le \text{count}(dist_2)
      $$
    - This monotonicity allows us to **binary search for the smallest distance** $dist$ that satisfies:
      $$
      \text{count}(dist) \ge k
      $$
  - **Fast Pair Counting on Sorted Array:**
    - Sort $nums$ ascending: $nums[0] \le nums[1] \dots \le nums[n-1]$.
    - For each right endpoint $i$ with value $b = nums[i]$:
      - We seek the earliest left index $j < i$ such that:
        $$
        nums[i] - nums[j] \le dist \iff nums[j] \ge nums[i] - dist
        $$
      - In a sorted array, all indices in $[j, \; i - 1]$ satisfy the condition.
      - Number of valid pairs ending at $i$:
        $$
        \Delta = i - j
        $$
      - Summing across all $i$ computes $\text{count}(dist)$ in $O(N)$ (via two pointers) or $O(N \log N)$ (via binary search).
- **Step-by-Step Worked Execution Trace on $nums = [1, 3, 1], k = 1$:**
  - **Step 1: Sort Array:**
    $$
    nums = [1, \; 1, \; 3]
    $$
  - Distance search space:
    $$
    low = 0, \quad high = nums[2] - nums[0] = 3 - 1 = \mathbf{2}
    $$
  - Target rank: $k = 1$.
  - **Iteration 1 (Test midpoint $mid = \lfloor (0 + 2) / 2 \rfloor = \mathbf{1}$):**
    - Compute $\text{count}(dist = 1)$:
      - For $i = 0$ ($nums[0] = 1$): No preceding pairs $\implies 0$.
      - For $i = 1$ ($nums[1] = 1$):
        - Needs $nums[j] \ge 1 - 1 = 0$.
        - Earliest $j$: index $0$ ($nums[0] = 1 \ge 0$).
        - Pairs: $i - j = 1 - 0 = \mathbf{1}$ (Pair $(1, 1)$ with dist $0 \le 1$).
      - For $i = 2$ ($nums[2] = 3$):
        - Needs $nums[j] \ge 3 - 1 = 2$.
        - Smallest element is $1 < 2$. Earliest valid $j$ is index $2$.
        - Pairs: $i - j = 2 - 2 = \mathbf{0}$ (No pairs with dist $\le 1$).
      - Total count:
        $$
        \text{count}(1) = 1 + 0 = \mathbf{1}
        $$
    - Evaluate predicate:
      $$
      \text{count}(1) = 1 \ge k = 1 \implies \mathbf{Threshold\ Met!}
      $$
    - The answer could be 1 or smaller. Contract upper bound:
      $$
      high \leftarrow mid = \mathbf{1}
      $$
  - **Iteration 2 (Test midpoint $mid = \lfloor (0 + 1) / 2 \rfloor = \mathbf{0}$):**
    - Compute $\text{count}(dist = 0)$:
      - For $i = 0$: $0$.
      - For $i = 1$ ($nums[1] = 1$):
        - Needs $nums[j] \ge 1 - 0 = 1$.
        - Earliest $j$: index $0$ ($nums[0] = 1 \ge 1$).
        - Pairs: $i - j = 1 - 0 = \mathbf{1}$ (Pair $(1, 1)$ with dist $0 \le 0$).
      - For $i = 2$ ($nums[2] = 3$):
        - Needs $nums[j] \ge 3 - 0 = 3$.
        - Earliest $j$: index $2$.
        - Pairs: $i - j = 2 - 2 = \mathbf{0}$.
      - Total count:
        $$
        \text{count}(0) = 1 + 0 = \mathbf{1}
        $$
    - Evaluate predicate:
      $$
      \text{count}(0) = 1 \ge k = 1 \implies \mathbf{Threshold\ Met!}
      $$
    - Contract upper bound:
      $$
      high \leftarrow mid = \mathbf{0}
      $$
  - **Termination:**
    - $low = 0, high = 0 \implies$ Pointers converged!
    - Smallest distance with at least $k = 1$ pairs:
      $$
      ans = \mathbf{0}
      $$
- **Larger Distance Trace ($nums = [1, 1, 6], k = 3$):**
  - Distances: $(1, 1) \to 0, \; (1, 6) \to 5, \; (1, 6) \to 5$.
  - Rank $k = 3$ requires all 3 pairs.
  - $\text{count}(4) = 1 < 3$.
  - $\text{count}(5) = 3 \ge 3$.
  - Converges to distance **`5`**.
- **All Identical Elements ($nums = [2, 2, 2], k = 2$):**
  - All pairs have distance 0.
  - $\text{count}(0) = 3 \ge 2$.
  - Returns **`0`**.

This instance demonstrates parametric search on continuous discrete spectrums and monotone pair counting reductions, mathematically proves why predicate monotonicity guarantees bisection correctness on quotient distance metrics, and derives $O(N \log N + N \log W)$ runtime and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $nums$ and integer $k$:
Find the **$k$-th smallest distance** among all pairs $|nums[i] - nums[j]|$.

```text
nums = [ 1, 3, 1 ], k = 1

Sorted nums = [ 1, 1, 3 ]
All pair distances:
  |1 - 1| = 0
  |3 - 1| = 2
  |3 - 1| = 2
Sorted distances = [ 0, 2, 2 ]

The 1st smallest distance (k = 1) is 0.
Result: 0
```

### The Invariant of Binary Search on Distance Values
- Directly generating all $O(N^2)$ distances causes Time Limit Exceeded.
- Instead, binary search over the possible distance range $[0, \max - \min]$.
- For each distance $d$, count how many pairs have distance $\le d$.
- Find the smallest $d$ where $count(d) \ge k$.

---

## 2. Conceptual Foundation & Invariants

### 1. Distance Domain Bisection:
$$
dist \in [0, \; nums[n-1] - nums[0]]
$$

### 2. Monotonic Pair Counter:
$$
\text{count}(dist) = \sum_{i=0}^{n-1} (i - \text{bisect\_left}(nums, \; nums[i] - dist, \; 0, \; i))
$$
$$
ans = \min \{ dist \mid \text{count}(dist) \ge k \}
$$

> **Distance Distribution Quantile Invariant.** The empirical cumulative distribution function $F(d) = \binom{n}{2}^{-1} \sum_{i<j} \mathbf{1}_{|x_i - x_j| \le d}$ is weakly monotonic, admitting exact quantile inversion via binary search on the image spectrum $[0, \text{diam}(X)]$.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [1, 1, 3], k = 1$:

---

### Step 1: Range
- $low = 0, high = 2$.

---

### Step 2: Test $dist = 1$
- Pair $(1, 1) \le 1$ (1 pair).
- Pairs with 3: $|3-1| = 2 > 1$ (0 pairs).
- $\text{count}(1) = 1 \ge 1 \implies high \leftarrow 1$.

---

### Step 3: Test $dist = 0$
- Pair $(1, 1) \le 0$ (1 pair).
- $\text{count}(0) = 1 \ge 1 \implies high \leftarrow 0$.

---

### Step 4: Output
- Converged at **`0`**.

---

## 4. Complete Execution Trace

| Tested Distance $mid$ | Valid Pairs Ending at Index 1 | Valid Pairs Ending at Index 2 | Total Pairs with $\text{dist} \le mid$ | Condition $\text{count} \ge 1$? | Search Bound Adjustment |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | $(1, 1)$ | None | $1$ | Yes | $high \leftarrow 1$ |
| **$0$** | **$(1, 1)$** | **None** | **$1$** | **Yes** | **$high \leftarrow 0$** |
| **Final** | — | — | — | — | **Result: `0`** |

---

## 5. Boundary Cases & Failure Modes

- **All Elements Identical:** Max distance is 0, binary search finishes in 1 step $\implies$ returns 0.
- **$k = 1$ (Minimum Distance):** Finds smallest adjacent difference in sorted array.
- **$k = \binom{N}{2}$ (Maximum Distance):** Returns $\max(nums) - \min(nums)$.
- **Large Array ($N = 10^4$):** Generates 50 million pairs; binary search evaluates $< 20$ iterations without generating any pairs.

---

## 6. Traps & Common Anti-Patterns

- **Generating All Pairs into a Heap ($O(N^2 \log k)$):** For $N = 10^4$, $N^2 \approx 10^8$ pairs, causing Out Of Memory and Time Limit Exceeded. Binary search on the answer runs in $O(N \log N + N \log W)$ without storing pairs.
- **Counting Pairs Linearly ($O(N)$ inside $O(N)$ loop):** Using a nested loop to count pairs makes each predicate evaluation $O(N^2)$, which defeats the purpose. Use binary search (`bisect_left`) or a two-pointer sliding window to count pairs in $O(N)$ or $O(N \log N)$.
- **Off-By-One on Range:** Range must span from $0$ to $\max(nums) - \min(nums)$ inclusive.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Sorting the array: $\mathcal{O}(N \log N)$.
  - Binary search over distance range $W = \max(nums) - \min(nums)$: $\mathcal{O}(\log W)$ iterations.
  - In each iteration, counting pairs takes $\mathcal{O}(N)$ with two pointers (or $\mathcal{O}(N \log N)$ with binary search).
  - Total Time: $\mathcal{O}(N \log N + N \log W)$. For $N = 10^4, W = 10^6$, executes in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space beyond input sorting.
