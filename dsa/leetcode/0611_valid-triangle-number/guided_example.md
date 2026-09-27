# Guided Example: Valid Triangle Number

We trace the step-by-step array pre-sorting, sorted triangle inequality simplification ($a \le b \le c \implies a + b > c$), dual two-pointer interval spanning ($r - l$), monotonic pointer contraction, and valid triplet count aggregation on representative side-length arrays:

- **Input:** $nums = [2, 2, 3, 4]$
- **Required output:** `3`
  - Valid triangle condition: Three lengths $a, b, c$ can form a non-degenerate triangle if and only if:
    $$
    a + b > c, \quad a + c > b, \quad b + c > a
    $$
- **Sorted Metric Simplification & Two-Pointer Invariant:**
  - If we sort the array in non-decreasing order:
    $$
    nums[i] \le nums[j] \le nums[k] \quad (i < j < k)
    $$
  - Because $nums[k] \ge nums[j]$ and $nums[k] \ge nums[i]$, the inequalities:
    $$
    nums[i] + nums[k] > nums[j] \quad \text{and} \quad nums[j] + nums[k] > nums[i]
    $$
    are **trivially guaranteed** for all positive lengths!
  - Therefore, the three inequalities collapse into a **single necessary and sufficient check**:
    $$
    nums[i] + nums[j] > nums[k]
    $$
  - **Two-Pointer Range Counting ($O(N^2)$):**
    - Fix the longest side index $k$ from $n - 1$ down to $2$.
    - Place two pointers for the two smaller sides:
      - Left pointer $l = 0$
      - Right pointer $r = k - 1$
    - Test the condition:
      $$
      nums[l] + nums[r] > nums[k]
      $$
    - **Case 1: $nums[l] + nums[r] > nums[k]$:**
      - Since the array is sorted, any element between $l$ and $r$ is $\ge nums[l]$.
      - Thus, paired with $nums[r]$, every index $m \in [l, r - 1]$ will also satisfy:
        $$
        nums[m] + nums[r] \ge nums[l] + nums[r] > nums[k]
        $$
      - There are exactly $r - l$ such valid indices!
      - Add $r - l$ directly to total count.
      - Decrement $r \leftarrow r - 1$ to test smaller pairs.
    - **Case 2: $nums[l] + nums[r] \le nums[k]$:**
      - The sum is too small to exceed $nums[k]$.
      - Increment $l \leftarrow l + 1$ to increase the sum.
- **Step-by-Step Worked Execution Trace on $[2, 2, 3, 4]$:**
  - Array is already sorted: $nums = [2, 2, 3, 4]$, length $n = 4$.
  - Initialize $ans = 0$.
  - **Iteration 1: Fix Longest Side $k = 3$ ($nums[k] = 4$):**
    - Pointers: $l = 0$ ($nums[l] = 2$), $r = 2$ ($nums[r] = 3$).
    - Check sum:
      $$
      nums[l] + nums[r] = 2 + 3 = 5
      $$
      $$
      5 > 4 \implies \mathbf{Valid!}
      $$
    - Valid pairs with $nums[r] = 3$:
      - Index $l=0$: pair $(nums[0], nums[2]) = (2, 3)$ with $4 \implies (2, 3, 4)$
      - Index $l=1$: pair $(nums[1], nums[2]) = (2, 3)$ with $4 \implies (2, 3, 4)$
    - Number of valid pairs:
      $$
      r - l = 2 - 0 = \mathbf{2}
      $$
    - Accumulate:
      $$
      ans \leftarrow 0 + 2 = \mathbf{2}
      $$
    - Move right pointer inward: $r \leftarrow 2 - 1 = 1$.
    - New pointers: $l = 0$ ($nums[l] = 2$), $r = 1$ ($nums[r] = 2$).
    - Check sum:
      $$
      nums[l] + nums[r] = 2 + 2 = 4
      $$
      $$
      4 \ngtr 4 \implies \mathbf{Too\ small!}
      $$
    - Move left pointer forward: $l \leftarrow 0 + 1 = 1$.
    - Pointers meet ($l == r == 1$). Finished for $k = 3$.
  - **Iteration 2: Fix Longest Side $k = 2$ ($nums[k] = 3$):**
    - Pointers: $l = 0$ ($nums[l] = 2$), $r = 1$ ($nums[r] = 2$).
    - Check sum:
      $$
      nums[l] + nums[r] = 2 + 2 = 4
      $$
      $$
      4 > 3 \implies \mathbf{Valid!}
      $$
    - Number of valid pairs:
      $$
      r - l = 1 - 0 = \mathbf{1} \quad (\text{triplet } (2, 2, 3))
      $$
    - Accumulate:
      $$
      ans \leftarrow 2 + 1 = \mathbf{3}
      $$
    - Decrement right pointer: $r \leftarrow 0$.
    - Pointers meet ($l > r$). Finished for $k = 2$.
  - **Termination:**
    - Longest side index $k$ has reached minimum ($k < 2$).
    - Total valid triplets:
      $$
      ans = \mathbf{3}
      $$
    - The 3 valid triplets are:
      1. Indices $(0, 2, 3) \implies (2, 3, 4)$
      2. Indices $(1, 2, 3) \implies (2, 3, 4)$
      3. Indices $(0, 1, 2) \implies (2, 2, 3)$
- **Zero-Length Elements Handling ($nums = [0, 1, 1, 1]$):**
  - Any triangle involving side $0$ has $0 + 1 \ngtr 1$, so it is automatically rejected by the strict inequality $a + b > c$.
