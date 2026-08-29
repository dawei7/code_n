# Guided Example: Partition Array Into K-Distinct Groups

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3, 4], "k": 2}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` and an integer `k`.

The objective is to compute `true` from `{"nums": [1, 2, 3, 4], "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Determine how many groups must exist

Every group must contain exactly `k` elements, and every input occurrence must be used exactly once. If `n = len(nums)`, the number of groups is forced to be

`m = n / k`.

This must be an integer. The source computes

`m, mod = divmod(n, k)`.

If `mod` is nonzero, some elements would remain after forming all full size-`k` groups, so a valid partition is impossible.

Passing this divisibility test fixes both dimensions of the desired arrangement: there are `m` groups, each with `k` slots, for exactly `mk = n` total slots.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3, 4], "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: A repeated value can appear at most once per group

All entries within one group must be distinct. If a value `x` occurs `f` times in `nums`, its copies must be assigned to `f` different groups.

There are only `m` groups, so a necessary condition is

`f <= m`

for every distinct value. Equivalently, the maximum frequency in the array must not exceed the number of groups.

The source obtains all frequencies with `Counter(nums)` and checks

`max(Counter(nums).values()) <= m`.

This detects the only remaining obstruction after divisibility.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the frequency bound is also sufficient

It is easy to see why too many copies fail, but the important part is proving that no more complicated conflict can occur.

Imagine listing equal values together in blocks. Distribute the occurrences cyclically among group zero, group one, ..., group `m - 1`, then wrap around and continue with the next value block.

Each value block has length at most `m` because of the frequency condition. Therefore, its occurrences land in distinct groups before the cycle could revisit a group. No group receives the same value twice.

Across all value blocks, exactly `n = mk` occurrences are distributed round-robin over `m` groups. Every full cycle gives one element to each group, and there are exactly `k` complete cycles in total. Consequently, every group receives exactly `k` elements.

This construction proves that divisibility plus the maximum-frequency bound is sufficient. The source does not need to construct the groups because the requested output is only a Boolean.

Another formal view is a bipartite assignment between distinct values and groups. A value with frequency `f` requests `f` different group neighbors, every group has capacity `k`, and the complete value-to-group availability together with `f <= m` and total demand `mk` guarantees a full assignment.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3, 4], "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Construct groups greedily with a heap:** Repeatedly choose distinct high-frequency values for each group. This can work but costs `O(n log d)` and is unnecessary once the sufficiency condition is known.
- **Round-robin construction:** It provides a witness in `O(n)` after grouping equal values, but the source needs only the feasibility test.
- **Check only `n % k == 0`:** Divisibility does not prevent one value from occurring more times than there are groups.
- **Check only the number of distinct values:** It misses excessive multiplicity and is not sufficient by itself.
- **Maximum frequency exactly `m`:** This is valid; that value appears once in every group.
- **Maximum frequency greater than `m`:** At least one group would need two copies of the same value, violating distinctness.
- **`k = 1`:** Every element forms a one-element group, which is automatically distinct. Here `m = n` and every frequency is at most `n`.
- **`k = n`:** There is one group, so every value must occur at most once; the condition becomes “the whole array is distinct.”
- **All values equal:** A partition is possible only when `k = 1`. For larger groups, the frequency exceeds the number of groups.
- **Array length not divisible by `k`:** Return false immediately without building a counter.
- **Duplicate occurrences are separate elements:** Every occurrence must be assigned, but copies of one value must go to different groups.
- **Input preservation:** `Counter` reads `nums` without sorting or modifying it.
- **Missing imports:** The stored source uses `List` and `Counter` without importing them. Standalone Python requires imports from `typing` and `collections` unless provided by the harness.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the number of elements and `d` the number of distinct values.
- **Auxiliary Space Complexity:** $O(d)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
