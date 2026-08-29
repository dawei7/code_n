# Guided Example: Combine Two Tables

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Person": [{"personId": 1, "lastName": "Wang", "firstName": "Allen"}, {"personId": 2, "lastName": "Alice", "firstName": "Bob"}], "Address": [{"addressId": 1, "personId": 2, "city": "New York City", "state": "New York"}, {"addressId": 2, "personId": 3, "city": "Leetcode", "state": "California"}]}}`
- **Required output:** `{"columns": ["firstName", "lastName", "city", "state"], "rows": [["Allen", "Wang", null, null], ["Bob", "Alice", "New York City", "New York"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Person`

The objective is to compute `{"columns": ["firstName", "lastName", "city", "state"], "rows": [["Allen", "Wang", null, null], ["Bob", "Alice", "New York City", "New York"]]}` from `{"tables": {"Person": [{"personId": 1, "lastName": "Wang", "firstName": "Allen"}, {"personId": 2, "lastName": "Alice", "firstName": "Bob"}], "Address": [{"addressId": 1, "personId": 2, "city": "New York City", "state": "New York"}, {"addressId": 2, "personId": 3, "city": "Leetcode", "state": "California"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Choose `Person` as the preserved relation

The requested output must contain every row from `Person`, even when no
matching address exists. That requirement determines the join type and its
direction:

`Person LEFT JOIN Address`.

A left outer join preserves all rows from the table written on the left. For
each person, it searches for `Address` rows with the same `personId`. A match
combines the columns from both rows. If no match exists, the database still
emits the person's row and supplies SQL `NULL` for columns belonging to
`Address`.

An inner join would discard unmatched people and therefore fail the central
contract.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Person": [{"personId": 1, "lastName": "Wang", "firstName": "Allen"}, {"personId": 2, "lastName": "Alice", "firstName": "Bob"}], "Address": [{"addressId": 1, "personId": 2, "city": "New York City", "state": "New York"}, {"addressId": 2, "personId": 3, "city": "Leetcode", "state": "California"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use the shared key explicitly through `USING`

The optimal query writes:

`LEFT JOIN Address USING (personId)`.

`USING (personId)` is join syntax available when both input tables have a
column with that exact name. It means the equality condition:

`Person.personId = Address.personId`.

It also presents the shared join key as one coalesced column in the joined
relation rather than two separately named copies. The query does not project
that key, so the visible difference is minor here.

`Person.personId` is a primary key, ensuring at most one person row for a given
identifier. `Address.addressId` is its primary key. The local schema does not
explicitly declare `Address.personId` unique, so relationally, multiple address
rows with the same person ID would produce multiple joined output rows for that
person. The query correctly follows ordinary join semantics rather than
silently choosing one.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Project only the required columns

After joining, the intermediate relation includes identifiers and name and
address fields. The `SELECT` list narrows it to:

- `firstName`;
- `lastName`;
- `city`;
- `state`.

Their order exactly matches the requested result schema. Avoiding `SELECT *`
prevents extra `personId` and `addressId` columns from leaking into the result.

The columns named `city` and `state` come only from `Address`; `firstName` and
`lastName` come only from `Person`, so they are unambiguous without table
qualifiers. Qualifiers could still improve readability, but they are not
required for this schema.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["firstName", "lastName", "city", "state"], "rows": [["Allen", "Wang", null, null], ["Bob", "Alice", "New York City", "New York"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Person": [{"personId": 1, "lastName": "Wang", "firstName": "Allen"}, {"personId": 2, "lastName": "Alice", "firstName": "Bob"}], "Address": [{"addressId": 1, "personId": 2, "city": "New York City", "state": "New York"}, {"addressId": 2, "personId": 3, "city": "Leetcode", "state": "California"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["firstName", "lastName", "city", "state"], "rows": [["Allen", "Wang", null, null], ["Bob", "Alice", "New York City", "New York"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Explicit `ON` condition:** `LEFT JOIN Address ON Person.personId = Address.personId` is equivalent and works even when key names differ.
- **Right join with reversed tables:** Can preserve `Person`, but is less direct and less portable in style.
- **Inner join:** Incorrect because it drops people without addresses.
- **Correlated subqueries:** Could fetch each address column separately, but duplicate work and multirow semantics are awkward.
- **No matching address:** Produces SQL `NULL` for both location fields.
- **Orphan address:** Produces no row because `Address` is not the preserved side.
- **Multiple matches:** Emits one joined row per address match unless uniqueness is separately guaranteed.
- **Column projection:** Omitting identifiers is required by the output schema.
- **Any order:** No `ORDER BY` is necessary.
- **Physical complexity:** Actual runtime depends on indexes, statistics, optimizer choices, and output cardinality.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(P+A)$. Let $P$ and $A$ be the row counts in `Person` and `Address`. With a hash join,
- **Auxiliary Space Complexity:** $O(P + A)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
