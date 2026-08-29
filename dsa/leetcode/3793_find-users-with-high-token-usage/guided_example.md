# Guided Example: Find Users with High Token Usage

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"prompts": [{"user_id": 1, "prompt": "Write a blog outline", "tokens": 120}, {"user_id": 1, "prompt": "Generate SQL query", "tokens": 80}, {"user_id": 1, "prompt": "Summarize an article", "tokens": 200}, {"user_id": 2, "prompt": "Create resume bullet", "tokens": 60}, {"user_id": 2, "prompt": "Improve LinkedIn bio", "tokens": 70}, {"user_id": 3, "prompt": "Explain neural networks", "tokens": 300}, {"user_id": 3, "prompt": "Generate interview Q&A", "tokens": 250}, {"user_id": 3, "prompt": "Write cover letter", "tokens": 180}, {"user_id": 3, "prompt": "Optimize Python code", "tokens": 220}]}}`
- **Required output:** `{"columns": ["user_id", "prompt_count", "avg_tokens"], "rows": [[3, 4, 237.5], [1, 3, 133.33]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `prompts`

The objective is to compute `{"columns": ["user_id", "prompt_count", "avg_tokens"], "rows": [[3, 4, 237.5], [1, 3, 133.33]]}` from `{"tables": {"prompts": [{"user_id": 1, "prompt": "Write a blog outline", "tokens": 120}, {"user_id": 1, "prompt": "Generate SQL query", "tokens": 80}, {"user_id": 1, "prompt": "Summarize an article", "tokens": 200}, {"user_id": 2, "prompt": "Create resume bullet", "tokens": 60}, {"user_id": 2, "prompt": "Improve LinkedIn bio", "tokens": 70}, {"user_id": 3, "prompt": "Explain neural networks", "tokens": 300}, {"user_id": 3, "prompt": "Generate interview Q&A", "tokens": 250}, {"user_id": 3, "prompt": "Write cover letter", "tokens": 180}, {"user_id": 3, "prompt": "Optimize Python code", "tokens": 220}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Aggregate one row per user

`GROUP BY user_id` collects every prompt row belonging to the same user. The selected aggregate columns then produce:

- `COUNT(1) AS prompt_count`: number of prompt rows;
- `ROUND(AVG(tokens),2) AS avg_tokens`: displayed average rounded to two decimal places.

The primary key guarantees prompt strings are unique per user, but counting rows is enough; no `DISTINCT` is required.

All three selected expressions are evaluated once per completed group. `user_id` is the grouping key, while the count and average summarize all token rows in that group. The query never mixes prompts from different users.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"prompts": [{"user_id": 1, "prompt": "Write a blog outline", "tokens": 120}, {"user_id": 1, "prompt": "Generate SQL query", "tokens": 80}, {"user_id": 1, "prompt": "Summarize an article", "tokens": 200}, {"user_id": 2, "prompt": "Create resume bullet", "tokens": 60}, {"user_id": 2, "prompt": "Improve LinkedIn bio", "tokens": 70}, {"user_id": 3, "prompt": "Explain neural networks", "tokens": 300}, {"user_id": 3, "prompt": "Generate interview Q&A", "tokens": 250}, {"user_id": 3, "prompt": "Write cover letter", "tokens": 180}, {"user_id": 3, "prompt": "Optimize Python code", "tokens": 220}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Filter completed groups with `HAVING`

Group-level conditions cannot be applied before aggregation. The query uses

`HAVING prompt_count >= 3 AND MAX(tokens) > avg_tokens`.

The first condition keeps users with at least three prompts. `MAX(tokens)` represents the user's largest individual prompt usage, so comparing it with the average tests whether at least one prompt is above the comparison threshold.

If the maximum is not above that threshold, no row can be above it. If it is above, the row attaining the maximum is the required witness. This avoids a self-join or correlated subquery.

For sample user one, the group contains 120, 80, and 200. Its count is three, displayed average is 133.33, and maximum 200 passes the second condition. User two's count is only two, so the conjunction rejects that group.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Apply the requested output order

`ORDER BY avg_tokens DESC, user_id` places higher displayed averages first. MySQL's default order is ascending for `user_id`, providing the required tie-break.

For the sample, user three has average 237.5 and user one has 133.33, so user three appears first. User two fails the count condition before its maximum matters.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["user_id", "prompt_count", "avg_tokens"], "rows": [[3, 4, 237.5], [1, 3, 133.33]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"prompts": [{"user_id": 1, "prompt": "Write a blog outline", "tokens": 120}, {"user_id": 1, "prompt": "Generate SQL query", "tokens": 80}, {"user_id": 1, "prompt": "Summarize an article", "tokens": 200}, {"user_id": 2, "prompt": "Create resume bullet", "tokens": 60}, {"user_id": 2, "prompt": "Improve LinkedIn bio", "tokens": 70}, {"user_id": 3, "prompt": "Explain neural networks", "tokens": 300}, {"user_id": 3, "prompt": "Generate interview Q&A", "tokens": 250}, {"user_id": 3, "prompt": "Write cover letter", "tokens": 180}, {"user_id": 3, "prompt": "Optimize Python code", "tokens": 220}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["user_id", "prompt_count", "avg_tokens"], "rows": [[3, 4, 237.5], [1, 3, 133.33]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Correct unrounded comparison:** Use `MAX(tokens)>AVG(tokens)` in `HAVING` and keep rounding only in `SELECT`.
- **Correlated existence subquery:** It can test an above-average prompt explicitly but repeats work that maximum and average summarize.
- **Use `WHERE` for aggregate conditions:** Aggregates are unavailable before grouping; `HAVING` is required.
- **Exactly three prompts:** The inclusive count condition accepts the group.
- **All token counts equal:** Maximum equals average, so strict comparison fails.
- **One value slightly below many maxima:** Rounding may make the source incorrectly exclude the group.
- **Strict versus inclusive comparison:** A prompt equal to the comparison average is not enough.
- **Rounded display:** `ROUND` affects the returned value and, in this source, mistakenly affects qualification.
- **Ordering tie:** Equal rounded averages use ascending user ID.
- **No qualifying users:** The result table is empty.
- **Dialect portability:** Alias references in `HAVING` are MySQL-specific behavior used by the exact source.
- **Maximum equivalence:** Checking maximum is sufficient for existence because it is at least every individual token value.
- **Source defect:** The query does not fully satisfy the contract's unrounded-comparison requirement.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R\log R)$. Let $R$ be the number of prompt rows and $U$ the number of user groups. Physical cost depends on indexes and the MySQL plan. Hash aggregation can process groups in expected $O(R)$ time; sort-based grouping may cost $O(R\log R)$. Sorting the qualifying user rows costs $O(U\log U)$.
- **Auxiliary Space Complexity:** $O(R + U)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
