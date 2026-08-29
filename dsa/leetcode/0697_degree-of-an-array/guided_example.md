# Guided Example: Degree of an Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 2, 3, 1]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a non-empty array of non-negative integers `nums`, the **degree** of this array is defined as the maximum frequency of any one of its elements.

The objective is to compute `2` from `{"nums": [1, 2, 2, 3, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Computing frequencies and the degree

`cnt = Counter(nums)` maps each value to its number of occurrences.

Because the input array is nonempty, `cnt.most_common()` returns at least one entry. Its first entry has a maximum frequency, and

`degree = cnt.most_common()[0][1]`

extracts that frequency.

Only the number is needed; it does not matter which value appears first among values tied for maximum frequency.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 2, 3, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Recording first and last positions

The dictionaries `left` and `right` are populated in one left-to-right pass.

When value `v` appears at index `i`:

- if `v` is not in `left`, `left[v] = i` records its first occurrence;
- `right[v] = i` always runs, so after the pass it records the most recent and therefore final occurrence.

Never overwriting `left[v]` is essential. Always overwriting `right[v]` is equally essential. Together, they identify the narrowest interval that contains every occurrence of `v` in the full array.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why a degree-preserving subarray must focus on a degree value

Let the full-array degree be `d`. No value appears more than `d` times anywhere in the array, so no subarray can have degree above `d`.

For a subarray to have degree exactly `d`, some value must occur `d` times inside it. That value also occurs at least `d` times in the full array, and because `d` is the maximum, its full count must equal `d`.

Therefore, every valid answer is associated with at least one value satisfying `cnt[v] == degree`. Values with smaller total counts can never make a subarray reach the full degree and need not be candidates.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 2, 3, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **One-pass combined records:** Store `count`, `first`, and `last` together while scanning, update the degree, then inspect unique records. This achieves `O(N)` expected time without sorting Counter entries.
- **Use `max(cnt.values())`:** This is a minimal change that avoids the `O(U\log U)` full `most_common()` ordering.
- **Sliding window:** A window could search for the shortest range with degree `d`, but first/last positions give the answer more directly.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `N` be the array length and `U` the number of distinct values.
- **Auxiliary Space Complexity:** $O(U)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
