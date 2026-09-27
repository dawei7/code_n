# Guided Example: Array Partition

We trace the step-by-step monotonicity sorting ($nums.\text{sort}()$), adjacent pairing gap minimization ($\min(a_i, b_i) = a_i$), sacrificed element loss reduction ($\sum (b_i - a_i)$), even-index subsequence stride summation ($\sum nums[2i]$), and global pair-sum maximization on representative integer arrays:

- **Input:** $nums = [1, 4, 3, 2]$
- **Required output:** `4`
  - Array length: $2n = 4 \implies n = 2$ pairs.
  - Problem objective: Partition the $2n$ integers into $n$ disjoint pairs $(a_1, b_1), (a_2, b_2), \dots, (a_n, b_n)$ such that the sum of pair minimums:
    $$
    S = \sum_{i=1}^n \min(a_i, b_i)
    $$
    is as large as possible.
- **Algebraic Gap Minimization & Sorting Trace:**
  - Let every pair be ordered so that $a_i \le b_i$.
  - Then $\min(a_i, b_i) = a_i$.
  - The total sum of all elements in the array is a constant:
    $$
    \sum_{i=1}^n (a_i + b_i) = \sum_{x \in nums} x = C
    $$
  - We can express the sum of pair differences as:
    $$
    \sum_{i=1}^n (b_i - a_i) = \sum_{i=1}^n (a_i + b_i) - 2 \sum_{i=1}^n a_i = C - 2S
    $$
  - Solving for the target sum $S$:
    $$
    S = \frac{1}{2} \left( C - \sum_{i=1}^n (b_i - a_i) \right)
    $$
  - **Key Mathematical Insight:** To **maximize $S$**, we must **minimize the sum of gaps $\sum (b_i - a_i)$** between paired numbers!
  - To minimize the gaps between pairs, we must pair each number with the closest available value—which is achieved by sorting the array and pairing adjacent numbers!
  - **Step 1: Sort Array in Ascending Order:**
    $$
    nums = [1, 4, 3, 2] \xrightarrow{\text{sort}} [1, \; 2, \; 3, \; 4]
    $$
  - **Step 2: Form Consecutive Adjacent Pairs:**
    - Pair 1: $(nums[0], nums[1]) = (1, 2)$
      - Minimum: $\min(1, 2) = \mathbf{1}$
      - Gap sacrificed: $2 - 1 = 1$
    - Pair 2: $(nums[2], nums[3]) = (3, 4)$
      - Minimum: $\min(3, 4) = \mathbf{3}$
      - Gap sacrificed: $4 - 3 = 1$
  - **Step 3: Sum the Selected Minimums:**
    - Notice that each pair minimum is precisely the element at the **even index**:
      $$
      nums[0] + nums[2] = 1 + 3 = \mathbf{4}
      $$
  - *Contrast with a non-adjacent pairing:*
    - If paired as $(1, 4)$ and $(2, 3)$:
      - Minimums: $\min(1, 4) + \min(2, 3) = 1 + 2 = \mathbf{3} < 4$.
      - Gaps sacrificed: $(4 - 1) + (3 - 2) = 3 + 1 = 4$ (wasting the value of $4$!).
    - Adjacent sorting preserves the large value $3$ by pairing it with $4$, sacrificing only a gap of $1$.
- **Six Element Instance ($nums = [6, 2, 6, 5, 1, 2]$):**
  - Sorted: $[1, 2, 2, 5, 6, 6]$
  - Even-index elements:
    $$
    nums[0] + nums[2] + nums[4] = 1 + 2 + 6 = \mathbf{9}
    $$
- **Uniform Array ($nums = [5, 5, 5, 5]$):**
  - All gaps are 0 $\implies 5 + 5 = \mathbf{10}$.
- **Negative Elements ($nums = [-1, -4, -3, -2]$):**
  - Sorted: $[-4, -3, -2, -1]$
  - Even-index elements: $-4 + (-2) = \mathbf{-6}$.

This instance demonstrates greedy adjacent matching under total sum invariance, mathematically proves why sorting minimizes the aggregate gap penalty $\sum (b_i - a_i)$, and derives $O(N \log N)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an array of $2n$ integers $nums$:
Group them into $n$ pairs $(a_1, b_1), \dots, (a_n, b_n)$ to **maximize the sum of pair minimums**:
$$
\sum_{i=1}^n \min(a_i, b_i)
$$

```text
Input: [ 1,  4,  3,  2 ]

Sort:  [ 1,  2,  3,  4 ]
Pairs: (1, 2),  (3, 4)
Mins:     1   +    3   = 4 (Maximum possible!)

Suboptimal pairing: (1, 4), (2, 3) -> 1 + 2 = 3
```

