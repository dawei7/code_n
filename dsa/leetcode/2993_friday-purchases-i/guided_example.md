# Guided Example: Friday Purchases I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Purchases": [{"user_id": 11, "purchase_date": "2023-11-07", "amount_spend": 1126}, {"user_id": 15, "purchase_date": "2023-11-30", "amount_spend": 7473}, {"user_id": 17, "purchase_date": "2023-11-14", "amount_spend": 2414}, {"user_id": 12, "purchase_date": "2023-11-24", "amount_spend": 9692}, {"user_id": 8, "purchase_date": "2023-11-03", "amount_spend": 5117}, {"user_id": 1, "purchase_date": "2023-11-16", "amount_spend": 5241}, {"user_id": 10, "purchase_date": "2023-11-12", "amount_spend": 8266}, {"user_id": 13, "purchase_date": "2023-11-24", "amount_spend": 12000}]}}`
- **Required output:** `{"columns": ["week_of_month", "purchase_date", "total_amount"], "rows": [[1, "2023-11-03", 5117], [4, "2023-11-24", 21692]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Purchases`

The objective is to compute `{"columns": ["week_of_month", "purchase_date", "total_amount"], "rows": [[1, "2023-11-03", 5117], [4, "2023-11-24", 21692]]}` from `{"tables": {"Purchases": [{"user_id": 11, "purchase_date": "2023-11-07", "amount_spend": 1126}, {"user_id": 15, "purchase_date": "2023-11-30", "amount_spend": 7473}, {"user_id": 17, "purchase_date": "2023-11-14", "amount_spend": 2414}, {"user_id": 12, "purchase_date": "2023-11-24", "amount_spend": 9692}, {"user_id": 8, "purchase_date": "2023-11-03", "amount_spend": 5117}, {"user_id": 1, "purchase_date": "2023-11-16", "amount_spend": 5241}, {"user_id": 10, "purchase_date": "2023-11-12", "amount_spend": 8266}, {"user_id": 13, "purchase_date": "2023-11-24", "amount_spend": 12000}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Filter to the dates that can appear

This version should output only weeks containing at least one Friday purchase. Therefore, it can begin from purchase rows and discard everything that is not a Friday in November 2023.

The `WHERE` clause has two tests:

- `DATE_FORMAT(purchase_date, '%Y%m') = '202311'` restricts rows to November 2023;
- `DAYOFWEEK(purchase_date) = 6` restricts rows to Friday under MySQL’s numbering.

In MySQL, `DAYOFWEEK` returns one for Sunday, two for Monday, through seven for Saturday. Friday is consequently six. Confusing this with ISO weekday numbering would select the wrong day.

The local table contract already says dates lie in November 2023, so the date-format test is redundant for valid inputs. It nevertheless makes the intended month explicit and does not change the result.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Purchases": [{"user_id": 11, "purchase_date": "2023-11-07", "amount_spend": 1126}, {"user_id": 15, "purchase_date": "2023-11-30", "amount_spend": 7473}, {"user_id": 17, "purchase_date": "2023-11-14", "amount_spend": 2414}, {"user_id": 12, "purchase_date": "2023-11-24", "amount_spend": 9692}, {"user_id": 8, "purchase_date": "2023-11-03", "amount_spend": 5117}, {"user_id": 1, "purchase_date": "2023-11-16", "amount_spend": 5241}, {"user_id": 10, "purchase_date": "2023-11-12", "amount_spend": 8266}, {"user_id": 13, "purchase_date": "2023-11-24", "amount_spend": 12000}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Aggregate every Friday date

`GROUP BY 2` groups by the second selected column, `purchase_date`. Every purchase made on the same Friday is combined, and `SUM(amount_spend)` gives that date’s total.

The grouping key is the full date rather than only the week number. In November 2023 there is exactly one Friday in each seven-day week block, so each qualifying week corresponds to one grouped date.

Because the query starts from actual purchases, a Friday with no rows never creates a group. This is exactly the difference between version I and version II.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `GROUP BY 2` groups by the second selected column, `purchase... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Derive the one-based week of month

The first output expression is:

`CEIL(DAYOFMONTH(purchase_date) / 7)`.

`DAYOFMONTH` returns a number from one through 30. Dividing by seven and rounding upward maps days 1–7 to week one, 8–14 to week two, 15–21 to week three, 22–28 to week four, and 29–30 to week five.

November 2023 Fridays are the 3rd, 10th, 17th, and 24th, so their derived week numbers are one through four. There is no Friday in the final two-day fifth block.

The expression is aliased `week_of_month`, while the sum is aliased `total_amount`. `purchase_date` itself remains the middle output column.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["week_of_month", "purchase_date", "total_amount"], "rows": [[1, "2023-11-03", 5117], [4, "2023-11-24", 21692]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Purchases": [{"user_id": 11, "purchase_date": "2023-11-07", "amount_spend": 1126}, {"user_id": 15, "purchase_date": "2023-11-30", "amount_spend": 7473}, {"user_id": 17, "purchase_date": "2023-11-14", "amount_spend": 2414}, {"user_id": 12, "purchase_date": "2023-11-24", "amount_spend": 9692}, {"user_id": 8, "purchase_date": "2023-11-03", "amount_spend": 5117}, {"user_id": 1, "purchase_date": "2023-11-16", "amount_spend": 5241}, {"user_id": 10, "purchase_date": "2023-11-12", "amount_spend": 8266}, {"user_id": 13, "purchase_date": "2023-11-24", "amount_spend": 12000}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["week_of_month", "purchase_date", "total_amount"], "rows": [[1, "2023-11-03", 5117], [4, "2023-11-24", 21692]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Generate a Friday calendar:** That is necessar:** - **Generate a Friday calendar:** That is necessary in version II but would add zero-purchase weeks that this version must omit.
- **Use ISO weekday numbers:** MySQL `DAYOFWEEK` is Sunday-based; Friday is six, not five.
- **Group by week alone:** It works for this fixed month’s one-Friday-per-block layout, but grouping by date directly preserves the requested date column.
- **Month filter via date range:** It is more index-friendly than `DATE_FORMAT` and equivalent for general data.
- **Several purchases on one Friday:** `SUM` combines them into one output row.
- **No Friday purchases:** Filtering leaves no groups, so the result is empty.
- **Purchases on other weekdays:** They are ignored even when they fall in a week that has a Friday purchase.
- **Fifth week block:** November 29–30, 2023 contains no Friday, so no week-five row can appear.
- **Output order:** `ORDER BY 1` sorts `week_of_month` ascending.
- **Week-number definition:** `CEIL(DAYOFMONTH(purchase_date) / 7)` maps days 1–7 to week one, 8–14 to week two, and so forth, matching the month's seven-day blocks.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(F\log F)$. Let $R$ be the number of purchase rows and $F$ the number that survive the Friday filter. Scanning and filtering costs $O(R)$. Grouping can use hashing in expected $O(F)$ time or sorting in $O(F\log F)$. Ordering the at most four November-Friday groups is constant for this fixed month.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
