# Guided Example: Employee Free Time

We trace the step-by-step multi-employee busy schedule flattening, chronological interval sorting by start time ($x.start$), union interval coalescing ($merged[-1].end \ge x.start$), inter-block finite gap extraction ($[a.end, b.start]$), infinite boundary truncation, and sorted common free-time interval generation on representative workforce schedules:

- **Input:**
  $$
  schedule = [[[1, 2], [5, 6]], \; [[1, 3]], \; [[4, 10]]]
  $$
- **Required output:**
  $$
  [[3, 4]]
  $$
  - Workforce free time criteria:
    - Each employee has a list of sorted, non-overlapping working intervals $[start, end]$.
    - A time period is **common free time** if and only if **no employee is working** during that entire period.
    - The output must contain only **finite** intervals with positive length ($start < end$). Infinite intervals like $(-\infty, 1)$ or $(10, \infty)$ are ignored.
    - For the input schedule:
      - Employee 0 works: $[1, 2]$ and $[5, 6]$.
      - Employee 1 works: $[1, 3]$.
      - Employee 2 works: $[4, 10]$.
      - Merging all work shifts:
        - Block 1: $[1, 3]$ (covered by Employee 0 and Employee 1).
        - Block 2: $[4, 10]$ (covered by Employee 2 and Employee 0).
      - Between time $3$ and time $4$, no employee is on duty!
      - Common free time: $[3, 4]$.
- **Interval Union & Complement Gap Invariant:**
  - **The Global Busy Union ($\mathcal{U}$):**
    - Flatten all intervals across all employees into a single collection:
      $$
      \mathcal{B} = \bigcup_{e \in schedule} \mathcal{I}_e
      $$
    - Sort all intervals by $start$ ascending.
    - Merge overlapping and contiguous busy periods into disjoint maximal busy intervals:
      $$
      \text{merged} = [B_1, B_2, \dots, B_m]
      $$
      where each $B_k = [s_k, e_k]$ with $e_k < s_{k + 1}$.
  - **Finite Complement Gaps:**
    - Because the merged blocks $B_k$ represent the complete union of all working hours, any gap between two consecutive merged blocks is by definition unoccupied by any employee:
      $$
      \text{Free Time Interval } k = [B_k.end, \; B_{k + 1}.start] = [e_k, \; s_{k + 1}]
      $$
    - Because the merged blocks are strictly disjoint ($e_k < s_{k + 1}$), every such gap is guaranteed to have strictly positive duration ($s_{k + 1} - e_k > 0$).
- **Step-by-Step Worked Execution Trace on the 3-Employee Schedule:**
  - **Phase 0: Flatten All Shifts:**
    - From Employee 0: $[1, 2], [5, 6]$.
    - From Employee 1: $[1, 3]$.
    - From Employee 2: $[4, 10]$.
    - Unsorted collection:
      $$
      intervals = [[1, 2], \; [5, 6], \; [1, 3], \; [4, 10]]
      $$
  - **Phase 1: Sort Shifts by Start Time:**
    $$
    intervals = [[1, 2], \; [1, 3], \; [4, 10], \; [5, 6]]
    $$
  - **Phase 2: Merge Overlapping Busy Intervals:**
    - Seed merged list with first interval:
      $$
      merged = [[1, 2]]
      $$
    - **Interval 2 ($[1, 3]$):**
      - Check overlap with tail $[1, 2]$:
        $$
        merged[-1].end \ge x.start \iff 2 \ge 1 \quad \mathbf{(Overlaps!)}
        $$
      - Extend tail end:
        $$
        merged[-1].end \leftarrow \max(2, 3) = \mathbf{3}
        $$
      - Merged list: $[[1, 3]]$.
    - **Interval 3 ($[4, 10]$):**
      - Check overlap with tail $[1, 3]$:
        $$
        merged[-1].end < x.start \iff 3 < 4 \quad \mathbf{(Gap\ Detected!)}
        $$
      - Start new disjoint busy block:
        $$
        merged = [[1, 3], \; [4, 10]]
        $$
    - **Interval 4 ($[5, 6]$):**
      - Check overlap with tail $[4, 10]$:
        $$
        merged[-1].end \ge x.start \iff 10 \ge 5 \quad \mathbf{(Overlaps!)}
        $$
      - Extend tail end:
        $$
        merged[-1].end \leftarrow \max(10, 6) = \mathbf{10}
        $$
      - Merged list: $[[1, 3], \; [4, 10]]$.
  - **Phase 3: Extract Gaps Between Merged Blocks:**
    - Pairwise consecutive blocks:
      - Block 1: $A = [1, 3]$ (ends at $3$).
      - Block 2: $B = [4, 10]$ (starts at $4$).
    - Construct free-time gap:
      $$
      \text{gap} = [A.end, \; B.start] = [\mathbf{3}, \; \mathbf{4}]
      $$
  - **Final Output:**
    $$
    ans = [[3, 4]]
    $$
- **Multiple Gaps Trace ($schedule = [[[1, 3], [6, 7]], [[2, 4]], [[2, 5], [9, 12]]]$):**
  - Flattened and merged:
    - Merged blocks: $[1, 5]$, $[6, 7]$, $[9, 12]$.
  - Gaps between blocks:
    - Between $[1, 5]$ and $[6, 7]$: $[5, 6]$.
    - Between $[6, 7]$ and $[9, 12]$: $[7, 9]$.
  - Returns `[[5, 6], [7, 9]]`.
