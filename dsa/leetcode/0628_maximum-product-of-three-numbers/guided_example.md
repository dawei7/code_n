# Guided Example: Maximum Product of Three Numbers

We trace the step-by-step array sorted order analysis ($nums[0] \le \dots \le nums[n-1]$), negative sign multiplication dynamics ($(-) \times (-) = (+)$), dual-candidate product evaluation ($P_1 = \text{top}_3$ vs $P_2 = \text{bottom}_2 \times \text{top}_1$), and global maximum product selection on representative integer sequences:

- **Input:** $nums = [-10, -10, 1, 2, 5]$
- **Required output:** `500`
  - Problem specification: Choose three elements from $nums$ such that their product is maximized.
  - Core challenge: The presence of **negative numbers**. The product of two large negative numbers produces a large positive number ($(-10) \times (-10) = +100$), which when multiplied by a positive number can exceed the product of the three largest positive numbers!
- **Sorted Candidate Partition Invariant:**
  - Let $nums$ be sorted in non-decreasing order:
    $$
    nums[0] \le nums[1] \le \dots \le nums[n-2] \le nums[n-1]
    $$
  - There are only **two structural candidates** for the maximum product of 3 elements:
    1. **Candidate 1 (Three Largest Values):**
       $$
       P_1 = nums[n-1] \times nums[n-2] \times nums[n-3]
       $$
       - Optimal when all numbers are positive, or when there are fewer than 2 negative numbers, or when all numbers are negative.
    2. **Candidate 2 (Two Smallest Values $\times$ Single Largest Value):**
       $$
       P_2 = nums[0] \times nums[1] \times nums[n-1]
       $$
       - Optimal when the two smallest numbers have large absolute values (large negatives), multiplying to a large positive product $nums[0] \times nums[1] > 0$, scaled by the largest positive number $nums[n-1]$.
  - No other combination can ever beat both $P_1$ and $P_2$.
  - Therefore, the global maximum is simply:
    $$
    \text{Max Product} = \max(P_1, \; P_2)
    $$
- **Step-by-Step Worked Execution Trace on $[-10, -10, 1, 2, 5]$:**
  - Length $n = 5$.
  - Sorted array:
    $$
    nums = [\mathbf{-10}, \; \mathbf{-10}, \; 1, \; \mathbf{2}, \; \mathbf{5}]
    $$
  - **Calculate Candidate 1 ($P_1$ - Three largest elements):**
    - The three largest values at the right end are:
      $$
      nums[4] = 5, \quad nums[3] = 2, \quad nums[2] = 1
      $$
    - Compute product:
      $$
      P_1 = 5 \times 2 \times 1 = \mathbf{10}
      $$
  - **Calculate Candidate 2 ($P_2$ - Two smallest and one largest):**
    - The two smallest elements at the left end are:
      $$
      nums[0] = -10, \quad nums[1] = -10
      $$
    - The single largest element is:
      $$
      nums[4] = 5
      $$
    - Compute product:
      $$
      P_2 = (-10) \times (-10) \times 5 = 100 \times 5 = \mathbf{500}
      $$
  - **Compare Candidates:**
    $$
    ans = \max(P_1, \; P_2) = \max(10, \; 500) = \mathbf{500}
    $$
    - Candidate 2 dominates Candidate 1 by a factor of 50!
- **All Positive Numbers Instance ($nums = [1, 2, 3, 4]$):**
  - $P_1 = 4 \times 3 \times 2 = 24$.
  - $P_2 = 1 \times 2 \times 4 = 8$.
  - $\max(24, 8) = \mathbf{24}$ (Candidate 1 wins).
- **All Negative Numbers Instance ($nums = [-5, -4, -3, -2, -1]$):**
  - $P_1 = (-1) \times (-2) \times (-3) = -6$.
  - $P_2 = (-5) \times (-4) \times (-1) = -20$.
  - $\max(-6, -20) = \mathbf{-6}$ (Candidate 1 wins with the least negative product).
- **Array with Zeros ($nums = [-10, 0, 1, 2]$):**
  - $P_1 = 2 \times 1 \times 0 = 0$.
  - $P_2 = (-10) \times 0 \times 2 = 0$.
  - $\max(0, 0) = \mathbf{0}$.

This instance demonstrates extremal case partitioning under signed multiplicative metrics, mathematically proves why exactly two endpoint boundary triplets span the entire search space, and derives $O(N \log N)$ runtime (or $O(N)$ with top-3 / bottom-2 scans) and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $nums$:
Find three elements whose product is **maximum**.

