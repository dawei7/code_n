# Guided Example: Daily Leads and Partners

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"DailySales": [{"date_id": "2020-12-08", "make_name": "toyota", "lead_id": 0, "partner_id": 1}, {"date_id": "2020-12-08", "make_name": "toyota", "lead_id": 1, "partner_id": 0}, {"date_id": "2020-12-08", "make_name": "toyota", "lead_id": 1, "partner_id": 2}, {"date_id": "2020-12-07", "make_name": "toyota", "lead_id": 0, "partner_id": 2}, {"date_id": "2020-12-07", "make_name": "toyota", "lead_id": 0, "partner_id": 1}, {"date_id": "2020-12-08", "make_name": "honda", "lead_id": 1, "partner_id": 2}, {"date_id": "2020-12-08", "make_name": "honda", "lead_id": 2, "partner_id": 1}, {"date_id": "2020-12-07", "make_name": "honda", "lead_id": 0, "partner_id": 1}, {"date_id": "2020-12-07", "make_name": "honda", "lead_id": 1, "partner_id": 2}, {"date_id": "2020-12-07", "make_name": "honda", "lead_id": 2, "partner_id": 1}]}}`
- **Required output:** `{"columns": ["date_id", "make_name", "unique_leads", "unique_partners"], "rows": [["2020-12-08", "toyota", 2, 3], ["2020-12-07", "toyota", 1, 2], ["2020-12-08", "honda", 2, 2], ["2020-12-07", "honda", 3, 2]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `DailySales`

The objective is to compute `{"columns": ["date_id", "make_name", "unique_leads", "unique_partners"], "rows": [["2020-12-08", "toyota", 2, 3], ["2020-12-07", "toyota", 1, 2], ["2020-12-08", "honda", 2, 2], ["2020-12-07", "honda", 3, 2]]}` from `{"tables": {"DailySales": [{"date_id": "2020-12-08", "make_name": "toyota", "lead_id": 0, "partner_id": 1}, {"date_id": "2020-12-08", "make_name": "toyota", "lead_id": 1, "partner_id": 0}, {"date_id": "2020-12-08", "make_name": "toyota", "lead_id": 1, "partner_id": 2}, {"date_id": "2020-12-07", "make_name": "toyota", "lead_id": 0, "partner_id": 2}, {"date_id": "2020-12-07", "make_name": "toyota", "lead_id": 0, "partner_id": 1}, {"date_id": "2020-12-08", "make_name": "honda", "lead_id": 1, "partner_id": 2}, {"date_id": "2020-12-08", "make_name": "honda", "lead_id": 2, "partner_id": 1}, {"date_id": "2020-12-07", "make_name": "honda", "lead_id": 0, "partner_id": 1}, {"date_id": "2020-12-07", "make_name": "honda", "lead_id": 1, "partner_id": 2}, {"date_id": "2020-12-07", "make_name": "honda", "lead_id": 2, "partner_id": 1}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Define one group by both requested dimensions

The result needs a separate row for each unique combination of `date_id` and `make_name`. Grouping by only the date would mix different product makes, while grouping only by make would mix different days.

The query uses `GROUP BY 1, 2`. In MySQL, these ordinals refer to the first and second select-list expressions: `date_id` and `make_name`. Thus it is equivalent to `GROUP BY date_id, make_name`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"DailySales": [{"date_id": "2020-12-08", "make_name": "toyota", "lead_id": 0, "partner_id": 1}, {"date_id": "2020-12-08", "make_name": "toyota", "lead_id": 1, "partner_id": 0}, {"date_id": "2020-12-08", "make_name": "toyota", "lead_id": 1, "partner_id": 2}, {"date_id": "2020-12-07", "make_name": "toyota", "lead_id": 0, "partner_id": 2}, {"date_id": "2020-12-07", "make_name": "toyota", "lead_id": 0, "partner_id": 1}, {"date_id": "2020-12-08", "make_name": "honda", "lead_id": 1, "partner_id": 2}, {"date_id": "2020-12-08", "make_name": "honda", "lead_id": 2, "partner_id": 1}, {"date_id": "2020-12-07", "make_name": "honda", "lead_id": 0, "partner_id": 1}, {"date_id": "2020-12-07", "make_name": "honda", "lead_id": 1, "partner_id": 2}, {"date_id": "2020-12-07", "make_name": "honda", "lead_id": 2, "partner_id": 1}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Count unique leads inside each group

`COUNT(DISTINCT lead_id)` forms the set of distinct lead IDs occurring among rows with that date and make, then returns its cardinality.

Plain `COUNT(lead_id)` would count duplicate occurrences and would be wrong because the source table has no primary key and may contain repeated rows. `DISTINCT` is essential.

The alias `unique_leads` gives the aggregate its required output name.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `COUNT(DISTINCT lead_id)` forms the set of distinct lead IDs... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count partners independently

`COUNT(DISTINCT partner_id)` performs a separate distinct count in the same group. It does not count distinct lead-partner pairs and does not require one-to-one relationships.

For example, one lead can appear with three partners. It contributes one to `unique_leads` while those partner values may contribute three to `unique_partners`. The two requested metrics describe independent sets.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["date_id", "make_name", "unique_leads", "unique_partners"], "rows": [["2020-12-08", "toyota", 2, 3], ["2020-12-07", "toyota", 1, 2], ["2020-12-08", "honda", 2, 2], ["2020-12-07", "honda", 3, 2]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"DailySales": [{"date_id": "2020-12-08", "make_name": "toyota", "lead_id": 0, "partner_id": 1}, {"date_id": "2020-12-08", "make_name": "toyota", "lead_id": 1, "partner_id": 0}, {"date_id": "2020-12-08", "make_name": "toyota", "lead_id": 1, "partner_id": 2}, {"date_id": "2020-12-07", "make_name": "toyota", "lead_id": 0, "partner_id": 2}, {"date_id": "2020-12-07", "make_name": "toyota", "lead_id": 0, "partner_id": 1}, {"date_id": "2020-12-08", "make_name": "honda", "lead_id": 1, "partner_id": 2}, {"date_id": "2020-12-08", "make_name": "honda", "lead_id": 2, "partner_id": 1}, {"date_id": "2020-12-07", "make_name": "honda", "lead_id": 0, "partner_id": 1}, {"date_id": "2020-12-07", "make_name": "honda", "lead_id": 1, "partner_id": 2}, {"date_id": "2020-12-07", "make_name": "honda", "lead_id": 2, "partner_id": 1}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["date_id", "make_name", "unique_leads", "unique_partners"], "rows": [["2020-12-08", "toyota", 2, 3], ["2020-12-07", "toyota", 1, 2], ["2020-12-08", "honda", 2, 2], ["2020-12-07", "honda", 3, 2]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **`SELECT DISTINCT` before grouping:** Deduplica:** - **`SELECT DISTINCT` before grouping:** Deduplicating whole rows first is unnecessary because distinct lead and partner counts are independent; whole-row duplicates already have no effect.
- **Count distinct pairs:** `COUNT(DISTINCT lead_id, partner_id)` answers how many unique relationships exist, not either requested metric.
- **Two separate subqueries:** They can compute leads and partners then join by date and make, but one grouped scan is clearer.
- **Duplicate rows:** Both distinct counts remain unchanged.
- **Same lead with multiple partners:** The lead counts once while each unique partner counts independently.
- **Same partner with multiple leads:** The partner counts once while unique leads are counted independently.
- **One row in a group:** Both counts are one for non-null IDs.
- **Null IDs outside the stated model:** `COUNT(DISTINCT column)` ignores null, which should be confirmed against any generalized business rule.
- **Ordinal grouping:** `GROUP BY 1, 2` is concise but sensitive to select-list reordering; explicit column names are more maintainable.
- **Any-order result:** No ordering clause is needed, and consumers must not assume a stable implicit order.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R)$. Let `R` be the number of rows, `G` the number of date-make groups, and `D` the total number of distinct ID entries maintained across group aggregates. A hash-based execution can scan rows in expected $O(R)$ time while maintaining per-group distinct sets.
- **Auxiliary Space Complexity:** $O(G+D)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
