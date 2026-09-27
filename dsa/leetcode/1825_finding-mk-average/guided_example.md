# Guided Example: Finding MK Average

We trace the step-by-step state management of a sliding window three-tier ordered partition on a representative stream of operations:

- **Input:**
  - Operations: `["MKAverage", "addElement", "addElement", "calculateMKAverage", "addElement", "calculateMKAverage", "addElement", "addElement", "addElement", "calculateMKAverage"]`
  - Arguments: `[[3, 1], [3], [1], [], [10], [], [5], [5], [5], []]`
- **Required Output:** `[null, null, null, -1, null, 3, null, null, null, 5]`

This instance demonstrates how maintaining three balanced ordered multisets ($\text{lo}$, $\text{mid}$, $\text{hi}$) enables $\mathcal{O}(\log m)$ stream updates and $\mathcal{O}(1)$ average queries without sorting the entire sliding window on each query.

---

## 1. Instance & Teaching Goal

We must design a data structure `MKAverage(m, k)` that maintains a stream of integers:
1. `addElement(num)`: Inserts a new number into the stream.
2. `calculateMKAverage()`:
   - If the stream contains fewer than $m$ numbers, returns $-1$.
   - Otherwise, takes the last $m$ numbers in the stream, removes the $k$ smallest numbers and the $k$ largest numbers, and computes the arithmetic average of the remaining $m - 2k$ numbers, rounded down to the nearest integer:
     $$\left\lfloor \frac{\sum \text{middle}}{m - 2k} \right\rfloor$$

In our instance:
- $m = 3, k = 1$. The sliding window has length $3$.
- Discard the smallest $k = 1$ element and largest $k = 1$ element, leaving $m - 2k = 3 - 2 = 1$ middle element.
- Initial calls:
  - Add $3 \implies$ stream has $1$ element ($< 3$).
  - Add $1 \implies$ stream has $2$ elements ($< 3$).
  - Query: returns $-1$ (insufficient elements).
  - Add $10 \implies$ stream has $3$ elements: $[3, 1, 10]$. Sorted: $[1, 3, 10]$. Discard $1$ and $10$; middle is $3$.
  - Query: returns $\lfloor 3 / 1 \rfloor = 3$.
  - Add $5 \implies$ window shifts to $[1, 10, 5]$. Sorted: $[1, 5, 10]$. Discard $1$ and $10$; middle is $5$.
  - Add $5 \implies$ window shifts to $[10, 5, 5]$. Sorted: $[5, 5, 10]$. Middle is $5$.
  - Add $5 \implies$ window shifts to $[5, 5, 5]$. Middle is $5$.
  - Query: returns $\lfloor 5 / 1 \rfloor = 5$.

The teaching goal is to avoid re-sorting the window on every query (which would cost $\mathcal{O}(m \log m)$ per query). Instead, we partition the $m$ active elements into three dynamic ordered collections ($\text{lo}$, $\text{mid}$, $\text{hi}$) and maintain the running sum of the $\text{mid}$ partition online.

---

## 2. Conceptual Foundation & Invariants

### The Tri-Partition Architecture

We maintain a FIFO queue of capacity $m$ to identify elements as they enter and expire, along with three ordered multisets:
1. **$\text{lo}$:** Holds the smallest $k$ elements in the active window. Target size: $|\text{lo}| = k$.
2. **$\text{hi}$:** Holds the largest $k$ elements in the active window. Target size: $|\text{hi}| = k$.
3. **$\text{mid}$:** Holds the remaining $m - 2k$ elements. Target size: $|\text{mid}| = m - 2k$.
4. **$S$:** Running scalar sum of all elements currently residing in $\text{mid}$:
   $$S = \sum_{x \in \text{mid}} x$$

### Three-Tier Balanced Multiset Invariant Theorem

> **Three-Tier Balanced Multiset Invariant Theorem.**
> At the end of every `addElement` call once the stream length reaches at least $m$:
> 1. **Cardinality Guarantees:** $|\text{lo}| = k$, $|\text{hi}| = k$, and $|\text{mid}| = m - 2k$.
> 2. **Boundary Ordering Invariant:**
>    $$\max(\text{lo}) \le \min(\text{mid}) \quad \text{and} \quad \max(\text{mid}) \le \min(\text{hi})$$
> 3. **Instantaneous Query Invariant:** Because $\text{mid}$ contains exactly the elements that remain after excluding the $k$ smallest and $k$ largest values, the MK Average is strictly:
>    $$\left\lfloor \frac{S}{m - 2k} \right\rfloor$$
>    evaluable in $\mathcal{O}(1)$ time.
> 4. When a new element arrives, it is placed in $\text{lo}$, $\text{mid}$, or $\text{hi}$ based on boundary comparisons. If the queue length exceeds $m$, the oldest element is removed from its respective multiset. Rebalancing shifts at most $\mathcal{O}(1)$ boundary elements between adjacent multisets, maintaining all invariants in $\mathcal{O}(\log m)$ time per insertion.

