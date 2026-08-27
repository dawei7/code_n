# Guided Example: Bind Function to Context

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"behavior": "multiply", "obj": {"x": 10}, "inputs": [5]}`
- **Required output:** `50`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Enhance all functions to have the `bindPolyfill` method. When `bindPolyfill` is called with a passed object `obj`, that object becomes the `this` context for the function.

The objective is to compute `50` from `{"behavior": "multiply", "obj": {"x": 10}, "inputs": [5]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Capture the original function

`bindPolyfill` is called as a method of the function being bound. Inside that method, `this` is the target function.

The code saves it in `const target = this`. The returned regular function closes over both `target` and the supplied context object `obj`, so they remain available whenever the bound function is invoked later.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"behavior": "multiply", "obj": {"x": 10}, "inputs": [5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why ordinary method invocation sets this

JavaScript determines a regular function's `this` from its call site. Calling:

`obj[key](...args)`

as a property of `obj` makes `obj` the receiver and therefore the `this` value inside that function.

The solution temporarily installs `target` as such a property, invokes it as a method, and then removes the property.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | JavaScript determines a regular function's `this` from its c... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Use a fresh Symbol key

Every invocation creates `const key = Symbol()`. A Symbol is guaranteed unique, even if another symbol has the same description.

Using a normal string such as `"temp"` could overwrite an existing user property. A fresh symbol cannot collide with any existing string or symbol key unless that exact symbol reference was already used, which is impossible before creation.

Creating the symbol inside the returned function also makes simultaneous or nested calls use independent keys.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `50` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"behavior": "multiply", "obj": {"x": 10}, "inputs": [5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `50` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Function.call:** `target.call(obj, ...args)` i:** - **Function.call:** `target.call(obj, ...args)` is simpler if built-in context-setting methods are allowed.
- **Function.apply:** Naturally accepts the collected argument array but is likewise a built-in helper.
- **Permanent Symbol property:** Sets context correctly but leaves an unnecessary mutation on `obj`.
- **Normal string key:** Risks overwriting user data.
- **No arguments:** The rest array is empty and the target is called with only its bound context.
- **Many arguments:** Spread preserves their order exactly.
- **Target throws:** `finally` deletes the temporary key, then the exception propagates.
- **Target returns a promise:** The promise is returned; deleting the property does not change the already established call context.
- **Nested invocation:** Fresh symbols prevent key collisions.
- **Frozen object:** Temporary assignment may fail; such objects are outside the normal extensible-object assumption.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(a)$. Let $a$ be the number of invocation arguments. Binding itself captures two references and creates one closure in $O(1)$ time and space.
- **Auxiliary Space Complexity:** $O(a)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
