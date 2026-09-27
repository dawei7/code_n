# Guided Example: Kth Largest Element in an Array

We trace the step-by-step target rank translation, Quickselect partition reduction, and min-heap bounding on representative unsorted arrays:

- **Input:** $\text{nums} = [3, 2, 1, 5, 6, 4], \quad k = 2$
- **Required output:** $5$ (Sorted descending: $[6, \mathbf{5}, 4, 3, 2, 1]$; the 2nd largest is $5$)
- **Duplicate Elements Instance:** $\text{nums} = [3, 2, 3, 1, 2, 4, 5, 5, 6], \quad k = 4 \implies 4$ (Duplicates occupy distinct rank positions)
- **Maximum Element Instance:** $k = 1 \implies \max(\text{nums}) = 6$
- **Minimum Element Instance:** $k = N \implies \min(\text{nums}) = 1$

This instance demonstrates selection without full sorting, proves the conversion of $k^{\text{th}}$ largest to ascending zero-based index $N - k$, contrasts randomized Quickselect ($O(N)$ expected time, $O(1)$ space) with a size-$k$ min-heap ($O(N \log k)$ time, $O(k)$ space), and details pivot partitioning invariants.

---

## 1. Instance & Teaching Goal

Given an unsorted array $\text{nums} = [3, 2, 1, 5, 6, 4]$ of length $N = 6$ and an integer $k = 2$:
Find the $2^{\text{nd}}$ largest value in sorted order without fully sorting the array.

### Conversion to Ascending Index
Sorting the entire array in ascending order yields:
$$
[1, 2, 3, 4, \mathbf{5}, 6]
$$
- Largest ($k = 1$): index $5$ (value $6$).
- $2^{\text{nd}}$ largest ($k = 2$): index $4$ (value $5$).
- $k^{\text{th}}$ largest corresponds to the zero-based index:
$$
\text{target} = N - k = 6 - 2 = \mathbf{4}
$$
Sorting the entire array takes $O(N \log N)$ time.
However, sorting all elements is wasteful because we only care about the single value at index $\text{target}$.
The **Quickselect** algorithm exploits the partition subroutine of Quicksort, but recurses into **only one side** of the partition, achieving $O(N)$ expected time.

### Rank Translation for Every $k$ on the Traced Array

The translation $\text{target} = N - k$ is a bijection between the two ways of naming a position, so every rank has exactly one answer, including both ends of the array:

| $k$ (rank from the largest) | Target index $N - k$ | Value at that index | What the extreme ranks demand |
|:---:|:---:|:---:|:---|
| 1 | 5 | 6 | The maximum; a size-$k$ min-heap degenerates to a single running maximum |
| 2 | 4 | **5** | The traced query |
| 3 | 3 | 4 | The upper median, where neither a heap of size $k$ nor one of size $N - k$ is small |
| 4 | 2 | 3 | Just below the median |
| 5 | 1 | 2 | Just above the minimum |
| 6 | 0 | 1 | The minimum; every element must be examined, and a size-$k$ heap would store the whole array |

Both endpoints are ordinary cases of the same rule rather than special branches: $k = 1$ maps to index $N - 1$ and $k = N$ maps to index $0$. Only the cost of the auxiliary strategies changes, which is why the conversion is stated once and never revisited.

---

## 2. Conceptual Foundation & Invariants

### Method A: Quickselect (In-Place Partitioning)
1. **Partition Around Pivot $p$:**
   Rearrange the active subarray $[L, R]$ into three segments:
   - Elements strictly less than $p$ on the left ($[L, \text{mid}_1 - 1]$).
   - Elements equal to $p$ in the middle ($[\text{mid}_1, \text{mid}_2]$).
   - Elements strictly greater than $p$ on the right ($[\text{mid}_2 + 1, R]$).
2. **Selective Branching:**
   - If $\text{target} < \text{mid}_1$: search left interval $[L, \text{mid}_1 - 1]$.
   - If $\text{target} > \text{mid}_2$: search right interval $[\text{mid}_2 + 1, R]$.
   - If $\text{mid}_1 \le \text{target} \le \text{mid}_2$: the pivot $p$ is at the target index! Return $p$.

### Method B: Min-Heap of Size $k$
Maintain a min-heap storing the $k$ largest elements seen so far:
- For each $x \in \text{nums}$:
  Push $x$ into the heap.
  If the heap size exceeds $k$, pop the minimum element.
- The root of the min-heap holds the $k^{\text{th}}$ largest element overall in $O(N \log k)$ time and $O(k)$ space.

> **Invariant.** After each Quickselect partition pass, the pivot element $p$ is placed at its permanent sorted index, and all elements to its left are $\le p$ while all elements to its right are $\ge p$.

---

