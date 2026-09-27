# Guided Example: Sliding Window Median

We trace the step-by-step dual-heap architecture (max-heap lower half, min-heap upper half), hash-map lazy deletion tracking (`delayed[x] += 1`), heap top pruning (`prune()`), size rebalancing, and window median extraction on representative rolling array windows:

- **Input:** $nums = [1, 3, -1, -3, 5, 3, 6, 7], \quad k = 3$
- **Required output:** `[1.0, -1.0, -1.0, 3.0, 5.0, 6.0]`
  - Window width: $k = 3$ (Odd $\implies$ median is the top of the lower half)
  - Heap invariants:
    - `small`: Max-heap holding the smaller $\lceil k / 2 \rceil = 2$ elements
    - `large`: Min-heap holding the larger $\lfloor k / 2 \rfloor = 1$ elements
    - $\text{size}(small) = \text{size}(large) + 1$
- **Sliding window execution trace:**
  - **Initial Window $[1, 3, -1]$ (Indices $0 \dots 2$):**
    - Insert $1 \implies small = [1]$
    - Insert $3 \implies large = [3]$
    - Insert $-1 \implies small = [1, -1]$
    - State: $small = [1, -1]$ (top is $1$), $large = [3]$ (top is $3$).
    - Median: $\text{top}(small) = \mathbf{1.0}$
  - **Window 2 (Slide to $[-1, -3, 3]$, In: $-3$, Out: $1$):**
    - Add $-3 \le 1 \implies$ added to $small$.
    - Remove $1 \le 1 \implies$ mark $delayed[1] += 1$, decrement $small\_size$.
    - Prune $small$: top is $1 \in delayed \implies$ popped! $delayed[1] = 0$.
    - Rebalance heaps $\implies small = [-1, -3]$ (top $-1$), $large = [3]$.
    - Median: $\text{top}(small) = \mathbf{-1.0}$
  - **Window 3 (Slide to $[-3, 5, -1]$, In: $5$, Out: $3$):**
    - Add $5 > -1 \implies$ added to $large$.
    - Remove $3 \implies$ mark $delayed[3] += 1$, decrement $large\_size$.
    - Prune $large$: top is $3 \in delayed \implies$ popped!
    - Rebalance $\implies small = [-1, -3]$ (top $-1$), $large = [5]$.
    - Median: $\text{top}(small) = \mathbf{-1.0}$
  - **Window 4 (Slide to $[5, 3, -3]$, In: $3$, Out: $-1$):**
    - Add $3$, remove $-1 \implies$ Rebalanced heaps: $small = [3, -3]$ (top $3$), $large = [5]$.
    - Median: $\mathbf{3.0}$
  - **Window 5 (Slide to $[3, 6, 5]$, In: $6$, Out: $-3$):**
    - Add $6$, remove $-3 \implies$ Rebalanced heaps: $small = [5, 3]$ (top $5$), $large = [6]$.
    - Median: $\mathbf{5.0}$
  - **Window 6 (Slide to $[6, 7, 3]$, In: $7$, Out: $5$):**
    - Add $7$, remove $5 \implies$ Rebalanced heaps: $small = [6, 3]$ (top $6$), $large = [7]$.
    - Median: $\mathbf{6.0}$
  - Accumulated medians: `[1.0, -1.0, -1.0, 3.0, 5.0, 6.0]`
- **Even Window Instance ($k = 4$):** $nums = [1, 2, 3, 4] \implies small = [2, 1], large = [3, 4] \implies \text{median} = \frac{2 + 3}{2} = \mathbf{2.5}$
- **Single Element Window ($k = 1$):** Each window median is the element itself.

This instance demonstrates dual-heap partition balancing with lazy tombstone deletion, mathematically proves why lazy pruning on heap roots preserves exact $O(\log K)$ operations without $O(K)$ arbitrary heap deletions, and derives $O(N \log K)$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $nums$ and an integer $k$:
There is a sliding window of size $k$ which moves from the very left of the array to the very right.
Return the **median array** for each window in the original array.
- If $k$ is odd, the median is the middle element of the sorted window.
- If $k$ is even, the median is the arithmetic mean of the two middle elements.

