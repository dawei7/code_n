# Guided Example: Maximum Average Subarray II

We trace the step-by-step continuous binary search over the real answer space ($v \in [\min, \max]$), mean-centered deviation transformation ($B[i] = nums[i] - v$), length-constrained prefix sum range testing ($j - i \ge k$), running prefix minimum maintenance ($mi = \min P[0 \dots j-k]$), feasibility decision testing ($s \ge mi \iff \text{exists subarray with avg } \ge v$), and precision convergence ($\epsilon \le 10^{-5}$) on representative variable-length array instances:

- **Input:** $nums = [1, 12, -5, -6, 50, 3], \quad k = 4$
- **Required output:** `12.75000`
  - Problem specification:
    - Find a contiguous subarray of length **at least $k$** ($length \ge k$) that maximizes the arithmetic mean:
      $$
      \mu = \frac{1}{L} \sum_{p=i}^{i+L-1} nums[p] \quad \text{where } L \ge k
      $$
    - Precision tolerance: Accepted if within $10^{-5}$ of the true maximum.
  - Key distinction from Part I: Subarray length $L$ is **variable** ($k \le L \le n$). Because the denominator $L$ is not constant, we cannot simply maximize the sum!
- **Binary Search on the Answer & Zero-Mean Reduction:**
  - The maximum average must lie in the continuous interval $[\min(nums), \max(nums)]$.
  - **The Decision Predicate ($check(v)$):**
    - Question: *Does there exist any contiguous subarray of length $L \ge k$ whose average is at least $v$?*
      $$
      \frac{\sum_{p=i}^j nums[p]}{j - i + 1} \ge v \iff \sum_{p=i}^j (nums[p] - v) \ge 0
      $$
    - Transform the array by subtracting $v$ from every element:
      $$
      B[p] = nums[p] - v
      $$
    - The question becomes: *Does $B$ contain a contiguous subarray of length $\ge k$ with sum $\ge 0$?*
  - **Linear Verification via Running Prefix Minimum:**
    - Let $P[t] = \sum_{p=0}^{t-1} B[p]$ be the prefix sum array of $B$ (with $P[0] = 0$).
    - The sum of subarray $B[i \dots j]$ is $P[j + 1] - P[i]$.
    - Length constraint $j - i + 1 \ge k \implies i \le j + 1 - k$.
    - To make $P[j + 1] - P[i] \ge 0$, we want to pick the **smallest possible prefix sum** $P[i]$ among all valid starting indices $0 \le i \le j + 1 - k$:
      $$
      \max_{i} (P[j + 1] - P[i]) = P[j + 1] - \min_{0 \le i \le j + 1 - k} P[i]
      $$
    - If this maximum exceeds or equals $0$, then a valid subarray exists $\implies check(v) = \mathbf{True}$.
    - As $j$ advances from $k$ to $n$, the boundary index $j + 1 - k$ advances by 1 at each step, allowing the minimum $mi$ to be maintained online in strictly $\mathcal{O}(1)$ time per element!
