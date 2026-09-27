# Guided Example: Number of Subarrays with Bounded Maximum

We trace the step-by-step contiguous subarray maximum bound constraint ($\max(nums[i \dots j]) \in [left, right]$), inclusion-exclusion monotonic prefix difference decomposition ($f(right) - f(left - 1)$), threshold barrier segmentation ($v > x \implies \text{reset}$), contiguous run accumulation ($cnt += t$), and valid subarray count evaluation on representative integer sequences:

- **Input:**
  $$
  nums = [2, 1, 4, 3], \quad left = 2, \quad right = 3
  $$
- **Required output:** `3`
  - Subarray maximum constraints:
    - A contiguous subarray $nums[i \dots j]$ ($0 \le i \le j < n$) is valid if and only if its maximum value satisfies:
      $$
      left \le \max_{i \le k \le j} nums[k] \le right
      $$
    - For $nums = [2, 1, 4, 3]$ with range $[2, 3]$:
      - Subarray $[2]$: max is 2 $\in [2, 3] \implies$ **Valid #1**
      - Subarray $[2, 1]$: max is 2 $\in [2, 3] \implies$ **Valid #2**
      - Subarray $[1]$: max is 1 $< 2 \implies$ Invalid (too small)
      - Subarrays containing 4 ($[4], [1, 4], [2, 1, 4], [4, 3]$, etc.): max is at least 4 $> 3 \implies$ Invalid (too large)
      - Subarray $[3]$: max is 3 $\in [2, 3] \implies$ **Valid #3**
      - Total valid subarrays: **3**.
- **Prefix Monotonicity & Complementary Difference Invariant:**
  - **The Sub-Problem $f(x)$:**
    - Define $f(x)$ as the number of contiguous subarrays where **every element is $\le x$**:
      $$
      \forall k \in [i, j]: \quad nums[k] \le x \iff \max_{k \in [i, j]} nums[k] \le x
      $$
  - **Inclusion-Exclusion Principle:**
    - A subarray has maximum in $[left, right]$ if and only if its maximum is $\le right$ and its maximum is NOT $\le left - 1$:
      $$
      \text{Valid Subarrays} = f(right) - f(left - 1)
      $$
  - **Linear Contiguous Streak Counting ($O(N)$):**
    - To compute $f(x)$ in a single pass:
      - Any element with $v > x$ acts as an impassable barrier: no subarray with maximum $\le x$ can contain this element!
      - Maintain a running counter $t$ of consecutive elements $\le x$:
        - If $v > x$: reset streak $t \leftarrow 0$.
        - If $v \le x$: extend streak $t \leftarrow t + 1$.
      - Each index $j$ contributes exactly $t$ subarrays ending at index $j$ (lengths $1, 2, \dots, t$):
        $$
        cnt \leftarrow cnt + t
        $$
    - Running this linear counter twice ($f(right)$ and $f(left - 1)$) computes the answer directly in $O(N)$ time and $O(1)$ space.
- **Step-by-Step Worked Execution Trace on $nums = [2, 1, 4, 3], left = 2, right = 3$:**
  - We compute $f(3)$ and $f(1)$:
  - **Part A: Compute $f(right) = f(3)$ (Subarrays with max $\le 3$):**
    - Initialize: $cnt = 0, t = 0$.
    - **Element 0 ($v = 2$):**
      - $2 \le 3 \implies t \leftarrow 0 + 1 = 1$.
      - Subarrays ending here: $[2]$.
      - Accumulate: $cnt \leftarrow 0 + 1 = \mathbf{1}$.
    - **Element 1 ($v = 1$):**
      - $1 \le 3 \implies t \leftarrow 1 + 1 = 2$.
      - Subarrays ending here: $[1], [2, 1]$.
      - Accumulate: $cnt \leftarrow 1 + 2 = \mathbf{3}$.
    - **Element 2 ($v = 4$):**
      - $4 > 3 \implies$ Barrier! Reset streak: $t \leftarrow 0$.
      - Subarrays ending here: None.
      - Accumulate: $cnt \leftarrow 3 + 0 = \mathbf{3}$.
    - **Element 3 ($v = 3$):**
      - $3 \le 3 \implies t \leftarrow 0 + 1 = 1$.
      - Subarrays ending here: $[3]$.
      - Accumulate: $cnt \leftarrow 3 + 1 = \mathbf{4}$.
    - Total:
      $$
      f(3) = \mathbf{4}
      $$
      *(Subarrays: $[2], [1], [2, 1], [3]$)*.
  - **Part B: Compute $f(left - 1) = f(1)$ (Subarrays with max $\le 1$):**
    - Initialize: $cnt = 0, t = 0$.
    - **Element 0 ($v = 2$):**
      - $2 > 1 \implies$ Barrier! $t \leftarrow 0, cnt = 0$.
    - **Element 1 ($v = 1$):**
      - $1 \le 1 \implies t \leftarrow 0 + 1 = 1$.
      - Subarrays ending here: $[1]$.
      - Accumulate: $cnt \leftarrow 0 + 1 = \mathbf{1}$.
    - **Element 2 ($v = 4$):**
      - $4 > 1 \implies$ Barrier! $t \leftarrow 0, cnt = 1$.
    - **Element 3 ($v = 3$):**
      - $3 > 1 \implies$ Barrier! $t \leftarrow 0, cnt = 1$.
    - Total:
      $$
      f(1) = \mathbf{1}
      $$
      *(Subarray: $[1]$)*.
  - **Part C: Complementary Difference:**
    $$
    ans = f(3) - f(1) = 4 - 1 = \mathbf{3}
    $$
    *(Valid subarrays: $[2], [2, 1], [3]$)*.
