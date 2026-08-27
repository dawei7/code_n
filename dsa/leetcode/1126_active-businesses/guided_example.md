# Guided Example: Active Businesses

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Events": [{"business_id": 1, "event_type": "views", "occurrences": 10}]}}`
- **Required output:** `{"columns": ["business_id"], "rows": []}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Events`

The objective is to compute `{"columns": ["business_id"], "rows": []}` from `{"tables": {"Events": [{"business_id": 1, "event_type": "views", "occurrences": 10}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Compute a separate benchmark for each event type

Activity values from different event types are not comparable through one global average. The derived table groups `Events` by `event_type` and computes `AVG(occurrences)` for each group.

Each derived row represents one event type and the average among only businesses that have a row for that type, exactly matching the definition.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Events": [{"business_id": 1, "event_type": "views", "occurrences": 10}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Join each business event to its matching average

The outer Events row `t1` is joined to derived row `t2` on equal `event_type`. Every business-event occurrence value is therefore placed beside the correct benchmark.

The `WHERE` predicate retains only rows where the business’s value is strictly greater than that event average. Equality is excluded because the definition says “strictly greater.”

After this filter, every remaining row is one event type on which one business performs above average.

The join is inner because every outer Events row has an event type that necessarily appears in the grouped averages derived from the same table. No source row can lack a benchmark, so a left join would add no information.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The outer Events row `t1` is joined to derived row `t2` on e... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count qualifying event types per business

The source grain has composite primary key `(business_id, event_type)`, so one business has at most one row for an event type. Consequently, counting filtered rows after grouping by `business_id` is the same as counting distinct qualifying event types.

`HAVING COUNT(1) > 1` keeps businesses with at least two such types. A business above average for exactly one event is rejected.

Only `business_id` is selected, and result order is unrestricted.

Filtering belongs before the business grouping. If all rows were grouped first, a single aggregate could lose the per-event comparison needed to decide which types qualify. The query preserves the unique business-event grain until each row has been compared with its matching average, then counts only successful comparisons.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["business_id"], "rows": []}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Events": [{"business_id": 1, "event_type": "views", "occurrences": 10}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["business_id"], "rows": []}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Window average:** Add `AVG(occurrences) OVER (:** - **Window average:** Add `AVG(occurrences) OVER (PARTITION BY event_type)` to every row, filter above-average rows, then group by business.
- **Correlated average:** Compare each row with a subquery average for its type. Correct indexing matters to avoid repeated scans.
- **Count distinct event type:** `COUNT(DISTINCT event_type) > 1` is more defensive if uniqueness were absent; the primary key makes plain row count sufficient.
- **Global average:** Incorrect because each event type needs its own peer benchmark.
- **Equality with average:** It does not qualify due to the strict greater-than predicate.
- **Exactly one qualifying type:** The business fails `COUNT(1) > 1`.
- **Exactly two qualifying types:** It passes.
- **One row for an event type:** Its occurrence equals that type’s average, so it cannot qualify.
- **Duplicate business-event rows:** The primary key forbids them, protecting the row-count interpretation.
- **Any result order:** No `ORDER BY` is needed.
- **Empty table:** No averages, joined rows, or businesses are returned.
- **Column spelling:** Every intended `occurences` reference must match the actual schema name `occurrences` for execution.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R \log R)$. Let $R$ be the number of Events rows. A sort-based database plan can group by event type, join, and group by business in $O(R\log R)$ time, matching the manifest.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
