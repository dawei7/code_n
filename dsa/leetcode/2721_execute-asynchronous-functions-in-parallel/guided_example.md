# Guided Example: Execute Asynchronous Functions in Parallel

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tasks": [{"delay": 200, "value": 5}]}`
- **Required output:** `{"status": "resolved", "value": [5], "completionTime": 200, "startTimes": [0]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of asynchronous functions `functions`, return a new promise `promise`. Each function in the array accepts no arguments and returns a promise. All the promises should be executed in parallel.

The objective is to compute `{"status": "resolved", "value": [5], "completionTime": 200, "startTimes": [0]}` from `{"tasks": [{"delay": 200, "value": 5}]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Create one promise that represents the whole group

Each input element is a function rather than an already-created promise. To run the operations in parallel, the solution must invoke every function without waiting for an earlier result. It also needs one returned promise whose eventual state summarizes the group.

The code returns `new Promise((resolve, reject) => { ... })`. The executor runs synchronously, setting up all of the asynchronous work before `promiseAll` returns.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tasks": [{"delay": 200, "value": 5}]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Start every function immediately

`functions.forEach((fn, index) => { ... })` walks through the array. For each function, `fn()` is called immediately, and handlers are attached to its returned promise.

There is no `await` inside this loop and no chain from one input promise to the next. Invocation of function at index one does not wait for index zero to fulfill. By the end of the synchronous loop, every input operation has been started. Their asynchronous portions can then make progress concurrently according to the JavaScript runtime.

“Parallel” here describes overlapping asynchronous lifetimes, not necessarily simultaneous JavaScript execution on several CPU cores. JavaScript callbacks still run through the host's event loop, but timers, network work, and other promise-producing operations are all initiated without artificial serialization.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `functions.forEach((fn, index) => { ...... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Reserve result positions before anything finishes

The array `results` is created with the same length as `functions`. A fulfillment handler stores each value at its original `index`:

`results[index] = value`.

This is crucial because completion order can differ from input order. If the third promise fulfills first, its value belongs at index two, not at the beginning of the result. Appending values as they arrive would produce completion order and violate the contract.

Sparse slots in the initially allocated array are filled as promises fulfill. The aggregate promise is resolved only after every slot has received its value.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"status": "resolved", "value": [5], "completionTime": 200, "startTimes": [0]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tasks": [{"delay": 200, "value": 5}]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"status": "resolved", "value": [5], "completionTime": 200, "startTimes": [0]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Built-in `Promise.all`:** Has the desired sema:** - **Built-in `Promise.all`:** Has the desired semantics but is explicitly forbidden by the problem.
- **Sequential `await` loop:** Preserves order easily but delays invocation of later functions, violating the required parallel start.
- **Append values on fulfillment:** Produces completion order rather than input order and is therefore incorrect.
- **Use `Promise.allSettled`:** Waits for every rejection and fulfillment and returns status objects, which does not match fail-fast behavior.
- **One function:** Its fulfillment becomes a one-element result, and its rejection is forwarded directly.
- **Out-of-order completion:** Indexed assignment keeps the output in input order.
- **Multiple rejections:** The first rejection handler to settle the outer promise determines its reason; later attempts are ignored.
- **Work after rejection:** Already-started operations continue unless they implement their own cancellation mechanism.
- **Empty array:** The constraints require at least one function. This exact code would leave the returned promise pending forever for an empty array because `completed === functions.length` is never checked before the loop.
- **Synchronous throw:** The outer Promise constructor rejects, although later functions after the throwing call are not invoked.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of functions. The aggregation layer invokes each function once, attaches handlers once, and processes one settlement callback per input, for $O(n)$ bookkeeping time excluding work performed inside the supplied functions.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
