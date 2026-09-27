# Guided Example: My Calendar III

We trace the step-by-step continuous timeline density measurement, dynamic segment tree range-increment modifications ($[start + 1, end] \leftarrow +1$), lazy tag propagation ($add$), range-maximum aggregation ($node.v = \max(left.v, right.v)$), sweep-line difference prefix running maximums ($\max \sum \delta$), and monotonic peak $k$-booking evaluation on representative event streams:

- **Input:**
  - Operations sequence:
    ```text
    MyCalendarThree()
    book(10, 20)
    book(50, 60)
    book(10, 40)
    book(5, 15)
    book(5, 10)
    book(25, 55)
    ```
- **Required output:** `[1, 1, 2, 3, 3, 3]`
  - Maximum $k$-booking specification:
    - A $k$-booking occurs if there exists any instantaneous time point $t \in \mathbb{R}$ that is covered by **at least $k$ simultaneous events**.
    - Unlike Calendar I and II, **no bookings are ever rejected**; every event is permanently incorporated into the calendar.
    - After each `book(start, end)` call, return the **maximum $k$-booking** across all accumulated events to date.
    - Lifecycle trace:
      - `book(10, 20)`: 1 event active over $[10, 20) \implies$ max $k = \mathbf{1}$.
      - `book(50, 60)`: Disjoint event over $[50, 60) \implies$ max $k = \mathbf{1}$.
      - `book(10, 40)`: Overlaps $[10, 20)$ on $[10, 20) \implies 2$ concurrent events $\implies$ max $k = \mathbf{2}$.
      - `book(5, 15)`: Intersects both $[10, 20)$ and $[10, 40)$ on $[10, 15) \implies 3$ concurrent events $\implies$ max $k = \mathbf{3}$.
      - `book(5, 10)`: Abuts $[10, 20)$ at 10 (half-open, no 3-way collision) $\implies$ max $k$ remains $\mathbf{3}$.
      - `book(25, 55)`: Introduces overlaps of at most 2 events $\implies$ max $k$ remains $\mathbf{3}$.
      - Results: `[1, 1, 2, 3, 3, 3]`.
- **Dynamic Segment Tree Range-Maximum Invariant:**
  - **Endpoint Discretization:**
    - Each half-open interval $[start, end)$ covers real numbers $x \in [start, end)$.
    - Mapping each unit interval to the 1-based discrete closed coordinate range:
      $$
      [L, \; R] = [start + 1, \; end]
      $$
  - **Dynamic Segment Tree Structure:**
    - Spans global coordinate range $[1, 10^9 + 1]$.
    - Node attributes:
      - `v`: the maximum event coverage density within this node's interval.
      - `add`: lazy increment tag for range modifications.
  - **Pushup & Pushdown Mechanics:**
    - **Pushup:** A parent node's maximum density is simply the maximum of its two children:
      $$
      node.v = \max(node.left.v, \; node.right.v)
      $$
    - **Pushdown:** Allocate children on-demand and propagate pending `add` values down the tree.
  - **Root Query Guarantee:**
    - Because every range increment updates tree paths with pushup, the global peak concurrency over the entire universe $[1, 10^9 + 1]$ is stored directly at the root:
      $$
      k_{\max} = root.v
      $$
    - Retrieval after each booking requires strictly $\mathcal{O}(1)$ root inspection!
