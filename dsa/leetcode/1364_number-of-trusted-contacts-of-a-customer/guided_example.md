# Guided Example: Number of Trusted Contacts of a Customer

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Customers": [{"customer_id": 1, "customer_name": "Alice", "email": "alice@leetcode.com"}, {"customer_id": 2, "customer_name": "Bob", "email": "bob@leetcode.com"}, {"customer_id": 13, "customer_name": "John", "email": "john@leetcode.com"}, {"customer_id": 6, "customer_name": "Alex", "email": "alex@leetcode.com"}], "Contacts": [{"user_id": 1, "contact_name": "Bob", "contact_email": "bob@leetcode.com"}, {"user_id": 1, "contact_name": "John", "contact_email": "john@leetcode.com"}, {"user_id": 1, "contact_name": "Jal", "contact_email": "jal@leetcode.com"}, {"user_id": 2, "contact_name": "Omar", "contact_email": "omar@leetcode.com"}, {"user_id": 2, "contact_name": "Meir", "contact_email": "meir@leetcode.com"}, {"user_id": 6, "contact_name": "Alice", "contact_email": "alice@leetcode.com"}], "Invoices": [{"invoice_id": 77, "price": 100, "user_id": 1}, {"invoice_id": 88, "price": 200, "user_id": 1}, {"invoice_id": 99, "price": 300, "user_id": 2}, {"invoice_id": 66, "price": 400, "user_id": 2}, {"invoice_id": 55, "price": 500, "user_id": 13}, {"invoice_id": 44, "price": 60, "user_id": 6}]}}`
- **Required output:** `{"columns": ["invoice_id", "customer_name", "price", "contacts_cnt", "trusted_contacts_cnt"], "rows": [[44, "Alex", 60, 1, 1], [55, "John", 500, 0, 0], [66, "Bob", 400, 2, 0], [77, "Alice", 100, 3, 2], [88, "Alice", 200, 3, 2], [99, "Bob", 300, 2, 0]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Customers`

