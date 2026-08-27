# Guided Example: Consecutive Available Seats II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Cinema": [{"seat_id": 1, "free": 1}, {"seat_id": 2, "free": 0}, {"seat_id": 3, "free": 1}, {"seat_id": 4, "free": 1}, {"seat_id": 5, "free": 1}]}}`
- **Required output:** `{"columns": ["first_seat_id", "last_seat_id", "consecutive_seats_len"], "rows": [[3, 5, 3]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Cinema`

The objective is to compute `{"columns": ["first_seat_id", "last_seat_id", "consecutive_seats_len"], "rows": [[3, 5, 3]]}` from `{"tables": {"Cinema": [{"seat_id": 1, "free": 1}, {"seat_id": 2, "free": 0}, {"seat_id": 3, "free": 1}, {"seat_id": 4, "free": 1}, {"seat_id": 5, "free": 1}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Filter to available seats, then identify consecutive islands

Only rows with `free = 1` can belong to an available-seat sequence, so CTE `T` filters occupied seats first.

Among the remaining rows, seats are ordered by `seat_id`. Because `seat_id` is an auto-increment identifier and therefore unique, `RANK() OVER (ORDER BY seat_id)` produces consecutive ranks 1, 2, 3, and so on. In this query, `RANK` behaves exactly like `ROW_NUMBER` because ties cannot occur.

For a consecutive run of seat identifiers, both `seat_id` and its rank increase by one from row to row. Their difference remains constant:

$$
\texttt{gid}=\texttt{seat_id}-\operatorname{rank}.
$$

For example, available seats 3, 4, and 5 may receive ranks 2, 3, and 4 after an earlier available seat 1. Their differences are all 1. If the next available seat is 8 with rank 5, its difference is 3, so it begins a new group.

This “value minus consecutive row number” pattern converts every island of consecutive integers into one group key.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Cinema": [{"seat_id": 1, "free": 1}, {"seat_id": 2, "free": 0}, {"seat_id": 3, "free": 1}, {"seat_id": 4, "free": 1}, {"seat_id": 5, "free": 1}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Aggregate each island

CTE `P` groups the rows by `gid`. Within each group:

- `MIN(seat_id)` is the first seat;
- `MAX(seat_id)` is the last seat;
- `COUNT(1)` is the consecutive run length.

The grouping is valid in both directions. Consecutive available identifiers keep the same difference. If two available identifiers have a gap greater than one, `seat_id` jumps by more than rank does, so the difference changes. Therefore, a group contains exactly one maximal consecutive available sequence.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | CTE `P` groups the rows by `gid`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Select every longest sequence

Within the grouped runs, the query computes

`RANK() OVER (ORDER BY COUNT(1) DESC) AS rk`.

The longest length sorts first and receives rank 1. If several runs have that same maximum length, `RANK` assigns rank 1 to all of them. The outer `WHERE rk = 1` therefore returns every tied longest sequence.

Finally, `ORDER BY 1` orders by the first selected column, `first_seat_id`, in ascending order as required.

The local description contains two lines that appear inconsistent: it says there is at most one longest sequence, then says to include all sequences when lengths tie. The exact query robustly follows the latter rule and returns all ties. If the uniqueness guarantee always holds, the tie support simply has no visible effect.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["first_seat_id", "last_seat_id", "consecutive_seats_len"], "rows": [[3, 5, 3]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Cinema": [{"seat_id": 1, "free": 1}, {"seat_id": 2, "free": 0}, {"seat_id": 3, "free": 1}, {"seat_id": 4, "free": 1}, {"seat_id": 5, "free": 1}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["first_seat_id", "last_seat_id", "consecutive_seats_len"], "rows": [[3, 5, 3]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **`LAG` break detection:** Compare each free `se:** - **`LAG` break detection:** Compare each free `seat_id` with the previous one, mark a new group when the difference is not 1, and use a cumulative sum of break flags. This is explicit but uses another window layer.
- **Recursive traversal:** Follow seat identifiers one by one and build runs. It is more complicated and usually less optimizer-friendly.
- **Self-join run starts and ends:** Detect free seats without free predecessors or successors, then pair boundaries. Correct pairing can become cumbersome.
- **`ROW_NUMBER` instead of `RANK` in T:** Because `seat_id` is unique, it produces identical group identifiers and communicates the intent more directly.
- **Tied longest runs:** The second `RANK` deliberately returns all ties. Replacing it with `ROW_NUMBER` would incorrectly keep only one.
- **Single free seat:** It forms a run with identical first and last IDs and length 1.
- **All seats free and consecutive:** All rows have one `gid` and form one group.
- **Occupied gap:** Filtering does not merge across it because the numeric `seat_id` jump changes `gid`.
- **Missing numeric IDs:** Even if an identifier is absent rather than occupied, the gap also breaks consecutiveness, as the definition is based on consecutive seat IDs.
- **No free seats:** Both CTEs produce no groups and the result is empty. The statement does not specify a synthetic zero-length row.
- **Ordering ties:** `ORDER BY 1` is positional SQL syntax for ascending `first_seat_id` and ensures deterministic required order.
- **Unique identifier assumption:** If duplicate `seat_id` values were allowed, `RANK` gaps could distort `gid`. The auto-increment contract rules duplicates out.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n log n)$. Let $r$ be the total number of rows in `Cinema` and $f$ the number of free-seat rows.
- **Auxiliary Space Complexity:** $O(f)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
