# Guided Example: Array Upper Bound

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [3, 4, 5], "target": 5}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Write code that enhances all arrays such that you can call the `upperBound()` method on any array and it will return the last index of a given `target` number. `nums` is a sorted ascending array of numbers that may contain duplicates. If the `target` number is not found in the array, return `-1`.

The objective is to compute `2` from `{"nums": [3, 4, 5], "target": 5}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Search for a boundary, not merely for an equal element

The array is sorted in ascending order and may contain duplicates. An ordinary binary search that returns as soon as it sees `target` could return any occurrence. The required answer is the last occurrence.

The exact method instead searches for the first index whose value is strictly greater than `target`. Once that upper boundary is known, the position immediately before it is the last value less than or equal to `target`. A final equality check decides whether that position is actually a target occurrence.

This boundary formulation handles duplicates without maintaining a separate “best match seen so far” variable.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [3, 4, 5], "target": 5}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use a half-open search interval

`left` starts at zero and `right` starts at `this.length`, one position beyond the last valid array index. The active search interval is `[left, right)`: it includes `left` but excludes `right`.

Allowing `right` to equal the length is important. If every array value is at most `target`, then the first value greater than `target` does not exist inside the array; its insertion boundary is naturally `this.length`.

The loop continues while `left < right`. The midpoint

`Math.floor((left + right) / 2)`

is always a valid index in the nonempty half-open interval.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `left` starts at zero and `right` starts at `this.length`, o... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The boundary invariant

The search maintains two facts:

- every index strictly before `left` contains a value less than or equal to `target`;
- every index at or after `right`, when it is an actual array index, contains a value greater than `target`.

Initially both regions are empty, so the statements are trivially true.

At `middle`:

- If `this[middle] <= target`, then sorted order implies every index through `middle` also has a value at most `target`. null can be the first greater value, so set `left = middle + 1`.
- Otherwise `this[middle] > target`. The boundary could be `middle` or somewhere earlier, so set `right = middle` rather than discarding `middle`.

Each update preserves the invariant and strictly shortens the interval.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [3, 4, 5], "target": 5}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Linear scan:** Remembering the last matching i:** - **Linear scan:** Remembering the last matching index is simple but costs `O(n)` and ignores the sorted-order opportunity.
- **Built-in `lastIndexOf`:** It has the desired equality behavior but also scans linearly.
- **Stop at the first equality:** Ordinary binary search may return a middle duplicate rather than the last occurrence.
- **Search for the lower bound:** The first value greater than or equal to target identifies the first occurrence, not the last. Upper bound minus one is the needed boundary.
- **Target smaller than every element:** The upper boundary is zero, candidate is `-1`, and the guard returns `-1` without indexing as a match.
- **Target larger than every element:** The boundary is `n`. The last index is checked and returned only if it equals the target; otherwise absence is reported.
- **All elements equal target:** The boundary advances to `n` and candidate `n - 1` is the correct last occurrence.
- **One-element array:** The method returns zero for a match and `-1` otherwise.
- **Duplicates at the end:** The half-open interval allows the boundary to be `n`, so the last duplicate is found correctly.
- **Target between two values:** Candidate is the smaller neighbor, but the final strict equality check prevents a false match.
- **Empty array outside the stated constraint:** The loop is skipped, candidate is `-1`, and the method still returns `-1` safely.
- **Unsorted receiver:** The monotonic boundary invariant fails, so results are unspecified; sorted ascending order is essential.
- **`NaN` values or target:** JavaScript comparisons with `NaN` are not a normal numerical order. Such values are outside the stated sorted-number contract.
- **Prototype modification:** Adding methods globally can affect enumeration in unrelated code, but the challenge explicitly requests an Array prototype enhancement.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(log n)$. Let `n` be the array length. Each iteration reduces the remaining interval to at most about half its previous size. After `O(log n)` iterations, `left` equals `right`. Each iteration performs constant work, and the final validation is constant time. Total time is `O(log n)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
