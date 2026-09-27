# Guided Example: Kth Largest Element in a Stream

We trace the step-by-step fixed-capacity min-heap maintenance ($|H| \le k$), streaming value insertion ($\text{heappush}(H, val)$), surplus minimum eviction ($\text{heappop}(H)$ when $|H| > k$), $k$-th order statistic isolation at the heap root ($H[0]$), and dynamic threshold updates on representative real-time data streams:

- **Input:**
  - Capacity: $k = 3$
  - Initial array: $nums = [4, 5, 8, 2]$
  - Query sequence: $\text{add}(3), \; \text{add}(5), \; \text{add}(10), \; \text{add}(9), \; \text{add}(4)$
- **Required output:** `[4, 5, 5, 8, 8]`
  - Problem objective:
    - Maintain a continuous stream of numerical insertions.
    - After each insertion, return the **$k$-th largest** element in the entire accumulated stream.
    - Note that this refers to sorted multiplicity order (duplicate values each count toward the rank).
- **The Min-Heap Size-$k$ Invariant:**
  - **The Top-$k$ Filtration Principle:**
    - To find the $k$-th largest element, we only ever care about the **top $k$ largest numbers** seen so far. All other smaller elements have zero chance of ever being the $k$-th largest again.
    - Store the $k$ largest elements in a **min-heap** $H$.
  - **Why a Min-Heap (Not a Max-Heap)?**
    - Inside a collection of the $k$ largest elements:
      - The **root** of the min-heap holds the **minimum** of these $k$ elements:
        $$
        H[0] = \min(k \text{ largest elements})
        $$
      - By definition, there are exactly $k - 1$ elements larger than $H[0]$ in the heap (and in the entire stream).
      - Therefore, the root $H[0]$ is mathematically the **$k$-th largest element**!
  - **Stream Insertion Protocol ($\text{add}(val)$):**
    1. Insert $val$ into min-heap $H$:
       $$
       H \leftarrow H \cup \{val\} \quad (|H| \le k + 1)
       $$
    2. If $|H| > k$:
       - Evict the smallest element (which cannot be in the top $k$):
         $$
         \text{pop}(H)
         $$
    3. Return root element $H[0]$ in $O(1)$ time.
- **Step-by-Step Worked Execution Trace on $k = 3, nums = [4, 5, 8, 2]$:**
  - **Phase 0: Initialization with $nums = [4, 5, 8, 2]$:**
    - Insert 4: $H = [4]$ (size 1)
    - Insert 5: $H = [4, 5]$ (size 2)
    - Insert 8: $H = [4, 5, 8]$ (size 3)
    - Insert 2: $H = [2, 4, 5, 8]$ (size 4 $> k$).
      - Pop minimum ($2$):
      - $H = [4, 5, 8]$ (size 3).
    - Stable min-heap: $H = [4, 5, 8]$ with root $H[0] = \mathbf{4}$.
  - **Stream Event 1: $\text{add}(3)$:**
    - Push 3: $H = [3, 4, 5, 8]$ (size 4).
    - Pop minimum: 3 is popped.
    - Heap remains: $H = [4, 5, 8]$.
    - Root: $H[0] = \mathbf{4}$.
    - Return **`4`**.
  - **Stream Event 2: $\text{add}(5)$:**
    - Push 5: $H = [4, 5, 5, 8]$ (size 4).
    - Pop minimum: 4 is popped.
    - Heap becomes: $H = [5, 5, 8]$.
    - Root: $H[0] = \mathbf{5}$.
    - Return **`5`**.
  - **Stream Event 3: $\text{add}(10)$:**
    - Push 10: $H = [5, 5, 8, 10]$ (size 4).
    - Pop minimum: 5 is popped.
    - Heap becomes: $H = [5, 8, 10]$.
    - Root: $H[0] = \mathbf{5}$.
    - Return **`5`**.
  - **Stream Event 4: $\text{add}(9)$:**
    - Push 9: $H = [5, 8, 9, 10]$ (size 4).
    - Pop minimum: 5 is popped.
    - Heap becomes: $H = [8, 9, 10]$.
    - Root: $H[0] = \mathbf{8}$.
    - Return **`8`**.
  - **Stream Event 5: $\text{add}(4)$:**
    - Push 4: $H = [4, 8, 9, 10]$ (size 4).
    - Pop minimum: 4 is popped.
    - Heap remains: $H = [8, 9, 10]$.
    - Root: $H[0] = \mathbf{8}$.
    - Return **`8`**.
  - **Consolidated Query Results:**
    $$
    [\mathbf{4}, \; \mathbf{5}, \; \mathbf{5}, \; \mathbf{8}, \; \mathbf{8}]
    $$
- **Empty Initial Array ($nums = [], k = 1$):**
  - First call `add(3)` pushes 3, heap has size 1 $\le k$. Root is 3 $\implies$ returns 3.
  - Subsequent call `add(5)` pushes 5, pops 3, root is 5 $\implies$ returns 5.
- **Handling Duplicate High Values ($k = 2, nums = [5, 5]$):**
  - Min-heap stores duplicate values faithfully: $H = [5, 5]$.
  - Root is 5 (the second largest element).

This instance demonstrates online dynamic order statistics and sliding window top-$k$ truncation, mathematically proves why a bounded min-heap of size $k$ maintains the $k$-th order statistic at its root in logarithmic time, and derives $O(N \log k)$ preprocessing, $O(\log k)$ query time, and $O(k)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a stream of numbers and integer $k$:
Implement a data structure that returns the **$k$-th largest element** after each incoming number.