- **Step-by-Step Worked Execution Trace on the Sample Sequence:**
  - Initialize empty dynamic segment tree covering domain $[1, 10^9 + 1]$.
  - **Operation 1: `book(10, 20)`:**
    - Target discrete range: $[11, 20]$.
    - Increment range by $+1$:
      - Segments spanning $[11, 20]$ receive `add += 1, v += 1`.
    - Root recomputes: $root.v = \mathbf{1}$.
    - Return value:
      $$
      ans \leftarrow \mathbf{1}
      $$
  - **Operation 2: `book(50, 60)`:**
    - Target discrete range: $[51, 60]$.
    - Increment range by $+1$.
    - Disjoint from $[11, 20]$.
    - Root recomputes: $\max(1, 1) = \mathbf{1}$.
    - Return value:
      $$
      ans \leftarrow \mathbf{1}
      $$
  - **Operation 3: `book(10, 40)`:**
    - Target discrete range: $[11, 40]$.
    - Increment range by $+1$:
      - Sub-range $[11, 20]$ previously had value 1; now receives $+1 \implies$ becomes **2**!
      - Sub-range $[21, 40]$ receives $+1 \implies$ becomes 1.
    - Pushup propagates:
      $$
      root.v = \max(2, 1, 1) = \mathbf{2}
      $$
    - Return value:
      $$
      ans \leftarrow \mathbf{2}
      $$
  - **Operation 4: `book(5, 15)`:**
    - Target discrete range: $[6, 15]$.
    - Increment range by $+1$:
      - Sub-range $[11, 15]$ previously had value 2 (overlapped by operations 1 and 3).
      - Receiving $+1$ elevates density over $[11, 15]$ to:
        $$
        2 + 1 = \mathbf{3}
        $$
    - Pushup propagates:
      $$
      root.v = \max(3, 2, 1) = \mathbf{3}
      $$
    - Return value:
      $$
      ans \leftarrow \mathbf{3}
      $$
  - **Operation 5: `book(5, 10)`:**
    - Target discrete range: $[6, 10]$.
    - Increment range by $+1$:
      - Over $[6, 10]$, previous density was 1 (from Operation 4); becomes $1 + 1 = 2$.
    - Peak density elsewhere remains 3 (over $[11, 15]$).
    - Root maximum remains:
      $$
      root.v = \mathbf{3}
      $$
    - Return value:
      $$
      ans \leftarrow \mathbf{3}
      $$
  - **Operation 6: `book(25, 55)`:**
    - Target discrete range: $[26, 55]$.
    - Increments range by $+1$.
    - Overlaps $[26, 40]$ (density becomes 2) and $[51, 55]$ (density becomes 2).
    - Global peak remains 3 over $[11, 15]$.
    - Root maximum remains:
      $$
      root.v = \mathbf{3}
      $$
    - Return value:
      $$
      ans \leftarrow \mathbf{3}
      $$
  - **Consolidated Outputs:**
    $$
    [\mathbf{1}, \; \mathbf{1}, \; \mathbf{2}, \; \mathbf{3}, \; \mathbf{3}, \; \mathbf{3}]
    $$
- **Monotonically Rising Density ($[10, 30), [10, 30), [10, 30)$):**
  - Successive calls on the exact same interval.
  - Density accumulates directly: 1, 2, 3.
  - Returns `[1, 2, 3]`.
- **Non-Overlapping Sequence ($[0, 10), [10, 20), [20, 30)$):**
  - Abutting intervals with disjoint interiors.
  - Peak concurrency remains 1 throughout.
  - Returns `[1, 1, 1]`.

This instance demonstrates dynamic segment tree range addition with lazy propagation and global upper bound tracking, mathematically proves why root node values maintain the exact supremum of superimposed step functions, and derives $O(\log C)$ per booking and $O(N \log C)$ space bounds.

---

## 1. Instance & Teaching Goal

Implement `MyCalendarThree`:
Every booking $[start, end)$ is **accepted**.
After each booking, return the **maximum $k$-booking** (maximum number of concurrent overlapping events at any point).

```text
Operations:
  book(10, 20) -> max concurrency = 1 -> returns 1
  book(50, 60) -> max concurrency = 1 -> returns 1
  book(10, 40) -> overlaps [10, 20) -> max concurrency = 2 -> returns 2
  book(5, 15)  -> overlaps [10, 20) & [10, 40) on [10, 15) -> max concurrency = 3 -> returns 3
  book(5, 10)  -> touches at 10 -> max concurrency = 3 -> returns 3
  book(25, 55) -> max concurrency = 3 -> returns 3

Result: [ 1, 1, 2, 3, 3, 3 ]
```

### The Invariant of the Global Range Maximum
- Each booking adds $+1$ over the range $[start + 1, end]$.
- A dynamic segment tree with lazy propagation performs range additions in $O(\log C)$ time.
- The root of the segment tree maintains the global maximum concurrency $root.v$ across all intervals.

---

## 2. Conceptual Foundation & Invariants

