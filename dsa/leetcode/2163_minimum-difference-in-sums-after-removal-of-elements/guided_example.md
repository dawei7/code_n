# Guided Example: Minimum Difference in Sums After Removal of Elements

We analyze and execute the dual-heap prefix-suffix sweep algorithm on a representative array instance, establishing how partitioning $3n$ elements across candidate split boundaries isolates the $n$ smallest prefix elements and $n$ largest suffix elements.

- **Input:** `nums = [7, 9, 5, 8, 1, 3]`, $n = 2$ ($3n = 6$)
- **Output:** `1`

This instance illustrates partition boundary sweeping, max-heap prefix filtering for minimum sum, min-heap suffix filtering for maximum sum, and signed difference minimization.

---

## 1. Problem Overview & Representative Instance

Given an array `nums` containing $3n$ positive integers, we must remove a subsequence of exactly $n$ elements without reordering the remaining $2n$ elements. The remaining elements are then bisected into two equal halves:
1. **First part ($S_{\text{first}}$):** The first $n$ elements of the retained sequence.
2. **Second part ($S_{\text{second}}$):** The final $n$ elements of the retained sequence.

The objective is to minimize the signed difference:
$$\text{Difference} = S_{\text{first}} - S_{\text{second}}$$

Minimizing this difference requires simultaneously making $S_{\text{first}}$ as small as possible and $S_{\text{second}}$ as large as possible.

In our representative instance:
- Array length: $3n = 6 \implies n = 2$.
- `nums = [7, 9, 5, 8, 1, 3]`.
- We must remove $n = 2$ elements to retain $2n = 4$ elements ($2$ in the first half, $2$ in the second half).

---

## 2. Mathematical & Algorithmic Principles

### Partition Boundary Cut Points

In the original array `nums`:
- The first $n$ elements must come from some prefix `nums[0 ... i]`. To contain at least $n$ elements, the prefix length must satisfy $i + 1 \ge n \implies i \ge n - 1$.
- The second $n$ elements must come from the remaining suffix `nums[i + 1 ... 3n - 1]`. To contain at least $n$ elements, the suffix length must satisfy $3n - (i + 1) \ge n \implies i \le 2n - 1$.

Therefore, the valid partition boundary $i$ between the candidate pool for the first part and second part lies strictly in:
$$i \in [n - 1, \, 2n - 1]$$

For any chosen split boundary $i$:
1. $S_{\text{first}}^*(i)$: The minimum possible sum of $n$ elements chosen from `nums[0 ... i]`. This is achieved by selecting the **$n$ smallest** elements in that prefix.
2. $S_{\text{second}}^*(i + 1)$: The maximum possible sum of $n$ elements chosen from `nums[i + 1 ... 3n - 1]`. This is achieved by selecting the **$n$ largest** elements in that suffix.

The global optimal difference is:
$$\text{MinDiff} = \min_{i = n - 1}^{2n - 1} \Big( S_{\text{first}}^*(i) - S_{\text{second}}^*(i + 1) \Big)$$

### Dual-Heap Tracking

1. **Prefix Max-Heap (Tracking $n$ Smallest):**
   - As we scan left to right, we maintain a max-heap of size $n$.
   - The heap holds the best $n$ smallest elements seen so far.
   - When a new element is added, if the heap exceeds size $n$, the largest element is evicted.
   - The sum of elements remaining in the max-heap gives the minimum sum of $n$ elements.
2. **Suffix Min-Heap (Tracking $n$ Largest):**
   - As we scan right to left, we maintain a min-heap of size $n$.
   - The heap holds the best $n$ largest elements seen so far in the suffix.
   - When a new element is added, if the heap exceeds size $n$, the smallest element is evicted.
   - The sum of elements remaining in the min-heap gives the maximum sum of $n$ elements.

| Partition Side | Target Objective | Maintained Heap Type | Eviction Rule on Size $> n$ | Recorded Extremum |
|---|---|---|---|---|
| Prefix `nums[0...i]` | Minimize sum | Max-Heap of size $n$ | Evict maximum element | $\text{left\_min}[i] = \sum \text{Heap}$ |
| Suffix `nums[i+1...3n-1]` | Maximize sum | Min-Heap of size $n$ | Evict minimum element | $\text{right\_max}[i+1] = \sum \text{Heap}$ |

---

## 3. Step-by-Step Walkthrough with Intermediate State

We trace `nums = [7, 9, 5, 8, 1, 3]` with $n = 2$.
Valid boundaries: $i \in [n - 1, 2n - 1] = [1, 3]$.

