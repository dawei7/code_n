# Guided Example: The Category of Each Member in the Store

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Members": [{"member_id": 9, "name": "Alice"}, {"member_id": 11, "name": "Bob"}, {"member_id": 3, "name": "Winston"}, {"member_id": 8, "name": "Hercy"}, {"member_id": 1, "name": "Narihan"}], "Visits": [{"visit_id": 22, "member_id": 11, "visit_date": "2021-10-28"}, {"visit_id": 16, "member_id": 11, "visit_date": "2021-01-12"}, {"visit_id": 18, "member_id": 9, "visit_date": "2021-12-10"}, {"visit_id": 19, "member_id": 3, "visit_date": "2021-10-19"}, {"visit_id": 12, "member_id": 11, "visit_date": "2021-03-01"}, {"visit_id": 17, "member_id": 8, "visit_date": "2021-05-07"}, {"visit_id": 21, "member_id": 9, "visit_date": "2021-05-12"}], "Purchases": [{"visit_id": 12, "charged_amount": 2000}, {"visit_id": 18, "charged_amount": 9000}, {"visit_id": 17, "charged_amount": 7000}]}}`
- **Required output:** `{"columns": ["member_id", "name", "category"], "rows": [[1, "Narihan", "Bronze"], [3, "Winston", "Silver"], [8, "Hercy", "Diamond"], [9, "Alice", "Gold"], [11, "Bob", "Silver"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Members`

