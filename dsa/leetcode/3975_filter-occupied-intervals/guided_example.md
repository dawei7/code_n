# Guided Example: Filter Occupied Intervals

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"occupiedIntervals": [[1, 5], [2, 3]], "freeStart": 3, "freeEnd": 8}`
- **Required output:** `[[1, 2]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a 2D integer array `occupiedIntervals`, where $\text{occupiedIntervals}[i] = [\text{start}_{i}, \text{end}_{i}]$ represents a time interval during which you are occupied. Each interval starts at $\text{start}_{i}$ and ends at $\text{end}_{i}$, **inclusive**. These intervals may **overlap**.

The objective is to compute `[[1, 2]]` from `{"occupiedIntervals": [[1, 5], [2, 3]], "freeStart": 3, "freeEnd": 8}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Sorting establishes left-to-right order

The source sorts `occupiedIntervals` by each interval's start. Afterward, when interval `[a,b]` is processed, every interval already in `busy` begins no later than `a`.

The first sorted interval initializes `busy`. Each later interval needs to be compared only with the last merged interval because earlier merged components end even farther left.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"occupiedIntervals": [[1, 5], [2, 3]], "freeStart": 3, "freeEnd": 8}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why touching intervals must merge

Let the last merged component be `[s,e]` and the next sorted interval be `[a,b]`.

For inclusive integer intervals, they are truly separated only when at least one unoccupied integer lies between them. The first integer after `e` is `e+1`, so a gap exists exactly when

$$
e+1<a.
$$

That is the source's condition:



If this inequality is false, the intervals overlap or touch. Their union is one continuous integer interval beginning at `s` and ending at `\max(e,b)`. The source extends the existing endpoint accordingly.

Examples clarify the `+1`:

- `[1,3]` and `[4,7]` touch because four is immediately after three, so they merge to `[1,7]`;
- `[1,3]` and `[5,7]` leave integer four uncovered, so they remain separate.

After the loop, `busy` is sorted, non-overlapping, non-touching, and maximal. No two entries can be combined without incorrectly adding an unoccupied point.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Let the last merged component be `[s,e]` and the next sorted... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Subtracting the free interval

Take one merged occupied interval `[s,e]`. There are two broad cases.

If it is entirely outside the free interval, meaning

$$
e<freeStart
\quad\text{or}\quad
freeEnd<s,
$$

no occupied point is removed. The entire interval is appended to the answer.

Otherwise the intervals overlap. Removing all points from `[freeStart,freeEnd]` can leave up to two pieces:

- a left piece `[s,freeStart-1]` when `s<freeStart`;
- a right piece `[freeEnd+1,e]` when `e>freeEnd`.

The strict comparisons ensure that an emitted piece is nonempty. If `s=freeStart`, there is no point before the free interval inside this component. If `e=freeEnd`, there is no point after it.

The source expresses those two pieces directly:



The `-1` and `+1` are required because endpoints are inclusive. The free endpoints themselves must not remain occupied.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[1, 2]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"occupiedIntervals": [[1, 5], [2, 3]], "freeStart": 3, "freeEnd": 8}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[1, 2]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate every occupied integer:** Endpoint v:** - **Enumerate every occupied integer:** Endpoint values can span up to `10^9`, so point-by-point sets are infeasible. Interval arithmetic depends only on the number of intervals.
- **- **Subtract before merging:** This can produce ov:** - **Subtract before merging:** This can produce overlapping or touching fragments from different inputs and requires another merge anyway. Merging first yields canonical components.
- **- **Merge overlaps but not touching intervals:** T:** - **Merge overlaps but not touching intervals:** That would return more intervals than necessary under the problem's integer-touch definition. The `end+1` comparison is essential.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let `n` be the number of occupied intervals. Sorting dominates with `O(n\log n)` time. The merge scan and subtraction scan are each linear, so total time is `O(n\log n)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
