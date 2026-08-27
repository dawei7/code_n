# Guided Example: Sleep

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"millis": 100}`
- **Required output:** `100`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a positive integer `millis`, write an asynchronous function that sleeps for `millis` milliseconds. It can resolve any value.

The objective is to compute `100` from `{"millis": 100}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Sleeping in JavaScript means postponing completion

JavaScript should not block the execution thread for the requested number of milliseconds. A busy loop would prevent other work, timers, and callbacks from running.

Instead, `sleep(millis)` returns a Promise whose settlement is scheduled for the future. Callers can either:

- use `await sleep(millis)` inside an asynchronous function, or
- attach a continuation with `sleep(millis).then(...)`.

In both cases, the caller receives an asynchronous pause while the JavaScript runtime remains free to process other work.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"millis": 100}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Create a Promise that starts pending

The expression

`new Promise(r => setTimeout(r, millis))`

constructs a Promise and immediately invokes its executor function. The parameter `r` is the Promise's resolver.

The executor does not call `r` immediately. It passes that resolver to `setTimeout` with delay `millis`. Therefore, the Promise remains pending after construction.

Once the timer becomes eligible and the runtime executes its callback, `r` is called. That resolves the Promise. The resolver receives no argument, so the resolved value is `undefined`, which is allowed because the contract says the Promise may resolve any value.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The expression

`new Promise(r => setTimeout(r, millis))`

c... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: What `setTimeout` actually guarantees

`setTimeout(callback, millis)` schedules the callback no earlier than approximately the requested delay. It does not reserve the JavaScript thread or guarantee execution at an exact wall-clock instant.

After the delay expires, the callback becomes eligible to run. It may wait until:

- the current call stack is empty;
- earlier queued work has completed;
- the runtime's timer resolution and scheduling permit it.

That is why minor positive deviation is acceptable. The solution promises a minimum-style asynchronous delay, not a hard real-time deadline.

For the challenge's values from one through 1000 milliseconds, ordinary timer scheduling directly models the requirement.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `100` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"millis": 100}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `100` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Normal function returning a Promise:** Removin:** - **Normal function returning a Promise:** Removing `async` preserves behavior because the body already returns a Promise.
- **Callback-only API:** A timer callback can delay work, but it does not provide the requested awaitable Promise interface.
- **Busy waiting:** It blocks the event loop and wastes CPU, so it is not an acceptable asynchronous sleep.
- **Exact timing expectation:** The callback may run later than requested because `setTimeout` specifies an earliest eligible time.
- **Several concurrent calls:** Each receives an independent Promise and timer.
- **Ignored resolved value:** The Promise fulfills with undefined, which the contract permits.
- **Very busy event loop:** Completion may be delayed beyond `millis` but cannot run synchronously before timer scheduling.
- **Positive delay:** Constraints exclude negative values and require at least one millisecond.
- **No cancellation:** Sleep always resolves; the returned API exposes no timer handle.
- **No thread blocking:** Other JavaScript work can run while the Promise is pending.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The function performs constant computational work: it creates one Promise, registers one timer, and later invokes one resolver. Computational time is $O(1)$, excluding time spent waiting.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