- **Step-by-Step Worked Execution Trace on $[1, 12, -5, -6, 50, 3], k = 4$:**
  - Global bounds:
    $$
    l = \min(nums) = -6.0, \quad r = \max(nums) = 50.0
    $$
  - **Trace Candidate Midpoint $v = 12.0$:**
    - Test if average $\ge 12.0$ is achievable.
    - Compute deviations $B[p] = nums[p] - 12$:
      - $B[0] = 1 - 12 = -11$
      - $B[1] = 12 - 12 = 0$
      - $B[2] = -5 - 12 = -17$
      - $B[3] = -6 - 12 = -18$
      - $B[4] = 50 - 12 = +38$
      - $B[5] = 3 - 12 = -9$
    - **Step 1: Check First Window of Length $k = 4$ ($B[0 \dots 3]$):**
      $$
      s = (-11) + 0 + (-17) + (-18) = \mathbf{-46} < 0
      $$
      - First 4 elements alone are not enough.
    - **Step 2: Expand to $j = 4$ (Examining Subarrays Ending at Index 4):**
      - Current cumulative prefix $P[5] = s + B[4] = -46 + 38 = \mathbf{-8}$.
      - Valid prefix starts can be index $0$ ($P[0] = 0$) or index $1$ ($P[1] = B[0] = -11$).
      - Minimum preceding prefix sum:
        $$
        mi = \min(P[0], \; P[1]) = \min(0, \; -11) = \mathbf{-11}
        $$
      - Maximize subarray sum ending at index 4:
        $$
        \text{Subarray Sum} = P[5] - mi = -8 - (-11) = \mathbf{+3}
        $$
      - Notice: $+3 \ge 0 \implies \mathbf{Feasible!}$
      - Indeed, subarray $nums[1 \dots 4] = [12, -5, -6, 50]$ has sum $51$, length $4$, average $51 / 4 = 12.75 > 12.0$.
    - Conclusion for $v = 12.0$: $check(12.0) = \mathbf{True}$.
    - Narrow search: $l \leftarrow 12.0$.
  - **Trace Candidate Midpoint $v = 13.0$:**
    - Deviations $B[p] = nums[p] - 13$:
      - $B = [-12, -1, -18, -19, 37, -10]$
    - Length 4 sum: $-12 - 1 - 18 - 19 = -50$.
    - At index 4: prefix $P[5] = -50 + 37 = -13$.
      - $mi = \min(0, -12) = -12$.
      - $P[5] - mi = -13 - (-12) = -1 < 0$.
    - At index 5: prefix $P[6] = -13 - 10 = -23$.
      - $P[2] = -12 - 1 = -13 \implies mi = \min(-12, -13) = -13$.
      - $P[6] - mi = -23 - (-13) = -10 < 0$.
    - No subarray has sum $\ge 0 \implies check(13.0) = \mathbf{False}$.
    - Narrow search: $r \leftarrow 13.0$.
  - **Convergence to Solution:**
    - Repeating bisection narrows $[l, r]$ until $r - l < 10^{-5}$.
    - Exact supremum is achieved on $[12, -5, -6, 50]$:
      $$
      v^* = \frac{12 + (-5) + (-6) + 50}{4} = \frac{51}{4} = \mathbf{12.75}
      $$
    - Returns: **`12.75000`**.
- **Variable Length Advantage:**
  - If array has $[1, 10, 10, 10]$ with $k = 2$:
  - Length 2 window $[10, 10]$ has average $10.0$.
  - Length 3 window $[10, 10, 10]$ also has average $10.0$.
  - The algorithm transparently tests all lengths $\ge k$.

This instance demonstrates real-valued bisection and online prefix minimum scanning for length-constrained fractional optimization, mathematically proves why mean-centering reduces fractional programming to sign-feasibility verification, and derives $O(N \log \frac{\max - \min}{\epsilon})$ runtime and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an array $nums$ and an integer $k$:
Find the **maximum average** of any contiguous subarray of length **at least $k$** ($L \ge k$).

```text
nums = [ 1, 12, -5, -6, 50, 3 ], k = 4

Subarray [ 12, -5, -6, 50 ]:
  Length = 4 (>= 4)
  Sum = 51
  Average = 51 / 4 = 12.75  <-- MAXIMUM!
```

### The Invariant of Mean-Centered Deviations
- Checking if there exists a subarray with average $\ge v$ is equivalent to:
  $$
  \sum_{p=i}^j (nums[p] - v) \ge 0
  $$
- This transforms a rational ratio optimization problem into a simple **zero-threshold prefix sum query**!

---

## 2. Conceptual Foundation & Invariants

