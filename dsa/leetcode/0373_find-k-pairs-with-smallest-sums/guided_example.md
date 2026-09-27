# Guided Example: Find K Pairs with Smallest Sums

We trace the step-by-step min-heap $K$-way merge frontier, Cartesian product row abstraction ($nums1[i] + nums2[j]$), initial prefix seeding ($\min(k, m)$ rows), and successive column pointer advances ($j \to j + 1$) on representative sorted array pairs:

- **Input:** $nums1 = [1, 7, 11], \quad nums2 = [2, 4, 6], \quad k = 3$
- **Required output:** `[[1, 2], [1, 4], [1, 6]]`
  - Pair sums matrix ($3 \times 3$):
    - Row 0 ($nums1[0] = 1$): $[1+2=3, \; 1+4=5, \; 1+6=7]$
    - Row 1 ($nums1[1] = 7$): $[7+2=9, \; 7+4=11, \; 7+6=13]$
    - Row 2 ($nums1[2] = 11$): $[11+2=13, \; 11+4=15, \; 11+6=17]$
  - Step 1: Pop minimum $[3, 0, 0]$ $\implies$ emit $[1, 2]$, push successor $[1+4=5, 0, 1]$
  - Step 2: Pop minimum $[5, 0, 1]$ $\implies$ emit $[1, 4]$, push successor $[1+6=7, 0, 2]$
  - Step 3: Pop minimum $[7, 0, 2]$ $\implies$ emit $[1, 6]$, row 0 exhausted
  - $k = 3$ pairs collected $\implies$ terminate
  - Final collection: `[[1, 2], [1, 4], [1, 6]]`
- **Tied Sums Instance:** $nums1 = [1, 1, 2], nums2 = [1, 2, 3], k = 2 \implies [[1, 1], [1, 1]]$
- **Large $k$ Saturation:** $k \ge |nums1| \cdot |nums2| \implies$ returns all Cartesian pairs in sorted order

This instance demonstrates multi-way stream merging using priority queues, mathematically proves why only the first $\min(k, |nums1|)$ rows can ever contribute to the top $k$ smallest pairs, avoids generating all $M \cdot N$ pairs, and achieves $O(K \log(\min(K, M)))$ time and $O(\min(K, M))$ space complexity.

---

## 1. Instance & Teaching Goal

Given two non-decreasing sorted integer arrays:
$$
nums1 = [1, 7, 11], \quad nums2 = [2, 4, 6], \quad k = 3
$$
Find the $k$ pairs $(u, v)$ (with $u \in nums1, v \in nums2$) that have the smallest sums $u + v$:

```text
Pair Sum Grid (nums1 along rows, nums2 along columns):
          nums2:   2    4    6
nums1:  1  ---> [  3,   5,   7 ]  <-- Row 0 (Sorted)
        7  ---> [  9,  11,  13 ]  <-- Row 1 (Sorted)
       11  ---> [ 13,  15,  17 ]  <-- Row 2 (Sorted)

All rows are monotonically non-decreasing because nums2 is sorted.
Problem reduces to: MERGE K SORTED LISTS!

Target: First 3 Smallest Pairs -> [1, 2] (sum 3), [1, 4] (sum 5), [1, 6] (sum 7)
```

### Why Generating All Pairs ($O(MN \log(MN))$) Fails
- The total number of pairs is $M \cdot N$. For $M, N = 10^5$, $M \cdot N = 10^{10}$, impossible to compute.
- However, $k$ is typically much smaller ($k \le 10^4$).
- Because each row $i$ is sorted, the smallest unused element in row $i$ is always at column $j$.
- By seeding the min-heap with the first element of each of the first $\min(k, M)$ rows, the global minimum is always at the top of the heap. When $(i, j)$ is popped, we only need to push $(i, j + 1)$!

---

## 2. Conceptual Foundation & Invariants

### 1. Min-Heap State Entry:
Each entry in min-heap `q` is a 3-tuple:
$$
[\text{sum}, \; i, \; j] = [nums1[i] + nums2[j], \; i, \; j]
$$
where $i$ is the row index in $nums1$ and $j$ is the column index in $nums2$.

