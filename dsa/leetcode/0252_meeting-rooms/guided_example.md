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

### Full Sweep Without Early Exit ($\text{intervals} = [[4, 1000000], [1, 3], [0, 1], [3, 4]]$)

This instance is the complement of the primary one: it never returns early, so every adjacent test runs and each of them lands exactly on an endpoint equality.

| Sweep position $i$ | $I_i$ after sorting | $I_{i+1}$ after sorting | $\text{end}_i$ | $\text{start}_{i+1}$ | Test $\text{end}_i \le \text{start}_{i+1}$ | Conclusion for this step |
|:---:|:---|:---|:---:|:---:|:---|:---|
| 0 | $[0, 1]$ | $[1, 3]$ | 1 | 1 | $1 \le 1$ holds | $I_0$ cannot overlap any interval of the remaining suffix |
| 1 | $[1, 3]$ | $[3, 4]$ | 3 | 3 | $3 \le 3$ holds | the suffix from $I_2$ on is still clear of $I_1$ |
| 2 | $[3, 4]$ | $[4, 1000000]$ | 4 | 4 | $4 \le 4$ holds | final pair cleared, so the answer is `true` |

Sorting turns the raw input $[[4, 1000000], [1, 3], [0, 1], [3, 4]]$ into $[[0, 1], [1, 3], [3, 4], [4, 1000000]]$, which is why three separate endpoint equalities become the decisive tests. Every one of them passes because the conflict condition is the strict inequality $\text{end}_i > \text{start}_{i+1}$; a chain of meetings that touch at $1$, $3$ and $4$ is fully compatible, and the large maximum time $1000000$ never even has to be compared against anything.

---

## 5. Algorithmic Correctness

**Soundness.** If the algorithm returns `false`, it found an index $i$ where $\text{end}_i > \text{start}_{i+1}$. Since $\text{start}_i \le \text{start}_{i+1}$, the time interval $(\text{start}_{i+1}, \min(\text{end}_i, \text{end}_{i+1}))$ has non-zero duration and is occupied by both meetings simultaneously, making simultaneous attendance impossible.

**Completeness.** By the Transitivity Lemma, if any pair of intervals overlaps, at least one adjacent pair in the sorted array must overlap. The algorithm inspects every adjacent pair, guaranteeing no conflict can escape detection.

---

## 6. Traps This Instance Exposes

- **Strict Inequality Trap ($<$ vs $\le$):** If a meeting ends at 10 and the next starts at 10, they do not overlap. The conflict condition is strictly $\text{end}_i > \text{start}_{i+1}$. Writing $\text{end}_i \ge \text{start}_{i+1}$ falsely flags back-to-back meetings as conflicts.
- **Unsorted Assumption:** Comparing adjacent elements without sorting first fails immediately if input intervals are scrambled (e.g. $[[7, 10], [2, 4]]$).
- **Tie-Breaking Start Times:** If two intervals have identical start times (e.g. $[1, 5]$ and $[1, 2]$), sorting places them consecutively. Since both meetings have positive duration ($\text{start} < \text{end}$), the first interval's end will exceed $1$, triggering conflict detection regardless of which is ordered first.

### Boundary instances of the same rule

Each row is a separate input evaluated by the identical protocol; the "first test" column reports the very first adjacent comparison the sorted sweep performs, which is often not the pair a reader would expect.

| Instance | First adjacent test after sorting | Verdict | What the boundary establishes |
|:---|:---|:---:|:---|
| `intervals = []` | none: there is no pair to test | `true` | an empty schedule is vacuously free of conflicts |
| `intervals = [[0, 1000000]]` | none: $N - 1 = 0$ | `true` | one meeting cannot conflict with itself, however long it lasts |
| `[[1, 3], [3, 5]]` | $3 \le 3$ holds | `true` | equality at a shared endpoint is allowed, so the conflict test must be strict |
| `[[5, 10], [5, 6]]` | sorted to $[[5, 6], [5, 10]]$: $6 \le 5$ fails | `false` | equal starts overlap even when one meeting lies entirely inside the other's span |
| `[[100, 101], [20, 30], [0, 100]]` | sorted to $[0, 100]$ then $[20, 30]$: $100 \le 20$ fails | `false` | containment is a genuine conflict, while the touching pair $[0, 100]$ and $[100, 101]$ is a distractor the sweep never needs to reach |
| `[[10, 12], [1, 5], [4, 8], [13, 15]]` | sorted to $[1, 5]$ then $[4, 8]$: $5 \le 4$ fails | `false` | the decisive pair can be created by the sort rather than appearing adjacent in the input order |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \log N)$, where $N$ is the number of intervals. Sorting $N$ intervals takes $O(N \log N)$ time. The linear sweep takes at most $N - 1$ comparisons ($O(N)$ time). Sorting dominates the total running time.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary space if sorted in-place (or $O(N)$ for sorting implementations like Timsort in Python that allocate auxiliary memory for merge runs).

### Cost of the rejected alternatives

The columns count the elementary work each strategy performs on the two traced instances, so the comparison is concrete rather than asymptotic.

| Approach | Decision rule | Work on the primary instance ($N = 3$) | Work on the touching chain ($N = 4$) | Cost or caveat |
|:---|:---|:---|:---|:---|
| All-pairs overlap test | intersect every unordered pair with no sorting at all | 3 pair tests | 6 pair tests | correct and $O(1)$ auxiliary, but $\binom{N}{2}$ tests, and it examines pairs that the transitivity lemma already proves redundant |
| Sort by start, then test adjacent pairs (the method used) | check $\text{end}_i \le \text{start}_{i+1}$ and stop at the first failure | 1 comparison | 3 comparisons, no early exit | $O(N \log N)$ dominated by the sort, with $O(1)$ work beyond it |
| Sort by end, then test the same inequality | sweep the mirrored order $[[5, 10], [15, 20], [0, 30]]$ identically | 2 comparisons | 3 comparisons | also correct — an exhaustive comparison against all-pairs agrees on every interval set of up to four meetings over a small time domain — but the decisive pair is reached one comparison later because $[0, 30]$ ends last |
| Merge overlapping intervals, then compare counts | merge the sorted list and declare failure as soon as two intervals merge | 1 comparison, then the merge | 3 comparisons, then three merges | identical comparison count with an early exit, yet it materializes the merged list, raising auxiliary memory to $O(N)$ |
| Endpoint event sweep with a concurrency counter | sort the $2N$ endpoints and keep a running count of open meetings | 6 events | 8 events | answers the stronger question of the maximum number of simultaneous meetings, which this problem never asks, and costs $O(N)$ memory plus a counter |

Only the first two rows answer the actual question with the information the input already provides; the last three either pay more comparisons, more memory, or answer a different question.
