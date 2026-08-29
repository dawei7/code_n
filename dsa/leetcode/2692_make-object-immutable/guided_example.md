# Guided Example: Make Object Immutable

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"obj": {"x": 5}, "action": {"type": "set", "path": ["x"], "value": 5}}`
- **Required output:** `{"value": null, "error": "Error Modifying: x"}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Write a function that takes an object `obj` and returns a new **immutable** version of this object.

The objective is to compute `{"value": null, "error": "Error Modifying: x"}` from `{"obj": {"x": 5}, "action": {"type": "set", "path": ["x"], "value": 5}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Wrap access rather than cloning the JSON value

The function returns a Proxy around the supplied object or array. The proxy forwards reads but intercepts mutation attempts and throws the exact required string.

Nested objects are wrapped lazily when accessed. This provides deep protection without traversing the entire JSON structure at creation time.

The underlying value remains the proxy's target; the solution does not deep-clone or eagerly freeze it.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"obj": {"x": 5}, "action": {"type": "set", "path": ["x"], "value": 5}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Recognize values that need wrapping

Helper `wrap(value)` returns `null` and primitive values directly.

Only non-null objects can contain writable JSON properties. Arrays also satisfy `typeof value === "object"`, so both objects and arrays enter the proxy path.

Functions obtained from normal property reads are not wrapped by this helper because their type is `"function"`. Mutating array methods are handled specially before that general read.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Cache one proxy per target

`proxies` is a `WeakMap` from an underlying object or array to the proxy already created for it.

Before creating a proxy, `wrap` checks this map. Reusing a cached proxy has two benefits:

- repeated access to the same nested value returns stable proxy identity;
- shared references do not create an unbounded series of wrappers.

JSON input has no cycles, but the same mechanism would also prevent recursive wrapping from duplicating proxy identity for repeated references. Weak keys do not by themselves keep discarded targets alive.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"value": null, "error": "Error Modifying: x"}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"obj": {"x": 5}, "action": {"type": "set", "path": ["x"], "value": 5}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"value": null, "error": "Error Modifying: x"}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **`Object.freeze` only at the root:** Shallow freezing leaves nested objects mutable and does not provide the required custom strings.
- **Recursive deep freeze:** Can protect all descendants eagerly but costs a full traversal and still does not naturally classify errors.
- **Deep clone then freeze:** Uses more time and space and changes identity relationships unnecessarily.
- **Assignment to the same value:** Still throws because an attempted modification occurred.
- **Nested assignment:** The get trap supplies a nested proxy, whose set trap throws.
- **Array index assignment:** Uses the index-specific message.
- **Array `length` assignment:** The array target produces an index-category message with property `length`.
- **Listed mutating method:** The replacement function throws the method-category message before mutation.
- **Null value:** Returned directly and cannot expose deeper properties.
- **Repeated nested access:** WeakMap returns the same proxy.
- **Deletion and definition:** Explicit traps prevent these alternate writes.
- **Original external alias:** Direct mutation through the unwrapped original is not prevented by this proxy-only design.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Creating the top-level proxy is $O(1)$. Each ordinary property access, cache lookup, or intercepted operation takes expected $O(1)$ time, excluding whatever read-only method the caller deliberately executes.
- **Auxiliary Space Complexity:** $O(p)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