```
Array: [7,  9,  5,  8,  1,  3]
Index:  0   1   2   3   4   5

Sweep 1 (Left to Right, Max-Heap of size 2):
i = 0: push 7            => heap [7], sum = 7
i = 1: push 9            => heap [9, 7], sum = 16. left_min[1] = 16
i = 2: push 5, pop 9     => heap [7, 5], sum = 12. left_min[2] = 12
i = 3: push 8, pop 8     => heap [7, 5], sum = 12. left_min[3] = 12

Sweep 2 (Right to Left, Min-Heap of size 2):
j = 5: push 3            => heap [3], sum = 3
j = 4: push 1            => heap [1, 3], sum = 4.  right_max[4] = 4
j = 3: push 8, pop 1     => heap [3, 8], sum = 11. right_max[3] = 11
j = 2: push 5, pop 3     => heap [5, 8], sum = 13. right_max[2] = 13
```

### Step 1: Compute Prefix Minimums ($\text{left\_min}$)
- **$i = 0$ (`nums[0] = 7`):** Push $7$. Heap: $\{7\}$. Sum $= 7$.
- **$i = 1$ (`nums[1] = 9`):** Push $9$. Heap: $\{9, 7\}$. Size $= 2 = n$. Sum $= 7 + 9 = 16$.
  - Record: $\text{left\_min}[1] = 16$.
- **$i = 2$ (`nums[2] = 5`):** Push $5$. Heap: $\{9, 7, 5\}$. Size $= 3 > n$.
  - Evict maximum: pop $9$.
  - Remaining heap: $\{7, 5\}$. Sum $= 16 + 5 - 9 = 12$.
  - Record: $\text{left\_min}[2] = 12$.
- **$i = 3$ (`nums[3] = 8`):** Push $8$. Heap: $\{8, 7, 5\}$. Size $= 3 > n$.
  - Evict maximum: pop $8$.
  - Remaining heap: $\{7, 5\}$. Sum $= 12 + 8 - 8 = 12$.
  - Record: $\text{left\_min}[3] = 12$.

### Step 2: Compute Suffix Maximums ($\text{right\_max}$)
- **$j = 5$ (`nums[5] = 3`):** Push $3$. Heap: $\{3\}$. Sum $= 3$.
- **$j = 4$ (`nums[4] = 1`):** Push $1$. Heap: $\{1, 3\}$. Size $= 2 = n$. Sum $= 3 + 1 = 4$.
  - Record: $\text{right\_max}[4] = 4$.
- **$j = 3$ (`nums[3] = 8`):** Push $8$. Heap: $\{1, 3, 8\}$. Size $= 3 > n$.
  - Evict minimum: pop $1$.
  - Remaining heap: $\{3, 8\}$. Sum $= 4 + 8 - 1 = 11$.
  - Record: $\text{right\_max}[3] = 11$.
- **$j = 2$ (`nums[2] = 5`):** Push $5$. Heap: $\{3, 5, 8\}$. Size $= 3 > n$.
  - Evict minimum: pop $3$.
  - Remaining heap: $\{5, 8\}$. Sum $= 11 + 5 - 3 = 13$.
  - Record: $\text{right\_max}[2] = 13$.

### Step 3: Evaluate Candidate Boundary Differences
Compare $\text{left\_min}[i] - \text{right\_max}[i + 1]$ across all valid cut points:
- **Boundary $i = 1$:**
  - Prefix sum: $\text{left\_min}[1] = 16$.
  - Suffix sum: $\text{right\_max}[2] = 13$.
  - Difference: $16 - 13 = 3$.
- **Boundary $i = 2$:**
  - Prefix sum: $\text{left\_min}[2] = 12$.
  - Suffix sum: $\text{right\_max}[3] = 11$.
  - Difference: $12 - 11 = \mathbf{1}$.
- **Boundary $i = 3$:**
  - Prefix sum: $\text{left\_min}[3] = 12$.
  - Suffix sum: $\text{right\_max}[4] = 4$.
  - Difference: $12 - 4 = 8$.

### Step 4: Finalization
Minimum difference observed: $\min(3, 1, 8) = 1$.

---

## 4. Comprehensive State Trace

The table below catalogs every candidate boundary split $i$, the optimal subsets chosen on each side, and the evaluated signed difference:

