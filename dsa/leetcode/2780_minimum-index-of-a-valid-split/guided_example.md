# Guided Example: Minimum Index of a Valid Split

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 2, 2]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

An element `x` of an integer array `arr` of length `m` is **dominant** if **more than half** the elements of `arr` have a value of `x`.

The objective is to compute `2` from `{"nums": [1, 2, 2, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Only the whole-array dominant value can dominate both halves

Suppose a valid split has left length `L` and right length `R`, and value `x` is dominant in both. It occurs more than `L / 2` times on the left and more than `R / 2` times on the right. Adding those counts shows it occurs more than

$$
\frac{L+R}{2} = \frac{n}{2}
$$

times overall. Therefore `x` must be the unique dominant element already guaranteed for `nums`.

This reduces the task from tracking every value on both sides to tracking one value and its counts.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 2, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Find that value and its total frequency

The exact solution constructs `Counter(nums)` and calls `most_common(1)[0]`. This returns a pair:

- `x`, the most frequent value;
- `cnt`, its total number of occurrences.

Because the contract guarantees exactly one dominant value, the most frequent key is unambiguous and is the only candidate that can satisfy a valid split.

This differs from the manifest description, which names Boyer–Moore voting and constant auxiliary space. The exact source uses a full frequency table.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The exact solution constructs `Counter(nums)` and calls `mos... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Scan split boundaries from left to right

`enumerate(nums, 1)` gives `i` as the current prefix length rather than a zero-based index. After consuming that element:

- the left side has length `i`;
- the right side has length `len(nums) - i`;
- `cur` is the number of `x` values in the left side;
- `cnt - cur` is the number in the right side.

The strict dominance tests are:

`cur * 2 > i`

and

`(cnt - cur) * 2 > len(nums) - i`.

Multiplying by two keeps the comparison integral and exactly expresses “more than half.” Equality is not enough.

When both hold, the split after a prefix of length `i` has zero-based split index `i - 1`, which the code returns. Because boundaries are scanned in increasing order, the first returned index is the minimum.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 2, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Boyer–Moore majority vote:** It identifies the:** - **Boyer–Moore majority vote:** It identifies the guaranteed dominant value in `O(n)` time and `O(1)` space, followed by a count and split scan. This matches the manifest but is not the exact code.
- **Two frequency maps:** Moving values from a suffix map to a prefix map works but tracks far more information than the single dominant candidate needs.
- **Check every boundary:** It is still `O(n)` and avoids the surplus proof for guarded checking. The exact code tests only after occurrences of `x`.
- **Strict majority:** Counts exactly equal to half fail because both comparisons use `>` rather than `>=`.
- **One-element array:** No nonempty two-way split exists. The final empty-suffix test fails and the method returns `-1`.
- **Dominant value at the first position:** Index zero is returned only if the remaining suffix also keeps that value dominant.
- **Valid split near the end:** The suffix may contain one dominant value, which is automatically a strict majority of a one-element side.
- **Empty suffix after the final element:** Its `0 > 0` test is false, preventing an out-of-range split.
- **Large element values:** Counter keys handle them directly; no value-indexed array is allocated.
- **Unique dominant guarantee:** The code does not need to verify the Counter winner exceeds half, because the contract proves it.
- **No valid split:** The total array can have a dominant element while every proper boundary fails on at least one side, producing `-1`.
- **Manifest mismatch:** Actual storage is linear in distinct values, not constant, because `Counter(nums)` is part of the exact source.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the array length and `u` the number of distinct values. Building the Counter takes `O(n)` expected time and stores `u` entries. Finding its most common entry costs `O(u)` for one requested item. The boundary scan is another `O(n)` pass. Total expected time is `O(n)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
