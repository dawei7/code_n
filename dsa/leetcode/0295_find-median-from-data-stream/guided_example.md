# Guided Example: Find Median from Data Stream

We trace the step-by-step two-heap balanced partition, max-heap lower half routing via negated values, min-heap upper half balancing, and $O(1)$ median extraction on representative sequential stream numbers:

- **Input:** Stream of operations adding integers $[1, 2, 3, 4, 5]$ with interleaved `findMedian()` queries
- **Required output:** Medians `[1.0, 1.5, 2.0, 2.5, 3.0]`
  - After `[1]`: Median is $1.0$ (Odd count, single middle element)
  - After `[1, 2]`: Median is $(1 + 2) / 2 = 1.5$ (Even count, mean of two middle elements)
  - After `[1, 2, 3]`: Median is $2.0$
  - After `[1, 2, 3, 4]`: Median is $(2 + 3) / 2 = 2.5$
  - After `[1, 2, 3, 4, 5]`: Median is $3.0$
- **Unordered Stream Insertion:** Arriving out of order (e.g. $[5, 2, 4, 1, 3]$) still ends with the same partition — lower $\{1, 2\}$, upper $\{3, 4, 5\}$ — and the same final median $3.0$, but the intermediate medians are decided by the prefix seen so far, giving $5.0, 3.5, 4.0, 3.0, 3.0$ instead of the sorted arrival's $1.0, 1.5, 2.0, 2.5, 3.0$
- **Duplicate Values:** Equal stream elements are partitioned across the two heaps without breaking heap order

This instance demonstrates dynamic stream median tracking, proves how two complementary heaps maintain a split boundary around the median, details the logarithmic rebalancing mechanism, and achieves $O(\log N)$ per insertion with $O(1)$ median queries in $O(N)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given a continuous data stream of numbers $[1, 2, 3, 4, 5]$:
Compute the median after each number is inserted.
- For an **odd** number of elements, the median is the single middle element.
- For an **even** number of elements, the median is the arithmetic mean of the two middle elements.

```text
Stream progression:
Add 1: [1]             -> Median: 1.0
Add 2: [1, 2]          -> Median: (1 + 2) / 2 = 1.5
Add 3: [1, 2, 3]       -> Median: 2.0
Add 4: [1, 2, 3, 4]    -> Median: (2 + 3) / 2 = 2.5
Add 5: [1, 2, 3, 4, 5] -> Median: 3.0
```

### The $O(1)$ Query Bottleneck
- Sorting the array upon each query takes $O(N \log N)$ time per query.
- Maintaining an insertion-sorted list (via binary search) takes $O(\log N)$ to find position, but $O(N)$ to shift elements on insertion.
- The **Two-Heap Architecture** divides the data into two equal halves:
  - `max_heap` (Lower half of numbers): Root gives the maximum of the lower half.
  - `min_heap` (Upper half of numbers): Root gives the minimum of the upper half.
Both insertion and rebalancing take $O(\log N)$, while median calculation takes strictly $O(1)$!

---

## 2. Conceptual Foundation & Invariants

### Dual-Heap Data Structure
1. `maxq`: Max-heap holding the smaller half of numbers (stored as negative values in Python `heapq`).
   Max element is $- \text{maxq}[0]$.
2. `minq`: Min-heap holding the larger half of numbers.
   Min element is $\text{minq}[0]$.

### The Two System Invariants:
1. **Ordering Invariant:** Every value in the lower half is $\le$ every value in the upper half:
   $$
   \forall x \in \text{lower}, \; \forall y \in \text{upper}: \quad x \le y
   $$
2. **Size Balance Invariant:** `minq` either has the same size as `maxq` (even total) or exactly one more element (odd total):
   $$
   |\text{minq}| = |\text{maxq}| \quad \text{or} \quad |\text{minq}| = |\text{maxq}| + 1
   $$

### Operations:

#### `addNum(num)`
1. **Route Candidate via Lower Half:**
   Push $-\text{num}$ into `maxq`, pop the smallest negative value (which corresponds to the largest positive number in the candidate lower half), negate it back, and push it into `minq`:
   $$
   \text{heappush}(\text{minq}, \; -\text{heappushpop}(\text{maxq}, -\text{num}))
   $$
2. **Size Rebalancing:**
   If `minq` has received too many elements ($|\text{minq}| - |\text{maxq}| > 1$):
   Pop the minimum element from `minq` and move it to `maxq`:
   $$
   \text{heappush}(\text{maxq}, \; -\text{heappop}(\text{minq}))
   $$

