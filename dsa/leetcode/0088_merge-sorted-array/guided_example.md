# Guided Example: Merge Sorted Array

We trace the step-by-step backward three-pointer in-place array merge on a representative instance:

- **Input:** $\text{nums1} = [1, 2, 3, 0, 0, 0], m = 3$, $\text{nums2} = [2, 5, 6], n = 3$
- **Required output:** $[1, 2, 2, 3, 5, 6]$

This instance demonstrates merging two sorted arrays from right to left, exploiting trailing buffer capacity to prevent overwriting unread values, comparing tails ($p_1$ vs $p_2$), and terminating early when $\text{nums2}$ is exhausted.

---

## 1. Instance & Teaching Goal

You are given two integer arrays $\text{nums1}$ and $\text{nums2}$, sorted in non-decreasing order, and two integers $m = 3$ and $n = 3$:
- $\text{nums1}$ has length $m + n = 6$, where the first $m = 3$ elements denote the sorted content, and the last $n = 3$ elements are set to $0$ as placeholder capacity.
- $\text{nums2}$ has length $n = 3$.

Merge $\text{nums2}$ into $\text{nums1}$ as one sorted array **in place**.

If we merge from left to right starting at index 0, placing a smaller element from $\text{nums2}$ would overwrite an unread element in $\text{nums1}$, requiring an auxiliary array of size $m$.
Because the empty slots are located at the back of $\text{nums1}$ (indices $m \dots m+n-1$), merging backwards from the largest elements guarantees that the write pointer $p$ never overtakes the read pointer $p_1$. This achieves strictly $O(1)$ auxiliary space.

---

## 2. Conceptual Foundation & Invariants

### Backward Three-Pointer Protocol
We initialize three pointers:
- $p_1 = m - 1$ (Points to the largest unplaced element in $\text{nums1}$).
- $p_2 = n - 1$ (Points to the largest unplaced element in $\text{nums2}$).
- $p = m + n - 1$ (Points to the next unfilled write slot at the tail of $\text{nums1}$).

### Comparison Loop (While $p_2 \ge 0$)
At each step:
- **If $p_1 \ge 0$ and $\text{nums1}[p_1] > \text{nums2}[p_2]$:**
  $\text{nums1}[p_1]$ is the globally largest remaining value:
  $$
  \text{nums1}[p] \leftarrow \text{nums1}[p_1], \quad p_1 \leftarrow p_1 - 1
  $$
- **Else:**
  $\text{nums2}[p_2]$ is the larger (or equal) value, or $\text{nums1}$ has been exhausted ($p_1 < 0$):
  $$
  \text{nums1}[p] \leftarrow \text{nums2}[p_2], \quad p_2 \leftarrow p_2 - 1
  $$
- Decrement write slot: $p \leftarrow p - 1$.

*(Note: Once $p_2 < 0$, any remaining elements in $\text{nums1}$ are already in their correct sorted positions, so the algorithm halts immediately).*

> **Invariant.** Throughout the merge, $p \ge p_1$ always holds, so writing to $\text{nums1}[p]$ can never overwrite an unread element at $p_1$.

---

## 3. Step-by-Step Worked Execution

We trace $\text{nums1} = [1, 2, 3, 0, 0, 0]$ ($m = 3$) and $\text{nums2} = [2, 5, 6]$ ($n = 3$):

### Initialization
- $p_1 = 3 - 1 = 2$ ($\text{nums1}[2] = 3$).
- $p_2 = 3 - 1 = 2$ ($\text{nums2}[2] = 6$).
- $p = 6 - 1 = 5$ (Tail write position).

---

### Step 1: Fill Index $p = 5$
- Compare $\text{nums1}[2] = 3$ vs $\text{nums2}[2] = 6$.
- $6 > 3 \implies$ Pick from $\text{nums2}$.
- Write: $\text{nums1}[5] \leftarrow 6$.
- Decrement: $p_2 \to 1, p \to 4$.
- Array: $[1, 2, 3, 0, 0, \mathbf{6}]$.

---

