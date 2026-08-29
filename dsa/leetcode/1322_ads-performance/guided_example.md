# Guided Example: Ads Performance

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Ads": {"columns": ["ad_id", "user_id", "action"], "rows": []}}}`
- **Required output:** `{"columns": ["ad_id", "ctr"], "rows": []}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Ads`

The objective is to compute `{"columns": ["ad_id", "ctr"], "rows": []}` from `{"tables": {"Ads": {"columns": ["ad_id", "user_id", "action"], "rows": []}}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: One group per advertisement

`GROUP BY 1` groups by the first selected expression, `ad_id`. Every interaction row for one advertisement is evaluated together, while actions for different advertisements stay separate.

The result contains one row for every distinct advertisement appearing in `Ads`. An ad with only `Ignored` actions still forms a group and therefore remains in the output.

Writing `GROUP BY ad_id` would be more explicit, but ordinal grouping has the same meaning here.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Ads": {"columns": ["ad_id", "user_id", "action"], "rows": []}}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Counting clicks with Boolean arithmetic

In MySQL, the expression `action = 'Clicked'` evaluates to one when true and zero when false. Therefore:

`SUM(action = 'Clicked')`

counts exactly the clicked rows in the current ad group.

The denominator uses:

`SUM(action IN ('Clicked', 'Viewed'))`.

`IN` is true for either a click or a view, so this sum counts both relevant action types. An ignored row contributes zero to both aggregates.

This denominator is equivalent to:

`SUM(action = 'Clicked') + SUM(action = 'Viewed')`,

but the `IN` form expresses the combined relevant-action count directly.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Computing a percentage

The click count is divided by the relevant-action count and multiplied by 100. MySQL performs numeric division here, producing a fractional rate rather than truncating to an integer.

For ad 1 in the reference example, there are two clicked rows, one viewed row, and one ignored row. The ignored action is excluded, so:

$$
\frac{2}{2+1}\times100=66.666\ldots.
$$

`ROUND(..., 2)` produces `66.67`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["ad_id", "ctr"], "rows": []}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Ads": {"columns": ["ad_id", "user_id", "action"], "rows": []}}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["ad_id", "ctr"], "rows": []}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Conditional `CASE` aggregation:** `SUM(CASE WHEN action = 'Clicked' THEN 1 ELSE 0 END)` is portable across more SQL engines.
- **Separate click and view subqueries:** Joining independent counts can work but is longer and must preserve ads missing one action type.
- **Only ignored actions:** The denominator is zero, division yields null, and `COALESCE` returns zero.
- **Clicks but no views:** Numerator equals denominator, so CTR is 100.
- **Views but no clicks:** Numerator is zero with a positive denominator, so CTR is zero without needing `COALESCE`.
- **Ignored rows mixed with relevant actions:** They do not change either count or the rate.
- **Rounding ties:** Ordering uses the selected rounded CTR because `ORDER BY 2` references the projected column.
- **Tie-breaking:** Ascending `ad_id` is mandatory after equal CTR values.
- **Ordinal clauses:** `GROUP BY 1` and `ORDER BY 2 DESC, 1` are concise but fragile if the select list changes.
- **Every ad remains represented:** Grouping starts from all `Ads` rows, so an ignored-only ad is not lost.
- **MySQL Boolean sums:** A different SQL dialect may require explicit `CASE` expressions.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(a)$. Let $r$ be the number of action rows and $a$ the number of distinct advertisements.
- **Auxiliary Space Complexity:** $O(a)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