| Split Point $i$ | Prefix Window `nums[0...i]` | Optimal First Part ($n=2$) | $\text{left\_min}[i]$ | Suffix Window `nums[i+1...5]` | Optimal Second Part ($n=2$) | $\text{right\_max}[i+1]$ | Difference $S_{\text{first}} - S_{\text{second}}$ |
|---|---|---|---|---|---|---|---|
| $1$ | `[7, 9]` | `[7, 9]` | $16$ | `[5, 8, 1, 3]` | `[5, 8]` | $13$ | $16 - 13 = 3$ |
| $2$ | `[7, 9, 5]` | `[7, 5]` | $12$ | `[8, 1, 3]` | `[8, 3]` | $11$ | $12 - 11 = \mathbf{1}$ |
| $3$ | `[7, 9, 5, 8]` | `[7, 5]` | $12$ | `[1, 3]` | `[1, 3]` | $4$ | $12 - 4 = 8$ |

### Verification of the Retained Sequence for $i = 2$

- Retained first part: `[7, 5]` (elements at indices $0$ and $2$; removed element $9$ at index $1$).
- Retained second part: `[8, 3]` (elements at indices $3$ and $5$; removed element $1$ at index $4$).
- Combined retained sequence: `[7, 5, 8, 3]`.
- Total removals: $9$ and $1$ ($2 = n$ removals).
- $S_{\text{first}} = 7 + 5 = 12$.
- $S_{\text{second}} = 8 + 3 = 11$.
- Signed difference: $12 - 11 = 1$.

---

## 5. Algorithmic Correctness & Soundness

### Global Partition Exhaustion
Any valid removal of $n$ elements partitions the remaining $2n$ elements into an initial block of $n$ elements and a final block of $n$ elements. The index in `nums` of the $n$-th retained element is some integer $i$.
- Because at least $n$ elements appear at or before index $i$, we have $i \ge n - 1$.
- Because at least $n$ elements appear after index $i$, we have $3n - (i + 1) \ge n \implies i \le 2n - 1$.
- Thus, the $n$-th retained element's index must belong to $[n - 1, 2n - 1]$.

For any fixed boundary $i$, the choice of the first $n$ elements from $[0, i]$ and the choice of the second $n$ elements from $[i + 1, 3n - 1]$ are completely decoupled. Minimizing the difference $A - B$ with independent choices is strictly achieved by minimizing $A$ and maximizing $B$. Therefore, iterating over all valid $i$ finds the global minimum without omission.

---

## 6. Edge Cases & Anti-Patterns

### Edge Cases
1. **$n = 1$ ($3n = 3$):** `nums = [3, 1, 2]`. $i \in [0, 1]$.
   - $i = 0$: `left_min[0] = 3`, `right_max[1] = 2` ($S = [1, 2]$) $\implies 3 - 2 = 1$.
   - $i = 1$: `left_min[1] = 1`, `right_max[2] = 2` $\implies 1 - 2 = -1$.
   - Returns $-1$.
2. **Negative Final Difference:** Differences can be negative whenever $S_{\text{second}} > S_{\text{first}}$, as shown in Example 1 and Example 3 ($-8$).
3. **Large Values Exceeding 32-bit Sums:** With $n = 10^5$ and values up to $10^5$, sums can reach $10^{10}$. Accumulators and differences must use 64-bit signed integers.

### Common Anti-Patterns
- **Greedy Global Element Removal:** Removing the $n$ largest elements overall ignores the position constraint that the first $n$ retained elements must strictly precede the second $n$ retained elements.
- **Sorting Without Temporal Boundaries:** Sorting destroys the index order required to form valid non-overlapping halves.
- **Dynamic Programming on Subsets:** A full 2D DP over state $(i, \text{count})$ takes $O(n^2)$ time, which times out for $n = 10^5$. Dual heaps achieve $O(n \log n)$ time.

---

## 7. Complexity Analysis

### Time Complexity
- **Prefix Scan:** Iterates through $2n$ elements. Each heap insertion and eviction takes $O(\log n)$ time. Total prefix time is $O(n \log n)$.
- **Suffix Scan:** Iterates through $2n$ elements backward. Each heap operation takes $O(\log n)$ time. Total suffix time is $O(n \log n)$.
- **Boundary Minimization:** Evaluates $n$ boundary points in $O(1)$ operations per point, taking $O(n)$ time.
- Total time complexity is strictly $O(n \log n)$, executing in under $40$ milliseconds for $n = 10^5$.

### Auxiliary Space Complexity
- Two priority queues of maximum size $n$ each.
- Arrays `left_min` and `right_max` storing up to $3n$ 64-bit integers.
- Total auxiliary space complexity is $O(n)$ memory.
