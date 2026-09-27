# Guided Example: Insert Interval

We trace the step-by-step 3-stage linear insertion and merging algorithm on a representative sorted interval collection:

- **Input:** $\text{intervals} = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]$, $\text{newInterval} = [4, 8]$
- **Required output:** $[[1, 2], [3, 10], [12, 16]]$

This instance demonstrates exploiting the pre-sorted non-overlapping property of the input to perform single-pass insertion ($O(N)$ time), partitioning the process into three distinct stages (pre-overlap, overlap absorption, and post-overlap), and updating interval endpoints in place.

---

## 1. Instance & Teaching Goal

Given an array of non-overlapping intervals $\text{intervals}$ sorted in ascending order by start time:
$$
[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
$$
and a new interval $\text{newInterval} = [4, 8]$, insert $\text{newInterval}$ into the list such that the list remains sorted and non-overlapping, merging any overlapping intervals.

A naive approach appends $\text{newInterval}$ to the end and re-sorts the entire array in $O(N \log N)$ time.
Because the existing intervals are already sorted and disjoint, we can resolve the insertion in a single linear pass ($O(N)$ time) by partitioning the array into three consecutive contiguous segments:
1. **Left Segment:** Intervals that end strictly before $\text{newInterval}$ begins ($e < \text{newInterval.start}$).
2. **Overlapping Segment:** Intervals that intersect with $\text{newInterval}$ ($s \le \text{newInterval.end}$).
3. **Right Segment:** Intervals that start strictly after $\text{newInterval}$ ends ($s > \text{newInterval.end}$).

---

## 2. Conceptual Foundation & Invariants

### 3-Stage Linear Partition Algorithm
Let $\text{newInterval} = [S, E]$. We iterate index $i$ through the array:

1. **Stage 1 (Strictly to the Left):**
   While $i < N$ and $\text{intervals}[i].\text{end} < S$:
   - $\text{intervals}[i]$ ends before the new interval starts.
   - Append $\text{intervals}[i]$ directly to the result.
   - Increment $i$.

2. **Stage 2 (Overlapping Zone):**
   While $i < N$ and $\text{intervals}[i].\text{start} \le E$:
   - $\text{intervals}[i]$ overlaps with the expanding new interval.
   - Absorb interval by updating:
     $$
     S \leftarrow \min(S, \, \text{intervals}[i].\text{start})
     $$
     $$
     E \leftarrow \max(E, \, \text{intervals}[i].\text{end})
     $$
   - Increment $i$.
   - *(Once the while-loop terminates, append the consolidated $[S, E]$ to the result).*

3. **Stage 3 (Strictly to the Right):**
   While $i < N$:
   - All remaining intervals start strictly after $E$.
   - Append $\text{intervals}[i]$ directly to the result.
   - Increment $i$.

> **Invariant.** The resulting list is strictly sorted and contains zero overlapping intervals at any point during construction.

---

## 3. Step-by-Step Worked Execution

We trace $\text{intervals} = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]$ with $\text{newInterval} = [4, 8]$ ($S = 4, E = 8$):

### Stage 1: Collect Left Disjoint Intervals
- **Index $i = 0$ ($[1, 2]$):**
  - Check: $\text{intervals}[0].\text{end} = 2 < S = 4$.
  - True! Append $[1, 2]$ directly to `res`.
  - `res = [[1, 2]]`, $i \leftarrow 1$.
- **Index $i = 1$ ($[3, 5]$):**
  - Check: $\text{intervals}[1].\text{end} = 5 < 4$.
  - False ($5 \ge 4$).
  - Stage 1 terminates.

---

### Stage 2: Absorb Overlapping Intervals
- **Index $i = 1$ ($[3, 5]$):**
  - Check: $\text{intervals}[1].\text{start} = 3 \le E = 8$. True!
  - Absorb:
    $$
    S = \min(4, 3) = 3, \quad E = \max(8, 5) = 8
    $$
    Current unified interval: $[3, 8]$. $i \leftarrow 2$.
- **Index $i = 2$ ($[6, 7]$):**
  - Check: $\text{intervals}[2].\text{start} = 6 \le E = 8$. True!
  - Absorb:
    $$
    S = \min(3, 6) = 3, \quad E = \max(8, 7) = 8
    $$
    Current unified interval: $[3, 8]$. $i \leftarrow 3$.
- **Index $i = 3$ ($[8, 10]$):**
  - Check: $\text{intervals}[3].\text{start} = 8 \le E = 8$. True!
  - Absorb:
    $$
    S = \min(3, 8) = 3, \quad E = \max(8, 10) = 10
    $$
    Current unified interval: $[3, 10]$. $i \leftarrow 4$.
- **Index $i = 4$ ($[12, 16]$):**
  - Check: $\text{intervals}[4].\text{start} = 12 \le E = 10$. False ($12 > 10$).
  - Stage 2 terminates.
- **Commit Merged Interval:**
  - Append $[S, E] = [3, 10]$ to `res`.
  - `res = [[1, 2], [3, 10]]`.

---

### Stage 3: Collect Right Disjoint Intervals
- **Index $i = 4$ ($[12, 16]$):**
  - Append $[12, 16]$ directly to `res`.
  - $i \leftarrow 5$ (End of array).

Final result: `[[1, 2], [3, 10], [12, 16]]`.

---

## 4. Complete Execution Trace