### 1. The Decision Predicate $check(v)$:
Let $B[i] = nums[i] - v$.
Compute prefix sums $P$ of $B$.
A valid subarray of length $\ge k$ with sum $\ge 0$ exists if:
$$
\exists j \ge k: \quad P[j] \ge \min_{0 \le i \le j - k} P[i]
$$

### 2. Binary Search Termination:
Loop while $r - l \ge 10^{-5}$:
- $mid = (l + r) / 2$
- If $check(mid) \implies l = mid$
- Else $r = mid$
Return $l$.

> **Dinkelbach Fractional Monotonicity Invariant.** The parametric deficit function $\delta(v) = \max_{L \ge k} \sum (x_i - v)$ is strictly decreasing and continuous in $v$, guaranteeing a unique root $\delta(v^*) = 0$ at the global maximum average.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [1, 12, -5, -6, 50, 3], k = 4$:

---

### Step 1: Initialize Range
- $l = -6.0, r = 50.0$.

---

### Step 2: Test Midpoint $v = 12.0$
- $B = [-11, 0, -17, -18, 38, -9]$.
- Subarray $B[1 \dots 4] = [0, -17, -18, 38]$ has sum $+3 \ge 0$.
- $check(12.0) = \mathbf{True} \implies l \leftarrow 12.0$.

---

### Step 3: Test Midpoint $v = 13.0$
- $B = [-12, -1, -18, -19, 37, -10]$.
- All valid subarray sums are strictly negative.
- $check(13.0) = \mathbf{False} \implies r \leftarrow 13.0$.

---

### Step 4: Final Convergence
- Bisection converges to $l = \mathbf{12.75}$.

---

## 4. Complete Execution Trace

| Tested Average $v$ | First Length-$k$ Sum | Running Prefix Min $mi$ | Max Subarray Sum $P[j] - mi$ | $check(v)$ Result | Search Interval After |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $22.0$ | $-86$ | $0$ | Negative | **False** | $[-6.0, 22.0]$ |
| $8.0$ | $-30$ | $-7$ | $+19$ | **True** | $[8.0, 22.0]$ |
| $12.0$ | $-46$ | $-11$ | $+3$ | **True** | $[12.0, 22.0]$ |
| $13.0$ | $-50$ | $-12$ | $-1$ | **False** | $[12.0, 13.0]$ |
| ... | ... | ... | ... | ... | $[12.74999, 12.75001]$ |
| **Final** | — | — | — | — | **`12.75000`** |

---

## 5. Boundary Cases & Failure Modes

- **$k = n$:** Subarray must be the entire array $\implies \text{sum}(nums) / n$.
- **$k = 1$:** Single maximum element $\implies \max(nums)$.
- **All Elements Equal:** Returns that common value.
- **Negative Values:** Binary search seamlessly handles negative ranges.

---

## 6. Traps & Common Anti-Patterns

- **Trying to Use Fixed-Size Window ($O(N)$):** Only checking subarrays of length exactly $k$ misses longer subarrays that have higher averages.
- **Brute Force All Subarrays ($O(N^2)$):** Checking all $O(N^2)$ pairs $(i, j)$ causes Time Limit Exceeded for $N = 10^5$.
- **Not Tracking Minimum Prefix:** Trying to find the best start index by re-scanning from 0 takes $O(N^2)$ per check. Tracking $mi = \min(mi, P[i-k])$ keeps the check strictly $O(N)$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Each call to $check(v)$ scans the array once in $\mathcal{O}(N)$ time.
  - Number of bisections to reach tolerance $\epsilon = 10^{-5}$:
    $$
    \log_2 \left( \frac{\max(nums) - \min(nums)}{10^{-5}} \right) \approx \log_2(10^9) \approx 30 \text{ iterations}
    $$
  - Total Time: $\mathcal{O}(N \log \frac{R}{\epsilon})$. For $N = 10^4$, executes $\approx 30 \times 10^4 = 3 \cdot 10^5$ operations, completing in $< 25$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ auxiliary space.
