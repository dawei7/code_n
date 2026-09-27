# Guided Example: Number of Longest Increasing Subsequence

We trace the step-by-step coupled dynamic programming recurrence ($f[i]$ for maximum length, $cnt[i]$ for frequency of length-maximizing paths), predecessor link testing ($nums[j] < nums[i]$), length superiority updating ($f[i] < f[j] + 1 \implies cnt[i] = cnt[j]$), path multiplicity accumulation ($f[i] == f[j] + 1 \implies cnt[i] += cnt[j]$), and global LIS count aggregation on representative integer sequences:

- **Input:** $nums = [1, 3, 5, 4, 7]$
- **Required output:** `2`
  - Subsequence definitions:
    - An increasing subsequence must be **strictly increasing** ($a_1 < a_2 < a_3 < \dots$).
    - Objective:
      1. Determine the length of the Longest Increasing Subsequence (LIS).
      2. Count the **total number of distinct subsequences** that achieve this maximum length.
    - For $[1, 3, 5, 4, 7]$:
      - Subsequence 1: $[1, 3, 5, 7]$ (length 4)
      - Subsequence 2: $[1, 3, 4, 7]$ (length 4)
      - Maximum length is $4$, and exactly **2** distinct subsequences achieve it.
- **Dual-State Dynamic Programming Architecture:**
  - For each index $i \in [0, n - 1]$, maintain two coupled state variables:
    1. $f[i]$: The **maximum length** of a strictly increasing subsequence ending at index $i$.
    2. $cnt[i]$: The **number of distinct ways** to form an increasing subsequence of length $f[i]$ ending at index $i$.
  - **Base State:**
    - Every element alone forms an increasing subsequence of length 1:
      $$
      f[i] = 1, \quad cnt[i] = 1
      $$
  - **Coupled State Transitions:**
    - For each predecessor $j < i$ with $nums[j] < nums[i]$:
      - **Case A: Strict Length Improvement ($f[i] < f[j] + 1$):**
        - Extending subsequences from $j$ creates a new strictly longer subsequence!
        - Overwrite length: $f[i] \leftarrow f[j] + 1$.
        - Reset count to match the number of ways reaching $j$:
          $$
          cnt[i] \leftarrow cnt[j]
          $$
      - **Case B: Length Equality / Path Convergence ($f[i] == f[j] + 1$):**
        - Extending from $j$ yields an alternative path that ties the existing best length for $i$.
        - Accumulate the additional distinct paths:
          $$
          cnt[i] \leftarrow cnt[i] + cnt[j]
          $$
  - **Global Tracking:**
    - Maintain $mx = \max_i f[i]$ (global maximum length).
    - Maintain $ans$ (total count of subsequences of length $mx$).
