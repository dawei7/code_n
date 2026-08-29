# Guided Example: Top Travellers

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Users": [{"id": 1, "name": "Ann"}, {"id": 2, "name": "Bob"}], "Rides": [{"id": 1, "user_id": 1, "distance": 10}, {"id": 2, "user_id": 1, "distance": 15}, {"id": 3, "user_id": 2, "distance": 20}]}}`
- **Required output:** `{"columns": ["name", "travelled_distance"], "rows": [["Ann", 25], ["Bob", 20]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Users`

The objective is to compute `{"columns": ["name", "travelled_distance"], "rows": [["Ann", 25], ["Bob", 20]]}` from `{"tables": {"Users": [{"id": 1, "name": "Ann"}, {"id": 2, "name": "Bob"}], "Rides": [{"id": 1, "user_id": 1, "distance": 10}, {"id": 2, "user_id": 1, "distance": 15}, {"id": 3, "user_id": 2, "distance": 20}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Begin from the table that defines who must appear

The result needs one row for every user, including a user who has never taken a ride. That requirement determines the join direction. `Users` is the preserved table, and `Rides` supplies zero or more matching detail rows:



A regular inner join would retain only users that have a matching ride. A left join instead keeps every row from `Users`. When a user has no match, SQL creates one joined result row whose columns from `Rides` are `NULL`. That synthetic unmatched row is what allows the later aggregation to produce an output row for a non-traveller.

The join predicate `u.id = r.user_id` expresses the schema relationship exactly. A ride belongs to the user whose unique `Users.id` equals its `Rides.user_id`. Joining on `name` would be incorrect because the ride table stores no name and because names need not be safe identifiers.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Users": [{"id": 1, "name": "Ann"}, {"id": 2, "name": "Bob"}], "Rides": [{"id": 1, "user_id": 1, "distance": 10}, {"id": 2, "user_id": 1, "distance": 15}, {"id": 3, "user_id": 2, "distance": 20}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Understand the intermediate joined rows

Before grouping, a user with several rides appears several times. If a user has ride distances 100, 120, and 230, the join produces three rows carrying that user's name and those three distances. A user with one ride appears once. A user with no ride also appears once because of the left join, but that row's `r.distance` is `NULL`.

This multiplicity is useful rather than accidental: the aggregate function can add every ride distance belonging to the same user.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Group by identity, not by display text

The clause



forms one group per user. Since `Users.id` contains unique values, it is the correct identity key. Two different people may have equal names; grouping by `name` would merge their rides and incorrectly return one combined traveller.

The selected `name` is functionally determined by `u.id`: every group represents exactly one Users row and therefore exactly one name. MySQL can return that name alongside the aggregate. Keeping the table alias on `u.id` also makes it unambiguous which identifier defines the group, since both input tables have a column called `id`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["name", "travelled_distance"], "rows": [["Ann", 25], ["Bob", 20]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Users": [{"id": 1, "name": "Ann"}, {"id": 2, "name": "Bob"}], "Rides": [{"id": 1, "user_id": 1, "distance": 10}, {"id": 2, "user_id": 1, "distance": 15}, {"id": 3, "user_id": 2, "distance": 20}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["name", "travelled_distance"], "rows": [["Ann", 25], ["Bob", 20]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Inner join:** This is shorter but wrong for the contract because every user without a ride disappears before aggregation.
- **Correlated subquery per user:** Selecting each user and running a separate sum over `Rides` can express the same result. Without a helpful index it may repeatedly scan rides and be much slower than joining and grouping once.
- **Pre-aggregate then join:** A derived table can first group `Rides` by `user_id` and then left join those totals to `Users`. It is correct and can make the one-row-per-user relationship explicit, but the stored query achieves the same logical result compactly.
- **Window function:** `SUM(distance) OVER (PARTITION BY u.id)` would repeat the total on every joined ride row, so an additional deduplication step would be required. Plain grouping is more direct here.
- **Grouping by name:** This can silently combine different users who share a name. The unique identifier `u.id` is the safe grouping key.
- **Using `COUNT` instead of `SUM`:** Counting rides reports how many journeys occurred, not the total distance travelled.
- **A user with no rides:** The left join preserves the user, `SUM` yields `NULL` for the unmatched group, and `COALESCE` changes it to zero.
- **A user with many rides:** Every matching distance contributes once because each Rides row joins to its one matching user before aggregation.
- **Equal travelled distances:** `ORDER BY 2 DESC` ties, then `ORDER BY 1` places names in ascending order.
- **Equal names for distinct users:** Grouping preserves separate rows because their identifiers differ. Their displayed names and totals may tie completely; the contract does not require another tie-breaker.
- **Ordinal ordering syntax:** `ORDER BY 2 DESC, 1` depends on the select-column positions. Writing `ORDER BY travelled_distance DESC, name ASC` is more self-documenting and equivalent, but the exact stored solution uses ordinals correctly.
- **Null handling location:** Omitting `COALESCE` returns `NULL` rather than zero for a non-traveller. Converting the completed aggregate is the key step because there is no non-null distance to sum in that group.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(U + R + U\log U)$. Let $U$ be the number of rows in `Users` and $R$ the number of rows in `Rides`. Under the usual database execution strategy, scanning the tables and building or probing an index or hash structure for the join and grouping takes expected $O(U + R)$ work. There is one aggregate result per user.
- **Auxiliary Space Complexity:** $O(U)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