```text
k = 3, initial nums = [ 4, 5, 8, 2 ]

Build min-heap of size 3:
  Top 3 elements: [ 4, 5, 8 ]
  Min-heap root: 4 (this is the 3rd largest!)

Stream additions:
  add(3)  -> min-heap keeps [ 4, 5, 8 ]  -> returns 4
  add(5)  -> min-heap becomes [ 5, 5, 8 ] -> returns 5
  add(10) -> min-heap becomes [ 5, 8, 10] -> returns 5
  add(9)  -> min-heap becomes [ 8, 9, 10] -> returns 8
  add(4)  -> min-heap keeps [ 8, 9, 10]  -> returns 8

Results: [ 4, 5, 5, 8, 8 ]
```

### The Invariant of the $k$-Element Min-Heap
- By capping the min-heap capacity at exactly $k$ items, the root of the heap is always the smallest of the top-$k$ numbers.
- The smallest of the top-$k$ numbers is, by definition, the $k$-th largest number overall.

---

## 2. Conceptual Foundation & Invariants

### 1. Ingestion Step:
$$
\text{heappush}(H, val)
$$
$$
\text{If } |H| > k \implies \text{heappop}(H)
$$

### 2. Order Statistic Retrieval:
$$
ans = H[0]
$$

> **Truncated Order Statistic Invariant.** For any multiset $S$ of cardinality $|S| \ge k$, the $k$-th order statistic with respect to descending order coincides identically with the infimum of the upper filter $\mathcal{F}_k(S) = \{x \in S \mid |\{y \in S \mid y \ge x\}| \le k\}$, maintained dynamically as the root of a min-heap of capacity $k$.

---

## 3. Step-by-Step Worked Execution

We trace the sample stream:

---

### Step 1: Initial Array $[4, 5, 8, 2]$
- Push all, keep top 3: $H = [4, 5, 8]$.

---

### Step 2: `add(3)`
- Push 3 $\implies [3, 4, 5, 8]$.
- Pop 3 $\implies [4, 5, 8]$. Root = **4**.

---

### Step 3: `add(5)`
- Push 5 $\implies [4, 5, 5, 8]$.
- Pop 4 $\implies [5, 5, 8]$. Root = **5**.

---

### Step 4: `add(10)`
- Push 10 $\implies [5, 5, 8, 10]$.
- Pop 5 $\implies [5, 8, 10]$. Root = **5**.

---

### Step 5: `add(9)`
- Push 9 $\implies [5, 8, 9, 10]$.
- Pop 5 $\implies [8, 9, 10]$. Root = **8**.

---

### Step 6: `add(4)`
- Push 4 $\implies [4, 8, 9, 10]$.
- Pop 4 $\implies [8, 9, 10]$. Root = **8**.

---

## 4. Complete Execution Trace

| Stream Operation | Incoming Value | Heap Before Pop | Evicted Minimum | Retained Top $k$ Heap | Root $H[0]$ (Returned) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `Init` | $nums = [4, 5, 8, 2]$ | $[2, 4, 5, 8]$ | $2$ | `[4, 5, 8]` | $4$ |
| `add(3)` | $3$ | $[3, 4, 5, 8]$ | $3$ | `[4, 5, 8]` | **`4`** |
| `add(5)` | $5$ | $[4, 5, 5, 8]$ | $4$ | `[5, 5, 8]` | **`5`** |
| `add(10)` | $10$ | $[5, 5, 8, 10]$ | $5$ | `[5, 8, 10]` | **`5`** |
| `add(9)` | $9$ | $[5, 8, 9, 10]$ | $5$ | `[8, 9, 10]` | **`8`** |
| `add(4)` | $4$ | $[4, 8, 9, 10]$ | $4$ | `[8, 9, 10]` | **`8`** |

---

## 5. Boundary Cases & Failure Modes

- **Initial Array Empty ($nums = []$):** Handled smoothly by adding elements until $|H| == k$.
- **$k = 1$:** Heap of size 1 acts as a running maximum tracker.
- **Negative Numbers ($nums = [-10, -5, -2]$):** Handled identically by standard integer ordering.
- **Large Stream ($M = 10^4$ calls):** Each call performs at most 1 heap push and 1 heap pop of size $k$.

---

## 6. Traps & Common Anti-Patterns

- **Sorting on Every `add` ($O(M \cdot N \log N)$):** Re-sorting the array on each incoming value causes quadratic blowup (TLE). A min-heap executes updates in $O(\log k)$.
- **Using a Max-Heap:** A max-heap would need to store all $N$ elements seen so far to find the $k$-th largest, consuming $O(N)$ space and $O(\log N)$ time per call. A min-heap of size $k$ consumes only $O(k)$ space.
- **Distinct Elements Assumption:** The problem specifies the $k$-th largest element in sorted order, **not** distinct values. Duplicates are retained in the heap.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Initialization: $N$ additions $\implies \mathcal{O}(N \log k)$.
  - Each `add` operation: 1 push and at most 1 pop in a heap of size $k$ $\implies \mathcal{O}(\log k)$.
  - For $M$ stream queries, total query time is $\mathcal{O}(M \log k)$. Completes in $< 15$ ms for $M = 10^4, k = 1000$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(k)$ auxiliary space to maintain the min-heap of at most $k + 1$ elements.