# Guided Example: Restaurant Growth

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Customer": [{"customer_id": 1, "name": "Jhon", "visited_on": "2019-01-01", "amount": 100}, {"customer_id": 2, "name": "Daniel", "visited_on": "2019-01-02", "amount": 110}, {"customer_id": 3, "name": "Jade", "visited_on": "2019-01-03", "amount": 120}, {"customer_id": 4, "name": "Khaled", "visited_on": "2019-01-04", "amount": 130}, {"customer_id": 5, "name": "Winston", "visited_on": "2019-01-05", "amount": 110}, {"customer_id": 6, "name": "Elvis", "visited_on": "2019-01-06", "amount": 140}, {"customer_id": 7, "name": "Anna", "visited_on": "2019-01-07", "amount": 150}, {"customer_id": 8, "name": "Maria", "visited_on": "2019-01-08", "amount": 80}, {"customer_id": 9, "name": "Jaze", "visited_on": "2019-01-09", "amount": 110}, {"customer_id": 1, "name": "Jhon", "visited_on": "2019-01-10", "amount": 130}, {"customer_id": 3, "name": "Jade", "visited_on": "2019-01-10", "amount": 150}]}}`
- **Required output:** `{"columns": ["visited_on", "amount", "average_amount"], "rows": [["2019-01-07", 860, 122.86], ["2019-01-08", 840, 120], ["2019-01-09", 840, 120], ["2019-01-10", 1000, 142.86]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Customer`

