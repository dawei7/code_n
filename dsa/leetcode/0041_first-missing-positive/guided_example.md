# Guided Example: First Missing Positive

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 0]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an unsorted integer array `nums`. Return the *smallest positive integer* that is *not present* in `nums`.

The objective is to compute `3` from `{"nums": [1, 2, 0]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: First narrow the only range that can contain the answer

Let $n$ be the array length. The smallest missing positive must lie between $1$ and $n + 1$. To see why, imagine that every number from $1$ through $n$ is present. Those $n$ distinct positive values already occupy all $n$ array positions, so the next missing positive is $n + 1$. Otherwise, at least one value in $[1,n]$ is absent, and the smallest absent value lies inside that range.

This observation makes negative numbers, zero, and values greater than $n$ irrelevant to the answer. They can remain in the array as unusable occupants. The algorithm only needs a constant-space way to record which values from $1$ through $n$ occur.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 0]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use each array index as a value's home

Instead of allocating a set, the solution rearranges the input. Value `1` belongs at index 0, value `2` at index 1, and in general value `v` belongs at index `v - 1`. After all possible placements, inspecting index `i` answers whether value `i + 1` was present: if it was present, one copy can occupy its home.

This is a cycle-placement or cyclic-sort idea, but the goal is not to sort arbitrary integers. Only in-range positive values have meaningful homes. An array such as `[100, -4, 1]` does not need to become globally ordered; the useful value `1` only needs to move to index 0.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Instead of allocating a set, the solution rearranges the inp... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why each index uses a `while`, not a single `if`

At index `i`, the code examines `nums[i]`. If it is an in-range value `v` and its home does not already contain `v`, the value is swapped into index `v - 1`. That swap brings some other value back into index `i`. The incoming value may also have a valid but different home, so the same index must be reconsidered. A `while` follows this chain until the current occupant is out of range, is already in its home, or is a duplicate whose home already contains the same value.

For `[3, 4, -1, 1]`, index 0 initially contains `3`, so it swaps with index 2 and leaves `3` at its home. Index 0 now contains `-1`, which is ignored. At index 1, `4` moves to index 3; the incoming `1` then moves to index 0. The resulting useful arrangement begins `[1, -1, 3, 4]`. The first index whose expected value is absent is index 1, so the answer is 2.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 0]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Hash set:** Insert every positive value, then :** - **Hash set:** Insert every positive value, then test `1, 2, 3, ...`. This is simple and linear-time on average, but it uses $O(n)$ extra space and misses the constant-space requirement.
- **Boolean presence array:** Mark indices for values in $[1,n]$ and scan for the first unmarked entry. It makes the home-index idea explicit but still allocates $O(n)$ auxiliary memory.
- **Sign marking:** After normalizing unusable values, use the sign at index `v - 1` to mark value `v` present. This also achieves $O(n)$ time and $O(1)$ space, but requires care with repeated values and absolute values.
- **Sorting normally:** Sorting followed by a scan is straightforward and can be in place, but comparison sorting costs $O(n \log n)$ time.
- **Value `1` missing:** Index 0 will not contain `1` after placement, so the second pass immediately returns 1, regardless of large or negative values elsewhere.
- **All values `1` through `n` present:** Every home is correct and the algorithm returns `n + 1`.
- **Duplicates:** Once one copy occupies its home, the guard leaves additional copies alone. They neither cause an infinite loop nor generate false presence information.
- **Negative, zero, and oversized values:** The range condition ignores them safely. They do not need to be deleted or replaced.
- **A value already in place:** If `nums[i] == i + 1`, its computed destination is the same index and the equality guard prevents a pointless self-swap.
- **Input mutation:** The final order generally differs from the original. This is the tradeoff that supplies constant auxiliary space; callers needing the original order must pass a copy, which would itself use $O(n)$ space.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. The two explicit `for` loops each visit $n$ indices. Although a `while` is nested inside the first loop, it does not create quadratic work. Every successful swap permanently places an in-range value into its correct home without dislodging another correctly homed value. There are only $n$ homes, so at most $n$ such progress-making swaps occur across the entire pass. The total time is therefore $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
