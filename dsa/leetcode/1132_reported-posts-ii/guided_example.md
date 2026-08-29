# Guided Example: Reported Posts II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Actions": [{"user_id": 1, "post_id": 1, "action_date": "2019-07-01", "action": "view", "extra": null}, {"user_id": 1, "post_id": 1, "action_date": "2019-07-01", "action": "like", "extra": null}, {"user_id": 1, "post_id": 1, "action_date": "2019-07-01", "action": "share", "extra": null}, {"user_id": 2, "post_id": 2, "action_date": "2019-07-04", "action": "view", "extra": null}, {"user_id": 2, "post_id": 2, "action_date": "2019-07-04", "action": "report", "extra": "spam"}, {"user_id": 3, "post_id": 4, "action_date": "2019-07-04", "action": "view", "extra": null}, {"user_id": 3, "post_id": 4, "action_date": "2019-07-04", "action": "report", "extra": "spam"}, {"user_id": 4, "post_id": 3, "action_date": "2019-07-02", "action": "view", "extra": null}, {"user_id": 4, "post_id": 3, "action_date": "2019-07-02", "action": "report", "extra": "spam"}, {"user_id": 5, "post_id": 2, "action_date": "2019-07-03", "action": "view", "extra": null}, {"user_id": 5, "post_id": 2, "action_date": "2019-07-03", "action": "report", "extra": "racism"}, {"user_id": 5, "post_id": 5, "action_date": "2019-07-03", "action": "view", "extra": null}, {"user_id": 5, "post_id": 5, "action_date": "2019-07-03", "action": "report", "extra": "racism"}], "Removals": [{"post_id": 2, "remove_date": "2019-07-20"}, {"post_id": 3, "remove_date": "2019-07-18"}]}}`
- **Required output:** `{"columns": ["average_daily_percent"], "rows": [[75]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Actions`

