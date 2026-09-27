# Guided Example: Subarray Sum Equals K

We trace the step-by-step prefix displacement accumulation ($s = \sum x$), prefix sum difference theorem ($sum(j \dots i) = s_i - s_{j-1} = k \iff s_{j-1} = s_i - k$), zero-offset frequency map seeding ($cnt[0] = 1$), running prefix frequency caching ($cnt[s] \mathrel{+}= 1$), and linear single-pass total subarray enumeration on representative integer arrays:

- **Input:** $nums = [1, 1, 1], \quad k = 2$
- **Required output:** `2`
  - Subarray definition: A contiguous, non-empty sequence of elements.
  - Objective: Count the number of pairs $(j, i)$ with $0 \le j \le i < n$ such that:
    $$
    \sum_{m=j}^i nums[m] = k
    $$
- **Prefix Sum Difference Principle:**
  - Let $s_i$ be the cumulative sum of elements from index $0$ to $i$:
    $$
    s_i = \sum_{m=0}^i nums[m]
    $$
  - The sum of subarray $nums[j \dots i]$ can be rewritten as:
    $$
    sum(j \dots i) = s_i - s_{j-1}
    $$
    *(where $s_{-1} = 0$ denotes the empty prefix before the array begins)*.
  - Setting this equal to $k$:
    $$
    s_i - s_{j-1} = k \iff s_{j-1} = s_i - k
    $$
  - **Deduction:** At any index $i$, the number of valid subarrays ending at $i$ with sum $k$ is **exactly equal to the number of earlier prefix sums equal to $s_i - k$**!
- **Single-Pass Hash Map Execution Trace:**
  - Initialize frequency map `cnt` with base entry $\{0: 1\}$:
    $$
    cnt = \{0: 1\}
    $$
    *(This represents the empty prefix sum $s_{-1} = 0$, ensuring subarrays starting at index $0$ are counted correctly)*.
  - Initialize running sum $s = 0$ and subarray counter $ans = 0$.
  - **Step 1 ($i = 0, \; x = nums[0] = 1$):**
    - Update running prefix sum:
      $$
      s \leftarrow 0 + 1 = \mathbf{1}
      $$
    - Look for required earlier prefix $s - k$:
      $$
      \text{target} = s - k = 1 - 2 = \mathbf{-1}
      $$
    - Query map: $cnt[-1] = 0$.
    - Add to answer: $ans \leftarrow 0 + 0 = 0$.
    - Register current prefix sum $s = 1$:
      $$
      cnt[1] \leftarrow 1 \implies cnt = \{0: 1, \; \mathbf{1: 1}\}
      $$
  - **Step 2 ($i = 1, \; x = nums[1] = 1$):**
    - Update running prefix sum:
      $$
      s \leftarrow 1 + 1 = \mathbf{2}
      $$
    - Look for required earlier prefix:
      $$
      \text{target} = s - k = 2 - 2 = \mathbf{0}
      $$
    - Query map: $cnt[0] = \mathbf{1}$ (the base empty prefix!).
    - Found 1 valid subarray ending at index 1 (subarray $nums[0 \dots 1] = [1, 1]$):
      $$
      ans \leftarrow ans + cnt[0] = 0 + 1 = \mathbf{1}
      $$
    - Register current prefix sum $s = 2$:
      $$
      cnt[2] \leftarrow 1 \implies cnt = \{0: 1, \; 1: 1, \; \mathbf{2: 1}\}
      $$
  - **Step 3 ($i = 2, \; x = nums[2] = 1$):**
    - Update running prefix sum:
      $$
      s \leftarrow 2 + 1 = \mathbf{3}
      $$
    - Look for required earlier prefix:
      $$
      \text{target} = s - k = 3 - 2 = \mathbf{1}
      $$
    - Query map: $cnt[1] = \mathbf{1}$ (registered at Step 1).
    - Found 1 valid subarray ending at index 2 (subarray $nums[1 \dots 2] = [1, 1]$):
      $$
      ans \leftarrow ans + cnt[1] = 1 + 1 = \mathbf{2}
      $$
    - Register current prefix sum $s = 3$:
      $$
      cnt[3] \leftarrow 1 \implies cnt = \{0: 1, \; 1: 1, \; 2: 1, \; \mathbf{3: 1}\}
      $$
  - Array fully traversed.
  - Final total count of valid subarrays: **`2`** (subarrays $[0 \dots 1]$ and $[1 \dots 2]$).