| Array Index $i$ | Examined Interval $[s, e]$ | Active Stage | Condition Evaluated | Unified $\text{newInterval}$ $[S, E]$ | Action on Output List |
|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | `[1, 2]` | Stage 1 (Left) | $2 < 4$ (True) | `[4, 8]` | Append `[1, 2]` |
| 1 | `[3, 5]` | Stage 2 (Overlap) | $3 \le 8$ (True) | $\min(4,3), \max(8,5) \to \mathbf{[3, 8]}$ | Expand merged interval |
| 2 | `[6, 7]` | Stage 2 (Overlap) | $6 \le 8$ (True) | $\min(3,6), \max(8,7) \to \mathbf{[3, 8]}$ | Fully contained |
| 3 | `[8, 10]` | Stage 2 (Overlap) | $8 \le 8$ (True) | $\min(3,8), \max(8,10) \to \mathbf{[3, 10]}$ | Extend right boundary |
| - | - | Stage 2 End | $12 \le 10$ (False) | `[3, 10]` | **Append `[3, 10]`** |
| 4 | `[12, 16]` | Stage 3 (Right) | Remainder | - | Append `[12, 16]` |

---

## 5. Algorithmic Correctness

**Soundness.** Stage 1 only admits intervals strictly preceding $S$. Stage 2 absorbs every interval that touches or intersects the expanding interval $[S, E]$. Stage 3 only admits intervals strictly succeeding $E$. The resulting concatenation is provably disjoint and sorted.

**Completeness.** Every interval in the input array is processed exactly once by one of the three stages. The index $i$ advances monotonically from $0$ to $N$, guaranteeing $O(N)$ execution.

---

## 6. Traps This Instance Exposes

- **Zero Overlaps (Disjoint Insertion):** If $\text{newInterval}$ does not overlap any interval (e.g. inserting $[5, 7]$ into $[[1, 2], [8, 9]]$), Stage 2 runs zero times, and $[5, 7]$ is inserted cleanly between Stage 1 and Stage 3.
- **Empty Intervals Input:** When $\text{intervals} = []$, Stage 1 and 3 are skipped, and Stage 2 simply appends $\text{newInterval}$, correctly returning $[\text{newInterval}]$.
- **Touching Boundaries ($e == S$ or $s == E$):** In closed intervals, touching endpoints constitute an overlap (e.g. $[8, 10]$ with $E = 8$). Using $\le$ rather than strictly $<$ in Stage 2 ensures contiguous intervals are properly coalesced.

### Where the New Interval Can Land

The three stages behave differently in each placement, and the table is the quickest way to see which stage carries the answer. Every result below is the verified output for the authored case.

| Placement of $[S, E]$ | Instance | How the stages divide the work | Verified result |
|---|---|---|---|
| Before every interval | `[[5,7],[9,11]]` with `[1,2]` | Stage 1 stops at index 0 because $5 \ge S = 1$; Stage 2 absorbs nothing since $5 > E = 2$; Stage 3 copies both intervals unchanged. | `[[1,2],[5,7],[9,11]]` |
| Into an empty list | `[]` with `[5,7]` | Stages 1 and 3 have no input, so Stage 2 absorbs nothing and must still commit $[S, E]$; the output is exactly the new interval. | `[[5,7]]` |
| Overlapping a single interval | `[[1,3],[6,9]]` with `[2,5]` | Stage 1 never fires ($3 \ge S = 2$); $[1,3]$ is absorbed, giving $S = \min(2,1) = 1$ and $E = \max(5,3) = 5$; Stage 3 copies $[6,9]$. | `[[1,5],[6,9]]` |
| Swallowing the whole list | `[[2,3],[5,6],[8,9]]` with `[0,12]` | Stage 1 never fires, Stage 2 absorbs all three intervals because every start is at most $E = 12$, and Stage 3 has nothing left to copy; $S$ stays $0$ while $E$ reaches $12$. | `[[0,12]]` |
| Touching both neighbours | `[[1,2],[4,5]]` with `[2,4]` | $[1,2]$ fails Stage 1 ($2 < S = 2$ is false) and is absorbed, as is $[4,5]$ because $4 \le E = 4$; a strict test in Stage 2 would leave $[2,4]$ glued to $[4,5]$ without merging them. | `[[1,5]]` |
| After every interval | `[[1,2],[5,7]]` with `[9,11]` | Stage 1 emits both intervals because $2 < 9$ and $7 < 9$; Stage 2 finds nothing to absorb yet must still place $[9,11]$ before Stage 3 runs. | `[[1,2],[5,7],[9,11]]` |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of intervals. The index $i$ moves strictly from $0$ to $N$ across the three stages. No sorting is needed.
- **Auxiliary Space Complexity:** $O(N)$ to hold the emitted output list. The iteration itself uses $O(1)$ scalar pointers.

### Comparison of Candidate Methods

The input is already sorted and disjoint, so the methods below differ mainly in how much of that order they exploit — and each has a distinct way of losing a touching neighbour.

| Method | Time | Auxiliary space | Tradeoff or failure mode |
|---|---|---|---|
| Three-stage linear partition (this lesson) | $O(N)$ | $O(N)$ for the output, $O(1)$ working pointers | The consolidated $[S, E]$ must be committed even when Stage 2 absorbed nothing, and Stage 2 must test start $\le E$; a strict test leaves a touching pair unmerged. |
| Append the new interval, re-sort, then merge | $O(N \log N)$ | $O(N)$ | Ignores the order the contract already guarantees and pays a full sort; correctness then depends on the general merge using a non-strict gap test. |
| Binary search for the first interval starting after $E$, then fold the covered range | $O(\log N + k)$ for $k$ absorbed intervals | $O(N)$ for the output | The search predicate must agree with the overlap test: looking for start $> E$ while merging on start $\le E$ is consistent, but searching on the end coordinate instead can skip a touching neighbour. |
| Single filtering pass that folds overlapping intervals with $\min$ and $\max$ | $O(N)$ | $O(N)$ for the output | No explicit stages means the merged interval needs a flag for whether it was already emitted; without it, a placement that overlaps nothing either loses the new interval or emits it twice. |
