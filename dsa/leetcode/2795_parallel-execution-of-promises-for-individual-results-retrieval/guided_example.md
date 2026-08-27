# Guided Example: Parallel Execution of Promises for Individual Results Retrieval

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tasks": [{"delay": 100, "value": 15}]}`
- **Required output:** `{"status": "resolved", "value": [{"status": "fulfilled", "value": 15}], "completionTime": 100, "startTimes": [0]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array `functions`, return a promise `promise`. `functions` is an array of functions that return promises `fnPromise.` Each `fnPromise` can be resolved or rejected.

The objective is to compute `{"status": "resolved", "value": [{"status": "fulfilled", "value": 15}], "completionTime": 100, "startTimes": [0]}` from `{"tasks": [{"delay": 100, "value": 15}]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Start every asynchronous operation without awaiting the previous one

The function returns one outer Promise. Inside its executor, a `for...in` loop invokes every promise-producing function immediately and attaches handlers to the returned Promise.

There is no `await` inside the loop and no chaining from one function to the next. Invocation of function index one does not wait for index zero's Promise to settle. After the synchronous loop finishes, all returned Promises are pending or already settled concurrently.

This is why total elapsed time is determined by the slowest operation, not by the sum of their durations.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tasks": [{"delay": 100, "value": 15}]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Convert rejection into ordinary fulfillment data

For one input function, the source builds this chain:

- fulfillment handler maps a value to `{ status: 'fulfilled', value }`;
- rejection handler maps a reason to `{ status: 'rejected', reason }`;
- a final fulfillment handler stores that outcome object.

The key idea is that `catch` returns an ordinary value object rather than throwing again. A rejected input Promise is therefore transformed into a fulfilled chain whose value describes the rejection. The outer coordination logic sees every chain complete normally, regardless of the original outcome.

This recreates the central behavior of `Promise.allSettled`: one failure is data, not a reason to reject the whole collection.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For one input function, the source builds this chain:

- ful... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Store results by input index

`res[i] = obj` writes each outcome at the same property index used to select `functions[i]`. Promises may settle in any order, but completion order affects only when assignments occur, not where they are stored.

For example, if function one resolves after 10 milliseconds and function zero after 100 milliseconds, result index one is filled first. The outer Promise waits for both, and the final array still places index zero's outcome before index one's outcome.

Array slots can temporarily be sparse while work remains. When every input has settled under the normal array contract, all original indices have been assigned.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"status": "resolved", "value": [{"status": "fulfilled", "value": 15}], "completionTime": 100, "startTimes": [0]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tasks": [{"delay": 100, "value": 15}]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"status": "resolved", "value": [{"status": "fulfilled", "value": 15}], "completionTime": 100, "startTimes": [0]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Built-in `Promise.allSettled`:** It provides t:** - **Built-in `Promise.allSettled`:** It provides the requested behavior directly, but the challenge asks for a manual implementation.
- **`Promise.all` without converting rejections:** It rejects as soon as one input rejects and loses the complete outcome report.
- **Map every Promise to a never-rejecting outcome, then use `Promise.all`:** This is a concise manual design with the same `O(n)` behavior.
- **Sequential `await` loop:** It preserves order but unnecessarily serializes independent work and makes elapsed time approach the sum of durations.
- **Out-of-order settlement:** Indexed assignment preserves input order in the final array.
- **Rejected input Promise:** Catch converts it to a fulfilled rejected-status object, so other operations continue.
- **Synchronous throw while invoking a function:** The exact code rejects the outer Promise instead of recording an outcome; the stated contract expects returned Promises.
- **Empty array outside constraints:** The exact outer Promise remains pending because there is no immediate resolve branch.
- **Never-settling input:** The outer Promise remains pending, matching the fact that not all inputs have settled.
- **Extra enumerable array properties:** `for...in` could visit them; a numeric loop or `forEach` is safer for general arrays.
- **Several promises settle in the same turn:** JavaScript runs handlers individually; each unique increment still contributes once.
- **Outcome value is undefined:** The fulfilled object still contains a `value` property with undefined.
- **Rejection reason is falsy:** Catch receives it and records it without a truthiness test.
- **Input function called once:** Each normal array index is invoked once during the initial synchronous loop.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the number of functions. The coordination code invokes `n` functions, attaches a constant number of handlers to each, stores `n` outcomes, and increments `n` counters. Excluding the unknown internal work of the supplied functions, total bookkeeping time is `O(n)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
