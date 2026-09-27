# Guided Example: Longest Continuous Increasing Subsequence

We trace the step-by-step contiguous subarray boundary maintenance, adjacent element strict inequality testing ($nums[i] < nums[i+1]$), running streak incrementation ($cnt \leftarrow cnt + 1$), monotonic violation streak resetting ($cnt \leftarrow 1$), running maximum preservation ($ans = \max(ans, cnt)$), and linear-time longest run isolation on representative integer sequences:

- **Input:** $nums = [1, 3, 5, 4, 7]$
- **Required output:** `3`
  - Subarray definition:
    - A **continuous** increasing subsequence is a contiguous slice $nums[l \dots r]$ such that every adjacent pair strictly increases:
      $$
      nums[i] < nums[i + 1] \quad \text{for all } l \le i < r
      $$
    - Unlike general subsequences, elements cannot be skipped; contiguity is mandatory.
    - Candidate contiguous runs in $[1, 3, 5, 4, 7]$:
      - Run 1: $[1, 3, 5]$ of length **3**.
      - Run 2: $[4, 7]$ of length **2**.
    - Maximum length is **3**.
- **Adjacent Difference & Streak Resetting Invariant:**
  - **The Contiguity Property:**
    - Because contiguity is required, any drop or plateau ($nums[i] \ge nums[i+1]$) completely terminates the current increasing streak!
    - The new increasing run must begin afresh from index $i + 1$.
  - **Single-Pass State Variables:**
    - $cnt$: Length of the active continuous increasing streak ending at the current element.
    - $ans$: Maximum streak length observed so far.
    - Base state at index 0: $cnt = 1, \; ans = 1$.
  - **State Transition for Step $i$ ($1 \le i < n$):**
    - If $nums[i - 1] < nums[i]$:
      - The streak extends seamlessly:
        $$
        cnt \leftarrow cnt + 1
        $$
        $$
        ans \leftarrow \max(ans, \; cnt)
        $$
    - If $nums[i - 1] \ge nums[i]$:
      - Monotonicity broken! The previous streak terminates.
      - Reset streak counter for the current element:
        $$
        cnt \leftarrow 1
        $$
- **Step-by-Step Worked Execution Trace on $[1, 3, 5, 4, 7]$:**
  - Array length: $n = 5$.
  - Initialize at index $0$:
    $$
    nums[0] = 1 \implies cnt = 1, \quad ans = 1
    $$
  - **Step 1: Inspect Index $1$ ($nums[1] = 3$):**
    - Compare with predecessor:
      $$
      nums[0] = 1, \quad nums[1] = 3 \implies 1 < 3 \quad \mathbf{(Strict\ Increase!)}
      $$
    - Extend streak:
      $$
      cnt \leftarrow 1 + 1 = \mathbf{2}
      $$
    - Active contiguous run: $[1, 3]$.
    - Update maximum:
      $$
      ans \leftarrow \max(1, 2) = \mathbf{2}
      $$
  - **Step 2: Inspect Index $2$ ($nums[2] = 5$):**
    - Compare with predecessor:
      $$
      nums[1] = 3, \quad nums[2] = 5 \implies 3 < 5 \quad \mathbf{(Strict\ Increase!)}
      $$
    - Extend streak:
      $$
      cnt \leftarrow 2 + 1 = \mathbf{3}
      $$
    - Active contiguous run: $[1, 3, 5]$.
    - Update maximum:
      $$
      ans \leftarrow \max(2, 3) = \mathbf{3}
      $$
  - **Step 3: Inspect Index $3$ ($nums[3] = 4$):**
    - Compare with predecessor:
      $$
      nums[2] = 5, \quad nums[3] = 4 \implies 5 \ge 4 \quad \mathbf{(Violation!\ Streak\ Broken)}
      $$
    - The run $[1, 3, 5]$ terminates at index 2.
    - Reset streak counter at index 3:
      $$
      cnt \leftarrow \mathbf{1}
      $$
    - Active contiguous run: $[4]$.
    - Maximum remains: $ans = 3$.
  - **Step 4: Inspect Index $4$ ($nums[4] = 7$):**
    - Compare with predecessor:
      $$
      nums[3] = 4, \quad nums[4] = 7 \implies 4 < 7 \quad \mathbf{(Strict\ Increase!)}
      $$
    - Extend streak:
      $$
      cnt \leftarrow 1 + 1 = \mathbf{2}
      $$
    - Active contiguous run: $[4, 7]$.
    - Update maximum:
      $$
      ans \leftarrow \max(3, 2) = \mathbf{3}
      $$
  - **Step 5: Emit Final Result:**
    - Array fully traversed.
    - Longest continuous increasing subsequence length:
      $$
      ans = \mathbf{3}
      $$
- **All Elements Equal ($nums = [2, 2, 2, 2, 2]$):**
  - For every step, $2 \not< 2$ (equality is not strictly increasing).
  - Streak resets to 1 at every index.
  - Maximum length: **`1`**.
