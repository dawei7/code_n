# Guided Example: Data Stream as Disjoint Intervals

We trace the step-by-step ordered map bisection (`bisect_right`), boundary interval identification (`lidx`, `ridx`), the four-way interval merging topology (Bridge Merge, Left Extend, Right Extend, New Interval), and sorted disjoint interval maintenance on representative data stream sequences:

- **Input:** Stream of operations:
  1. `addNum(1)` $\implies [[1, 1]]$
  2. `addNum(3)` $\implies [[1, 1], [3, 3]]$
  3. `addNum(7)` $\implies [[1, 1], [3, 3], [7, 7]]$
  4. `addNum(2)` $\implies [[1, 3], [7, 7]]$ (Bridge merges $[1, 1]$ and $[3, 3]$ into $[1, 3]$!)
  5. `addNum(6)` $\implies [[1, 3], [6, 7]]$ (Left-extends $[7, 7]$ into $[6, 7]$!)
- **Required output:** `[[[1, 1]], [[1, 1], [3, 3]], [[1, 1], [3, 3], [7, 7]], [[1, 3], [7, 7]], [[1, 3], [6, 7]]]`
- **Redundant Value Handling:** `addNum(2)` when `[1, 3]` already exists leaves interval unchanged
- **Boundary Extension:** `addNum(4)` when `[1, 3]` exists right-extends it to `[1, 4]`

This instance demonstrates interval consolidation in dynamic streaming environments, proves why ordered balanced search trees maintain logarithmic insertion times without full list re-sorting, details the four interval merge states, and analyzes time and space complexity.

---

## 1. Instance & Teaching Goal

Given a continuous data stream of non-negative integers:
$$
\text{Values added}: 1 \to 3 \to 7 \to 2 \to 6
$$
Summarize the numbers seen so far into a list of sorted, mutually disjoint intervals $[start_i, end_i]$:

```text
Stream Progression:
addNum(1) -> [1, 1]
addNum(3) -> [1, 1], [3, 3]
addNum(7) -> [1, 1], [3, 3], [7, 7]
addNum(2) -> [1, 3], [7, 7]         <-- 2 bridges [1, 1] and [3, 3]!
addNum(6) -> [1, 3], [6, 7]         <-- 6 connects directly to [7, 7]!
```

### The 4 Interval Topological Cases on `addNum(val)`
When inserting `val`, query its immediate predecessor interval $L = [s_L, e_L]$ and successor interval $R = [s_R, e_R]$:
1. **Case 1 (Bridge Merge):** $e_L + 1 = val$ and $s_R - 1 = val$.
   $val$ bridges both intervals into one continuous interval $[s_L, e_R]$. Delete $R$.
2. **Case 2 (Left Extend / Internal):** $val \le e_L + 1$.
   If $val == e_L + 1$, expand right boundary: $e_L \leftarrow val$. If $val \le e_L$, already contained.
3. **Case 3 (Right Extend):** $val \ge s_R - 1$.
   Expand left boundary: $s_R \leftarrow val$.
4. **Case 4 (Disjoint Island):** Neither neighbor touches $val$.
   Create new singleton interval $[val, val]$.

---

## 2. Conceptual Foundation & Invariants

### 1. Data Structure: Ordered Map (`SortedDict`)
Maintain a sorted dictionary `mp` mapping each interval's start coordinate to its interval pair:
$$
mp[start] = [start, \; end]
$$
- `bisect_right(val)` locates index `ridx` of the first interval starting strictly after `val`.
- The predecessor interval index is `lidx = ridx - 1` (if `ridx > 0`).

### 2. Transition Logic:
- **Case 1:** If $e_L + 1 == val$ and $s_R - 1 == val$:
  $$
  mp[s_L][1] \leftarrow mp[s_R][1], \quad \text{pop}(s_R)
  $$
- **Case 2:** Else if $lidx$ exists and $val \le e_L + 1$:
  $$
  mp[s_L][1] \leftarrow \max(val, \; mp[s_L][1])
  $$
- **Case 3:** Else if $ridx$ exists and $val \ge s_R - 1$:
  $$
  mp[s_R][0] \leftarrow \min(val, \; mp[s_R][0])
  $$
- **Case 4:** Else:
  $$
  mp[val] = [val, \; val]
  $$

> **Invariant.** All intervals stored in `mp` are strictly disjoint, non-adjacent ($e_i + 1 < s_{i+1}$), and ordered by increasing start coordinate.

---

## 3. Step-by-Step Worked Execution

We trace the arrival of stream elements: `1, 3, 7, 2, 6`:

---

### Step 1: `addNum(1)`
- Map is empty ($n = 0$).
- Falls into **Case 4**: create new interval.
- `mp[1] = [1, 1]`.
- Output: `[[1, 1]]`.

---

### Step 2: `addNum(3)`
- `ridx = 1` (no successor interval), `lidx = 0` ($[1, 1]$).
- Neighbor check: $e_L + 1 = 1 + 1 = 2 \ne 3$.
- Falls into **Case 4**: create new interval.
- `mp[3] = [3, 3]`.
- Output: `[[1, 1], [3, 3]]`.

---

