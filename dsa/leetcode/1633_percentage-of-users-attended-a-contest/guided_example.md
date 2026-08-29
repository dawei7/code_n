# Guided Example: Percentage of Users Attended a Contest

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Users": [{"user_id": 6, "user_name": "Alice"}, {"user_id": 2, "user_name": "Bob"}, {"user_id": 7, "user_name": "Alex"}], "Register": [{"contest_id": 215, "user_id": 6}, {"contest_id": 209, "user_id": 2}, {"contest_id": 208, "user_id": 2}, {"contest_id": 210, "user_id": 6}, {"contest_id": 208, "user_id": 6}, {"contest_id": 209, "user_id": 7}, {"contest_id": 209, "user_id": 6}, {"contest_id": 215, "user_id": 7}, {"contest_id": 208, "user_id": 7}, {"contest_id": 210, "user_id": 2}, {"contest_id": 207, "user_id": 2}, {"contest_id": 210, "user_id": 7}]}}`
- **Required output:** `{"columns": ["contest_id", "percentage"], "rows": [[208, 100], [209, 100], [210, 100], [215, 66.67], [207, 33.33]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Users`

The objective is to compute `{"columns": ["contest_id", "percentage"], "rows": [[208, 100], [209, 100], [210, 100], [215, 66.67], [207, 33.33]]}` from `{"tables": {"Users": [{"user_id": 6, "user_name": "Alice"}, {"user_id": 2, "user_name": "Bob"}, {"user_id": 7, "user_name": "Alex"}], "Register": [{"contest_id": 215, "user_id": 6}, {"contest_id": 209, "user_id": 2}, {"contest_id": 208, "user_id": 2}, {"contest_id": 210, "user_id": 6}, {"contest_id": 208, "user_id": 6}, {"contest_id": 209, "user_id": 7}, {"contest_id": 209, "user_id": 6}, {"contest_id": 215, "user_id": 7}, {"contest_id": 208, "user_id": 7}, {"contest_id": 210, "user_id": 2}, {"contest_id": 207, "user_id": 2}, {"contest_id": 210, "user_id": 7}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The denominator is the complete user population

The requested percentage for a contest is

$$
\frac{\text{number of users registered for that contest}}
{\text{number of users in Users}}\times100.
$$

The scalar subquery `(SELECT COUNT(1) FROM Users)` computes the denominator. `COUNT(1)` counts every row because the constant 1 is never null. Since `user_id` is the primary key, each Users row represents one distinct user, so counting rows is the same as counting users.

This denominator is common to every contest. Although it is written as a scalar subquery inside the select expression, it returns exactly one number and can be reused conceptually for every group. A database optimizer will commonly evaluate or cache such an uncorrelated scalar subquery once.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Users": [{"user_id": 6, "user_name": "Alice"}, {"user_id": 2, "user_name": "Bob"}, {"user_id": 7, "user_name": "Alex"}], "Register": [{"contest_id": 215, "user_id": 6}, {"contest_id": 209, "user_id": 2}, {"contest_id": 208, "user_id": 2}, {"contest_id": 210, "user_id": 6}, {"contest_id": 208, "user_id": 6}, {"contest_id": 209, "user_id": 7}, {"contest_id": 209, "user_id": 6}, {"contest_id": 215, "user_id": 7}, {"contest_id": 208, "user_id": 7}, {"contest_id": 210, "user_id": 2}, {"contest_id": 207, "user_id": 2}, {"contest_id": 210, "user_id": 7}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Group registrations by contest

The outer query reads `Register` and groups by the first selected expression through `GROUP BY 1`. The first selected expression is `contest_id`, so this is positional shorthand for `GROUP BY contest_id`.

Each resulting group contains all registration rows for one contest. `COUNT(1)` counts those rows. The composite primary key `(contest_id, user_id)` guarantees that one user cannot appear twice in the same contest group. Therefore the row count is already the number of distinct registered users; `COUNT(DISTINCT user_id)` would produce the same result but is unnecessary under the schema.

Only contests represented in `Register` form groups. That matches the data model used by the query: the result reports contests with registration records, and there is no separate Contests table from which to generate empty contests.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Calculate and round the percentage

For each group, the source evaluates

`COUNT(1) * 100 / total_users`.

Multiplying by 100 converts the registration fraction into a percentage. In MySQL, the `/` operator performs division rather than integer `DIV`, so a count such as 2 out of 3 can retain its fractional part instead of becoming zero.

`ROUND(..., 2)` rounds the computed percentage to two digits after the decimal point. For 2 registered users among 3 total users, the unrounded percentage is approximately $66.666\ldots$, and the selected value is $66.67$.

The alias `percentage` gives the calculated column its required output name. The only other selected column is `contest_id`, so the result schema is exact.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["contest_id", "percentage"], "rows": [[208, 100], [209, 100], [210, 100], [215, 66.67], [207, 33.33]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Users": [{"user_id": 6, "user_name": "Alice"}, {"user_id": 2, "user_name": "Bob"}, {"user_id": 7, "user_name": "Alex"}], "Register": [{"contest_id": 215, "user_id": 6}, {"contest_id": 209, "user_id": 2}, {"contest_id": 208, "user_id": 2}, {"contest_id": 210, "user_id": 6}, {"contest_id": 208, "user_id": 6}, {"contest_id": 209, "user_id": 7}, {"contest_id": 209, "user_id": 6}, {"contest_id": 215, "user_id": 7}, {"contest_id": 208, "user_id": 7}, {"contest_id": 210, "user_id": 2}, {"contest_id": 207, "user_id": 2}, {"contest_id": 210, "user_id": 7}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["contest_id", "percentage"], "rows": [[208, 100], [209, 100], [210, 100], [215, 66.67], [207, 33.33]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Use `COUNT(DISTINCT user_id)`:** This is robust to duplicate registration rows, but the composite primary key already forbids them. Distinct aggregation can require extra work.
- **Cross join a one-row total CTE:** Compute the Users count once in a CTE and cross join it to contest aggregates. This can make denominator reuse explicit but produces the same result.
- **Join Register to Users:** It is unnecessary when registration user IDs conform to the intended schema and no user attributes are needed. A join adds work without changing the numerator.
- **Spell out column names:** `GROUP BY contest_id ORDER BY percentage DESC, contest_id ASC` is more resilient to select-list reordering than positional ordinals. The exact source uses positions.
- **Contest with every user registered:** Its percentage is exactly 100.
- **Contest with one of three users:** The expression retains the fraction and `ROUND` returns 33.33.
- **Tied percentages:** Contest ID ascending is the deterministic secondary key.
- **Duplicate registration attempt:** The primary key prevents two rows for the same contest-user pair, which is why `COUNT(1)` is sufficient.
- **No registration rows:** The query returns no contest groups. There is no separate contest table in the contract from which to emit zero-percent rows.
- **Empty Users table:** Division by zero would be undefined. The intended problem data assumes a user population for percentages; a broader production query would need an explicit zero-denominator policy.
- **Rounding point:** The source rounds the final percentage, not the numerator or denominator separately.
- **Changing select order:** Because `GROUP BY 1` and `ORDER BY 2, 1` are positional, such a refactor must update the ordinals or replace them with names.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(u+r+c\log c)$. Let $u$ be the number of Users rows, $r$ the number of Register rows, and $c$ the number of distinct contests represented in Register.
- **Auxiliary Space Complexity:** $O(c)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
