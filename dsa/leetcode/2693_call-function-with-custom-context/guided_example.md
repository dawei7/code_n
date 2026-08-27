# Guided Example: Call Function with Custom Context

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"behavior": "add", "context": {"a": 5}, "args": [7]}`
- **Required output:** `12`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Enhance all functions to have the `callPolyfill` method. The method accepts an object `obj` as its first parameter and any number of additional arguments. The `obj` becomes the `this` context for the function. The additional arguments are passed to the function (that the `callPolyfill` method belongs on).

The objective is to compute `12` from `{"behavior": "add", "context": {"a": 5}, "args": [7]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Add one shared method to all functions

JavaScript function objects inherit from `Function.prototype`. Assigning `callPolyfill` there makes the method available to ordinary functions through prototype lookup.

When code evaluates `fn.callPolyfill(context, ...args)`, the `this` value inside `callPolyfill` is `fn` itself. The implementation can therefore install and invoke the function without receiving it as a separate parameter.

The prototype method is shared rather than recreated for every function object.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"behavior": "add", "context": {"a": 5}, "args": [7]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Create a collision-free temporary property

To make `context` become `this` inside `fn` without using built-in `Function.call`, the solution temporarily makes the function a method of `context`.

It creates `const key = Symbol()`. Every new Symbol is unique, even if another Symbol has the same description.

Using that symbol as a property key guarantees it cannot collide with any existing string key or independently created symbol key on the context object.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | To make `context` become `this` inside `fn` without using bu... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why method-call syntax sets the receiver

JavaScript determines a regular function's dynamic `this` from the call form.

After:

`context[key] = this`,

the expression:

`context[key](...args)`

is a method call whose base object is `context`. JavaScript therefore invokes the stored function with `this === context`.

This reproduces the central behavior of `call` without invoking the forbidden built-in method.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `12` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"behavior": "add", "context": {"a": 5}, "args": [7]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `12` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Built-in `call`:** Directly solves context bin:** - **Built-in `call`:** Directly solves context binding but is explicitly forbidden.
- **Built-in `apply`:** Could pass the argument array and context, but bypasses the intended polyfill mechanism.
- **`bind(context)(...args)`:** Creates a bound function and works for regular functions, but relies on another built-in binding facility.
- **Temporary string key:** Risks overwriting an existing context property.
- **Target returns normally:** Its value is forwarded after cleanup.
- **Target throws:** `finally` deletes the symbol and the exception propagates.
- **No extra arguments:** The target is called with an empty argument list.
- **Many arguments:** Rest and spread preserve their order.
- **Target mutates `this`:** Those deliberate context changes persist; only the temporary symbol is removed.
- **Frozen or non-extensible context:** Cannot accept the temporary property and is outside the guaranteed JSON-object use.
- **Arrow function target:** Its lexical `this` cannot be rebound by JavaScript call syntax.
- **Prototype modification:** Appropriate for this challenge but should be used cautiously in shared production environments.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(a)$. Let $a$ be the number of additional arguments. Collecting the rest parameter and spreading it into the target both require $O(a)$ time. Symbol creation, property assignment, lookup, deletion, and result forwarding are $O(1)$ expected operations, excluding the target function's own work.
- **Auxiliary Space Complexity:** $O(a)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