## 3. Step-by-Step Worked Execution

We trace Quickselect on $\text{nums} = [3, 2, 1, 5, 6, 4]$ with $\text{target} = N - k = 6 - 2 = 4$:

### Pass 1: Active Interval $[L=0, R=5]$
- Array: $[3, 2, 1, 5, 6, 4]$.
- Select pivot $p = \text{nums}[3] = 5$ (or random).
- Three-way partition around $p = 5$:
  - Elements $< 5$: $[3, 2, 1, 4]$ (Indices $0 \dots 3$).
  - Elements $== 5$: $[5]$ (Index $4$).
  - Elements $> 5$: $[6]$ (Index $5$).
- Partitioned array:
  $$
  [\underbrace{3, 2, 1, 4}_{\text{Indices } 0 \dots 3}, \; \underbrace{\mathbf{5}}_{\text{Index } 4}, \; \underbrace{6}_{\text{Index } 5}]
  $$
- Pivot index is $\text{mid} = 4$.
- Check target:
  $$
  \text{target} = 4 == \text{mid}
  $$
- The target index matches the pivot index on the very first partition!
- Return pivot value $\mathbf{5}$.

---

### Alternative: Min-Heap Trace ($k = 2$)
We trace the size-$2$ min-heap evolution:
1. $x = 3$: $\text{heap} = [3]$.
2. $x = 2$: $\text{heap} = [2, 3]$ (Size $= 2$).
3. $x = 1$: Push $1 \implies [1, 3, 2]$. Pop min ($1$) $\implies \text{heap} = [2, 3]$.
4. $x = 5$: Push $5 \implies [2, 3, 5]$. Pop min ($2$) $\implies \text{heap} = [3, 5]$.
5. $x = 6$: Push $6 \implies [3, 5, 6]$. Pop min ($3$) $\implies \text{heap} = [5, 6]$.
6. $x = 4$: Push $4 \implies [4, 6, 5]$. Pop min ($4$) $\implies \text{heap} = [5, 6]$.
Final min-heap root: $\mathbf{5}$!

---

### When the First Partition Misses: The Duplicate Instance

The $k = 2$ sample is unusually kind — the first partition lands exactly on the target. The duplicate sample $\text{nums} = [3, 2, 3, 1, 2, 4, 5, 5, 6]$ with $k = 4$ forces three partitions, and it is the instance that shows what "recurse into one side" actually saves. Here $N = 9$, so the target index is $9 - 4 = 5$, and the ascending order of the array is $[1, 2, 2, 3, 3, 4, 5, 5, 6]$, confirming that index $5$ holds $4$.

Each partition runs over the active range only, takes the element at the middle index of that range as its pivot, and groups the range into values below the pivot, values equal to it, and values above it:

| Pass | Active range $[L, R]$ | Elements in play | Pivot (middle index of the range) | Whole array after the partition | Block of values equal to the pivot | Decision |
|:---:|:---:|:---:|:---:|:---|:---|:---|
| 1 | $[0, 8]$ | 9 | $2$ | `[1, 2, 2, 3, 4, 5, 5, 6, 3]` | $[1, 2]$ holds `2, 2` | $5 > 2$, so discard everything below the block and continue on $[3, 8]$ |
| 2 | $[3, 8]$ | 6 | $5$ | `[1, 2, 2, 3, 4, 3, 5, 5, 6]` | $[6, 7]$ holds `5, 5` | $5 < 6$, so discard the block and everything above it and continue on $[3, 5]$ |
| 3 | $[3, 5]$ | 3 | $4$ | `[1, 2, 2, 3, 3, 4, 5, 5, 6]` | $[5, 5]$ holds `4` | The target index lies inside the block, so the pivot value $4$ is the answer |

Three facts make this trace more instructive than the one-pass sample. First, the work shrinks geometrically: $9$, then $6$, then $3$ elements are examined, and the total of $18$ is linear in $N$, whereas ordering all nine elements would cost a multiple of $N \log N$. Second, the equal-value block is what makes duplicates safe — on the all-equal input $[2, 2, 2, 2]$ the very first partition puts every element into the block, so the search ends after one pass instead of degrading. Third, no element is ever compared with a discarded segment again: once the block $[1, 2]$ is known to sit below the target index, its values can never be the answer, because the target index is a position in the sorted order and positions are fixed.

---

## 4. Complete Execution Trace

```text
Target rank: k = 2nd largest -> target ascending index = 6 - 2 = 4

Quickselect Trace:
Range [0, 5]: [3, 2, 1, 5, 6, 4]
Pivot = 5
Partition result: [3, 2, 1, 4 | 5 | 6]
Pivot placed at index 4.
Target index is 4 -> MATCH! Return nums[4] = 5

Min-Heap Trace (capacity 2):
Add 3 -> [3]
Add 2 -> [2, 3]
Add 1 -> [2, 3] (1 evicted)
Add 5 -> [3, 5] (2 evicted)
Add 6 -> [5, 6] (3 evicted)
Add 4 -> [5, 6] (4 evicted)
Top element = 5 -> Result: 5
```

