# Guided Example: Meeting Rooms

We trace the step-by-step start-time ordering, adjacent interval conflict detection, and transitivity proof on representative meeting schedules:

- **Input:** $\text{intervals} = [[0, 30], [5, 10], [15, 20]]$
- **Required output:** `false` (Meeting $[0, 30]$ conflicts with meeting $[5, 10]$ because $30 > 5$)
- **Compatible Schedule Instance:** $\text{intervals} = [[7, 10], [2, 4]] \implies \text{true}$ (Sorted: $[[2, 4], [7, 10]]$; $4 \le 7$)
- **Touching Boundary Instance:** $\text{intervals} = [[1, 3], [3, 5]] \implies \text{true}$ (A meeting ending at 3 permits the next meeting to start at 3)
- **Identical Start Conflict:** $\text{intervals} = [[1, 5], [1, 2]] \implies \text{false}$ (Two meetings starting at the same time conflict immediately)

This instance demonstrates interval scheduling validation, proves by start-time transitivity why sorting reduces an all-pairs $O(N^2)$ quadratic overlap verification to adjacent $O(1)$ comparisons, handles boundary equality ($\text{end} \le \text{start}$), and runs in $O(N \log N)$ sorting-dominated time.

---

## 1. Instance & Teaching Goal

Given a list of meeting time intervals:
$$
\text{intervals} = [[0, 30], [5, 10], [15, 20]]
$$
Determine whether a single person can attend all meetings without overlap.
```text
Time:      0----5----10---15---20--------30
Meeting 0: [==============================] (0 to 30)
Meeting 1:      [====]                     (5 to 10)  <- OVERLAP!
Meeting 2:                [====]           (15 to 20)
```
Meeting 0 runs until time $30$, but Meeting 1 begins at time $5$. Since $30 > 5$, both meetings cannot be attended by one person.
Return `false`.

### The All-Pairs vs Adjacent Reduction
A person can attend all meetings if and only if **no two intervals overlap**.
- Checking every pair $(I_i, I_j)$ requires $\binom{N}{2} = \frac{N(N-1)}{2} = O(N^2)$ comparisons.
- If we sort the intervals in ascending order of their start times:
  $$
  I_0, I_1, I_2, \dots, I_{N-1} \quad \text{where } \text{start}_0 \le \text{start}_1 \le \dots \le \text{start}_{N-1}
  $$
  We only need to check **adjacent neighbors**: $\text{end}_i \le \text{start}_{i+1}$.
  Sorting brings total time down to $O(N \log N)$ with $O(1)$ comparisons per pair.

---

## 2. Conceptual Foundation & Invariants

### The Start-Time Transitivity Lemma
Suppose intervals are sorted such that $\text{start}_i \le \text{start}_{i+1} \le \text{start}_j$ for all $j > i$.
Suppose an interval $I_i$ overlaps with some distant future interval $I_j$ ($j > i + 1$).
By definition of overlap with a later starting interval:
$$
\text{end}_i > \text{start}_j
$$
Since the sequence is sorted by start times, $\text{start}_j \ge \text{start}_{i+1}$.
Combining inequalities:
$$
\text{end}_i > \text{start}_j \ge \text{start}_{i+1} \implies \text{end}_i > \text{start}_{i+1}
$$
Therefore, **if $I_i$ overlaps with any future interval $I_j$, it MUST overlap with the immediately following interval $I_{i+1}$**!

Thus, verifying $\text{end}_i \le \text{start}_{i+1}$ for all adjacent pairs $i \in [0, N-2]$ guarantees zero overlaps across the entire array.

### Algorithm Protocol
1. Sort `intervals` in-place by `start` time:
   $$
   \text{intervals}.\text{sort}(\text{key} = \lambda x: x[0])
   $$
2. For $i$ from $0$ to $N - 2$:
   If $\text{intervals}[i][1] > \text{intervals}[i+1][0]$:
   $$
   \text{return false} \quad (\text{Conflict found!})
   $$
3. Return `true`.

> **Invariant.** After validating pair $(i, i+1)$, interval $I_i$ is guaranteed not to overlap with any interval in the suffix $I_{i+1 \dots N-1}$.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $\text{intervals} = [[0, 30], [5, 10], [15, 20]]$ ($N = 3$):