- **Step-by-Step Worked Execution Trace on $[1, 3, 5, 4, 7]$:**
  - Length $n = 5$.
  - Initialize $f = [1, 1, 1, 1, 1]$ and $cnt = [1, 1, 1, 1, 1]$.
  - **Index $i = 0$ ($nums[0] = 1$):**
    - $f[0] = 1, \; cnt[0] = 1$. Subsequence: `[1]`.
    - Global: $mx = 1, \; ans = 1$.
  - **Index $i = 1$ ($nums[1] = 3$):**
    - Compare with $j = 0$ ($nums[0] = 1 < 3$):
      - $f[0] + 1 = 1 + 1 = 2 > f[1] = 1 \implies \mathbf{Strict\ Improvement!}$
      - $f[1] = 2, \quad cnt[1] = cnt[0] = 1$.
    - Subsequence ending at 1: `[1, 3]`.
    - Global: $mx = 2, \; ans = 1$.
  - **Index $i = 2$ ($nums[2] = 5$):**
    - Predecessor $j = 0$ ($1 < 5$): $f[2] \leftarrow 1 + 1 = 2, cnt[2] = 1$.
    - Predecessor $j = 1$ ($3 < 5$):
      - $f[1] + 1 = 2 + 1 = 3 > f[2] = 2 \implies \mathbf{Strict\ Improvement!}$
      - $f[2] = 3, \quad cnt[2] = cnt[1] = 1$.
    - Subsequence ending at 2: `[1, 3, 5]`.
    - Global: $mx = 3, \; ans = 1$.
  - **Index $i = 3$ ($nums[3] = 4$):**
    - Predecessor $j = 0$ ($1 < 4$): $f[3] \leftarrow 2, cnt[3] = 1$.
    - Predecessor $j = 1$ ($3 < 4$):
      - $f[1] + 1 = 2 + 1 = 3 > f[3] = 2 \implies \mathbf{Strict\ Improvement!}$
      - $f[3] = 3, \quad cnt[3] = cnt[1] = 1$.
    - Predecessor $j = 2$ ($5 \not< 4$): Skip.
    - Subsequence ending at 3: `[1, 3, 4]`.
    - Global: $mx = 3$, $f[3] == mx \implies ans \leftarrow 1 + cnt[3] = \mathbf{2}$.
  - **Index $i = 4$ ($nums[4] = 7$):**
    - Predecessor $j = 0$ ($1 < 7$): $f[4] = 2, cnt[4] = 1$.
    - Predecessor $j = 1$ ($3 < 7$): $f[4] = 3, cnt[4] = 1$.
    - Predecessor $j = 2$ ($5 < 7$):
      - $f[2] + 1 = 3 + 1 = 4 > f[4] = 3 \implies \mathbf{Strict\ Improvement!}$
      - $f[4] = 4, \quad cnt[4] = cnt[2] = 1$.
      - Path ending here: `[1, 3, 5, 7]`.
    - Predecessor $j = 3$ ($4 < 7$):
      - $f[3] + 1 = 3 + 1 = 4 == f[4] = 4 \implies \mathbf{Length\ Tie\ (Case\ B)!}$
      - Accumulate path multiplicity:
        $$
        cnt[4] \leftarrow cnt[4] + cnt[3] = 1 + 1 = \mathbf{2}
        $$
      - Both paths `[1, 3, 5, 7]` and `[1, 3, 4, 7]` converge at $nums[4] = 7$!
    - Update global tracking:
      - $f[4] = 4 > mx = 3 \implies \mathbf{New\ Global\ Maximum!}$
      - $mx \leftarrow 4$
      - $ans \leftarrow cnt[4] = \mathbf{2}$.
  - **Step 6: Emit Final Answer:**
    $$
    ans = \mathbf{2}
    $$
- **All Elements Equal ($nums = [2, 2, 2, 2, 2]$):**
  - Because elements must be *strictly* increasing, no element can follow another.
  - $f[i] = 1, cnt[i] = 1$ for all $i$.
  - Maximum length is $1$, with $ans = 1 + 1 + 1 + 1 + 1 = \mathbf{5}$ distinct singletons.

This instance demonstrates path counting on directed acyclic posets and coupled Bellman recurrence, mathematically proves why branching sum accumulation enumerates all maximal topological paths, and derives $O(N^2)$ runtime (or $O(N \log N)$ with Fenwick trees) and $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $nums$:
Find the **number of longest strictly increasing subsequences**.

```text
nums = [ 1, 3, 5, 4, 7 ]

Longest increasing subsequences:
  1. [ 1, 3, 5, 7 ]  (length 4)
  2. [ 1, 3, 4, 7 ]  (length 4)

Max Length = 4
Total Count = 2
```

### The Invariant of Coupled DP States
- To count optimal paths, each state must record both its **maximum length** and the **number of distinct ways** to reach that maximum length.
- When a strictly longer path is found, the count resets to the predecessor's count ($cnt[i] = cnt[j]$).
- When an equal-length path is found, the count accumulates ($cnt[i] += cnt[j]$).

---

## 2. Conceptual Foundation & Invariants

