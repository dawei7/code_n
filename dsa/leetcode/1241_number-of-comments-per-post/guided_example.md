# Guided Example: Number of Comments per Post

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Submissions": [{"sub_id": 1, "parent_id": null}, {"sub_id": 2, "parent_id": null}, {"sub_id": 1, "parent_id": null}, {"sub_id": 12, "parent_id": null}, {"sub_id": 3, "parent_id": 1}, {"sub_id": 5, "parent_id": 2}, {"sub_id": 3, "parent_id": 1}, {"sub_id": 4, "parent_id": 1}, {"sub_id": 9, "parent_id": 1}, {"sub_id": 10, "parent_id": 2}, {"sub_id": 6, "parent_id": 7}]}}`
- **Required output:** `{"columns": ["post_id", "number_of_comments"], "rows": [[1, 3], [2, 2], [12, 0]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Submissions`

The objective is to compute `{"columns": ["post_id", "number_of_comments"], "rows": [[1, 3], [2, 2], [12, 0]]}` from `{"tables": {"Submissions": [{"sub_id": 1, "parent_id": null}, {"sub_id": 2, "parent_id": null}, {"sub_id": 1, "parent_id": null}, {"sub_id": 12, "parent_id": null}, {"sub_id": 3, "parent_id": 1}, {"sub_id": 5, "parent_id": 2}, {"sub_id": 3, "parent_id": 1}, {"sub_id": 4, "parent_id": 1}, {"sub_id": 9, "parent_id": 1}, {"sub_id": 10, "parent_id": 2}, {"sub_id": 6, "parent_id": 7}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use the table once as posts and once as comments

Posts and comments share the same `Submissions` table. A row is a post when `parent_id IS NULL`; a comment row names its parent post in `parent_id`.

The query self-joins the table:

- `s1` represents candidate post rows;
- `s2` represents comment rows whose `parent_id` equals `s1.sub_id`.

The join condition `s1.sub_id = s2.parent_id` attaches each comment to its post.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Submissions": [{"sub_id": 1, "parent_id": null}, {"sub_id": 2, "parent_id": null}, {"sub_id": 1, "parent_id": null}, {"sub_id": 12, "parent_id": null}, {"sub_id": 3, "parent_id": 1}, {"sub_id": 5, "parent_id": 2}, {"sub_id": 3, "parent_id": 1}, {"sub_id": 4, "parent_id": 1}, {"sub_id": 9, "parent_id": 1}, {"sub_id": 10, "parent_id": 2}, {"sub_id": 6, "parent_id": 7}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the join is a left join

An inner join would omit posts that have no comments. The output must include them with count zero, so `LEFT JOIN` preserves each `s1` post even when no matching `s2` row exists. In that case, the comment-side columns are `NULL`.

The filter `WHERE s1.parent_id IS NULL` ensures only genuine post rows drive the result. A comment whose parent post is absent cannot find a qualifying `s1` row and is ignored.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Remove duplicate posts and duplicate comments together

The table may duplicate both kinds of rows. If a post row appears twice and one of its comments appears twice, the raw self-join can create four copies of the same post-comment relationship.

The common table expression selects:

`DISTINCT s1.sub_id AS post_id, s2.sub_id AS sub_id`.

`DISTINCT` collapses every repeated relationship to one pair. It also collapses duplicate no-comment post rows to a single pair `(post_id, NULL)`.

This is why the outer query can use ordinary `COUNT(sub_id)` instead of `COUNT(DISTINCT sub_id)`. Uniqueness has already been established per post-comment pair.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["post_id", "number_of_comments"], "rows": [[1, 3], [2, 2], [12, 0]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Submissions": [{"sub_id": 1, "parent_id": null}, {"sub_id": 2, "parent_id": null}, {"sub_id": 1, "parent_id": null}, {"sub_id": 12, "parent_id": null}, {"sub_id": 3, "parent_id": 1}, {"sub_id": 5, "parent_id": 2}, {"sub_id": 3, "parent_id": 1}, {"sub_id": 4, "parent_id": 1}, {"sub_id": 9, "parent_id": 1}, {"sub_id": 10, "parent_id": 2}, {"sub_id": 6, "parent_id": 7}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["post_id", "number_of_comments"], "rows": [[1, 3], [2, 2], [12, 0]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **`COUNT(DISTINCT s2.sub_id)` directly:** Group post-side IDs after a left join and count distinct comment IDs. This can express the same result in one query level.
- **Pre-deduplicate posts and comments separately:** Build one CTE for unique posts and another for unique comment pairs, then left join them. It is more verbose but makes duplicate handling explicit.
- **Use of `COUNT(*)`:** Incorrect for posts without comments because the left join supplies one null-extended row.
- **Duplicate post rows:** `DISTINCT` collapses the repeated post-comment pairs.
- **Duplicate comment rows:** The same comment ID for the same post is counted once.
- **Post with no comments:** The null placeholder survives and counts as zero.
- **Comment with deleted parent:** No qualifying post-side row exists, so it is ignored.
- **Same comment ID under different posts:** Pair-level distinctness treats those as separate relationships, one per post.
- **Null semantics:** `parent_id IS NULL` must be used; equality to `NULL` is not valid SQL filtering.
- **Ordering:** The final sort is by numeric `post_id` ascending, independent of join or grouping order.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(r)$. Let \(r\) be the number of input rows. With hash-based join, duplicate elimination, and grouping, the logical work can be expected \(O(r)\) plus output ordering, matching the manifest under favorable indexing and execution planning.
- **Auxiliary Space Complexity:** $O(r)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