### Step 3: `addNum(7)`
- `lidx = [3, 3]`, no successor. $e_L + 1 = 3 + 1 = 4 \ne 7$.
- Falls into **Case 4**: create new interval.
- `mp[7] = [7, 7]`.
- Output: `[[1, 1], [3, 3], [7, 7]]`.

---

### Step 4: `addNum(2)` — Bridge Merge!
- Search position for $val = 2$:
  - Predecessor $L = [1, 1]$ at `lidx = 0`.
  - Successor $R = [3, 3]$ at `ridx = 1`.
- Check **Case 1 (Bridge)**:
  $$
  e_L + 1 = 1 + 1 = 2 == val \quad (\mathbf{\text{True}})
  $$
  $$
  s_R - 1 = 3 - 1 = 2 == val \quad (\mathbf{\text{True}})
  $$
- Actions:
  - Extend $L$'s end to $R$'s end: $mp[1][1] \leftarrow 3 \implies [1, 3]$.
  - Delete interval $R$: `mp.pop(3)`.
- Intervals: `[[1, 3], [7, 7]]`.

---

### Step 5: `addNum(6)` — Right Extend!
- Search position for $val = 6$:
  - Predecessor $L = [1, 3]$ (`lidx = 0`).
  - Successor $R = [7, 7]$ (`ridx = 1`).
- Check conditions:
  - $e_L + 1 = 3 + 1 = 4 \ne 6$ (Case 1 and Case 2 false).
  - $s_R - 1 = 7 - 1 = 6 == val$ (**Case 3 True!**).
- Action:
  - Extend $R$'s start coordinate: $mp[7][0] \leftarrow \min(6, 7) = 6 \implies [6, 7]$.
- Intervals: `[[1, 3], [6, 7]]`.

---

## 4. Complete Execution Trace

```text
SummaryRanges Execution:
addNum(1): Case 4 -> mp = {1: [1, 1]}
getIntervals()   -> [[1, 1]]

addNum(3): Case 4 -> mp = {1: [1, 1], 3: [3, 3]}
getIntervals()   -> [[1, 1], [3, 3]]

addNum(7): Case 4 -> mp = {1: [1, 1], 3: [3, 3], 7: [7, 7]}
getIntervals()   -> [[1, 1], [3, 3], [7, 7]]

addNum(2): Case 1 (Bridge [1,1] and [3,3]) -> mp = {1: [1, 3], 7: [7, 7]}
getIntervals()   -> [[1, 3], [7, 7]]

addNum(6): Case 3 (Extend [7,7] left) -> mp = {1: [1, 3], 7: [6, 7]}
getIntervals()   -> [[1, 3], [6, 7]]
```

| Operation | Added $val$ | Predecessor $L$ | Successor $R$ | Merge Condition Triggered | Action Taken | Active Disjoint Intervals |
|:---:|:---:|:---:|:---:|:---:|:---|:---|
| `addNum(1)` | 1 | None | None | Case 4: Disjoint | Insert `[1, 1]` | `[[1, 1]]` |
| `addNum(3)` | 3 | `[1, 1]` | None | Case 4: Disjoint | Insert `[3, 3]` | `[[1, 1], [3, 3]]` |
| `addNum(7)` | 7 | `[3, 3]` | None | Case 4: Disjoint | Insert `[7, 7]` | `[[1, 1], [3, 3], [7, 7]]` |
| **`addNum(2)`** | **2** | **`[1, 1]`** | **`[3, 3]`** | **Case 1: Bridge** | **Merge $L$ with $R$, pop $R$** | **`[[1, 3], [7, 7]]`** |
| **`addNum(6)`** | **6** | **`[1, 3]`** | **`[7, 7]`** | **Case 3: Right Extend** | **Update $R$'s start to 6** | **`[[1, 3], [6, 7]]`** |

---

## 5. Algorithmic Correctness

**Soundness.** Because intervals in `mp` are kept non-overlapping and ordered, any new value $val$ can only interact with its immediate predecessor $L$ and successor $R$. The 4 exhaustive conditions correctly identify whether $val$ bridges both neighbors, attaches to one neighbor, is already contained, or starts an isolated interval. Therefore, all maintained intervals remain strictly maximal and disjoint.

**Completeness.** Bisection finds the exact neighboring interval bounds in logarithmic time. Since all potential merge partners are examined at insertion time, adjacent integers are never left split across separate intervals.

---

## 6. Traps This Instance Exposes

- **Duplicate Values in Stream:** If an already seen value (e.g. $2$ inside $[1, 3]$) arrives again, Case 2 detects $val \le e_L$ and performs a no-op $\max(2, 3) = 3$.
- **Bridge Merging Order:** In Case 1, the predecessor interval absorbs the successor interval, and the successor interval must be explicitly removed from the sorted map. Failing to pop $R$ would leave overlapping duplicates.
- **Sorted Output Guarantee:** Returning `list(self.mp.values())` directly satisfies the requirement that intervals are returned sorted by start time without additional sort passes.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - `addNum(val)`: $O(\log K)$ where $K$ is the number of disjoint intervals currently stored. Bisection and dictionary insertion/deletion in `SortedDict` operate in logarithmic time.
  - `getIntervals()`: $O(K)$ to extract and return the values of the ordered map.
- **Auxiliary Space Complexity:** $O(K)$ auxiliary memory to store at most $K \le N$ disjoint intervals.
