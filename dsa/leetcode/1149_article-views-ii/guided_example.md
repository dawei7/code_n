# Guided Example: Article Views II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Views": [{"article_id": 1, "author_id": 3, "viewer_id": 5, "view_date": "2019-08-01"}, {"article_id": 3, "author_id": 4, "viewer_id": 5, "view_date": "2019-08-01"}, {"article_id": 1, "author_id": 3, "viewer_id": 6, "view_date": "2019-08-02"}, {"article_id": 2, "author_id": 7, "viewer_id": 7, "view_date": "2019-08-01"}, {"article_id": 2, "author_id": 7, "viewer_id": 6, "view_date": "2019-08-02"}, {"article_id": 4, "author_id": 7, "viewer_id": 1, "view_date": "2019-07-22"}, {"article_id": 3, "author_id": 4, "viewer_id": 4, "view_date": "2019-07-21"}, {"article_id": 3, "author_id": 4, "viewer_id": 4, "view_date": "2019-07-21"}]}}`
- **Required output:** `{"columns": ["id"], "rows": [[5], [6]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Views`

The objective is to compute `{"columns": ["id"], "rows": [[5], [6]]}` from `{"tables": {"Views": [{"article_id": 1, "author_id": 3, "viewer_id": 5, "view_date": "2019-08-01"}, {"article_id": 3, "author_id": 4, "viewer_id": 5, "view_date": "2019-08-01"}, {"article_id": 1, "author_id": 3, "viewer_id": 6, "view_date": "2019-08-02"}, {"article_id": 2, "author_id": 7, "viewer_id": 7, "view_date": "2019-08-01"}, {"article_id": 2, "author_id": 7, "viewer_id": 6, "view_date": "2019-08-02"}, {"article_id": 4, "author_id": 7, "viewer_id": 1, "view_date": "2019-07-22"}, {"article_id": 3, "author_id": 4, "viewer_id": 4, "view_date": "2019-07-21"}, {"article_id": 3, "author_id": 4, "viewer_id": 4, "view_date": "2019-07-21"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The qualifying unit is a viewer-date pair

The condition says a person must view more than one article on the same date. Neither a viewer's total across all dates nor an article's total viewers answers that question. The query must examine each combination of `viewer_id` and `view_date` independently.

`GROUP BY viewer_id, view_date` forms exactly those groups. All events for one viewer on one calendar date enter the same group, while a different viewer or a different date enters another group.

The `author_id` column does not participate. Qualification depends only on who viewed, which article was viewed, and when. Whether the viewer authored any of those articles is irrelevant to this problem.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Views": [{"article_id": 1, "author_id": 3, "viewer_id": 5, "view_date": "2019-08-01"}, {"article_id": 3, "author_id": 4, "viewer_id": 5, "view_date": "2019-08-01"}, {"article_id": 1, "author_id": 3, "viewer_id": 6, "view_date": "2019-08-02"}, {"article_id": 2, "author_id": 7, "viewer_id": 7, "view_date": "2019-08-01"}, {"article_id": 2, "author_id": 7, "viewer_id": 6, "view_date": "2019-08-02"}, {"article_id": 4, "author_id": 7, "viewer_id": 1, "view_date": "2019-07-22"}, {"article_id": 3, "author_id": 4, "viewer_id": 4, "view_date": "2019-07-21"}, {"article_id": 3, "author_id": 4, "viewer_id": 4, "view_date": "2019-07-21"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Count distinct articles rather than rows

The table may contain duplicate rows, and one person may generate multiple records involving the same article on the same date. “More than one article” means at least two different `article_id` values, not at least two view-event rows.

Within each viewer-date group, `COUNT(DISTINCT article_id)` measures the number of unique articles. A duplicated view of article three still contributes one. Views of articles one and three contribute two even if either event is repeated.

`HAVING COUNT(DISTINCT article_id) > 1` retains only groups whose unique-article count is at least two. `HAVING` is necessary because this condition depends on an aggregate computed after grouping. A `WHERE` clause cannot directly filter on that group count.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The table may contain duplicate rows, and one person may gen... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Deduplicate viewers who qualify on multiple dates

After `HAVING`, one row conceptually remains for each qualifying viewer-date group. A person who views several articles on two different dates creates two qualifying groups, but the output should contain that person's identifier only once.

`SELECT DISTINCT viewer_id AS id` performs this second kind of deduplication. The inner distinctness in `COUNT(DISTINCT article_id)` answers “how many different articles in one group?” The outer `SELECT DISTINCT` answers “how many different qualifying people in the final result?” They solve separate duplicate problems and are both needed.

The alias `id` gives the single output column its required name. `ORDER BY 1` sorts that first selected expression in ascending order, satisfying the presentation requirement.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["id"], "rows": [[5], [6]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Views": [{"article_id": 1, "author_id": 3, "viewer_id": 5, "view_date": "2019-08-01"}, {"article_id": 3, "author_id": 4, "viewer_id": 5, "view_date": "2019-08-01"}, {"article_id": 1, "author_id": 3, "viewer_id": 6, "view_date": "2019-08-02"}, {"article_id": 2, "author_id": 7, "viewer_id": 7, "view_date": "2019-08-01"}, {"article_id": 2, "author_id": 7, "viewer_id": 6, "view_date": "2019-08-02"}, {"article_id": 4, "author_id": 7, "viewer_id": 1, "view_date": "2019-07-22"}, {"article_id": 3, "author_id": 4, "viewer_id": 4, "view_date": "2019-07-21"}, {"article_id": 3, "author_id": 4, "viewer_id": 4, "view_date": "2019-07-21"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["id"], "rows": [[5], [6]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Use `COUNT(*) > 1`:** Duplicate views of the s:** - **Use `COUNT(*) > 1`:** Duplicate views of the same article would create a false qualification. The count must be over distinct `article_id` values.
- **Group only by viewer:** That combines articles viewed on different dates and can qualify someone who never viewed two articles on one day.
- **Group only by date:** That mixes different people and answers how many articles everyone viewed collectively.
- **Self-join `Views`:** Joining rows on equal viewer and date with different article IDs can prove that a qualifying pair exists. It is valid but can create many row pairs and demands careful deduplication.
- **Use `WHERE` for the aggregate threshold:** `WHERE` is evaluated before grouping and cannot test the distinct count. `HAVING` filters completed groups.
- **Omit outer `DISTINCT`:** A viewer qualifying on multiple dates could appear once per date even though only one identifier is requested.
- **Duplicate rows:** They are neutralized by `COUNT(DISTINCT article_id)` and cannot manufacture a second article.
- **Repeated views of two articles:** The group qualifies because its distinct set has size two, regardless of the number of repeated events.
- **Self-views:** They count exactly like any other article view; author identity does not affect this task.
- **No qualifying viewer-date group:** The result is an empty table with the column named `id`.
- **Required ordering:** `ORDER BY 1` sorts the final distinct viewer identifiers, not the underlying events.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(r\log r)$. Let `r` be the number of rows in `Views`. Grouping by viewer and date and deduplicating article identifiers can require sorting `r` records, giving the manifest's conservative `O(r log r)` time bound. The final distinct projection and ordering do not exceed that worst-case order because there can be at most `r` qualifying group rows.
- **Auxiliary Space Complexity:** $O(r)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
