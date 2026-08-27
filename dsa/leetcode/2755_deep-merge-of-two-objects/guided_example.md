# Guided Example: Deep Merge of Two Objects

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"obj1": {"a": 1, "c": 3}, "obj2": {"a": 2, "b": 2}}`
- **Required output:** `{"a": 2, "c": 3, "b": 2}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two values `obj1` and `obj2`, return a **deepmerged** value.

The objective is to compute `{"a": 2, "c": 3, "b": 2}` from `{"obj1": {"a": 1, "c": 3}, "obj2": {"a": 2, "b": 2}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: First decide whether recursive merging is allowed

Recursive merging happens only when both current values are non-null objects and both are the same container kind: either both arrays or both non-array objects.

The code computes object flags explicitly because JavaScript reports `typeof null === "object"` even though null must behave like a primitive replacement value here.

If either value is primitive or null, or one is an array while the other is an object, the function returns `obj2` immediately. This implements the rule that incompatible or non-container pairs are replaced by the second value.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"obj1": {"a": 1, "c": 3}, "obj2": {"a": 2, "b": 2}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Create a new top-level container from obj1

For compatible arrays, `[...obj1]` shallowly copies the first array. For compatible objects, `{ ...obj1 }` shallowly copies its enumerable own properties.

This establishes every key or index that exists only in `obj1`. Such entries remain in the result unless `obj2` has the same key.

The top-level compatible container is not mutated in place; a new result container is returned.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For compatible arrays, `[...obj1]` shallowly copies the firs... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Traverse keys from obj2

`Object.keys(obj2)` lists its enumerable own string keys. For a JSON object, these are its properties. For a JSON array, they are its existing numeric index strings.

Each key from `obj2` must appear in the result. The only question is whether to merge it with a corresponding `obj1` value or copy it as a new key.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"a": 2, "c": 3, "b": 2}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"obj1": {"a": 1, "c": 3}, "obj2": {"a": 2, "b": 2}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"a": 2, "c": 3, "b": 2}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Mutate obj1 in place:** Uses fewer new contain:** - **Mutate obj1 in place:** Uses fewer new containers but changes caller-owned input and differs from this source.
- **JSON serialization clone:** Loses the recursive override logic and performs unnecessary copying.
- **Array versus object:** Types are incompatible, so the entire second value replaces the first.
- **Null:** Explicitly treated as a replacement value, not a mergeable object.
- **Primitive conflict:** Always choose `obj2`, even when the primitive values have different types.
- **Key only in obj1:** Preserved by the initial shallow copy.
- **Key only in obj2:** Added directly and may share a nested reference.
- **Different array lengths:** Overlapping indices merge and the longer tail survives.
- **Deep nesting:** Correct recursively but may approach JavaScript call-stack limits.
- **Reference independence:** Only overlapping compatible container paths are newly copied; unique nested objects are shared.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the total number of keys, indices, and primitive values visited across both structures. Shallow copies enumerate first-container keys at every compatible recursive level, and `Object.keys` enumerates second-container keys. Each visited property performs constant expected work, so total time is $O(N)$, commonly written $O(n+m)$ for the two input sizes.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