- **Single Continuous Block ($schedule = [[[1, 5]], [[2, 6]], [[3, 4]]]$):**
  - Merged into a single uninterrupted block $[1, 6]$.
  - Zero internal gaps exist.
  - Returns empty list `[]`.

This instance demonstrates interval union consolidation and 1D topological complement extraction, mathematically proves why pairwise boundary differences between disjoint closed intervals partition the free open space, and derives $O(N \log N)$ runtime and $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given employee working intervals:
Find all **finite intervals of common free time** (when NO employee is working).

```text
schedule:
  Emp 0: [1, 2], [5, 6]
  Emp 1: [1, 3]
  Emp 2: [4, 10]

Flatten and merge all busy times:
  [1, 2] + [1, 3] -> [1, 3]
  [4, 10] + [5, 6] -> [4, 10]

Merged busy blocks: [1, 3] and [4, 10]
Gap between them: [3, 4]!

Result: [ [3, 4] ]
```

### The Invariant of the Merged Complement
- The common free time is the complement of the union of all employees' working hours.
- Merging all intervals into disjoint blocks $B_1, B_2, \dots, B_m$ means common free time consists strictly of the intervals between them: $[B_i.end, B_{i+1}.start]$.

---

## 2. Conceptual Foundation & Invariants

### 1. Global Busy Interval Union:
$$
\mathcal{B} = \bigcup_{i, j} schedule[i][j]
$$
$$
merged = \text{MergeOverlapping}(\text{sort}(\mathcal{B}))
$$

### 2. Gap Extraction:
$$
ans = \{ [merged[i].end, \; merged[i + 1].start] \mid 0 \le i < |merged| - 1 \}
$$

> **Complement Open Set Invariant.** For any finite collection of closed intervals $\{I_k\}$, their union $U = \bigcup I_k$ is a disjoint union of closed components $\bigsqcup_{j=1}^m [s_j, e_j]$, whose bounded complement $\mathbb{R} \setminus U \cap [s_1, e_m]$ consists of open intervals $(e_j, s_{j+1})$, whose topological closures form the desired free intervals $[e_j, s_{j+1}]$.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Flatten & Sort
- $[1, 2], [1, 3], [4, 10], [5, 6]$.

---

### Step 2: Merge
- $[1, 2] + [1, 3] \implies [1, 3]$.
- $[4, 10] + [5, 6] \implies [4, 10]$.
- Merged: $[1, 3]$ and $[4, 10]$.

---

### Step 3: Extract Gaps
- Between $[1, 3]$ and $[4, 10] \implies [3, 4]$.

---

### Step 4: Output
$$
[[3, 4]]
$$

---

## 4. Complete Execution Trace

| Shift Scanned $[s, e]$ | Current Merged Tail | Overlap? | Action Taken | Active Merged Blocks List |
|:---:|:---:|:---:|:---:|:---:|
| `[1, 2]` | None | Base | Initialize | `[[1, 2]]` |
| `[1, 3]` | `[1, 2]` | Yes ($1 \le 2$) | Extend end to $3$ | `[[1, 3]]` |
| `[4, 10]` | `[1, 3]` | No ($4 > 3$) | Append new block | `[[1, 3], [4, 10]]` |
| `[5, 6]` | `[4, 10]` | Yes ($5 \le 10$) | Extend end to $\max(10, 6)$ | `[[1, 3], [4, 10]]` |
| **Gaps** | — | — | **Extract $[3, 4]$** | **`[[3, 4]]`** |

---

## 5. Boundary Cases & Failure Modes

- **No Gaps (Continuous Coverage):** Merged into one single block $[1, 10] \implies$ returns empty list `[]`.
- **Single Employee with Gaps ($[[[1, 2], [4, 5]]]$):** That employee's internal gap $[2, 4]$ is valid common free time.
- **Multiple Intersecting Gaps:** Pairwise loop cleanly extracts all internal gaps in sorted order.
- **Infinite Boundaries ($(-\infty, 1)$ or $(10, \infty)$):** Excluded by problem specification; only interior finite gaps are returned.

---

## 6. Traps & Common Anti-Patterns

- **Using a Priority Queue / Min-Heap When Not Needed:** While a $K$-way merge heap works in $O(N \log K)$, flattening and sorting all intervals directly takes $O(N \log N)$ and is vastly simpler and faster in practice for typical constraints.
- **Zero-Length Gaps ($a.end == b.start$):** If an interval starts exactly when another ends (e.g. $[1, 3]$ and $[3, 5]$), they touch with zero free time. The merge check must use $merged[-1].end \ge x.start$ to combine them into $[1, 5]$.
- **Forgetting to Update Tail End with Max:** When an incoming interval is fully enclosed (e.g. $[5, 6]$ inside $[4, 10]$), setting `end = x.end` would shrink the block! Must use `max(merged[-1].end, x.end)`.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $N$ be the total number of intervals across all employees ($N \le 500$).
  - Sorting all $N$ intervals: $\mathcal{O}(N \log N)$.
  - Single pass to merge and extract gaps: $\mathcal{O}(N)$.
  - Total Time: strictly $\mathcal{O}(N \log N)$. Completes in $< 1$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ memory to store the flattened interval list and merged blocks.
