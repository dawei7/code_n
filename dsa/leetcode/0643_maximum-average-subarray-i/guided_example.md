# Guided Example: Maximum Average Subarray I

We trace the step-by-step fixed-width sliding window initialization ($s = \sum_{j=0}^{k-1} nums[j]$), constant-divisor monotonicity reduction ($\max \text{avg} \iff \max \text{sum}$), sliding window differential update ($s \leftarrow s + nums[i] - nums[i-k]$), running maximum sum tracking ($ans = \max(ans, s)$), and final floating-point arithmetic mean projection ($ans / k$) on representative integer arrays:

- **Input:** $nums = [1, 12, -5, -6, 50, 3], \quad k = 4$
- **Required output:** `12.75000`
  - Problem objective: Find a contiguous subarray of length **exactly $k$** that maximizes the average:
    $$
    \mu = \frac{1}{k} \sum_{j=i}^{i+k-1} nums[j]
    $$
  - Subarray length is fixed at $k = 4$.
- **Fixed-Divisor Monotonicity & Differential Sliding Window Invariant:**
  - **Optimization Reduction:**
    - Since the window length $k > 0$ is constant for all candidates:
      $$
      \frac{\sum A}{k} > \frac{\sum B}{k} \iff \sum A > \sum B
      $$
    - Maximizing the average is mathematically **identical to maximizing the window sum**.
    - We can perform all intermediate comparisons using pure integers, deferring the single division by $k$ to the very end! This eliminates floating-point rounding errors during the search.
  - **$\mathcal{O}(1)$ Window Slide:**
    - As the window slides from $[i - k \dots i - 1]$ to $[i - k + 1 \dots i]$:
      - It gains the new element entering on the right: $+nums[i]$.
      - It loses the old element leaving on the left: $-nums[i - k]$.
    - Updating the sum takes strictly constant time:
      $$
      s_{new} = s_{old} + nums[i] - nums[i - k]
      $$
- **Step-by-Step Worked Execution Trace:**
  - Input array: $[1, 12, -5, -6, 50, 3]$, window size $k = 4$.
  - **Step 1: Compute Initial Window Sum (indices $0 \dots 3$):**
    - Elements: $[1, 12, -5, -6]$
    - Sum:
      $$
      s = 1 + 12 + (-5) + (-6) = 13 - 11 = \mathbf{2}
      $$
    - Initialize maximum:
      $$
      ans = s = \mathbf{2}
      $$
  - **Step 2: Slide Window to $i = 4$ (indices $1 \dots 4$):**
    - Element entering right: $nums[4] = 50$.
    - Element leaving left: $nums[4 - 4] = nums[0] = 1$.
    - Update running sum:
      $$
      s \leftarrow 2 + 50 - 1 = \mathbf{51}
      $$
    - Window elements: $[12, -5, -6, 50]$.
    - Update maximum:
      $$
      ans \leftarrow \max(2, \; 51) = \mathbf{51}
      $$
  - **Step 3: Slide Window to $i = 5$ (indices $2 \dots 5$):**
    - Element entering right: $nums[5] = 3$.
    - Element leaving left: $nums[5 - 4] = nums[1] = 12$.
    - Update running sum:
      $$
      s \leftarrow 51 + 3 - 12 = 54 - 12 = \mathbf{42}
      $$
    - Window elements: $[-5, -6, 50, 3]$.
    - Update maximum:
      $$
      ans \leftarrow \max(51, \; 42) = \mathbf{51}
      $$
  - **Step 4: Compute Final Floating-Point Average:**
    - The array has been fully scanned.
    - Highest contiguous sum found is $51$ (spanning $[12, -5, -6, 50]$).
    - Divide by fixed length $k = 4$:
      $$
      \text{Maximum Average} = \frac{ans}{k} = \frac{51}{4} = \mathbf{12.75}
      $$
    - Return **`12.75`**.
- **Single-Element Window ($nums = [5], k = 1$):**
  - Initial sum $s = 5 \implies$ average $= 5 / 1 = \mathbf{5.0}$.
- **All Negative Values ($nums = [-1, -12, -5, -6], k = 2$):**
  - Window 0: $-1 + (-12) = -13$.
  - Window 1: $-12 + (-5) = -17$.
  - Window 2: $-5 + (-6) = -11$.
  - Max sum is $-11 \implies$ average $= -11 / 2 = \mathbf{-5.5}$.