```mermaid
flowchart LR
    accTitle: Tri-Partition Balanced Multiset Structure
    accDescr: Diagram showing window elements divided into lo of size k, mid of size m-2k, and hi of size k, with running sum maintained on mid.
    subgraph Window ["Sliding Window of Last m Elements"]
        LO["lo: Smallest k elements (size = k)"]
        MID["mid: Middle elements (size = m - 2k, Sum = S)"]
        HI["hi: Largest k elements (size = k)"]
    end
    LO <=-=>|"Boundary Balance"| MID
    MID <=-=>|"Boundary Balance"| HI
    MID --> Query["Query: floor(S / (m - 2k)) in O(1)"]
```

---

## 3. Step-by-Step Worked Execution

We trace the full sequence of calls with $m = 3, k = 1$, where $m - 2k = 1$:

---

### Step 1: Initialization
- Execute `MKAverage(3, 1)`.
- Set $m = 3, k = 1$. Initialize empty queue $Q = []$, empty multisets $\text{lo} = \emptyset, \text{mid} = \emptyset, \text{hi} = \emptyset$, and sum $S = 0$.
- Emits: `null`.

---

### Step 2: `addElement(3)`
- Insert $3$ into $\text{lo}$ (as $\text{lo}$ is empty).
- Append $3 \to Q$.
- Current state: $Q = [3]$, $\text{lo} = \{3\}$, $\text{mid} = \emptyset$, $\text{hi} = \emptyset$, $S = 0$.
- Emits: `null`.

---

### Step 3: `addElement(1)`
- Compare $1$ with $\max(\text{lo}) = 3$: since $1 \le 3$, insert $1$ into $\text{lo} \implies \text{lo} = \{1, 3\}$.
- Append $1 \to Q$.
- Rebalance $\text{lo}$ size ($|\text{lo}| = 2 > k = 1$):
  - Pop largest element of $\text{lo}$ ($3$) and insert into $\text{mid}$.
  - Update sum: $S \to S + 3 = 3$.
- Current state: $Q = [3, 1]$, $\text{lo} = \{1\}$, $\text{mid} = \{3\}$, $\text{hi} = \emptyset$, $S = 3$.
- Emits: `null`.

---

### Step 4: `calculateMKAverage()`
- Check active window length: $|Q| = 2 < m = 3$.
- Insufficient elements.
- Emits: **`-1`**.

---

### Step 5: `addElement(10)`
- Compare $10$: since $\text{hi}$ is empty and $10 > \max(\text{lo}) = 1$, insert $10$ into $\text{hi}$.
- Append $10 \to Q$.
- Window length $|Q| = 3 == m$.
- Multisets: $\text{lo} = \{1\}$, $\text{mid} = \{3\}$, $\text{hi} = \{10\}$.
- Cardinalities: $|\text{lo}| = 1 = k$, $|\text{mid}| = 1 = m - 2k$, $|\text{hi}| = 1 = k$. Invariants hold!
- Sum $S = 3$.
- Emits: `null`.

---

### Step 6: `calculateMKAverage()`
- Window length $|Q| = 3 \ge m$.
- Compute average from $\text{mid}$:
  $$\left\lfloor \frac{S}{m - 2k} \right\rfloor = \left\lfloor \frac{3}{1} \right\rfloor = 3$$
- Emits: **`3`**.

---

### Step 7: `addElement(5)`
- Stream queue exceeds $m = 3$: pop oldest element $x = Q[0] = 3$.
  - $3 \in \text{mid}$. Remove $3$ from $\text{mid}$.
  - Update sum: $S \to S - 3 = 0$.
- Insert new element $5$:
  - Compare $5$: $1 < 5 < 10 \implies$ insert into $\text{mid}$.
  - Update sum: $S \to S + 5 = 5$.
- Current state: $Q = [1, 10, 5]$, $\text{lo} = \{1\}$, $\text{mid} = \{5\}$, $\text{hi} = \{10\}$, $S = 5$.
- Emits: `null`.

---

### Step 8: `addElement(5)`
- Pop oldest element $x = Q[0] = 1$.
  - $1 \in \text{lo}$. Remove $1$ from $\text{lo} \implies \text{lo} = \emptyset$.
- Insert new element $5$:
  - Insert into $\text{mid} \implies \text{mid} = \{5, 5\}$, $S = 5 + 5 = 10$.
- Rebalance: $|\text{lo}| = 0 < k = 1$.
  - Pop smallest element from $\text{mid}$ ($5$) and insert into $\text{lo}$.
  - Update sum: $S \to S - 5 = 5$.
- Current state: $Q = [10, 5, 5]$, $\text{lo} = \{5\}$, $\text{mid} = \{5\}$, $\text{hi} = \{10\}$, $S = 5$.
- Emits: `null`.

---

### Step 9: `addElement(5)`
- Pop oldest element $x = Q[0] = 10$.
  - $10 \in \text{hi}$. Remove $10$ from $\text{hi} \implies \text{hi} = \emptyset$.