The objective is to compute `{"columns": ["invoice_id", "customer_name", "price", "contacts_cnt", "trusted_contacts_cnt"], "rows": [[44, "Alex", 60, 1, 1], [55, "John", 500, 0, 0], [66, "Bob", 400, 2, 0], [77, "Alice", 100, 3, 2], [88, "Alice", 200, 3, 2], [99, "Bob", 300, 2, 0]]}` from `{"tables": {"Customers": [{"customer_id": 1, "customer_name": "Alice", "email": "alice@leetcode.com"}, {"customer_id": 2, "customer_name": "Bob", "email": "bob@leetcode.com"}, {"customer_id": 13, "customer_name": "John", "email": "john@leetcode.com"}, {"customer_id": 6, "customer_name": "Alex", "email": "alex@leetcode.com"}], "Contacts": [{"user_id": 1, "contact_name": "Bob", "contact_email": "bob@leetcode.com"}, {"user_id": 1, "contact_name": "John", "contact_email": "john@leetcode.com"}, {"user_id": 1, "contact_name": "Jal", "contact_email": "jal@leetcode.com"}, {"user_id": 2, "contact_name": "Omar", "contact_email": "omar@leetcode.com"}, {"user_id": 2, "contact_name": "Meir", "contact_email": "meir@leetcode.com"}, {"user_id": 6, "contact_name": "Alice", "contact_email": "alice@leetcode.com"}], "Invoices": [{"invoice_id": 77, "price": 100, "user_id": 1}, {"invoice_id": 88, "price": 200, "user_id": 1}, {"invoice_id": 99, "price": 300, "user_id": 2}, {"invoice_id": 66, "price": 400, "user_id": 2}, {"invoice_id": 55, "price": 500, "user_id": 13}, {"invoice_id": 44, "price": 60, "user_id": 6}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: What one output row represents

The query starts from `Invoices` because the required result contains exactly one row for every invoice. An invoice supplies three important facts: its unique `invoice_id`, its `price`, and the `user_id` of the customer who owns it. The other two tables add information about that owner. `Customers` supplies the owner's name, while `Contacts` supplies zero or more people whom that owner trusts.

There are two related counts, and keeping their meanings separate is the central difficulty:

- `contacts_cnt` counts every contact row belonging to the invoice's customer.
- `trusted_contacts_cnt` counts only those contact rows whose `contact_email` also appears as an `email` in `Customers`.

A contact does not become trusted because its name resembles a customer's name. The test used by the exact solution is email equality.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Customers": [{"customer_id": 1, "customer_name": "Alice", "email": "alice@leetcode.com"}, {"customer_id": 2, "customer_name": "Bob", "email": "bob@leetcode.com"}, {"customer_id": 13, "customer_name": "John", "email": "john@leetcode.com"}, {"customer_id": 6, "customer_name": "Alex", "email": "alex@leetcode.com"}], "Contacts": [{"user_id": 1, "contact_name": "Bob", "contact_email": "bob@leetcode.com"}, {"user_id": 1, "contact_name": "John", "contact_email": "john@leetcode.com"}, {"user_id": 1, "contact_name": "Jal", "contact_email": "jal@leetcode.com"}, {"user_id": 2, "contact_name": "Omar", "contact_email": "omar@leetcode.com"}, {"user_id": 2, "contact_name": "Meir", "contact_email": "meir@leetcode.com"}, {"user_id": 6, "contact_name": "Alice", "contact_email": "alice@leetcode.com"}], "Invoices": [{"invoice_id": 77, "price": 100, "user_id": 1}, {"invoice_id": 88, "price": 200, "user_id": 1}, {"invoice_id": 99, "price": 300, "user_id": 2}, {"invoice_id": 66, "price": 400, "user_id": 2}, {"invoice_id": 55, "price": 500, "user_id": 13}, {"invoice_id": 44, "price": 60, "user_id": 6}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why every join is a left join

The first join is `Invoices AS t1 LEFT JOIN Customers AS t2 ON t1.user_id = t2.customer_id`. It attaches the invoice owner's customer record, allowing the query to select `t2.customer_name`. Starting with invoices and preserving the left side makes the intended ownership of the output clear: an invoice is the unit that must survive to the final result.

The second join is `LEFT JOIN Contacts AS t3 ON t1.user_id = t3.user_id`. For a customer with three contacts, the invoice row expands into three intermediate rows, one per contact. For a customer with no contacts, a left join still produces one intermediate row, but all columns from `t3` are `NULL`. An inner join would remove that invoice entirely, which would be wrong: its two counts should be zero.

The third join is `LEFT JOIN Customers AS t4 ON t3.contact_email = t4.email`. Here `t4` does not represent the invoice owner. It represents a possible shop customer whose email matches the current contact's email. A match fills `t4.email` with a non-`NULL` value. A non-customer contact remains in the intermediate result because this is also a left join, but its `t4.email` is `NULL`.

For Alice's invoice in the example, the contacts join produces rows for Bob, John, and Jal. The final join finds customer rows for Bob's and John's emails, but not for Jal's email. Those three rows therefore contain three non-`NULL` values of `t3.user_id` and two non-`NULL` values of `t4.email`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The first join is `Invoices AS t1 LEFT JOIN Customers AS t2 ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the two `COUNT` expressions give different answers

SQL's `COUNT(column)` counts non-`NULL` values in that column; it does not count every intermediate row blindly. Consequently, `COUNT(t3.user_id)` counts contact rows. On the placeholder row created for an owner with no contacts, `t3.user_id` is `NULL`, so the count is zero rather than one.