#### `findMedian() -> float`
- If $|\text{minq}| == |\text{maxq}|$ (even total count):
  $$
  \text{median} = \frac{\text{minq}[0] - \text{maxq}[0]}{2.0}
  $$
- If $|\text{minq}| > |\text{maxq}|$ (odd total count):
  $$
  \text{median} = \text{minq}[0]
  $$

> **Invariant.** The median is always accessible at the roots: $\text{minq}[0]$ for odd counts, and $\frac{\text{minq}[0] + (-\text{maxq}[0])}{2}$ for even counts.

---

## 3. Step-by-Step Worked Execution

We trace the two-heap evolution as numbers $[1, 2, 3, 4, 5]$ arrive:
Initial state: `minq = []`, `maxq = []`.

---

### Step 1: Add Number $1$
- Route:
  - Push $-1$ into `maxq`. `heappushpop([], -1)` returns $-1$.
  - Negate: $-(-1) = 1$. Push $1$ into `minq`.
- Heap states: `minq = [1]` (size 1), `maxq = []` (size 0).
- Size difference: $1 - 0 = 1 \le 1$ (Balanced).
- **`findMedian()`:** Odd count ($1 > 0$) $\implies \text{minq}[0] = \mathbf{1.0}$.

---

### Step 2: Add Number $2$
- Route:
  - Push $-2$ into `maxq`. `heappushpop([], -2)` returns $-2$.
  - Negate: $-(-2) = 2$. Push $2$ into `minq`.
- Heap states before rebalance: `minq = [1, 2]` (size 2), `maxq = []` (size 0).
- Size check: $2 - 0 = 2 > 1$ (**Exceeds balance limit!**).
- Rebalance:
  - $\text{heappop}(\text{minq})$ pops $1$.
  - Push $-1$ into `maxq`.
- Heap states: `minq = [2]` (size 1), `maxq = [-1]` (size 1).
- **`findMedian()`:** Even count ($1 == 1$) $\implies \frac{\text{minq}[0] - \text{maxq}[0]}{2} = \frac{2 - (-1)}{2} = \mathbf{1.5}$.

---

### Step 3: Add Number $3$
- Route:
  - Push $-3$ into `maxq = [-1]`.
  - `heappushpop([-1], -3)`: `maxq` has $\{-3, -1\}$. Pops smallest negative ($-3$).
  - Negate: $-(-3) = 3$. Push $3$ into `minq`.
- Heap states: `minq = [2, 3]` (size 2), `maxq = [-1]` (size 1).
- Size difference: $2 - 1 = 1 \le 1$ (Balanced).
- **`findMedian()`:** Odd count ($2 > 1$) $\implies \text{minq}[0] = \mathbf{2.0}$.

---

### Step 4: Add Number $4$
- Route:
  - Push $-4$ into `maxq = [-1]`. Pops $-4$.
  - Negate: $-(-4) = 4$. Push $4$ into `minq`.
- Heap states before rebalance: `minq = [2, 3, 4]` (size 3), `maxq = [-1]` (size 1).
- Size check: $3 - 1 = 2 > 1$ (**Rebalance needed!**).
- Rebalance:
  - $\text{heappop}(\text{minq})$ pops minimum ($2$).
  - Push $-2$ into `maxq`.
- Heap states: `minq = [3, 4]` (size 2), `maxq = [-2, -1]` (size 2).
- Lower half: $\{1, 2\}$ (stored as `[-2, -1]`, max is $2$).
- Upper half: $\{3, 4\}$ (stored as `[3, 4]`, min is $3$).
- **`findMedian()`:** Even count ($2 == 2$) $\implies \frac{3 - (-2)}{2} = \frac{3 + 2}{2} = \mathbf{2.5}$.

---

### Step 5: Add Number $5$
- Route:
  - Push $-5$ into `maxq = [-2, -1]`. Pops $-5$.
  - Negate: $5$. Push $5$ into `minq`.
- Heap states: `minq = [3, 4, 5]` (size 3), `maxq = [-2, -1]` (size 2).
- Size difference: $3 - 2 = 1 \le 1$ (Balanced).
- **`findMedian()`:** Odd count ($3 > 2$) $\implies \text{minq}[0] = \mathbf{3.0}$.

