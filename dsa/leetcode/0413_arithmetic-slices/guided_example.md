# Guided Example: Arithmetic Slices

We trace the step-by-step adjacent difference monitoring, consecutive run-length tracking, incremental triangular contribution summation ($\Delta ans = cnt$), and reset transitions on representative numerical arrays:

- **Input:** $nums = [1, 2, 3, 4, 5]$
- **Required output:** `6`
  - Total length: $N = 5$
  - Step 1 ($i = 2$, triplet $[1, 2, 3]$):
    - $3 - 2 = 2 - 1 = 1 \implies$ Difference matches ($d = 1$)
    - Run count: $cnt = 1$
    - Valid slices ending here: `[1, 2, 3]` (Length 3)
    - Running total: $ans = 0 + 1 = 1$
  - Step 2 ($i = 3$, quadruplet $[1, 2, 3, 4]$):
    - $4 - 3 = 3 - 2 = 1 \implies$ Difference matches ($d = 1$)
    - Run count: $cnt \leftarrow 1 + 1 = 2$
    - Valid slices ending here: `[2, 3, 4]` (Length 3), `[1, 2, 3, 4]` (Length 4)
    - Running total: $ans = 1 + 2 = 3$
  - Step 3 ($i = 4$, quintuplet $[1, 2, 3, 4, 5]$):
    - $5 - 4 = 4 - 3 = 1 \implies$ Difference matches ($d = 1$)
    - Run count: $cnt \leftarrow 2 + 1 = 3$
    - Valid slices ending here: `[3, 4, 5]` (Length 3), `[2, 3, 4, 5]` (Length 4), `[1, 2, 3, 4, 5]` (Length 5)
    - Running total: $ans = 3 + 3 = 6$
  - Final total arithmetic slices: $\mathbf{6}$
- **Short Array ($N < 3$):** $nums = [1, 2] \implies$ arithmetic slice requires at least 3 elements $\implies \mathbf{0}$
- **Discontinuous Difference:** $nums = [1, 2, 3, 8, 9, 10] \implies [1, 2, 3]$ gives 1, jump to 8 resets $cnt=0$, $[8, 9, 10]$ gives 1 $\implies 1 + 1 = \mathbf{2}$

This instance demonstrates linear dynamic programming with $O(1)$ state compression, mathematically proves why an arithmetic run of length $L$ contributes $T_{L-2} = \frac{(L-1)(L-2)}{2}$ subarrays, and derives $O(N)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $nums = [1, 2, 3, 4, 5]$:
Find the total number of **arithmetic subarrays** (contiguous sequences of at least 3 elements with identical consecutive differences):

```text
Array: [1,  2,  3,  4,  5]

Valid Arithmetic Subarrays:
  Length 3:
    [1, 2, 3]         (diff = 1)
    [2, 3, 4]         (diff = 1)
    [3, 4, 5]         (diff = 1)
  Length 4:
    [1, 2, 3, 4]      (diff = 1)
    [2, 3, 4, 5]      (diff = 1)
  Length 5:
    [1, 2, 3, 4, 5]   (diff = 1)

Total Arithmetic Slices: 3 + 2 + 1 = 6
```

### The Incremental Subarray Theorem
Suppose an array ends with a valid arithmetic sequence of length $k \ge 3$.
If the next element continues the same arithmetic difference:
- It forms a new length-3 slice with the previous 2 elements.
- It extends every existing arithmetic slice ending at the previous element by 1 element.
- Therefore, the number of new arithmetic slices ending at the current index is:
  $$
  cnt_i = cnt_{i-1} + 1
  $$
- If the difference does not match, no arithmetic slice of length $\ge 3$ can end at the current index, so $cnt_i = 0$.

This eliminates the need to inspect all $O(N^2)$ candidate pairs $(L, R)$.

---

## 2. Conceptual Foundation & Invariants

### 1. The Closed-Form Triplet Accumulation:
For a contiguous maximal arithmetic subsegment of length $L \ge 3$:
- Number of length-3 slices: $L - 2$
- Number of length-4 slices: $L - 3$
- $\dots$
- Number of length-$L$ slices: $1$
The sum is the $(L-2)$-th triangular number:
$$
\text{Total Slices} = \sum_{k=1}^{L-2} k = \frac{(L - 1)(L - 2)}{2}
$$

### 2. State Transition Function:
Iterate over pairs $(nums[i-1], nums[i])$:
- Let $d_i = nums[i] - nums[i-1]$.
- If $d_i == d_{i-1}$:
  $$
  cnt \leftarrow cnt + 1, \quad ans \leftarrow ans + cnt
  $$
- If $d_i \ne d_{i-1}$:
  $$
  d \leftarrow d_i, \quad cnt \leftarrow 0
  $$

> **Invariant.** At any index $i$, $cnt$ represents the exact number of valid arithmetic slices whose right boundary ends at index $i$, and $ans$ represents the cumulative sum of all arithmetic slices ending at or before $i$.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [1, 2, 3, 4, 5]$ ($N = 5$):
Initial state: $ans = 0, cnt = 0, d = \infty$.

---

