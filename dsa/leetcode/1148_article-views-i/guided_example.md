# Guided Example: Article Views I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Views": [{"article_id": 1, "author_id": 3, "viewer_id": 5, "view_date": "2019-08-01"}, {"article_id": 1, "author_id": 3, "viewer_id": 6, "view_date": "2019-08-02"}, {"article_id": 2, "author_id": 7, "viewer_id": 7, "view_date": "2019-08-01"}, {"article_id": 2, "author_id": 7, "viewer_id": 6, "view_date": "2019-08-02"}, {"article_id": 4, "author_id": 7, "viewer_id": 1, "view_date": "2019-07-22"}, {"article_id": 3, "author_id": 4, "viewer_id": 4, "view_date": "2019-07-21"}, {"article_id": 3, "author_id": 4, "viewer_id": 4, "view_date": "2019-07-21"}]}}`
- **Required output:** `{"columns": ["id"], "rows": [[4], [7]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Views`

The objective is to compute `{"columns": ["id"], "rows": [[4], [7]]}` from `{"tables": {"Views": [{"article_id": 1, "author_id": 3, "viewer_id": 5, "view_date": "2019-08-01"}, {"article_id": 1, "author_id": 3, "viewer_id": 6, "view_date": "2019-08-02"}, {"article_id": 2, "author_id": 7, "viewer_id": 7, "view_date": "2019-08-01"}, {"article_id": 2, "author_id": 7, "viewer_id": 6, "view_date": "2019-08-02"}, {"article_id": 4, "author_id": 7, "viewer_id": 1, "view_date": "2019-07-22"}, {"article_id": 3, "author_id": 4, "viewer_id": 4, "view_date": "2019-07-21"}, {"article_id": 3, "author_id": 4, "viewer_id": 4, "view_date": "2019-07-21"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Translate “viewed their own article” into an equality

Each row identifies the article's author and the person who viewed it. The schema explicitly says equal `author_id` and `viewer_id` values represent the same person. Therefore, a row is evidence of a self-view exactly when

`author_id = viewer_id`.

The `WHERE` clause applies this condition before the result is projected. Rows where somebody viewed another person's article are discarded. The article identifier and date do not affect qualification: the problem asks whether an author viewed at least one of their own articles, not which article it was or when it occurred.

This is a row-level predicate, so `WHERE` is the correct SQL stage. `HAVING` is intended for conditions on groups or aggregate values and would introduce unnecessary grouping here.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Views": [{"article_id": 1, "author_id": 3, "viewer_id": 5, "view_date": "2019-08-01"}, {"article_id": 1, "author_id": 3, "viewer_id": 6, "view_date": "2019-08-02"}, {"article_id": 2, "author_id": 7, "viewer_id": 7, "view_date": "2019-08-01"}, {"article_id": 2, "author_id": 7, "viewer_id": 6, "view_date": "2019-08-02"}, {"article_id": 4, "author_id": 7, "viewer_id": 1, "view_date": "2019-07-22"}, {"article_id": 3, "author_id": 4, "viewer_id": 4, "view_date": "2019-07-21"}, {"article_id": 3, "author_id": 4, "viewer_id": 4, "view_date": "2019-07-21"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Return each qualifying person only once

One author may view the same self-authored article many times, may view several of their own articles, and may have duplicate rows because the table has no primary key. The requested output is a set of authors, not a list of view events. Consequently, the selected expression is

`DISTINCT author_id`.

`DISTINCT` collapses all identical selected author identifiers after the `WHERE` filter. It handles both meaningful multiple self-views and literal duplicate table rows. A qualifying author contributes exactly one output row no matter how many pieces of evidence exist.

The query aliases `author_id` as `id` because the required result column is named `id`. The alias changes only the output label; the underlying value remains the qualifying person's identifier.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Sort by the requested output identifier

`ORDER BY 1` sorts by the first selected expression, which is the aliased author identifier. The default SQL sort direction is ascending, so this produces increasing `id` values as required.

Using the positional form avoids any ambiguity about whether the engine permits the output alias in the order clause, though `ORDER BY id` would be an equivalent and often more explicit formulation in MySQL.

The order step occurs after duplicate elimination in the conceptual result. It therefore sorts only the distinct qualifying authors, not every source view row.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["id"], "rows": [[4], [7]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Views": [{"article_id": 1, "author_id": 3, "viewer_id": 5, "view_date": "2019-08-01"}, {"article_id": 1, "author_id": 3, "viewer_id": 6, "view_date": "2019-08-02"}, {"article_id": 2, "author_id": 7, "viewer_id": 7, "view_date": "2019-08-01"}, {"article_id": 2, "author_id": 7, "viewer_id": 6, "view_date": "2019-08-02"}, {"article_id": 4, "author_id": 7, "viewer_id": 1, "view_date": "2019-07-22"}, {"article_id": 3, "author_id": 4, "viewer_id": 4, "view_date": "2019-07-21"}, {"article_id": 3, "author_id": 4, "viewer_id": 4, "view_date": "2019-07-21"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["id"], "rows": [[4], [7]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Use `GROUP BY author_id`:** Filtering self-view rows and grouping by author can also return one row per person. `DISTINCT` is more direct because no aggregate value is needed.
- **Use a self-join:** All necessary fields are already in one row. A join would create needless row combinations and make duplicate handling harder.
- **Select every matching row without `DISTINCT`:** Authors with repeated self-views or duplicate source rows would appear several times, violating the one-row-per-author result.
- **Compare `article_id` with `viewer_id`:** Those columns represent different kinds of identifiers. Self-view status is defined by equality between author and viewer.
- **Filter by date:** The problem imposes no date range. Every row is eligible evidence regardless of `view_date`.
- **Duplicate rows:** They do not change the answer because `DISTINCT` collapses their repeated author identifier.
- **Several own articles:** An author who self-views multiple articles still appears once.
- **Author also views other people's articles:** Non-self rows are ignored, while any self-view row is sufficient for qualification.
- **No self-views:** The filter leaves no rows, and the query returns an empty one-column result.
- **Ordering:** Ascending order is mandatory here, unlike SQL tasks that permit any order. `ORDER BY 1` supplies it explicitly.
- **Null considerations:** The stated schema does not introduce a special null rule. If null identifiers existed, SQL equality with null would not evaluate true, so such a row would not prove a known self-view.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(r+a\log a)$. Let `r` be the number of rows in `Views` and `a` be the number of distinct authors that pass the equality filter.
- **Auxiliary Space Complexity:** $O(a)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