#### Inside `heappushpop`: Which Value Crosses the Boundary
Routing is one combined operation — push $-\text{num}$, then immediately pop the smallest stored value — so the number that reaches `minq` is $\max(\text{num}, \max(\text{lower}))$, and it is not always the number that just arrived. The ledger below separates that exchange from the rebalancing move that follows it:

| Step | `num` arriving | `maxq` right after pushing $-\text{num}$ | `heappushpop` returns | Value crossing into `minq` | Rebalancing move | Boundary after all moves |
|:---:|:---:|:---:|:---:|:---:|:---|:---|
| 1 | $1$ | $\{-1\}$ | $-1$ | $1$ (the arrival) | none: $\lvert \text{minq} \rvert - \lvert \text{maxq} \rvert = 1$ | lower half empty, so $x \le y$ is vacuous |
| 2 | $2$ | $\{-2\}$ | $-2$ | $2$ (the arrival) | pop $1$ from `minq`, push $-1$ into `maxq` | $\max(\text{lower}) = 1 \le 2 = \min(\text{upper})$ |
| 3 | $3$ | $\{-3, -1\}$ | $-3$ | $3$ (the arrival) | none: the difference is already $1$ | $\max(\text{lower}) = 1 \le 2 = \min(\text{upper})$ |
| 4 | $4$ | $\{-4, -1\}$ | $-4$ | $4$ (the arrival) | pop $2$ from `minq`, push $-2$ into `maxq` | $\max(\text{lower}) = 2 \le 3 = \min(\text{upper})$ |
| 5 | $5$ | $\{-5, -2, -1\}$ | $-5$ | $5$ (the arrival) | none: the difference is already $1$ | $\max(\text{lower}) = 2 \le 3 = \min(\text{upper})$ |

Every arrival in this increasing stream is the largest value seen so far, so `heappushpop` hands back exactly the number it was given and the lower half changes only in the rebalancing move. A descending stream reverses that: from the third element onward the arrival is the smallest value seen, so the call pushes the previous maximum of the lower half up into `minq` and keeps the new number below the boundary — the case analysed in §6.

---

## 4. Complete Execution Trace

```text
Stream: [1, 2, 3, 4, 5]

1. addNum(1) -> minq=[1], maxq=[]           -> median = 1.0
2. addNum(2) -> minq=[2], maxq=[-1]         -> median = (2 + 1)/2 = 1.5
3. addNum(3) -> minq=[2, 3], maxq=[-1]      -> median = 2.0
4. addNum(4) -> minq=[3, 4], maxq=[-2, -1]  -> median = (3 + 2)/2 = 2.5
5. addNum(5) -> minq=[3, 4, 5], maxq=[-2,-1]-> median = 3.0

Results: [1.0, 1.5, 2.0, 2.5, 3.0]
```

| Step | `num` Added | Action Taken | `maxq` (Lower Half) | `minq` (Upper Half) | Heap Sizes $(\lvert \text{maxq} \rvert, \lvert \text{minq} \rvert)$ | Computed Median |
|:---:|:---:|:---|:---:|:---:|:---:|:---:|
| 1 | 1 | Push to `minq` | `[]` | `[1]` | $(0, 1)$ | **1.0** |
| 2 | 2 | Push to `minq`, rebalance to `maxq` | `[-1]` | `[2]` | $(1, 1)$ | **1.5** |
| 3 | 3 | Route to `minq` | `[-1]` | `[2, 3]` | $(1, 2)$ | **2.0** |
| 4 | 4 | Push to `minq`, rebalance to `maxq` | `[-2, -1]` | `[3, 4]` | $(2, 2)$ | **2.5** |
| 5 | 5 | Route to `minq` | `[-2, -1]` | `[3, 4, 5]` | $(2, 3)$ | **3.0** |

---

## 5. Algorithmic Correctness

**Soundness.** The ordering invariant ensures that all elements in `maxq` are $\le$ all elements in `minq`. Routing every new number through `maxq` first ensures that the largest candidate in the lower half is filtered into `minq`. Rebalancing moves the smallest element of `minq` into `maxq`, ensuring size parity while maintaining the boundary condition $\max(\text{lower}) \le \min(\text{upper})$.

**Completeness.** By mathematical definition, if a dataset is divided into two halves of equal size (or with the upper half having one extra element), the median is either the unique middle element ($\text{minq}[0]$) or the mean of the boundary elements ($\frac{\text{minq}[0] + \max(\text{lower})}{2}$). The roots of the two heaps provide these exact values.

