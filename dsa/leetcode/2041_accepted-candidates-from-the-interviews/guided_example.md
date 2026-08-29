# Guided Example: Accepted Candidates From the Interviews

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Candidates": [{"candidate_id": 11, "name": "Atticus", "years_of_exp": 1, "interview_id": 101}, {"candidate_id": 9, "name": "Ruben", "years_of_exp": 6, "interview_id": 104}, {"candidate_id": 6, "name": "Aliza", "years_of_exp": 10, "interview_id": 109}, {"candidate_id": 8, "name": "Alfredo", "years_of_exp": 0, "interview_id": 107}], "Rounds": [{"interview_id": 109, "round_id": 3, "score": 4}, {"interview_id": 101, "round_id": 2, "score": 8}, {"interview_id": 109, "round_id": 4, "score": 1}, {"interview_id": 107, "round_id": 1, "score": 3}, {"interview_id": 104, "round_id": 3, "score": 6}, {"interview_id": 109, "round_id": 1, "score": 4}, {"interview_id": 104, "round_id": 4, "score": 7}, {"interview_id": 104, "round_id": 1, "score": 2}, {"interview_id": 109, "round_id": 2, "score": 1}, {"interview_id": 104, "round_id": 2, "score": 7}, {"interview_id": 107, "round_id": 2, "score": 3}, {"interview_id": 101, "round_id": 1, "score": 8}]}}`
- **Required output:** `{"columns": ["candidate_id"], "rows": [[9]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Candidates`

