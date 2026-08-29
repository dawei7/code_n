# Guided Example: Print FooBar Alternately

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 1}`
- **Required output:** `"foobar"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Suppose you are given the following code:

The objective is to compute `"foobar"` from `{"n": 1}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Represent whose turn it is with permits

Two threads must print alternating tokens for $n$ rounds. A semaphore count represents permission to proceed.

`f = Semaphore(1)` gives the foo thread one initial permit, so foo may print first. `b = Semaphore(0)` gives the bar thread no initial permit, so bar blocks if scheduled before foo.

Only one side has a permit at a time. After printing, that side releases the other side’s semaphore, explicitly handing over the turn.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: One foo iteration

At the start of every foo iteration, `f.acquire()` waits for a foo permit and consumes it. The count changes from one to zero, so foo cannot pass another iteration until bar returns a permit.

`printFoo` runs while bar still has no permit. Only after the callback returns does `b.release()` create one bar permit.

This ordering guarantees that the complete text `foo` is produced before the corresponding `bar` callback can begin.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: One bar iteration

The bar thread mirrors the process. `b.acquire()` waits until foo finishes one callback and releases a permit. Bar consumes it, calls `printBar`, and then releases `f`.

That last release authorizes exactly the next foo iteration. Bar cannot immediately print twice because its own semaphore returned to zero when it acquired the permit.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"foobar"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"foobar"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Two locks as gates:** Start foo’s lock open and bar’s closed, then release the opposite lock after each callback. Semaphore ownership rules often make repeated cross-thread handoffs clearer.
- **Condition variable with turn flag:** Wait for a Boolean turn, print, flip it, and notify. Correct use requires a loop around waits to handle wakeups.
- **Events:** Events can coordinate turns but must be cleared and set carefully to prevent one thread from passing multiple iterations.
- **Busy waiting:** Polling a shared turn flag wastes CPU and needs synchronization for visibility.
- **`n = 1`:** Foo consumes the initial permit, prints once, enables bar, and bar prints once.
- **Bar scheduled first:** Its zero-permit acquire blocks safely until foo prints.
- **Foo repeatedly scheduled:** It cannot begin its next iteration until bar returns the permit.
- **Equal loop counts:** Both methods must run $n$ iterations; mismatched counts could strand one thread.
- **Permit counts:** Each acquire consumes the only active permit before printing, preventing duplicate consecutive tokens.
- **Release placement:** Releasing before the callback would weaken the required ordering.
- **Final permit:** A leftover foo permit after all work is harmless because no additional loop iteration exists.
- **Callback exception:** It can interrupt the handoff and block the peer; normal callback completion is assumed.
- **No output buffer:** The class controls callback order and does not build the output string itself.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Each thread performs $n$ loop iterations. Every iteration has one acquire, one callback, and one release, all constant synchronization work apart from the external callback’s own cost. Total algorithmic work is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