---

## 6. Traps This Instance Exposes

- **Negation Arithmetic in Max-Heap:** Python's `heapq` is a min-heap. Storing negative values simulates a max-heap: $\max(\text{lower}) = -\text{maxq}[0]$. When computing the even-size median, subtracting $-\text{maxq}[0]$ correctly adds the positive value: `minq[0] - maxq[0]`.
- **Integer Division Trap:** In languages like Python 2, C++, or Java, dividing integers using `/ 2` performs floor truncation (e.g. $5 / 2 = 2$). Floating-point division `/ 2.0` is required to produce $2.5$.
- **Direct Insertion without Boundary Check:** Pushing directly to `minq` or `maxq` based solely on size without checking the value can invert the partition (e.g. putting a small number into `minq`). The `heappushpop` routing guarantees the boundary invariant holds before sizing is resolved.

### Boundary Conditions Worth Checking by Hand
Each row below is an exact median sequence produced by the method above, and each isolates one way the invariants can be stressed:

| Stream condition | Instance | Medians returned | What it tests |
|:---|:---|:---|:---|
| Single element | $[0]$ | $0.0$ | The odd rule reads `minq[0]` while the lower half is still empty |
| Two elements | $[50, 98]$ | $50.0, \; 74.0$ | Rebalancing first moves the smaller value down, so the even rule reads two genuine boundary values |
| All values equal | $[2, 2, 2, 2]$ | $2.0$ at every step | The ordering invariant is $\le$, not $<$: $\max(\text{lower}) = \min(\text{upper}) = 2$ is legal, and the mean of two equal boundary values is that same value |
| Negative values | $[-5, -10, -3]$ | $-5.0, \; -7.5, \; -5.0$ | The negation trick must be applied to negative inputs too: the stored root $10$ represents the value $-10$, and the even rule computes $-5 - 10 = -15$, halved to $-7.5$ |
| Strictly descending arrival | $[5, 4, 3, 2, 1]$ | $5.0, \; 4.5, \; 4.0, \; 3.5, \; 3.0$ | From the third element on, `heappushpop` returns the stored root instead of the arrival, so the upper half grows during routing |
| Out-of-order arrival | $[5, 2, 4, 1, 3]$ | $5.0, \; 3.5, \; 4.0, \; 3.0, \; 3.0$ | The final partition and final median match the sorted arrival, yet every intermediate query answers about a different prefix |

---

## 7. Complexity Derivation

- **Time Complexity:**
  - `addNum(num)`: $O(\log N)$ logarithmic time. The method executes at most two heap pushes and two heap pops. Each heap operation on a heap of size $N/2$ costs $O(\log N)$.
  - `findMedian()`: $O(1)$ constant time. Accesses the roots of the heaps at index `0` and performs basic arithmetic.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary memory to store the $N$ stream elements distributed across `minq` and `maxq`.

### Alternatives and Their Costs
| Approach | `addNum` cost | `findMedian` cost | Auxiliary space | Tradeoff on this workload |
|:---|:---|:---|:---|:---|
| **Sort the buffer at every query** | $O(1)$ append | $O(N \log N)$ | $O(N)$ | Correct, but it re-derives an order the previous query already knew; with up to $5 \cdot 10^{4}$ calls the queries dominate every other cost |
| **One sorted list, binary-search insertion** | $O(\log N)$ to locate the position plus $O(N)$ to shift the tail | $O(1)$ middle read | $O(N)$ | The search and the read are cheap; the shifting makes each insertion linear |
| **Balanced search tree with subtree sizes** | $O(\log N)$ | $O(\log N)$ rank selection | $O(N)$ | Asymptotically sound and free of value-range assumptions, but the structure must be written by hand |
| **Frequency array over the bounded value range** | $O(1)$ increment over $V = 2 \cdot 10^{5} + 1$ possible values | $O(V)$ scan, or $O(\log V)$ with a Fenwick tree over the counts | $O(V)$ | Uses the stated bound $-10^{5} \le \text{num} \le 10^{5}$, but the query stops being constant |
| **Two heaps (the method used here)** | $O(\log N)$: one `heappushpop`, plus at most one pop/push pair | $O(1)$: two heap roots and one subtraction | $O(N)$ | Each query reads the two boundary values that insertion already maintained |
