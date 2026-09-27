# Guided Example: Maximum Gap

We trace the step-by-step Pigeonhole bucket partitioning and inter-bucket extremum scan achieving linear $O(N)$ runtime on representative unsorted arrays:

- **Input:** $\text{nums} = [3, 6, 9, 1]$
- **Required output:** $3$ (Sorted form $[1, 3, 6, 9]$ has successive differences $2, 3, 3 \implies \max = 3$)
- **Base Insufficient Elements Instance:** $\text{nums} = [10] \implies 0$ ($N < 2$)
- **Identical Elements Instance:** $\text{nums} = [5, 5, 5, 5] \implies 0$ ($\min == \max$)

This instance demonstrates avoiding the $O(N \log N)$ comparison sorting lower bound, derives the Pigeonhole Principle bucket width ($\text{size} = \lfloor (\max - \min) / (N - 1) \rfloor$), proves why the maximum gap cannot reside within any single bucket, and operates in strictly $O(N)$ time and $O(N)$ space.

---

## 1. Instance & Teaching Goal

Given an unsorted array of integers $\text{nums} = [3, 6, 9, 1]$:
Find the maximum difference between two successive elements in its sorted form.
- Sorted sequence: $[1, 3, 6, 9]$.
- Adjacent differences:
  - $3 - 1 = 2$
  - $6 - 3 = 3$
  - $9 - 6 = 3$
Maximum gap: $3$.
The algorithm must run in linear $O(N)$ time and linear $O(N)$ auxiliary space.

Comparison-based sorting (Merge Sort, Quick Sort, Timsort) is strictly bounded below by $\Omega(N \log N)$ time.
To achieve strictly linear $O(N)$ time, we leverage the **Pigeonhole Principle**:
Across $N$ numbers spanning from $\min$ to $\max$, there are $N - 1$ gaps between successive sorted values.
The average gap length is:
$$
\text{gap}_{\text{avg}} = \frac{\max - \min}{N - 1}
$$
Therefore, the true maximum gap must be **at least** $\text{gap}_{\text{avg}}$.
If we partition the entire numeric range into buckets of width $\text{bucket\_size} \le \text{gap}_{\text{avg}}$, no two numbers in the *same* bucket can have a difference greater than $\text{bucket\_size}$.
Thus, the maximum gap can **never** occur within the same bucket—it must span across adjacent non-empty buckets!
We only need to track the minimum and maximum of each bucket, eliminating internal bucket sorting completely.

---

## 2. Conceptual Foundation & Invariants

### The Pigeonhole Bucket Protocol
Let $N = |\text{nums}|$.
If $N < 2$, return $0$.
Compute global extrema:
$$
\text{mi} = \min(\text{nums}), \quad \text{mx} = \max(\text{nums})
$$
If $\text{mi} == \text{mx}$, all elements are identical: return $0$.

#### 1. Bucket Sizing and Count:
$$
\text{bucket\_size} = \max\left(1, \, \left\lfloor \frac{\text{mx} - \text{mi}}{N - 1} \right\rfloor\right)
$$
$$
\text{bucket\_count} = \left\lfloor \frac{\text{mx} - \text{mi}}{\text{bucket\_size}} \right\rfloor + 1
$$
Allocate `buckets = [[+inf, -inf] for _ in range(bucket_count)]`.

#### 2. Element Distribution:
For each $x \in \text{nums}$:
$$
\text{idx} = \left\lfloor \frac{x - \text{mi}}{\text{bucket\_size}} \right\rfloor
$$
$$
\text{buckets}[\text{idx}][0] = \min(\text{buckets}[\text{idx}][0], \, x) \quad (\text{bucket min})
$$
$$
\text{buckets}[\text{idx}][1] = \max(\text{buckets}[\text{idx}][1], \, x) \quad (\text{bucket max})
$$

