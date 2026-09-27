# Guided Example: Max Consecutive Ones II

We trace the step-by-step sliding window expansion, zero-budget tracking ($\le 1$ zero flipped), left-pointer contraction ($cnt > 1$), non-shrinking maximum window frame ($N - l$), and continuous run bridging on representative binary arrays:

- **Input:** $nums = [1, 0, 1, 1, 0]$
- **Required output:** `4`
  - Array length: $N = 5$
  - Budget: At most $1$ zero may be flipped to a $1$.
  - Objective: Maximum length of a contiguous subarray containing at most one zero.
- **Sliding window execution trace:**
  - Pointers: left boundary $l = 0$, zero counter $cnt = 0$
  - **Index 0 ($x = 1$):**
    - $x = 1 \implies cnt += 0$ ($cnt = 0 \le 1$)
    - Window $[0 \dots 0] = [1]$ (Length 1)
  - **Index 1 ($x = 0$):**
    - $x = 0 \implies cnt += 1$ ($cnt = 1 \le 1$, budget intact!)
    - Window $[0 \dots 1] = [1, 0]$ (Length 2)
  - **Index 2 ($x = 1$):**
    - $x = 1 \implies cnt = 1 \le 1$
    - Window $[0 \dots 2] = [1, 0, 1]$ (Length 3)
  - **Index 3 ($x = 1$):**
    - $x = 1 \implies cnt = 1 \le 1$
    - Window $[0 \dots 3] = [1, 0, 1, 1]$ (Length 4)
  - **Index 4 ($x = 0$):**
    - $x = 0 \implies cnt += 1$ ($cnt = 2 > 1$, budget exceeded!)
    - Shift left boundary to expel earliest zero:
      - At $l = 0$, $nums[0] = 1 \implies cnt$ remains $2$. Advance $l \leftarrow 1$.
      - Window size maintained at $4$ ($r - l + 1 = 4 - 1 + 1 = 4$).
  - Final maximum window size:
    $$
    N - l = 5 - 1 = \mathbf{4}
    $$
  - Subarray $[1, 0, 1, 1]$ (indices $0 \dots 3$) with the zero flipped produces $4$ consecutive ones.
- **Middle Run Instance ($nums = [1, 0, 1, 1, 0, 1]$):**
  - Subarrays with 1 zero: $[1, 0, 1, 1]$ (len 4) and $[1, 1, 0, 1]$ (len 4) $\implies \mathbf{4}$
- **All Ones ($nums = [1, 1, 1]$):**
  - $cnt$ stays $0 \implies$ window spans entire array $\implies \mathbf{3}$
- **All Zeroes ($nums = [0, 0, 0]$):**
  - Can flip at most one zero $\implies \mathbf{1}$

This instance demonstrates sliding window rate-limiting with budget constraints, mathematically proves why a non-shrinking window preserves the historical maximum in a single pass, and derives $O(N)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a binary array $nums = [1, 0, 1, 1, 0]$:
Find the **maximum number of consecutive `1`s** in the array if you can **flip at most one `0`**.

```text
Array:               [ 1,   0,   1,   1,   0 ]
Flip First Zero:     [ 1,  (1),  1,   1,   0 ] -> Length 4
Flip Second Zero:    [ 1,   0,   1,  (1), (1)] -> Length 3

Maximum Length = 4 (Subarray [1, 0, 1, 1])
```

### Problem Reduction to Bounded-Zero Subarrays
- Flipping at most one `0` to `1` means:
  We are searching for the **longest contiguous subarray that contains at most ONE zero**!
- Once found, flipping that single zero inside the subarray transforms the entire segment into a contiguous streak of ones.

---

## 2. Conceptual Foundation & Invariants

### 1. Two-Pointer Window Invariant:
Let $[l, r]$ denote the current sliding window:
- Count of zeroes inside the window: $cnt = \sum_{i=l}^r (nums[i] \oplus 1)$.
- **Feasibility Condition:**
  $$
  cnt \le 1
  $$
- While $cnt \le 1$, the window is valid, and its length is $r - l + 1$.

### 2. The Non-Shrinking Window Optimization:
Instead of shrinking $l$ all the way until $cnt \le 1$:
- We simply advance $l$ by **at most 1 step** whenever $cnt > 1$:
  $$
  \text{if } cnt > 1: \quad cnt \leftarrow cnt - (nums[l] \oplus 1), \quad l \leftarrow l + 1
  $$
