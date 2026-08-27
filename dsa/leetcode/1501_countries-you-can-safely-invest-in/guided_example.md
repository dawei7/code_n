# Guided Example: Countries You Can Safely Invest In

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Person": [{"id": 3, "name": "Jonathan", "phone_number": "051-1234567"}, {"id": 12, "name": "Elvis", "phone_number": "051-7654321"}, {"id": 1, "name": "Moncef", "phone_number": "212-1234567"}, {"id": 2, "name": "Maroua", "phone_number": "212-6523651"}, {"id": 7, "name": "Meir", "phone_number": "972-1234567"}, {"id": 9, "name": "Rachel", "phone_number": "972-0011100"}], "Country": [{"name": "Peru", "country_code": "051"}, {"name": "Israel", "country_code": "972"}, {"name": "Morocco", "country_code": "212"}, {"name": "Germany", "country_code": "049"}, {"name": "Ethiopia", "country_code": "251"}], "Calls": [{"caller_id": 1, "callee_id": 9, "duration": 33}, {"caller_id": 2, "callee_id": 9, "duration": 4}, {"caller_id": 1, "callee_id": 2, "duration": 59}, {"caller_id": 3, "callee_id": 12, "duration": 102}, {"caller_id": 3, "callee_id": 12, "duration": 330}, {"caller_id": 12, "callee_id": 3, "duration": 5}, {"caller_id": 7, "callee_id": 9, "duration": 13}, {"caller_id": 7, "callee_id": 1, "duration": 3}, {"caller_id": 9, "callee_id": 7, "duration": 1}, {"caller_id": 1, "callee_id": 7, "duration": 7}]}}`
- **Required output:** `{"columns": ["country"], "rows": [["Peru"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table `Person`:

The objective is to compute `{"columns": ["country"], "rows": [["Peru"]]}` from `{"tables": {"Person": [{"id": 3, "name": "Jonathan", "phone_number": "051-1234567"}, {"id": 12, "name": "Elvis", "phone_number": "051-7654321"}, {"id": 1, "name": "Moncef", "phone_number": "212-1234567"}, {"id": 2, "name": "Maroua", "phone_number": "212-6523651"}, {"id": 7, "name": "Meir", "phone_number": "972-1234567"}, {"id": 9, "name": "Rachel", "phone_number": "972-0011100"}], "Country": [{"name": "Peru", "country_code": "051"}, {"name": "Israel", "country_code": "972"}, {"name": "Morocco", "country_code": "212"}, {"name": "Germany", "country_code": "049"}, {"name": "Ethiopia", "country_code": "251"}], "Calls": [{"caller_id": 1, "callee_id": 9, "duration": 33}, {"caller_id": 2, "callee_id": 9, "duration": 4}, {"caller_id": 1, "callee_id": 2, "duration": 59}, {"caller_id": 3, "callee_id": 12, "duration": 102}, {"caller_id": 3, "callee_id": 12, "duration": 330}, {"caller_id": 12, "callee_id": 3, "duration": 5}, {"caller_id": 7, "callee_id": 9, "duration": 13}, {"caller_id": 7, "callee_id": 1, "duration": 3}, {"caller_id": 9, "callee_id": 7, "duration": 1}, {"caller_id": 1, "callee_id": 7, "duration": 7}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why each call must be viewed from both endpoints

A country's average is based on calls involving people in that country, whether those people were callers or callees. The join

`Person JOIN Calls ON id IN (caller_id, callee_id)`

matches a call row to its caller's person row and separately to its callee's person row. Because the contract guarantees different caller and callee IDs, each call produces exactly two endpoint rows when both people exist.

This duplication is intentional. A call between two countries contributes its full duration once to each country's endpoint statistics. A call within one country contributes twice to that country's sum and count, once for each participating person. The sample explanation follows precisely this endpoint interpretation.

Duplicate rows in `Calls` remain separate events. Each duplicate also generates two endpoint rows and therefore retains its multiplicity in every average.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Person": [{"id": 3, "name": "Jonathan", "phone_number": "051-1234567"}, {"id": 12, "name": "Elvis", "phone_number": "051-7654321"}, {"id": 1, "name": "Moncef", "phone_number": "212-1234567"}, {"id": 2, "name": "Maroua", "phone_number": "212-6523651"}, {"id": 7, "name": "Meir", "phone_number": "972-1234567"}, {"id": 9, "name": "Rachel", "phone_number": "972-0011100"}], "Country": [{"name": "Peru", "country_code": "051"}, {"name": "Israel", "country_code": "972"}, {"name": "Morocco", "country_code": "212"}, {"name": "Germany", "country_code": "049"}, {"name": "Ethiopia", "country_code": "251"}], "Calls": [{"caller_id": 1, "callee_id": 9, "duration": 33}, {"caller_id": 2, "callee_id": 9, "duration": 4}, {"caller_id": 1, "callee_id": 2, "duration": 59}, {"caller_id": 3, "callee_id": 12, "duration": 102}, {"caller_id": 3, "callee_id": 12, "duration": 330}, {"caller_id": 12, "callee_id": 3, "duration": 5}, {"caller_id": 7, "callee_id": 9, "duration": 13}, {"caller_id": 7, "callee_id": 1, "duration": 3}, {"caller_id": 9, "callee_id": 7, "duration": 1}, {"caller_id": 1, "callee_id": 7, "duration": 7}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Mapping a person to a country

Phone numbers begin with a three-character country code and may contain leading zeroes. `LEFT(phone_number, 3)` extracts those first three characters as text. Joining that value to `Country.country_code` preserves codes such as `051` that would be damaged by numeric conversion.

The alias `c` refers to `Country`, and `c.name AS country` gives the result column its required name. An inner join means a person whose prefix has no country row contributes to no country group.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Phone numbers begin with a three-character country code and ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Building each country's average

The derived table groups endpoint rows by the selected country. `AVG(duration) AS duration` computes the arithmetic mean of every incident call endpoint for that country.

`GROUP BY 1` is positional syntax meaning group by the first selected expression, which is `c.name AS country`. Grouping by an explicit column expression would be more descriptive, but the positional form is valid MySQL syntax.

For a cross-country call of duration thirty, each involved country receives one thirty-minute endpoint. For a domestic call of duration thirty, the same country receives two thirty-minute endpoints. Duplicating a value twice does not change that individual call's value, but it gives appropriate weight to both residents participating under the endpoint definition.

Countries with no call endpoint never appear in the person-call join and therefore never form a group.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["country"], "rows": [["Peru"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Person": [{"id": 3, "name": "Jonathan", "phone_number": "051-1234567"}, {"id": 12, "name": "Elvis", "phone_number": "051-7654321"}, {"id": 1, "name": "Moncef", "phone_number": "212-1234567"}, {"id": 2, "name": "Maroua", "phone_number": "212-6523651"}, {"id": 7, "name": "Meir", "phone_number": "972-1234567"}, {"id": 9, "name": "Rachel", "phone_number": "972-0011100"}], "Country": [{"name": "Peru", "country_code": "051"}, {"name": "Israel", "country_code": "972"}, {"name": "Morocco", "country_code": "212"}, {"name": "Germany", "country_code": "049"}, {"name": "Ethiopia", "country_code": "251"}], "Calls": [{"caller_id": 1, "callee_id": 9, "duration": 33}, {"caller_id": 2, "callee_id": 9, "duration": 4}, {"caller_id": 1, "callee_id": 2, "duration": 59}, {"caller_id": 3, "callee_id": 12, "duration": 102}, {"caller_id": 3, "callee_id": 12, "duration": 330}, {"caller_id": 12, "callee_id": 3, "duration": 5}, {"caller_id": 7, "callee_id": 9, "duration": 13}, {"caller_id": 7, "callee_id": 1, "duration": 3}, {"caller_id": 9, "callee_id": 7, "duration": 1}, {"caller_id": 1, "callee_id": 7, "duration": 7}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["country"], "rows": [["Peru"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **UNION ALL endpoint normalization:** Produce ca:** - **UNION ALL endpoint normalization:** Produce caller-duration rows and callee-duration rows separately, combine them with `UNION ALL`, then join people and countries. This makes the two-endpoint semantics explicit and can improve optimizer options.
- **UNION instead of UNION ALL:** It is wrong because it could remove duplicate endpoint rows, while every call row and both endpoints must retain their weight.
- **Conditional joins:** Joining calls to caller and callee people in separate aliases can work but requires reshaping both endpoints before one country aggregation.
- **Domestic call:** It contributes twice to the same country, once per distinct participant.
- **International call:** Its duration contributes once to each endpoint country.
- **Duplicate call rows:** They count independently and must not be deduplicated.
- **Country with no calls:** It has no group and is absent rather than treated as having average zero.
- **Average equal to global:** Strict greater-than excludes it.
- **Leading-zero country code:** Text prefix extraction preserves the zeros.
- **Null durations:** SQL `AVG` ignores nulls; the reference presents duration values but does not specify null semantics.
- **Unrestricted output order:** No `ORDER BY` is needed or implied.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(P+C+E)$. Let $P$ be the number of people, $C$ the number of countries, and $E$ the number of call rows. The endpoint join can produce up to $2E$ person-call matches before country grouping. A plan using indexes or hash structures can process the base rows and joins near linearly, while grouping may use hashing or sorting.
- **Auxiliary Space Complexity:** $O(P + C + E)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