### Step 1: Sort by Start Time
- Given intervals: $[0, 30], [5, 10], [15, 20]$.
- Start times: $0 \le 5 \le 15$.
- Already sorted:
  - $I_0 = [0, 30]$
  - $I_1 = [5, 10]$
  - $I_2 = [15, 20]$

---

### Step 2: Evaluate Adjacent Pair $(I_0, I_1)$
- Interval $I_0$: Start $= 0$, End $= 30$.
- Interval $I_1$: Start $= 5$, End $= 10$.
- Compatibility check:
  $$
  \text{end}_0 \le \text{start}_1 \iff 30 \le 5 \quad (\mathbf{\text{Violated! } 30 > 5})
  $$
- Conflict detected! Meeting $0$ does not conclude before Meeting $1$ begins.
- Early short-circuit return:
  $$
  \text{return false}
  $$

---

## 4. Complete Execution Trace

```text
Input: [[0, 30], [5, 10], [15, 20]]
Sorted: [[0, 30], [5, 10], [15, 20]]

i = 0: Compare [0, 30] and [5, 10]
       end[0] = 30, start[1] = 5
       30 > 5 -> Conflict!
Early exit: return False
```

| Step | Pair Tested $(I_i, I_{i+1})$ | Previous End $\text{end}_i$ | Next Start $\text{start}_{i+1}$ | Condition $\text{end}_i \le \text{start}_{i+1}$ | Outcome |
|:---:|:---:|:---:|:---:|:---:|:---|
| **1** | **$([0, 30], [5, 10])$** | **30** | **5** | **$30 \le 5$ (False: $30 > 5$)** | **Conflict! Return `false`** |

### Contrast: Valid Schedule Execution ($\text{intervals} = [[7, 10], [2, 4]]$)
1. Sort by start: $[[2, 4], [7, 10]]$.
2. Adjacent check $i = 0$:
   - Previous end $= 4$, Next start $= 7$.
   - $4 \le 7$ holds!
3. Loop completes $\implies$ **`true`**.

### Contrast: Touching Interval Execution ($\text{intervals} = [[1, 3], [3, 5]]$)
1. Sort by start: $[[1, 3], [3, 5]]$.
2. Adjacent check:
   - Previous end $= 3$, Next start $= 3$.
   - $3 \le 3$ holds! (Meeting ends at 3, next starts at 3; no overlap).
3. Loop completes $\implies$ **`true`**.

---

## 5. Algorithmic Correctness

**Soundness.** If the algorithm returns `false`, it found an index $i$ where $\text{end}_i > \text{start}_{i+1}$. Since $\text{start}_i \le \text{start}_{i+1}$, the time interval $(\text{start}_{i+1}, \min(\text{end}_i, \text{end}_{i+1}))$ has non-zero duration and is occupied by both meetings simultaneously, making simultaneous attendance impossible.

**Completeness.** By the Transitivity Lemma, if any pair of intervals overlaps, at least one adjacent pair in the sorted array must overlap. The algorithm inspects every adjacent pair, guaranteeing no conflict can escape detection.

---

## 6. Traps This Instance Exposes

- **Strict Inequality Trap ($<$ vs $\le$):** If a meeting ends at 10 and the next starts at 10, they do not overlap. The conflict condition is strictly $\text{end}_i > \text{start}_{i+1}$. Writing $\text{end}_i \ge \text{start}_{i+1}$ falsely flags back-to-back meetings as conflicts.
- **Unsorted Assumption:** Comparing adjacent elements without sorting first fails immediately if input intervals are scrambled (e.g. $[[7, 10], [2, 4]]$).
- **Tie-Breaking Start Times:** If two intervals have identical start times (e.g. $[1, 5]$ and $[1, 2]$), sorting places them consecutively. Since both meetings have positive duration ($\text{start} < \text{end}$), the first interval's end will exceed $1$, triggering conflict detection regardless of which is ordered first.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \log N)$, where $N$ is the number of intervals. Sorting $N$ intervals takes $O(N \log N)$ time. The linear sweep takes at most $N - 1$ comparisons ($O(N)$ time). Sorting dominates the total running time.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary space if sorted in-place (or $O(N)$ for sorting implementations like Timsort in Python that allocate auxiliary memory for merge runs).
