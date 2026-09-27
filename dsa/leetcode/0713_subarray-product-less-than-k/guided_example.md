# Guided Example: Subarray Product Less Than K

We trace the step-by-step two-pointer sliding window expansion ($r$), running product accumulation ($p \leftarrow p \times nums[r]$), left-boundary contraction upon threshold violation ($p \ge k \implies p \leftarrow p / nums[l], \; l \leftarrow l + 1$), right-anchored valid subarray counting ($r - l + 1$), and cumulative non-negative product sum aggregation on representative positive integer arrays:

- **Input:** $nums = [10, 5, 2, 6], \quad k = 100$
- **Required output:** `8`
  - Subarray criteria:
    - Elements are strictly positive integers ($nums[i] \ge 1$).
    - A contiguous subarray $nums[i \dots j]$ is valid if the product of its elements is **strictly less than $k$**:
      $$
      \prod_{t=i}^j nums[t] < k
      $$
    - Find the total count of valid contiguous subarrays.
    - For $[10, 5, 2, 6]$ with $k = 100$:
      - Subarrays with 1 element: $[10], [5], [2], [6]$ (4 subarrays, products: 10, 5, 2, 6).
      - Subarrays with 2 elements: $[10, 5]$ (50), $[5, 2]$ (10), $[2, 6]$ (12) (3 subarrays).
      - Subarrays with 3 elements: $[5, 2, 6]$ (60) (1 subarray).
      - Total count is $4 + 3 + 1 = \mathbf{8}$.
- **Sliding Window Monotonicity & Right-Anchored Invariant:**
  - **The Positive Multiplicative Monotonicity:**
    - Because every element in $nums$ is an integer $\ge 1$:
      - Extending the right pointer ($r \to r + 1$) weakly increases the running product $p$.
      - Contracting the left pointer ($l \to l + 1$) weakly decreases the running product $p$.
    - This monotonicity guarantees that for each fixed right endpoint $r$, the valid starting indices form a contiguous interval $[l, r]$.
  - **The Window Contraction Rule:**
    - Multiply the incoming element: $p \leftarrow p \times nums[r]$.
    - If $p \ge k$, slide the left pointer forward while dividing out the exited elements:
      $$
      \text{while } l \le r \text{ and } p \ge k: \quad p \leftarrow \lfloor p / nums[l] \rfloor, \quad l \leftarrow l + 1
      $$
  - **Right-Anchored Subarray Counting:**
    - After contraction, the window $[l, r]$ is the maximal valid window ending at $r$.
    - Every subarray starting at any index $i \in [l, r]$ and ending at $r$ has product $\le p < k$.
    - The number of such newly introduced valid subarrays ending strictly at $r$ is:
      $$
      \text{Count}_r = r - l + 1
      $$
    - Summing over all $r \in [0, N - 1]$ accounts for every valid subarray exactly once without omission or duplication:
      $$
      ans = \sum_{r=0}^{N-1} (r - l + 1)
      $$
