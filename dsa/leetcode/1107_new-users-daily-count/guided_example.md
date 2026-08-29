# Guided Example: New Users Daily Count

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Traffic": [{"user_id": 1, "activity": "login", "activity_date": "2019-05-01"}, {"user_id": 1, "activity": "homepage", "activity_date": "2019-05-01"}, {"user_id": 1, "activity": "logout", "activity_date": "2019-05-01"}, {"user_id": 2, "activity": "login", "activity_date": "2019-06-21"}, {"user_id": 2, "activity": "logout", "activity_date": "2019-06-21"}, {"user_id": 3, "activity": "login", "activity_date": "2019-01-01"}, {"user_id": 3, "activity": "jobs", "activity_date": "2019-01-01"}, {"user_id": 3, "activity": "logout", "activity_date": "2019-01-01"}, {"user_id": 4, "activity": "login", "activity_date": "2019-06-21"}, {"user_id": 4, "activity": "groups", "activity_date": "2019-06-21"}, {"user_id": 4, "activity": "logout", "activity_date": "2019-06-21"}, {"user_id": 5, "activity": "login", "activity_date": "2019-03-01"}, {"user_id": 5, "activity": "logout", "activity_date": "2019-03-01"}, {"user_id": 5, "activity": "login", "activity_date": "2019-06-21"}, {"user_id": 5, "activity": "logout", "activity_date": "2019-06-21"}]}}`
- **Required output:** `{"columns": ["login_date", "user_count"], "rows": [["2019-05-01", 1], ["2019-06-21", 2]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Traffic`

