# Guided Example: Convert Callback Based Function to Promise Based Function

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"behavior": "product", "args": [1, 2, 3], "errorMessage": null}`
- **Required output:** `{"resolved": 6}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Write a function that accepts another function `fn` and converts the callback-based function into a promise-based function.

The objective is to compute `{"resolved": 6}` from `{"behavior": "product", "args": [1, 2, 3], "errorMessage": null}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Build an adapter instead of changing the original function

The input `fn` follows a result-first callback convention: its first argument is a callback, later arguments are the ordinary inputs, and that callback receives `result` first and an optional `error` second. The requested `promisify` function must return a new function with a Promise-based interface.

The exact solution creates two nested closures. Calling `promisify(fn)` stores the original function and returns a wrapper. Calling that wrapper with `...args` creates and returns one new Promise for that invocation. This separation is important: promisifying a function does not execute it, and every later wrapper call gets an independent Promise with independent settlement functions.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"behavior": "product", "args": [1, 2, 3], "errorMessage": null}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Capture every forwarded argument

The returned regular function declares a rest parameter `...args`. JavaScript gathers the caller's separate arguments into an array while preserving their order. Inside the Promise executor, the original function is invoked as

`fn(customCallback, ...args)`.

The adapter inserts its own callback at position zero, exactly where `fn` expects it, and spreads all user arguments after it. If the wrapper is called with `(a, b, c)`, the original function observes `(customCallback, a, b, c)`.

The wrapper does not interpret, reorder, or copy the semantic contents of the arguments. Its job is only to bridge the completion mechanism.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Translate the callback into Promise settlement

The inserted callback receives `(result, error)`. Its branches are:

- If `error !== undefined`, reject the Promise with that exact value.
- Otherwise, resolve the Promise with `result`.

The explicit comparison with `undefined` matters. It does not test whether the error is truthy. An error value such as an empty string, zero, false, or null is still considered present and causes rejection. Only the absence marker `undefined` selects success.

On success, the first callback argument becomes the Promise fulfillment value. On failure, the result is ignored and the second callback argument becomes the rejection reason. This matches the examples, including one where both a numeric result and an error string are supplied.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"resolved": 6}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"behavior": "product", "args": [1, 2, 3], "errorMessage": null}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"resolved": 6}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Node.js error-first adapter:** Many Node APIs call `callback(error, result)`. This problem uses result first and error second, so an error-first implementation would reverse the outcomes.
- **Truthy error test:** `if (error)` would treat zero, false, an empty string, or null as success. The exact `error !== undefined` test recognizes every supplied error value.
- **Preserve method receiver:** Invoking `fn.call(this, callback, ...args)` can forward the wrapper's receiver. The exact implementation calls `fn` plainly and therefore does not preserve method context.
- **Synchronous callback:** The Promise settles during executor execution, while consumer handlers still follow normal microtask scheduling.
- **Asynchronous callback:** Closure capture keeps the correct settlement functions alive until the callback runs.
- **Synchronous throw from `fn`:** The Promise constructor converts it into a rejection automatically.
- **Multiple callback calls:** Only the first settlement affects the Promise; later resolve or reject calls are ignored.
- **Callback supplies both result and error:** Any second argument other than undefined wins, so the Promise rejects and the result is ignored.
- **Callback supplies no arguments:** Error is undefined, so the Promise fulfills with undefined.
- **Concurrent wrapper invocations:** Each call creates new resolver functions and a new callback closure, preventing cross-settlement.
- **Argument order:** Rest gathering and spread preserve the exact left-to-right order expected by `fn`.
- **Work inside `fn`:** Its own time, memory, side effects, and cancellation behavior are outside the adapter's `O(a)` overhead.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(a)$. Let `a` be the number of ordinary arguments supplied to one call of the returned function. Gathering the rest arguments and forwarding them through spread requires `O(a)` time. Creating the Promise, creating the callback, and selecting a settlement branch are `O(1)`. Excluding the unknown work performed by `fn`, one wrapper invocation therefore adds `O(a)` time overhead.
- **Auxiliary Space Complexity:** $O(a)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
