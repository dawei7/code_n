# Guided Example: Differences Between Two Objects

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"obj1": {}, "obj2": {"a": 1, "b": 2}}`
- **Required output:** `{}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Write a function that accepts two deeply nested objects or arrays `obj1` and `obj2` and returns a new object representing their differences.

The objective is to compute `{}` from `{"obj1": {}, "obj2": {"a": 1, "b": 2}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A difference can be a leaf pair or a nested object

The recursive function returns one of two shapes:

- `{}` when there is no reportable difference;
- `[obj1, obj2]` when the two current values differ as leaves or incompatible container types;
- an object whose keys contain deeper differences when both values are comparable containers.

Using an empty object as the “no difference” marker makes it possible for a parent to prune unchanged children uniformly.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"obj1": {}, "obj2": {"a": 1, "b": 2}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Stop immediately for strict equality

The first test is `obj1 === obj2`.

For JSON primitives, this recognizes equal numbers, strings, Booleans, and null. It also recognizes the same object reference, although separately parsed equal containers usually have different identities.

An equal value contributes nothing to the output, so the function returns `{}` without descending.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Decide whether recursive comparison is meaningful

A value is treated as a container only when it is non-null and has JavaScript type `"object"`.

The explicit null test is necessary because `typeof null` is historically `"object"` even though null has no keys to traverse.

If either value is not a container, strict equality has already failed, so the correct leaf difference is `[obj1, obj2]`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"obj1": {}, "obj2": {"a": 1, "b": 2}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Serialize and compare whole objects:** Detects equality but does not produce the required nested changed paths and is sensitive to key order.
- **Iterative stack traversal:** Avoids recursion depth while preserving shared-key semantics.
- **Include union of keys:** Would report additions and removals, which the problem explicitly excludes.
- **Equal primitives:** Return no difference.
- **Null versus value:** Return a direct two-element difference array.
- **Array versus object:** Return a direct difference rather than comparing keys.
- **Different array lengths:** Extra indices on either side are ignored.
- **Empty containers:** Two empty containers of the same kind produce `{}`.
- **Different key order:** Has no effect because comparison is by key.
- **Same object reference:** Strict-equality shortcut avoids traversal.
- **Sparse output:** Array-index changes are stored in an object, not padded array.
- **Input preservation:** The function creates new result containers and never mutates either input.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the total number of keys and array indices visited across comparable shared structure. Each is processed once with expected constant-time property lookup, so time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
