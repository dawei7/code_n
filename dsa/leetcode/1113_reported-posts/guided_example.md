# Guided Example: Reported Posts

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Actions": [{"user_id": 1, "post_id": 1, "action_date": "2019-07-01", "action": "view", "extra": null}, {"user_id": 1, "post_id": 1, "action_date": "2019-07-01", "action": "like", "extra": null}, {"user_id": 1, "post_id": 1, "action_date": "2019-07-01", "action": "share", "extra": null}, {"user_id": 2, "post_id": 4, "action_date": "2019-07-04", "action": "view", "extra": null}, {"user_id": 2, "post_id": 4, "action_date": "2019-07-04", "action": "report", "extra": "spam"}, {"user_id": 3, "post_id": 4, "action_date": "2019-07-04", "action": "view", "extra": null}, {"user_id": 3, "post_id": 4, "action_date": "2019-07-04", "action": "report", "extra": "spam"}, {"user_id": 4, "post_id": 3, "action_date": "2019-07-02", "action": "view", "extra": null}, {"user_id": 4, "post_id": 3, "action_date": "2019-07-02", "action": "report", "extra": "spam"}, {"user_id": 5, "post_id": 2, "action_date": "2019-07-04", "action": "view", "extra": null}, {"user_id": 5, "post_id": 2, "action_date": "2019-07-04", "action": "report", "extra": "racism"}, {"user_id": 5, "post_id": 5, "action_date": "2019-07-04", "action": "view", "extra": null}, {"user_id": 5, "post_id": 5, "action_date": "2019-07-04", "action": "report", "extra": "racism"}]}}`
- **Required output:** `{"columns": ["report_reason", "report_count"], "rows": [["spam", 1], ["racism", 2]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Actions`

