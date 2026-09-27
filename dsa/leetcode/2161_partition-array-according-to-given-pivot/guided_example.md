# Guided Example: Partition Array According to Given Pivot

We analyze and execute the stable three-way partition algorithm on a representative problem instance, demonstrating how precomputed bucket offset pointers guarantee relative order preservation across trichotomy partitions in a single linear pass.

- **Input:** `nums = [9, 12, 5, 10, 14, 3, 10]`, `pivot = 10`
- **Output:** `[9, 5, 3, 10, 10, 12, 14]`

This instance illustrates trichotomy classification, stable sequence preservation, base-offset index assignment, and single-pass destination routing.

---

## 1. Problem Overview & Representative Instance

Given an integer array `nums` of length $n$ and an integer `pivot` present in `nums`, we must rearrange all elements into three consecutive contiguous segments:
1. **Left Segment ($< \text{pivot}$):** All elements strictly smaller than `pivot`.
2. **Middle Segment ($= \text{pivot}$):** All elements strictly equal to `pivot`.
3. **Right Segment ($> \text{pivot}$):** All elements strictly greater than `pivot`.

Crucially, the rearrangement must be **stable**:
- If $x < \text{pivot}$ and $y < \text{pivot}$ with $x$ appearing before $y$ in the original array, $x$ must appear before $y$ in the partitioned array.
- If $u > \text{pivot}$ and $v > \text{pivot}$ with $u$ appearing before $v$ in the original array, $u$ must appear before $v$ in the partitioned array.

In our representative instance:
- `nums = [9, 12, 5, 10, 14, 3, 10]` ($n = 7$).
- `pivot = 10`.
- Subsequence of elements $< 10$: $[9, 5, 3]$.
- Subsequence of elements $= 10$: $[10, 10]$.
- Subsequence of elements $> 10$: $[12, 14]$.

The combined stable output must be $[9, 5, 3, 10, 10, 12, 14]$.

---

## 2. Mathematical & Algorithmic Principles

### Trichotomy Partition Topology

Every integer $x$ in `nums` satisfies exactly one of three mutually exclusive relations with `pivot`:
$$x < \text{pivot} \quad \lor \quad x = \text{pivot} \quad \lor \quad x > \text{pivot}$$

Let:
- $C_{<} = \sum_{j=0}^{n-1} \mathbf{1}_{\{\text{nums}[j] < \text{pivot}\}}$ (count of smaller elements).
- $C_{=} = \sum_{j=0}^{n-1} \mathbf{1}_{\{\text{nums}[j] = \text{pivot}\}}$ (count of equal elements).
- $C_{>} = \sum_{j=0}^{n-1} \mathbf{1}_{\{\text{nums}[j] > \text{pivot}\}}$ (count of larger elements).

Because every element belongs to exactly one bucket:
$$C_{<} + C_{=} + C_{>} = n$$

The destination indices in the output array $A$ of size $n$ are partitioned into three static intervals:
1. **Less-than interval:** $[0, \, C_{<} - 1]$
2. **Equal-to interval:** $[C_{<}, \, C_{<} + C_{=} - 1]$
3. **Greater-than interval:** $[C_{<} + C_{=}, \, n - 1]$

### Stable Single-Pass Routing via Offset Pointers

We maintain three write pointers initialized to the base offsets of their respective intervals:
- $\text{ptr}_{<} = 0$
- $\text{ptr}_{=} = C_{<}$
- $\text{ptr}_{>} = C_{<} + C_{=}$

As we scan `nums` from index $0$ to $n - 1$:
- If $\text{nums}[i] < \text{pivot}$: write to $A[\text{ptr}_{<}]$, and advance $\text{ptr}_{<} \leftarrow \text{ptr}_{<} + 1$.
- If $\text{nums}[i] == \text{pivot}$: write to $A[\text{ptr}_{=}]$, and advance $\text{ptr}_{=} \leftarrow \text{ptr}_{=} + 1$.
- If $\text{nums}[i] > \text{pivot}$: write to $A[\text{ptr}_{>}]$, and advance $\text{ptr}_{>} \leftarrow \text{ptr}_{>} + 1$.

Because the original array is scanned sequentially from left to right and each pointer advances monotonically, every bucket retains its original chronological order, achieving 100% stability.

| Bucket | Condition | Initial Offset | Target Interval | Elements in Instance |
|---|---|---|---|---|
| Less Than | $x < 10$ | $0$ | $[0, 2]$ | $[9, 5, 3]$ (3 elements) |
| Equal To | $x = 10$ | $C_{<} = 3$ | $[3, 4]$ | $[10, 10]$ (2 elements) |
| Greater Than | $x > 10$ | $C_{<} + C_{=} = 5$ | $[5, 6]$ | $[12, 14]$ (2 elements) |

