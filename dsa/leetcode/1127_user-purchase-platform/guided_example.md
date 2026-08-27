# Guided Example: User Purchase Platform

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Spending": [{"user_id": 1, "spend_date": "2019-07-01", "platform": "mobile", "amount": 100}, {"user_id": 1, "spend_date": "2019-07-01", "platform": "desktop", "amount": 100}, {"user_id": 2, "spend_date": "2019-07-01", "platform": "mobile", "amount": 100}, {"user_id": 2, "spend_date": "2019-07-02", "platform": "mobile", "amount": 100}, {"user_id": 3, "spend_date": "2019-07-01", "platform": "desktop", "amount": 100}, {"user_id": 3, "spend_date": "2019-07-02", "platform": "desktop", "amount": 100}]}}`
- **Required output:** `{"columns": ["spend_date", "platform", "total_amount", "total_users"], "rows": [["2019-07-01", "desktop", 100, 1], ["2019-07-01", "mobile", 100, 1], ["2019-07-01", "both", 200, 1], ["2019-07-02", "desktop", 100, 1], ["2019-07-02", "mobile", 100, 1], ["2019-07-02", "both", 0, 0]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Spending`

The objective is to compute `{"columns": ["spend_date", "platform", "total_amount", "total_users"], "rows": [["2019-07-01", "desktop", 100, 1], ["2019-07-01", "mobile", 100, 1], ["2019-07-01", "both", 200, 1], ["2019-07-02", "desktop", 100, 1], ["2019-07-02", "mobile", 100, 1], ["2019-07-02", "both", 0, 0]]}` from `{"tables": {"Spending": [{"user_id": 1, "spend_date": "2019-07-01", "platform": "mobile", "amount": 100}, {"user_id": 1, "spend_date": "2019-07-01", "platform": "desktop", "amount": 100}, {"user_id": 2, "spend_date": "2019-07-01", "platform": "mobile", "amount": 100}, {"user_id": 2, "spend_date": "2019-07-02", "platform": "mobile", "amount": 100}, {"user_id": 3, "spend_date": "2019-07-01", "platform": "desktop", "amount": 100}, {"user_id": 3, "spend_date": "2019-07-02", "platform": "desktop", "amount": 100}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The output needs rows even for empty categories

For every represented date, the result must contain desktop, mobile, and both, including categories with zero users. Aggregating Spending directly cannot create a group that has no source row.

CTE `P` builds the complete date-category skeleton. Each distinct spending date is paired once with each of the three literal platform labels through three `UNION` branches.

Using `UNION` deduplicates rows across branch outputs, although the labels differ and each branch already selects distinct dates.

This skeleton establishes the output grain before measures are calculated: exactly one row per represented date and requested category. Later joins may attach zero, one, or many classified users, but the final grouping returns to this predetermined grain.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Spending": [{"user_id": 1, "spend_date": "2019-07-01", "platform": "mobile", "amount": 100}, {"user_id": 1, "spend_date": "2019-07-01", "platform": "desktop", "amount": 100}, {"user_id": 2, "spend_date": "2019-07-01", "platform": "mobile", "amount": 100}, {"user_id": 2, "spend_date": "2019-07-02", "platform": "mobile", "amount": 100}, {"user_id": 3, "spend_date": "2019-07-01", "platform": "desktop", "amount": 100}, {"user_id": 3, "spend_date": "2019-07-02", "platform": "desktop", "amount": 100}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Classify each user separately on each date

CTE `T` groups by `user_id` and `spend_date`. The primary key allows at most one desktop and one mobile row for that user-date.

`SUM(amount)` combines all money the user spent that date. If only one platform row exists, `COUNT(platform) = 1` and the classification remains that row’s platform. If both rows exist, count is two and classification becomes literal `'both'`.

Thus a two-platform user contributes one combined record to both rather than one record to each single-platform category.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | CTE `T` groups by `user_id` and `spend_date`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Join classified users onto the skeleton

`P LEFT JOIN T USING (spend_date, platform)` preserves every date-category row. Matching classified user records attach their amounts and IDs. A category with no users remains as one null-extended row.

Grouping by date and platform then computes category totals.

`SUM(amount)` adds every classified user’s daily amount. For an empty category it sees only null, so `COALESCE(..., 0)` returns numeric zero.

`COUNT(t.user_id)` counts non-null user IDs. It returns zero for a null-extended skeleton row. Since `T` has exactly one row per user-date, ordinary count is the number of users without needing `DISTINCT`.

Counting a column from `T` rather than `COUNT(*)` is essential. A left join always retains one skeleton row even without a match, so `COUNT(*)` would incorrectly report one user for an empty category.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["spend_date", "platform", "total_amount", "total_users"], "rows": [["2019-07-01", "desktop", 100, 1], ["2019-07-01", "mobile", 100, 1], ["2019-07-01", "both", 200, 1], ["2019-07-02", "desktop", 100, 1], ["2019-07-02", "mobile", 100, 1], ["2019-07-02", "both", 0, 0]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Spending": [{"user_id": 1, "spend_date": "2019-07-01", "platform": "mobile", "amount": 100}, {"user_id": 1, "spend_date": "2019-07-01", "platform": "desktop", "amount": 100}, {"user_id": 2, "spend_date": "2019-07-01", "platform": "mobile", "amount": 100}, {"user_id": 2, "spend_date": "2019-07-02", "platform": "mobile", "amount": 100}, {"user_id": 3, "spend_date": "2019-07-01", "platform": "desktop", "amount": 100}, {"user_id": 3, "spend_date": "2019-07-02", "platform": "desktop", "amount": 100}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["spend_date", "platform", "total_amount", "total_users"], "rows": [["2019-07-01", "desktop", 100, 1], ["2019-07-01", "mobile", 100, 1], ["2019-07-01", "both", 200, 1], ["2019-07-02", "desktop", 100, 1], ["2019-07-02", "mobile", 100, 1], ["2019-07-02", "both", 0, 0]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Cross join dates with a three-row platform tab:** - **Cross join dates with a three-row platform table:** This explicitly constructs the same skeleton and can be clearer than three UNION branches.
- **Conditional aggregation:** Classify user-date rows first, then aggregate CASE expressions. A skeleton is still needed to emit zero categories.
- **Separate queries per category:** Compute desktop-only, mobile-only, and both, then union them with missing-row handling. It is more repetitive.
- **User spends on both platforms:** Their two amounts combine and the user counts once in both.
- **User spends on one platform:** They remain in that single category.
- **Empty category:** Left join plus `COALESCE` and non-null count produce zero and zero.
- **Same user on different dates:** Classification is independent per date.
- **Primary key:** It limits one row per user-date-platform, making platform count one or two.
- **No Spending rows:** There are no represented dates, so the result is empty.
- **Amount zero:** The user still counts, while total amount may remain zero.
- **ONLY_FULL_GROUP_BY:** The unaggregated platform reference in `T` may require a portable rewrite.
- **Any result order:** No final sorting is required.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R \log R)$. Let $R$ be the number of Spending rows. Distinct-date generation, user-date grouping, joining, and final grouping can require sorting, giving a conservative $O(R\log R)$ time bound.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
