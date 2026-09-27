# Guided Example: Shortest Unsorted Continuous Subarray

We trace the step-by-step sorted reference alignment ($arr = \text{sorted}(nums)$), left and right monotonic boundary shrinking ($l, r$), first-inversion coordinate discovery, already-sorted empty interval handling ($l > r$), and minimal subarray length evaluation ($r - l + 1$) on representative integer arrays:

- **Input:** $nums = [2, 6, 4, 8, 10, 9, 15]$
- **Required output:** `5`
  - Problem goal: Identify the shortest contiguous subarray $nums[l \dots r]$ such that sorting only this window puts the entire array into non-decreasing order.
  - Return the length of this subarray: $r - l + 1$ (or $0$ if already sorted).
- **Sorted Reference Comparison Principle:**
  - Let $arr$ be the ideal, fully sorted version of $nums$.
  - In any valid solution:
    - Any prefix $nums[0 \dots l-1]$ that is already identical to $arr[0 \dots l-1]$ does **not** need to be touched.
    - Any suffix $nums[r+1 \dots n-1]$ that is already identical to $arr[r+1 \dots n-1]$ does **not** need to be touched.
    - The minimal subarray that must be rearranged spans from the **first index where $nums$ deviates from $arr$** on the left to the **first index where $nums$ deviates from $arr$** on the right!
- **Step-by-Step Worked Trace:**
  - **Step 1: Construct Sorted Reference:**
    $$
    nums = [2, \; 6, \; 4, \; 8, \; 10, \; 9, \; 15]
    $$
    $$
    arr = [2, \; 4, \; 6, \; 8, \; 9, \; 10, \; 15]
    $$
  - **Step 2: Two-Pointer Boundary Initialization:**
    - Set left pointer at start: $l = 0$.
    - Set right pointer at end: $r = n - 1 = 6$.
  - **Step 3: Advance Left Pointer $l$ Past Matching Prefix:**
    - Index $0$: $nums[0] = 2, \; arr[0] = 2 \implies$ Match! Advance $l \leftarrow 1$.
    - Index $1$: $nums[1] = 6, \; arr[1] = 4 \implies$ **Mismatch! ($6 \ne 4$)**
    - Stop left pointer at:
      $$
      l = \mathbf{1}
      $$
  - **Step 4: Retreat Right Pointer $r$ Past Matching Suffix:**
    - Index $6$: $nums[6] = 15, \; arr[6] = 15 \implies$ Match! Retreat $r \leftarrow 5$.
    - Index $5$: $nums[5] = 9, \; arr[5] = 10 \implies$ **Mismatch! ($9 \ne 10$)**
    - Stop right pointer at:
      $$
      r = \mathbf{5}
      $$
  - **Step 5: Compute Subarray Length:**
    - Left boundary: $l = 1$.
    - Right boundary: $r = 5$.
    - Unsorted window spans $nums[1 \dots 5] = [6, 4, 8, 10, 9]$.
    - Length:
      $$
      r - l + 1 = 5 - 1 + 1 = \mathbf{5}
      $$
    - *(Sorting $[6, 4, 8, 10, 9] \to [4, 6, 8, 9, 10]$ results in the fully sorted array $[2, 4, 6, 8, 9, 10, 15]$!)*
- **Already Sorted Array Instance ($nums = [1, 2, 3, 4]$):**
  - $arr = [1, 2, 3, 4]$.
  - Pointer $l$ advances all the way past $r$ ($l = 4, r = -1$).
  - $r - l + 1 = -1 - 4 + 1 = -4 \le 0 \implies \mathbf{0}$.
- **Completely Inverted Array ($nums = [5, 4, 3, 2, 1]$):**
  - Mismatches at indices $0$ and $4 \implies l = 0, r = 4 \implies 4 - 0 + 1 = \mathbf{5}$.
- **Single Displaced Element ($nums = [1, 3, 2, 4]$):**
  - Mismatches at indices $1$ and $2 \implies l = 1, r = 2 \implies 2 - 1 + 1 = \mathbf{2}$.

This instance demonstrates boundary contraction relative to monotonic canonical references, mathematically proves why the outermost mismatch positions define the minimal necessary permutation interval, and derives $O(N \log N)$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $nums$:
Find the **length of the shortest contiguous subarray** that, if sorted, makes the entire array sorted.
If the array is already sorted, return `0`.

```text
nums: [ 2,  6,  4,  8,  10,  9,  15 ]
arr:  [ 2,  4,  6,  8,   9, 10,  15 ]
            ^                ^
         l = 1            r = 5

Subarray nums[1..5] = [6, 4, 8, 10, 9]
Length = 5 - 1 + 1 = 5
```

