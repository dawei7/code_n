# Guided Example: Find All Duplicates in an Array

We trace the step-by-step in-place cyclic sort index mapping ($nums[i] \leftrightarrow nums[nums[i] - 1]$), canonical bucket placement, duplicate collision detection, and mismatched index collection on representative permutation arrays:

- **Input:** $nums = [4, 3, 2, 7, 8, 2, 3, 1]$
- **Required output:** `[2, 3]` (in any order)
  - Array length: $n = 8$, values in range $[1, 8]$
  - Canonical placement rule: value $v$ belongs at 0-indexed position $v - 1$.
- **Cyclic sort execution trace:**
  - **At Index 0 ($nums[0] = 4$):**
    - Target for 4 is index $3$. $nums[3] = 7$.
    - Swap $nums[0] \leftrightarrow nums[3] \implies nums = [7, 3, 2, \mathbf{4}, 8, 2, 3, 1]$
    - Now $nums[0] = 7$. Target index is $6$. $nums[6] = 3$.
    - Swap $nums[0] \leftrightarrow nums[6] \implies nums = [3, 3, 2, 4, 8, 2, \mathbf{7}, 1]$
    - Now $nums[0] = 3$. Target index is $2$. $nums[2] = 2$.
    - Swap $nums[0] \leftrightarrow nums[2] \implies nums = [2, 3, \mathbf{3}, 4, 8, 2, 7, 1]$
    - Now $nums[0] = 2$. Target index is $1$. $nums[1] = 3$.
    - Swap $nums[0] \leftrightarrow nums[1] \implies nums = [3, \mathbf{2}, 3, 4, 8, 2, 7, 1]$
    - Now $nums[0] = 3$. Target index $2$ already contains $nums[2] = 3$ (Collision!).
    - Stop swapping at index 0.
  - **At Index 4 ($nums[4] = 8$):**
    - Target for 8 is index $7$. $nums[7] = 1$.
    - Swap $nums[4] \leftrightarrow nums[7] \implies nums = [3, 2, 3, 4, 1, 2, 7, \mathbf{8}]$
    - Now $nums[4] = 1$. Target index is $0$. $nums[0] = 3$.
    - Swap $nums[4] \leftrightarrow nums[0] \implies nums = [\mathbf{1}, 2, 3, 4, \mathbf{3}, 2, 7, 8]$
    - Now $nums[4] = 3$. Target index $2$ already has $3$. Stop.
  - Final sorted array state:
    $$
    nums = [1, \; 2, \; 3, \; 4, \; \mathbf{3}, \; \mathbf{2}, \; 7, \; 8]
    $$
  - Filter positions where $nums[i] \ne i + 1$:
    - Index 4: $nums[4] = 3 \ne 5 \implies \mathbf{3}$ is a duplicate!
    - Index 5: $nums[5] = 2 \ne 6 \implies \mathbf{2}$ is a duplicate!
  - Output: `[2, 3]`
- **No Duplicates Instance:** $nums = [1, 2, 3] \implies nums[i] == i + 1$ for all $i \implies \mathbf{[]}$
- **All Pairs Duplicated:** $nums = [1, 1, 2, 2] \implies \mathbf{[1, 2]}$

This instance demonstrates in-place cyclic sort and sign-negation index mapping, mathematically proves why each element is swapped at most twice across the entire array ($O(N)$ total swaps), and derives $O(N)$ runtime and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $nums = [4, 3, 2, 7, 8, 2, 3, 1]$ of length $n = 8$:
All integers are in the range $[1, n]$ and each integer appears **once or twice**.
Find all integers that appear **twice** in **$O(N)$ runtime** and using only **$O(1)$ auxiliary space**:

```text
Input Array:   [ 4,  3,  2,  7,  8,  2,  3,  1 ]
Indices:         0   1   2   3   4   5   6   7

Ideal Placement: Value v belongs at Index (v - 1):
  Value 1 -> Index 0
  Value 2 -> Index 1
  Value 3 -> Index 2
  ...

After Cyclic Placement:
  Array:       [ 1,  2,  3,  4,  3,  2,  7,  8 ]
  Expected:      1   2   3   4   5   6   7   8
  Mismatches:                    ^   ^
                           Index 4   Index 5
                           holds 3   holds 2

Duplicate Values: [3, 2]
```