### The Sacrificed Value Theorem
- In every pair $(a_i, b_i)$ where $a_i \le b_i$:
  - The smaller element $a_i$ is counted in the sum.
  - The larger element $b_i$ is discarded (sacrificed).
- The total sum of all numbers is fixed.
- To maximize what we keep, we must **minimize what is wasted**:
  $$
  \text{Wasted} = \sum_{i=1}^n (b_i - a_i)
  $$
- Pairing each number with its immediate neighbor in sorted order minimizes the difference between paired numbers, making the wasted amount as small as mathematically possible.

---

## 2. Conceptual Foundation & Invariants

### 1. The Greedy Strategy:
1. Sort $nums$ in non-decreasing order:
   $$
   nums[0] \le nums[1] \le nums[2] \le \dots \le nums[2n-1]
   $$
2. Pair adjacent elements:
   $$
   (nums[0], nums[1]), \; (nums[2], nums[3]), \; \dots, \; (nums[2n-2], nums[2n-1])
   $$
3. The minimum of each pair $(nums[2i], nums[2i+1])$ is always the first element:
   $$
   \min(nums[2i], nums[2i+1]) = nums[2i]
   $$
4. The maximum sum is simply:
   $$
   \sum_{i=0}^{n-1} nums[2i]
   $$

> **Adjacent Neighbor Optimality Invariant.** Any cross-pairing of non-adjacent sorted elements $(x_1, y_2)$ and $(x_2, y_1)$ with $x_1 \le x_2 \le y_1 \le y_2$ produces a sum $\min(x_1, y_2) + \min(x_2, y_1) = x_1 + x_2$, which is identical to or strictly dominated by adjacent pairing $x_1 + y_1$.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [1, 4, 3, 2]$:

---

### Step 1: Sort
$$
nums = [1, \; 2, \; 3, \; 4]
$$

---

### Step 2: Form Pairs
- Pair 0: $(nums[0], nums[1]) = (1, 2) \implies \min = 1$
- Pair 1: $(nums[2], nums[3]) = (3, 4) \implies \min = 3$

---

### Step 3: Sum Even Elements
$$
nums[0] + nums[2] = 1 + 3 = \mathbf{4}
$$

---

## 4. Complete Execution Trace

| Step | Array State | Elements at Even Indices | Elements at Odd Indices (Sacrificed) | Running Sum of Minimums |
|:---:|:---:|:---:|:---:|:---:|
| **Sort** | `[1, 2, 3, 4]` | — | — | $0$ |
| **Pair 0** | $(1, 2)$ | $nums[0] = \mathbf{1}$ | $nums[1] = 2$ | $1$ |
| **Pair 1** | $(3, 4)$ | $nums[2] = \mathbf{3}$ | $nums[3] = 4$ | $1 + 3 = \mathbf{4}$ |
| **Result** | — | — | Total sacrificed: $3$ | **`4`** |

---

## 5. Boundary Cases & Failure Modes

- **Minimum Length ($2n = 2$):** Only one pair exists $\implies \min(nums[0], nums[1])$.
- **All Elements Equal ($[5, 5, 5, 5]$):** Any pairing produces the same sum $\implies 5 + 5 = \mathbf{10}$.
- **Negative Elements ($[-4, -3, -2, -1]$):** Sorting places most negative numbers first. $-4 + (-2) = \mathbf{-6}$. (Pairing $(-4, -1)$ would yield $-4 + (-3) = -7 < -6$).
- **Large Arrays ($2 \times 10^4$ elements):** In-place sorting executes in $O(N \log N)$ time with zero memory allocation.

---

## 6. Traps & Common Anti-Patterns

- **Attempting Dynamic Programming:** Since the problem asks for optimal partitioning, one might consider subset-sum DP. However, the greedy adjacent sorting strategy is provably globally optimal, reducing an exponential search to a simple sort.
- **Pairing Smallest with Largest:** Pairing $(nums[0], nums[2n-1])$ wastes the largest number in the array on the smallest number, achieving the absolute *minimum* possible sum instead of the maximum.
- **Manual Loop vs Slice Stride:** Summing `nums[::2]` directly computes the result in Python with fast C-level iteration.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Sorting $2N$ integers: $\mathcal{O}(N \log N)$.
  - Stepping through the even indices takes $N$ operations: $\mathcal{O}(N)$.
  - Total Time: $\mathcal{O}(N \log N)$. For $2N = 2 \times 10^4$, finishes in $< 3$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ beyond standard in-place sorting memory.
