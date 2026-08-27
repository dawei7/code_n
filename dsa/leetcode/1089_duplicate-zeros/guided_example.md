# Guided Example: Duplicate Zeros

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": [1, 0, 2, 3, 0, 4, 5, 0]}`
- **Required output:** `[1, 0, 0, 2, 3, 0, 0, 4]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a fixed-length integer array `arr`, duplicate each occurrence of zero, shifting the remaining elements to the right.

The objective is to compute `[1, 0, 0, 2, 3, 0, 0, 4]` from `{"arr": [1, 0, 2, 3, 0, 4, 5, 0]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why ordinary left-to-right writing destroys unread data

Duplicating a zero shifts every later logical element one position farther right. If the algorithm writes those shifted values from left to right inside the same fixed array, a newly written duplicate can overwrite an original value before that value has been read. An extra output array would avoid the problem, but the contract requires an in-place modification with constant auxiliary space.

The safe direction for the actual copy is therefore right to left. Before that copy can begin, the algorithm must determine which original element is the last one that contributes to the fixed-length result. Some original suffix elements are pushed beyond the array and must never be copied.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": [1, 0, 2, 3, 0, 4, 5, 0]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Measure the virtual expanded length

The first loop uses two conceptual positions. `i` is an index in the original array, initially before the first element at `-1`. The value `k` is how many positions the examined source prefix would occupy after zero duplication.

Each iteration advances `i` to the next source element. A nonzero occupies one destination position, so it adds one to `k`. A zero occupies two positions, so the conditional expression adds two. The loop continues while the virtual length is smaller than the real length `n`.

When it stops, `i` points to the last source element that contributes at least one copy to the result. Because an iteration adds only one or two, `k` can finish in only two states:

- `k == n` means the source prefix fits the destination exactly.
- `k == n + 1` means the last processed item was a zero whose first copy fits but whose duplicate would fall one position beyond the boundary.

It cannot overshoot by more than one, and a nonzero cannot cause the overshoot because it increases `k` by only one.

For `[1,0,2,3,0,4,5,0]`, virtual positions grow by one for nonzeros and two for zeros. The scan stops once the prefix through `4` accounts for all eight output slots. Original values `5` and the final zero are outside the source prefix that survives after shifting.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The first loop uses two conceptual positions.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Handle a half-fitting boundary zero

The second state is the subtle edge case. If `k == n + 1`, the zero at source index `i` has room for only one copy at the final destination index `j = n - 1`. The code writes that zero directly to `arr[j]`. It then decrements both `i` and `j`, excluding the already handled source zero and filled destination slot from the backward copy.

Without this adjustment, the general zero-copy logic would try to write two zeros even though only one destination slot remains. It could use an invalid or unrelated index and misalign the rest of the array.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 0, 0, 2, 3, 0, 0, 4]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": [1, 0, 2, 3, 0, 4, 5, 0]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 0, 0, 2, 3, 0, 0, 4]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Extra output array:** Simulate duplication fro:** - **Extra output array:** Simulate duplication from left to right into a new list and copy its first $n$ values back. This is easy to reason about but uses $O(n)$ extra space and misses the in-place objective.
- **Repeated insertion and deletion:** Insert a zero next to every zero and trim the end. Python list insertion shifts many elements, so the worst-case time becomes $O(n^2)$ even if the final length is restored.
- **Count duplicable zeros explicitly:** The editorial formulation counts how many duplicates fit and then uses an offset during a backward pass. It is equivalent to tracking the virtual destination length used here.
- **No zeros:** The first scan advances one virtual position per source element, and the backward loop copies every value onto itself. The array remains unchanged.
- **All zeros:** Only the prefix needed to fill $n$ virtual slots is considered. Backward writes still leave every array position zero.
- **Length one with zero:** The forward scan overshoots to two, the boundary case writes the sole zero, and both indices move before the general loop.
- **Length one with nonzero:** The virtual length reaches one exactly, and the backward pass copies that single value.
- **Boundary zero with only one slot:** This is exactly the `k == n + 1` case. Only one zero is written because its duplicate would be truncated.
- **Zero with two available slots:** The general backward branch writes two copies, and at that point `j` is at least one, so `j - 1` is a valid destination.
- **Values after the surviving prefix:** They are intentionally discarded because duplication of earlier zeros shifts them beyond the fixed array boundary.
- **Input mutation:** Callers must inspect the original list after the method returns. Assigning the return value is incorrect because the method deliberately returns `null`.
- **Compact loop condition:** `while ~j` is valid Python but less readable than `while j >= 0`. Both have identical behavior for the integer index used here.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the fixed array length. The virtual-length scan advances `i` at most $n$ times. The backward copy decreases `j` on every iteration and sometimes twice for a zero, so it performs at most $n$ destination writes up to constant factors. The two sequential passes therefore take $O(n)$ time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