```text
nums = [-10, -10, 1, 2, 5]

Candidate 1 (3 largest):
  5 * 2 * 1 = 10

Candidate 2 (2 smallest negatives * largest positive):
  (-10) * (-10) * 5 = 500  <-- MUCH LARGER!

Result: 500
```

### The Invariant of the 5 Extremal Elements
- In any array of size $N \ge 3$, the answer is completely determined by at most 5 numbers:
  - The **3 largest numbers**: $\max_1, \max_2, \max_3$.
  - The **2 smallest numbers**: $\min_1, \min_2$.
- Every other element in the interior of the sorted array is strictly suboptimal.

---

## 2. Conceptual Foundation & Invariants

### 1. Closed-Form Evaluation:
After sorting:
$$
P_1 = nums[-1] \cdot nums[-2] \cdot nums[-3]
$$
$$
P_2 = nums[-1] \cdot nums[0] \cdot nums[1]
$$
$$
\text{Ans} = \max(P_1, P_2)
$$

### 2. Proof of Exclusivity:
- To maximize $a \cdot b \cdot c$:
  - If the result is positive, it must be formed by 3 positives or 2 negatives $\times$ 1 positive.
  - For 3 positives: product is maximized by the 3 largest positives.
  - For 2 negatives $\times$ 1 positive: product is maximized by the 2 negatives with largest magnitudes (i.e. smallest algebraic values) and the single largest positive.
  - If the result must be negative (all numbers negative), it is maximized by the 3 least negative numbers (the 3 largest).
- In all cases, the optimal triplet is either $P_1$ or $P_2$.

> **Boundary Extremum Invariant.** The maximum product of three points from a compact subset of $\mathbb{R}$ is attained exclusively on the extremal boundary points $\{\min_1, \min_2\} \cup \{\max_3, \max_2, \max_1\}$.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [-10, -10, 1, 2, 5]$:

---

### Step 1: Sort the Array
$$
nums = [-10, \; -10, \; 1, \; 2, \; 5]
$$

---

### Step 2: Compute Right-End Product $P_1$
$$
P_1 = 5 \times 2 \times 1 = \mathbf{10}
$$

---

### Step 3: Compute Left-End Product $P_2$
$$
P_2 = (-10) \times (-10) \times 5 = \mathbf{500}
$$

---

### Step 4: Compare
$$
\max(10, 500) = \mathbf{500}
$$

---

## 4. Complete Execution Trace

| Candidate | Multiplied Elements | Algebraic Sign Breakdown | Sub-Product | Final Product |
|:---:|:---:|:---:|:---:|:---:|
| **$P_1$ (Top 3)** | $nums[-3], nums[-2], nums[-1] = (1, 2, 5)$ | $(+) \times (+) \times (+)$ | $2 \times 5$ | $10$ |
| **$P_2$ (Bottom 2 $\times$ Top 1)** | $nums[0], nums[1], nums[-1] = (-10, -10, 5)$ | $(-) \times (-) \times (+)$ | $100 \times 5$ | **`500` (Max)** |
| **Conclusion** | — | — | — | **`500`** |

---

## 5. Boundary Cases & Failure Modes

- **Exactly 3 Elements ($N = 3$):** Both $P_1$ and $P_2$ equal the exact same 3 elements $\implies$ returns their product.
- **All Negatives ($[-5, -4, -3, -2, -1]$):** Evaluates $(-3)(-2)(-1) = -6$ vs $(-5)(-4)(-1) = -20 \implies -6$.
- **Contains Zeros ($[-5, -2, 0, 1, 3]$):** Evaluates cleanly with 0 products.
- **Large Values ($1000 \times 1000 \times 1000$):** Product fits comfortably inside standard 64-bit integers.

---

## 6. Traps & Common Anti-Patterns

- **Assuming the 3 Largest Numbers are Always Optimal:** Forgetting the product of two negative numbers is the most common bug in this problem.
- **Checking 3 Smallest Negatives ($nums[0] \cdot nums[1] \cdot nums[2]$):** Three negative numbers produce a negative product, which can never exceed $P_2$ (which pairs two negatives with a positive).
- **Brute Force Triple Loop ($O(N^3)$):** Checking all triplets takes cubic time; sorting takes $O(N \log N)$, and a single pass for top-3 / bottom-2 takes $O(N)$ time.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Sorting: $\mathcal{O}(N \log N)$ time.
  - Or using a single linear pass to track 5 variables ($\max_1, \max_2, \max_3, \min_1, \min_2$): $\mathcal{O}(N)$ time.
  - Closed-form comparison: $\mathcal{O}(1)$.
  - Total Time: $\mathcal{O}(N \log N)$ (or $\mathcal{O}(N)$). Completes in $< 2$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ auxiliary space.