- **Prefix and Singleton Instance ($nums = [1, 2, 3], k = 3$):**
  - At index 1 ($nums[1]=2$): $s = 3$, target $3 - 3 = 0 \implies cnt[0] = 1$ (subarray $[1, 2]$).
  - At index 2 ($nums[2]=3$): $s = 6$, target $6 - 3 = 3 \implies cnt[3] = 1$ (subarray $[3]$).
  - Total: $1 + 1 = \mathbf{2}$.
- **Zero Values Creating Multiple Matches ($nums = [0, 0, 0], k = 0$):**
  - Running sum stays 0; $cnt[0]$ increments at each step ($1 \to 2 \to 3 \to 4$).
  - Evaluates all $\binom{4}{2} = \mathbf{6}$ zero-sum subarrays in $O(N)$ time.

This instance demonstrates prefix sum complement matching via frequency hash maps, mathematically proves why initializing $cnt[0] = 1$ is necessary to capture root prefixes, and derives $O(N)$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $nums$ and an integer $k$:
Find the **total number of subarrays whose elements sum to $k$**.

```text
nums = [ 1,  1,  1 ],   k = 2

Subarrays of sum 2:
  1. nums[0..1] = [1, 1] -> sum = 2
  2. nums[1..2] = [1, 1] -> sum = 2

Total Valid Subarrays = 2
```

### Why Sliding Window / Two Pointers Cannot Be Used Here
- Standard two-pointer sliding window requires the array elements to be **non-negative** (so expanding the window monotonically increases the sum, and shrinking monotonically decreases it).
- In this problem, $nums[i]$ can be **negative, zero, or positive** ($nums[i] \in [-1000, 1000]$).
- Because negative numbers break monotonicity, a sliding window cannot determine whether to expand or contract.
- The **prefix sum + hash map** pattern handles arbitrary negative and positive numbers in strictly linear $O(N)$ time!

---

## 2. Conceptual Foundation & Invariants

### 1. Algebraic Subarray Sum Identity:
$$
\sum_{m=j}^i nums[m] = s_i - s_{j-1}
$$
Setting $\sum = k$:
$$
s_i - s_{j-1} = k \iff s_{j-1} = s_i - k
$$
Every time we reach a prefix sum $s_i$, any earlier prefix index with sum $s_i - k$ forms a valid subarray ending at $i$.

### 2. Frequency Hash Map:
- $cnt[v]$ stores how many times prefix sum value $v$ has appeared so far.
- Base initialization:
  $$
  cnt[0] = 1
  $$
  *(An empty subarray before index 0 has sum 0. If $s_i = k$, then $s_i - k = 0$, matching this base entry)*.

### 3. Execution Invariant:
For each element $x$:
1. $s \leftarrow s + x$.
2. Add $cnt[s - k]$ to total answer $ans$.
3. Increment $cnt[s] \leftarrow cnt[s] + 1$.

> **Order of Operations Invariant.** Querying $cnt[s - k]$ *before* incrementing $cnt[s]$ guarantees that empty subarrays of length 0 (which would require $k = 0$ within the same index) are never counted.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [1, 1, 1]$ with $k = 2$:

---

### Step 1: Initialize
- $cnt = \{0: 1\}$
- $s = 0, \; ans = 0$

---

### Step 2: Index 0 ($nums[0] = 1$)
- $s = 0 + 1 = 1$.
- Target: $s - k = 1 - 2 = -1$.
- $cnt[-1] = 0 \implies ans = 0$.
- Update map: $cnt[1] = 1$.
- Map: $\{0: 1, \; 1: 1\}$.

