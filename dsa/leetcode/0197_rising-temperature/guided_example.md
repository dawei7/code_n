# Guided Example: Rising Temperature

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Weather": [{"id": 1, "recordDate": "2015-01-01", "temperature": 10}, {"id": 2, "recordDate": "2015-01-02", "temperature": 25}, {"id": 3, "recordDate": "2015-01-03", "temperature": 20}, {"id": 4, "recordDate": "2015-01-04", "temperature": 30}]}}`
- **Required output:** `{"columns": ["id"], "rows": [[2], [4]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Weather`

The objective is to compute `{"columns": ["id"], "rows": [[2], [4]]}` from `{"tables": {"Weather": [{"id": 1, "recordDate": "2015-01-01", "temperature": 10}, {"id": 2, "recordDate": "2015-01-02", "temperature": 25}, {"id": 3, "recordDate": "2015-01-03", "temperature": 20}, {"id": 4, "recordDate": "2015-01-04", "temperature": 30}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Pair each current day with the exact calendar day before it

The query reads `Weather` twice through aliases `w1` and `w2`. Alias `w1`
represents the candidate current day whose ID might be returned. Alias `w2`
represents that candidate's possible yesterday row.

This self-join is needed because current and previous temperatures live in two
different table rows. Joining places both values into one logical result row so
they can be compared.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Weather": [{"id": 1, "recordDate": "2015-01-01", "temperature": 10}, {"id": 2, "recordDate": "2015-01-02", "temperature": 25}, {"id": 3, "recordDate": "2015-01-03", "temperature": 20}, {"id": 4, "recordDate": "2015-01-04", "temperature": 30}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use date arithmetic rather than row order

`DATEDIFF(w1.recordDate, w2.recordDate) = 1` requires `w1` to be exactly one
calendar day after `w2`. In MySQL, `DATEDIFF(later, earlier)` returns their day
difference, so argument order matters. Reversing the arguments would identify
tomorrow relative to `w1` instead of yesterday.

The condition does not mean “the previous row” and does not depend on IDs being
consecutive. IDs are merely unique labels; dates determine chronology. It also
does not compare with the nearest earlier available record if a date is
missing. A gap of two or more days fails the equality and correctly provides no
yesterday comparison.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Require a strict temperature increase

The second join predicate is `w1.temperature > w2.temperature`. Equality is not
a rise, so it must not use `>=`. A lower current temperature also fails.

Both date adjacency and temperature increase appear in the `ON` clause. Since
this is an inner join, placing the temperature predicate in a `WHERE` clause
would produce the same result. Keeping both pair-validity conditions together
makes the meaning of a qualifying pair explicit.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["id"], "rows": [[2], [4]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Weather": [{"id": 1, "recordDate": "2015-01-01", "temperature": 10}, {"id": 2, "recordDate": "2015-01-02", "temperature": 25}, {"id": 3, "recordDate": "2015-01-03", "temperature": 20}, {"id": 4, "recordDate": "2015-01-04", "temperature": 30}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["id"], "rows": [[2], [4]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Date-add equality join:** Join `w1.recordDate = DATE_ADD(w2.recordDate, INTERVAL 1 DAY)`; this states the transformed-yesterday relation directly.
- **`LAG()` window function:** Sort by date, retrieve prior date and temperature, then verify the date gap is exactly one day.
- **Correlated subquery:** Look up temperature at `DATE_SUB(w1.recordDate, INTERVAL 1 DAY)` for each current row.
- **Pandas shifted merge:** Add one day to a copied date column and merge, as the local editorial describes.
- **Missing calendar day:** Do not compare with the nearest older observation.
- **Equal temperature:** Strict `>` rejects it.
- **Duplicate dates:** Excluded by contract; otherwise duplicate output or ambiguous comparison could occur.
- **First represented date:** Qualifies only if its actual yesterday is also represented.
- **Null data:** Cannot establish both predicates and is omitted by SQL three-valued logic.
- **Any order:** No `ORDER BY` is required.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. Let $n$ be the number of Weather rows. A naive self-join evaluates up to $n^2$
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
