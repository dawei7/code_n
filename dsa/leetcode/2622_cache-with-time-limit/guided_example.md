# Guided Example: Cache With Time Limit

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"actions": ["TimeLimitedCache", "set", "get", "count", "get"], "values": [[], [1, 42, 100], [1], [], [1]], "timeDelays": [0, 0, 50, 50, 150]}`
- **Required output:** `[null, false, 42, 1, -1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Write a class that allows getting and setting key-value pairs, however a **time until expiration** is associated with each key.

The objective is to compute `[null, false, 42, 1, -1]` from `{"actions": ["TimeLimitedCache", "set", "get", "count", "get"], "values": [[], [1, 42, 100], [1], [], [1]], "timeDelays": [0, 0, 50, 50, 150]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Represent only currently active keys

The class stores a `Map` named `cache`. Every present entry has:

- `value`: the value returned by `get`;
- `timeout`: the timer handle responsible for expiring this exact entry.

An expired key is physically deleted from the map when its timer fires. This design gives a strong invariant:

> A key is present in `cache` exactly while it is considered unexpired.

Because the map contains no stale records, both `get` and `count` can answer directly without comparing timestamps.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"actions": ["TimeLimitedCache", "set", "get", "count", "get"], "values": [[], [1, 42, 100], [1], [], [1]], "timeDelays": [0, 0, 50, 50, 150]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Construct an empty independent cache

`TimeLimitedCache` is a constructor function. Calling it with `new` creates an instance, and the constructor assigns a new `Map` to `this.cache`.

Each cache instance therefore owns separate entries and timer handles. Setting key one in one instance does not affect key one in another instance.

The public operations are installed on `TimeLimitedCache.prototype`, so all instances share the same method functions while using their own `this.cache` state.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `TimeLimitedCache` is a constructor function.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Set a new key

At the beginning of `set(key, value, duration)`, the code evaluates:

`const existed = this.cache.has(key)`.

By the class invariant, this Boolean says exactly whether the same key currently has an unexpired value. It is saved before any overwrite so the method can return the required historical fact.

For a new key, no old timer needs cancellation. The method schedules a callback that deletes the key after `duration` milliseconds, stores the new value and timer handle, and returns false.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[null, false, 42, 1, -1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"actions": ["TimeLimitedCache", "set", "get", "count", "get"], "values": [[], [1, 42, 100], [1], [], [1]], "timeDelays": [0, 0, 50, 50, 150]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[null, false, 42, 1, -1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Store expiration timestamps:** Check time duri:** - **Store expiration timestamps:** Check time during `get` and `count`; this avoids one timer per key but makes accurate count require cleanup or scanning.
- **Priority queue of expirations:** Efficiently expire keys in chronological order, but replacement generations need validation and the implementation is more complex.
- **Overwrite without `clearTimeout`:** Incorrect because the old timer can delete the new value early.
- **New key:** `set` returns false and increases active count.
- **Unexpired replacement:** `set` returns true, preserves key count, and restarts duration.
- **Expired replacement:** The old callback has removed the key, so `set` returns false.
- **Cached value zero:** Membership, not truthiness, ensures it is returned correctly.
- **Duration zero:** Expiration is timer-scheduled after the synchronous call rather than performed inline.
- **Repeated `get`:** Reads do not extend the expiration time.
- **Separate instances:** Each constructor call owns its own map and timers.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. `Map.has`, `Map.get`, `Map.set`, `Map.delete`, and `Map.size` are expected $O(1)$ operations. Timer registration and cancellation are treated as $O(1)$ runtime operations, so each `set`, `get`, `count`, and expiration callback takes expected $O(1)$ time.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
