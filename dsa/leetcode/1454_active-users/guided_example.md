# Guided Example: Active Users

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Accounts": [{"id": 1, "name": "Winston"}, {"id": 7, "name": "Jonathan"}], "Logins": [{"id": 7, "login_date": "2020-05-30"}, {"id": 1, "login_date": "2020-05-30"}, {"id": 7, "login_date": "2020-05-31"}, {"id": 7, "login_date": "2020-06-01"}, {"id": 7, "login_date": "2020-06-02"}, {"id": 7, "login_date": "2020-06-02"}, {"id": 7, "login_date": "2020-06-03"}, {"id": 1, "login_date": "2020-06-07"}, {"id": 7, "login_date": "2020-06-10"}]}}`
- **Required output:** `{"columns": ["id", "name"], "rows": [[7, "Jonathan"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Accounts`

The objective is to compute `{"columns": ["id", "name"], "rows": [[7, "Jonathan"]]}` from `{"tables": {"Accounts": [{"id": 1, "name": "Winston"}, {"id": 7, "name": "Jonathan"}], "Logins": [{"id": 7, "login_date": "2020-05-30"}, {"id": 1, "login_date": "2020-05-30"}, {"id": 7, "login_date": "2020-05-31"}, {"id": 7, "login_date": "2020-06-01"}, {"id": 7, "login_date": "2020-06-02"}, {"id": 7, "login_date": "2020-06-02"}, {"id": 7, "login_date": "2020-06-03"}, {"id": 1, "login_date": "2020-06-07"}, {"id": 7, "login_date": "2020-06-10"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**First reduce login events to login days.** A user may log in multiple times on the same date, but consecutive activity is measured in distinct calendar days. Counting raw rows could falsely turn several same-day events into a five-day streak.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Accounts": [{"id": 1, "name": "Winston"}, {"id": 7, "name": "Jonathan"}], "Logins": [{"id": 7, "login_date": "2020-05-30"}, {"id": 1, "login_date": "2020-05-30"}, {"id": 7, "login_date": "2020-05-31"}, {"id": 7, "login_date": "2020-06-01"}, {"id": 7, "login_date": "2020-06-02"}, {"id": 7, "login_date": "2020-06-02"}, {"id": 7, "login_date": "2020-06-03"}, {"id": 1, "login_date": "2020-06-07"}, {"id": 7, "login_date": "2020-06-10"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The first common table expression, `T`, joins `Logins` with `Accounts` through their shared `id` and applies `SELECT DISTINCT *`. The join attaches the account name to each login. Because `Accounts.id` is a primary key, one login ID matches at most one name. `DISTINCT` then collapses duplicate joined rows for the same account and date.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

After `T`, each user-date combination appears once. This makes a later `COUNT(*)` count calendar days rather than login events. Joining early also carries `name` into the later rows so the final result can return it.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["id", "name"], "rows": [[7, "Jonathan"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Accounts": [{"id": 1, "name": "Winston"}, {"id": 7, "name": "Jonathan"}], "Logins": [{"id": 7, "login_date": "2020-05-30"}, {"id": 1, "login_date": "2020-05-30"}, {"id": 7, "login_date": "2020-05-31"}, {"id": 7, "login_date": "2020-06-01"}, {"id": 7, "login_date": "2020-06-02"}, {"id": 7, "login_date": "2020-06-02"}, {"id": 7, "login_date": "2020-06-03"}, {"id": 1, "login_date": "2020-06-07"}, {"id": 7, "login_date": "2020-06-10"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["id", "name"], "rows": [[7, "Jonathan"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **LAG plus break markers:** Compare each date with the previous date, mark the start of a new streak, take a cumulative sum of breaks, and group by that island number. It is more verbose but expresses gaps explicitly.
- **Self-join five dates:** Join each distinct login date to dates one through four days later for the same ID. This can solve a fixed threshold but becomes cumbersome and duplicates work; the row-number key generalizes cleanly.
- **Correlated existence checks:** Test whether four required following dates exist for each date. Indexes can help, but the logic repeats lookups and is less convenient for a variable threshold.
- **Count raw login rows:** This is wrong because multiple logins on one day do not represent consecutive days. Deduplication must happen first.
- **Group only by g:** Different users can share the same shifted date. `id` must remain part of the grouping key.
- **Omit final DISTINCT:** A user with two separate qualifying streaks would appear twice. The result requires one account row.
- **Exactly five consecutive days:** The streak group count is five and passes the inclusive `>= 5` test.
- **Longer streak:** All of its dates share one key, and its larger count also passes.
- **Duplicate logins on a streak day:** `T` collapses them, so they neither inflate the length nor break the sequence.
- **Several separated streaks:** Different gaps create different `g` values. Any qualifying group makes the user active.
- **Five total days with gaps:** They form multiple smaller groups and do not pass merely because their total count is five.
- **Month boundary:** Calendar subtraction keeps adjacent dates in the same island.
- **Year boundary and leap day:** SQL date arithmetic handles actual consecutive calendar days across these boundaries.
- **Account with no login:** It has no row in `T` and cannot appear in the active result.
- **Login ID without an account outside the contract:** The inner join would discard it because no name can be returned. The expected relational data associates login IDs with accounts.
- **Same name for different IDs:** Grouping and identity use `id`, so two accounts may share a display name without being merged.
- **General threshold n:** Replace five in `HAVING` with the desired threshold; duplicate removal and island construction remain identical.
- **Ordered output:** `ORDER BY 1` refers to selected `id`. Writing `ORDER BY id` would be equivalent and more explicit.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(L\log L+A)$. Let `A` be the number of account rows and `L` the number of distinct `id, login_date` pairs after duplicate removal. Joining accounts to logins and deduplicating requires reading the relevant rows; with suitable keys, this contributes roughly `O(A + L)` plus the work needed to eliminate raw duplicates.
- **Auxiliary Space Complexity:** $O(L)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