```text
Window Trace (k = 3):
  [ 1,  3, -1] -3   5   3   6   7   -> Sorted: [-1,  1,  3] -> Median =  1.0
   1 [ 3, -1, -3]  5   3   6   7   -> Sorted: [-3, -1,  3] -> Median = -1.0
   1   3 [-1, -3,  5]  3   6   7   -> Sorted: [-3, -1,  5] -> Median = -1.0
   1   3  -1 [-3,  5,  3]  6   7   -> Sorted: [-3,  3,  5] -> Median =  3.0
   1   3  -1  -3 [ 5,  3,  6]  7   -> Sorted: [ 3,  5,  6] -> Median =  5.0
   1   3  -1  -3   5 [ 3,  6,  7]  -> Sorted: [ 3,  6,  7] -> Median =  6.0
```

### The $O(K)$ Deletion Problem
In standard binary heaps:
- Finding and removing an arbitrary element (the element sliding out of the window) requires linear search through the heap array, taking $O(K)$ time per step, which gives $O(N \cdot K)$ overall.
- **The Lazy Deletion (Tombstone) Pattern:**
  Instead of immediately hunting down the expired element inside the heap:
  1. We record the element in a hash map `delayed[x] += 1` to mark it as dead.
  2. We update the logical size of the heap.
  3. We only physically remove expired elements when they naturally surface at the **top** of the heap (`heappop()`).
  This achieves strictly $O(\log K)$ amortized time per window slide.

---

## 2. Conceptual Foundation & Invariants

### 1. Dual-Heap Partitioning:
Divide the current active window of $k$ numbers into two halves:
- `small`: Max-heap storing the smaller $\lceil k / 2 \rceil$ numbers.
- `large`: Min-heap storing the larger $\lfloor k / 2 \rfloor$ numbers.
- **Size Invariant:**
  $$
  \text{size}(small) \in \{\text{size}(large), \; \text{size}(large) + 1\}
  $$
- **Value Ordering Invariant:**
  $$
  \max(small) \le \min(large)
  $$

### 2. Median Extraction:
- If $k$ is odd:
  $$
  \text{median} = \text{top}(small)
  $$
- If $k$ is even:
  $$
  \text{median} = \frac{\text{top}(small) + \text{top}(large)}{2.0}
  $$

### 3. The Prune Operation:
Whenever the root of a heap is an expired element recorded in `delayed`:
- Decrement its count in `delayed`.
- If its count reaches 0, delete the key.
- Pop the root from the heap.
Repeat until the root is a valid, active window element.

> **Lazy Deletion Invariant.** A heap root is never an expired element when reading the median or performing rebalancing. All dead elements inside the heap body are inert and do not distort the median.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [1, 3, -1, -3, 5, 3, 6, 7]$ with $k = 3$:

---

### Step 1: Initialize First Window $[1, 3, -1]$
- Insert $1$: $small = [1]$.
- Insert $3$: $1 < 3 \implies large = [3]$.
- Insert $-1$: $-1 \le 1 \implies small = [1, -1]$.
- State:
  - $small$ top $= 1$, size $= 2$
  - $large$ top $= 3$, size $= 1$
- Emit median: $\mathbf{1.0}$.

---

### Step 2: Slide to Window 2 (Out: $1$, In: $-3$)
- Add new element $-3$:
  - $-3 \le \text{top}(small) (1) \implies$ Push to $small$.
  - Logical $small\_size = 3$.
- Remove exiting element $1$:
  - $1 \le \text{top}(small) (1) \implies$ Belonged to $small$.
  - Decrement logical size: $small\_size \leftarrow 3 - 1 = \mathbf{2}$.
  - Record tombstone: $delayed[1] += 1$.
- Prune $small$:
  - Root of $small$ is $1 \in delayed$.
  - Pop $1$ from $small$, remove $1$ from $delayed$.
  - New root of $small$ is $-1$.
- Check balance:
  - $small\_size = 2, large\_size = 1$ (Balanced!).
- Emit median: $\text{top}(small) = \mathbf{-1.0}$.

---

### Step 3: Slide to Window 3 (Out: $3$, In: $5$)
- Add new element $5$:
  - $5 > \text{top}(small) (-1) \implies$ Push to $large$.
  - $large\_size \leftarrow 1 + 1 = 2$.