### The Boundary Mismatch Theorem
- An element $nums[i]$ is in its correct global position if and only if:
  1. All elements to its left are $\le nums[i]$.
  2. All elements to its right are $\ge nums[i]$.
- In the sorted reference array $arr = \text{sorted}(nums)$, this is guaranteed everywhere.
- Any element $nums[i] \ne arr[i]$ is out of place and must be contained inside the rearranged window $[l, r]$.
- Therefore, $l$ is the **first mismatch from the left**, and $r$ is the **first mismatch from the right**.

---

## 2. Conceptual Foundation & Invariants

### 1. The Algorithm:
1. Create sorted copy $arr = \text{sorted}(nums)$.
2. Initialize $l = 0, \; r = n - 1$.
3. Advance $l$ while $l \le r$ and $nums[l] == arr[l]$.
4. Retreat $r$ while $l \le r$ and $nums[r] == arr[r]$.
5. Return $\max(0, r - l + 1)$.

> **Prefix-Suffix Monotonicity Invariant.** The prefix $nums[0 \dots l-1]$ and suffix $nums[r+1 \dots n-1]$ are already sorted and strictly bound all values within the central window $[l, r]$.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [2, 6, 4, 8, 10, 9, 15]$:

---

### Step 1: Create Sorted Copy
- $nums = [2, 6, 4, 8, 10, 9, 15]$
- $arr  = [2, 4, 6, 8, 9, 10, 15]$

---

### Step 2: Left Pointer Scan
- $nums[0] == arr[0]$ ($2 == 2$) $\to l = 1$.
- $nums[1] \ne arr[1]$ ($6 \ne 4$) $\to$ Stop at $l = \mathbf{1}$.

---

### Step 3: Right Pointer Scan
- $nums[6] == arr[6]$ ($15 == 15$) $\to r = 5$.
- $nums[5] \ne arr[5]$ ($9 \ne 10$) $\to$ Stop at $r = \mathbf{5}$.

---

### Step 4: Calculate Length
$$
r - l + 1 = 5 - 1 + 1 = \mathbf{5}
$$

---

## 4. Complete Execution Trace

| Index | $nums[i]$ | $arr[i]$ | Match Status | Pointer Actions | Subarray Status |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | $2$ | $2$ | Match | $l$ advances to $1$ | Preserved prefix |
| **$1$** | **$6$** | **$4$** | **Mismatch** | **$l$ stops at $1$** | **Left boundary** |
| $2$ | $4$ | $6$ | Mismatch | — | Inside window |
| $3$ | $8$ | $8$ | Match | — | Inside window |
| $4$ | $10$ | $9$ | Mismatch | — | Inside window |
| **$5$** | **$9$** | **$10$** | **Mismatch** | **$r$ stops at $5$** | **Right boundary** |
| $6$ | $15$ | $15$ | Match | $r$ retreats past $6$ | Preserved suffix |
| **Result** | — | — | — | — | **Length: $5 - 1 + 1 = \mathbf{5}$** |

---

## 5. Boundary Cases & Failure Modes

- **Already Sorted ($[1, 2, 3]$):** $l$ crosses $r$ ($l = 3, r = -1$) $\implies r - l + 1 \le 0 \implies \mathbf{0}$.
- **Two Inverted Elements ($[1, 3, 2, 4]$):** Window is $[3, 2]$ of length $2$.
- **All Identical Elements ($[1, 1, 1]$):** Fully matches sorted copy $\implies \mathbf{0}$.
- **Duplicate Values with Mismatches ($[1, 3, 2, 2, 2]$):** Matches correctly identify the bounds of the disorder.

---

## 6. Traps & Common Anti-Patterns

- **Searching for Adjacent Decreases Only:** Finding where $nums[i] > nums[i+1]$ fails to capture the full window. In `[1, 3, 2, 2, 2]`, the decrease is between 3 and 2, but all three 2s must be included in the sort.
- **Returning Negative Length for Sorted Arrays:** If $nums$ is already sorted, $l > r$. Ensure negative differences return $0$.
- **Sorting in Place:** Modifying the input array destroys the original order before pointer comparison. Always sort into a separate reference array.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Sorting $nums$ takes $\mathcal{O}(N \log N)$ time.
  - The two while loops take at most $N$ comparisons.
  - Total Time: $\mathcal{O}(N \log N)$. For $N = 10^4$, completes in $< 3$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space to store the sorted reference array $arr$.
