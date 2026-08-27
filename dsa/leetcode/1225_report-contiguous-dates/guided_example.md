# Guided Example: Report Contiguous Dates

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Failed": [{"fail_date": "2018-12-28"}, {"fail_date": "2018-12-29"}, {"fail_date": "2019-01-04"}, {"fail_date": "2019-01-05"}], "Succeeded": [{"success_date": "2018-12-30"}, {"success_date": "2018-12-31"}, {"success_date": "2019-01-01"}, {"success_date": "2019-01-02"}, {"success_date": "2019-01-03"}, {"success_date": "2019-01-06"}]}}`
- **Required output:** `{"columns": ["period_state", "start_date", "end_date"], "rows": [["succeeded", "2019-01-01", "2019-01-03"], ["failed", "2019-01-04", "2019-01-05"], ["succeeded", "2019-01-06", "2019-01-06"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Failed`

The objective is to compute `{"columns": ["period_state", "start_date", "end_date"], "rows": [["succeeded", "2019-01-01", "2019-01-03"], ["failed", "2019-01-04", "2019-01-05"], ["succeeded", "2019-01-06", "2019-01-06"]]}` from `{"tables": {"Failed": [{"fail_date": "2018-12-28"}, {"fail_date": "2018-12-29"}, {"fail_date": "2019-01-04"}, {"fail_date": "2019-01-05"}], "Succeeded": [{"success_date": "2018-12-30"}, {"success_date": "2018-12-31"}, {"success_date": "2019-01-01"}, {"success_date": "2019-01-02"}, {"success_date": "2019-01-03"}, {"success_date": "2019-01-06"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Normalize two outcome tables into one timeline

The input stores failed dates and succeeded dates in separate tables, but the output needs one chronological sequence of state intervals. The common table expression `T` converts both sources to the same two-column shape:

- `dt` is the task date;
- `st` is the literal state, either `'failed'` or `'succeeded'`.

Each branch filters with `YEAR(...)=2019` before combining the rows. Dates from 2018 or another year therefore cannot influence ranks, groups, or output endpoints.

`UNION ALL` retains every selected row without paying for duplicate elimination. Each source date is a primary key, and the problem states that one task runs per day, so a valid dataset assigns a day one state rather than presenting duplicate same-state rows. Under that contract, deduplication is unnecessary.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Failed": [{"fail_date": "2018-12-28"}, {"fail_date": "2018-12-29"}, {"fail_date": "2019-01-04"}, {"fail_date": "2019-01-05"}], "Succeeded": [{"success_date": "2018-12-30"}, {"success_date": "2018-12-31"}, {"success_date": "2019-01-01"}, {"success_date": "2019-01-02"}, {"success_date": "2019-01-03"}, {"success_date": "2019-01-06"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: The gaps-and-islands idea

The desired output is a set of maximal “islands” of consecutive dates with the same state. The central challenge is to create a group key that stays constant while dates are consecutive and changes after a gap.

Within each state, the query assigns dates a rank in increasing order:

`RANK() OVER (PARTITION BY st ORDER BY dt)`.

Partitioning by `st` means failed dates are ranked independently from succeeded dates. Because dates within each source are unique, `RANK` produces consecutive integers \(1,2,3,\ldots\), behaving the same as `ROW_NUMBER` here.

The query subtracts that integer number of days from each date:

`SUBDATE(dt, rank) AS pt`.

Suppose failed dates are January 4 and January 5. Their ranks among failed dates are one and two. Subtracting gives January 3 for both:

\[
\text{Jan 4}-1\text{ day}=\text{Jan 3},
\qquad
\text{Jan 5}-2\text{ days}=\text{Jan 3}.
\]

The shifted date `pt` is constant because both the real date and rank advance by one across consecutive rows.

Now suppose the next failed date is January 9, after successful days create a gap. Its failed-state rank may be three, but January 9 minus three days is January 6, not January 3. The key changes, starting a new failed island.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The desired output is a set of maximal “islands” of consecut... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why state must be part of the group

The derived `pt` alone is not globally unique. A failed island and a succeeded island could coincidentally produce the same shifted date. The outer query therefore groups by both `st` and `pt` using `GROUP BY 1, pt`, where ordinal one refers to the first selected grouping expression, `st`.

Within one such group, every row has the same state and belongs to one consecutive run. `MIN(dt)` is its first date and `MAX(dt)` is its last date. The aliases produce exactly the requested columns:

- `st AS period_state`;
- `MIN(dt) AS start_date`;
- `MAX(dt) AS end_date`.

A one-day island contains one row, so its minimum and maximum are naturally the same date.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["period_state", "start_date", "end_date"], "rows": [["succeeded", "2019-01-01", "2019-01-03"], ["failed", "2019-01-04", "2019-01-05"], ["succeeded", "2019-01-06", "2019-01-06"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Failed": [{"fail_date": "2018-12-28"}, {"fail_date": "2018-12-29"}, {"fail_date": "2019-01-04"}, {"fail_date": "2019-01-05"}], "Succeeded": [{"success_date": "2018-12-30"}, {"success_date": "2018-12-31"}, {"success_date": "2019-01-01"}, {"success_date": "2019-01-02"}, {"success_date": "2019-01-03"}, {"success_date": "2019-01-06"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["period_state", "start_date", "end_date"], "rows": [["succeeded", "2019-01-01", "2019-01-03"], ["failed", "2019-01-04", "2019-01-05"], ["succeeded", "2019-01-06", "2019-01-06"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **`LAG` plus cumulative group numbers:** Compare:** - **`LAG` plus cumulative group numbers:** Compare each date with the previous date and state, mark every break, and cumulatively sum break flags. This is explicit and flexible but needs multiple window stages.
- **Recursive calendar generation:** Generate every 2019 date and join outcomes before grouping runs. It can work, but it processes the entire calendar and is more elaborate than ranking existing daily rows.
- **`UNION` instead of `UNION ALL`:** It would perform unnecessary duplicate elimination under the one-task-per-day and primary-key guarantees.
- **`ROW_NUMBER` instead of `RANK`:** The two are equivalent here because each state’s dates are unique. If duplicates were allowed, `RANK` gaps could break the shifted-key property.
- **Dates outside 2019:** They are filtered before ranking, so they cannot shift rank values or extend an interval across the reporting boundary.
- **One-day period:** `MIN(dt)` and `MAX(dt)` return the same date, as required.
- **Alternating outcomes every day:** Each date becomes its own island because consecutive rows of the same state are separated by a calendar gap.
- **One state for all reported days:** All rows share one state and consecutive shifted key, producing one interval.
- **Empty 2019 input:** The CTE has no rows and the query returns no intervals. The stated system model normally supplies one task every day.
- **Dialect dependence:** `YEAR` and integer-form `SUBDATE` are MySQL syntax. Other engines need equivalent date extraction and date arithmetic.
- **Ordinal grouping and ordering:** `GROUP BY 1` means the first selected grouping column and `ORDER BY 2` means `start_date`. Reordering the select list without updating ordinals would change behavior.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(d\log d)$. Let \(d\) be the total number of 2019 rows from both tables. Filtering and combining rows is linear in the rows examined, subject to database indexing and optimization. The window function must order dates within each state, and the grouping and final ordering may also require sorting or hashing. A conventional upper bound for this plan is \(O(d\log d)\) time.
- **Auxiliary Space Complexity:** $O(d)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