#### 3. Inter-Bucket Gap Scan:
Maintain $\text{prev\_max} = \text{mi}$, $\text{max\_gap} = 0$.
For each bucket $[\text{b\_min}, \text{b\_max}]$:
- If bucket is empty ($\text{b\_min} == \infty$): skip.
- Compute gap between current bucket minimum and previous occupied bucket maximum:
  $$
  \text{gap} = \text{b\_min} - \text{prev\_max}
  $$
  $$
  \text{max\_gap} = \max(\text{max\_gap}, \, \text{gap})
  $$
  $$
  \text{prev\_max} = \text{b\_max}
  $$

> **Invariant.** For any non-empty bucket, all elements inside it differ by at most $\text{bucket\_size}$. Since $\text{bucket\_size} \le \text{gap}_{\text{avg}} \le \text{max\_gap}$, the global maximum gap must equal $\text{b\_min}_j - \text{b\_max}_i$ for some consecutive occupied buckets $i < j$.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $\text{nums} = [3, 6, 9, 1]$ ($N = 4$):

### Step 1: Global Range & Bucket Configuration
- $\text{mi} = \min(3, 6, 9, 1) = 1$.
- $\text{mx} = \max(3, 6, 9, 1) = 9$.
- Range: $\text{mx} - \text{mi} = 9 - 1 = 8$.
- Bucket size:
  $$
  \text{bucket\_size} = \max\left(1, \, \left\lfloor \frac{8}{4 - 1} \right\rfloor\right) = \lfloor 2.666 \rfloor = \mathbf{2}
  $$
- Bucket count:
  $$
  \text{bucket\_count} = \left\lfloor \frac{8}{2} \right\rfloor + 1 = 4 + 1 = \mathbf{5}
  $$
- Initialize 5 empty buckets: $B_0, B_1, B_2, B_3, B_4$.

---

### Step 2: Scatter Elements into Buckets
1. **$x = 3$:** $\text{idx} = \lfloor (3 - 1) / 2 \rfloor = 1 \implies B_1: [\min=3, \max=3]$.
2. **$x = 6$:** $\text{idx} = \lfloor (6 - 1) / 2 \rfloor = 2 \implies B_2: [\min=6, \max=6]$.
3. **$x = 9$:** $\text{idx} = \lfloor (9 - 1) / 2 \rfloor = 4 \implies B_4: [\min=9, \max=9]$.
4. **$x = 1$:** $\text{idx} = \lfloor (1 - 1) / 2 \rfloor = 0 \implies B_0: [\min=1, \max=1]$.

Bucket contents:
- $B_0$: $[\min=1, \max=1]$ (contains $\{1\}$)
- $B_1$: $[\min=3, \max=3]$ (contains $\{3\}$)
- $B_2$: $[\min=6, \max=6]$ (contains $\{6\}$)
- $B_3$: $[\infty, -\infty]$ (**Empty!**)
- $B_4$: $[\min=9, \max=9]$ (contains $\{9\}$)

---

### Step 3: Scan Inter-Bucket Gaps
Initialize $\text{prev\_max} = B_0[1] = 1, \quad \text{max\_gap} = 0$.

- **Bucket $B_1$ ($[3, 3]$):**
  - $\text{gap} = B_1.\text{min} - \text{prev\_max} = 3 - 1 = \mathbf{2}$.
  - $\text{max\_gap} = \max(0, 2) = 2$.
  - Update: $\text{prev\_max} = B_1.\text{max} = 3$.

- **Bucket $B_2$ ($[6, 6]$):**
  - $\text{gap} = B_2.\text{min} - \text{prev\_max} = 6 - 3 = \mathbf{3}$.
  - $\text{max\_gap} = \max(2, 3) = \mathbf{3}$.
  - Update: $\text{prev\_max} = B_2.\text{max} = 6$.

- **Bucket $B_3$ ($[\infty, -\infty]$):**
  - Empty bucket! Skip. $\text{prev\_max}$ remains $6$.