- Insert new element $5$:
  - Insert into $\text{mid} \implies \text{mid} = \{5, 5\}$, $S = 5 + 5 = 10$.
- Rebalance: $|\text{hi}| = 0 < k = 1$.
  - Pop largest element from $\text{mid}$ ($5$) and insert into $\text{hi}$.
  - Update sum: $S \to S - 5 = 5$.
- Current state: $Q = [5, 5, 5]$, $\text{lo} = \{5\}$, $\text{mid} = \{5\}$, $\text{hi} = \{5\}$, $S = 5$.
- Emits: `null`.

---

### Step 10: `calculateMKAverage()`
- Window length $|Q| = 3 \ge m$.
- Compute average:
  $$\left\lfloor \frac{S}{m - 2k} \right\rfloor = \left\lfloor \frac{5}{1} \right\rfloor = 5$$
- Emits: **`5`**.

---

## 4. Complete Execution Trace

| Op # | Method Invocation | Argument | Window Queue $Q$ | $\text{lo}$ ($k = 1$) | $\text{mid}$ ($m - 2k = 1$) | $\text{hi}$ ($k = 1$) | Running Sum $S$ | Output |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | `MKAverage` | `[3, 1]` | `[]` | $\emptyset$ | $\emptyset$ | $\emptyset$ | $0$ | `null` |
| $2$ | `addElement` | `3` | `[3]` | $\{3\}$ | $\emptyset$ | $\emptyset$ | $0$ | `null` |
| $3$ | `addElement` | `1` | `[3, 1]` | $\{1\}$ | $\{3\}$ | $\emptyset$ | $3$ | `null` |
| $4$ | `calculateMKAverage` | `[]` | `[3, 1]` | $\{1\}$ | $\{3\}$ | $\emptyset$ | $3$ | **`-1`** |
| $5$ | `addElement` | `10` | `[3, 1, 10]` | $\{1\}$ | $\{3\}$ | $\{10\}$ | $3$ | `null` |
| $6$ | `calculateMKAverage` | `[]` | `[3, 1, 10]` | $\{1\}$ | $\{3\}$ | $\{10\}$ | $3$ | **`3`** |
| $7$ | `addElement` | `5` | `[1, 10, 5]` | $\{1\}$ | $\{5\}$ | $\{10\}$ | $5$ | `null` |
| $8$ | `addElement` | `5` | `[10, 5, 5]` | $\{5\}$ | $\{5\}$ | $\{10\}$ | $5$ | `null` |
| $9$ | `addElement` | `5` | `[5, 5, 5]` | $\{5\}$ | $\{5\}$ | $\{5\}$ | $5$ | `null` |
| $10$ | `calculateMKAverage` | `[]` | `[5, 5, 5]` | $\{5\}$ | $\{5\}$ | $\{5\}$ | $5$ | **`5`** |

Sequence of results: `[null, null, null, -1, null, 3, null, null, null, 5]`.

---

## 5. Algorithmic Correctness

**Soundness.** Because the queue enforces strict FIFO sliding window semantics, the multisets always contain exactly the last $m$ elements. Maintaining $\max(\text{lo}) \le \min(\text{mid}) \le \max(\text{mid}) \le \min(\text{hi})$ guarantees that the $k$ smallest and $k$ largest elements are segregated into $\text{lo}$ and $\text{hi}$, ensuring that $\text{mid}$ contains precisely the remaining $m - 2k$ elements. Thus, $\lfloor S / (m - 2k) \rfloor$ computes the exact required mathematical average.

**Completeness.** Every insertion and eviction triggers local rebalancing to maintain target sizes. Because an insertion adds $1$ element and eviction removes $1$ element, at most one boundary migration between adjacent multisets is ever required per update, ensuring invariants hold at all times.

---

## 6. Traps This Instance Exposes

- **Duplicate Values Across Multisets:** Multiple identical values can span across $\text{lo}$, $\text{mid}$, and $\text{hi}$ (as in Step 9 where $5$ appears in all three). Multisets (frequency-aware ordered lists or balanced BSTs) must distinguish duplicate elements and delete only one instance of an evicted value.
- **Integer Division vs. Floating Point:** The problem specifies integer truncation ($\lfloor \cdot \rfloor$), not round-to-nearest.
- **Window Initialization Guard:** Calling `calculateMKAverage` before $m$ elements have been added must return $-1$ immediately.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - `addElement`: $\mathcal{O}(\log m)$. Inserting into and removing from an ordered list or balanced BST takes $\mathcal{O}(\log m)$ time. Rebalancing shifts at most $\mathcal{O}(1)$ elements, each costing $\mathcal{O}(\log m)$.
  - `calculateMKAverage`: $\mathcal{O}(1)$. The sum $S$ is tracked incrementally, so computing the average requires a single integer division.
- **Auxiliary Space Complexity:** $\mathcal{O}(m)$ to store the $m$ active elements in the queue and the three ordered multisets.
