# Guided Example: Compact Object

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"obj": [null, 0, false, 1]}`
- **Required output:** `[1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an object or array `obj`, return a **compact object**.

The objective is to compute `[1]` from `{"obj": [null, 0, false, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Remove falsy children while rebuilding containers

The function recursively creates a new array or object rather than deleting from the input.

At every container, a child is retained only if the child's original value is truthy. Retained nested containers are then compacted recursively.

The distinction between filtering and recursion order is important because an empty object or array is truthy in JavaScript and must remain present even if all of its own children are removed.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"obj": [null, 0, false, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Base case for primitives and null

The first condition is:

`if (!obj || typeof obj !== "object") return obj`.

It returns any falsy value immediately and also returns truthy primitives such as numbers and strings.

Under valid JSON, falsy values include `null`, `false`, zero, and the empty string. `undefined` and `NaN` are not JSON values.

The parent container decides whether a falsy child is retained, so returning it here is safe.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Handle arrays with filter before map

For an array, the exact expression is:

`obj.filter(Boolean).map(compactObject)`.

`filter(Boolean)` removes every element whose Boolean conversion is false. It also packs surviving values into consecutive indices, which is the required array behavior after removals.

`map(compactObject)` then recursively rebuilds every truthy survivor.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"obj": [null, 0, false, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Mutate containers in place:** Can reduce allocations but risks index-shift bugs and violates input preservation.
- **Iterative explicit stack:** Avoids call-stack overflow for extremely deep JSON while keeping $O(n)$ work.
- **Delete empty containers:** Incorrect because empty arrays and objects are truthy.
- **Zero:** Removed wherever it is a child value.
- **false:** Removed even though it is a meaningful Boolean in other applications.
- **Empty string:** Removed because its Boolean conversion is false.
- **Null:** Removed and never traversed.
- **Empty array or object:** Retained because it is truthy.
- **Nested container becomes empty:** Still retained if its original container value was truthy.
- **Array removal:** Survivors shift left into a packed array.
- **Object removal:** Other property names remain unchanged.
- **Valid JSON guarantee:** Excludes functions, symbols, undefined, and cyclic structures.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the total number of array elements and object properties across the JSON structure. Every child is examined once and every retained container is rebuilt once, so total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
