# Guided Example: Throttle

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"t": 100, "calls": [{"t": 20, "inputs": [1]}]}`
- **Required output:** `[{"t": 20, "inputs": [1]}]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a function `fn` and a time in milliseconds `t`, return a **throttled** version of that function.

The objective is to compute `[{"t": 20, "inputs": [1]}]` from `{"t": 100, "calls": [{"t": 20, "inputs": [1]}]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Model throttling as idle versus waiting

The returned function has two modes. When `waiting` is false, no throttle window is active, so a call is a leading call and must execute `fn` immediately. When `waiting` is true, `fn` may not execute immediately; the wrapper remembers only the most recent blocked call.

Two closure variables represent all persistent state:

- `waiting` tells whether a timer chain currently owns the next permitted execution point.
- `pending` is either `null` or one record containing the latest blocked call's `context` and `args`.

The closure matters because these values must survive after `throttle` itself returns and across many later invocations of the wrapper.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"t": 100, "calls": [{"t": 20, "inputs": [1]}]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Execute an idle call immediately

The returned function accepts arbitrary arguments with `...args`. When `waiting` is false, it runs:

`fn.apply(this, args)`.

This is the required leading execution. It then changes `waiting` to true and schedules `release` after `t` milliseconds.

Changing the flag before any later external call can arrive establishes the closed window. Until the timer fires, calls take the other branch.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Preserve the receiver as well as the arguments

A JavaScript method call has both explicit arguments and an implicit `this` value. Saving only `args` would be wrong when callers use the throttled function as methods of different objects.

The immediate branch passes the wrapper's current `this` directly to `fn.apply`. The blocked branch stores:

`{ context: this, args }`.

The trailing execution later uses `fn.apply(call.context, call.args)`. Therefore it reproduces both parts of the latest suppressed invocation.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[{"t": 20, "inputs": [1]}]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"t": 100, "calls": [{"t": 20, "inputs": [1]}]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[{"t": 20, "inputs": [1]}]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Schedule every blocked call:** Incorrect because intermediate calls must be coalesced, not queued.
- **Debounce:** It waits for activity to stop before executing and therefore does not provide the required immediate leading call.
- **Fixed `setInterval`:** It can implement the same state machine, but it must be cleared when a whole interval has no pending work.
- **Timestamp plus replaceable timeout:** Also valid, but it needs careful delay calculations and timer cancellation.
- **No blocked calls:** The release callback returns the wrapper to idle without invoking `fn`.
- **Many blocked calls:** Only the latest receiver and argument array survive.
- **Different `this` values:** The pending record preserves the receiver belonging to the latest call.
- **Zero interval:** The leading call is immediate; suppressed synchronous calls are coalesced until the zero-delay timer task runs.
- **Call at a timer boundary:** JavaScript event-loop ordering determines which task runs first, but the state machine remains internally consistent.
- **Callback throws:** The exact source does not catch errors; a thrown trailing callback can prevent scheduling the next release and is outside the ordinary promised-call behavior.
- **Return values:** The wrapper does not return `fn`'s result; the problem evaluates execution timing and arguments.
- **Sustained activity:** Each trailing execution starts another complete interval, enforcing the frequency limit continuously.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Each wrapper call performs a constant number of flag checks, assignments, and timer operations, excluding the work performed by `fn` itself. With the challenge's bounded argument count, this is $O(1)$ time per call. More generally, collecting and later spreading $a$ arguments costs $O(a)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