### Step 1: Pair $(1, 2)$ at index 1
- Difference: $\Delta = 2 - 1 = \mathbf{1}$.
- Since $\Delta \ne d$ ($\infty$):
  $$
  d \leftarrow 1, \quad cnt \leftarrow 0
  $$
- Length processed is only 2 (need $\ge 3$ for a slice).
- $ans \leftarrow ans + cnt = 0 + 0 = \mathbf{0}$.

---

### Step 2: Pair $(2, 3)$ at index 2
- Difference: $\Delta = 3 - 2 = \mathbf{1}$.
- Compare with $d$: $\Delta == 1 == d$ (**Match!**).
- Increment run count:
  $$
  cnt \leftarrow 0 + 1 = \mathbf{1}
  $$
  - New slice ending at index 2: `[1, 2, 3]` (Length 3).
- Update cumulative total:
  $$
  ans \leftarrow 0 + 1 = \mathbf{1}
  $$

---

### Step 3: Pair $(3, 4)$ at index 3
- Difference: $\Delta = 4 - 3 = \mathbf{1}$.
- Compare with $d$: $\Delta == 1 == d$ (**Match!**).
- Increment run count:
  $$
  cnt \leftarrow 1 + 1 = \mathbf{2}
  $$
  - New slices ending at index 3:
    1. `[2, 3, 4]` (Length 3)
    2. `[1, 2, 3, 4]` (Length 4)
- Update cumulative total:
  $$
  ans \leftarrow 1 + 2 = \mathbf{3}
  $$

---

### Step 4: Pair $(4, 5)$ at index 4
- Difference: $\Delta = 5 - 4 = \mathbf{1}$.
- Compare with $d$: $\Delta == 1 == d$ (**Match!**).
- Increment run count:
  $$
  cnt \leftarrow 2 + 1 = \mathbf{3}
  $$
  - New slices ending at index 4:
    1. `[3, 4, 5]` (Length 3)
    2. `[2, 3, 4, 5]` (Length 4)
    3. `[1, 2, 3, 4, 5]` (Length 5)
- Update cumulative total:
  $$
  ans \leftarrow 3 + 3 = \mathbf{6}
  $$

---

## 4. Complete Execution Trace

| Index $i$ | Pair $(nums[i-1], nums[i])$ | Current Difference $\Delta$ | Stored Difference $d$ | Invariant Evaluation | Active Run $cnt$ | New Slices Ending at $i$ | Total Slices $ans$ |
|:---:|:---:|:---:|:---:|:---|:---:|:---|:---:|
| $0$ | $(-, 1)$ | — | $\infty$ | Array start | $0$ | None | $0$ |
| $1$ | $(1, 2)$ | $1$ | $\infty \to 1$ | First difference established | $0$ | None (Length $< 3$) | $0$ |
| $2$ | $(2, 3)$ | $1$ | $1$ | Match ($1 == 1$) | $1$ | `[1, 2, 3]` | **$1$** |
| $3$ | $(3, 4)$ | $1$ | $1$ | Match ($1 == 1$) | $2$ | `[2, 3, 4]`, `[1, 2, 3, 4]` | **$3$** |
| $4$ | $(4, 5)$ | $1$ | $1$ | Match ($1 == 1$) | $3$ | `[3, 4, 5]`, `[2, 3, 4, 5]`, `[1, 2, 3, 4, 5]` | **$6$** |

---

## 5. Boundary Cases & Failure Modes

- **Length Less Than 3 ($N < 3$):** Loops over pairwise adjacent elements zero or one time. $cnt$ never reaches 1. Returns $0$ directly.
- **Strictly Constant Array ($[3, 3, 3, 3]$):** Difference is $\Delta = 0$. Algorithm handles $0$ identically to non-zero differences, yielding $1 + 2 = 3$ slices.
- **Negative Differences ($[9, 7, 5, 3]$):** $\Delta = -2$. Runs identically, correctly identifying slices with decreasing arithmetic progressions.
- **Alternating Differences ($[1, 2, 4, 5, 7]$):** Differences alternate between $1$ and $2$. $cnt$ resets to 0 at every step, yielding total slices $0$.

---

## 6. Traps & Common Anti-Patterns

- **Brute-Force Subarray Checking ($O(N^3)$ or $O(N^2)$):** Enumerating all pairs $(i, j)$ and verifying arithmetic progression by scanning across $k \in [i, j]$ causes Time Limit Exceeded on arrays with $N = 5000$. Linear scan $O(N)$ with running counter $cnt$ executes in under 1 millisecond.
- **Recomputing Subarrays on Discontinuity:** Forgetting to reset $cnt = 0$ when a difference changes falsely merges two disjoint arithmetic progressions into one.
- **Integer Difference Underflow/Overflow:** In languages with fixed integer widths, differences between large positive and negative values could overflow if not stored in 64-bit integers. (Here numbers are bounded by $[-1000, 1000]$, safely within standard bounds).

---

## 7. Complexity Derivation

- **Time Complexity:**
  - The algorithm performs a single pass over the array of $N$ elements.
  - In each iteration, exactly one subtraction, one comparison, and one addition are performed in $O(1)$ time.
  - Total Time: $\mathcal{O}(N)$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$. The algorithm maintains only three integer variables: $ans, cnt, d$. No dynamic arrays, stacks, or memoization tables are allocated.