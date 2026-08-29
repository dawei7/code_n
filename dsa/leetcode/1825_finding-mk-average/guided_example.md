# Guided Example: Finding MK Average

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": ["MKAverage", "addElement", "addElement", "calculateMKAverage", "addElement", "calculateMKAverage", "addElement", "addElement", "addElement", "calculateMKAverage"], "arguments": [[3, 1], [3], [1], [], [10], [], [5], [5], [5], []]}`
- **Required output:** `[null, null, null, -1, null, 3, null, null, null, 5]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two integers, `m` and `k`, and a stream of integers. You are tasked to implement a data structure that calculates the **MKAverage** for the stream.

The objective is to compute `[null, null, null, -1, null, 3, null, null, null, 5]` from `{"operations": ["MKAverage", "addElement", "addElement", "calculateMKAverage", "addElement", "calculateMKAverage", "addElement", "addElement", "addElement", "calculateMKAverage"], "arguments": [[3, 1], [3], [1], [], [10], [], [5], [5], [5], []]}` while avoiding redundant calculations and unnecessary overhead.

A naive or brute-force exploration risks evaluating infeasible states or repeating subproblem computations. The optimal method establishes a clear invariant that advances deterministically toward the goal.

---

## 2. Conceptual Foundation & Invariants

We maintain the core conceptual parameters and state variables:

| State Parameter | Role & Purpose | Initial State |
|---|---|---|
| Primary State | Tracks active elements, frontier indices, or DP table cells | Initialized at boundary |
| Accumulator | Preserves confirmed optimal sub-answers or counts | Empty / Neutral |

> **Invariant.** At every processing step, all previously evaluated subproblems strictly satisfy the problem constraints, and no viable candidate solution has been omitted.

---

## 3. Step-by-Step Worked Execution

### Step 1: Core Step 1

**Keep only the active window and split it by rank.** An MKAverage depends exclusively on the last `m` stream values. Among those values, the smallest `k` and largest `k` must be discarded, while the remaining `m - 2k` values must be summed and averaged. Re-sorting all `m` values for every query would repeat almost all previous work. This implementation instead maintains the window continuously in three ordered multisets:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": ["MKAverage", "addElement", "addElement", "calculateMKAverage", "addElement", "calculateMKAverage", "addElement", "addElement", "addElement", "calculateMKAverage"], "arguments": [[3, 1], [3], [1], [], [10], [], [5], [5], [5], []]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

- `lo` contains the smallest values, with a target size of `k`.
- `mid` contains the values that contribute to the average.
- `hi` contains the largest values, with a target size of `k`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

All three are `SortedList` objects, so equal values are preserved as separate occurrences and the smallest or largest element can be accessed by position. The ordering invariant is that every value in `lo` is no greater than every value in `mid`, and every value in `mid` is no greater than every value in `hi`. Boundaries may contain equal values; rank removal does not require equal copies to have distinct identities.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[null, null, null, -1, null, 3, null, null, null, 5]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": ["MKAverage", "addElement", "addElement", "calculateMKAverage", "addElement", "calculateMKAverage", "addElement", "addElement", "addElement", "calculateMKAverage"], "arguments": [[3, 1], [3], [1], [], [10], [], [5], [5], [5], []]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[null, null, null, -1, null, 3, null, null, null, 5]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sort on every calculation:** Copying and sorting the last `m` values is simple, but each query costs `O(m log m)` instead of reusing the maintained rank partition.
- **Fenwick tree over the bounded value domain:** Frequency and sum trees can locate rank cutoffs and compute retained sums in `O(log U)` time, where `U` is the maximum value. This is efficient but requires coordinate or domain indexing and more intricate rank-sum logic.
- **Two heaps alone:** Heaps expose extremes but do not support arbitrary expired-value deletion cleanly without lazy-deletion maps and careful duplicate accounting. Three ordered multisets express the needed ranks more directly.
- **Fewer than `m` values:** The partitions may not yet have both boundary groups at full size, but `calculateMKAverage` deliberately returns `-1` and never divides an incomplete middle.
- **Exactly `m` values:** No expiration occurs until the next insertion; the first complete window is already fully partitioned and queryable.
- **More than `m` values:** Exactly one oldest value is removed per insertion, so `q` and all three sorted lists represent only the latest window.
- **Many duplicate boundary values:** Equal occurrences can be stored in different buckets. Removing any one equal copy is equivalent, and the subsequent size repair keeps the middle sum correct.
- **A removed middle value:** The code subtracts it from `s` immediately, then may move a boundary value into the middle and add that replacement.
- **A removed low or high value:** No immediate sum change is needed because boundary values were excluded; if a middle value fills the gap, that move subtracts the value from `s`.
- **Integer rounding:** Positive inputs and a positive denominator make `//` the required mathematical floor.
- **Repeated queries without additions:** They do not mutate any structure, so every such call returns the same value in constant time.
- **Library requirement:** The solution relies on `SortedList` supporting duplicates and ordered index operations; replacing it with a plain Python list would make middle insertions and removals linear.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(q log m)$. Let `m` be the window size and let `q` be the number of calls to `addElement`. Each sorted partition holds at most `m` active occurrences in total. A `SortedList` search, insertion, membership test, removal, or boundary pop takes logarithmic time in the active size under the ordered-container interface used here. Each added value is inserted once, at most one expired value is removed, and only a constant number of boundary values can move during that call: insertion or deletion changes a bucket size by only one. Therefore `addElement` takes `O(log m)` time, and `q` additions take `O(q log m)` time. `calculateMKAverage` performs only a length check, subtraction, multiplication, and floor division, so it takes `O(1)` time.
- **Auxiliary Space Complexity:** $O(m+U)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