The objective is to compute `{"columns": ["candidate_id"], "rows": [[9]]}` from `{"tables": {"Candidates": [{"candidate_id": 11, "name": "Atticus", "years_of_exp": 1, "interview_id": 101}, {"candidate_id": 9, "name": "Ruben", "years_of_exp": 6, "interview_id": 104}, {"candidate_id": 6, "name": "Aliza", "years_of_exp": 10, "interview_id": 109}, {"candidate_id": 8, "name": "Alfredo", "years_of_exp": 0, "interview_id": 107}], "Rounds": [{"interview_id": 109, "round_id": 3, "score": 4}, {"interview_id": 101, "round_id": 2, "score": 8}, {"interview_id": 109, "round_id": 4, "score": 1}, {"interview_id": 107, "round_id": 1, "score": 3}, {"interview_id": 104, "round_id": 3, "score": 6}, {"interview_id": 109, "round_id": 1, "score": 4}, {"interview_id": 104, "round_id": 4, "score": 7}, {"interview_id": 104, "round_id": 1, "score": 2}, {"interview_id": 109, "round_id": 2, "score": 1}, {"interview_id": 104, "round_id": 2, "score": 7}, {"interview_id": 107, "round_id": 2, "score": 3}, {"interview_id": 101, "round_id": 1, "score": 8}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Join candidates to all rounds of their interview

The candidate row contains `interview_id` but not the individual scores. The `Rounds` table contains those scores under the same identifier. The query uses

`Candidates JOIN Rounds USING (interview_id)`

to create one joined row for each matching candidate-round combination.

`JOIN` without another qualifier is an inner join. A candidate whose interview has no matching round contributes no joined row and therefore cannot appear in the final grouped result.

`USING (interview_id)` is shorthand for equality of the two tables' identically named `interview_id` columns. It also exposes one merged join column rather than two separately qualified copies.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Candidates": [{"candidate_id": 11, "name": "Atticus", "years_of_exp": 1, "interview_id": 101}, {"candidate_id": 9, "name": "Ruben", "years_of_exp": 6, "interview_id": 104}, {"candidate_id": 6, "name": "Aliza", "years_of_exp": 10, "interview_id": 109}, {"candidate_id": 8, "name": "Alfredo", "years_of_exp": 0, "interview_id": 107}], "Rounds": [{"interview_id": 109, "round_id": 3, "score": 4}, {"interview_id": 101, "round_id": 2, "score": 8}, {"interview_id": 109, "round_id": 4, "score": 1}, {"interview_id": 107, "round_id": 1, "score": 3}, {"interview_id": 104, "round_id": 3, "score": 6}, {"interview_id": 109, "round_id": 1, "score": 4}, {"interview_id": 104, "round_id": 4, "score": 7}, {"interview_id": 104, "round_id": 1, "score": 2}, {"interview_id": 109, "round_id": 2, "score": 1}, {"interview_id": 104, "round_id": 2, "score": 7}, {"interview_id": 107, "round_id": 2, "score": 3}, {"interview_id": 101, "round_id": 1, "score": 8}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Apply the experience requirement before aggregation

`WHERE years_of_exp >= 2` removes candidates with fewer than two years of experience.

The boundary is inclusive: a candidate with exactly two years passes. Filtering before grouping is appropriate because `years_of_exp` is a property of the candidate row, not an aggregate of interview rounds.

Once an inexperienced candidate is removed, none of that candidate's joined round rows contribute to later grouping.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Group all round rows by candidate

`GROUP BY 1` uses an ordinal reference to the first selected expression. The only selected expression is `candidate_id`, so this means “group by candidate identifier.”

Every joined round belonging to the same candidate enters that candidate's group. The composite primary key on `Rounds` ensures each interview round identifier occurs at most once for an interview, so a single round row is not duplicated within `Rounds` itself.

If two candidate rows happen to reference the same interview identifier, they still have different `candidate_id` groups. Each candidate is evaluated separately, which is consistent with reporting candidate IDs.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["candidate_id"], "rows": [[9]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Candidates": [{"candidate_id": 11, "name": "Atticus", "years_of_exp": 1, "interview_id": 101}, {"candidate_id": 9, "name": "Ruben", "years_of_exp": 6, "interview_id": 104}, {"candidate_id": 6, "name": "Aliza", "years_of_exp": 10, "interview_id": 109}, {"candidate_id": 8, "name": "Alfredo", "years_of_exp": 0, "interview_id": 107}], "Rounds": [{"interview_id": 109, "round_id": 3, "score": 4}, {"interview_id": 101, "round_id": 2, "score": 8}, {"interview_id": 109, "round_id": 4, "score": 1}, {"interview_id": 107, "round_id": 1, "score": 3}, {"interview_id": 104, "round_id": 3, "score": 6}, {"interview_id": 109, "round_id": 1, "score": 4}, {"interview_id": 104, "round_id": 4, "score": 7}, {"interview_id": 104, "round_id": 1, "score": 2}, {"interview_id": 109, "round_id": 2, "score": 1}, {"interview_id": 104, "round_id": 2, "score": 7}, {"interview_id": 107, "round_id": 2, "score": 3}, {"interview_id": 101, "round_id": 1, "score": 8}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["candidate_id"], "rows": [[9]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Aggregate rounds first:** Build one total per `interview_id`, filter totals above fifteen, then join to experienced candidates; often reduces join volume.
- **Correlated subquery:** Sum rounds for each candidate, but without good indexing it can repeat work.
- **`WHERE` for experience:** Correct because experience is a row attribute evaluated before grouping.
- **`HAVING` for score total:** Required because the threshold applies to an aggregate.
- **Exactly two years of experience:** Included by `>= 2`.
- **Exactly fifteen total points:** Excluded by strict `> 15`.
- **No matching rounds:** Excluded by the inner join and cannot form a qualifying total.
- **Several rounds:** All matching `score` values are added.
- **Shared interview identifier:** Candidates remain separate because grouping uses `candidate_id`.
- **Duplicate candidate output:** Prevented by one group per primary-key identifier.
- **Any row order:** No `ORDER BY` is necessary.
- **`GROUP BY 1`:** Refers to the first selected expression, `candidate_id`; naming the column explicitly would be clearer but equivalent.
- **Null score outside the stated model:** `SUM` ignores null values; an all-null group would not pass the comparison.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(J)$. Let $C$ be candidate rows, $R$ round rows, and $J$ the number of joined candidate-round rows after matching interview IDs. With hash-based join and aggregation, expected work is $O(C+R+J)$ and working space is $O(C+R)$ in a broad upper-bound description.
- **Auxiliary Space Complexity:** $O(C+R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
