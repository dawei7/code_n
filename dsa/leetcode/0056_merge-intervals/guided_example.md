# Guided Example: Merge Intervals

We trace the step-by-step execution of sorted interval merging on a representative collection of ranges:

- **Input:** $\text{intervals} = [[1, 3], [2, 6], [8, 10], [15, 18]]$
- **Required output:** $[[1, 6], [8, 10], [15, 18]]$

This instance demonstrates sorting intervals by start point, extending active intervals when start $\le$ end ($\text{last\_end} = \max(\text{last\_end}, \text{cur\_end})$), recognizing disjoint separation gaps, and handling complete containment.

---

## 1. Instance & Teaching Goal

Given an array of $N = 4$ intervals:
$$
[[1, 3], [2, 6], [8, 10], [15, 18]]
$$
we must merge all overlapping intervals and return an array of non-overlapping intervals that cover the entire range.

Without sorting, an interval might overlap with another interval located anywhere in the list, requiring $O(N^2)$ comparisons or connected component graph traversals. By sorting intervals by their start coordinate, all potentially overlapping intervals become adjacent in the array, reducing merging to a single $O(N)$ linear scan.

---

## 2. Conceptual Foundation & Invariants

### Sorting & The Overlap Invariant
We reorder the intervals so that their start coordinates are non-decreasing:
$$
s_1 \le s_2 \le \dots \le s_N
$$

For any two adjacent intervals $A = [s_A, e_A]$ and $B = [s_B, e_B]$ with $s_A \le s_B$:
1. **Overlap Condition ($s_B \le e_A$):**
   Interval $B$ begins before interval $A$ ends. Their union is a single contiguous interval:
   $$
   [s_A, \, \max(e_A, e_B)]
   $$
2. **Disjoint Condition ($s_B > e_A$):**
   A non-empty gap exists between $e_A$ and $s_B$. Because the array is sorted, all subsequent intervals $C$ will have $s_C \ge s_B > e_A$. Therefore, interval $A$ can never overlap with any future interval and is finalized.

> **Invariant.** The last element in the merged list always represents the maximal rightward extension of all overlapping intervals processed so far.

---

## 3. Step-by-Step Worked Execution

We trace sorted intervals $[[1, 3], [2, 6], [8, 10], [15, 18]]$:

### Initialization
- Sort intervals: Already sorted by start coordinate.
- Initialize `merged = []`.
- Insert first interval: `merged.append([1, 3])`.

---

### Step 1: Process Interval $[2, 6]$
- Active merged tail: $\text{last} = [1, 3]$.
- New interval: $\text{cur} = [2, 6]$.
- Compare: Does $\text{cur}[0] \le \text{last}[1]$?
  $$
  2 \le 3 \implies \textbf{True (Overlapping)}
  $$
- Merge action: Update tail endpoint to $\max(\text{last}[1], \text{cur}[1]) = \max(3, 6) = 6$.
- Updated merged list: $[[1, 6]]$.

---

### Step 2: Process Interval $[8, 10]$
- Active merged tail: $\text{last} = [1, 6]$.
- New interval: $\text{cur} = [8, 10]$.
- Compare: Does $8 \le 6$?
  $$
  8 \le 6 \implies \textbf{False (Disjoint)}
  $$
- Action: Finalize $[1, 6]$ and append $[8, 10]$.
- Updated merged list: $[[1, 6], [8, 10]]$.

---

### Step 3: Process Interval $[15, 18]$
- Active merged tail: $\text{last} = [8, 10]$.
- New interval: $\text{cur} = [15, 18]$.
- Compare: Does $15 \le 10$?
  $$
  15 \le 10 \implies \textbf{False (Disjoint)}
  $$
- Action: Finalize $[8, 10]$ and append $[15, 18]$.
- Updated merged list: $[[1, 6], [8, 10], [15, 18]]$.

All intervals processed. Return `merged`.

---

## 4. Complete Execution Trace

| Step | Candidate Interval $[s, e]$ | Current Tail of Merged List | Overlap Test ($s \le \text{tail}[1]$) | Action Taken | Resulting Merged List |
|:---:|:---:|:---:|:---:|:---|:---|
| 0 | `[1, 3]` | None | - | Initial append | `[[1, 3]]` |
| 1 | `[2, 6]` | `[1, 3]` | $2 \le 3$ (True) | Extend tail: $\max(3, 6) = 6$ | `[[1, 6]]` |
| 2 | `[8, 10]` | `[1, 6]` | $8 \le 6$ (False) | Disjoint: Append new interval | `[[1, 6], [8, 10]]` |
| 3 | `[15, 18]` | `[8, 10]` | $15 \le 10$ (False) | Disjoint: Append new interval | `[[1, 6], [8, 10], [15, 18]]` |

