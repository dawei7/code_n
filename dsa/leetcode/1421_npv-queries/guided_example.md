# Guided Example: NPV Queries

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"NPV": [{"id": 1, "year": 2018, "npv": 100}, {"id": 7, "year": 2020, "npv": 30}, {"id": 13, "year": 2019, "npv": 40}, {"id": 1, "year": 2019, "npv": 113}, {"id": 2, "year": 2008, "npv": 121}, {"id": 3, "year": 2009, "npv": 12}, {"id": 11, "year": 2020, "npv": 99}, {"id": 7, "year": 2019, "npv": 0}], "Queries": [{"id": 1, "year": 2019}, {"id": 2, "year": 2008}, {"id": 3, "year": 2009}, {"id": 7, "year": 2018}, {"id": 7, "year": 2019}, {"id": 7, "year": 2020}, {"id": 13, "year": 2019}]}}`
- **Required output:** `{"columns": ["id", "year", "npv"], "rows": [[1, 2019, 113], [2, 2008, 121], [3, 2009, 12], [7, 2018, 0], [7, 2019, 0], [7, 2020, 30], [13, 2019, 40]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `NPV`

The objective is to compute `{"columns": ["id", "year", "npv"], "rows": [[1, 2019, 113], [2, 2008, 121], [3, 2009, 12], [7, 2018, 0], [7, 2019, 0], [7, 2020, 30], [13, 2019, 40]]}` from `{"tables": {"NPV": [{"id": 1, "year": 2018, "npv": 100}, {"id": 7, "year": 2020, "npv": 30}, {"id": 13, "year": 2019, "npv": 40}, {"id": 1, "year": 2019, "npv": 113}, {"id": 2, "year": 2008, "npv": 121}, {"id": 3, "year": 2009, "npv": 12}, {"id": 11, "year": 2020, "npv": 99}, {"id": 7, "year": 2019, "npv": 0}], "Queries": [{"id": 1, "year": 2019}, {"id": 2, "year": 2008}, {"id": 3, "year": 2009}, {"id": 7, "year": 2018}, {"id": 7, "year": 2019}, {"id": 7, "year": 2020}, {"id": 13, "year": 2019}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Treat Queries as the required output population

The result must contain one row for every pair in `Queries`. Some pairs have a stored net present value and some do not, but missing reference data must not remove the query. This immediately makes `Queries` the preserved left side of the join:



A left join emits every left row. When the matching key exists in `NPV`, its columns are attached. When no match exists, SQL still emits the query row and fills columns from the NPV side with `NULL`.

An inner join would be wrong because it would discard queries without a stored value. Starting from NPV would also be wrong because it could emit stored inventory-year pairs nobody requested.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"NPV": [{"id": 1, "year": 2018, "npv": 100}, {"id": 7, "year": 2020, "npv": 30}, {"id": 13, "year": 2019, "npv": 40}, {"id": 1, "year": 2019, "npv": 113}, {"id": 2, "year": 2008, "npv": 121}, {"id": 3, "year": 2009, "npv": 12}, {"id": 11, "year": 2020, "npv": 99}, {"id": 7, "year": 2019, "npv": 0}], "Queries": [{"id": 1, "year": 2019}, {"id": 2, "year": 2008}, {"id": 3, "year": 2009}, {"id": 7, "year": 2018}, {"id": 7, "year": 2019}, {"id": 7, "year": 2020}, {"id": 13, "year": 2019}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Both columns form the lookup key

The schemas define the composite key `(id, year)`. The same inventory ID can have different NPV values in different years. A correct lookup must require equality on both columns.

`USING (id, year)` is concise SQL for joining equal same-named key columns. It is logically equivalent to:



It also merges each equal key pair into one output column, preventing duplicate `id` and `year` columns in the joined row.

Joining only by `id` could attach a value from the wrong year and could multiply one query into several rows when that ID has multiple stored years. Joining only by `year` would mix unrelated inventories.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The schemas define the composite key `(id, year)`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the join cannot duplicate a query

`NPV` has primary key `(id, year)`, so at most one NPV row can match a given query pair. `Queries` also has that primary key, so each requested pair appears at most once. Therefore, the left join produces exactly one result row per Queries row: either one matched row or one unmatched null-extended row.

This uniqueness is what lets the query avoid grouping or deduplication.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["id", "year", "npv"], "rows": [[1, 2019, 113], [2, 2008, 121], [3, 2009, 12], [7, 2018, 0], [7, 2019, 0], [7, 2020, 30], [13, 2019, 40]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"NPV": [{"id": 1, "year": 2018, "npv": 100}, {"id": 7, "year": 2020, "npv": 30}, {"id": 13, "year": 2019, "npv": 40}, {"id": 1, "year": 2019, "npv": 113}, {"id": 2, "year": 2008, "npv": 121}, {"id": 3, "year": 2009, "npv": 12}, {"id": 11, "year": 2020, "npv": 99}, {"id": 7, "year": 2019, "npv": 0}], "Queries": [{"id": 1, "year": 2019}, {"id": 2, "year": 2008}, {"id": 3, "year": 2009}, {"id": 7, "year": 2018}, {"id": 7, "year": 2019}, {"id": 7, "year": 2020}, {"id": 13, "year": 2019}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["id", "year", "npv"], "rows": [[1, 2019, 113], [2, 2008, 121], [3, 2009, 12], [7, 2018, 0], [7, 2019, 0], [7, 2020, 30], [13, 2019, 40]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Correlated scalar subquery:** Look up NPV sepa:** - **Correlated scalar subquery:** Look up NPV separately for every Queries row and wrap the subquery in `COALESCE`. It is correct but can perform repeated lookups and is less direct than one join.
- **Inner join:** This incorrectly removes requested pairs that have no stored NPV value.
- **Right join from NPV:** It can be arranged to preserve Queries, but reversing the table roles makes the intent harder to read.
- **Join by ID only:** This can retrieve a value from the wrong year or duplicate query rows.
- **Join by year only:** This mixes different inventory IDs from the same year.
- **`IFNULL`:** In MySQL, `IFNULL(npv, 0)` is an equivalent two-argument alternative to `COALESCE` here.
- **Stored zero:** It remains zero; `COALESCE` does not treat zero as missing.
- **Missing pair:** The left join produces null only on the NPV side and the fallback becomes zero.
- **Unrequested NPV row:** It is absent because no preserved Queries row points to it.
- **Any-order contract:** No `ORDER BY` is required, and consumers must not infer a stable natural order.
- **Composite primary keys:** Their uniqueness guarantees at most one match on each side and prevents accidental multiplicative joins.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(P+Q)$. Let $P$ be the number of NPV rows and $Q$ the number of Queries rows. With a hash join, building and probing keyed structures takes expected $O(P+Q)$ time. With a suitable composite index on NPV, an execution plan may instead scan Queries and perform indexed lookups. Exact physical cost depends on the database optimizer, available indexes, and data distribution.
- **Auxiliary Space Complexity:** $O(P+Q)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
