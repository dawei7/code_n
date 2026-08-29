# Guided Example: Friendly Movies Streamed Last Month

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"TVProgram": [{"program_date": "2020-06-10 08:00:00", "content_id": 1, "channel": "LC-Channel"}, {"program_date": "2020-05-11 12:00:00", "content_id": 2, "channel": "LC-Channel"}, {"program_date": "2020-05-12 12:00:00", "content_id": 3, "channel": "LC-Channel"}, {"program_date": "2020-05-13 14:00:00", "content_id": 4, "channel": "Disney Ch"}, {"program_date": "2020-06-18 14:00:00", "content_id": 4, "channel": "Disney Ch"}, {"program_date": "2020-07-15 16:00:00", "content_id": 5, "channel": "Disney Ch"}], "Content": [{"content_id": 1, "title": "Leetcode Movie", "Kids_content": "N", "content_type": "Movies"}, {"content_id": 2, "title": "Alg. for Kids", "Kids_content": "Y", "content_type": "Series"}, {"content_id": 3, "title": "Database Sols", "Kids_content": "N", "content_type": "Series"}, {"content_id": 4, "title": "Aladdin", "Kids_content": "Y", "content_type": "Movies"}, {"content_id": 5, "title": "Cinderella", "Kids_content": "Y", "content_type": "Movies"}]}}`
- **Required output:** `{"columns": ["title"], "rows": [["Aladdin"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `TVProgram`

The objective is to compute `{"columns": ["title"], "rows": [["Aladdin"]]}` from `{"tables": {"TVProgram": [{"program_date": "2020-06-10 08:00:00", "content_id": 1, "channel": "LC-Channel"}, {"program_date": "2020-05-11 12:00:00", "content_id": 2, "channel": "LC-Channel"}, {"program_date": "2020-05-12 12:00:00", "content_id": 3, "channel": "LC-Channel"}, {"program_date": "2020-05-13 14:00:00", "content_id": 4, "channel": "Disney Ch"}, {"program_date": "2020-06-18 14:00:00", "content_id": 4, "channel": "Disney Ch"}, {"program_date": "2020-07-15 16:00:00", "content_id": 5, "channel": "Disney Ch"}], "Content": [{"content_id": 1, "title": "Leetcode Movie", "Kids_content": "N", "content_type": "Movies"}, {"content_id": 2, "title": "Alg. for Kids", "Kids_content": "Y", "content_type": "Series"}, {"content_id": 3, "title": "Database Sols", "Kids_content": "N", "content_type": "Series"}, {"content_id": 4, "title": "Aladdin", "Kids_content": "Y", "content_type": "Movies"}, {"content_id": 5, "title": "Cinderella", "Kids_content": "Y", "content_type": "Movies"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why both tables are required

`TVProgram` tells us which content item was streamed and when, but it does not contain the title, child-friendly flag, or content category. `Content` contains those descriptive fields, but it does not say whether or when an item was streamed. The query must combine rows that refer to the same `content_id`.

The clause `JOIN Content USING (content_id)` is an inner join. `USING` is shorthand for equality between the identically named columns and exposes one joined `content_id` column. Only content records with a matching program record survive. That is correct because a title cannot qualify without at least one stream event.

The reference schemas show `TVProgram.content_id` as an integer and `Content.content_id` as text. MySQL commonly applies implicit conversion when comparing these values. A schema with matching column types would be safer and more portable, but the exact query relies on the database's coercion behavior.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"TVProgram": [{"program_date": "2020-06-10 08:00:00", "content_id": 1, "channel": "LC-Channel"}, {"program_date": "2020-05-11 12:00:00", "content_id": 2, "channel": "LC-Channel"}, {"program_date": "2020-05-12 12:00:00", "content_id": 3, "channel": "LC-Channel"}, {"program_date": "2020-05-13 14:00:00", "content_id": 4, "channel": "Disney Ch"}, {"program_date": "2020-06-18 14:00:00", "content_id": 4, "channel": "Disney Ch"}, {"program_date": "2020-07-15 16:00:00", "content_id": 5, "channel": "Disney Ch"}], "Content": [{"content_id": 1, "title": "Leetcode Movie", "Kids_content": "N", "content_type": "Movies"}, {"content_id": 2, "title": "Alg. for Kids", "Kids_content": "Y", "content_type": "Series"}, {"content_id": 3, "title": "Database Sols", "Kids_content": "N", "content_type": "Series"}, {"content_id": 4, "title": "Aladdin", "Kids_content": "Y", "content_type": "Movies"}, {"content_id": 5, "title": "Cinderella", "Kids_content": "Y", "content_type": "Movies"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Applying all three content conditions

After joining, the `WHERE` clause keeps only rows satisfying all of these rules:

- `DATE_FORMAT(program_date, '%Y%m') = '202006'` means the stream timestamp formats to year 2020 and month 06.
- `kids_content = 'Y'` means the content is intended for children.
- `content_type = 'Movies'` means the content category is a movie rather than a series or another type.

The conditions are connected with `AND`, so satisfying only one or two is not enough. A child-friendly series is rejected by the category condition. A movie not intended for children is rejected by the flag. A friendly movie streamed in May or July is rejected by the formatted date.

The date format string has no separator: `%Y` emits the four-digit year and `%m` emits the two-digit month. A timestamp in June 2020 therefore becomes exactly `202006`. The time of day does not matter because it is absent from the formatted result.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why DISTINCT is needed

The query selects `DISTINCT title` rather than one row for every joined stream record. A movie may have been streamed on several dates or channels during June. Those events produce several joined rows with the same title, but the requested output should report the title once.

`DISTINCT` applies to the selected title value. It can also merge two different content records if they share the same title. That behavior matches a request for distinct titles rather than distinct content identifiers.

The result has no `ORDER BY` clause because output order is unrestricted. SQL result order should never be inferred from join order, primary keys, or the internal strategy used for `DISTINCT`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["title"], "rows": [["Aladdin"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"TVProgram": [{"program_date": "2020-06-10 08:00:00", "content_id": 1, "channel": "LC-Channel"}, {"program_date": "2020-05-11 12:00:00", "content_id": 2, "channel": "LC-Channel"}, {"program_date": "2020-05-12 12:00:00", "content_id": 3, "channel": "LC-Channel"}, {"program_date": "2020-05-13 14:00:00", "content_id": 4, "channel": "Disney Ch"}, {"program_date": "2020-06-18 14:00:00", "content_id": 4, "channel": "Disney Ch"}, {"program_date": "2020-07-15 16:00:00", "content_id": 5, "channel": "Disney Ch"}], "Content": [{"content_id": 1, "title": "Leetcode Movie", "Kids_content": "N", "content_type": "Movies"}, {"content_id": 2, "title": "Alg. for Kids", "Kids_content": "Y", "content_type": "Series"}, {"content_id": 3, "title": "Database Sols", "Kids_content": "N", "content_type": "Series"}, {"content_id": 4, "title": "Aladdin", "Kids_content": "Y", "content_type": "Movies"}, {"content_id": 5, "title": "Cinderella", "Kids_content": "Y", "content_type": "Movies"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["title"], "rows": [["Aladdin"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Half-open date range:** Use a lower bound at `2020-06-01` and an exclusive upper bound at `2020-07-01`. This handles timestamps precisely and can use a normal date index more effectively than `DATE_FORMAT`.
- **YEAR and MONTH functions:** Testing year 2020 and month 6 is readable but remains a function-based filter that may inhibit an ordinary index seek.
- **EXISTS subquery:** Select qualifying content titles and test whether a June program row exists. This can avoid generating multiple joined rows before deduplication, depending on indexes and optimizer choices.
- **Missing content match:** An inner join drops the program row, which is appropriate because its title and classification cannot be established.
- **Multiple June streams:** `DISTINCT` returns the title once regardless of event count or channel.
- **Same title on different content IDs:** The output still contains one row because distinctness is defined on title.
- **Boundary timestamps:** Formatting includes every time on June 30 and excludes every time on July 1. A half-open range alternative makes those boundaries more explicit.
- **Case and collation:** Comparisons to `Y` and `Movies`, as well as title deduplication, follow MySQL collation rules unless a collation is specified.
- **Null fields:** A null date, flag, type, or join key does not make the equality predicate true and therefore does not qualify.
- **No qualifying movies:** The query correctly returns an empty result set.
- **Unrestricted order:** Adding an order is unnecessary; without `ORDER BY`, consumers must not rely on a stable row sequence.
- **Mismatched join-key types:** Implicit conversion may work in MySQL but can hurt portability and index use. Consistent schema types are preferable.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(T \log T)$. Let $P$ be the number of `TVProgram` rows, $C$ the number of `Content` rows, and $T$ the number of qualifying joined rows or title values processed by duplicate elimination. A typical hash-join plan can scan and join in expected $O(P+C)$ time. Removing duplicates can use hashing in expected $O(T)$ time or sorting in $O(T \log T)$ time. The manifest's $O(P + C + T \log T)$ time and $O(C + T)$ space describe a reasonable sort-based physical model.
- **Auxiliary Space Complexity:** $O(C + T)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
