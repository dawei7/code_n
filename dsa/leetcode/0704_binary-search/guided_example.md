# Guided Example: Binary Search

We trace the step-by-step two-pointer interval bisection ($[l, r]$), midpoint candidate evaluation ($mid = \lfloor (l + r) / 2 \rfloor$), monotonic range elimination ($nums[mid] \ge target \implies r = mid$ vs $l = mid + 1$), boundary convergence ($l == r$), final equality verification ($nums[l] == target$), and absent element rejection ($-1$) on representative sorted integer sequences:

- **Input:** $nums = [-1, 0, 3, 5, 9, 12], \quad target = 9$
- **Required output:** `4`
  - Problem requirements:
    - Given an array $nums$ sorted in strictly ascending order.
    - Find the 0-based index of $target$.
    - If $target$ is absent from the array, return $-1$.
    - Algorithm must operate in guaranteed logarithmic time $O(\log N)$.
    - For the input array: $nums[4] = 9$. The target is located at index **4**.
- **The Binary Search Range Elimination Invariant:**
  - **The Search Interval $[l, r]$:**
    - Let $[l, r]$ denote the active candidate index interval that is guaranteed to contain $target$ (if $target$ exists).
    - Initialize $l = 0$ and $r = N - 1$.
  - **Midpoint Bisection:**
    - Compute the midpoint:
      $$
      mid = \left\lfloor \frac{l + r}{2} \right\rfloor
      $$
    - Because $nums$ is monotonically sorted:
      1. If $nums[mid] \ge target$:
         - The target cannot lie anywhere to the right of $mid$ (all elements $nums[mid+1 \dots r] > nums[mid] \ge target$).
         - The search space can safely contract to the left half, retaining $mid$ as a candidate:
           $$
           r \leftarrow mid
           $$
      2. If $nums[mid] < target$:
         - The target cannot lie at $mid$ or anywhere to the left of $mid$ (all elements $nums[l \dots mid] \le nums[mid] < target$).
         - The search space contracts strictly to the right:
           $$
           l \leftarrow mid + 1
           $$
  - **Loop Invariant and Termination:**
    - In each iteration where $l < r$, the interval width strictly shrinks:
      $$
      (r_{new} - l_{new}) < (r_{old} - l_{old})
      $$
    - The loop terminates precisely when $l == r$, isolating a single candidate index $l$.
    - Check if $nums[l] == target$. If true, return $l$; otherwise, return $-1$.
- **Step-by-Step Worked Execution Trace on $[-1, 0, 3, 5, 9, 12]$ for $target = 9$:**
  - Array length $N = 6$.
  - Initial pointers:
    $$
    l = 0, \quad r = 5, \quad \text{active range: } [0, 5]
    $$
  - **Iteration 1 ($l = 0, r = 5$):**
    - Midpoint calculation:
      $$
      mid = \lfloor (0 + 5) / 2 \rfloor = \mathbf{2}
      $$
    - Element at midpoint: $nums[2] = 3$.
    - Compare with target:
      $$
      nums[2] = 3 < target = 9 \implies \mathbf{Target\ is\ to\ the\ Right}
      $$
    - Eliminate indices $0, 1, 2$. Advance left pointer:
      $$
      l \leftarrow mid + 1 = 2 + 1 = \mathbf{3}
      $$
    - New active range: $[3, 5]$.
  - **Iteration 2 ($l = 3, r = 5$):**
    - Midpoint calculation:
      $$
      mid = \lfloor (3 + 5) / 2 \rfloor = \mathbf{4}
      $$
    - Element at midpoint: $nums[4] = 9$.
    - Compare with target:
      $$
      nums[4] = 9 \ge target = 9 \implies \mathbf{Candidate\ Located\ on\ Left/At\ Mid}
      $$
    - Eliminate index $5$. Contract right pointer:
      $$
      r \leftarrow mid = \mathbf{4}
      $$
    - New active range: $[3, 4]$.
  - **Iteration 3 ($l = 3, r = 4$):**
    - Midpoint calculation:
      $$
      mid = \lfloor (3 + 4) / 2 \rfloor = \mathbf{3}
      $$
    - Element at midpoint: $nums[3] = 5$.
    - Compare with target:
      $$
      nums[3] = 5 < target = 9 \implies \mathbf{Target\ is\ to\ the\ Right}
      $$
    - Eliminate index $3$. Advance left pointer:
      $$
      l \leftarrow mid + 1 = 3 + 1 = \mathbf{4}
      $$
    - New active range: $[4, 4]$.
  - **Termination ($l = 4, r = 4$):**
    - Pointers have converged: $l == r$.
    - Inspect candidate at index $l = 4$:
      $$
      nums[4] = 9 == target \implies \mathbf{Match\ Confirmed!}
      $$
    - Return index:
      $$
      ans = \mathbf{4}
      $$
- **Absent Target Trace ($target = 2$ on $[-1, 0, 3, 5, 9, 12]$):**
  - Iteration 1: $l = 0, r = 5 \implies mid = 2, nums[2] = 3 \ge 2 \implies r \leftarrow 2$. Range: $[0, 2]$.
  - Iteration 2: $l = 0, r = 2 \implies mid = 1, nums[1] = 0 < 2 \implies l \leftarrow 2$. Range: $[2, 2]$.
  - Convergence at $l = 2$.
  - Verification: $nums[2] = 3 \ne 2$.
  - Return **`-1`**.