- **Step-by-Step Worked Execution Trace on $nums = [10, 5, 2, 6]$ with $k = 100$:**
  - Initial state: $l = 0, \; p = 1, \; ans = 0$.
  - **Step 1 ($r = 0, nums[0] = 10$):**
    - Multiply:
      $$
      p \leftarrow 1 \times 10 = \mathbf{10}
      $$
    - Check threshold: $10 < 100$ (Valid).
    - Window $[0, 0]$ is valid.
    - Subarrays ending at index 0: $[10]$ (1 subarray).
    - Contribution:
      $$
      r - l + 1 = 0 - 0 + 1 = \mathbf{1}
      $$
      $$
      ans \leftarrow 0 + 1 = \mathbf{1}
      $$
  - **Step 2 ($r = 1, nums[1] = 5$):**
    - Multiply:
      $$
      p \leftarrow 10 \times 5 = \mathbf{50}
      $$
    - Check threshold: $50 < 100$ (Valid).
    - Window $[0, 1]$ is valid.
    - Subarrays ending at index 1: $[5]$ and $[10, 5]$ (2 subarrays).
    - Contribution:
      $$
      r - l + 1 = 1 - 0 + 1 = \mathbf{2}
      $$
      $$
      ans \leftarrow 1 + 2 = \mathbf{3}
      $$
  - **Step 3 ($r = 2, nums[2] = 2$):**
    - Multiply:
      $$
      p \leftarrow 50 \times 2 = \mathbf{100}
      $$
    - Check threshold: $100 \ge k = 100 \implies \mathbf{Threshold\ Violated!}$
    - Contract window from left:
      - Divide out $nums[0] = 10$:
        $$
        p \leftarrow 100 / 10 = \mathbf{10}
        $$
      - Advance left pointer:
        $$
        l \leftarrow 0 + 1 = \mathbf{1}
        $$
      - Check: $10 < 100$ (Contraction halts).
    - Active valid window: $[1, 2]$ with elements $[5, 2]$ (product 10).
    - Subarrays ending at index 2: $[2]$ and $[5, 2]$ (2 subarrays).
    - Contribution:
      $$
      r - l + 1 = 2 - 1 + 1 = \mathbf{2}
      $$
      $$
      ans \leftarrow 3 + 2 = \mathbf{5}
      $$
  - **Step 4 ($r = 3, nums[3] = 6$):**
    - Multiply:
      $$
      p \leftarrow 10 \times 6 = \mathbf{60}
      $$
    - Check threshold: $60 < 100$ (Valid).
    - Active valid window: $[1, 3]$ with elements $[5, 2, 6]$ (product 60).
    - Subarrays ending at index 3: $[6]$, $[2, 6]$, $[5, 2, 6]$ (3 subarrays).
    - Contribution:
      $$
      r - l + 1 = 3 - 1 + 1 = \mathbf{3}
      $$
      $$
      ans \leftarrow 5 + 3 = \mathbf{8}
      $$
  - **Step 5: Output:**
    $$
    ans = \mathbf{8}
    $$
- **Non-Positive Threshold Gate ($k \le 1$):**
  - Because all array elements are positive integers ($nums[i] \ge 1$), any non-empty subarray has product $\ge 1$.
  - For $k = 0$ or $k = 1$, no subarray can ever have a product strictly less than $k$.
  - The contraction while-loop would contract until $l > r$ at every step, yielding 0 contributions.
  - Returns **`0`**.
- **All Elements Large ($nums = [100, 200], k = 50$):**
  - Every single element exceeds $k$.
  - Window empties at each step ($l$ moves to $r + 1$, adding 0).
  - Returns **`0`**.

This instance demonstrates two-pointer amortized window management and right-anchored combinatorial interval decomposition, mathematically proves why positive integer multiplicativity guarantees monotone sliding bounds, and derives $O(N)$ execution time and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an array of positive integers $nums$ and threshold $k$:
Count the number of contiguous subarrays whose **product is strictly less than $k$**.

```text
nums = [ 10, 5, 2, 6 ], k = 100

Right pointer r slides across array:
  r = 0 (10): prod = 10 < 100  -> l = 0 -> adds 1 ([10])
  r = 1 (5):  prod = 50 < 100  -> l = 0 -> adds 2 ([5], [10, 5])
  r = 2 (2):  prod = 100 >= 100 -> divide 10 -> prod = 10, l = 1 -> adds 2 ([2], [5, 2])
  r = 3 (6):  prod = 60 < 100  -> l = 1 -> adds 3 ([6], [2, 6], [5, 2, 6])

Total valid subarrays = 1 + 2 + 2 + 3 = 8
```

### The Invariant of the Right-Anchored Window
- For any valid window $[l, r]$ with product $< k$, there are exactly $r - l + 1$ valid contiguous subarrays ending at index $r$.
- Because each element is positive, growing $r$ increases product and advancing $l$ decreases product, enabling amortized $O(1)$ window tracking.

---

