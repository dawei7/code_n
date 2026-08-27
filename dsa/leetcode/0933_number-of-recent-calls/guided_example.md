# Guided Example: Number of Recent Calls

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": [["ping", 1], ["ping", 100], ["ping", 3001], ["ping", 3002]]}`
- **Required output:** `[1, 2, 3, 3]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You have a `RecentCounter` class which counts the number of recent requests within a certain time frame.

The objective is to compute `[1, 2, 3, 3]` from `{"operations": [["ping", 1], ["ping", 100], ["ping", 3001], ["ping", 3002]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The data that a call needs

Each call `ping(t)` must return how many recorded requests have timestamps in the inclusive interval `[t - 3000, t]`. The timestamps arrive in strictly increasing order. That ordering guarantee is the key to the optimal solution.

At the moment a new timestamp arrives, it is later than every stored timestamp. Any old timestamp smaller than `t - 3000` is now outside the requested window. More importantly, it can never become relevant again: every future timestamp will be still larger, so every future lower boundary will be at least as large as the current lower boundary.

The algorithm can therefore permanently discard expired requests. It needs to retain only the timestamps in the current sliding time window.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": [["ping", 1], ["ping", 100], ["ping", 3001], ["ping", 3002]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why a deque matches the operations

Because calls arrive in increasing order, the retained timestamps are sorted from oldest at the front to newest at the back. Every new timestamp belongs at the back. Every expired timestamp, if one exists, must be among the oldest values at the front.

A deque supports both needed operations efficiently:

- `append(t)` adds the new, largest timestamp to the back;
- `popleft()` removes an expired, smallest timestamp from the front.

A regular Python list can append efficiently, but removing index zero shifts every remaining element and costs linear time. The deque avoids those repeated shifts.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Because calls arrive in increasing order, the retained times... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The exact order inside `ping`

The method first executes `q.append(t)`. This is important for two reasons. The current request belongs to its own interval because `t` is at the inclusive upper boundary, so it must be counted. Appending first also guarantees that the deque is nonempty before the code reads `q[0]` in the loop condition.

Next, the loop checks `q[0] < t - 3000`. If the oldest timestamp is strictly below the lower boundary, it is outside the inclusive interval and is removed. The loop repeats because several old calls may expire at once.

The comparison must be strict. A request at exactly `t - 3000` is inside `[t - 3000, t]` and must remain. Replacing `<` with `<=` would incorrectly discard a boundary request.

Once the oldest timestamp is not below the lower boundary, every later timestamp is also at least that large because the deque is sorted. No additional element can be expired. The method returns `len(q)`, which is exactly the number of requests still in the window.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 2, 3, 3]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": [["ping", 1], ["ping", 100], ["ping", 3001], ["ping", 3002]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 2, 3, 3]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Scanning an array of all timestamps:** Append :** - **Scanning an array of all timestamps:** Append every call and count values in the range each time. This is simple but can cost `O(m)` per call and `O(m^2)` across the full sequence.
- **Array plus a moving start index:** Keep every timestamp in a list and advance an index past expired values. This also gives amortized `O(1)` query time, but old entries remain allocated unless the list is occasionally compacted. The deque naturally releases them.
- **Binary search over all timestamps:** Since arrival order is sorted, binary search can find the first valid timestamp in `O(log m)` time. It retains every historical call and is slower than the deque's amortized constant time.
- **Balanced tree or ordered multiset:** Such a structure supports general insertions and range counts, but it is unnecessary because timestamps arrive in a much stronger order. It adds logarithmic overhead and implementation complexity.
- **Timestamp exactly at `t - 3000`:** It is valid and must stay. This is the central reason for using `<` rather than `<=` in the expiration test.
- **A very large jump in time:** Many values may be popped in one call. The current timestamp remains because it was appended first and can never be smaller than its own lower boundary.
- **Safety of reading the front:** `q[0]` cannot fail inside `ping` because the method appends `t` before entering the loop, and that newly appended value is never expired.
- **Strictly increasing timestamps:** The correctness and efficiency rely on this contract. If timestamps could arrive out of order, expired values would not necessarily form a prefix and a deque alone would not be sufficient.
- **Duplicate timestamps:** The stated contract excludes them. If nondecreasing timestamps were allowed, the same deque mechanics would still count duplicates correctly, but that is not the interface guarantee being used.
- **Inclusive upper boundary:** The new request at `t` is always counted. Appending before returning the length handles this automatically.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(m)$. Let `m` be the total number of calls made to `ping`.
- **Auxiliary Space Complexity:** $O(m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
