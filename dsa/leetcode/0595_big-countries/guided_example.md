# Guided Example: Big Countries

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"World": [{"name": "AreaLand", "continent": "X", "area": 3000000, "population": 1, "gdp": 10}, {"name": "Small", "continent": "X", "area": 2999999, "population": 24999999, "gdp": 20}]}}`
- **Required output:** `{"columns": ["name", "population", "area"], "rows": [["AreaLand", 1, 3000000]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `World`

The objective is to compute `{"columns": ["name", "population", "area"], "rows": [["AreaLand", 1, 3000000]]}` from `{"tables": {"World": [{"name": "AreaLand", "continent": "X", "area": 3000000, "population": 1, "gdp": 10}, {"name": "Small", "continent": "X", "area": 2999999, "population": 24999999, "gdp": 20}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Translating “at least”

“At least three million” means `area >= 3000000`. Equality must qualify. Using `>` would wrongly exclude a country whose area is exactly three million.

Likewise, “at least twenty-five million” becomes `population >= 25000000`.

The two conditions are joined by `OR`:



`OR` matches the definition: satisfying either condition is sufficient. `AND` would require a country to meet both and would incorrectly discard large-area countries with smaller populations and populous countries with smaller areas.

For example, Afghanistan in the sample has area below three million but population 25,500,100, so the second predicate is true and the row remains. Algeria also qualifies through population even though its area is below the area threshold. Albania satisfies neither and is removed.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"World": [{"name": "AreaLand", "continent": "X", "area": 3000000, "population": 1, "gdp": 10}, {"name": "Small", "continent": "X", "area": 2999999, "population": 24999999, "gdp": 20}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Projection is part of the contract

`SELECT name, population, area` returns exactly three requested columns and in that order. `continent` and `gdp` help describe the table but play no role in either classification or output. `SELECT *` would expose unwanted columns and fail the expected result schema.

The result may be returned in any order, so the query does not include `ORDER BY`. Adding one would not improve correctness and could force avoidable sorting work.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why no `DISTINCT` is necessary

`name` is the primary key, so each row represents a unique country. Filtering cannot duplicate rows; it only retains or discards each one. `DISTINCT` would therefore be redundant.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["name", "population", "area"], "rows": [["AreaLand", 1, 3000000]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"World": [{"name": "AreaLand", "continent": "X", "area": 3000000, "population": 1, "gdp": 10}, {"name": "Small", "continent": "X", "area": 2999999, "population": 24999999, "gdp": 20}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["name", "population", "area"], "rows": [["AreaLand", 1, 3000000]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **`UNION` of two filters:** Query large-area countries and populous countries separately, then union them. `UNION` must remove duplicates for countries satisfying both; `UNION ALL` would incorrectly repeat them.
- **`AND` instead of `OR`:** Incorrect because the definition requires either threshold, not both.
- **Strict comparison:** `>` is incorrect at the exact boundary; “at least” requires `>=`.
- **`SELECT *`:** Returns extra `continent` and `gdp` columns not requested.
- **Country meeting both thresholds:** It appears once because one input row passes one combined predicate.
- **Exactly 3,000,000 area:** Qualifies through the inclusive area comparison.
- **Exactly 25,000,000 population:** Qualifies through the inclusive population comparison.
- **Neither threshold:** Must be excluded even if GDP is large; GDP is irrelevant.
- **Primary-key names:** Unique country names mean no deduplication is needed.
- **Any output order:** Omitting `ORDER BY` is intentional and avoids an unnecessary sort.
- **Potential `NULL` values:** SQL comparisons with `NULL` are unknown. If nullability were part of the domain, its intended classification would need specification; do not silently treat missing as zero without a rule.
- **Index behavior:** Separate indexes on area and population may help an optimizer, but the query remains correct without them.
- **Complexity fidelity:** The exact relational operation is filtering, not sorting; its natural full-scan time is $O(n)$ despite the manifest’s conservative $O(n\log n)$ label.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of rows in `World`. With no useful index, a standard execution scans all $n$ rows, evaluates two constant-time comparisons, and streams matching columns. Logical time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
