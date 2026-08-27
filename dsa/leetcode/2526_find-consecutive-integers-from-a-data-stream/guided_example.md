# Guided Example: Find Consecutive Integers from a Data Stream

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"commands": ["DataStream", "consec", "consec", "consec", "consec"], "inputs": [[4, 3], [4], [4], [4], [3]]}`
- **Required output:** `[null, false, false, true, false]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

For a stream of integers, implement a data structure that checks if the last `k` integers parsed in the stream are **equal** to `value`.

The objective is to compute `[null, false, false, true, false]` from `{"commands": ["DataStream", "consec", "consec", "consec", "consec"], "inputs": [[4, 3], [4], [4], [4], [3]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Only the trailing run matters

After each new stream value, the question asks whether the last `k` parsed integers all equal `value`.

There is no need to remember the full stream or even the last `k` items. It is sufficient to know the length of the current consecutive run of `value` at the stream's end.

If that trailing run has length at least `k`, then the last `k` elements are all `value`. If it is shorter, some position among the last `k` is missing or contains a different value.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"commands": ["DataStream", "consec", "consec", "consec", "consec"], "inputs": [[4, 3], [4], [4], [4], [3]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Persistent object state

The constructor stores:

- `val`: the target value;
- `k`: required trailing length;
- `cnt`: current trailing run length, initially zero because the stream is empty.

These fields persist across calls to `consec`. A local variable would be lost after each call and could not describe the accumulated stream.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The constructor stores:

- `val`: the target value;
- `k`: r... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Update on a matching number

If incoming `num` equals `val`, it extends the existing trailing run by one:

`cnt+1`.

For three consecutive target values, the counter progresses 1, 2, 3. Once it reaches `k`, the method returns true.

Additional target values keep increasing the counter. Returning `cnt>=k` remains true because the last `k` positions of a longer matching run are still all targets.

Testing equality `==k` would be wrong after the run grows beyond `k`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[null, false, false, true, false]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"commands": ["DataStream", "consec", "consec", "consec", "consec"], "inputs": [[4, 3], [4], [4], [4], [3]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[null, false, false, true, false]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Queue of last `k` values:** It works but uses :** - **Queue of last `k` values:** It works but uses $O(k)$ memory and more updates.
- **`k=1`:** Return true exactly when the current number equals the target.
- **Run longer than `k`:** Continue returning true; use `>=` rather than equality.
- **Mismatch after success:** Reset immediately and return false.
- **New run after mismatch:** The first matching value sets the count to one.
- **Fewer than `k` calls:** Counter cannot reach the threshold.
- **Target never appears:** Every call leaves or resets the counter to zero.
- **All values match:** Results become true starting with call `k`.
- **Persistent state:** Constructor fields must survive between method calls.
- **No stream storage:** The trailing-run invariant is sufficient.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(q)$. Each `consec` call performs one comparison, one assignment, and one threshold test, taking $O(1)$ time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