---

## 5. Algorithmic Correctness

**Soundness.** Because intervals are sorted by start coordinate, if $s_{i} \le e_{i-1}$, the two intervals intersect at least on $[s_i, e_{i-1}]$. Their union is $[s_{i-1}, \max(e_{i-1}, e_i)]$.

**Completeness.** If $s_i > e_{i-1}$, then for any $k > i$, $s_k \ge s_i > e_{i-1}$. No later interval can overlap with interval $i - 1$. Hence, committing $[s_{i-1}, e_{i-1}]$ to the output is safe and permanent.

---

## 6. Traps This Instance Exposes

- **Touching Endpoints ($[1, 4]$ and $[4, 5]$):** The definition of interval overlap is closed: $[1, 4]$ and $[4, 5]$ share point $4$. The condition must be $s \le \text{tail}[1]$, not strictly $<$.
- **Complete Containment ($[1, 5]$ and $[2, 3]$):** If the new interval is fully contained, blindly setting $\text{tail}[1] = e$ would shorten the interval from $5$ to $3$. Using $\max(\text{tail}[1], e)$ ensures the end never shrinks.
- **Unsorted Input:** If the input is unsorted (e.g. $[[2, 6], [1, 3]]$), linear merging will miss the overlap. Sorting upfront is mandatory.

### Boundary and Nested Instances

Each row below is settled by the same two operations, and each one isolates a different way the scan can go wrong. Values are the verified outputs for the authored cases.

| Scenario | Instance | Order actually scanned | Decision that settles the case | Verified result |
|---|---|---|---|---|
| Closed endpoints touching | `[[1,4],[4,5]]` | `[[1,4],[4,5]]` | $4 \le 4$ is true, so the shared point $4$ joins the two intervals; a strict $<$ test would wrongly emit two intervals. | `[[1,5]]` |
| Touching pair supplied out of order | `[[4,7],[1,4]]` | `[[1,4],[4,7]]` | Sorting moves the later-starting interval second; then $4 \le 4$ extends the tail to $\max(4, 7) = 7$. | `[[1,7]]` |
| Nested intervals | `[[1,10],[2,3],[4,8]]` | `[[1,10],[2,3],[4,8]]` | Both followers satisfy start $\le 10$, and $\max(10, 3) = \max(10, 8) = 10$: replacing the end with the candidate end would shrink the interval. | `[[1,10]]` |
| Disjoint intervals given unsorted | `[[9,11],[1,2],[5,7]]` | `[[1,2],[5,7],[9,11]]` | After sorting, $5 > 2$ and $9 > 7$, so each gap finalizes the interval already held. | `[[1,2],[5,7],[9,11]]` |
| Transitive overlap chain | `[[1,2],[5,8],[2,6],[10,12],[11,15]]` | `[[1,2],[2,6],[5,8],[10,12],[11,15]]` | $[1,2]$ touches $[2,6]$, which reaches $[5,8]$ although $[1,2]$ and $[5,8]$ are disjoint; the single running end carries the chain forward. | `[[1,8],[10,15]]` |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \log N)$ to sort $N$ intervals. The subsequent linear merging pass takes $O(N)$ time. Total runtime is $O(N \log N)$.
- **Auxiliary Space Complexity:** $O(N)$ (or $O(\log N)$ depending on sorting implementation) to store the output merged list.

### Comparison of Candidate Methods

Every method below returns the same three intervals on this instance; they differ in how much order they impose before merging and in which boundary ordering destroys them.

| Method | What it maintains | Time | Auxiliary space | Tradeoff or failure mode |
|---|---|---|---|---|
| Sort by start, then one scan (this lesson) | A single open interval $[s, e]$ | $O(N \log N)$ | $O(N)$ for the result, $O(\log N)$ extra from the sort | The gap test must be $e < s$; writing it as $e \le s$ splits intervals that share an endpoint, such as $[1,4]$ and $[4,5]$. |
| Sweep over the $2N$ endpoints with an active counter | A sorted endpoint list and a running count | $O(N \log N)$ | $O(N)$ | Whenever one interval ends exactly where the next starts, the starting event must be consumed before the ending event; the opposite tie order separates those two intervals. |
| Pairwise overlap as connected components | A parent pointer per interval | $O(N^{2})$ to test every pair | $O(N)$ | At $N = 10^{4}$ that is about $10^{8}$ pair tests, and the components still need a second pass to be turned back into intervals. |
| Insert each interval into a kept-sorted non-overlapping list | The current merged list and the insertion position | $O(N^{2})$ from shifting elements | $O(N)$ | Every insertion has to handle containment, full overlap and touching neighbours, and the list must be re-scanned from the insertion point forward. |
