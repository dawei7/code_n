# Guided Example: Winning Candidate

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Candidate": [{"id": 1, "Name": "A"}, {"id": 2, "Name": "B"}, {"id": 3, "Name": "C"}, {"id": 4, "Name": "D"}, {"id": 5, "Name": "E"}], "Vote": [{"id": 1, "CandidateId": 2}, {"id": 2, "CandidateId": 4}, {"id": 3, "CandidateId": 3}, {"id": 4, "CandidateId": 2}, {"id": 5, "CandidateId": 5}]}}`
- **Required output:** `{"columns": ["Name"], "rows": [["B"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Candidate`

The objective is to compute `{"columns": ["Name"], "rows": [["B"]]}` from `{"tables": {"Candidate": [{"id": 1, "Name": "A"}, {"id": 2, "Name": "B"}, {"id": 3, "Name": "C"}, {"id": 4, "Name": "D"}, {"id": 5, "Name": "E"}], "Vote": [{"id": 1, "CandidateId": 2}, {"id": 2, "CandidateId": 4}, {"id": 3, "CandidateId": 3}, {"id": 4, "CandidateId": 2}, {"id": 5, "CandidateId": 5}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Building one group per voted-for candidate

The derived table named `t` reads `Vote` and executes:



`GROUP BY CandidateId` collects all vote rows with the same `CandidateId` into one group. If candidate 2 appears in three vote rows, the group for candidate 2 contains three rows. The expression `COUNT(id)` then counts the non-`NULL` `Vote.id` values in that group. According to the schema, `Vote.id` is an auto-increment primary key, so it is present and unique for every vote. Consequently, `COUNT(id)` is exactly the number of votes in the group. `COUNT(*)` would express the same fact here, but `COUNT(id)` is correct because that column cannot be `NULL`.

The grouped result conceptually contains one row per candidate who received at least one vote. Although the count is used for ordering, it does not have to appear in the selected output. `ORDER BY COUNT(id) DESC` places the group with the greatest count first. `LIMIT 1` then retains only that first group, leaving the winning candidate’s ID.

The statement guarantees that exactly one candidate wins. This guarantee matters: if two groups had the same maximum count, ordering only by the count would not specify which tied group comes first. The query deliberately has no tie-breaking rule because the input contract says no tie for first place exists. With a unique maximum, the first row after descending ordering is unambiguous.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Candidate": [{"id": 1, "Name": "A"}, {"id": 2, "Name": "B"}, {"id": 3, "Name": "C"}, {"id": 4, "Name": "D"}, {"id": 5, "Name": "E"}], "Vote": [{"id": 1, "CandidateId": 2}, {"id": 2, "CandidateId": 4}, {"id": 3, "CandidateId": 3}, {"id": 4, "CandidateId": 2}, {"id": 5, "CandidateId": 5}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why candidates with zero votes do not need a group

The grouped subquery begins from `Vote`, so a candidate with no ballots never appears in `t`. That is safe. A zero-vote candidate cannot have a strictly larger count than the unique winner when the election contains votes. The winner’s ID must therefore occur in `Vote`. Starting with `Candidate` and left-joining every possible vote count would include extra zero-count rows without changing which candidate has the maximum.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Turning the winning ID into the requested name

The outer part gives the `Candidate` table the alias `c` and performs:



The schema states that `Vote.candidateId` references `Candidate.id`. The ID selected by `t` therefore has a matching candidate row. An inner join is the appropriate operation: it combines the single winning-ID row with that matching candidate record. The final `SELECT Name` discards the ID and returns precisely the requested column.

It helps to trace the sample. The vote IDs point to candidates 2, 4, 3, 2, and 5. Grouping produces counts equivalent to `(2, 2)`, `(3, 1)`, `(4, 1)`, and `(5, 1)`, where each pair is candidate ID followed by count. Descending order places candidate 2 first; `LIMIT 1` keeps ID 2; and the join finds `Candidate.id = 2`, whose name is `B`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["Name"], "rows": [["B"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Candidate": [{"id": 1, "Name": "A"}, {"id": 2, "Name": "B"}, {"id": 3, "Name": "C"}, {"id": 4, "Name": "D"}, {"id": 5, "Name": "E"}], "Vote": [{"id": 1, "CandidateId": 2}, {"id": 2, "CandidateId": 4}, {"id": 3, "CandidateId": 3}, {"id": 4, "CandidateId": 2}, {"id": 5, "CandidateId": 5}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["Name"], "rows": [["B"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Aggregate first, then use `MAX`:** A second aggregation can compute the largest count, after which another join selects the group with that count. This avoids `LIMIT` but usually makes the query longer. It must still rely on the unique-winner guarantee or intentionally return every tied winner.
- **Join names before grouping:** Joining `Vote` to `Candidate` first and grouping by candidate ID and name can also work. It carries name data through aggregation even though only the winning name is needed, so selecting the ID first keeps the intermediate relation narrower.
- **Window-function ranking:** A count per candidate followed by `ROW_NUMBER` or `RANK` can express the ranking explicitly. It is valuable when tied winners need special handling, but it is more machinery than this unique-winner contract requires.
- **Correlated count per candidate:** Counting votes separately for every candidate is easy to imagine but may repeatedly scan `Vote`, producing much more work than one grouped pass.
- **Unique winner:** The lack of a secondary `ORDER BY` key is correct only because exactly one candidate has the largest count. If ties were allowed, `LIMIT 1` would arbitrarily choose one tied row unless the problem specified a tie rule.
- **Candidates with no votes:** They are absent from the grouped subquery. That does not affect a nonempty election’s unique positive-count winner, and it avoids inventing zero-valued groups.
- **Foreign-key integrity:** The inner join assumes every voted-for `CandidateId` exists in `Candidate`, exactly as the schema guarantees. Without that guarantee, an invalid winning ID could disappear during the join.
- **Counting the right column:** `COUNT(id)` is safe because `Vote.id` is a non-`NULL` primary key. Counting a nullable column could undercount rows; `COUNT(*)` is the clearer general choice when nullability is uncertain.
- **Output order:** Only one row is returned, so no final ordering is needed.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(C)$. Let $V$ be the number of rows in `Vote`, let $C$ be the number of rows in `Candidate`, and let $G$ be the number of distinct candidate IDs that actually receive votes. We have $G \le C$ and $G \le V$.
- **Auxiliary Space Complexity:** $O(C)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