### The $O(1)$ Extra Space Constraint
A hash set easily detects duplicates in $O(N)$ time, but uses $O(N)$ extra memory.
Because the array values are strictly bounded by $1 \le nums[i] \le n$:
**The array itself can serve as its own hash table!**
Every integer $v$ has a designated "home bucket" at index $v - 1$.
By rearranging elements so each number resides in its home bucket, any element that collides with an identical number already occupying that home bucket is displaced to an unnatural index, exposing itself as a duplicate.

---

## 2. Conceptual Foundation & Invariants

### 1. The Cyclic Sort Invariant:
For index $i$ from $0$ to $n - 1$:
While $nums[i] \ne nums[nums[i] - 1]$:
- Value $nums[i]$ belongs at index $target = nums[i] - 1$.
- Swap $nums[i]$ with $nums[target]$.
- Each swap puts at least one number into its permanent home bucket ($nums[target] == target + 1$).
- If $nums[i] == nums[target]$, the home bucket is already occupied by a copy of this number; the swap terminates.

### 2. Post-Scan Identification:
After the loop finishes:
- For every unique number present in the array, its home index $k - 1$ contains $k$.
- Any remaining position $i$ that does not contain $i + 1$ holds an orphaned second copy of some number.
- Thus, $v = nums[i]$ for all $i$ where $nums[i] \ne i + 1$ is a duplicate.

> **Amortization Invariant.** Although a `while` loop is nested inside a `for` loop, each swap permanently places a number into its final position. Since there are $n$ positions, at most $n$ successful swaps occur across the entire algorithm, bounding total operations to $O(N)$.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [4, 3, 2, 7, 8, 2, 3, 1]$:

---

### Step 1: Process Index $i = 0$
- $nums[0] = 4$. Target index: $4 - 1 = 3$.
- $nums[3] = 7 \ne 4$. Swap $nums[0] \leftrightarrow nums[3]$:
  $$
  nums = [7, 3, 2, \mathbf{4}, 8, 2, 3, 1] \quad (\text{4 is now in its home bucket})
  $$
- $nums[0] = 7$. Target index: $7 - 1 = 6$.
- $nums[6] = 3 \ne 7$. Swap $nums[0] \leftrightarrow nums[6]$:
  $$
  nums = [3, 3, 2, 4, 8, 2, \mathbf{7}, 1] \quad (\text{7 is in its home bucket})
  $$
- $nums[0] = 3$. Target index: $3 - 1 = 2$.
- $nums[2] = 2 \ne 3$. Swap $nums[0] \leftrightarrow nums[2]$:
  $$
  nums = [2, 3, \mathbf{3}, 4, 8, 2, 7, 1] \quad (\text{3 is in its home bucket})
  $$
- $nums[0] = 2$. Target index: $2 - 1 = 1$.
- $nums[1] = 3 \ne 2$. Swap $nums[0] \leftrightarrow nums[1]$:
  $$
  nums = [3, \mathbf{2}, 3, 4, 8, 2, 7, 1] \quad (\text{2 is in its home bucket})
  $$
- $nums[0] = 3$. Target index is $2$.
- $nums[2] = 3$. $nums[0] == nums[2]$! **Collision detected.**
- Swapping at index 0 ceases.

---

### Step 2: Indices $i = 1, 2, 3$
- $i = 1: nums[1] = 2 == 1 + 1$ (Home).
- $i = 2: nums[2] = 3 == 2 + 1$ (Home).
- $i = 3: nums[3] = 4 == 3 + 1$ (Home).

---

### Step 3: Process Index $i = 4$
- $nums[4] = 8$. Target index: $8 - 1 = 7$.
- $nums[7] = 1 \ne 8$. Swap $nums[4] \leftrightarrow nums[7]$:
  $$
  nums = [3, 2, 3, 4, 1, 2, 7, \mathbf{8}] \quad (\text{8 is in its home bucket})
  $$
- $nums[4] = 1$. Target index: $1 - 1 = 0$.
- $nums[0] = 3 \ne 1$. Swap $nums[4] \leftrightarrow nums[0]$:
  $$
  nums = [\mathbf{1}, 2, 3, 4, \mathbf{3}, 2, 7, 8] \quad (\text{1 is in its home bucket})
  $$
- $nums[4] = 3$. Target index $2$ has $nums[2] = 3$. Collision. Stop.

