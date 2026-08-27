# Guided Example: Human Traffic of Stadium

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Stadium": [{"id": 1, "visit_date": "2017-01-01", "people": 10}, {"id": 2, "visit_date": "2017-01-02", "people": 109}, {"id": 3, "visit_date": "2017-01-03", "people": 150}, {"id": 4, "visit_date": "2017-01-04", "people": 99}, {"id": 5, "visit_date": "2017-01-05", "people": 145}, {"id": 6, "visit_date": "2017-01-06", "people": 1455}, {"id": 7, "visit_date": "2017-01-07", "people": 199}, {"id": 8, "visit_date": "2017-01-08", "people": 188}]}}`
- **Required output:** `{"columns": ["id", "visit_date", "people"], "rows": [[5, "2017-01-05", 145], [6, "2017-01-06", 1455], [7, "2017-01-07", 199], [8, "2017-01-08", 188]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Stadium`

The objective is to compute `{"columns": ["id", "visit_date", "people"], "rows": [[5, "2017-01-05", 145], [6, "2017-01-06", 1455], [7, "2017-01-07", 199], [8, "2017-01-08", 188]]}` from `{"tables": {"Stadium": [{"id": 1, "visit_date": "2017-01-01", "people": 10}, {"id": 2, "visit_date": "2017-01-02", "people": 109}, {"id": 3, "visit_date": "2017-01-03", "people": 150}, {"id": 4, "visit_date": "2017-01-04", "people": 99}, {"id": 5, "visit_date": "2017-01-05", "people": 145}, {"id": 6, "visit_date": "2017-01-06", "people": 1455}, {"id": 7, "visit_date": "2017-01-07", "people": 199}, {"id": 8, "visit_date": "2017-01-08", "people": 188}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Filter before identifying runs

The first common table expression reads:



A low-attendance row must break a qualifying run even if its ID is numerically between two high-attendance rows. Filtering first removes it, but the remaining IDs still retain the numeric gap. The gaps-and-islands label will detect that jump.

For the sample, IDs 2, 3, 5, 6, 7, and 8 remain. ID 4’s removal creates the gap between 3 and 5.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Stadium": [{"id": 1, "visit_date": "2017-01-01", "people": 10}, {"id": 2, "visit_date": "2017-01-02", "people": 109}, {"id": 3, "visit_date": "2017-01-03", "people": 150}, {"id": 4, "visit_date": "2017-01-04", "people": 99}, {"id": 5, "visit_date": "2017-01-05", "people": 145}, {"id": 6, "visit_date": "2017-01-06", "people": 1455}, {"id": 7, "visit_date": "2017-01-07", "people": 199}, {"id": 8, "visit_date": "2017-01-08", "people": 188}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why `id - ROW_NUMBER()` is constant on a consecutive run

`ROW_NUMBER() OVER (ORDER BY id)` assigns 1, 2, 3, ... to filtered rows in increasing ID order. Define:

$$
\texttt{rk}=\texttt{id}-\operatorname{row\_number}.
$$

When both ID and row number increase by one, their difference stays fixed. For IDs 5, 6, 7, and 8 with row numbers 3, 4, 5, and 6, the difference is always two.

At a gap, ID jumps by more than one while row number still advances by exactly one, so the difference changes. IDs 2 and 3 have differences one, while ID 5 starts difference two. Thus, equal `rk` values identify exactly maximal consecutive-ID islands among qualified rows.

This works because `id` values define an ordered integer sequence. The date can skip a day—as between sample IDs 7 and 8—without affecting the island, exactly as the problem states.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `ROW_NUMBER() OVER (ORDER BY id)` assigns 1, 2, 3, ...... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Annotating each island with its size

The second CTE computes:



Window counting retains every original row while attaching the total size of its island. A grouped query would reduce an island to one row and lose the individual records that must be returned.

Every row in the 5–8 island receives `cnt = 4`. Rows 2 and 3 receive count two. The outer `WHERE cnt >= 3` therefore keeps all four rows from the long island and removes both rows from the short island.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["id", "visit_date", "people"], "rows": [[5, "2017-01-05", 145], [6, "2017-01-06", 1455], [7, "2017-01-07", 199], [8, "2017-01-08", 188]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Stadium": [{"id": 1, "visit_date": "2017-01-01", "people": 10}, {"id": 2, "visit_date": "2017-01-02", "people": 109}, {"id": 3, "visit_date": "2017-01-03", "people": 150}, {"id": 4, "visit_date": "2017-01-04", "people": 99}, {"id": 5, "visit_date": "2017-01-05", "people": 145}, {"id": 6, "visit_date": "2017-01-06", "people": 1455}, {"id": 7, "visit_date": "2017-01-07", "people": 199}, {"id": 8, "visit_date": "2017-01-08", "people": 188}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["id", "visit_date", "people"], "rows": [[5, "2017-01-05", 145], [6, "2017-01-06", 1455], [7, "2017-01-07", 199], [8, "2017-01-08", 188]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **`LEAD`/`LAG` neighbors:** Attach the previous :** - **`LEAD`/`LAG` neighbors:** Attach the previous two and next two qualified IDs, then retain a row if it occupies any position in a consecutive triple. Effective for fixed run length three but less scalable.
- **Three-way self-join:** Match triples of high-attendance rows with IDs one apart and use `DISTINCT` to return all members. More expensive and verbose.
- **Recursive run tracking:** A recursive CTE can propagate run IDs, but row-number subtraction is simpler.
- **Filter after row numbering:** Incorrect: low-attendance rows would consume row numbers and could distort which qualified IDs form islands. The intended sequence is the filtered set.
- **Exactly two consecutive high rows:** Their count is two, so neither appears.
- **Exactly three:** All three receive count three and are returned.
- **Longer run:** Every row shares one label and is returned.
- **Low-attendance row inside numeric sequence:** It is filtered and creates an ID gap between remaining rows, splitting islands.
- **Date gap with consecutive IDs:** Does not break the run; only ID consecutiveness matters.
- **Order by ordinal:** `ORDER BY 1` means ascending ID. It relies on the schema guarantee that date increases with ID.
- **Threshold boundary:** `people = 100` qualifies because the comparison is inclusive.
- **No qualifying island:** The output is empty.
- **Unique dates:** The schema’s unique `visit_date` and monotonic relation make the final ordering deterministic.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n \log n)$. Let $n$ be the number of `Stadium` rows. The window row numbering requires rows ordered by ID; absent a reusable index order, sorting costs $O(n\log n)$. Partitioning/counting by `rk` may require additional hashing or sorting but remains within $O(n\log n)$ under a standard plan.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