- **Single Element Array Match ($nums = [5], target = 5$):**
  - $l = 0, r = 0 \implies$ loop does not run.
  - $nums[0] == 5 \implies$ returns index **`0`**.

This instance demonstrates foundational logarithmic bisection and binary search predicate invariants, mathematically proves why single-element convergence eliminates off-by-one boundary errors, and derives $O(\log N)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a sorted array $nums$ and an integer $target$:
Find the index of $target$ in $O(\log N)$ time.
If not present, return $-1$.

```text
nums = [ -1, 0, 3, 5, 9, 12 ], target = 9

Iteration 1: range [0, 5], mid = 2 (val 3) -> 3 < 9 -> l = 3
Iteration 2: range [3, 5], mid = 4 (val 9) -> 9 >= 9 -> r = 4
Iteration 3: range [3, 4], mid = 3 (val 5) -> 5 < 9 -> l = 4

Converged at index 4!
nums[4] == 9 -> return 4
```

### The Invariant of Closed-Interval Convergence
- By maintaining the invariant that the first element $\ge target$ lies in $[l, r]$, the loop `while l < r` always contracts the window without infinite looping.
- Upon convergence $l == r$, checking $nums[l] == target$ resolves both presence and absence in a single check.

---

## 2. Conceptual Foundation & Invariants

### 1. The Bisection Recurrence:
$$
mid = \lfloor (l + r) / 2 \rfloor
$$
$$
\text{If } nums[mid] \ge target \implies r \leftarrow mid \quad \text{else} \quad l \leftarrow mid + 1
$$

### 2. Equality Post-Condition:
$$
ans = \begin{cases} l & \text{if } nums[l] == target \\ -1 & \text{otherwise} \end{cases}
$$

> **Order-Theoretic Bisection Invariant.** For any totally ordered array $A$, the indicator function $\mathbf{1}_{A[i] \ge target}$ is weakly increasing on $[0, n-1]$, allowing binary search to discover the unique partition boundary $i^* = \min \{i \mid A[i] \ge target\}$ in $\lfloor \log_2 n \rfloor + 1$ comparisons.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Iteration 1
- $l = 0, r = 5$.
- $mid = 2, nums[2] = 3 < 9 \implies l \leftarrow 3$.

---

### Step 2: Iteration 2
- $l = 3, r = 5$.
- $mid = 4, nums[4] = 9 \ge 9 \implies r \leftarrow 4$.

---

### Step 3: Iteration 3
- $l = 3, r = 4$.
- $mid = 3, nums[3] = 5 < 9 \implies l \leftarrow 4$.

---

### Step 4: Verification
- $l = r = 4$.
- $nums[4] = 9 == target \implies$ Return **`4`**.

---

## 4. Complete Execution Trace

| Iteration | Active Range $[l, r]$ | Midpoint $mid$ | Value $nums[mid]$ | Comparison with $target = 9$ | Next Active Range |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | $[0, 5]$ | $2$ | $3$ | $3 < 9$ | $[3, 5]$ |
| $2$ | $[3, 5]$ | $4$ | $9$ | $9 \ge 9$ | $[3, 4]$ |
| $3$ | $[3, 4]$ | $3$ | $5$ | $5 < 9$ | $[4, 4]$ |
| **End** | **$[4, 4]$** | **$4$** | **$9$** | **$9 == 9$ (Match!)** | **Return `4`** |

---

## 5. Boundary Cases & Failure Modes

- **Target Smaller than All Elements ($target = -10$):** Converges at index 0, $nums[0] \ne -10 \implies -1$.
- **Target Larger than All Elements ($target = 100$):** Converges at index $N - 1$, $nums[N - 1] \ne 100 \implies -1$.
- **Target in Internal Gap ($target = 2$):** Converges at index 2 (value 3), $3 \ne 2 \implies -1$.
- **Single Element Present ($[7], target = 7$):** Returns 0.

---

## 6. Traps & Common Anti-Patterns

- **Integer Overflow in Midpoint:** In languages with fixed 32-bit integers, $(l + r) / 2$ can overflow if $l + r > 2^{31} - 1$. Using $l + ((r - l) // 2)$ or bit shift `(l + r) >> 1` avoids overflow.
- **Infinite Loop with $mid = (l + r) // 2$ and $l = mid$:** If $l = mid$ is used when only 2 elements remain ($r = l + 1$), $mid$ evaluates to $l$, causing an infinite loop. Always pair $r = mid$ with $l = mid + 1$.
- **Linear Scan ($O(N)$):** Searching element by element fails the $O(\log N)$ algorithmic requirement.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Search range halves at each iteration: $N \to N/2 \to N/4 \dots \to 1$.
  - Maximum iterations: $\lfloor \log_2 N \rfloor + 1$.
  - Total Time: strictly logarithmic $\mathcal{O}(\log N)$. For $N = 10^4$, at most 14 comparisons, completing in $< 0.01$ ms.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space (only scalar indices $l, r, mid$).