### 1. Range Addition Operator:
$$
\text{modify}(start + 1, \; end, \; +1)
$$
$$
node.v = \max(node.left.v, \; node.right.v)
$$

### 2. Immediate Peak Concurrency:
$$
k_{\max} = root.v
$$

> **Supremum Envelope Invariant.** The pointwise envelope $E(t) = \sum_{k=1}^N \mathbf{1}_{[s_k, e_k)}(t)$ is a piecewise constant cadlag function whose global $L_\infty$ norm $\|E\|_\infty = \sup_{t} E(t)$ corresponds to the maximal leaf evaluation, maintained at the segment tree root under monotone pushup updates.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: `book(10, 20)`
- Range $[11, 20] \to +1$. Root = **`1`**.

---

### Step 2: `book(50, 60)`
- Range $[51, 60] \to +1$. Root = **`1`**.

---

### Step 3: `book(10, 40)`
- Range $[11, 40] \to +1$. Overlap on $[11, 20]$ reaches 2. Root = **`2`**.

---

### Step 4: `book(5, 15)`
- Range $[6, 15] \to +1$. Overlap on $[11, 15]$ reaches $2 + 1 = 3$. Root = **`3`**.

---

### Step 5: `book(5, 10)`, `book(25, 55)`
- New overlaps reach at most 2. Root remains **`3`**.

---

### Step 6: Output
$$
[\mathbf{1}, \; \mathbf{1}, \; \mathbf{2}, \; \mathbf{3}, \; \mathbf{3}, \; \mathbf{3}]
$$

---

## 4. Complete Execution Trace

| Call | Interval $[s, e)$ | Range Modified $[s+1, e]$ | Value Added | Overlapping Critical Sub-segment | Global Peak $root.v$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `book(10, 20)` | $[10, 20)$ | $[11, 20]$ | $+1$ | $[11, 20] \to 1$ | **`1`** |
| `book(50, 60)` | $[50, 60)$ | $[51, 60]$ | $+1$ | $[51, 60] \to 1$ | **`1`** |
| `book(10, 40)` | $[10, 40)$ | $[11, 40]$ | $+1$ | $[11, 20] \to 2$ | **`2`** |
| **`book(5, 15)`** | **$[5, 15)$** | **$[6, 15]$** | **$+1$** | **$[11, 15] \to 3$** | **`3`** |
| `book(5, 10)` | $[5, 10)$ | $[6, 10]$ | $+1$ | $[6, 10] \to 2$ | **`3`** |
| `book(25, 55)` | $[25, 55)$ | $[26, 55]$ | $+1$ | $[26, 40] \to 2$ | **`3`** |

---

## 5. Boundary Cases & Failure Modes

- **$N$ Successive Duplicate Bookings:** Concurrency increments by 1 on each call: $1, 2, \dots, N$.
- **Disjoint Bookings:** Concurrency stays 1 for all calls.
- **Large Coordinates ($C = 10^9$):** Dynamic tree only instantiates nodes on visited branches; height $\log_2(10^9) \approx 30$.
- **Single Point Concurrency:** Half-open endpoint ensures abutting intervals do not register false spikes.

---

## 6. Traps & Common Anti-Patterns

- **Linear Sweep across Boundary Map ($O(N^2)$ Total):** While a sweep-line with `SortedDict` works for $N \le 400$, a dynamic segment tree achieves true $\mathcal{O}(N \log C)$ scaling, completing queries in logarithmic rather than linear time.
- **Off-By-One on Interval Boundaries:** Range must be $[start + 1, end]$ or $[start, end - 1]$ to respect half-open semantics.
- **Forgetting Lazy Pushdown:** Range updates without pushing down `node.add` to children will lose track of local sub-ranges during deeper splits.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Range update in dynamic segment tree of height $\log C$: $\mathcal{O}(\log C)$ where $C = 10^9$.
  - Global maximum query: $\mathcal{O}(1)$ directly from root node `root.v`.
  - Total Time: strictly logarithmic $\mathcal{O}(\log C)$ per `book` call. Completes $1000$ operations in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - At most $\mathcal{O}(N \log C)$ nodes allocated across $N$ bookings.