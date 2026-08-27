# Guided Example: Undefined to Null

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"value": {"a": 0, "b": 3}, "undefinedPaths": [["a"]], "objectPlan": null}`
- **Required output:** `{"a": null, "b": 3}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a deeply nested object or array `obj`, return the object `obj` with any `undefined` values replaced by `null`.

The objective is to compute `{"a": null, "b": 3}` from `{"value": {"a": 0, "b": 3}, "undefinedPaths": [["a"]], "objectPlan": null}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Traverse containers, replace leaf values in place

The input is a nested arrangement of objects and arrays. Any property or array element whose value is exactly JavaScript `undefined` must become `null`. The exact solution performs an iterative depth-first traversal with an explicit `stack`.

The stack initially contains the root `obj`. Each loop iteration pops one container, inspects all of its own enumerable string-keyed properties with `Object.keys(current)`, replaces direct undefined values, and schedules nested non-null objects for later inspection.

The same mechanism works for both plain objects and arrays because arrays are JavaScript objects and their present elements appear as enumerable keys such as `"0"`, `"1"`, and so on.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"value": {"a": 0, "b": 3}, "undefinedPaths": [["a"]], "objectPlan": null}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why an explicit stack is useful

Nested data naturally suggests recursion, but a deeply nested object can exceed JavaScript's function call-stack limit. The explicit array stores pending containers on the heap and keeps the function's own call depth constant.

Traversal order does not affect the result. Because `stack.pop()` uses last-in, first-out order, the code behaves like depth-first search, but breadth-first search would replace exactly the same values. What matters is that every reachable container is eventually inspected.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Nested data naturally suggests recursion, but a deeply neste... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Inspect the current value before deciding to descend

For each key, the code reads `const value = current[key]` once.

- If `value === undefined`, it assigns `current[key] = null`.
- Otherwise, if `value !== null && typeof value === "object"`, it pushes that nested container.
- All other primitive values are left unchanged.

The order of these conditions is significant. `undefined` must be replaced rather than ignored. Also, JavaScript historically reports `typeof null` as `"object"`, so the explicit `value !== null` guard is necessary. Pushing `null` would later cause `Object.keys(null)` to throw.

Strings, numbers, booleans, and other non-object primitives contain no nested properties relevant to this JSON-like input and require no action.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"a": null, "b": 3}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"value": {"a": 0, "b": 3}, "undefinedPaths": [["a"]], "objectPlan": null}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"a": null, "b": 3}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Recursive deep copy:** Recursively map arrays :** - **Recursive deep copy:** Recursively map arrays and rebuild objects for concise immutable-style code, but it allocates `O(n)` output and may overflow the call stack on deep input.
- **Recursive in-place traversal:** It preserves identity like the exact method but uses call-stack space proportional to nesting depth.
- **JSON stringify/parse round trip:** A replacer can sometimes convert undefined values, but serialization has special rules, loses object identity, and is unnecessary for direct traversal.
- **Existing `null`:** The explicit guard leaves it unchanged and prevents `Object.keys(null)` from throwing.
- **Explicit undefined array entry:** It appears in `Object.keys` and is assigned null at the same index.
- **Sparse array hole:** A hole is not an own key, so the exact implementation leaves it sparse. The contract and examples concern explicit undefined values.
- **Empty object or array:** `Object.keys` returns an empty list; the container is popped and returned unchanged.
- **Deep nesting:** The explicit stack avoids recursive call-stack overflow.
- **Wide root object:** Many child containers can be pending simultaneously, producing the `O(n)` stack bound.
- **Circular reference outside the contract:** Without a visited set, traversal would not terminate.
- **Shared acyclic child outside ordinary JSON trees:** It may be inspected more than once, but replacements remain correct because setting undefined to null is idempotent.
- **Inherited property:** `Object.keys` excludes it, which is appropriate because inherited data is not an own JSON property.
- **Symbol or non-enumerable property:** It is not visited by this exact implementation and is outside the stated JSON data model.
- **Root identity:** The returned object is strictly the original `obj` after mutation, not a clone.
- **Primitive nested value:** It is neither undefined nor a non-null object, so it remains unchanged.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the total number of own enumerable properties and present array elements across the JSON-like structure. Every container is popped once in the ordinary tree-shaped input, and every key is inspected once. `Object.keys` itself produces a list proportional to the current container's key count; summed across all containers, time is `O(n)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