- **Strictly Decreasing Array ($nums = [5, 4, 3, 2, 1]$):**
  - Resets to 1 at every step $\implies$ returns **`1`**.
- **Strictly Increasing Array ($nums = [1, 2, 3, 4, 5]$):**
  - Streak increases monotonically from 1 to 5 $\implies$ returns **`5`**.

This instance demonstrates contiguous run-length encoding and online threshold monitoring, mathematically proves why local violation resets partition the sequence into maximal monotonic intervals, and derives $O(N)$ execution time and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $nums$:
Find the length of the **longest contiguous strictly increasing subarray**.

```text
nums = [ 1, 3, 5, 4, 7 ]

Trace:
  1 -> 3 -> 5 : length 3  (streak: [1, 3, 5])
  5 -> 4      : DROPPED!  (reset streak to 1)
  4 -> 7      : length 2  (streak: [4, 7])

Max Length = 3
```

### The Invariant of Contiguity
- Unlike non-contiguous subsequences (which require $O(N^2)$ or $O(N \log N)$ DP), a **contiguous** increasing subsequence requires that every adjacent pair satisfy $nums[i] < nums[i+1]$.
- A single failure instantly resets the current run, reducing the problem to a strictly linear $O(N)$ running counter.

---

## 2. Conceptual Foundation & Invariants

### 1. The Streak Recurrence:
Initialize $cnt = 1, ans = 1$.
For $i = 1 \dots n - 1$:
$$
cnt \leftarrow \begin{cases} cnt + 1 & \text{if } nums[i] > nums[i - 1] \\ 1 & \text{otherwise} \end{cases}
$$
$$
ans \leftarrow \max(ans, \; cnt)
$$

### 2. Maximal Interval Partition:
The array is partitioned into disjoint contiguous intervals $[l_k, r_k]$ of strictly increasing elements:
$$
\text{LCIS} = \max_k (r_k - l_k + 1)
$$

> **Contiguous Monotonic Partition Invariant.** The set of boundary cut points $\{i \mid nums[i] \ge nums[i+1]\}$ uniquely decomposes the array into maximal strictly increasing contiguous components, whose maximum cardinality is computable in a single prefix scan.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [1, 3, 5, 4, 7]$:

---

### Step 1: Start at 0
- $cnt = 1, ans = 1$.

---

### Step 2: Step to $nums[1] = 3$
- $1 < 3 \implies cnt = 2$.
- $ans = \max(1, 2) = 2$.

---

### Step 3: Step to $nums[2] = 5$
- $3 < 5 \implies cnt = 3$.
- $ans = \max(2, 3) = \mathbf{3}$.

---

### Step 4: Step to $nums[3] = 4$
- $5 \not< 4 \implies cnt = 1$.
- $ans = 3$.

---

### Step 5: Step to $nums[4] = 7$
- $4 < 7 \implies cnt = 2$.
- $ans = \max(3, 2) = 3$.

---

### Step 6: Output
$$
\mathbf{3}
$$

---

## 4. Complete Execution Trace

| Index $i$ | Value $nums[i]$ | Predecessor $nums[i-1]$ | Strict Increase? | Active Streak $cnt$ | Global Best $ans$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | $1$ | — | Start | $1$ | $1$ |
| $1$ | $3$ | $1$ | **Yes ($1 < 3$)** | $2$ | $2$ |
| **$2$** | **$5$** | **$3$** | **Yes ($3 < 5$)** | **$3$** | **`3`** |
| $3$ | $4$ | $5$ | No ($5 \ge 4$) | **$1$ (Reset)** | $3$ |
| $4$ | $7$ | $4$ | **Yes ($4 < 7$)** | $2$ | $3$ |
| **Final** | — | — | — | — | **`3`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Element ($[5]$):** $N = 1 \implies$ loop doesn't execute $\implies$ returns 1.
- **Empty Array:** (Constraints specify $N \ge 1$).
- **Equal Adjacent Elements ($[1, 2, 2, 3]$):** At $2 \to 2$, $2 < 2$ is false $\implies$ streak resets to 1.
- **Alternating Zig-Zag ($[1, 3, 2, 4, 3, 5]$):** Max streak is 2 throughout.

---

## 6. Traps & Common Anti-Patterns

- **Confusing Subarray with Subsequence:** Do not implement an $O(N^2)$ LIS dynamic program or binary search; the problem requires **continuous** subarrays.
- **Weak Inequality ($nums[i-1] \le nums[i]$):** The problem specifies *strictly* increasing. Equal adjacent elements must reset the streak.
- **Forgetting to Update Answer on the Last Element:** Updating $ans = \max(ans, cnt)$ whenever $cnt$ increments ensures the answer is captured even if the longest run reaches the very end of the array.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - A single pass through the $N$ array elements: $\mathcal{O}(N)$.
  - Each step does a single comparison and integer addition: $\mathcal{O}(1)$.
  - Total Time: strictly linear $\mathcal{O}(N)$. Completes in $< 1$ ms for $N = 10^4$.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space (only two scalar variables $cnt$ and $ans$).