### Step 2: Fill Index $p = 4$
- Compare $\text{nums1}[2] = 3$ vs $\text{nums2}[1] = 5$.
- $5 > 3 \implies$ Pick from $\text{nums2}$.
- Write: $\text{nums1}[4] \leftarrow 5$.
- Decrement: $p_2 \to 0, p \to 3$.
- Array: $[1, 2, 3, 0, \mathbf{5}, 6]$.

---

### Step 3: Fill Index $p = 3$
- Compare $\text{nums1}[2] = 3$ vs $\text{nums2}[0] = 2$.
- $3 > 2 \implies$ Pick from $\text{nums1}$.
- Write: $\text{nums1}[3] \leftarrow 3$.
- Decrement: $p_1 \to 1, p \to 2$.
- Array: $[1, 2, 3, \mathbf{3}, 5, 6]$.

---

### Step 4: Fill Index $p = 2$
- Compare $\text{nums1}[1] = 2$ vs $\text{nums2}[0] = 2$.
- $2 \ngtr 2 \implies$ Pick from $\text{nums2}$.
- Write: $\text{nums1}[2] \leftarrow 2$.
- Decrement: $p_2 \to -1, p \to 1$.
- Array: $[1, 2, \mathbf{2}, 3, 5, 6]$.

---

### Termination
- $p_2 = -1 < 0$. All elements of $\text{nums2}$ are placed.
- Remaining elements at $\text{nums1}[0 \dots 1]$ are $[1, 2]$, which are already in their final sorted spots.
- Final $\text{nums1}$: $[1, 2, 2, 3, 5, 6]$.

---

## 4. Complete Execution Trace

| Step | Write Index $p$ | $p_1$ Val ($\text{nums1}$) | $p_2$ Val ($\text{nums2}$) | Comparison Condition | Chosen Source | Value Written | Resulting $\text{nums1}$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | 5 | $\text{nums1}[2] = 3$ | $\text{nums2}[2] = 6$ | $6 > 3$ | $\text{nums2}$ | 6 | `[1, 2, 3, 0, 0, 6]` |
| 2 | 4 | $\text{nums1}[2] = 3$ | $\text{nums2}[1] = 5$ | $5 > 3$ | $\text{nums2}$ | 5 | `[1, 2, 3, 0, 5, 6]` |
| 3 | 3 | $\text{nums1}[2] = 3$ | $\text{nums2}[0] = 2$ | $3 > 2$ | $\text{nums1}$ | 3 | `[1, 2, 3, 3, 5, 6]` |
| 4 | 2 | $\text{nums1}[1] = 2$ | $\text{nums2}[0] = 2$ | $2 \ngtr 2$ | $\text{nums2}$ | 2 | `[1, 2, 2, 3, 5, 6]` |
| Exit | 1 | - | $p_2 = -1$ | Halts | - | - | **`[1, 2, 2, 3, 5, 6]`** |

---

## 5. Algorithmic Correctness

**Soundness.** Both arrays are sorted non-decreasingly. The maximum element among all unplaced numbers must be either $\text{nums1}[p_1]$ or $\text{nums2}[p_2]$. Placing the larger of the two into slot $p$ and decrementing that pointer ensures that elements are written to $\text{nums1}$ in strictly descending order from index $m + n - 1$ down to 0.

**Completeness.** The loop runs until $p_2 < 0$. If $\text{nums1}$ empties first ($p_1 < 0$), the remaining elements of $\text{nums2}$ are simply copied into the front of $\text{nums1}$. If $\text{nums2}$ empties first, the front of $\text{nums1}$ is already sorted and requires no copying.

---

## 6. Traps This Instance Exposes

- **Overwriting Unread Data:** Forward merging writes to index 0, corrupting $\text{nums1}[0]$ before it can be compared. Backward merging completely avoids memory collision because empty capacity is consumed first.
- **Empty Second Array ($n = 0$):** If $n = 0$, $p_2 = -1$ initially; the loop executes zero times and $\text{nums1}$ remains unchanged.
- **Empty First Array ($m = 0$):** If $m = 0$, $p_1 = -1$ initially; the loop copies all $n$ elements from $\text{nums2}$ directly into $\text{nums1}$.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(m + n)$. In each step, exactly one element is placed at position $p$, requiring at most $m + n$ iterations.
- **Auxiliary Space Complexity:** $O(1)$. Elements are written directly into the pre-allocated trailing space of `nums1`.