The objective is to compute `{"columns": ["report_reason", "report_count"], "rows": [["spam", 1], ["racism", 2]]}` from `{"tables": {"Actions": [{"user_id": 1, "post_id": 1, "action_date": "2019-07-01", "action": "view", "extra": null}, {"user_id": 1, "post_id": 1, "action_date": "2019-07-01", "action": "like", "extra": null}, {"user_id": 1, "post_id": 1, "action_date": "2019-07-01", "action": "share", "extra": null}, {"user_id": 2, "post_id": 4, "action_date": "2019-07-04", "action": "view", "extra": null}, {"user_id": 2, "post_id": 4, "action_date": "2019-07-04", "action": "report", "extra": "spam"}, {"user_id": 3, "post_id": 4, "action_date": "2019-07-04", "action": "view", "extra": null}, {"user_id": 3, "post_id": 4, "action_date": "2019-07-04", "action": "report", "extra": "spam"}, {"user_id": 4, "post_id": 3, "action_date": "2019-07-02", "action": "view", "extra": null}, {"user_id": 4, "post_id": 3, "action_date": "2019-07-02", "action": "report", "extra": "spam"}, {"user_id": 5, "post_id": 2, "action_date": "2019-07-04", "action": "view", "extra": null}, {"user_id": 5, "post_id": 2, "action_date": "2019-07-04", "action": "report", "extra": "racism"}, {"user_id": 5, "post_id": 5, "action_date": "2019-07-04", "action": "view", "extra": null}, {"user_id": 5, "post_id": 5, "action_date": "2019-07-04", "action": "report", "extra": "racism"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Filter to the exact event type and date first

The report asks about posts reported yesterday, where the assumed current date makes yesterday July 4, 2019. A row qualifies only when both:

- `action_date = '2019-07-04'`, and
- `action = 'report'`.

The `WHERE` clause applies both predicates before grouping. Views, likes, reactions, comments, and shares on that date are irrelevant. Reports on any other date are also irrelevant.

Filtering first ensures later aggregation sees only evidence that can contribute to the answer.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Actions": [{"user_id": 1, "post_id": 1, "action_date": "2019-07-01", "action": "view", "extra": null}, {"user_id": 1, "post_id": 1, "action_date": "2019-07-01", "action": "like", "extra": null}, {"user_id": 1, "post_id": 1, "action_date": "2019-07-01", "action": "share", "extra": null}, {"user_id": 2, "post_id": 4, "action_date": "2019-07-04", "action": "view", "extra": null}, {"user_id": 2, "post_id": 4, "action_date": "2019-07-04", "action": "report", "extra": "spam"}, {"user_id": 3, "post_id": 4, "action_date": "2019-07-04", "action": "view", "extra": null}, {"user_id": 3, "post_id": 4, "action_date": "2019-07-04", "action": "report", "extra": "spam"}, {"user_id": 4, "post_id": 3, "action_date": "2019-07-02", "action": "view", "extra": null}, {"user_id": 4, "post_id": 3, "action_date": "2019-07-02", "action": "report", "extra": "spam"}, {"user_id": 5, "post_id": 2, "action_date": "2019-07-04", "action": "view", "extra": null}, {"user_id": 5, "post_id": 2, "action_date": "2019-07-04", "action": "report", "extra": "racism"}, {"user_id": 5, "post_id": 5, "action_date": "2019-07-04", "action": "view", "extra": null}, {"user_id": 5, "post_id": 5, "action_date": "2019-07-04", "action": "report", "extra": "racism"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use the report reason as the grouping key

For report actions, `extra` contains the reason. The query selects it as `report_reason` and uses `GROUP BY 1`, meaning group by the first selected expression.

Every qualifying row with the same reason enters the same group. A reason with no qualifying report rows creates no group, which naturally omits zero-count reasons as required.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count posts rather than rows or reporters

The table may contain duplicate rows. Several users may also report the same post for the same reason. The requested quantity is the number of posts, not the number of report actions.

`COUNT(DISTINCT post_id)` counts each post identifier at most once inside one reason group. Two spam reports for post four contribute one spam-reported post. Reports for posts two and five under racism contribute two.

Distinctness is scoped to each group. If the same post is reported for two different reasons, it may correctly contribute once to each reason because the problem asks for a separate count per reason.

This scope can be viewed as deduplicating ordered pairs `(report_reason, post_id)`. Rows with the same pair collapse to one logical contribution, while rows differing in either component remain separate. User ID and the number of physical rows do not participate in that logical identity, which exactly matches the requested statistic.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["report_reason", "report_count"], "rows": [["spam", 1], ["racism", 2]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Actions": [{"user_id": 1, "post_id": 1, "action_date": "2019-07-01", "action": "view", "extra": null}, {"user_id": 1, "post_id": 1, "action_date": "2019-07-01", "action": "like", "extra": null}, {"user_id": 1, "post_id": 1, "action_date": "2019-07-01", "action": "share", "extra": null}, {"user_id": 2, "post_id": 4, "action_date": "2019-07-04", "action": "view", "extra": null}, {"user_id": 2, "post_id": 4, "action_date": "2019-07-04", "action": "report", "extra": "spam"}, {"user_id": 3, "post_id": 4, "action_date": "2019-07-04", "action": "view", "extra": null}, {"user_id": 3, "post_id": 4, "action_date": "2019-07-04", "action": "report", "extra": "spam"}, {"user_id": 4, "post_id": 3, "action_date": "2019-07-02", "action": "view", "extra": null}, {"user_id": 4, "post_id": 3, "action_date": "2019-07-02", "action": "report", "extra": "spam"}, {"user_id": 5, "post_id": 2, "action_date": "2019-07-04", "action": "view", "extra": null}, {"user_id": 5, "post_id": 2, "action_date": "2019-07-04", "action": "report", "extra": "racism"}, {"user_id": 5, "post_id": 5, "action_date": "2019-07-04", "action": "view", "extra": null}, {"user_id": 5, "post_id": 5, "action_date": "2019-07-04", "action": "report", "extra": "racism"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["report_reason", "report_count"], "rows": [["spam", 1], ["racism", 2]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Subquery with `SELECT DISTINCT extra, post_id`:** Deduplicate reason-post pairs first, then count rows per reason. This is equivalent but uses an extra query layer.
- **`COUNT(*)`:** Incorrect when duplicate rows or multiple users report the same post.
- **`COUNT(DISTINCT user_id)`:** Counts reporters, not reported posts.
- **Group by post first:** Possible in a two-stage query, but grouping directly by reason with a distinct post aggregate is simpler.
- **Same post reported by many users:** It contributes once for that reason.
- **Duplicate report rows:** Distinct post counting neutralizes them.
- **Same post with different reasons:** It contributes once within each separate reason group.
- **Non-report action with non-null extra:** It is removed by the action predicate and cannot create a reason group.
- **Report on July 3 or July 5:** It is removed by the exact-date predicate.
- **One qualifying report:** Its reason receives count one.
- **No qualifying reports:** No groups form, yielding an empty result.
- **Null reason on a report:** SQL would group null reasons together if such rows exist; the local contract describes `extra` as optional but does not specify excluding null report reasons, so the exact query preserves that group.
- **Any result order:** No sort is needed because the contract explicitly permits arbitrary order.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R \log R)$. Let $R$ be the number of Actions rows. The database must inspect or index-filter the relevant rows. A general sort-based grouping and distinct aggregation can take $O(R\log R)$ time, matching the manifest.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