- This prevents the window size from ever decreasing!
- The window expands whenever a larger valid window is found, and shifts without shrinking otherwise.
- At the end of the array, the maximum window length is simply:
  $$
  \text{Max Length} = N - l
  $$

> **Window Monotonicity Invariant.** The span $N - l$ monotonically tracks the maximum valid window width discovered across the entire prefix without requiring separate max tracking.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [1, 0, 1, 1, 0]$ ($N = 5$):
Initialize $l = 0, \; cnt = 0$.

---

### Step 1: Right Pointer $r = 0$ ($x = 1$)
- $nums[0] = 1 \implies x \oplus 1 = 0 \implies cnt = 0$.
- $cnt \le 1$ (Valid).
- Window $[0 \dots 0]$ has length $1$.

---

### Step 2: Right Pointer $r = 1$ ($x = 0$)
- $nums[1] = 0 \implies x \oplus 1 = 1 \implies cnt \leftarrow 0 + 1 = 1$.
- $cnt \le 1$ (Valid: 1 zero flipped).
- Window $[0 \dots 1]$ has length $2$.

---

### Step 3: Right Pointer $r = 2$ ($x = 1$)
- $nums[2] = 1 \implies cnt = 1$.
- $cnt \le 1$ (Valid).
- Window $[0 \dots 2]$ has length $3$.

---

### Step 4: Right Pointer $r = 3$ ($x = 1$)
- $nums[3] = 1 \implies cnt = 1$.
- $cnt \le 1$ (Valid).
- Window $[0 \dots 3]$ has length $4$.

---

### Step 5: Right Pointer $r = 4$ ($x = 0$)
- $nums[4] = 0 \implies cnt \leftarrow 1 + 1 = \mathbf{2}$.
- Condition $cnt > 1$ triggered (two zeroes in window):
  - Slide left boundary by 1 step:
    $$
    cnt \leftarrow cnt - (nums[0] \oplus 1) = 2 - (1 \oplus 1) = 2 - 0 = 2
    $$
    $$
    l \leftarrow 0 + 1 = \mathbf{1}
    $$
- Window shifts to $[1 \dots 4]$, preserving width $4$.

---

### Step 6: Final Answer
$$
\text{Result} = N - l = 5 - 1 = \mathbf{4}
$$

---

## 4. Complete Execution Trace

| Step $r$ | Value $nums[r]$ | Bit Flip $x \oplus 1$ | Zero Count $cnt$ | Condition $cnt > 1$? | Left Pointer $l$ | Effective Window Size |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **$0$** | $1$ | $0$ | $0$ | No | $0$ | $1$ |
| **$1$** | $0$ | $1$ | $1$ | No | $0$ | $2$ |
| **$2$** | $1$ | $0$ | $1$ | No | $0$ | $3$ |
| **$3$** | $1$ | $0$ | $1$ | No | $0$ | **$4$** |
| **$4$** | $0$ | $1$ | $2$ | **Yes** | $1$ | **$4$** |
| **Final** | — | — | — | — | $l = 1$ | **$N - l = 4$** |

---

## 5. Boundary Cases & Failure Modes

- **Single Zero ($nums = [0]$):** $cnt$ reaches 1 $\implies l = 0 \implies N - l = 1 - 0 = \mathbf{1}$ (flipping the single zero yields 1).
- **Single One ($nums = [1]$):** $cnt = 0 \implies l = 0 \implies \mathbf{1}$.
- **All Zeroes ($[0, 0, 0]$):** Can only flip 1 zero $\implies \mathbf{1}$.
- **All Ones ($[1, 1, 1, 1]$):** $cnt$ remains $0 \implies \mathbf{4}$.

---

## 6. Traps & Common Anti-Patterns

- **Searching for Zero Indices and Re-scanning:** Storing all zero indices and re-counting between them takes $O(N)$ extra space and requires multiple passes. Sliding window solves it in a single continuous stream pass.
- **Forgetting that Budget is 1:** Trying to use a dynamic programming table of size $N \times 2$ works, but wastes unnecessary memory when two pointers operate in $O(1)$ space.
- **Shrinking Window Completely with While Loops:** While a `while cnt > 1: l += 1` loop is correct, a non-shrinking `if cnt > 1: l += 1` is cleaner and directly guarantees $N - l$ equals the maximum.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - The right pointer visits each of the $N$ elements once.
  - The left pointer advances at most once per iteration.
  - Total Time: $\mathcal{O}(N)$. For $N = 10^5$, runs in $< 5$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ space using scalar pointers $l$ and $cnt$.