- **All Identical Elements ($[2, 2, 2, 2]$):**
  - All $\binom{4}{3} = 4$ combinations form valid equilateral triangles $\implies ans = 4$.

This instance demonstrates two-pointer boundary sweeping on monotonic sequences, mathematically proves why sorting collapses 3-variable geometric constraints into single-inequality interval summations, and derives $O(N^2)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $nums$:
Count how many triplets $(i, j, k)$ can form the side lengths of a valid triangle.

```text
nums = [2, 2, 3, 4]

Triplets tested:
  (2, 3, 4) -> 2 + 3 = 5 > 4 (Valid!)
  (2, 3, 4) -> 2 + 3 = 5 > 4 (Valid!)
  (2, 2, 3) -> 2 + 2 = 4 > 3 (Valid!)
  (2, 2, 4) -> 2 + 2 = 4 <= 4 (Invalid)

Total valid triplets = 3
```

### The Sorted Triangle Theorem
- For three sides $a \le b \le c$:
  - $a + c > b$ is always true (since $c \ge b$ and $a > 0$).
  - $b + c > a$ is always true (since $c \ge a$ and $b > 0$).
- Thus, once the array is sorted, only **one check** is needed:
  $$
  a + b > c
  $$
- This reduces 3D geometric testing to a 2D sorted interval search.

---

## 2. Conceptual Foundation & Invariants

### 1. Reverse Two-Pointer Technique:
- Fix the hypotenuse/largest side $k$ from $n - 1$ down to 2.
- Set $l = 0$ and $r = k - 1$.
- While $l < r$:
  - If $nums[l] + nums[r] > nums[k]$:
    - All elements between $l$ and $r-1$ paired with $r$ also exceed $nums[k]$.
    - Add $r - l$ to total count.
    - $r \leftarrow r - 1$.
  - Else:
    - $l \leftarrow l + 1$.

> **Monotonic Interval Invariant.** In a non-decreasing array, if $nums[l] + nums[r] > nums[k]$, then for all $m$ satisfying $l \le m < r$, $nums[m] + nums[r] \ge nums[l] + nums[r] > nums[k]$, ensuring all $r - l$ pairs are simultaneously valid.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [2, 2, 3, 4]$:

---

### Step 1: Fix $k = 3$ ($nums[k] = 4$)
- $l = 0$ ($nums[l] = 2$), $r = 2$ ($nums[r] = 3$).
- $2 + 3 = 5 > 4 \implies$ Add $r - l = 2 - 0 = \mathbf{2}$.
- $r \leftarrow 1$.
- $l = 0$ ($nums[l] = 2$), $r = 1$ ($nums[r] = 2$).
- $2 + 2 = 4 \ngtr 4 \implies l \leftarrow 1$.
- $l == r \implies$ End iteration for $k = 3$. Subtotal = 2.

---

### Step 2: Fix $k = 2$ ($nums[k] = 3$)
- $l = 0$ ($nums[l] = 2$), $r = 1$ ($nums[r] = 2$).
- $2 + 2 = 4 > 3 \implies$ Add $r - l = 1 - 0 = \mathbf{1}$.
- $r \leftarrow 0$.
- $l > r \implies$ End iteration for $k = 2$. Subtotal = $2 + 1 = 3$.

---

### Step 3: Return Total
$$
ans = \mathbf{3}
$$

---

## 4. Complete Execution Trace

| Fixed Largest Index $k$ | $nums[k]$ | Left Ptr $l$ | Right Ptr $r$ | Sum $nums[l] + nums[r]$ | Sum $> nums[k]$? | Add $r - l$ | Running $ans$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $3$ | $4$ | $0$ ($2$) | $2$ ($3$) | $5$ | **Yes** | $+2$ | $2$ |
| $3$ | $4$ | $0$ ($2$) | $1$ ($2$) | $4$ | No | $+0$ | $2$ |
| **$2$** | **$3$** | **$0$ ($2$)** | **$1$ ($2$)** | **$4$** | **Yes** | **$+1$** | **`3`** |
| **End** | — | — | — | — | — | — | **`3`** |

---

## 5. Boundary Cases & Failure Modes

- **Less Than 3 Elements ($N < 3$):** Cannot form a triangle $\implies 0$.
- **Zeros in Array ($[0, 0, 0]$):** $0 + 0 \ngtr 0 \implies 0$.
- **Collinear Sides ($[1, 2, 3]$):** $1 + 2 = 3 \ngtr 3 \implies 0$.
- **Strictly Increasing Run ($[3, 4, 5, 6]$):** Multiple triangles counted efficiently.

---

## 6. Traps & Common Anti-Patterns

- **Brute Force Three Nested Loops ($O(N^3)$):** Checking all $\binom{N}{3}$ triplets times out for $N = 1000$.
- **Binary Search ($O(N^2 \log N)$) vs Two Pointers ($O(N^2)$):** While binary search passes, two pointers with fixed $k$ eliminates the $\log N$ factor.
- **Counting Permutations Instead of Combinations:** Triplet indices must satisfy $i < j < k$; do not multiply by permutations.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Sorting the array: $\mathcal{O}(N \log N)$.
  - Outer loop for $k$ runs $N - 2$ times.
  - Inner two-pointer loop advances $l$ or decrements $r$ at each step, running in $\mathcal{O}(N)$ amortized time.
  - Total Time: $\mathcal{O}(N^2)$. For $N = 1000$, completes in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ auxiliary space beyond input sorting memory.
