# Guided Example: Consecutive Available Seats

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Cinema": [{"seat_id": 1, "free": 1}, {"seat_id": 2, "free": 0}, {"seat_id": 3, "free": 1}, {"seat_id": 4, "free": 1}, {"seat_id": 5, "free": 1}]}}`
- **Required output:** `{"columns": ["seat_id"], "rows": [[3], [4], [5]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Cinema`

The objective is to compute `{"columns": ["seat_id"], "rows": [[3], [4], [5]]}` from `{"tables": {"Cinema": [{"seat_id": 1, "free": 1}, {"seat_id": 2, "free": 0}, {"seat_id": 3, "free": 1}, {"seat_id": 4, "free": 1}, {"seat_id": 5, "free": 1}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Matching adjacent IDs

The join condition:



accepts both directions:

- `b.seat_id = a.seat_id - 1`;
- `b.seat_id = a.seat_id + 1`.

Absolute difference one means numerical adjacency. Difference zero would pair a seat with itself and must not count. A larger difference leaves at least one seat ID between them and is not consecutive.

The schema calls `seat_id` auto-incrementing and models the $i$th seat with that ID. The problem’s consecutive-seat rule is therefore based on consecutive ID values.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Cinema": [{"seat_id": 1, "free": 1}, {"seat_id": 2, "free": 0}, {"seat_id": 3, "free": 1}, {"seat_id": 4, "free": 1}, {"seat_id": 5, "free": 1}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Both endpoints must be available

The rest of the join condition is:



In MySQL Boolean context, a stored 1 is true and 0 is false. Requiring both filters out:

- an occupied candidate `a` beside a free seat;
- a free candidate beside only an occupied `b`;
- two occupied adjacent seats.

Only a free-free adjacent pair creates joined rows.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The rest of the join condition is:



In MySQL Boolean conte... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why `DISTINCT` is necessary

Consider three free seats 3, 4, and 5. Alias `a` at seat 4 matches both `b = 3` and `b = 5`, so the join produces two rows whose selected `a.seat_id` is 4. The answer should list seat 4 once.

`SELECT DISTINCT a.seat_id` removes duplicate candidate IDs after all matching neighbors have established eligibility. Endpoint seats 3 and 5 each have one matching neighbor and also appear once.

The join is symmetric, so adjacent pair 3–4 produces one result with `a=3,b=4` and another with `a=4,b=3`. This is intentional: both seats belong in the answer.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["seat_id"], "rows": [[3], [4], [5]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Cinema": [{"seat_id": 1, "free": 1}, {"seat_id": 2, "free": 0}, {"seat_id": 3, "free": 1}, {"seat_id": 4, "free": 1}, {"seat_id": 5, "free": 1}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["seat_id"], "rows": [[3], [4], [5]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **`LAG` and `LEAD`:** Order rows by `seat_id` an:** - **`LAG` and `LEAD`:** Order rows by `seat_id` and inspect neighboring IDs/free flags. Avoids a self-join but must verify ID difference one, not merely row adjacency if gaps are possible.
- **Two explicit joins or `EXISTS`:** Check for a free row at `seat_id - 1` or `seat_id + 1`. Equality predicates can use an index more directly than `ABS`.
- **Union oriented neighbor pairs:** Select both endpoints of every free pair with `UNION`. Naturally deduplicates but repeats query structure.
- **Missing `DISTINCT`:** A middle seat in a run appears once per free neighbor and would be duplicated.
- **Occupied middle seat:** Breaks the run; free seats on opposite sides are two IDs apart and do not match directly.
- **Run of two:** Both seats qualify because each has the other as a neighbor.
- **Run of three or more:** Every endpoint has one match and every interior seat has two; all appear once after deduplication.
- **Isolated free seat:** Has no joined row and is correctly excluded.
- **First or last seat:** Needs only its one possible in-range neighbor; no boundary special case is required in a relational join.
- **ID gaps:** Difference one, not physical row adjacency, controls qualification.
- **Boolean semantics:** `a.free` and `b.free` rely on 1/0 truth values stated by the schema.
- **Ordinal ordering:** `ORDER BY 1` means selected seat ID ascending.
- **Physical-plan caveat:** An `ABS` join can degrade to quadratic pair testing; asymptotic performance is not guaranteed solely by the manifest.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of cinema rows. SQL is declarative, so physical cost depends heavily on how the optimizer executes the self-join.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
