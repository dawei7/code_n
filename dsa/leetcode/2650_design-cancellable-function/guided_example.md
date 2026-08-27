# Guided Example: Design Cancellable Function

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"scenario": "immediate-return", "cancelledAt": 10}`
- **Required output:** `{"resolved": 42}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Sometimes you have a long running task, and you may wish to cancel it before it completes. To help with this goal, write a function `cancellable` that accepts a generator object and returns an array of two values: a **cancel function** and a **promise**.

The objective is to compute `{"resolved": 42}` from `{"scenario": "immediate-return", "cancelledAt": 10}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Drive the generator one yielded Promise at a time

A generator does not run continuously. It advances only when the controller calls:

- `generator.next(value)` to deliver a successful yielded result;
- `generator.throw(error)` to inject a rejection or cancellation.

The returned controller Promise repeatedly waits for the current yielded Promise, feeds its outcome back into the generator, and stops when the generator returns or throws.

Cancellation is modeled as one more injected error: the exact string `"Cancelled"`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"scenario": "immediate-return", "cancelledAt": 10}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Track cancellation and the current waiter

Two closure variables coordinate the cancel function and asynchronous driver:

- `cancelled` records whether cancellation has ever been requested;
- `rejectCurrent` points to the rejection function of the bridge Promise currently being awaited, or null when no bridge is pending.

The cancel function is synchronous. On its first call, it sets `cancelled = true`. If a bridge is active, it rejects that bridge with `"Cancelled"`.

Later cancel calls do nothing because the flag is already true. Cancellation is idempotent.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Two closure variables coordinate the cancel function and asy... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Start the generator

The async immediately invoked function begins with:

`let iteration = generator.next()`.

An iterator result has:

- `value`: either the yielded Promise or final return value;
- `done`: whether the generator has finished.

If the generator returns immediately, `done` is true. The while-loop is skipped and the async driver returns `iteration.value`, resolving its Promise with the generator's return value.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"resolved": 42}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"scenario": "immediate-return", "cancelledAt": 10}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"resolved": 42}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Poll a cancelled flag:** Cannot promptly inter:** - **Poll a cancelled flag:** Cannot promptly interrupt a long pending Promise; rejecting the current bridge wakes the driver immediately.
- **Race every yield with a cancellation Promise:** Valid, but the stored reject callback is a compact one-pending-wait implementation.
- **Call `generator.return()` on cancellation:** Skips the required `throw("Cancelled")` semantics and prevents generator catch logic.
- **Immediate generator return:** The controller Promise resolves without waiting, and later cancellation is harmless.
- **Yielded Promise rejects:** Its error is thrown into the generator and may be caught.
- **Cancellation uncaught:** The outer Promise rejects with the exact string.
- **Cancellation caught with return:** The outer Promise resolves with the returned recovery value.
- **Repeated cancel calls:** Only the first has an effect.
- **Underlying Promise after cancellation:** It is not physically cancelled; its later settlement cannot change the bridge.
- **One pending bridge:** `rejectCurrent` always refers only to the yield currently being awaited.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(y)$. Let $y$ be the number of yielded Promises the driver processes before completion or cancellation. Each yield creates one bridge and performs constant controller work, so scheduling overhead is $O(y)$, excluding time and work inside yielded Promises.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
