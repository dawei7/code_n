# Guided Example: Find Overlapping Shifts

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"EmployeeShifts": [{"employee_id": 1, "start_time": "08:00:00", "end_time": "12:00:00"}, {"employee_id": 1, "start_time": "11:00:00", "end_time": "15:00:00"}, {"employee_id": 1, "start_time": "14:00:00", "end_time": "18:00:00"}, {"employee_id": 2, "start_time": "09:00:00", "end_time": "17:00:00"}, {"employee_id": 2, "start_time": "16:00:00", "end_time": "20:00:00"}, {"employee_id": 3, "start_time": "10:00:00", "end_time": "12:00:00"}, {"employee_id": 3, "start_time": "13:00:00", "end_time": "15:00:00"}, {"employee_id": 3, "start_time": "16:00:00", "end_time": "18:00:00"}, {"employee_id": 4, "start_time": "08:00:00", "end_time": "10:00:00"}, {"employee_id": 4, "start_time": "09:00:00", "end_time": "11:00:00"}]}}`
- **Required output:** `{"columns": ["employee_id", "overlapping_shifts"], "rows": [[1, 2], [2, 1], [4, 1]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `EmployeeShifts`

The objective is to compute `{"columns": ["employee_id", "overlapping_shifts"], "rows": [[1, 2], [2, 1], [4, 1]]}` from `{"tables": {"EmployeeShifts": [{"employee_id": 1, "start_time": "08:00:00", "end_time": "12:00:00"}, {"employee_id": 1, "start_time": "11:00:00", "end_time": "15:00:00"}, {"employee_id": 1, "start_time": "14:00:00", "end_time": "18:00:00"}, {"employee_id": 2, "start_time": "09:00:00", "end_time": "17:00:00"}, {"employee_id": 2, "start_time": "16:00:00", "end_time": "20:00:00"}, {"employee_id": 3, "start_time": "10:00:00", "end_time": "12:00:00"}, {"employee_id": 3, "start_time": "13:00:00", "end_time": "15:00:00"}, {"employee_id": 3, "start_time": "16:00:00", "end_time": "18:00:00"}, {"employee_id": 4, "start_time": "08:00:00", "end_time": "10:00:00"}, {"employee_id": 4, "start_time": "09:00:00", "end_time": "11:00:00"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

The exact SQL solution pairs shifts belonging to the same employee. It orders each candidate pair by start time, then tests whether the earlier-starting shift is still active when the later shift begins.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"EmployeeShifts": [{"employee_id": 1, "start_time": "08:00:00", "end_time": "12:00:00"}, {"employee_id": 1, "start_time": "11:00:00", "end_time": "15:00:00"}, {"employee_id": 1, "start_time": "14:00:00", "end_time": "18:00:00"}, {"employee_id": 2, "start_time": "09:00:00", "end_time": "17:00:00"}, {"employee_id": 2, "start_time": "16:00:00", "end_time": "20:00:00"}, {"employee_id": 3, "start_time": "10:00:00", "end_time": "12:00:00"}, {"employee_id": 3, "start_time": "13:00:00", "end_time": "15:00:00"}, {"employee_id": 3, "start_time": "16:00:00", "end_time": "18:00:00"}, {"employee_id": 4, "start_time": "08:00:00", "end_time": "10:00:00"}, {"employee_id": 4, "start_time": "09:00:00", "end_time": "11:00:00"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

Aliases `t1` and `t2` both refer to `EmployeeShifts`. The first join condition,

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Aliases `t1` and `t2` both refer to `EmployeeShifts`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

prevents shifts from different employees from being compared. Overlap counts are independent per employee.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["employee_id", "overlapping_shifts"], "rows": [[1, 2], [2, 1], [4, 1]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"EmployeeShifts": [{"employee_id": 1, "start_time": "08:00:00", "end_time": "12:00:00"}, {"employee_id": 1, "start_time": "11:00:00", "end_time": "15:00:00"}, {"employee_id": 1, "start_time": "14:00:00", "end_time": "18:00:00"}, {"employee_id": 2, "start_time": "09:00:00", "end_time": "17:00:00"}, {"employee_id": 2, "start_time": "16:00:00", "end_time": "20:00:00"}, {"employee_id": 3, "start_time": "10:00:00", "end_time": "12:00:00"}, {"employee_id": 3, "start_time": "13:00:00", "end_time": "15:00:00"}, {"employee_id": 3, "start_time": "16:00:00", "end_time": "18:00:00"}, {"employee_id": 4, "start_time": "08:00:00", "end_time": "10:00:00"}, {"employee_id": 4, "start_time": "09:00:00", "end_time": "11:00:00"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["employee_id", "overlapping_shifts"], "rows": [[1, 2], [2, 1], [4, 1]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Sweep line by employee:** Sort start and end e:** - **Sweep line by employee:** Sort start and end events, count active earlier shifts at each start, and sum those active counts. This achieves $O(m\log m)$ time and matches the manifest summary, but it is not the exact SQL shown.
- **Window plus event expansion:** SQL can union start and end events and use window sums, with careful tie ordering so ends at a start time are processed first for strict overlap.
- **Correlated subquery:** Counting later starts inside each shift gives similar pair logic but may be less transparent and still quadratic without strong indexing.
- **Touching shifts:** `end_time = start_time` is excluded by strict `>`.
- **Nested shifts:** An outer shift overlaps every inner shift whose start occurs before its end, and each pair is counted once.
- **Three-way overlap:** The result counts three pairs, not one overlap episode.
- **No overlaps:** The employee has no joined rows and is omitted from output.
- **One shift:** It cannot form a pair and is omitted.
- **Equal starts:** The unique key rules them out for one employee; otherwise strict start ordering would fail to count such overlapping pairs.
- **Different employees:** They never join even when their times coincide.
- **Overnight shifts:** A time-only interval with end earlier than start is not handled as crossing midnight. The intended data must describe shifts within one date consistently.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(m^2)$. Let $m$ be the total number of shifts and let $P$ be the number of overlapping pairs emitted by the join. A naive self-join examines $O(m^2)$ pairs in the worst case. Indexes on `employee_id` and `start_time` can reduce candidate lookup, but when one employee has many mutually overlapping shifts, $P=\Theta(m^2)$ output join rows still exist before aggregation.
- **Auxiliary Space Complexity:** $O(P)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
