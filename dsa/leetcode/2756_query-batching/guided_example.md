# Guided Example: Query Batching

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"queryDelay": "none", "t": 500, "calls": []}`
- **Required output:** `[]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Batching multiple small queries into a single large query can be a useful optimization. Write a class `QueryBatcher` that implements this functionality.

The objective is to compute `[]` from `{"queryDelay": "none", "t": 500, "calls": []}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: What the class must coordinate

Each call to `getValue(key)` must eventually receive the value for that particular key, but the class should combine waiting keys into calls to `queryMultiple`. The timing rule is the important part: a request may be dispatched immediately when no cooldown is active, and after a dispatch the next batch may not be dispatched until `t` milliseconds have elapsed. The exact solution separates those two responsibilities with two pieces of state:

- `queue` contains records for requests that have arrived but have not yet been dispatched. Each record stores both the requested `key` and the Promise's `resolve` function.
- `throttled` says whether the cooldown following the most recent dispatch is still active.

The queue is not merely a collection of keys. Keeping the resolver beside its key is what allows one batched response to settle many independently returned Promises later.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"queryDelay": "none", "t": 500, "calls": []}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What happens when a caller asks for a value

`getValue` constructs and immediately returns a new Promise. The Promise executor runs synchronously, so its `{ key, resolve }` record is appended to `queue` before `getValue` returns. It then calls `flush()`.

`flush` has two guard conditions. If `throttled` is true, another dispatch would be too early, so the queued request is left in place. If the queue is empty, there is nothing to send. Otherwise, this request is allowed to start a batch immediately. This explains why the first request after an idle period is not delayed by `t`: no cooldown exists yet, and the call to `flush` proceeds at once.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `getValue` constructs and immediately returns a new Promise.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the queue is detached before asynchronous work starts

An allowed flush executes:

1. Set `throttled` to true.
2. Save the current array in `batch`.
3. Replace `queue` with a new empty array.
4. Schedule a timer for the end of the cooldown.
5. Call `queryMultiple` with the keys in `batch`.

The assignment `const batch = this.queue; this.queue = [];` is crucial. `batch` is a stable snapshot of exactly the requests covered by this one external query. Calls arriving afterward append to a different array, so they cannot accidentally become associated with the already-dispatched result.

For example, suppose key `A` arrives while idle. It forms a one-key batch immediately. If `B` and `C` arrive during the next `t` milliseconds, their calls to `flush` see `throttled === true`, so both records remain in the new queue. When the timer fires, it clears the flag and invokes `flush` again. That second flush snapshots `B` and `C` together.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"queryDelay": "none", "t": 500, "calls": []}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Delay-first debounce:** Waiting `t` millisecon:** - **Delay-first debounce:** Waiting `t` milliseconds before the first dispatch could collect a larger initial batch, but it violates the required behavior because an idle batch must start immediately.
- **Wait for query completion before unlocking:** This would cap concurrency at one, yet it would measure the gap from response completion rather than dispatch time. A slow query would incorrectly delay later work beyond the stated throttle interval.
- **One timer per incoming request:** Repeatedly scheduling timers complicates ordering and can produce duplicate flush attempts. The single cooldown timer established by the dispatch is sufficient.
- **Key-to-resolver map:** A map can associate results by key, but it is unnecessary because the API guarantees aligned result order and keys are unique. The positional batch array is both smaller conceptually and faithful to the contract.
- **Calls arriving synchronously:** The first synchronous call dispatches immediately and turns on throttling. Further synchronous calls in the same JavaScript turn enter the next batch rather than the first one.
- **`t = 0`:** The timer still runs asynchronously through `setTimeout`. Requests arriving before that callback executes may batch together; the implementation does not recursively spin.
- **A timer finds an empty queue:** It clears `throttled` and `flush` returns. No external query is made, and a future request starts immediately.
- **Slow external queries:** Multiple batches may be in flight, but each callback closes over its own detached `batch`, so responses that finish out of order still resolve the correct Promises.
- **Rejected external queries:** The local reference promises this cannot happen. Without that guarantee, the exact implementation would leave the affected Promises pending because it has no rejection callback.
- **Mutable or repeated keys:** The contract guarantees unique keys. The implementation forwards each stored key value as received and relies only on response position, not object identity or a deduplication rule.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(q)$. Let `c` be the total number of `getValue` calls and let `b` be the number of non-empty batches. Across the lifetime of the object, each request record is created once, appended once, included in one key-mapping pass, and resolved once. The class therefore performs `O(c)` total bookkeeping work, in addition to the external work and latency of `queryMultiple`. Each `getValue` does `O(1)` immediate work. A particular `flush` that dispatches a batch of size `q` spends `O(q)` time building the key array and later `O(q)` time resolving its values.
- **Auxiliary Space Complexity:** $O(c)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
