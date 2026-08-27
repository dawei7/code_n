# Guided Example: The Airport With the Most Traffic

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Flights": [{"departure_airport": 1, "arrival_airport": 2, "flights_count": 4}, {"departure_airport": 2, "arrival_airport": 1, "flights_count": 5}, {"departure_airport": 2, "arrival_airport": 4, "flights_count": 5}]}}`
- **Required output:** `{"columns": ["airport_id"], "rows": [[2]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Flights`

The objective is to compute `{"columns": ["airport_id"], "rows": [[2]]}` from `{"tables": {"Flights": [{"departure_airport": 1, "arrival_airport": 2, "flights_count": 4}, {"departure_airport": 2, "arrival_airport": 1, "flights_count": 5}, {"departure_airport": 2, "arrival_airport": 4, "flights_count": 5}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Normalize departures and arrivals into one airport column

Every flight row contributes `flights_count` traffic to two endpoint roles: its departure airport and its arrival airport. Aggregating only one original column would miss half of the traffic.

The CTE `T` creates rows in both orientations:

- `SELECT * FROM Flights` keeps `departure_airport` as the first column;
- `SELECT arrival_airport, departure_airport, flights_count FROM Flights` swaps the endpoints, making the original arrival airport the first column.

Although the column retains the name `departure_airport` from the first query, after normalization it means “the airport receiving this traffic contribution.” The second column is no longer used by the later aggregation.

For route 1 to 2 with count 4, the normalized data includes a row whose first airport is 1 and another whose first airport is 2. Both airports consequently receive a contribution of 4.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Flights": [{"departure_airport": 1, "arrival_airport": 2, "flights_count": 4}, {"departure_airport": 2, "arrival_airport": 1, "flights_count": 5}, {"departure_airport": 2, "arrival_airport": 4, "flights_count": 5}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Aggregate all contributions by airport

The second CTE `P` groups `T` by its first column and calculates

`SUM(flights_count) AS cnt`.

This combines outbound and inbound traffic contributions into one total for each airport.

In the first example, airport 1 receives 4 from departing on route 1 to 2 and 5 from arriving on route 2 to 1, totaling 9. Airport 2 receives contributions 4, 5, and 5 from its incident routes, totaling 14.

`GROUP BY 1` means group by the first selected expression, which is `departure_airport`. Writing the name explicitly would be equivalent and somewhat more verbose.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The second CTE `P` groups `T` by its first column and calcul... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Select every airport tied for the maximum

The scalar subquery `SELECT MAX(cnt) FROM P` finds the greatest aggregated traffic total.

The outer query keeps every row of `P` whose `cnt` equals that maximum. This equality, rather than a one-row `ORDER BY ... LIMIT 1`, preserves ties.

The airport column is renamed `airport_id` to match the required result schema. No `ORDER BY` is needed because any row order is allowed.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["airport_id"], "rows": [[2]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Flights": [{"departure_airport": 1, "arrival_airport": 2, "flights_count": 4}, {"departure_airport": 2, "arrival_airport": 1, "flights_count": 5}, {"departure_airport": 2, "arrival_airport": 4, "flights_count": 5}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["airport_id"], "rows": [[2]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Use `UNION ALL`:** This is the correct weighte:** - **Use `UNION ALL`:** This is the correct weighted-event normalization because every route must contribute independently to both endpoints.
- **Separate departure and arrival aggregates:** Aggregate each role, combine airport totals, and aggregate again. It is correct but more verbose than a safe `UNION ALL` normalization.
- **Window rank:** `DENSE_RANK` over descending traffic can select rank one and preserve ties, but the scalar maximum is simpler.
- **`ORDER BY cnt DESC LIMIT 1`:** Incorrect when multiple airports tie for maximum.
- **Reciprocal equal-count routes:** The exact `UNION` may collapse contributions and undercount traffic.
- **Primary key interpretation:** It prevents duplicate directed pairs but does not make all normalized endpoint triples unique.
- **Airport appearing only as arrival:** The swapped branch brings it into the aggregate.
- **Airport appearing only as departure:** The original branch includes it.
- **Tied totals:** Equality with the global maximum returns every tied airport.
- **Any result order:** No sort is required.
- **Exact output alias:** The selected column must be named `airport_id`.
- **Empty input:** `P` is empty and the query returns no airport rows.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N log N)$. Let $N$ be the number of `Flights` rows.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