### 1. Coupled Recurrence Rules:
For $j < i$ with $nums[j] < nums[i]$:
- If $f[i] < f[j] + 1$:
  $$
  f[i] \leftarrow f[j] + 1, \quad cnt[i] \leftarrow cnt[j]
  $$
- If $f[i] == f[j] + 1$:
  $$
  cnt[i] \leftarrow cnt[i] + cnt[j]
  $$

### 2. Global Aggregation:
$$
mx = \max_{0 \le i < n} f[i]
$$
$$
ans = \sum_{i: f[i] = mx} cnt[i]
$$

> **Poset Path Multiplicity Invariant.** The number of maximal chains terminating at vertex $v_i$ in the comparability graph equals the sum of chain counts over all immediate lower neighbors achieving the maximum rank $f[i] - 1$.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [1, 3, 5, 4, 7]$:

---

### Step 1: Elements 1, 3
- $nums[0] = 1 \implies f = 1, cnt = 1$.
- $nums[1] = 3 \implies f = 2, cnt = 1$.

---

### Step 2: Elements 5, 4
- $nums[2] = 5 \implies f = 3, cnt = 1$ (via 3).
- $nums[3] = 4 \implies f = 3, cnt = 1$ (via 3).

---

### Step 3: Element 7
- From 5: length $3 + 1 = 4 \implies f[4] = 4, cnt[4] = 1$.
- From 4: length $3 + 1 = 4 == f[4] \implies cnt[4] \leftarrow 1 + 1 = \mathbf{2}$.

---

### Step 4: Output
- Global max length is 4.
- Total count is **`2`**.

---

## 4. Complete Execution Trace

| Index $i$ | Value $nums[i]$ | Valid Predecessors $j$ | Best Length $f[i]$ | Path Count $cnt[i]$ | Active Subsequences Ending at $i$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | $1$ | None | $1$ | $1$ | `[1]` |
| $1$ | $3$ | $j = 0$ | $2$ | $1$ | `[1, 3]` |
| $2$ | $5$ | $j \in \{0, 1\}$ | $3$ | $1$ | `[1, 3, 5]` |
| $3$ | $4$ | $j \in \{0, 1\}$ | $3$ | $1$ | `[1, 3, 4]` |
| **$4$** | **$7$** | **$j \in \{0, 1, 2, 3\}$** | **`4`** | **`2`** | **`[1, 3, 5, 7]` and `[1, 3, 4, 7]`** |

---

## 5. Boundary Cases & Failure Modes

- **Strictly Decreasing Array ($[5, 4, 3, 2, 1]$):** $f[i] = 1$ for all; count is $N$.
- **Strictly Increasing Array ($[1, 2, 3, 4, 5]$):** Exactly 1 subsequence of length $N \implies 1$.
- **All Equal Elements ($[2, 2, 2]$):** No element can follow another $\implies$ count is $N$.
- **Single Element ($[1]$):** 1 subsequence of length 1 $\implies 1$.

---

## 6. Traps & Common Anti-Patterns

- **Only Storing Lengths:** Standard LIS only computes $f[i]$; without coupled count tracking, recovering the number of distinct sequences requires exponential backtracking.
- **Forgetting to Reset Count on Length Improvement:** If $f[i] < f[j] + 1$, you must set $cnt[i] = cnt[j]$, NOT $cnt[i] += cnt[j]$. Adding is only done on length equality.
- **Non-Strict Inequality ($nums[j] \le nums[i]$):** The problem strictly requires increasing sequences ($nums[j] < nums[i]$).

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Double loop over $0 \le j < i < N$: $\frac{N(N-1)}{2}$ comparisons.
  - Total Time: $\mathcal{O}(N^2)$ (can be optimized to $\mathcal{O}(N \log N)$ with a Fenwick tree or Segment tree).
  - For $N = 2000$, executes $\approx 2 \times 10^6$ operations, completing in $< 25$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space for the $f$ and $cnt$ arrays.