The objective is to compute `{"columns": ["visited_on", "amount", "average_amount"], "rows": [["2019-01-07", 860, 122.86], ["2019-01-08", 840, 120], ["2019-01-09", 840, 120], ["2019-01-10", 1000, 142.86]]}` from `{"tables": {"Customer": [{"customer_id": 1, "name": "Jhon", "visited_on": "2019-01-01", "amount": 100}, {"customer_id": 2, "name": "Daniel", "visited_on": "2019-01-02", "amount": 110}, {"customer_id": 3, "name": "Jade", "visited_on": "2019-01-03", "amount": 120}, {"customer_id": 4, "name": "Khaled", "visited_on": "2019-01-04", "amount": 130}, {"customer_id": 5, "name": "Winston", "visited_on": "2019-01-05", "amount": 110}, {"customer_id": 6, "name": "Elvis", "visited_on": "2019-01-06", "amount": 140}, {"customer_id": 7, "name": "Anna", "visited_on": "2019-01-07", "amount": 150}, {"customer_id": 8, "name": "Maria", "visited_on": "2019-01-08", "amount": 80}, {"customer_id": 9, "name": "Jaze", "visited_on": "2019-01-09", "amount": 110}, {"customer_id": 1, "name": "Jhon", "visited_on": "2019-01-10", "amount": 130}, {"customer_id": 3, "name": "Jade", "visited_on": "2019-01-10", "amount": 150}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Creating one row per day

The innermost derived table performs:

`SELECT visited_on, SUM(amount) AS amount FROM Customer GROUP BY visited_on`.

Every customer payment on one date contributes to the same daily total. This is essential for dates such as 2019-01-10 in the example, where two customers paid $130$ and $150$. The daily row must contain $280$ before the moving window is calculated.

If the window operated directly on customer rows, “six preceding rows” would mean six transactions rather than six days and would give incorrect results whenever a day had multiple customers.

The statement guarantees at least one customer every day. After daily grouping, adjacent rows in date order therefore represent adjacent calendar dates. This guarantee is what makes a seven-row frame equivalent to a seven-day frame.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Customer": [{"customer_id": 1, "name": "Jhon", "visited_on": "2019-01-01", "amount": 100}, {"customer_id": 2, "name": "Daniel", "visited_on": "2019-01-02", "amount": 110}, {"customer_id": 3, "name": "Jade", "visited_on": "2019-01-03", "amount": 120}, {"customer_id": 4, "name": "Khaled", "visited_on": "2019-01-04", "amount": 130}, {"customer_id": 5, "name": "Winston", "visited_on": "2019-01-05", "amount": 110}, {"customer_id": 6, "name": "Elvis", "visited_on": "2019-01-06", "amount": 140}, {"customer_id": 7, "name": "Anna", "visited_on": "2019-01-07", "amount": 150}, {"customer_id": 8, "name": "Maria", "visited_on": "2019-01-08", "amount": 80}, {"customer_id": 9, "name": "Jaze", "visited_on": "2019-01-09", "amount": 110}, {"customer_id": 1, "name": "Jhon", "visited_on": "2019-01-10", "amount": 130}, {"customer_id": 3, "name": "Jade", "visited_on": "2019-01-10", "amount": 150}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Computing the seven-row sum

The CTE `t` applies:

`SUM(amount) OVER (ORDER BY visited_on ROWS 6 PRECEDING)`.

`ROWS 6 PRECEDING` is shorthand for a frame beginning six rows before the current row and ending at the current row. Once enough dates exist, it contains seven daily rows:

$$
\text{current day}+\text{six preceding days}.
$$

For the first date, the frame contains only one row. For the second, it contains two. The seventh date is the first whose frame contains all seven required daily totals.

The resulting rolling total is also aliased `amount`. Inside `t`, that name now refers to the window sum rather than the one-day sum from the derived table.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Numbering dates to remove incomplete windows

The query also computes:

`RANK() OVER (ORDER BY visited_on ROWS 6 PRECEDING) AS rk`.

Ranking functions are based on the window order and do not meaningfully use the frame bounds. After grouping, `visited_on` is unique, so `RANK` produces $1,2,3,\ldots$ without gaps.

The outer `WHERE rk > 6` removes ranks one through six. Every surviving row has at least six earlier daily rows and therefore a complete seven-day window.

`ROW_NUMBER() OVER (ORDER BY visited_on)` would state the intended numbering more directly. With unique dates, it gives the same values as `RANK`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["visited_on", "amount", "average_amount"], "rows": [["2019-01-07", 860, 122.86], ["2019-01-08", 840, 120], ["2019-01-09", 840, 120], ["2019-01-10", 1000, 142.86]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Customer": [{"customer_id": 1, "name": "Jhon", "visited_on": "2019-01-01", "amount": 100}, {"customer_id": 2, "name": "Daniel", "visited_on": "2019-01-02", "amount": 110}, {"customer_id": 3, "name": "Jade", "visited_on": "2019-01-03", "amount": 120}, {"customer_id": 4, "name": "Khaled", "visited_on": "2019-01-04", "amount": 130}, {"customer_id": 5, "name": "Winston", "visited_on": "2019-01-05", "amount": 110}, {"customer_id": 6, "name": "Elvis", "visited_on": "2019-01-06", "amount": 140}, {"customer_id": 7, "name": "Anna", "visited_on": "2019-01-07", "amount": 150}, {"customer_id": 8, "name": "Maria", "visited_on": "2019-01-08", "amount": 80}, {"customer_id": 9, "name": "Jaze", "visited_on": "2019-01-09", "amount": 110}, {"customer_id": 1, "name": "Jhon", "visited_on": "2019-01-10", "amount": 130}, {"customer_id": 3, "name": "Jade", "visited_on": "2019-01-10", "amount": 150}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["visited_on", "amount", "average_amount"], "rows": [["2019-01-07", 860, 122.86], ["2019-01-08", 840, 120], ["2019-01-09", 840, 120], ["2019-01-10", 1000, 142.86]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Self-join date ranges:** Join each date to transactions in the previous six days and group. It is direct but can create a much larger intermediate relation.
- **Correlated subquery:** Sum a seven-day range separately for each date. Indexes may help, but repeated range work is less elegant than one window pass.
- **`RANGE INTERVAL 6 DAY` frame:** A date-based frame can handle missing calendar days more explicitly, though MySQL syntax and exact requirements must be considered.
- **`ROW_NUMBER` instead of `RANK`:** Dates are unique after grouping, so both number rows identically; `ROW_NUMBER` communicates the filtering purpose better.
- **Several customers on one day:** The inner aggregation must combine them before the seven-row frame.
- **Continuous-day guarantee:** It is what makes seven rows equal seven calendar days. Without it, the exact query could span more than seven days.
- **First six dates:** Their frames are incomplete and are correctly removed.
- **Exactly seven dates:** The result contains one row for the seventh date.
- **Rounding:** The total is divided by seven before rounding, preserving the requested two-decimal average.
- **Required output order:** The exact source needs an outer `ORDER BY visited_on`; window-local order is insufficient.
- **Window frame on `RANK`:** The frame clause does not change ranking and is unnecessary.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(d)$. Let $r$ be the number of customer transaction rows and $d$ the number of distinct dates.
- **Auxiliary Space Complexity:** $O(d)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