---

### Step 4: Indices $i = 5, 6, 7$
- $i = 5: nums[5] = 2$. Target index $1$ already has $2$. Stop.
- $i = 6: nums[6] = 7 == 6 + 1$ (Home).
- $i = 7: nums[7] = 8 == 7 + 1$ (Home).

---

### Step 5: Filter Mismatches
Compare each $nums[i]$ with $i + 1$:
- $i = 0: nums[0] = 1 == 1$
- $i = 1: nums[1] = 2 == 2$
- $i = 2: nums[2] = 3 == 3$
- $i = 3: nums[3] = 4 == 4$
- $i = 4: nums[4] = \mathbf{3} \ne 5 \implies \mathbf{3}$
- $i = 5: nums[5] = \mathbf{2} \ne 6 \implies \mathbf{2}$
- $i = 6: nums[6] = 7 == 7$
- $i = 7: nums[7] = 8 == 8$
Duplicates collected: **`[3, 2]`**.

---

## 4. Complete Execution Trace

| Pass | Scanned Index $i$ | Value $nums[i]$ | Target Index $v - 1$ | Target Value $nums[v - 1]$ | Action Taken | Array State Snapshot |
|:---:|:---:|:---:|:---:|:---:|:---|:---|
| **1** | $0$ | $4$ | $3$ | $7$ | Swap $(0, 3)$ | `[7, 3, 2, 4, 8, 2, 3, 1]` |
| **1** | $0$ | $7$ | $6$ | $3$ | Swap $(0, 6)$ | `[3, 3, 2, 4, 8, 2, 7, 1]` |
| **1** | $0$ | $3$ | $2$ | $2$ | Swap $(0, 2)$ | `[2, 3, 3, 4, 8, 2, 7, 1]` |
| **1** | $0$ | $2$ | $1$ | $3$ | Swap $(0, 1)$ | `[3, 2, 3, 4, 8, 2, 7, 1]` |
| **1** | $0$ | $3$ | $2$ | $3$ | Equal: Stop | `[3, 2, 3, 4, 8, 2, 7, 1]` |
| **2** | $4$ | $8$ | $7$ | $1$ | Swap $(4, 7)$ | `[3, 2, 3, 4, 1, 2, 7, 8]` |
| **2** | $4$ | $1$ | $0$ | $3$ | Swap $(4, 0)$ | `[1, 2, 3, 4, 3, 2, 7, 8]` |
| **Scan**| All $i$ | — | — | — | Filter $nums[i] \ne i + 1$ | Indices $4, 5 \implies \mathbf{[3, 2]}$ |

---

## 5. Boundary Cases & Failure Modes

- **No Duplicates ($[1, 2, 3, 4]$):** All values match their home indices. Returns `[]`.
- **All Pairs Duplicated ($[2, 2, 1, 1]$):** Sort yields `[1, 2, 1, 2]`. Indices 2 and 3 produce `[1, 2]`.
- **Two Elements ($[2, 2]$):** Index 0 holds 2, target index 1 holds 2. Collision $\implies$ returns `[2]`.
- **Already Sorted Array ($[1, 2, 3]$):** While loop makes 0 swaps. Returns `[]`.

---

## 6. Traps & Common Anti-Patterns

- **Infinite Loop on Swapping Identical Values:** Writing `while nums[i] != i + 1: swap(...)` instead of `while nums[i] != nums[nums[i] - 1]: swap(...)` causes an infinite loop when a duplicate tries to swap with another copy of itself. Testing $nums[i] \ne nums[target]$ cleanly halts duplicate swaps.
- **Modifying the Array During Iteration with Indices:** Swapping $nums[i]$ changes the value being inspected; in Python, assigning `nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]` must evaluate the left target index before mutating `nums[i]`.
- **Allocating Output Sets:** Storing intermediate duplicates in a hash set violates $O(1)$ extra space requirements. Collecting final mismatches directly into the return list preserves space limits.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Each swap places at least one number into its correct position ($nums[x - 1] = x$).
  - A number placed in its correct position is never swapped again.
  - Therefore, at most $N$ swaps occur across the entire loop.
  - The final scan takes $O(N)$ time.
  - Total Time: $\mathcal{O}(N)$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ beyond the return list, since all reordering is performed in-place within the input array.
