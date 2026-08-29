# Guided Example: Kth Distinct String in an Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": ["d", "b", "c", "b", "c", "a"], "k": 2}`
- **Required output:** `"a"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A **distinct string** is a string that is present only **once** in an array.

The objective is to compute `"a"` from `{"arr": ["d", "b", "c", "b", "c", "a"], "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Distinct means global frequency exactly one

A string is not distinct merely because it differs from its immediate neighbors. It must occur exactly once in the entire array.

The source begins with `cnt = Counter(arr)`. This scans all array entries and maps each string value to its total occurrence count.

Duplicates are recorded regardless of how far apart their occurrences are.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": ["d", "b", "c", "b", "c", "a"], "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Make a second pass to preserve original order

A frequency map identifies which values are distinct, but map iteration order is not the requested ordering rule. The $k$th distinct string is based on positions in `arr`.

The source therefore scans `arr` again from left to right. Whenever `cnt[s] == 1`, the current occurrence is one distinct string in the required sequence.

It decrements `k` for those entries only. When `k` reaches zero, the current `s` is returned.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why duplicate occurrences are skipped

If a value appears twice or more, every occurrence has the same counter value greater than one. null decrements `k`.

This correctly excludes the string value altogether. The task does not ask for the first occurrence of each different value; it asks only for values appearing once.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"a"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": ["d", "b", "c", "b", "c", "a"], "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"a"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Two sets:** Move values from a once-seen set to a duplicate set, then scan the array again.
- **Nested comparisons:** Test every string against every other string, costing $O(N^2)$.
- **Build a distinct list:** Filter after counting and index `k-1`; correct but allocates another list.
- **All strings distinct:** The answer is simply the original $k$th array entry.
- **No distinct strings:** Return the empty string.
- **Exactly `k` distinct strings:** Return the final one encountered.
- **Fewer than `k`:** The scan ends and returns `""`.
- **Separated duplicates:** Counter still excludes all occurrences.
- **Repeated string many times:** It remains one map key with a larger count.
- **Original order:** The second array scan, not counter order, determines rank.
- **One-element array:** Its only nonempty string is the first distinct.
- **Input preservation:** `arr` is read twice but never changed.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S)$. Let $N$ be the number of strings and $S$ their total character count. Building the counter takes expected $O(S)$ time when string hashing is included, and the second pass takes expected $O(S)$ worst-case character work for lookups. With maximum string length treated as constant, this is $O(N)$.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
