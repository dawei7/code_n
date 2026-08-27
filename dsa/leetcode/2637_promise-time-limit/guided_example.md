# Guided Example: Promise Time Limit

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"duration": 100, "t": 150, "behavior": "square", "inputs": [5]}`
- **Required output:** `{"status": "resolved", "value": 25, "time": 100}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an asynchronous function `fn` and a time `t` in milliseconds, return a new **time limited** version of the input function. `fn` takes arguments provided to the **time limited **function.

The objective is to compute `{"status": "resolved", "value": 25, "time": 100}` from `{"duration": 100, "t": 150, "behavior": "square", "inputs": [5]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Create a race between work and a deadline

The limited wrapper must settle according to whichever event occurs first:

- the original function's Promise settles;
- $t$ milliseconds elapse.

`Promise.race` implements exactly this “first settlement wins” rule. The solution races the source Promise against a timer-backed Promise that rejects with the required string.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"duration": 100, "t": 150, "behavior": "square", "inputs": [5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Return a reusable wrapper

`timeLimit(fn, t)` stores `fn` and `t` in a closure and returns an async function accepting `...args`.

No timer starts when the wrapper is created. Each invocation starts its own source call and its own deadline, so separately timed invocations do not share or cancel one another.

Rest syntax collects all invocation arguments in their original order. `fn(...args)` forwards them as positional arguments.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `timeLimit(fn, t)` stores `fn` and `t` in a closure and retu... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Build the rejecting timeout Promise

Inside one invocation, `timeoutId` is declared so it can later be cleared.

The timeout Promise executor calls:

`setTimeout(() => reject('Time Limit Exceeded'), t)`.

It saves the returned handle in `timeoutId`. The Promise remains pending until the timer callback rejects it with the exact string required by the contract.

The unused `resolve` parameter is present only because Promise executors receive both settlement functions.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"status": "resolved", "value": 25, "time": 100}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"duration": 100, "t": 150, "behavior": "square", "inputs": [5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"status": "resolved", "value": 25, "time": 100}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Wrap everything in one manually settled Promis:** - **Wrap everything in one manually settled Promise:** Correct but requires explicit success, failure, timeout, and cleanup wiring that `Promise.race` already provides.
- **Race without clearing the timer:** Returns correctly but leaves unnecessary timer callbacks after fast source completion.
- **AbortController:** Can cooperatively cancel supported underlying work, but the problem only asks to time-limit the wrapper result.
- **`t = 0`:** The timer is scheduled immediately, though an already-settled source Promise may compete through event-loop ordering.
- **Source rejects before deadline:** Its original rejection propagates.
- **Source fulfills before deadline:** Its exact value is returned.
- **Source finishes after deadline:** The wrapper rejects, but underlying work is not physically cancelled.
- **Multiple wrapper calls:** Each owns an independent timer and race.
- **Several arguments:** Rest and spread preserve their order.
- **Cleanup on every path:** `finally` runs after both fulfillment and rejection.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(a)$. Let $a$ be the number of arguments. Rest collection and spreading take $O(a)$ time and $O(a)$ temporary space. Timer creation, Promise creation, racing two Promises, and cleanup use constant additional work.
- **Auxiliary Space Complexity:** $O(a)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
