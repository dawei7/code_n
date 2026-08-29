# Guided Example: Interval Cancellation

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operation": "double", "args": [7], "t": 100, "cancelTimeMs": 10}`
- **Required output:** `[{"time": 0, "returned": 14}]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a function `fn`, an array of arguments `args`, and an interval time `t`, return a cancel function `cancelFn`.

The objective is to compute `[{"time": 0, "returned": 14}]` from `{"operation": "double", "args": [7], "t": 100, "cancelTimeMs": 10}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The schedule has one immediate call and one repeating timer

The required timeline begins at time zero, but `setInterval` schedules its first callback only after roughly `t` milliseconds. Therefore the exact solution separates the immediate execution from the repeating schedule.

It first calls `fn(...args)` synchronously. The spread syntax expands the array so that each entry becomes a positional argument, matching calls such as `fn(2, 5)` rather than passing one array argument.

Only after that first call returns does the code create the interval.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operation": "double", "args": [7], "t": 100, "cancelTimeMs": 10}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Create the repeating callback

`setInterval(() => fn(...args), t)` registers an arrow-function callback with the host timer system. After at least approximately `t` milliseconds, the event loop may run that callback, which invokes `fn` with the same arguments. The timer continues requesting another callback at each interval until cleared.

The arrow function is necessary because passing `fn` alone would not supply `args`. It also delays the call: `fn(...args)` is executed only when the timer callback runs.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Keep the interval handle

`setInterval` returns an interval identifier. The code stores it in `intervalId`. That handle identifies this particular repeating schedule among every timer the environment may be managing.

Without preserving the handle, the returned cancel function would have no reliable way to tell the host which interval to stop.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[{"time": 0, "returned": 14}]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operation": "double", "args": [7], "t": 100, "cancelTimeMs": 10}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[{"time": 0, "returned": 14}]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Recursive `setTimeout`:** Can schedule the next callback after each execution and may avoid interval backlog, but requires explicit rescheduling and a stored timeout handle or cancellation flag.
- **Call only through `setInterval`:** Incorrect because the first invocation would be delayed by `t` instead of occurring immediately.
- **Lose the interval ID:** Makes precise cancellation impossible.
- **Cancel before the first interval tick:** The immediate call still occurs, while all delayed repetitions are prevented.
- **Cancel exactly near a tick:** Actual ordering depends on which event-loop task runs first; timer timestamps are not strict simultaneous guarantees.
- **Repeated cancellation:** Clearing an already-cleared interval is harmless.
- **Long-running fn:** A cancellation request cannot preempt a callback already executing.
- **Thrown initial call:** No interval is created because setup has not reached `setInterval`.
- **Thrown later call:** The exception belongs to the timer callback; the wrapper does not catch it or automatically clear the interval.
- **Argument identity:** The same values from `args` are spread on every call; nested objects are passed by reference.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(k(A+F)$. Let $k$ be the number of times `fn` is invoked before cancellation, including the immediate call, let $A=\lvert\texttt{args}\rvert$, and let $F$ represent the cost of one execution of `fn`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
