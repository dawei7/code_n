# Guided Example: Bank Account Summary II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Users": [{"account": 900001, "name": "Alice"}, {"account": 900002, "name": "Bob"}, {"account": 900003, "name": "Charlie"}], "Transactions": [{"trans_id": 1, "account": 900001, "amount": 7000, "transacted_on": "2020-08-01"}, {"trans_id": 2, "account": 900001, "amount": 7000, "transacted_on": "2020-09-01"}, {"trans_id": 3, "account": 900001, "amount": -3000, "transacted_on": "2020-09-02"}, {"trans_id": 4, "account": 900002, "amount": 1000, "transacted_on": "2020-09-12"}, {"trans_id": 5, "account": 900003, "amount": 6000, "transacted_on": "2020-08-07"}, {"trans_id": 6, "account": 900003, "amount": 6000, "transacted_on": "2020-09-07"}, {"trans_id": 7, "account": 900003, "amount": -4000, "transacted_on": "2020-09-11"}]}}`
- **Required output:** `{"columns": ["name", "balance"], "rows": [["Alice", 11000]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Users`

The objective is to compute `{"columns": ["name", "balance"], "rows": [["Alice", 11000]]}` from `{"tables": {"Users": [{"account": 900001, "name": "Alice"}, {"account": 900002, "name": "Bob"}, {"account": 900003, "name": "Charlie"}], "Transactions": [{"trans_id": 1, "account": 900001, "amount": 7000, "transacted_on": "2020-08-01"}, {"trans_id": 2, "account": 900001, "amount": 7000, "transacted_on": "2020-09-01"}, {"trans_id": 3, "account": 900001, "amount": -3000, "transacted_on": "2020-09-02"}, {"trans_id": 4, "account": 900002, "amount": 1000, "transacted_on": "2020-09-12"}, {"trans_id": 5, "account": 900003, "amount": 6000, "transacted_on": "2020-08-07"}, {"trans_id": 6, "account": 900003, "amount": 6000, "transacted_on": "2020-09-07"}, {"trans_id": 7, "account": 900003, "amount": -4000, "transacted_on": "2020-09-11"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: From transaction changes to account balances

Every account begins with balance zero. Each transaction’s `amount` is a signed change: positive amounts add money and negative amounts subtract money. Therefore, an account’s final balance is the sum of `amount` over all transaction rows carrying that account number.

The query needs two pieces from different tables:

- `Transactions` supplies the signed amounts and account identifier needed for aggregation;
- `Users` supplies the human-readable `name` required in the output.

The checked-in query joins these tables first, groups the joined transaction rows by account, calculates `SUM(amount)`, and keeps only sums strictly greater than 10000.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Users": [{"account": 900001, "name": "Alice"}, {"account": 900002, "name": "Bob"}, {"account": 900003, "name": "Charlie"}], "Transactions": [{"trans_id": 1, "account": 900001, "amount": 7000, "transacted_on": "2020-08-01"}, {"trans_id": 2, "account": 900001, "amount": 7000, "transacted_on": "2020-09-01"}, {"trans_id": 3, "account": 900001, "amount": -3000, "transacted_on": "2020-09-02"}, {"trans_id": 4, "account": 900002, "amount": 1000, "transacted_on": "2020-09-12"}, {"trans_id": 5, "account": 900003, "amount": 6000, "transacted_on": "2020-08-07"}, {"trans_id": 6, "account": 900003, "amount": 6000, "transacted_on": "2020-09-07"}, {"trans_id": 7, "account": 900003, "amount": -4000, "transacted_on": "2020-09-11"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Joining each transaction to its owner

The `FROM` clause is:

`Users JOIN Transactions USING (account)`.

`USING (account)` is shorthand for an equality join on the same-named `account` column in both tables. Each transaction is matched with the user whose primary-key account number equals the transaction’s account number.

Because `Users.account` is unique, one transaction can match at most one user. Thus the join attaches a name without multiplying a transaction across several user rows. After joining, each row conceptually contains the transaction’s amount together with its owner’s name and account.

This is an inner join. A user with no transactions produces no joined row. Such a user’s balance is zero because all accounts start at zero, so that user cannot satisfy a balance greater than 10000. Excluding the user early is therefore safe.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The `FROM` clause is:

`Users JOIN Transactions USING (accou... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Grouping at the account level

`GROUP BY account` places every joined transaction for the same bank account into one group. The selected aggregate

`SUM(amount) AS balance`

adds all signed changes in that group. Deposits increase the sum, transfers out decrease it, and the final sum is exactly the account balance.

The alias `balance` gives the calculated column the required output name. It is also reused in the `HAVING` clause.

Grouping by account rather than by transaction is necessary because an account may have many transactions. Grouping by name could also distinguish users under this particular contract because names are unique, but the account is the relational key shared by the tables and directly identifies the balance being calculated.

MySQL permits selecting `name` while grouping by `account` because `Users.account` is a primary key and functionally determines exactly one `Users.name`. Within any account group, all joined rows carry the same name. In database modes or systems that do not infer this functional dependency, grouping by both `account` and `name` would express the same result more explicitly.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["name", "balance"], "rows": [["Alice", 11000]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Users": [{"account": 900001, "name": "Alice"}, {"account": 900002, "name": "Bob"}, {"account": 900003, "name": "Charlie"}], "Transactions": [{"trans_id": 1, "account": 900001, "amount": 7000, "transacted_on": "2020-08-01"}, {"trans_id": 2, "account": 900001, "amount": 7000, "transacted_on": "2020-09-01"}, {"trans_id": 3, "account": 900001, "amount": -3000, "transacted_on": "2020-09-02"}, {"trans_id": 4, "account": 900002, "amount": 1000, "transacted_on": "2020-09-12"}, {"trans_id": 5, "account": 900003, "amount": 6000, "transacted_on": "2020-08-07"}, {"trans_id": 6, "account": 900003, "amount": 6000, "transacted_on": "2020-09-07"}, {"trans_id": 7, "account": 900003, "amount": -4000, "transacted_on": "2020-09-11"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["name", "balance"], "rows": [["Alice", 11000]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Aggregate transactions before joining:** A sub:** - **Aggregate transactions before joining:** A subquery can compute `SUM(amount)` per account, filter with `HAVING`, and then join the smaller qualifying result to `Users`. It expresses the same logic and may reduce join volume.
- **`LEFT JOIN` from users:** This would retain users without transactions and require `COALESCE` to treat their sum as zero. Since zero cannot exceed 10000, the checked-in inner join is simpler and sufficient.
- **Filtering with `WHERE amount > 10000`:** This is incorrect because the condition belongs to the total balance, not each transaction. It also drops negative adjustments that must be included.
- **Summing only deposits:** Negative amounts represent outgoing money and are part of the balance. Ignoring them can falsely qualify an account.
- **Balance exactly 10000:** The strict `> 10000` condition rejects it. Replacing it with `>=` would violate the statement.
- **No transactions for a user:** The inner join omits the user. Their starting balance remains zero, so omission is correct.
- **One transaction:** The account qualifies exactly when that signed amount is greater than 10000.
- **Many transactions:** Every joined row in the account group contributes once to `SUM(amount)`, regardless of date or transaction identifier.
- **Net negative balance:** The signed sum is negative and cannot pass the positive threshold.
- **Unique account key:** It prevents a transaction from joining to multiple names and makes `name` functionally dependent on the grouping column.
- **Unique names:** The contract also says names do not repeat, but the query correctly groups by account, the actual balance identity.
- **Strict SQL grouping modes:** MySQL can infer that primary-key `account` determines `name`. For portability, write `GROUP BY account, name` if the database requires every selected nonaggregate column to appear explicitly.
- **Alias use in `HAVING`:** MySQL permits `HAVING balance > 10000`. A dialect that does not allow select aliases there should repeat `SUM(amount)`.
- **`USING (account)` support:** It is standard shorthand when both inputs share the same column name. An explicit `ON Users.account = Transactions.account` is equivalent and more portable across unusual dialects.
- **Output order:** No ordering is promised or needed. Add `ORDER BY` only if a consumer imposes a separate presentation requirement.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O((U+T)\log(U+T))$. Let $U$ be the number of users and $T$ the number of transactions.
- **Auxiliary Space Complexity:** $O(U+T)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