## 2. Conceptual Foundation & Invariants

### 1. Sliding Window Extension and Shrinking:
$$
p \leftarrow p \times nums[r]
$$
$$
\text{While } l \le r \land p \ge k: \quad p \leftarrow \lfloor p / nums[l] \rfloor, \quad l \leftarrow l + 1
$$

### 2. Combinatorial Accumulation:
$$
ans \leftarrow ans + (r - l + 1)
$$

> **Monotone Multiplicative Interval Invariant.** Over positive integer sequences, the condition $\prod_{t=i}^j A[t] < k$ defines a downward-closed order ideal on the product poset $\{ (i, j) \mid 0 \le i \le j < n \}$, whose fiber cardinality over fixed $j$ is uniquely given by $\max(0, j - \min \{i \mid \prod_{t=i}^j A[t] < k\} + 1)$.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [10, 5, 2, 6], k = 100$:

---

### Step 1: $r = 0$ ($nums[0] = 10$)
- $p = 10 < 100 \implies l = 0$.
- Add $0 - 0 + 1 = 1$. $ans = 1$.

---

### Step 2: $r = 1$ ($nums[1] = 5$)
- $p = 50 < 100 \implies l = 0$.
- Add $1 - 0 + 1 = 2$. $ans = 3$.

---

### Step 3: $r = 2$ ($nums[2] = 2$)
- $p = 100 \ge 100 \implies$ divide 10, $l = 1, p = 10$.
- Add $2 - 1 + 1 = 2$. $ans = 5$.

---

### Step 4: $r = 3$ ($nums[3] = 6$)
- $p = 60 < 100 \implies l = 1$.
- Add $3 - 1 + 1 = 3$. $ans = \mathbf{8}$.

---

### Step 5: Output
$$
\mathbf{8}
$$

---

## 4. Complete Execution Trace

| Right Index $r$ | Incoming $nums[r]$ | Product Before Shrink | Left Index $l$ Adjusted | Final Window $[l, r]$ | Added Count $(r - l + 1)$ | Running Total $ans$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | $10$ | $10$ | $0$ | $[0, 0]$ | $1$ | $1$ |
| $1$ | $5$ | $50$ | $0$ | $[0, 1]$ | $2$ | $3$ |
| $2$ | $2$ | $100 \to 10$ | $1$ | $[1, 2]$ | $2$ | $5$ |
| **$3$** | **$6$** | **$60$** | **$1$** | **$[1, 3]$** | **$3$** | **`8`** |

---

## 5. Boundary Cases & Failure Modes

- **$k \le 1$:** All numbers $\ge 1$, so product is $\ge 1$. Subarrays strictly $< k$ cannot exist $\implies$ returns 0.
- **Single Element Array ($[5], k = 10$):** Returns 1.
- **All Elements Large ($[100, 200], k = 50$):** Product always $\ge 50 \implies$ returns 0.
- **Long Sequence of 1s ($k = 2$):** Product of 1s is always $1 < 2 \implies N(N+1)/2$ subarrays.

---

## 6. Traps & Common Anti-Patterns

- **Brute Force Double Loop ($O(N^2)$):** Computing all subarrays causes Time Limit Exceeded for $N = 3 \times 10^4$. Two-pointer sliding window guarantees strictly linear $O(N)$ time.
- **Floating-Point Division:** Using `/` introduces floating-point precision inaccuracies on large integers. Always use integer division `//`.
- **Negative Numbers or Zeros:** The problem specifies strictly positive integers $nums[i] \ge 1$. If zeros were allowed, division-by-zero would break the sliding window.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - The right pointer $r$ advances from $0$ to $N - 1$: $N$ steps.
  - The left pointer $l$ advances from $0$ to at most $N$: at most $N$ steps.
  - Each element is multiplied once and divided at most once.
  - Total Time: strictly linear $\mathcal{O}(N)$. Completes in $< 5$ ms for $N = 3 \times 10^4$.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space (only scalar variables $l, r, p, ans$).