The objective is to compute `{"columns": ["login_date", "user_count"], "rows": [["2019-05-01", 1], ["2019-06-21", 2]]}` from `{"tables": {"Traffic": [{"user_id": 1, "activity": "login", "activity_date": "2019-05-01"}, {"user_id": 1, "activity": "homepage", "activity_date": "2019-05-01"}, {"user_id": 1, "activity": "logout", "activity_date": "2019-05-01"}, {"user_id": 2, "activity": "login", "activity_date": "2019-06-21"}, {"user_id": 2, "activity": "logout", "activity_date": "2019-06-21"}, {"user_id": 3, "activity": "login", "activity_date": "2019-01-01"}, {"user_id": 3, "activity": "jobs", "activity_date": "2019-01-01"}, {"user_id": 3, "activity": "logout", "activity_date": "2019-01-01"}, {"user_id": 4, "activity": "login", "activity_date": "2019-06-21"}, {"user_id": 4, "activity": "groups", "activity_date": "2019-06-21"}, {"user_id": 4, "activity": "logout", "activity_date": "2019-06-21"}, {"user_id": 5, "activity": "login", "activity_date": "2019-03-01"}, {"user_id": 5, "activity": "logout", "activity_date": "2019-03-01"}, {"user_id": 5, "activity": "login", "activity_date": "2019-06-21"}, {"user_id": 5, "activity": "logout", "activity_date": "2019-06-21"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Discard non-login activity before finding first login

Install or new-user status depends only on login rows. The CTE first applies `WHERE activity = 'login'`, so homepage, logout, jobs, and groups events cannot become a user’s first login.

For each remaining row, `MIN(activity_date) OVER (PARTITION BY user_id)` computes the earliest login date across that user’s complete login history. A window function preserves every login row while attaching the same `login_date` to all of them.

This order is essential. Filtering the final date range before computing the minimum would incorrectly classify a returning user as new if their real first login occurred earlier than the reporting window.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Traffic": [{"user_id": 1, "activity": "login", "activity_date": "2019-05-01"}, {"user_id": 1, "activity": "homepage", "activity_date": "2019-05-01"}, {"user_id": 1, "activity": "logout", "activity_date": "2019-05-01"}, {"user_id": 2, "activity": "login", "activity_date": "2019-06-21"}, {"user_id": 2, "activity": "logout", "activity_date": "2019-06-21"}, {"user_id": 3, "activity": "login", "activity_date": "2019-01-01"}, {"user_id": 3, "activity": "jobs", "activity_date": "2019-01-01"}, {"user_id": 3, "activity": "logout", "activity_date": "2019-01-01"}, {"user_id": 4, "activity": "login", "activity_date": "2019-06-21"}, {"user_id": 4, "activity": "groups", "activity_date": "2019-06-21"}, {"user_id": 4, "activity": "logout", "activity_date": "2019-06-21"}, {"user_id": 5, "activity": "login", "activity_date": "2019-03-01"}, {"user_id": 5, "activity": "logout", "activity_date": "2019-03-01"}, {"user_id": 5, "activity": "login", "activity_date": "2019-06-21"}, {"user_id": 5, "activity": "logout", "activity_date": "2019-06-21"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Collapse repeated rows and later logins by distinct user

The CTE may contain several rows for one user: later login dates, repeated login records, or exact duplicates are all permitted by the table. In the outer grouping, `COUNT(DISTINCT user_id)` ensures that the user contributes once to the cohort identified by their true first-login date.

`GROUP BY 1` groups by the first selected expression, `login_date`. Each produced row therefore represents one date with at least one qualifying user. Dates with zero users never form a group, as required.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Apply the exact protected date predicate

`DATEDIFF('2019-06-30', login_date)` measures how many calendar days the first login precedes the assumed current date. The query retains values no greater than 90. First login on June 30 has difference zero and qualifies; April 1 has difference 90 and also qualifies; March 31 has difference 91 and is excluded.

However, the exact predicate has no lower bound. A future login produces a negative difference, and every negative number is also `<= 90`. Therefore, the protected query assumes no future first-login dates, or else it would include them.

The local Reference contract explicitly defines the closed interval April 1 through June 30 and says future dates do not qualify. To implement that broader contract independently of source-data assumptions, the outer filter must require the difference to be between zero and ninety inclusive.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["login_date", "user_count"], "rows": [["2019-05-01", 1], ["2019-06-21", 2]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Traffic": [{"user_id": 1, "activity": "login", "activity_date": "2019-05-01"}, {"user_id": 1, "activity": "homepage", "activity_date": "2019-05-01"}, {"user_id": 1, "activity": "logout", "activity_date": "2019-05-01"}, {"user_id": 2, "activity": "login", "activity_date": "2019-06-21"}, {"user_id": 2, "activity": "logout", "activity_date": "2019-06-21"}, {"user_id": 3, "activity": "login", "activity_date": "2019-01-01"}, {"user_id": 3, "activity": "jobs", "activity_date": "2019-01-01"}, {"user_id": 3, "activity": "logout", "activity_date": "2019-01-01"}, {"user_id": 4, "activity": "login", "activity_date": "2019-06-21"}, {"user_id": 4, "activity": "groups", "activity_date": "2019-06-21"}, {"user_id": 4, "activity": "logout", "activity_date": "2019-06-21"}, {"user_id": 5, "activity": "login", "activity_date": "2019-03-01"}, {"user_id": 5, "activity": "logout", "activity_date": "2019-03-01"}, {"user_id": 5, "activity": "login", "activity_date": "2019-06-21"}, {"user_id": 5, "activity": "logout", "activity_date": "2019-06-21"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["login_date", "user_count"], "rows": [["2019-05-01", 1], ["2019-06-21", 2]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Grouped CTE:** Select `user_id, MIN(activity_date)` from login rows grouped by user, then filter and group those one-row-per-user results. This eliminates the need for outer `DISTINCT` and aligns directly with $O(U)$ intermediate state.
- **Correlated minimum:** Test each login against the minimum for its user. It is correct with proper indexing but usually less clear than a grouped or window calculation.
- **Filter date before minimum:** Incorrect because it can hide an older first login and count an existing user as new.
- **Duplicate login rows:** Window output repeats them, but `COUNT(DISTINCT user_id)` prevents inflated counts.
- **Several later logins:** They carry the same first date and still count the user once.
- **No login activity:** A user with only other activity is absent from the CTE and is not counted.
- **April 1, 2019:** Difference is exactly 90, so it qualifies.
- **March 31, 2019:** Difference is 91, so it is excluded.
- **June 30, 2019:** Difference is zero, so it qualifies.
- **Future first login:** The exact query incorrectly admits it unless the source guarantees no future dates; adding a nonnegative condition fixes this.
- **Dates with zero users:** SQL grouping emits no synthetic rows, matching the requirement to omit them.
- **Any result order:** The missing `ORDER BY` is intentional and valid.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \log N)$. Let $N$ be the number of Traffic rows and $U$ the number of distinct users. Filtering scans $N$ rows. A typical window implementation sorts or partitions login rows by user, leading to $O(N\log N)$ time, followed by another grouping pass. This matches the manifest’s time bound.
- **Auxiliary Space Complexity:** $O(U)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