### 2. Heap Seeding:
Seed only the first element ($j = 0$) of the first $\min(k, |nums1|)$ rows:
$$
q = \big\{ [nums1[i] + nums2[0], \; i, \; 0] \;\big|\; 0 \le i < \min(k, |nums1|) \big\}
$$
Any row $i \ge k$ can never supply a pair smaller than the already seeded $k$ pairs because $nums1$ is sorted.

### 3. Extraction & Advancement Loop:
While $q$ is non-empty and $k > 0$:
1. Pop minimum: $(\_, i, j) = heappop(q)$.
2. Record output pair: $ans.\text{append}([nums1[i], nums2[j]])$.
3. Decrement: $k \leftarrow k - 1$.
4. Advance frontier in row $i$:
   $$
   \text{if } j + 1 < \text{len}(nums2): \quad heappush(q, \; [nums1[i] + nums2[j+1], \; i, \; j+1])
   $$

> **Invariant.** The min-heap always contains the smallest uncollected element from every active row, guaranteeing that the heap root is the globally minimal uncollected pair sum.

---

## 3. Step-by-Step Worked Execution

We trace $nums1 = [1, 7, 11], nums2 = [2, 4, 6], k = 3$:
$M = 3, N = 3, k = 3$.

---

### Step 1: Heap Initialization
Seed rows $i = 0, 1, 2$ with column $j = 0$:
- Row 0: $nums1[0] + nums2[0] = 1 + 2 = 3 \implies [3, 0, 0]$
- Row 1: $nums1[1] + nums2[0] = 7 + 2 = 9 \implies [9, 1, 0]$
- Row 2: $nums1[2] + nums2[0] = 11 + 2 = 13 \implies [13, 2, 0]$
Heap state:
$$
q = \big[ [3, 0, 0], \; [9, 1, 0], \; [13, 2, 0] \big]
$$

---

### Step 2: Extraction 1 ($k = 3 \to 2$)
- Pop root: $[3, 0, 0]$.
- Selected pair: $[nums1[0], nums2[0]] = [\mathbf{1}, \mathbf{2}]$ (Sum = 3).
- Append: $ans = [[\mathbf{1, 2}]]$.
- Advance row 0: $j + 1 = 1 < 3$.
  $$
  \text{new\_sum} = nums1[0] + nums2[1] = 1 + 4 = \mathbf{5}
  $$
  Push $[5, 0, 1]$ into heap.
- Heap: `[[5, 0, 1], [9, 1, 0], [13, 2, 0]]`.

---

### Step 3: Extraction 2 ($k = 2 \to 1$)
- Pop root: $[5, 0, 1]$.
- Selected pair: $[nums1[0], nums2[1]] = [\mathbf{1}, \mathbf{4}]$ (Sum = 5).
- Append: $ans = [[1, 2], \; [\mathbf{1, 4}]]$.
- Advance row 0: $j + 1 = 2 < 3$.
  $$
  \text{new\_sum} = nums1[0] + nums2[2] = 1 + 6 = \mathbf{7}
  $$
  Push $[7, 0, 2]$ into heap.
- Heap: `[[7, 0, 2], [9, 1, 0], [13, 2, 0]]`.

---

### Step 4: Extraction 3 ($k = 1 \to 0$)
- Pop root: $[7, 0, 2]$.
- Selected pair: $[nums1[0], nums2[2]] = [\mathbf{1}, \mathbf{6}]$ (Sum = 7).
- Append: $ans = [[1, 2], [1, 4], \; [\mathbf{1, 6}]]$.
- Advance row 0: $j + 1 = 3 \not< 3$. Row 0 is now completely exhausted.
- Counter $k = 0 \implies$ loop terminates!

---

### Step 5: Final Result
Return the 3 collected pairs:
$$
\mathbf{[[1, 2], [1, 4], [1, 6]]}
$$

---

## 4. Complete Execution Trace

