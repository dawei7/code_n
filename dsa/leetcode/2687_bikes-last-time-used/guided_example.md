# Guided Example: Bikes Last Time Used 

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Bikes": [{"ride_id": 1, "bike_number": "W00576", "start_time": "2012-03-25 11:30:00", "end_time": "2012-03-25 12:40:00"}, {"ride_id": 2, "bike_number": "W00300", "start_time": "2012-03-25 10:30:00", "end_time": "2012-03-25 10:50:00"}, {"ride_id": 3, "bike_number": "W00455", "start_time": "2012-03-26 14:30:00", "end_time": "2012-03-26 17:40:00"}, {"ride_id": 4, "bike_number": "W00455", "start_time": "2012-03-25 12:30:00", "end_time": "2012-03-25 13:40:00"}, {"ride_id": 5, "bike_number": "W00576", "start_time": "2012-03-25 08:10:00", "end_time": "2012-03-25 09:10:00"}, {"ride_id": 6, "bike_number": "W00576", "start_time": "2012-03-28 02:30:00", "end_time": "2012-03-28 02:50:00"}]}}`
- **Required output:** `{"columns": ["bike_number", "end_time"], "rows": [["W00576", "2012-03-28 02:50:00"], ["W00455", "2012-03-26 17:40:00"], ["W00300", "2012-03-25 10:50:00"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Bikes`

The objective is to compute `{"columns": ["bike_number", "end_time"], "rows": [["W00576", "2012-03-28 02:50:00"], ["W00455", "2012-03-26 17:40:00"], ["W00300", "2012-03-25 10:50:00"]]}` from `{"tables": {"Bikes": [{"ride_id": 1, "bike_number": "W00576", "start_time": "2012-03-25 11:30:00", "end_time": "2012-03-25 12:40:00"}, {"ride_id": 2, "bike_number": "W00300", "start_time": "2012-03-25 10:30:00", "end_time": "2012-03-25 10:50:00"}, {"ride_id": 3, "bike_number": "W00455", "start_time": "2012-03-26 14:30:00", "end_time": "2012-03-26 17:40:00"}, {"ride_id": 4, "bike_number": "W00455", "start_time": "2012-03-25 12:30:00", "end_time": "2012-03-25 13:40:00"}, {"ride_id": 5, "bike_number": "W00576", "start_time": "2012-03-25 08:10:00", "end_time": "2012-03-25 09:10:00"}, {"ride_id": 6, "bike_number": "W00576", "start_time": "2012-03-28 02:30:00", "end_time": "2012-03-28 02:50:00"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Define “last used” by the latest end time

Each row is one bike ride. For a fixed bike, the requested last-use timestamp is the greatest `end_time` among all of that bike's rides.

SQL's `MAX` aggregate expresses exactly this selection. Datetime values have chronological ordering, so the maximum is the most recent timestamp.

The query does not need the row's `ride_id` or `start_time` to determine when a ride finished.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Bikes": [{"ride_id": 1, "bike_number": "W00576", "start_time": "2012-03-25 11:30:00", "end_time": "2012-03-25 12:40:00"}, {"ride_id": 2, "bike_number": "W00300", "start_time": "2012-03-25 10:30:00", "end_time": "2012-03-25 10:50:00"}, {"ride_id": 3, "bike_number": "W00455", "start_time": "2012-03-26 14:30:00", "end_time": "2012-03-26 17:40:00"}, {"ride_id": 4, "bike_number": "W00455", "start_time": "2012-03-25 12:30:00", "end_time": "2012-03-25 13:40:00"}, {"ride_id": 5, "bike_number": "W00576", "start_time": "2012-03-25 08:10:00", "end_time": "2012-03-25 09:10:00"}, {"ride_id": 6, "bike_number": "W00576", "start_time": "2012-03-28 02:30:00", "end_time": "2012-03-28 02:50:00"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Create one group per bike

`GROUP BY bike_number` partitions the `Bikes` table into all rides belonging to the same bike.

Within each group, `MAX(end_time)` examines every ending timestamp and returns one value. The result therefore has exactly one row per distinct bike number.

This avoids returning several rides for a bike or requiring a separate lookup after identifying its latest time.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `GROUP BY bike_number` partitions the `Bikes` table into all... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Name the aggregate as the expected column

The selected expression is:

`MAX(end_time) AS end_time`.

The alias makes the grouped maximum appear under the expected output name `end_time` rather than a database-generated expression label.

It also allows the later `ORDER BY end_time DESC` to refer clearly to the aggregated result.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["bike_number", "end_time"], "rows": [["W00576", "2012-03-28 02:50:00"], ["W00455", "2012-03-26 17:40:00"], ["W00300", "2012-03-25 10:50:00"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Bikes": [{"ride_id": 1, "bike_number": "W00576", "start_time": "2012-03-25 11:30:00", "end_time": "2012-03-25 12:40:00"}, {"ride_id": 2, "bike_number": "W00300", "start_time": "2012-03-25 10:30:00", "end_time": "2012-03-25 10:50:00"}, {"ride_id": 3, "bike_number": "W00455", "start_time": "2012-03-26 14:30:00", "end_time": "2012-03-26 17:40:00"}, {"ride_id": 4, "bike_number": "W00455", "start_time": "2012-03-25 12:30:00", "end_time": "2012-03-25 13:40:00"}, {"ride_id": 5, "bike_number": "W00576", "start_time": "2012-03-25 08:10:00", "end_time": "2012-03-25 09:10:00"}, {"ride_id": 6, "bike_number": "W00576", "start_time": "2012-03-28 02:30:00", "end_time": "2012-03-28 02:50:00"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["bike_number", "end_time"], "rows": [["W00576", "2012-03-28 02:50:00"], ["W00455", "2012-03-26 17:40:00"], ["W00300", "2012-03-25 10:50:00"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Window function with row numbers:** Can rank r:** - **Window function with row numbers:** Can rank rides per bike and keep rank one, but returns more row detail than needed.
- **Anti-join against later rides:** Correct when carefully written, but more complex and potentially more expensive.
- **Correlated `MAX` subquery:** Produces the right value but may repeat aggregation for many rows.
- **Maximum ride ID:** Incorrect because unique IDs are not guaranteed chronological.
- **Maximum start time:** Answers a different question from latest end time.
- **One ride for a bike:** Its end time is returned directly by `MAX`.
- **Several rides for a bike:** Only the greatest ending timestamp survives.
- **Equal latest times across bikes:** Relative tie order is unspecified without a secondary key.
- **Equal latest times within one bike:** The grouped result still contains one bike row.
- **Descending direction:** Required to place most recently used bikes first.
- **Column alias:** Ensures the aggregate has the expected output name.
- **Source preservation:** The query reads and summarizes rows without modifying `Bikes`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R log R)$. Let $R$ be the number of ride rows and $B$ the number of distinct bikes. Reading and aggregating rows requires at least $O(R)$ work. Without assuming a supporting index, grouping and sorting are conservatively bounded by $O(R\log R)$ time.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
