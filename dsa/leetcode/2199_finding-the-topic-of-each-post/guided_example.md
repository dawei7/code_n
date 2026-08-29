# Guided Example: Finding the Topic of Each Post

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Keywords": [{"topic_id": 1, "word": "handball"}, {"topic_id": 1, "word": "football"}, {"topic_id": 3, "word": "WAR"}, {"topic_id": 2, "word": "Vaccine"}], "Posts": [{"post_id": 1, "content": "We call it soccer They call it football hahaha"}, {"post_id": 2, "content": "Americans prefer basketball while Europeans love handball and football"}, {"post_id": 3, "content": "stop the war and play handball"}, {"post_id": 4, "content": "warning I planted some flowers this morning and then got vaccinated"}]}}`
- **Required output:** `{"columns": ["post_id", "topic"], "rows": [[1, "1"], [2, "1"], [3, "1,3"], [4, "Ambiguous!"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Keywords`

The objective is to compute `{"columns": ["post_id", "topic"], "rows": [[1, "1"], [2, "1"], [3, "1,3"], [4, "Ambiguous!"]]}` from `{"tables": {"Keywords": [{"topic_id": 1, "word": "handball"}, {"topic_id": 1, "word": "football"}, {"topic_id": 3, "word": "WAR"}, {"topic_id": 2, "word": "Vaccine"}], "Posts": [{"post_id": 1, "content": "We call it soccer They call it football hahaha"}, {"post_id": 2, "content": "Americans prefer basketball while Europeans love handball and football"}, {"post_id": 3, "content": "stop the war and play handball"}, {"post_id": 4, "content": "warning I planted some flowers this morning and then got vaccinated"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Preserve every post with a left join

`Posts LEFT JOIN Keywords` keeps one output-side row for every post even when no keyword satisfies the join condition.

An inner join would discard posts with no topic, making it impossible to return their required ambiguous label without a separate recovery step.

When no keyword matches, columns from `Keywords` are null in the retained joined row.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Keywords": [{"topic_id": 1, "word": "handball"}, {"topic_id": 1, "word": "football"}, {"topic_id": 3, "word": "WAR"}, {"topic_id": 2, "word": "Vaccine"}], "Posts": [{"post_id": 1, "content": "We call it soccer They call it football hahaha"}, {"post_id": 2, "content": "Americans prefer basketball while Europeans love handball and football"}, {"post_id": 3, "content": "stop the war and play handball"}, {"post_id": 4, "content": "warning I planted some flowers this morning and then got vaccinated"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Pad both content and keyword with spaces

The join condition searches

`CONCAT(' ', content, ' ')`

for

`CONCAT(' ', word, ' ')`.

Adding a space on both sides turns beginning and ending word boundaries into the same pattern as internal boundaries. Keyword `"war"` matches `"war stories"`, `"stop war"`, or content exactly `"war"` because the padded text contains `" war "`.

It does not match `"warning"` because that substring is followed by `"ning"` rather than a space.

The content contract contains only English letters and spaces, so spaces are the only token boundaries the query needs to recognize. Multiple spaces do not prevent a word itself from having at least one space immediately before and after it.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Use `INSTR` as an existence test

`INSTR(haystack, needle)` returns a positive position when the padded keyword occurs and zero otherwise. Comparing it with `> 0` turns the search into the join predicate.

Only existence matters. A keyword appearing several times in the same post still produces one joined row for that `Keywords` record.

If the same word maps to several topics, there are several keyword rows and all corresponding topics can join.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["post_id", "topic"], "rows": [[1, "1"], [2, "1"], [3, "1,3"], [4, "Ambiguous!"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Keywords": [{"topic_id": 1, "word": "handball"}, {"topic_id": 1, "word": "football"}, {"topic_id": 3, "word": "WAR"}, {"topic_id": 2, "word": "Vaccine"}], "Posts": [{"post_id": 1, "content": "We call it soccer They call it football hahaha"}, {"post_id": 2, "content": "Americans prefer basketball while Europeans love handball and football"}, {"post_id": 3, "content": "stop the war and play handball"}, {"post_id": 4, "content": "warning I planted some flowers this morning and then got vaccinated"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["post_id", "topic"], "rows": [[1, "1"], [2, "1"], [3, "1,3"], [4, "Ambiguous!"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Explicit lowercase normalization:** Apply `LOWER` to both padded operands or a declared case-insensitive collation so correctness does not depend on the database default.
- **Explicit ordered aggregation:** Use the target dialect's syntax to sort distinct numeric topic IDs inside aggregation; this is required for a guaranteed ascending topic string.
- **MySQL `GROUP_CONCAT`:** In native MySQL, distinct ordered aggregation is normally expressed with `GROUP_CONCAT` and an internal `ORDER BY`.
- **Split content into tokens:** Tokenization and equality joins can avoid repeated substring searches, but require engine-specific string-splitting support.
- **Keyword at content start or end:** Padding creates the missing outside boundary and allows the match.
- **Keyword inside a longer word:** Required surrounding spaces prevent false matches such as `war` in `warning`.
- **Several keywords for one topic:** `DISTINCT topic_id` prevents duplicate IDs in the result.
- **One keyword for several topics:** Separate keyword rows cause all those distinct topics to appear.
- **No matching keyword:** The left join retains the post and `COALESCE` returns `Ambiguous!`.
- **Case difference:** Correctness depends on a case-insensitive collation because the exact source performs no lowercase conversion.
- **Output row order:** No final `ORDER BY` is needed because the result table may be returned in any order.
- **Topic-string order:** Unlike row order, numeric order inside the topic string is required and is not guaranteed by the exact aggregate text.
- **Dialect portability:** `STRING_AGG(DISTINCT ..., ',')` is not uniformly supported under the MySQL label.
- **Manifest discrepancy:** The source neither lowercases explicitly nor orders the aggregate explicitly.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(pkL + t log t)$. Let $P$ be the number of posts, $K$ the number of keyword rows, and $L$ an upper bound on the text inspected by one substring search. Without a specialized text index, the join may test every post-keyword pair, costing $O(PKL)$.
- **Auxiliary Space Complexity:** $O(T)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