---

## 3. Step-by-Step Walkthrough with Intermediate State

We trace the stable routing on `nums = [9, 12, 5, 10, 14, 3, 10]`, `pivot = 10`.

```
Input: [9, 12, 5, 10, 14, 3, 10], pivot = 10
Counts: C_< = 3, C_= = 2, C_> = 2

Target Buffer: [ _,  _,  _,  _,  _,  _,  _ ]
Pointers: ptr_< = 0, ptr_= = 3, ptr_> = 5
```

### Step 1: Precompute Bucket Cardinalities
Scan `nums` to count bucket sizes:
- Elements $< 10$: $9, 5, 3 \implies C_{<} = 3$.
- Elements $= 10$: $10, 10 \implies C_{=} = 2$.
- Elements $> 10$: $12, 14 \implies C_{>} = 2$.
- Base write offsets:
  - $\text{ptr}_{<} = 0$
  - $\text{ptr}_{=} = 3$
  - $\text{ptr}_{>} = 3 + 2 = 5$

### Step 2: Route Elements Sequentially

- **Index 0 ($x = 9$):**
  - $9 < 10$. Write to $A[\text{ptr}_{<}] = A[0] = 9$.
  - Advance $\text{ptr}_{<} \leftarrow 1$.
  - Buffer: $[9, \_, \_, \_, \_, \_, \_]$.
- **Index 1 ($x = 12$):**
  - $12 > 10$. Write to $A[\text{ptr}_{>}] = A[5] = 12$.
  - Advance $\text{ptr}_{>} \leftarrow 6$.
  - Buffer: $[9, \_, \_, \_, \_, 12, \_]$.
- **Index 2 ($x = 5$):**
  - $5 < 10$. Write to $A[\text{ptr}_{<}] = A[1] = 5$.
  - Advance $\text{ptr}_{<} \leftarrow 2$.
  - Buffer: $[9, 5, \_, \_, \_, 12, \_]$.
- **Index 3 ($x = 10$):**
  - $10 == 10$. Write to $A[\text{ptr}_{=}] = A[3] = 10$.
  - Advance $\text{ptr}_{=} \leftarrow 4$.
  - Buffer: $[9, 5, \_, 10, \_, 12, \_]$.
- **Index 4 ($x = 14$):**
  - $14 > 10$. Write to $A[\text{ptr}_{>}] = A[6] = 14$.
  - Advance $\text{ptr}_{>} \leftarrow 7$.
  - Buffer: $[9, 5, \_, 10, \_, 12, 14]$.
- **Index 5 ($x = 3$):**
  - $3 < 10$. Write to $A[\text{ptr}_{<}] = A[2] = 3$.
  - Advance $\text{ptr}_{<} \leftarrow 3$.
  - Buffer: $[9, 5, 3, 10, \_, 12, 14]$.
- **Index 6 ($x = 10$):**
  - $10 == 10$. Write to $A[\text{ptr}_{=}] = A[4] = 10$.
  - Advance $\text{ptr}_{=} \leftarrow 5$.
  - Buffer: $[9, 5, 3, 10, 10, 12, 14]$.

### Step 3: Final State Verification
All pointers reach their segment upper bounds:
- $\text{ptr}_{<} = 3$
- $\text{ptr}_{=} = 5$
- $\text{ptr}_{>} = 7$

Output array is completely filled: $[9, 5, 3, 10, 10, 12, 14]$.

---

## 4. Comprehensive State Trace

The table below catalogs every step of the sequential placement:

