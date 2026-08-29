# Guided Example: Delay the Resolution of Each Promise

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tasks": [{"delay": 30, "value": null}], "ms": 50}`
- **Required output:** `[{"status": "resolved", "value": null, "completionTime": 80}]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array `functions` and a number `ms`, return a new array of functions.

The objective is to compute `[{"status": "resolved", "value": null, "completionTime": 80}]` from `{"tasks": [{"delay": 30, "value": null}], "ms": 50}` while avoiding redundant calculations and unnecessary overhead.

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

**Return wrappers without starting the original work yet.** `delayAll` maps every input function `fn` to a new zero-argument function. The mapping step creates closures but does not call `fn`. This preserves laziness: constructing the returned array causes no asynchronous task to begin.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tasks": [{"delay": 30, "value": null}], "ms": 50}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The array order is preserved because JavaScript `map` places each produced wrapper at the same index as its source function. Calling returned wrapper $i$ invokes source function $i$.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Start the source promise when its wrapper is called.** The wrapper body begins with `fn()`. The exact implementation therefore does not wait `ms` before starting the original operation. It starts the operation immediately, waits for its promise to settle, and then delays propagation of that settlement by an additional `ms`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[{"status": "resolved", "value": null, "completionTime": 80}]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tasks": [{"delay": 30, "value": null}], "ms": 50}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[{"status": "resolved", "value": null, "completionTime": 80}]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Delay before source invocation:** Start a timer first and call `fn` after it fires. Simple examples show the same summed duration, but source side effects and rejection timing begin later than in the exact implementation.
- **Reusable `sleep` helper:** Define a promise-based delay and chain `sleep(ms).then(() => value)` in both outcome handlers. This can reduce duplication while preserving post-settlement delay.
- **`finally` alone:** `finally` can wait for a promise, but forwarding both the original fulfillment value and rejection reason correctly still depends on promise adoption semantics; explicit handlers are clearer.
- **Rejected source promise:** The reason is retained and rejection is delayed, rather than converted into fulfillment.
- **Immediate source settlement:** Even `Promise.resolve(value)` remains externally pending until the timer fires.
- **Multiple wrappers:** They are independent and may execute concurrently; array order does not serialize them.
- **Repeated wrapper call:** It invokes `fn` again and creates a fresh delayed promise each time.
- **Synchronous throw:** It escapes immediately because `fn()` is outside a protective promise callback. The contract's promise-returning guarantee avoids this case.
- **Thenable instead of native promise:** If `fn()` returns an object with a compatible `then` method, the code may work through that method, but the formal contract promises actual promises.
- **Timer accuracy:** Host scheduling can add delay beyond `ms`, so tests should allow timing tolerance.
- **Receiver-dependent function:** Calling `fn()` does not forward a wrapper receiver. Use `fn.call(this)` inside an ordinary wrapper if receiver preservation is required.
- **Sparse input array outside normal constraints:** `map` preserves holes rather than creating wrappers at missing positions.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of input functions. Creating the returned array calls `map` once per entry and allocates one wrapper closure per entry, taking $O(n)$ time and $O(n)$ space.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