```text
nums1 = [1, 7, 11], nums2 = [2, 4, 6], k = 3
Seeded Heap: [[3, 0, 0], [9, 1, 0], [13, 2, 0]]

Extraction 1:
  pop [3, 0, 0] -> ans = [[1, 2]]
  push [1+4=5, 0, 1]
  heap = [[5, 0, 1], [9, 1, 0], [13, 2, 0]]

Extraction 2:
  pop [5, 0, 1] -> ans = [[1, 2], [1, 4]]
  push [1+6=7, 0, 2]
  heap = [[7, 0, 2], [9, 1, 0], [13, 2, 0]]

Extraction 3:
  pop [7, 0, 2] -> ans = [[1, 2], [1, 4], [1, 6]]
  row 0 col 3 out of bounds
  k reached 0 -> Exit

Output: [[1, 2], [1, 4], [1, 6]]
```

| Step | Heap Minimum Popped | Pair Sum | Emitted Pair $[u, v]$ | Successor Pushed into Heap | Updated Heap Contents | Remaining $k$ |
|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Init | - | - | - | Seed rows $0 \dots 2$ | `[[3, 0, 0], [9, 1, 0], [13, 2, 0]]` | 3 |
| 1 | `[3, 0, 0]` | 3 | `[1, 2]` | `[5, 0, 1]` | `[[5, 0, 1], [9, 1, 0], [13, 2, 0]]` | 2 |
| 2 | `[5, 0, 1]` | 5 | `[1, 4]` | `[7, 0, 2]` | `[[7, 0, 2], [9, 1, 0], [13, 2, 0]]` | 1 |
| **3** | **`[7, 0, 2]`** | **7** | **`[1, 6]`** | **None (Row 0 done)** | **`[[9, 1, 0], [13, 2, 0]]`** | **0 (Done)** |

---

## 5. Algorithmic Correctness

**Soundness.** Because both arrays are sorted in non-decreasing order, the sum matrix satisfies $S_{i, j} \le S_{i, j+1}$. At any point, the uncollected elements of each row form a contiguous suffix starting at the current column pointer. Since the heap holds the smallest element of each active row, the minimum entry in the heap is smaller than or equal to all uncollected elements in all active rows. By induction, every popped pair is the globally minimal uncollected pair.

**Completeness.** Since $nums1$ is non-decreasing, any row $i \ge k$ has $nums1[i] + nums2[0] \ge nums1[p] + nums2[0]$ for all $p < k$. Hence, the first $k$ rows alone are sufficient to supply at least $k$ elements that are smaller than or equal to any element in row $i \ge k$. Pruning rows beyond $k$ guarantees completeness without omitting valid candidates.

---

## 6. Traps This Instance Exposes

- **Seeding All $M$ Rows:** If $|nums1| = 10^5$ and $k = 3$, seeding all $M$ rows takes $O(M)$ memory and $O(M)$ heap construction time. Seeding only $\min(k, |nums1|)$ bounds initialization strictly by $k$.
- **2D Grid Frontier Duplication:** In grid BFS, moving both Right and Down from $(i, j)$ can push $(i+1, j+1)$ twice from $(i+1, j)$ and $(i, j+1)$, requiring a large hash set for deduplication. In contrast, fixed-row merging assigns each row exclusively to one pointer, ensuring zero duplicate heap pushes without visited sets.
- **Tied Pair Sums:** When multiple pairs have equal sums, Python compares the tuple coordinates `(sum, i, j)`. Because coordinates $(i, j)$ are unique, no comparison errors occur.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(K \log(\min(K, M)))$, where $M = \text{len}(nums1)$.
  - Heap size is at most $H = \min(K, M)$.
  - Heapifying the first $H$ elements takes $O(H)$ time.
  - The while loop executes exactly $K$ iterations (or until pairs exhaust).
  - Each iteration performs one `heappop` and at most one `heappush`, taking $O(\log H)$ time.
  - Total time: $O(H + K \log H) = O(K \log(\min(K, M)))$.
- **Auxiliary Space Complexity:** $O(\min(K, M))$ auxiliary space to maintain the priority queue `q`.