The objective is to compute `{"columns": ["member_id", "name", "category"], "rows": [[1, "Narihan", "Bronze"], [3, "Winston", "Silver"], [8, "Hercy", "Diamond"], [9, "Alice", "Gold"], [11, "Bob", "Silver"]]}` from `{"tables": {"Members": [{"member_id": 9, "name": "Alice"}, {"member_id": 11, "name": "Bob"}, {"member_id": 3, "name": "Winston"}, {"member_id": 8, "name": "Hercy"}, {"member_id": 1, "name": "Narihan"}], "Visits": [{"visit_id": 22, "member_id": 11, "visit_date": "2021-10-28"}, {"visit_id": 16, "member_id": 11, "visit_date": "2021-01-12"}, {"visit_id": 18, "member_id": 9, "visit_date": "2021-12-10"}, {"visit_id": 19, "member_id": 3, "visit_date": "2021-10-19"}, {"visit_id": 12, "member_id": 11, "visit_date": "2021-03-01"}, {"visit_id": 17, "member_id": 8, "visit_date": "2021-05-07"}, {"visit_id": 21, "member_id": 9, "visit_date": "2021-05-12"}], "Purchases": [{"visit_id": 12, "charged_amount": 2000}, {"visit_id": 18, "charged_amount": 9000}, {"visit_id": 17, "charged_amount": 7000}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Preserve every member with left joins

The report must include members who never visited. Starting from `Members AS m` and using a left join to `Visits` ensures every member contributes at least one result row.

When a member has no visit, all joined `v` columns are `NULL`. A normal inner join would discard that member and make the Bronze category impossible to report.

The second left join connects each visit to an optional purchase by matching `visit_id`. A visit without a purchase remains present with null purchase columns.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Members": [{"member_id": 9, "name": "Alice"}, {"member_id": 11, "name": "Bob"}, {"member_id": 3, "name": "Winston"}, {"member_id": 8, "name": "Hercy"}, {"member_id": 1, "name": "Narihan"}], "Visits": [{"visit_id": 22, "member_id": 11, "visit_date": "2021-10-28"}, {"visit_id": 16, "member_id": 11, "visit_date": "2021-01-12"}, {"visit_id": 18, "member_id": 9, "visit_date": "2021-12-10"}, {"visit_id": 19, "member_id": 3, "visit_date": "2021-10-19"}, {"visit_id": 12, "member_id": 11, "visit_date": "2021-03-01"}, {"visit_id": 17, "member_id": 8, "visit_date": "2021-05-07"}, {"visit_id": 21, "member_id": 9, "visit_date": "2021-05-12"}], "Purchases": [{"visit_id": 12, "charged_amount": 2000}, {"visit_id": 18, "charged_amount": 9000}, {"visit_id": 17, "charged_amount": 7000}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the joined rows have the right counting unit

`visit_id` is unique in `Visits`, and it is also unique in `Purchases`. Therefore each visit joins to at most one purchase row.

This prevents a purchase join from duplicating a visit. Within one member group, there is one joined row per visit, with `charged_amount` nonnull exactly when that visit has a recorded purchase under the ordinary nonnull data model.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count visits with a nullable joined key

`COUNT(v.visit_id)` counts only nonnull visit IDs. For a member with real visits, it counts those visits. For a never-visiting member's null-extended row, it returns zero.

Using `COUNT(*)` would be wrong for Bronze detection because the left join still produces one placeholder row, causing a never-visiting member to appear to have one visit.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["member_id", "name", "category"], "rows": [[1, "Narihan", "Bronze"], [3, "Winston", "Silver"], [8, "Hercy", "Diamond"], [9, "Alice", "Gold"], [11, "Bob", "Silver"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Members": [{"member_id": 9, "name": "Alice"}, {"member_id": 11, "name": "Bob"}, {"member_id": 3, "name": "Winston"}, {"member_id": 8, "name": "Hercy"}, {"member_id": 1, "name": "Narihan"}], "Visits": [{"visit_id": 22, "member_id": 11, "visit_date": "2021-10-28"}, {"visit_id": 16, "member_id": 11, "visit_date": "2021-01-12"}, {"visit_id": 18, "member_id": 9, "visit_date": "2021-12-10"}, {"visit_id": 19, "member_id": 3, "visit_date": "2021-10-19"}, {"visit_id": 12, "member_id": 11, "visit_date": "2021-03-01"}, {"visit_id": 17, "member_id": 8, "visit_date": "2021-05-07"}, {"visit_id": 21, "member_id": 9, "visit_date": "2021-05-12"}], "Purchases": [{"visit_id": 12, "charged_amount": 2000}, {"visit_id": 18, "charged_amount": 9000}, {"visit_id": 17, "charged_amount": 7000}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["member_id", "name", "category"], "rows": [[1, "Narihan", "Bronze"], [3, "Winston", "Silver"], [8, "Hercy", "Diamond"], [9, "Alice", "Gold"], [11, "Bob", "Silver"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Aggregate visits first:** Compute visit and purchase counts per member in a subquery, then left join that compact result to `Members`.
- **Conditional aggregation:** Count purchases with `SUM(p.visit_id IS NOT NULL)` instead of `COUNT(charged_amount)`.
- **Cross-multiplied thresholds:** Compare `100 * purchases >= 80 * visits` and similarly for Gold to avoid division.
- **No visits:** Bronze, detected with `COUNT(v.visit_id)=0`.
- **Visits but no purchases:** Silver with zero-percent conversion, not Bronze.
- **Exactly 50 percent:** Gold.
- **Exactly 80 percent:** Diamond.
- **Above 80 percent:** First matching branch remains Diamond.
- **One purchase per visit:** Enforced by unique `Purchases.visit_id`, preventing visit duplication.
- **Null charged amount outside the ordinary model:** `COUNT(charged_amount)` would not count that purchase row.
- **`COUNT(*)`:** Incorrect for no-visit detection because left joins create a placeholder row.
- **Any output order:** No sort is needed.
- **Functional dependency:** Unique `member_id` determines `name` within each group.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M+V+P)$. Let $M$, $V$, and $P$ be the numbers of member, visit, and purchase rows. With indexes or hash joins on the key columns, joining and grouping can be performed in expected $O(M+V+P)$ time and $O(M+V+P)$ working space in a broad upper-bound model.
- **Auxiliary Space Complexity:** $O(M+V+P)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