The objective is to compute `{"columns": ["average_daily_percent"], "rows": [[75]]}` from `{"tables": {"Actions": [{"user_id": 1, "post_id": 1, "action_date": "2019-07-01", "action": "view", "extra": null}, {"user_id": 1, "post_id": 1, "action_date": "2019-07-01", "action": "like", "extra": null}, {"user_id": 1, "post_id": 1, "action_date": "2019-07-01", "action": "share", "extra": null}, {"user_id": 2, "post_id": 2, "action_date": "2019-07-04", "action": "view", "extra": null}, {"user_id": 2, "post_id": 2, "action_date": "2019-07-04", "action": "report", "extra": "spam"}, {"user_id": 3, "post_id": 4, "action_date": "2019-07-04", "action": "view", "extra": null}, {"user_id": 3, "post_id": 4, "action_date": "2019-07-04", "action": "report", "extra": "spam"}, {"user_id": 4, "post_id": 3, "action_date": "2019-07-02", "action": "view", "extra": null}, {"user_id": 4, "post_id": 3, "action_date": "2019-07-02", "action": "report", "extra": "spam"}, {"user_id": 5, "post_id": 2, "action_date": "2019-07-03", "action": "view", "extra": null}, {"user_id": 5, "post_id": 2, "action_date": "2019-07-03", "action": "report", "extra": "racism"}, {"user_id": 5, "post_id": 5, "action_date": "2019-07-03", "action": "view", "extra": null}, {"user_id": 5, "post_id": 5, "action_date": "2019-07-03", "action": "report", "extra": "racism"}], "Removals": [{"post_id": 2, "remove_date": "2019-07-20"}, {"post_id": 3, "remove_date": "2019-07-18"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Compute one percentage per reporting date

The requested average is not one global ratio. Each date with spam-reported posts first receives its own percentage, and those daily percentages are then averaged with equal weight.

CTE `T` creates exactly that intermediate grain: one row per qualifying `action_date` containing column `percent`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Actions": [{"user_id": 1, "post_id": 1, "action_date": "2019-07-01", "action": "view", "extra": null}, {"user_id": 1, "post_id": 1, "action_date": "2019-07-01", "action": "like", "extra": null}, {"user_id": 1, "post_id": 1, "action_date": "2019-07-01", "action": "share", "extra": null}, {"user_id": 2, "post_id": 2, "action_date": "2019-07-04", "action": "view", "extra": null}, {"user_id": 2, "post_id": 2, "action_date": "2019-07-04", "action": "report", "extra": "spam"}, {"user_id": 3, "post_id": 4, "action_date": "2019-07-04", "action": "view", "extra": null}, {"user_id": 3, "post_id": 4, "action_date": "2019-07-04", "action": "report", "extra": "spam"}, {"user_id": 4, "post_id": 3, "action_date": "2019-07-02", "action": "view", "extra": null}, {"user_id": 4, "post_id": 3, "action_date": "2019-07-02", "action": "report", "extra": "spam"}, {"user_id": 5, "post_id": 2, "action_date": "2019-07-03", "action": "view", "extra": null}, {"user_id": 5, "post_id": 2, "action_date": "2019-07-03", "action": "report", "extra": "racism"}, {"user_id": 5, "post_id": 5, "action_date": "2019-07-03", "action": "view", "extra": null}, {"user_id": 5, "post_id": 5, "action_date": "2019-07-03", "action": "report", "extra": "racism"}], "Removals": [{"post_id": 2, "remove_date": "2019-07-20"}, {"post_id": 3, "remove_date": "2019-07-18"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Preserve every spam-reported post with a left join

`Actions AS t1 LEFT JOIN Removals AS t2 ON t1.post_id = t2.post_id` keeps an action row even when its post was never removed. For a removed post, `t2.post_id` is non-null; for an unremoved post, it is null.

The removal date is not part of the join because the contract cares only whether the post appears in Removals, not when removal happened relative to reporting.

Removals has primary key `post_id`, so a post matches at most one removal row and is not multiplied by the join.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Use distinct posts in both numerator and denominator

Actions may contain duplicate rows and several users may report the same post. The daily denominator must be the number of distinct spam-reported posts, so it uses `COUNT(DISTINCT t1.post_id)`.

The numerator uses `COUNT(DISTINCT t2.post_id)`. SQL count ignores null, so only matched removed posts contribute, and distinct prevents multiple action rows from counting one removed post repeatedly.

Their quotient is the fraction removed. Multiplication by 100 converts it to a percentage.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["average_daily_percent"], "rows": [[75]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Actions": [{"user_id": 1, "post_id": 1, "action_date": "2019-07-01", "action": "view", "extra": null}, {"user_id": 1, "post_id": 1, "action_date": "2019-07-01", "action": "like", "extra": null}, {"user_id": 1, "post_id": 1, "action_date": "2019-07-01", "action": "share", "extra": null}, {"user_id": 2, "post_id": 2, "action_date": "2019-07-04", "action": "view", "extra": null}, {"user_id": 2, "post_id": 2, "action_date": "2019-07-04", "action": "report", "extra": "spam"}, {"user_id": 3, "post_id": 4, "action_date": "2019-07-04", "action": "view", "extra": null}, {"user_id": 3, "post_id": 4, "action_date": "2019-07-04", "action": "report", "extra": "spam"}, {"user_id": 4, "post_id": 3, "action_date": "2019-07-02", "action": "view", "extra": null}, {"user_id": 4, "post_id": 3, "action_date": "2019-07-02", "action": "report", "extra": "spam"}, {"user_id": 5, "post_id": 2, "action_date": "2019-07-03", "action": "view", "extra": null}, {"user_id": 5, "post_id": 2, "action_date": "2019-07-03", "action": "report", "extra": "racism"}, {"user_id": 5, "post_id": 5, "action_date": "2019-07-03", "action": "view", "extra": null}, {"user_id": 5, "post_id": 5, "action_date": "2019-07-03", "action": "report", "extra": "racism"}], "Removals": [{"post_id": 2, "remove_date": "2019-07-20"}, {"post_id": 3, "remove_date": "2019-07-18"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["average_daily_percent"], "rows": [[75]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Pre-deduplicate date-post pairs:** Select distinct spam report pairs first, left join removals, then average daily conditional counts.
- **Conditional numerator:** Count distinct `CASE WHEN removal matched THEN post_id END`; it makes the removed test explicit.
- **Global ratio:** Incorrect because it weights dates by their post counts.
- **Inner join:** Incorrect because it removes unremoved posts from the denominator.
- **Duplicate reports:** Distinct post counts prevent inflation.
- **Several reporters for one post:** The post contributes once on that date.
- **Same post on two dates:** It contributes independently to both daily percentages.
- **Removal date:** Its value is intentionally ignored.
- **Zero removed on a date:** Numerator zero produces a zero-percent daily value.
- **All removed on a date:** Numerator equals denominator and produces one hundred percent.
- **Non-report row with extra spam:** The exact query includes it; adding the action predicate is required by the written contract.
- **Final rounding:** Only the average is rounded to two decimals.
- **No qualifying rows:** The aggregate row contains null unless an explicit fallback is added.
- **Equal weighting across dates:** `AVG(percent)` gives every reporting date one vote regardless of how many distinct spam posts it contains, which is the required daily-average interpretation.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R \log R)$. Let $R$ be Actions rows plus relevant Removals rows. A general sort-based join, daily grouping, and distinct aggregation can take $O(R\log R)$ time.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