Similarly, `COUNT(t4.email)` counts only contacts that found a matching customer email. An unmatched contact is preserved by the left join, but `t4.email` is `NULL` and contributes nothing. This use of nullability turns the same joined rows into both the total count and the filtered trusted count without a separate conditional expression.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["invoice_id", "customer_name", "price", "contacts_cnt", "trusted_contacts_cnt"], "rows": [[44, "Alex", 60, 1, 1], [55, "John", 500, 0, 0], [66, "Bob", 400, 2, 0], [77, "Alice", 100, 3, 2], [88, "Alice", 200, 3, 2], [99, "Bob", 300, 2, 0]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Customers": [{"customer_id": 1, "customer_name": "Alice", "email": "alice@leetcode.com"}, {"customer_id": 2, "customer_name": "Bob", "email": "bob@leetcode.com"}, {"customer_id": 13, "customer_name": "John", "email": "john@leetcode.com"}, {"customer_id": 6, "customer_name": "Alex", "email": "alex@leetcode.com"}], "Contacts": [{"user_id": 1, "contact_name": "Bob", "contact_email": "bob@leetcode.com"}, {"user_id": 1, "contact_name": "John", "contact_email": "john@leetcode.com"}, {"user_id": 1, "contact_name": "Jal", "contact_email": "jal@leetcode.com"}, {"user_id": 2, "contact_name": "Omar", "contact_email": "omar@leetcode.com"}, {"user_id": 2, "contact_name": "Meir", "contact_email": "meir@leetcode.com"}, {"user_id": 6, "contact_name": "Alice", "contact_email": "alice@leetcode.com"}], "Invoices": [{"invoice_id": 77, "price": 100, "user_id": 1}, {"invoice_id": 88, "price": 200, "user_id": 1}, {"invoice_id": 99, "price": 300, "user_id": 2}, {"invoice_id": 66, "price": 400, "user_id": 2}, {"invoice_id": 55, "price": 500, "user_id": 13}, {"invoice_id": 44, "price": 60, "user_id": 6}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["invoice_id", "customer_name", "price", "contacts_cnt", "trusted_contacts_cnt"], "rows": [[44, "Alex", 60, 1, 1], [55, "John", 500, 0, 0], [66, "Bob", 400, 2, 0], [77, "Alice", 100, 3, 2], [88, "Alice", 200, 3, 2], [99, "Bob", 300, 2, 0]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Pre-aggregate contacts first:** Group `Contact:** - **Pre-aggregate contacts first:** Group `Contacts` by `user_id`, compute total and trusted counts, and then join that compact result to `Invoices`. This can avoid repeating the same aggregation work for customers with many invoices, but it requires a longer query or a common table expression.
- **Conditional aggregation:** A query can use a condition inside `SUM` or `COUNT` to identify trusted contacts. This makes the predicate explicit, although the extra customer-email lookup is still required.
- **`EXISTS` for trust membership:** Testing whether a customer email exists avoids multiplying rows when `Customers.email` is not unique. The exact solution instead counts rows produced by its final join, so it relies on each contact email matching at most one relevant customer row.
- **No contacts:** The contact left join creates a null placeholder. Both counted columns are null, producing `0` and `0` while keeping the invoice.
- **Contact who is not a customer:** `t3.user_id` is present but `t4.email` is null. The row increases `contacts_cnt` only.
- **Contact who is a customer:** Both counted values are present. The row increases both totals exactly once under the intended unique-email lookup.
- **Several invoices for one customer:** Each invoice forms a separate `invoice_id` group. The contact counts repeat, but invoice IDs and prices remain distinct.
- **Duplicate customer emails:** The local schema explicitly makes `customer_id` unique but does not state the same property for `email`. If duplicate email rows are legal, the final join duplicates a contact and the exact `COUNT` expressions overcount; pre-deduplicating emails or using `EXISTS` is the robust remedy.
- **Missing owner row:** The first left join preserves such an invoice but returns a null customer name. Normal problem data is expected to associate invoices with customers; preserving the row is still safer than silently discarding it.
- **Ordering:** `GROUP BY` does not promise sorted output. `ORDER BY invoice_id` is essential, including when the sample input already appears nearly ordered.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $C$, $K$, and $I$ denote the numbers of rows in `Customers`, `Contacts`, and `Invoices`, and let $N=C+K+I$. The manifest states $O(N\log N)$ time and $O(N)$ space. This is a useful high-level bound for a conventional execution plan: the database can build indexes or hash tables for the equality joins and grouping, while the final ordering of up to $I$ result rows costs $O(I\log I)$. The sort is the part that naturally introduces the logarithmic factor.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
