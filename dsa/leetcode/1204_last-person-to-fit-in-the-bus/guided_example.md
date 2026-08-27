# Guided Example: Last Person to Fit in the Bus

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Queue": [{"person_id": 5, "person_name": "Alice", "weight": 250, "turn": 1}, {"person_id": 4, "person_name": "Bob", "weight": 175, "turn": 5}, {"person_id": 3, "person_name": "Alex", "weight": 350, "turn": 2}, {"person_id": 6, "person_name": "John Cena", "weight": 400, "turn": 3}, {"person_id": 1, "person_name": "Winston", "weight": 500, "turn": 6}, {"person_id": 2, "person_name": "Marie", "weight": 200, "turn": 4}]}}`
- **Required output:** `{"columns": ["person_name"], "rows": [["John Cena"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Queue`

The objective is to compute `{"columns": ["person_name"], "rows": [["John Cena"]]}` from `{"tables": {"Queue": [{"person_id": 5, "person_name": "Alice", "weight": 250, "turn": 1}, {"person_id": 4, "person_name": "Bob", "weight": 175, "turn": 5}, {"person_id": 3, "person_name": "Alex", "weight": 350, "turn": 2}, {"person_id": 6, "person_name": "John Cena", "weight": 400, "turn": 3}, {"person_id": 1, "person_name": "Winston", "weight": 500, "turn": 6}, {"person_id": 2, "person_name": "Marie", "weight": 200, "turn": 4}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Create every candidate-prefix relationship

The `FROM` clause lists `Queue AS a, Queue AS b`, which is the older comma syntax for a cross join. Alias `a` represents a candidate last person. Alias `b` represents a person who may belong to that candidate’s boarding prefix.

The condition `a.turn >= b.turn` retains exactly the `b` rows whose turn is no later than candidate `a`. Thus candidate at turn one pairs with one row, candidate at turn two pairs with the first two rows, and candidate at turn $t$ pairs with all $t$ prefix rows.

The input guarantees that turns contain every integer from one through $n$, so there are no gaps or ties in boarding order.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Queue": [{"person_id": 5, "person_name": "Alice", "weight": 250, "turn": 1}, {"person_id": 4, "person_name": "Bob", "weight": 175, "turn": 5}, {"person_id": 3, "person_name": "Alex", "weight": 350, "turn": 2}, {"person_id": 6, "person_name": "John Cena", "weight": 400, "turn": 3}, {"person_id": 1, "person_name": "Winston", "weight": 500, "turn": 6}, {"person_id": 2, "person_name": "Marie", "weight": 200, "turn": 4}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Group the joined rows back by candidate

`GROUP BY a.person_id` gathers all retained prefix rows for one candidate. Because `person_id` is unique, it functionally determines that candidate’s name and turn. Selecting `a.person_name` and later ordering by `a.turn` therefore refers to one unambiguous candidate within each group.

Some strict SQL configurations express this dependency more clearly by grouping by every selected nonaggregate column as well. Under the intended MySQL semantics and unique-ID guarantee, grouping by the ID identifies the row.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `GROUP BY a.person_id` gathers all retained prefix rows for ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Use the prefix sum as the feasibility test

`SUM(b.weight)` is the total weight of everyone whose turn is at most the candidate’s turn. The `HAVING` clause is used rather than `WHERE` because the condition depends on an aggregate:

`HAVING SUM(b.weight) <= 1000`.

A prefix totaling exactly 1000 is feasible. Only a value greater than 1000 is rejected.

For candidate John Cena at turn three in the example, the matching `b` rows are Alice, Alex, and John Cena. Their weights total 1000, so the candidate survives. Marie at turn four has a prefix total of 1200 and is filtered out.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["person_name"], "rows": [["John Cena"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Queue": [{"person_id": 5, "person_name": "Alice", "weight": 250, "turn": 1}, {"person_id": 4, "person_name": "Bob", "weight": 175, "turn": 5}, {"person_id": 3, "person_name": "Alex", "weight": 350, "turn": 2}, {"person_id": 6, "person_name": "John Cena", "weight": 400, "turn": 3}, {"person_id": 1, "person_name": "Winston", "weight": 500, "turn": 6}, {"person_id": 2, "person_name": "Marie", "weight": 200, "turn": 4}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["person_name"], "rows": [["John Cena"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Window-function running sum:** Compute `SUM(we:** - **Window-function running sum:** Compute `SUM(weight) OVER (ORDER BY turn)` once, filter running totals at most 1000, and choose the greatest turn. This gives a clearer $O(n\log n)$ sort-based plan on modern MySQL.
- **Correlated prefix subquery:** Sum rows with turn no greater than each candidate’s turn. It expresses the same logic but may also become quadratic without optimizer help.
- **First person exactly reaches 1000:** The inclusive `<=` condition keeps that person, and every later positive weight makes later prefixes infeasible.
- **First-person guarantee:** It ensures `LIMIT 1` has a surviving row to return.
- **Unique turns:** Descending order identifies one last candidate without tie handling.
- **Unique person IDs:** Grouping by `a.person_id` identifies one candidate’s name and turn through functional dependency.
- **Positive weights:** They make cumulative totals monotone and match the boarding interpretation. Negative weights would make a later prefix feasible again, an unrealistic case not intended by the table semantics.
- **Any input row order:** The query uses `turn` values rather than physical table order, so shuffled storage does not change the result.
- **Capacity equality:** A total of exactly 1000 is allowed and must not be rejected.
- **Comma join syntax:** It is equivalent here to `CROSS JOIN` followed by the `WHERE` condition, but explicit join syntax is often easier to read.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let $n$ be the number of queue rows.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
