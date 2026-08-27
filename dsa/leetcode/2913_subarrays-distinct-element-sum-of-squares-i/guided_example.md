# Guided Example: Subarrays Distinct Element Sum of Squares I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 1]}`
- **Required output:** `15`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed **integer array `nums`.

The objective is to compute `15` from `{"nums": [1, 2, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why the set is the exact state we need

A mathematical set keeps one copy of each value, regardless of how many times that value occurs. Python's `set.add` has the same behavior:

- adding a value that is not present increases `len(s)` by one;
- adding a duplicate leaves `len(s)` unchanged.

This precisely matches the definition of a distinct-element count.

The invariant of the inner loop is:

> Immediately after adding `nums[j]`, `s` equals the set of values occurring from index $i$ through index $j$, inclusive.

It is true at $j=i$ because the formerly empty set receives exactly `nums[i]`. If it is true for $j-1$, adding `nums[j]` extends the represented range by exactly the next element. Whether that element is new or duplicated, the resulting set is exactly the distinct values of the extended subarray. This proves the invariant by induction.

Once the invariant holds, `len(s)` is $\operatorname{distinct}(i,j)$, so squaring it produces the required contribution of this specific subarray.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why every subarray contributes exactly once

The outer loop visits every possible left endpoint $i$. For that fixed $i$, the inner loop visits every possible right endpoint $j\ge i$. Therefore every legal endpoint pair $(i,j)$ is reached.

No pair is repeated: two different loop iterations must differ in $i$, in $j$, or in both. Since a contiguous subarray is uniquely identified by its endpoint pair, its squared distinct count is added exactly once. Summing those contributions gives the requested total.

For example, with `nums = [1, 2, 1]` and $i=0$, the set sizes as $j$ advances are $1,2,2$. The contributions are $1,4,4$. The final $1$ is a duplicate, so it does not raise the distinct count. When $i=1$, a new set is used for subarrays `[2]` and `[2,1]`, producing sizes $1,2$. Finally, $i=2$ contributes the one-element subarray `[1]`. This accounts for all six subarrays.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The outer loop visits every possible left endpoint $i$.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why no frequency map is required

For a fixed $i$, the right endpoint only moves forward. Values are added but never removed from the current subarray. We only need to know whether a value has appeared, not how many times it appears, so a set is sufficient.

A frequency map would become useful in a sliding window where both endpoints move and elements leave the window. That is not the access pattern here. Avoiding unnecessary counts keeps the implementation close to the mathematical quantity.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `15` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `15` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Build every subarray separately:** Slicing eac:** - **Build every subarray separately:** Slicing each `nums[i:j+1]` and converting it to a set takes up to $O(n)$ work per subarray, leading to $O(n^3)$ total time and repeated allocation.
- **Use a frequency dictionary:** This also produces the distinct count but stores counts that never need to be decremented. A set is the smaller and clearer state for a one-directional extension.
- **Advanced contribution aggregation:** The larger version of this problem can update the sum of squared distinct counts for many left endpoints together, often using range data structures. That complexity is unnecessary for the constraints and exact source used here.
- **All elements equal:** Every subarray has exactly one distinct value and contributes $1$. Repeated `set.add` calls correctly leave the size at one.
- **All elements distinct:** A subarray of length $\ell$ has $\ell$ distinct values and contributes $\ell^2$. The set grows by one at every extension.
- **One-element subarrays:** Each outer iteration starts with $j=i$, adds one value, and contributes $1^2$. These subarrays are included naturally.
- **Set reset between left endpoints:** Reusing the old set would retain values lying before the new $i$ and corrupt the invariant. Creating `s = set()` inside the outer loop is essential.
- **No modulo reduction:** This first-version contract asks for the exact sum, and the source solution returns the full Python integer. Adding an unrequested modulo would change correct outputs.
- **Duplicate occurrences:** A duplicate must not increase the distinct count, but it still defines a different endpoint and therefore a different subarray contribution. The algorithm handles both facts simultaneously.
- **Input order matters for subarrays:** A global set of all array values is insufficient because distinct counts depend on the selected contiguous range. The per-left incremental set preserves those boundaries.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. Let $n$ be the number of elements in `nums`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
