# Guided Example: Deep Object Filter

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"obj": [-5, -4, -3, -2, -1, 0, 1], "predicate": "positive"}`
- **Required output:** `{"defined": true, "value": [1]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an object or an array `obj` and a function `fn`, return a filtered object or array `filteredObject`.

The objective is to compute `{"defined": true, "value": [1]}` from `{"obj": [-5, -4, -3, -2, -1, 0, 1], "predicate": "positive"}` while avoiding redundant calculations and unnecessary overhead.

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

**Filter leaves and rebuild containers from the bottom up.** The input is a JSON object or array whose nested values form a tree. The filter function applies to primitive leaves, not to container objects themselves. A container survives only if at least one descendant survives. This makes depth-first recursion a natural fit: children must be filtered before the parent can decide whether it became empty.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"obj": [-5, -4, -3, -2, -1, 0, 1], "predicate": "positive"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

Each call determines whether its current container is an array with `Array.isArray(obj)`. It creates an empty result of the same container kind: `[]` for an array or `{}` for an object.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Use one local insertion helper for two container semantics.** The nested `add` function captures `isArray` and `filtered`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"defined": true, "value": [1]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"obj": [-5, -4, -3, -2, -1, 0, 1], "predicate": "positive"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"defined": true, "value": [1]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Iterative postorder traversal:** Use an explicit stack with enter/exit markers to process children before parents. This preserves $O(V)$ work and avoids native call-stack overflow at the cost of more bookkeeping.
- **Mutate the input in place:** Deleting rejected object properties and splicing arrays can save output allocations, but it changes caller-owned data and array deletion must be handled carefully to avoid skipped indices.
- **Call `fn` on containers:** That is a different contract. The exact solution filters only primitive leaves, which is why an array predicate does not preserve arrays by itself.
- **Null leaf:** The explicit null guard routes it to `fn` rather than attempting `Object.entries(null)`.
- **Empty input container:** No properties are added, so the top-level result is undefined.
- **Nested container becomes empty:** Its recursive undefined result prevents the parent from retaining an empty placeholder.
- **Array compaction:** Removed entries do not leave holes; surviving values are pushed in original enumeration order.
- **Object key preservation:** Surviving properties retain their names, including special strings handled safely by `defineProperty`.
- **false, zero, and empty string:** They are primitive leaves and may survive if `fn` explicitly returns true; the code tests `fn`'s result, not the leaf's own truthiness.
- **Undefined input outside JSON:** The return sentinel would be ambiguous with a legitimate undefined leaf, which is why the JSON guarantee matters.
- **Deep nesting:** Recursive correctness remains valid, but engine stack limits may require an iterative implementation.
- **Input preservation:** Every surviving container is newly allocated, so structural mutations to the result do not directly mutate the original containers.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(V)$. Let $V$ be the total number of container entries plus primitive leaves in the input tree, and let $D$ be maximum nesting depth. Each entry is visited once by its parent's `Object.entries` loop. Every surviving entry is inserted once.
- **Auxiliary Space Complexity:** $O(V+D)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
