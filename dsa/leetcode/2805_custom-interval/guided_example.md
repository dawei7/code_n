# Guided Example: Custom Interval

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"delay": 50, "period": 20, "cancelTime": 225}`
- **Required output:** `[50, 120, 210]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

**Function **`customInterval`

The objective is to compute `[50, 120, 210]` from `{"delay": 50, "period": 20, "cancelTime": 225}` while avoiding redundant calculations and unnecessary overhead.

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

**The delay grows after every callback.** This interval is not a fixed-period timer. If the initial delay is `delay` and the increment is `period`, the first callback is scheduled after `delay` milliseconds, the second after an additional `delay + period` milliseconds, the third after another `delay + 2 * period` milliseconds, and so forth. The implementation realizes that behavior as a chain of one-shot `setTimeout` calls.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"delay": 50, "period": 20, "cancelTime": 225}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

**Give each custom interval its own identity and state.** A module-level `Map` named `intervals` associates numeric custom IDs with state objects. `nextIntervalId` starts at one and is incremented for each creation, so concurrently active intervals receive different IDs even though the native environment may represent timeout handles in its own way.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The state contains `count`, `handle`, and `active`. `count` is the number of callbacks that have already completed. `handle` is the currently pending native timeout handle. `active` is a logical cancellation flag that protects against timing races and cancellation during a callback.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[50, 120, 210]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"delay": 50, "period": 20, "cancelTime": 225}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[50, 120, 210]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Native `setInterval`:** It repeats a fixed delay and therefore cannot directly express a delay that grows by `period` after every callback.
- **Recursive `setTimeout` without a map:** This handles one interval but provides no stable custom ID lookup for cancelling among multiple active intervals.
- **Absolute-deadline scheduling:** Compute each desired cumulative deadline from the original start time and subtract the current time before scheduling. That can reduce drift from timer lateness, but it differs from the exact after-callback chaining behavior.
- **Cancellation before the first firing:** Native `clearTimeout` removes the pending handle, the active flag is false, and no callback should execute.
- **Cancellation during `fn`:** The post-callback active check prevents rescheduling, even though `count` is still incremented after `fn` returns.
- **Cancellation after host queueing:** The leading active check suppresses a queued callback that native clearing can no longer retract.
- **Unknown or repeated ID:** The map lookup fails and clearing becomes a harmless no-op.
- **Multiple intervals:** Unique IDs and separate state objects prevent one interval's count or handle from affecting another.
- **Zero period:** Every requested wait is `delay`, so the custom timer behaves like a chained fixed-delay interval.
- **Zero delay:** The first callback is eligible immediately through the event loop, and later waits grow by multiples of `period`; callbacks still do not run synchronously during creation.
- **Slow callback:** The next timeout is registered only after completion, so observed start-to-start spacing includes callback execution time.
- **Thrown callback:** Rescheduling is skipped and the map entry is retained. A production implementation could use `try...finally` and define an explicit error policy.
- **Timer clamping:** Browsers and Node.js may delay or clamp timers. The algorithm controls requested delays but cannot promise exact wall-clock execution.
- **ID growth:** IDs increase monotonically and are not reused. Ordinary challenge workloads cannot approach Number precision limits, but a permanent service might need wraparound handling.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Creating an interval performs a constant amount of JavaScript work plus one map insertion and one host timer registration, so it is expected $O(1)$ time. Clearing by ID performs an expected $O(1)$ map lookup and deletion plus one host cancellation.
- **Auxiliary Space Complexity:** $O(a)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
