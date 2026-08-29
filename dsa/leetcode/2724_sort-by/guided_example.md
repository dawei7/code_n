# Guided Example: Sort By

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": [5, 4, 1, 2, 3], "selector": "identity"}`
- **Required output:** `[1, 2, 3, 4, 5]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array `arr` and a function `fn`, return a sorted array `sortedArr`. You can assume `fn` only returns numbers and those numbers determine the sort order of `sortedArr`. `sortedArr` must be sorted in **ascending order** by `fn` output.

The objective is to compute `[1, 2, 3, 4, 5]` from `{"arr": [5, 4, 1, 2, 3], "selector": "identity"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Sort elements by a derived numeric key

The elements of `arr` may be numbers, objects, or arrays. Their raw representation is not the ordering rule. The supplied function `fn` maps each element to the number that determines where it belongs.

The implementation delegates the reordering to JavaScript's in-place `Array.prototype.sort` and supplies a comparator:

`fn(left) - fn(right)`.

This is the standard numerical ascending comparator applied to derived keys.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": [5, 4, 1, 2, 3], "selector": "identity"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: How a comparator controls the sort

When the sorting engine asks how `left` and `right` should be ordered, the comparator returns:

- a negative number when `fn(left) < fn(right)`, placing `left` earlier;
- a positive number when `fn(left) > fn(right)`, placing `left` later;
- zero when the keys are equal.

The problem guarantees that `fn` does not return duplicate numbers for the given array, so legal comparisons between different elements do not produce a key tie. No secondary tie-breaking rule is required.

Subtraction matters. Calling `sort()` without a comparator would convert values to strings and use lexicographic ordering, which would put values such as ten and two in the wrong numeric relationship.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The elements themselves are preserved

The comparator only reads elements and calculates keys. `sort` moves the original element values or object references; it does not replace each item with its key.

For `arr = [{"x": 1}, {"x": 0}, {"x": -1}]` and `fn = d => d.x`, comparisons use one, zero, and negative one. The returned array still contains the three original objects, ordered as keys negative one, zero, one.

For nested arrays such as `[[3,4],[5,2],[10,1]]` with `fn = x => x[1]`, the second entries one, two, and four determine the order, yielding `[[10,1],[5,2],[3,4]]`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 2, 3, 4, 5]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": [5, 4, 1, 2, 3], "selector": "identity"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 2, 3, 4, 5]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Decorate, sort, undecorate:** Compute `fn` once per element, sort key-element pairs, and strip keys; this helps when `fn` is expensive but allocates $O(n)$ explicit records.
- **Copy before sorting:** `[...arr].sort(...)` preserves the input array at the cost of $O(n)$ additional visible storage.
- **Default `sort()`:** Incorrect for numeric keys because it uses string ordering.
- **Handwritten merge sort:** Gives direct control over stability and storage but adds substantial code without changing the target order.
- **Single element:** No meaningful comparison is needed, and the same one-element array is returned.
- **Unique-key guarantee:** Eliminates ambiguity and the need for a tie-breaker.
- **Objects and nested arrays:** They are valid because `fn` extracts the numeric key while sort moves the original values.
- **Mutation:** Callers holding `arr` observe its new order after the function returns.
- **Expensive `fn`:** Repeated comparator evaluation can dominate the runtime; precomputing keys would then be preferable.
- **Side-effecting `fn`:** Can make comparisons inconsistent and should be avoided even though the contract focuses only on numeric return values.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(Cn\log n)$. Let $n$ be `arr.length` and let $C$ be the cost of one call to `fn`. A comparison sort performs $O(n\log n)$ comparisons in the standard worst-case model, and this comparator invokes `fn` twice per comparison. The time is therefore $O(Cn\log n)$. When `fn` is $O(1)$, this is the manifest's $O(n\log n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