---

### Step 3: Index 1 ($nums[1] = 1$)
- $s = 1 + 1 = 2$.
- Target: $s - k = 2 - 2 = \mathbf{0}$.
- $cnt[0] = 1 \implies ans \leftarrow 0 + 1 = \mathbf{1}$.
  *(Subarray: $nums[0 \dots 1] = [1, 1]$)*.
- Update map: $cnt[2] = 1$.
- Map: $\{0: 1, \; 1: 1, \; 2: 1\}$.

---

### Step 4: Index 2 ($nums[2] = 1$)
- $s = 2 + 1 = 3$.
- Target: $s - k = 3 - 2 = \mathbf{1}$.
- $cnt[1] = 1 \implies ans \leftarrow 1 + 1 = \mathbf{2}$.
  *(Subarray: $nums[1 \dots 2] = [1, 1]$)*.
- Update map: $cnt[3] = 1$.
- Map: $\{0: 1, \; 1: 1, \; 2: 1, \; 3: 1\}$.

---

### Step 5: Final Result
$$
ans = \mathbf{2}
$$

---

## 4. Complete Execution Trace

| Index $i$ | Value $nums[i]$ | Running Sum $s$ | Target $s - k$ | Found in $cnt$? | Subarray Identified | Running Count $ans$ | Map After Step |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Init** | — | $0$ | — | — | — | $0$ | $\{0: 1\}$ |
| $0$ | $1$ | $1$ | $-1$ | $0$ | None | $0$ | $\{0: 1, 1: 1\}$ |
| $1$ | $1$ | $2$ | **$0$** | **$1$** | $nums[0 \dots 1]$ | **$1$** | $\{0: 1, 1: 1, 2: 1\}$ |
| $2$ | $1$ | $3$ | **$1$** | **$1$** | $nums[1 \dots 2]$ | **$2$** | $\{0: 1, 1: 1, 2: 1, 3: 1\}$ |
| **Result** | — | — | — | — | — | **`2`** | — |

---

## 5. Boundary Cases & Failure Modes

- **$k = 0$ with Zero Elements ($[0, 0]$):**
  - $i=0: s=0, target=0 \implies cnt[0]=1 \implies ans=1, cnt[0]=2$.
  - $i=1: s=0, target=0 \implies cnt[0]=2 \implies ans=1+2=3, cnt[0]=3$.
  - Correctly counts all 3 subarrays: $[0]$ at idx 0, $[0]$ at idx 1, $[0, 0]$.
- **Negative Numbers ($[1, -1, 0], k = 0$):** Prefix sum dips and rises; map accumulates occurrences without issue $\implies ans = 3$.
- **No Subarray Sums to $k$ ($[1, 2, 3], k = 10$):** Targets never match $\implies ans = 0$.

---

## 6. Traps & Common Anti-Patterns

- **Forgetting $\{0: 1\}$ Base Initialization:** Without $cnt[0] = 1$, any subarray starting at index $0$ will look for $s_i - k = 0$, find count 0, and be completely missed.
- **Using a Set Instead of a Counter:** Multiple different prefixes can produce the same cumulative sum (especially when zeros or positive/negative pairs exist). Storing counts in a frequency map (`Counter`) is mandatory.
- **Updating the Map Before Querying:** If you update $cnt[s] += 1$ before querying $cnt[s - k]$, when $k = 0$, you would count $s - 0 = s$ with an inflated count including the current index itself (counting an illegal 0-length subarray).

---

## 7. Complexity Derivation

- **Time Complexity:**
  - A single pass over the array of length $N$.
  - At each step, hash map lookup and insertion take $\mathcal{O}(1)$ average time.
  - Total Time: $\mathcal{O}(N)$. For $N = 2 \times 10^4$, finishes in $< 10$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space to store up to $N + 1$ unique prefix sum frequencies.
