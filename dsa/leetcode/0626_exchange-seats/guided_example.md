# Guided Example: Exchange Seats

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Seat": [{"id": 1, "student": "Abbot"}, {"id": 2, "student": "Doris"}, {"id": 3, "student": "Emerson"}, {"id": 4, "student": "Green"}, {"id": 5, "student": "Jeames"}]}}`
- **Required output:** `{"columns": ["id", "student"], "rows": [[1, "Doris"], [2, "Abbot"], [3, "Green"], [4, "Emerson"], [5, "Jeames"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Seat`

The objective is to compute `{"columns": ["id", "student"], "rows": [[1, "Doris"], [2, "Abbot"], [3, "Green"], [4, "Emerson"], [5, "Jeames"]]}` from `{"tables": {"Seat": [{"id": 1, "student": "Abbot"}, {"id": 2, "student": "Doris"}, {"id": 3, "student": "Emerson"}, {"id": 4, "student": "Green"}, {"id": 5, "student": "Jeames"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**Keep each output seat ID and fetch the student from its partner seat.** The result can be viewed in two equivalent ways: change every student's ID, or keep the ordered ID rows and replace each row's student with the student from the paired ID. The exact query uses the second view.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Seat": [{"id": 1, "student": "Abbot"}, {"id": 2, "student": "Doris"}, {"id": 3, "student": "Emerson"}, {"id": 4, "student": "Green"}, {"id": 5, "student": "Jeames"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

`Seat AS s1` is the output-seat side. The query always selects `s1.id`, so every original seat ID appears exactly once. `Seat AS s2` is the partner side. A self-join calculates which partner ID should provide the student for each `s1` row.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Derive the partner transformation.** Consecutive pairs are `(1,2)`, `(3,4)`, `(5,6)`, and so on. The required mapping is:

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["id", "student"], "rows": [[1, "Doris"], [2, "Abbot"], [3, "Green"], [4, "Emerson"], [5, "Jeames"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Seat": [{"id": 1, "student": "Abbot"}, {"id": 2, "student": "Doris"}, {"id": 3, "student": "Emerson"}, {"id": 4, "student": "Green"}, {"id": 5, "student": "Jeames"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["id", "student"], "rows": [[1, "Doris"], [2, "Abbot"], [3, "Green"], [4, "Emerson"], [5, "Jeames"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **`CASE` on odd and even IDs:** Count rows, map complete odd IDs to `id + 1`, even IDs to `id - 1`, and retain the final odd ID. This is more verbose but avoids bit manipulation.
- **Window functions:** Use `LEAD(student)` for odd rows and `LAG(student)` for even rows after ordering by ID. This states the neighboring-row intent clearly but still needs the last-row fallback.
- **Fully parenthesized bit expression:** Write `((s1.id + 1) ^ 1) - 1` to make precedence explicit.
- **Even number of rows:** Every ID has a partner, so `COALESCE` always chooses `s2.student`.
- **Odd number of rows:** Only the final odd ID lacks a partner and retains its original student.
- **One row:** Its computed partner is ID 2, which is absent, so the sole student remains unchanged.
- **Continuous-ID guarantee:** Without it, missing interior partners would silently trigger the fallback and no longer represent consecutive-seat swapping.
- **Primary-key guarantee:** It ensures each computed partner contributes at most one joined row.
- **Nullable student names:** If a real partner row existed with `student = NULL`, `COALESCE` would fall back to the wrong original name. The intended challenge data treats student names as present; otherwise partner existence should be tested separately.
- **`ORDER BY 1`:** It depends on the first projection remaining `s1.id`. Naming the column is more maintainable.
- **Dialect portability:** `^` is bitwise XOR in MySQL but can mean something else elsewhere; a `CASE` or modulo expression is easier to port.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R\log R)$. Let $R$ be the number of rows in `Seat`. The query scans $R$ output-side rows. Looking up each computed partner through the primary-key index can cost $O(\log R)$ per lookup in a general tree index, and the final ordering can cost $O(R\log R)$. The manifest's conservative total time bound is therefore $O(R\log R)$.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
