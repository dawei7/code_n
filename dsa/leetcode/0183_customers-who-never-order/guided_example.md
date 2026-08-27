# Guided Example: Customers Who Never Order

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Customers": [{"id": 1, "name": "Joe"}, {"id": 2, "name": "Henry"}, {"id": 3, "name": "Sam"}, {"id": 4, "name": "Max"}], "Orders": [{"id": 1, "customerId": 1}, {"id": 2, "customerId": 3}]}}`
- **Required output:** `{"columns": ["Customers"], "rows": [["Henry"], ["Max"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Customers`

The objective is to compute `{"columns": ["Customers"], "rows": [["Henry"], ["Max"]]}` from `{"tables": {"Customers": [{"id": 1, "name": "Joe"}, {"id": 2, "name": "Henry"}, {"id": 3, "name": "Sam"}, {"id": 4, "name": "Max"}], "Orders": [{"id": 1, "customerId": 1}, {"id": 2, "customerId": 3}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Translate “never ordered” into set exclusion

The two tables describe opposite sides of one relationship. `Customers.id` is
the unique identifier of a registered customer, while `Orders.customerId`
records which customer placed an order. A customer has ordered something when
that customer's ID occurs at least once in the order table. Consequently, a
customer has never ordered when the ID does not occur there at all.

This reformulation is important because the required output is not an order
count. It is an anti-membership question: retain rows from `Customers` for
which no related row exists in `Orders`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Customers": [{"id": 1, "name": "Joe"}, {"id": 2, "name": "Henry"}, {"id": 3, "name": "Sam"}, {"id": 4, "name": "Max"}], "Orders": [{"id": 1, "customerId": 1}, {"id": 2, "customerId": 3}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Construct the set of IDs that have ordered

The inner query selects `customerId` from every order. Conceptually, this is
the collection of customer IDs that must be excluded:

`SELECT customerId FROM Orders`

Several orders may belong to the same customer, so the collection can contain
duplicates. Those duplicates do not affect membership. If ID 3 appears once
or one hundred times, the outer condition still learns the same fact: customer
3 has placed at least one order. For that reason, the subquery does not need a
`DISTINCT` operation.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The inner query selects `customerId` from every order.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Keep IDs absent from that collection

The outer query scans customer rows and evaluates `id NOT IN (...)`. A row
survives exactly when its ID is not among the IDs produced by the inner query.
The row's name is then projected as the answer.

The alias in `name AS Customers` is part of the result contract. The source
column is named `name`, but the requested one-column table must be headed
`Customers`. The alias changes result metadata, not the stored value.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["Customers"], "rows": [["Henry"], ["Max"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Customers": [{"id": 1, "name": "Joe"}, {"id": 2, "name": "Henry"}, {"id": 3, "name": "Sam"}, {"id": 4, "name": "Max"}], "Orders": [{"id": 1, "customerId": 1}, {"id": 2, "customerId": 3}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["Customers"], "rows": [["Henry"], ["Max"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Correlated `NOT EXISTS`:** Test that no order :** - **Correlated `NOT EXISTS`:** Test that no order has `customerId = Customers.id`; this is explicit anti-membership and remains safe when unrelated nulls occur.
- **Left anti-join:** Left-join orders and retain rows whose right-side key is null; often clear to beginners and optimizer-friendly.
- **Pandas exclusion:** Use negated `isin` on customer IDs, then select and rename `name`, as the local editorial demonstrates.
- **Duplicate orders:** Repeated order IDs for one customer do not change membership, so no `DISTINCT` is necessary.
- **Duplicate customer names:** Filter by ID and preserve one result row per qualifying customer rather than deduplicating names.
- **No orders:** With an empty subquery, every customer qualifies.
- **Every customer ordered:** Every ID is excluded, producing an empty table.
- **No customers:** There are no outer rows to return.
- **Nullable `customerId`:** A null can poison `NOT IN`; prefer `NOT EXISTS` unless non-nullness is guaranteed.
- **Any result order:** Do not add sorting unless a separate presentation requirement asks for it.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(o)$. Let $c$ be the number of rows in `Customers` and $o$ the number of rows in
- **Auxiliary Space Complexity:** $O(c)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