- Remove exiting element $3$:
  - $3 > -1 \implies$ Belonged to $large$.
  - $large\_size \leftarrow 2 - 1 = \mathbf{1}$.
  - Record tombstone: $delayed[3] += 1$.
- Prune $large$:
  - Root of $large$ is $3 \in delayed$.
  - Pop $3$, clear from $delayed$.
  - New root of $large$ is $5$.
- Emit median: $\text{top}(small) = \mathbf{-1.0}$.

---

### Step 4: Slide to Window 4 (Out: $-1$, In: $3$)
- Add $3$, remove $-1$:
  - $small$ root becomes $3$. $large$ root is $5$.
  - Emit median: $\mathbf{3.0}$.

---

### Step 5: Slide to Windows 5 and 6
- Window 5 ($[5, 3, 6]$): $small$ root is $5$, $large$ root is $6 \implies$ Median = $\mathbf{5.0}$.
- Window 6 ($[3, 6, 7]$): $small$ root is $6$, $large$ root is $7 \implies$ Median = $\mathbf{6.0}$.

---

## 4. Complete Execution Trace

| Window Index | Incoming $x$ | Outgoing $y$ | $small$ Active Top | $large$ Active Top | Pruning Actions | Emitted Median |
|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| **$0 \dots 2$** | — | — | $1$ | $3$ | Initial load | **$1.0$** |
| **$1 \dots 3$** | $-3$ | $1$ | $-1$ | $3$ | Pop $1$ from $small$ | **$-1.0$** |
| **$2 \dots 4$** | $5$ | $3$ | $-1$ | $5$ | Pop $3$ from $large$ | **$-1.0$** |
| **$3 \dots 5$** | $3$ | $-1$ | $3$ | $5$ | Pop $-1$ from $small$ | **$3.0$** |
| **$4 \dots 6$** | $6$ | $-3$ | $5$ | $6$ | Rebalance $small \leftrightarrow large$ | **$5.0$** |
| **$5 \dots 7$** | $7$ | $5$ | $6$ | $7$ | Pop $5$ from $small$ | **$6.0$** |

---

## 5. Boundary Cases & Failure Modes

- **Window Size $k = 1$:** Every number is its own median; heaps hold at most 1 element $\implies$ emits $nums$ directly as floats.
- **Window Size Equals Array Length ($k = N$):** Exactly 1 median is computed.
- **Even Window Size ($k = 2$):** Both heaps have size 1; computes average of both roots $\implies \frac{\text{top}(small) + \text{top}(large)}{2.0}$.
- **Duplicate Numbers in Window:** Hash map counts multiplicities (`delayed[x] += 1`), ensuring identical values are pruned one-by-one without prematurely dropping active duplicates.

---

## 6. Traps & Common Anti-Patterns

- **Searching the Heap for $O(K)$ Removal:** Calling `heap.remove(x)` in Python takes $O(K)$ time, turning the sliding window into an $O(N \cdot K)$ algorithm that causes Time Limit Exceeded. Lazy deletion with pruning guarantees logarithmic bounds.
- **Integer Division Truncation in Even Windows:** In languages like C++/Java, writing `(a + b) / 2` performs integer division (truncating $5 / 2 = 2$). Using `(a + b) / 2.0` or converting to double ensures correct floating-point medians ($2.5$).
- **Integer Overflow in Summation:** Summing two 32-bit integers $a + b$ can overflow if both are close to $2^{31} - 1$. Performing addition with 64-bit integers (`long long` or Python's arbitrary precision) prevents overflow.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Each of the $N$ numbers is inserted into a heap once: $O(\log K)$.
  - Each number is marked in the hash map once: $O(1)$.
  - Each number is popped from a heap during pruning at most once: $O(\log K)$.
  - Total Time: $\mathcal{O}(N \log K)$. For $N = 10^5$ and $K = 10^4$, $10^5 \times 14 \approx 1.4 \times 10^6$ operations, finishing in $< 120$ ms.
- **Auxiliary Space Complexity:**
  - The heaps and delayed hash map collectively store at most $O(N)$ elements. Total Space: $\mathcal{O}(N)$.