| Scan Step $i$ | Element $\text{nums}[i]$ | Comparison vs Pivot ($10$) | Selected Pointer | Target Index Written | Pointer Update | Array State After Step |
|---|---|---|---|---|---|---|
| Initial | - | - | - | - | $\text{less}=0, \text{eq}=3, \text{gt}=5$ | `[_, _, _, _, _, _, _]` |
| $0$ | $9$ | $9 < 10$ | $\text{ptr}_{<} = 0$ | $0$ | $\text{ptr}_{<} \leftarrow 1$ | `[9, _, _, _, _, _, _]` |
| $1$ | $12$ | $12 > 10$ | $\text{ptr}_{>} = 5$ | $5$ | $\text{ptr}_{>} \leftarrow 6$ | `[9, _, _, _, _, 12, _]` |
| $2$ | $5$ | $5 < 10$ | $\text{ptr}_{<} = 1$ | $1$ | $\text{ptr}_{<} \leftarrow 2$ | `[9, 5, _, _, _, 12, _]` |
| $3$ | $10$ | $10 = 10$ | $\text{ptr}_{=} = 3$ | $3$ | $\text{ptr}_{=} \leftarrow 4$ | `[9, 5, _, 10, _, 12, _]` |
| $4$ | $14$ | $14 > 10$ | $\text{ptr}_{>} = 6$ | $6$ | $\text{ptr}_{>} \leftarrow 7$ | `[9, 5, _, 10, _, 12, 14]` |
| $5$ | $3$ | $3 < 10$ | $\text{ptr}_{<} = 2$ | $2$ | $\text{ptr}_{<} \leftarrow 3$ | `[9, 5, 3, 10, _, 12, 14]` |
| $6$ | $10$ | $10 = 10$ | $\text{ptr}_{=} = 4$ | $4$ | $\text{ptr}_{=} \leftarrow 5$ | `[9, 5, 3, 10, 10, 12, 14]` |

### Verification of Stability Criteria

- **Left Subsequence ($< 10$):** Original appearance was $9, 5, 3$. Output contains $9, 5, 3$. (Stable)
- **Middle Subsequence ($= 10$):** Output contains $10, 10$. (Stable)
- **Right Subsequence ($> 10$):** Original appearance was $12, 14$. Output contains $12, 14$. (Stable)

---

## 5. Algorithmic Correctness & Soundness

### Interval Non-Interference
The intervals $[0, C_{<} - 1]$, $[C_{<}, C_{<} + C_{=} - 1]$, and $[C_{<} + C_{=}, n - 1]$ are mutually disjoint and their union equals $[0, n - 1]$.
- No pointer ever writes outside its designated interval.
- Each element of `nums` increments exactly one pointer by $1$.
- At termination, $\text{ptr}_{<} = C_{<}$, $\text{ptr}_{=} = C_{<} + C_{=}$, and $\text{ptr}_{>} = n$.
- Every cell in $A$ is written to exactly once, with zero holes or overwrites.

### Stability Proof
Within any bucket $B \in \{<, =, >\}$, the $k$-th element encountered in `nums` belonging to bucket $B$ is placed at index $\text{base}(B) + k - 1$. Because the mapping $k \mapsto \text{base}(B) + k - 1$ is strictly monotonically increasing, relative order is preserved unconditionally.

---

## 6. Edge Cases & Anti-Patterns

### Edge Cases
1. **No Smaller Elements ($C_{<} = 0$):** For example, `nums = [10, 12, 14]`, `pivot = 10`. The less-than segment has length $0$; $\text{ptr}_{<} = 0, \text{ptr}_{=} = 0$. Equal elements start at index $0$.
2. **No Greater Elements ($C_{>} = 0$):** `nums = [5, 3, 10]`, `pivot = 10`. Greater-than segment has length $0$. Pointers fill the array up to index $n - 1$ without writing to greater-than.
3. **All Elements Equal to Pivot:** `nums = [10, 10, 10]`, `pivot = 10`. $C_{<} = 0, C_{=} = 3, C_{>} = 0$. Array is filled exclusively by $\text{ptr}_{=}$.
4. **Pivot at Extremes of Value Range:** Negative numbers and large numbers (e.g., $-10^6$ to $10^6$) are handled naturally by standard numerical inequalities.

### Common Anti-Patterns
- **Dutch National Flag (In-Place Two Pointers):** The classic Dutch National Flag algorithm uses in-place swapping (from both ends), which is **not stable** and reverses or scrambles the relative order of elements greater than the pivot.
- **Sorting Approaches:** Sorting `nums` alters the relative order among smaller and greater elements (sorting $9, 5, 3$ would yield $3, 5, 9$, violating stability).
- **Three Separate List Allocations:** Creating three intermediate arrays and concatenating them creates multiple memory reallocations. Precalculating counts allows direct placement into a single preallocated output array.

---

## 7. Complexity Analysis

### Time Complexity
- **Pass 1:** Counting $C_{<}$ and $C_{=}$ takes $n$ comparisons, running in $O(n)$ time.
- **Pass 2:** Routing each element into the preallocated buffer takes $n$ comparisons and $n$ assignments, running in $O(n)$ time.
- Total time complexity is strictly $O(n)$, executing in under $2$ milliseconds for $n = 10^5$.

### Auxiliary Space Complexity
- A single destination array of size $n$ stores the rearranged output.
- Three integer pointer variables maintain write offsets.
- Total auxiliary space complexity is $O(n)$ for the returned result array (and $O(1)$ additional working memory).