| Element $x$ | Min-Heap State (Size $\le 2$) | Evicted Smallest Element | Active Window Top |
|:---:|:---|:---:|:---:|
| 3 | `[3]` | None | 3 |
| 2 | `[2, 3]` | None | 2 |
| 1 | `[2, 3]` | 1 | 2 |
| **5** | **`[3, 5]`** | **2** | **3** |
| **6** | **`[5, 6]`** | **3** | **5** |
| **4** | **`[5, 6]`** | **4** | **5 (Result)** |

---

## 5. Algorithmic Correctness

**Soundness.** In Quickselect, placing a pivot at index $m$ guarantees that all elements in $[0, m-1]$ are $\le \text{nums}[m]$ and all elements in $[m+1, N-1]$ are $\ge \text{nums}[m]$. If $m == \text{target}$, then $\text{nums}[m]$ is by definition the element that would appear at index $\text{target}$ in a fully sorted array.

**Completeness.** In each step, the algorithm discards the partition half that does not contain $\text{target}$. Since the true target element is contained within the retained partition, the search space strictly shrinks until the target index is reached.

---

## 6. Traps This Instance Exposes

- **Quicksort vs Quickselect:** Quicksort branches into both subintervals, taking $O(N \log N)$. Quickselect branches into **only one** subinterval, summing work geometrically: $N + N/2 + N/4 + \dots \le 2N = O(N)$.
- **Worst-Case Pivot Degradation:** Always picking the first element as pivot on an already-sorted array leads to $O(N^2)$ worst-case time. Using random pivot selection or middle-index selection avoids adversarial degradation in practice.
- **Handling Duplicate Values:** Arrays with many identical values (e.g. $[2, 2, 2, 2]$) can degrade two-way partitioning to $O(N^2)$. Three-way partitioning ($<, ==, >$) groups duplicates together and terminates immediately if $\text{target}$ falls in the middle range.

### Alternative Strategies and Their Tradeoffs

| Strategy | Mechanism | Time | Auxiliary space | Failure mode or tradeoff |
|:---|:---|:---|:---|:---|
| Three-way Quickselect (used above) | Partition, then recurse into the one segment that contains the target index | $O(N)$ expected, $O(N^2)$ worst case | $O(1)$ if iterated, $O(\log N)$ recursion depth | The worst case is possible, not merely unlikely, when the pivot rule is adversarial |
| Full sort, then read index $N - k$ | Order every element and index into the result | $O(N \log N)$ deterministic | Depends on the sort; $O(N)$ for a merge sort | Simple and predictable, but it computes $N$ answers when one is needed |
| Size-$k$ min-heap over a single pass | Keep the $k$ largest values seen, evicting the smallest | $O(N \log k)$ deterministic | $O(k)$ | Excellent for small $k$ and for streaming input, but it stores the whole array when $k$ approaches $N$ |
| Max-heap of all elements, then $k$ extractions | Build a heap of every value and pop $k$ times | $O(N + k \log N)$ | $O(N)$ | The $k$-th pop is the answer, but the heap holds the entire array, which the size-$k$ heap avoids |
| Frequency array indexed by value | Count occurrences over the bounded value range and walk from the largest value downward | $O(N + V)$, where $V$ is the range of allowed values | $O(V)$ | Deterministic and linear, but it exploits the stated value bound and does not generalize to unbounded or non-numeric keys |
| Median-of-medians pivot selection inside Quickselect | Choose a provably good pivot so each partition removes a constant fraction | $O(N)$ worst case | $O(1)$ beyond the input | Removes the quadratic risk entirely, at the cost of a heavier pivot routine and larger constants than randomization |

The choice is driven by two questions that this instance answers concretely. How large is $k$ relative to $N$? A small $k$ favors the heap; a $k$ near the middle favors selection. And must the bound hold in the worst case, or is an expected bound acceptable? Quickselect with a randomized or middle-index pivot is expected linear, while median-of-medians is linear with certainty but slower in practice.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Quickselect: $O(N)$ expected average time. Worst-case is $O(N^2)$, mitigated by random pivot selection.
  - Min-Heap: $O(N \log k)$ deterministic time.
- **Auxiliary Space Complexity:**
  - Quickselect: $O(1)$ auxiliary space if implemented iteratively, or $O(\log N)$ recursion call stack space.
  - Min-Heap: $O(k)$ auxiliary space to maintain the priority queue.