- **Single Large Barrier Trace ($nums = [2, 9, 2, 5, 6], left = 2, right = 8$):**
  - Element 9 acts as a wall that cleanly segments the array into two independent components: $[2]$ and $[2, 5, 6]$.
  - Subarrays never cross 9, so counts in both segments sum up independently.
- **Empty Valid Interval Trace ($left > right$ or all elements $> right$):**
  - $f(right) = 0 \implies ans = 0$.

This instance demonstrates monotone predicate filtration and 1D interval decomposition, mathematically proves why the set of bounded-extremum sub-intervals factors into a difference of lower-contour segments, and derives $O(N)$ execution time and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given array $nums$ and range $[left, right]$:
Find the number of contiguous subarrays where the **maximum element** lies in $[left, right]$.

```text
nums = [ 2, 1, 4, 3 ], left = 2, right = 3

Subarrays with max <= 3:
  [2], [1], [2, 1], [3] -> 4 subarrays

Subarrays with max <= 1 (too small!):
  [1] -> 1 subarray

Valid subarrays with max in [2, 3]:
  4 - 1 = 3  ([2], [2, 1], [3])

Result: 3
```

### The Invariant of the Complementary Difference
- Counting subarrays with maximum in $[left, right]$ directly is messy.
- By transforming the problem to counting subarrays with maximum $\le x$:
  $$\text{valid} = f(right) - f(left - 1)$$
- In $f(x)$, elements $> x$ act as barriers, and streaks of elements $\le x$ of length $t$ add $t$ subarrays.

---

## 2. Conceptual Foundation & Invariants

### 1. Cumulative Subarray Metric:
$$
f(x) = \sum_{i = 0}^{n - 1} t_i \quad \text{where } t_i = \begin{cases} 0 & nums[i] > x \\ t_{i - 1} + 1 & nums[i] \le x \end{cases}
$$

### 2. Set Difference Reduction:
$$
|\{ S \subseteq nums \mid \max(S) \in [left, right] \}| = f(right) - f(left - 1)
$$

> **Poset Filter Difference Invariant.** Let $\mathcal{I}(nums)$ be the poset of intervals ordered by inclusion, and $\max: \mathcal{I}(nums) \to \mathbb{R}$ the supremum morphism. The preimage $\max^{-1}([left, right])$ is the set-theoretic difference of lower principal ideals $\max^{-1}((-\infty, right]) \setminus \max^{-1}((-\infty, left - 1])$.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [2, 1, 4, 3], left = 2, right = 3$:

---

### Step 1: Compute $f(3)$
- $2 \le 3 \implies t = 1, cnt = 1$.
- $1 \le 3 \implies t = 2, cnt = 1 + 2 = 3$.
- $4 > 3 \implies t = 0, cnt = 3$.
- $3 \le 3 \implies t = 1, cnt = 3 + 1 = 4$.
- $f(3) = 4$.

---

### Step 2: Compute $f(1)$
- $2 > 1 \implies t = 0, cnt = 0$.
- $1 \le 1 \implies t = 1, cnt = 1$.
- $4 > 1 \implies t = 0, cnt = 1$.
- $3 > 1 \implies t = 0, cnt = 1$.
- $f(1) = 1$.

---

### Step 3: Difference
- $4 - 1 = \mathbf{3}$.

---

### Step 4: Output
$$
\mathbf{3}
$$

---

## 4. Complete Execution Trace

| Index $i$ | Element $v$ | Streak $t$ for $f(3)$ | Running $cnt$ for $f(3)$ | Streak $t$ for $f(1)$ | Running $cnt$ for $f(1)$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | $2$ | $1$ | $1$ | $0$ | $0$ |
| $1$ | $1$ | $2$ | $3$ | $1$ | $1$ |
| $2$ | $4$ | $0$ | $3$ | $0$ | $1$ |
| **$3$** | **$3$** | **$1$** | **$4$** | **$0$** | **$1$** |
| **Final** | — | — | **$f(3) = 4$** | — | **$f(1) = 1 \implies \mathbf{3}$** |

---

## 5. Boundary Cases & Failure Modes

- **All Elements in Range ($nums = [2, 2, 2], [2, 2]$):** $f(2) = 1 + 2 + 3 = 6$, $f(1) = 0 \implies 6$.
- **No Elements in Range ($nums = [1, 1, 1], [2, 3]$):** $f(3) = 6, f(1) = 6 \implies 0$.
- **All Elements Exceed $right$ ($nums = [5, 5], [2, 3]$):** $f(3) = 0, f(1) = 0 \implies 0$.
- **Large Array ($N = 10^5$):** $f(x)$ sums up to $N(N+1)/2 \approx 5 \times 10^9$; ensure 64-bit integer tracking.

---

## 6. Traps & Common Anti-Patterns

- **Direct Segment / Sliding Window with Dual Conditions:** Maintaining two pointers with both lower and upper bounds leads to complicated edge cases with overlapping segments. Decomposing into $f(right) - f(left - 1)$ requires only 1 condition per pass and is 100% bug-free.
- **Quadratic Nested Loops ($O(N^2)$):** Iterating through all pairs $(i, j)$ and finding the maximum takes $O(N^2)$ or $O(N^3)$, which times out on $N = 10^5$.
- **Off-By-One on Lower Bound:** The lower bound subtraction must be $left - 1$, not $left$, because elements equal to $left$ are permitted in the target range $[left, right]$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Function $f(x)$ performs a single linear pass over the array: $\mathcal{O}(N)$.
  - Called twice: $f(right)$ and $f(left - 1)$.
  - Total Time: strictly linear $\mathcal{O}(N)$ where $N \le 10^5$. Completes in $< 3$ ms.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space.
