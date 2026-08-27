# Guided Example: Customer Placing the Largest Number of Orders

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Orders": [{"order_number": 77, "customer_number": 9}]}}`
- **Required output:** `{"columns": ["customer_number"], "rows": [[9]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Orders`

The objective is to compute `{"columns": ["customer_number"], "rows": [[9]]}` from `{"tables": {"Orders": [{"order_number": 77, "customer_number": 9}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: One group represents one customer

`GROUP BY customer_number` partitions all `Orders` rows according to their customer ID. If customer 3 appears in two rows, both rows belong to the same group. If customer 1 appears once, that group contains one row.

The aggregate `COUNT(1)` counts the number of rows in each group. The literal 1 is non-`NULL` for every row, so it contributes one every time. In this schema, `COUNT(*)` would give the same result. Counting `order_number` would also work because it is a non-`NULL` primary key, but `COUNT(1)` directly represents counting rows.

The query selects only `customer_number`. An aggregate used by `ORDER BY` does not have to appear in the output list, so the count can guide ranking without becoming an unwanted result column.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Orders": [{"order_number": 77, "customer_number": 9}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Ranking groups instead of individual orders

After grouping, the logical relation is equivalent to pairs such as:



`ORDER BY COUNT(1) DESC` places the group with the largest count first. Descending order is crucial; ascending order would select the customer with the fewest orders.

`LIMIT 1` retains only the first group. The input guarantee says exactly one customer has strictly more orders than every other customer. Therefore, there is no tie for first place and no secondary ordering key is needed.

The order in which SQL logically processes these clauses helps make the compact query understandable:

1. `FROM Orders` supplies individual order rows.
2. `GROUP BY customer_number` forms one group per customer.
3. `ORDER BY COUNT(1) DESC` ranks those groups by size.
4. `LIMIT 1` keeps the maximum group.
5. `SELECT customer_number` returns that group’s customer ID.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | After grouping, the logical relation is equivalent to pairs ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why a maximum of raw identifiers would be wrong

Neither the largest `customer_number` nor the largest `order_number` says anything about how many orders a customer placed. IDs are labels. The frequency of a customer label across rows is the required measure, so aggregation must precede selection.

For the sample, the four order rows contain customer numbers 1, 2, 3, and 3. Group sizes are one, one, and two. Ordering by those sizes puts customer 3 first, and the result is the single value 3.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["customer_number"], "rows": [[9]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Orders": [{"order_number": 77, "customer_number": 9}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["customer_number"], "rows": [[9]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Window ranking:** Compute counts in a grouped :** - **Window ranking:** Compute counts in a grouped common table expression and apply `ROW_NUMBER` ordered by count descending. This is explicit but longer for a guaranteed unique winner.
- **Maximum-count subquery:** Build customer counts, find their maximum, and return groups equal to it. This naturally solves the tie-inclusive follow-up but usually repeats or layers aggregation.
- **`RANK` for all leaders:** Use `RANK() OVER (ORDER BY order_count DESC)` and retain rank one. Unlike `LIMIT 1`, this returns every tied maximum.
- **Correlated count per customer:** Count one customer’s rows repeatedly from a distinct-customer list. Without an index, it can do much more work than one grouping pass.
- **Unique winner:** This guarantee is why an unspecified tie order is harmless. Remove the guarantee and the exact query may return an arbitrary tied leader.
- **One customer:** Its only group is necessarily the maximum and is returned.
- **One order per customer:** Such data would create a full tie, contradicting the unique-winner guarantee unless only one customer exists.
- **Multiple orders have unique IDs:** `order_number` uniqueness prevents duplicate order records under that primary key, but customer IDs are intentionally repeated.
- **Empty table:** `LIMIT 1` returns no row. The problem’s intended tests provide orders; an empty-input output policy is not otherwise specified.
- **Counting rows:** `COUNT(1)` and `COUNT(*)` are equivalent here. Counting a nullable expression could undercount and should be avoided.
- **No output ordering requirement beyond selection:** Once exactly one row remains, an additional final order is meaningless.
- **Follow-up with ties:** Replace top-one selection with a maximum comparison or rank-one filter; do not add an arbitrary customer-ID tie-breaker if the requirement is to return all leaders.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(c)$. Let $n$ be the number of order rows and $c$ the number of distinct customers. A hash aggregation reads $n$ rows and maintains one counter per customer, taking expected $O(n)$ time and $O(c)$ space.
- **Auxiliary Space Complexity:** $O(c)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