This instance demonstrates fixed-radius kernel convolution and incremental running sum accumulation, mathematically proves why strictly positive scalar scaling preserves discrete order isomorphisms, and derives $O(N)$ execution time and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an array $nums$ and an integer $k$:
Find a contiguous subarray of length $k$ with the **maximum average value**.

```text
nums = [ 1, 12, -5, -6, 50, 3 ], k = 4

Window 0 (indices 0..3): [ 1, 12, -5, -6 ]    -> sum = 2
Window 1 (indices 1..4): [ 12, -5, -6, 50 ]   -> sum = 51  <-- BEST!
Window 2 (indices 2..5): [ -5, -6, 50, 3 ]    -> sum = 42

Max Sum = 51
Max Average = 51 / 4 = 12.75
```

### The Invariant of Sum-Average Isomorphism
- For any positive constant $k$:
  $$
  \arg\max \frac{\sum_{j=i}^{i+k-1} nums[j]}{k} \equiv \arg\max \sum_{j=i}^{i+k-1} nums[j]
  $$
- Tracking integer sums avoids floating-point operations inside the loop.

---

## 2. Conceptual Foundation & Invariants

### 1. Sliding Window Incremental Step:
$$
s_i = s_{i-1} + nums[i] - nums[i - k]
$$

### 2. Maximum Tracking:
$$
ans = \max_{k-1 \le i < n} s_i
$$
$$
\text{Result} = \frac{ans}{k}
$$

> **Telescoping Window Invariant.** In a translation of interval $[a, b] \to [a+1, b+1]$, the sum changes by exactly $nums[b+1] - nums[a]$, making the differential state transition independent of interval width $k$.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [1, 12, -5, -6, 50, 3], k = 4$:

---

### Step 1: Initial Window $[0 \dots 3]$
- $s = 1 + 12 - 5 - 6 = 2$.
- $ans = 2$.

---

### Step 2: Slide to $i = 4$
- Add $nums[4] = 50$, drop $nums[0] = 1$.
- $s \leftarrow 2 + 50 - 1 = 51$.
- $ans = \max(2, 51) = \mathbf{51}$.

---

### Step 3: Slide to $i = 5$
- Add $nums[5] = 3$, drop $nums[1] = 12$.
- $s \leftarrow 51 + 3 - 12 = 42$.
- $ans = \max(51, 42) = 51$.

---

### Step 4: Final Division
$$
\frac{51}{4} = \mathbf{12.75}
$$

---

## 4. Complete Execution Trace

| Step | Window Range | Element Added | Element Dropped | Running Sum $s$ | Running Best $ans$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Init | $[0 \dots 3]$ | — | — | $2$ | $2$ |
| $i = 4$ | $[1 \dots 4]$ | $nums[4] = 50$ | $nums[0] = 1$ | **$51$** | **`51`** |
| $i = 5$ | $[2 \dots 5]$ | $nums[5] = 3$ | $nums[1] = 12$ | $42$ | **`51`** |
| **Average** | $ans / 4$ | — | — | — | **`12.75`** |

---

## 5. Boundary Cases & Failure Modes

- **$k = n$:** Only 1 window exists $\implies \text{sum}(nums) / n$.
- **$k = 1$:** Reduces to finding the maximum single element: $\max(nums) / 1.0$.
- **All Elements Negative:** Sums remain negative; maximum correctly identifies the least negative window.
- **Large Values ($10^5$ elements of $10^4$):** Max sum fits within 64-bit integer limits.

---

## 6. Traps & Common Anti-Patterns

- **Recalculating Window Sum from Scratch ($O(N \cdot k)$):** Using `sum(nums[i:i+k])` inside a loop takes quadratic time. The sliding window update must be strictly $O(1)$.
- **Dividing by $k$ at Every Step:** Floating-point division at every iteration introduces precision drift and is slower than a single final division.
- **Off-by-One in Dropped Index:** When adding $nums[i]$, the element that fell out on the left is $nums[i - k]$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Initial slice sum of $k$ items: $\mathcal{O}(k)$.
  - Sliding loop runs $n - k$ times with $\mathcal{O}(1)$ updates.
  - Total Time: strictly linear $\mathcal{O}(N)$. Completes in $< 3$ ms for $N = 10^5$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ auxiliary space (only scalar integer accumulators).
