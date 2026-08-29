# Guided Example: Debounce

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"t": 50, "calls": [{"t": 50, "inputs": [1]}, {"t": 75, "inputs": [2]}]}`
- **Required output:** `[{"t": 125, "inputs": [2]}]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a function `fn` and a time in milliseconds `t`, return a **debounced** version of that function.

The objective is to compute `[{"t": 125, "inputs": [2]}]` from `{"t": 50, "calls": [{"t": 50, "inputs": [1]}, {"t": 75, "inputs": [2]}]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Keep only the latest pending invocation

Debouncing groups calls that occur close together. Every call schedules execution for $t$ milliseconds later, but a newer call arriving before that execution cancels the old schedule.

At any moment, the wrapper needs to remember only one thing: the timer handle for the currently pending invocation. Variable `timeoutId` is stored in the closure returned by `debounce`.

The closure persists across calls, so every invocation can cancel the schedule created by the previous invocation.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"t": 50, "calls": [{"t": 50, "inputs": [1]}, {"t": 75, "inputs": [2]}]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Cancel before scheduling

Each wrapper call begins with:

`clearTimeout(timeoutId)`.

On the very first call, `timeoutId` is undefined. JavaScript safely treats clearing an unknown or undefined handle as doing nothing, so no first-call branch is required.

On later calls, if the prior timer has not fired, cancellation prevents its callback from executing. The wrapper then creates a new timer for the full delay $t$.

The order matters. Scheduling first and clearing afterward could cancel the newly created timer instead of the previous one.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Capture the latest arguments

The wrapper uses rest syntax `(...args)`, producing an array containing exactly the arguments from that invocation in order.

The timer callback closes over this particular `args` array. When a newer invocation cancels the timer, the old callback becomes unreachable by the timer system. The new timer captures the new call's arguments.

Therefore, the eventual execution receives the arguments of the last call in the quiet period, not those of the first call.

For calls with inputs one at 50 milliseconds and two at 75 milliseconds under $t=50$:

- the first timer was due at 100;
- the second call cancels it;
- the second timer is due at about 125;
- only `fn(2)` runs.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[{"t": 125, "inputs": [2]}]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"t": 50, "calls": [{"t": 50, "inputs": [1]}, {"t": 75, "inputs": [2]}]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[{"t": 125, "inputs": [2]}]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **`setInterval` polling:** Can implement delayed detection but repeatedly wakes and tracks timestamps; one timeout per latest call is simpler.
- **Throttle:** It enforces a different policy and may execute the first call rather than the last.
- **Call `fn(...args)` directly in the timer:** Works for context-free functions but can lose the original `this` receiver.
- **First call:** Clearing undefined is harmless, then one timer is scheduled.
- **Call inside the delay window:** It cancels the preceding pending execution and restarts the full delay.
- **Call after prior execution:** It begins a new independent debounce group.
- **`t = 0`:** Execution is still deferred to a timer task; another synchronous call can cancel it first.
- **Several arguments:** Rest and `apply` preserve their order.
- **Simultaneous calls:** The last invocation in event-loop execution order survives.
- **Return value:** The debounced wrapper returns immediately and does not expose the later function result.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Each wrapper invocation cancels at most one timer, captures its arguments and receiver, and schedules one timer. With at most ten arguments by the challenge constraints, this is treated as $O(1)$ time and $O(1)$ retained space, matching the manifest.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
