# Guided Example: Promise Pool

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"durations": [300, 400, 200], "n": 2}`
- **Required output:** `{"startTimes": [0, 0, 300], "finishTimes": [300, 400, 500], "completionTime": 500, "maxPending": 2}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of asynchronous functions `functions` and a **pool limit** `n`, return an asynchronous function `promisePool`. It should return a promise that resolves when all the input functions resolve.

The objective is to compute `{"startTimes": [0, 0, 300], "finishTimes": [300, 400, 500], "completionTime": 500, "maxPending": 2}` from `{"durations": [300, 400, 200], "n": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use a fixed number of long-lived workers

The pool must start functions in array order while never allowing more than $n$ returned promises to remain pending.

The solution creates at most one asynchronous worker per available pool slot. Each worker repeatedly:

1. claims the next unstarted function index;
2. starts that function;
3. waits for its Promise to resolve;
4. returns to claim another index.

Because a worker never claims its next task before its current `await` finishes, each worker contributes at most one pending task. With at most $n$ workers, the concurrency limit follows automatically.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"durations": [300, 400, 200], "n": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: One shared index distributes work

`nextIndex` begins at zero and is captured by every worker.

At the top of the worker loop, a worker checks whether an unstarted function remains. It then performs:

`const index = nextIndex`

followed by:

`nextIndex += 1`.

The local `index` permanently identifies this worker's current task. Incrementing the shared pointer makes the following worker claim the next array position.

No function is removed from the input array, and no queue shifting is needed.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why workers cannot claim the same index

JavaScript executes synchronous statements on one event-loop thread. A worker runs from the loop condition through reading and incrementing `nextIndex` before it reaches:

`await functions[index]()`.

Only at that await can control yield to other asynchronous work. Consequently, another worker cannot interleave between the read and increment and capture the same value.

This atomicity is based on JavaScript's run-to-completion semantics for synchronous code, not on locks or threads.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"startTimes": [0, 0, 300], "finishTimes": [300, 400, 500], "completionTime": 500, "maxPending": 2}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"durations": [300, 400, 200], "n": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"startTimes": [0, 0, 300], "finishTimes": [300, 400, 500], "completionTime": 500, "maxPending": 2}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Launch every Promise with `Promise.all`:** Violates the pool limit when $m>n$.
- **One recursive launcher per slot:** Equivalent in principle, but the worker loop avoids recursive chaining.
- **Shift from an array queue:** Works but mutates or copies input and repeated shifting can be inefficient.
- **`n = 1`:** One worker executes every function sequentially.
- **`n >= m`:** Every function begins immediately, and completion waits for the slowest.
- **Empty function array:** Zero workers are created and the pool resolves immediately.
- **Different completion order:** Allowed; only start order and concurrency are constrained.
- **Fast synchronous fulfillment:** Await still resumes through Promise scheduling, and the worker then claims the next index.
- **Rejection:** Outside the stated input guarantee, it propagates through the worker and `Promise.all`.
- **Shared index safety:** Claims contain no await between reading and incrementing `nextIndex`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(m)$. Let $m=\texttt{functions.length}$. Each function index is claimed and invoked exactly once, so scheduler work is $O(m)$, excluding time spent inside the asynchronous functions.
- **Auxiliary Space Complexity:** $O(\min(m,n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