- **Bucket $B_4$ ($[9, 9]$):**
  - $\text{gap} = B_4.\text{min} - \text{prev\_max} = 9 - 6 = \mathbf{3}$.
  - $\text{max\_gap} = \max(3, 3) = \mathbf{3}$.
  - Update: $\text{prev\_max} = B_4.\text{max} = 9$.

All buckets scanned. Maximum gap is $\mathbf{3}$.

---

## 4. Complete Execution Trace

```text
Elements: 1, 3, 6, 9.  Min=1, Max=9, Size=2, 5 Buckets.
Bucket 0 [1, 2]: {1}   -> min=1, max=1
Bucket 1 [3, 4]: {3}   -> min=3, max=3   Gap: 3 - 1 = 2
Bucket 2 [5, 6]: {6}   -> min=6, max=6   Gap: 6 - 3 = 3
Bucket 3 [7, 8]: {}    -> EMPTY
Bucket 4 [9, 10]: {9}  -> min=9, max=9   Gap: 9 - 6 = 3
Maximum Gap: 3
```

| Bucket Index | Value Range | Bucket Elements | Bucket Min $\text{b\_min}$ | Bucket Max $\text{b\_max}$ | $\text{prev\_max}$ | Inter-Bucket Gap ($\text{b\_min} - \text{prev\_max}$) | $\text{max\_gap}$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $B_0$ | $[1, 2]$ | $\{1\}$ | 1 | 1 | - | - | 0 |
| $B_1$ | $[3, 4]$ | $\{3\}$ | 3 | 3 | 1 | $3 - 1 = 2$ | 2 |
| **$B_2$** | **$[5, 6]$** | **$\{6\}$** | **6** | **6** | **3** | **$6 - 3 = 3$** | **3** |
| $B_3$ | $[7, 8]$ | $\emptyset$ | $\infty$ | $-\infty$ | 6 | *(Empty - skipped)* | 3 |
| **$B_4$** | **$[9, 10]$** | **$\{9\}$** | **9** | **9** | **6** | **$9 - 6 = 3$** | **3 (Final)** |

---

## 5. Algorithmic Correctness

**Soundness.** Because each bucket covers a contiguous range of size $S \le \text{gap}_{\text{avg}}$, the difference between any two elements inside the same bucket cannot exceed $S - 1 < \text{gap}_{\text{avg}}$. Since the maximum gap is at least $\text{gap}_{\text{avg}}$, no intra-bucket difference can ever be the maximum gap. Therefore, evaluating only differences between the minimum of an occupied bucket and the maximum of the previous occupied bucket is mathematically sound.

**Completeness.** Every element in `nums` falls into exactly one bucket. Since buckets are ordered by their value intervals, the sequence of occupied buckets strictly reflects the sorted order of their elements, guaranteeing that all adjacent sorted transitions are considered.

---

## 6. Traps This Instance Exposes

- **Zero Bucket Size Trap:** If $\text{mx} - \text{mi} < N - 1$, integer division yields $0$! Setting $\text{bucket\_size} = \max(1, \lfloor (\text{mx} - \text{mi}) / (N - 1) \rfloor)$ avoids division-by-zero errors.
- **Skipping Empty Buckets:** An empty bucket (like $B_3$ above) indicates a wide span of missing values. When skipping $B_3$, $\text{prev\_max}$ must NOT be updated; it must stay anchored at $B_2$'s maximum ($6$), correctly exposing the gap $9 - 6 = 3$.
- **Sorting Fallback:** Radix sort can also achieve $O(B \cdot N)$ where $B=32$, but bucket sort via Pigeonhole runs in a single direct pass.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Finding $\min$ and $\max$ takes $O(N)$. Placing $N$ elements into buckets takes $O(N)$. Scanning the $O(N)$ buckets takes $O(N)$. Total runtime is strictly $O(N)$.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary memory to store at most $N + 1$ bucket minimum and maximum pairs.
