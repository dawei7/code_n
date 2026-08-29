# Guided Example: Make Two Arrays Equal by Reversing Subarrays

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"target": [1, 2, 3, 4], "arr": [2, 4, 1, 3]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two integer arrays of equal length `target` and `arr`. In one step, you can select any **non-empty subarray** of `arr` and reverse it. You are allowed to make any number of steps.

The objective is to compute `true` from `{"target": [1, 2, 3, 4], "arr": [2, 4, 1, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

**A reversal preserves the multiset of values.** Reversing a subarray changes positions but never creates, removes, or changes an element. Therefore, if `arr` can become `target`, the two arrays must contain every value with exactly the same frequency.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"target": [1, 2, 3, 4], "arr": [2, 4, 1, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

This necessary condition is also sufficient because a subarray of length two may be reversed. Reversing positions `j - 1` through `j` swaps two adjacent elements. Adjacent swaps can generate any permutation: to place `target[i]` at position `i`, find one matching occurrence at or after `i` and repeatedly swap it left until it reaches that position. Repeating this from left to right constructs `target` whenever all required occurrences exist.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Thus the allowed operations erase every ordering restriction. The question reduces completely to whether the arrays represent the same multiset.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"target": [1, 2, 3, 4], "arr": [2, 4, 1, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Fixed-size frequency array:** Increment counts for `target` and decrement for `arr` across the bounded value domain. This achieves the manifest's `O(n)` time and `O(1)` space.
- **Hash frequency map:** Compare counters in expected `O(n)` time and `O(n)` space. It generalizes beyond bounded values.
- **In-place sorting:** Sorting both input lists in place avoids the two returned copies but mutates caller-owned data and Python sorting still uses implementation workspace.
- **Simulate adjacent reversals:** It can construct an actual transformation but may take quadratic operations. The problem asks only whether transformation is possible.
- **Already equal arrays:** Their sorted forms agree, so the function returns true without needing an operation.
- **Single element:** Equal values return true; unequal values return false.
- **Same distinct values but different counts:** Sorted sequences differ, correctly returning false.
- **Many duplicates:** Sorting and equality preserve every occurrence, so duplicates cause no ambiguity.
- **Different order only:** Equal multisets sort identically and are reachable through adjacent swaps.
- **A missing target value:** No reversal can create it, and sorted comparison exposes the difference.
- **Equal-length guarantee:** It is given. If lengths differed, sorted lists would also compare unequal.
- **Nonempty subarray:** Length-two subarrays are legal, enabling adjacent swaps. Length-one reversals do nothing but do not restrict reachability.
- **Unlimited operations:** Sufficiency relies on being allowed enough adjacent swaps; there is no operation-count limit.
- **Input preservation:** `sorted` leaves both original arrays unchanged.
- **Complexity reporting:** Use `O(n log n)` time and `O(n)` space for this source, not the fixed-domain counting bounds.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the common array length. Sorting each list takes `O(n log n)` worst-case time, and comparing the resulting lists takes `O(n)`. Total time is `O(n log n)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
