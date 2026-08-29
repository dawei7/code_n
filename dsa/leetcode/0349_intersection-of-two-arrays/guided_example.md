# Guided Example: Intersection of Two Arrays

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums1": [1, 2, 2, 1], "nums2": [2, 2]}`
- **Required output:** `[2]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two integer arrays `nums1` and `nums2`, return *an array of their intersection*. Each element in the result must be **unique** and you may return the result in **any order**.

The objective is to compute `[2]` from `{"nums1": [1, 2, 2, 1], "nums2": [2, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why duplicates disappear without special cases.

Suppose `nums1` contains `[1, 2, 2, 1]`. Inserting the first `1` creates membership for `1`; inserting the later `1` does not create a second copy. The same is true for `2`. Thus `set(nums1)` represents `{1, 2}`. If `nums2` is `[2, 2]`, its set is `{2}`. Their intersection is `{2}`, and converting it to a list produces `[2]`.

No frequency table is needed because the result does not care whether a common value occurs once or a thousand times. It asks only the yes-or-no question “does this value occur in each input?” A set stores exactly that information and no irrelevant multiplicity.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums1": [1, 2, 2, 1], "nums2": [2, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the intersection is correct.

Consider any value `x` that appears in the returned list. It came from the temporary intersection set. By the definition of `&`, `x` can be in that set only if it is a member of both `set(nums1)` and `set(nums2)`. Set construction includes a value exactly when that value appeared in the corresponding array. Therefore every returned value truly appears in both input arrays.

Now consider any distinct value `y` that appears in both arrays. The first set construction includes `y`, and the second set construction also includes `y`. The intersection operator consequently includes `y`, and converting the set to a list retains it. Therefore no required common value is omitted.

Finally, the intermediate result is a set, so it cannot contain duplicate entries. The conversion to a list copies each set member once; it does not reintroduce duplicates. These three facts establish that the returned list contains exactly the distinct common values.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why arbitrary output order is acceptable.

Sets are not used here to preserve the arrays' encounter order. Their iteration order is an implementation detail and should not be treated as sorted order or as a stable part of this algorithm's contract. For the second example, either `[9, 4]` or `[4, 9]` is valid because both describe the same mathematical set. If the judge required a particular order, an extra ordering step or an order-preserving scan would be necessary. This problem explicitly removes that requirement.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums1": [1, 2, 2, 1], "nums2": [2, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **One set from the smaller input:** Store the distinct values of the shorter array, scan the other array, and add matches to a result set or remove each match after output. This can use $O(\min(n,m))$ membership storage plus output, matching the manifest summary, but it is not the checked-in source.
- **Sort and use two pointers:** Sort both arrays, advance the pointer at the smaller value, and emit equal values while skipping duplicates. This avoids hash assumptions but costs $O(n\log n+m\log m)$ time and may mutate the inputs if sorting is done in place.
- **Boolean presence table:** Because values lie from `0` to `1000`, a fixed table can record membership from one array and a second state can prevent duplicate output. It provides deterministic linear scanning time and bounded storage, but it relies on the small value range and generalizes poorly to arbitrary integers.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+m)$. Let $n$ be `len(nums1)`, let $m$ be `len(nums2)`, let $u_1$ and $u_2$ be their respective numbers of distinct values, and let $r$ be the number of distinct values present in both. Then $u_1\le n$, $u_2\le m$, and $r\le\min(u_1,u_2)$.
- **Auxiliary Space Complexity:** $O(u_1+u_2+r)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
