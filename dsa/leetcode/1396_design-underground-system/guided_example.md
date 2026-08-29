# Guided Example: Design Underground System

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": [["checkIn", [1, "A", 3]], ["checkOut", [1, "B", 13]], ["getAverageTime", ["A", "B"]]]}`
- **Required output:** `[null, null, 10.0]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

An underground railway system is keeping track of customer travel times between different stations. They are using this data to calculate the average time it takes to travel from one station to another.

The objective is to compute `[null, null, 10.0]` from `{"operations": [["checkIn", [1, "A", 3]], ["checkOut", [1, "B", 13]], ["getAverageTime", ["A", "B"]]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Store only the information future operations need

The system receives three kinds of calls. A check-in starts a trip, a check-out finishes one, and an average query asks about all completed trips for a directed station pair.

Two dictionaries separate these responsibilities:

- `ts` maps a customer ID to that customer's most recent check-in time and start station.
- `d` maps a pair `(startStation, endStation)` to the total duration and number of completed trips on that route.

The design never stores every individual finished duration. An average needs only the sum and the count, because

$$
\text{average}=\frac{\text{total duration}}{\text{number of trips}}.
$$

This compression keeps queries constant time even after many journeys.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": [["checkIn", [1, "A", 3]], ["checkOut", [1, "B", 13]], ["getAverageTime", ["A", "B"]]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Check-in

`ts[id] = (t, stationName)` records the two facts that a later check-out does not provide: the start time and start station. Customer ID is the lookup key because interleaved calls for many customers may occur before any particular one checks out.

The contract guarantees one active location per customer, so a valid `checkIn` does not overwrite an unfinished trip. If the same customer takes another trip later, the new check-in overwrites the old completed-trip data stored under that ID.

The tuple order is time first and station second. `checkOut` unpacks it as `t0, station` in the same order.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Check-out

For a customer checking out at time `t` from `stationName`, the stored tuple identifies the route start. The trip duration is `t - t0`, which is positive by the consistency guarantee.

The directed route key is `(station, stationName)`. Direction matters: Leyton to Waterloo and Waterloo to Leyton are different dictionary entries and can have different averages.

`d.get(key, (0, 0))` returns the previous total and trip count or zeroes for a route seen for the first time. The update

`(x[0] + t - t0, x[1] + 1)`

adds the new duration and increments the number of completed journeys exactly once.

For two trips lasting 12 and 10 minutes, the route entry evolves from absent to `(12,1)` and then `(22,2)`. No averaging or floating-point rounding occurs during updates.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[null, null, 10.0]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": [["checkIn", [1, "A", 3]], ["checkOut", [1, "B", 13]], ["getAverageTime", ["A", "B"]]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[null, null, 10.0]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Remove check-ins on checkout:** Use `pop` to keep only active journeys. This improves long-running memory without changing expected operation time.
- **Store all trip durations:** It preserves raw data but uses space per journey and makes naive average queries slower.
- **Store a running average:** It saves neither the need for a count nor much space and introduces compounded floating-point error.
- **Nested route dictionaries:** Map start station to a dictionary of end stations. It is equivalent but more verbose than a tuple key.
- **Reverse direction:** `(A,B)` and `(B,A)` are distinct keys, as required.
- **First trip on a route:** The default `(0,0)` makes its total and count initialize correctly.
- **Interleaved passengers:** Customer-ID lookup pairs each checkout with its own check-in regardless of other calls.
- **Repeated customer trips:** A later valid check-in overwrites the retained old tuple before its next checkout.
- **Query before any trip:** The contract excludes it; otherwise direct dictionary access would raise a key error.
- **Invalid checkout:** The contract guarantees consistency; otherwise missing `id` would raise a key error.
- **Chronological events:** Positive duration follows from `t0 < t` and no timestamp sorting is needed.
- **Real-world persistence:** In-memory dictionaries satisfy the coding contract but would need durable, concurrent storage in a production transit system.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Under expected constant-time dictionary operations, each individual `checkIn`, `checkOut`, and `getAverageTime` call is $O(1)$. Across $q$ calls, total time is $O(q)$, matching the manifest.
- **Auxiliary Space Complexity:** $O(A+R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
