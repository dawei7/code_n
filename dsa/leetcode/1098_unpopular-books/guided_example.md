# Guided Example: Unpopular Books

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Books": [{"book_id": 1, "name": "Kalila And Demna", "available_from": "2010-01-01"}, {"book_id": 2, "name": "28 Letters", "available_from": "2012-05-12"}, {"book_id": 3, "name": "The Hobbit", "available_from": "2019-06-10"}, {"book_id": 4, "name": "13 Reasons Why", "available_from": "2019-06-01"}, {"book_id": 5, "name": "The Hunger Games", "available_from": "2008-09-21"}], "Orders": [{"order_id": 1, "book_id": 1, "quantity": 2, "dispatch_date": "2018-07-26"}, {"order_id": 2, "book_id": 1, "quantity": 1, "dispatch_date": "2018-11-05"}, {"order_id": 3, "book_id": 3, "quantity": 8, "dispatch_date": "2019-06-11"}, {"order_id": 4, "book_id": 4, "quantity": 6, "dispatch_date": "2019-06-05"}, {"order_id": 5, "book_id": 4, "quantity": 5, "dispatch_date": "2019-06-20"}, {"order_id": 6, "book_id": 5, "quantity": 9, "dispatch_date": "2009-02-02"}, {"order_id": 7, "book_id": 5, "quantity": 8, "dispatch_date": "2010-04-13"}]}}`
- **Required output:** `{"columns": ["book_id", "name"], "rows": [[1, "Kalila And Demna"], [2, "28 Letters"], [5, "The Hunger Games"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Books`

The objective is to compute `{"columns": ["book_id", "name"], "rows": [[1, "Kalila And Demna"], [2, "28 Letters"], [5, "The Hunger Games"]]}` from `{"tables": {"Books": [{"book_id": 1, "name": "Kalila And Demna", "available_from": "2010-01-01"}, {"book_id": 2, "name": "28 Letters", "available_from": "2012-05-12"}, {"book_id": 3, "name": "The Hobbit", "available_from": "2019-06-10"}, {"book_id": 4, "name": "13 Reasons Why", "available_from": "2019-06-01"}, {"book_id": 5, "name": "The Hunger Games", "available_from": "2008-09-21"}], "Orders": [{"order_id": 1, "book_id": 1, "quantity": 2, "dispatch_date": "2018-07-26"}, {"order_id": 2, "book_id": 1, "quantity": 1, "dispatch_date": "2018-11-05"}, {"order_id": 3, "book_id": 3, "quantity": 8, "dispatch_date": "2019-06-11"}, {"order_id": 4, "book_id": 4, "quantity": 6, "dispatch_date": "2019-06-05"}, {"order_id": 5, "book_id": 4, "quantity": 5, "dispatch_date": "2019-06-20"}, {"order_id": 6, "book_id": 5, "quantity": 9, "dispatch_date": "2009-02-02"}, {"order_id": 7, "book_id": 5, "quantity": 8, "dispatch_date": "2010-04-13"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Begin with books so zero-sale books survive

The query starts from `Books` and uses a `LEFT JOIN Orders USING (book_id)`. This direction matters. A book with no matching order must still be considered, because zero sales is less than ten. An inner join would delete that book before aggregation.

For a book without orders, the joined order columns are null. The later conditional aggregate converts nonqualifying rows to zero, allowing the book’s sales total to be treated as zero.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Books": [{"book_id": 1, "name": "Kalila And Demna", "available_from": "2010-01-01"}, {"book_id": 2, "name": "28 Letters", "available_from": "2012-05-12"}, {"book_id": 3, "name": "The Hobbit", "available_from": "2019-06-10"}, {"book_id": 4, "name": "13 Reasons Why", "available_from": "2019-06-01"}, {"book_id": 5, "name": "The Hunger Games", "available_from": "2008-09-21"}], "Orders": [{"order_id": 1, "book_id": 1, "quantity": 2, "dispatch_date": "2018-07-26"}, {"order_id": 2, "book_id": 1, "quantity": 1, "dispatch_date": "2018-11-05"}, {"order_id": 3, "book_id": 3, "quantity": 8, "dispatch_date": "2019-06-11"}, {"order_id": 4, "book_id": 4, "quantity": 6, "dispatch_date": "2019-06-05"}, {"order_id": 5, "book_id": 4, "quantity": 5, "dispatch_date": "2019-06-20"}, {"order_id": 6, "book_id": 5, "quantity": 9, "dispatch_date": "2009-02-02"}, {"order_id": 7, "book_id": 5, "quantity": 8, "dispatch_date": "2010-04-13"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Apply the protected query’s release cutoff

The `WHERE` clause keeps rows satisfying `available_from < '2019-05-23'`. Because this predicate references only the Books side, it safely filters book eligibility without turning the left join into an inner join.

The strict operator is an exact detail of the protected SQL: a book first available on May 23 is excluded, while one available on May 22 is included. The local Reference contract describes old-enough books with `available_from <= '2019-05-23'`, so that boundary is broader by one date. To implement that written boundary literally, the operator would need to be `<=`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Aggregate quantities per book

`GROUP BY 1` groups by the first selected expression, `book_id`. Since `book_id` is the Books primary key, one group corresponds to one book and determines one `name`. At most one result row is emitted for each qualifying book.

The conditional expression `IF(dispatch_date >= '2018-06-23', quantity, 0)` contributes an order’s quantity when its dispatch date is on or after the lower boundary, and zero otherwise. `SUM` then totals those contributions across the book’s joined order rows.

For a book with no orders, `dispatch_date` is null. The comparison is not true, so `IF` chooses zero. The aggregate receives a numeric zero rather than only nulls, and the book can pass the threshold.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["book_id", "name"], "rows": [[1, "Kalila And Demna"], [2, "28 Letters"], [5, "The Hunger Games"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Books": [{"book_id": 1, "name": "Kalila And Demna", "available_from": "2010-01-01"}, {"book_id": 2, "name": "28 Letters", "available_from": "2012-05-12"}, {"book_id": 3, "name": "The Hobbit", "available_from": "2019-06-10"}, {"book_id": 4, "name": "13 Reasons Why", "available_from": "2019-06-01"}, {"book_id": 5, "name": "The Hunger Games", "available_from": "2008-09-21"}], "Orders": [{"order_id": 1, "book_id": 1, "quantity": 2, "dispatch_date": "2018-07-26"}, {"order_id": 2, "book_id": 1, "quantity": 1, "dispatch_date": "2018-11-05"}, {"order_id": 3, "book_id": 3, "quantity": 8, "dispatch_date": "2019-06-11"}, {"order_id": 4, "book_id": 4, "quantity": 6, "dispatch_date": "2019-06-05"}, {"order_id": 5, "book_id": 4, "quantity": 5, "dispatch_date": "2019-06-20"}, {"order_id": 6, "book_id": 5, "quantity": 9, "dispatch_date": "2009-02-02"}, {"order_id": 7, "book_id": 5, "quantity": 8, "dispatch_date": "2010-04-13"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["book_id", "name"], "rows": [[1, "Kalila And Demna"], [2, "28 Letters"], [5, "The Hunger Games"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Preaggregate the date window:** Group qualifying Orders by `book_id` first, then left join those totals to eligible Books and use `COALESCE(total, 0) < 10`. This often makes the zero-sale logic especially clear.
- **Correlated subquery:** For each book, compute the sum of its in-window orders. With an appropriate index this can be efficient, but the grouped left join is usually easier to inspect.
- **`NOT EXISTS` with grouped orders:** Exclude books whose in-window quantity reaches ten. This is possible but less direct than comparing an aggregate total.
- **Inner join:** Incorrectly removes books with zero relevant orders, even though they should qualify when old enough.
- **Date predicate in `WHERE` on Orders:** This would reject null-extended left-join rows and again lose books with no matching order unless the condition is moved into `ON` or the aggregate.
- **Exactly ten copies:** The strict `< 10` comparison excludes the book.
- **No orders:** The null joined row contributes zero through `IF`, so the book passes the sales threshold if it passes the release cutoff.
- **Only old orders:** Orders before June 23, 2018 contribute zero and do not prevent qualification.
- **Future orders:** The exact query counts them because it lacks an upper bound. Adding the closed-window upper predicate is necessary if such rows are possible.
- **Release on May 23, 2019:** The exact query excludes it because it uses `<`; the local Reference’s `<=` statement would include it.
- **Duplicate book names:** Grouping by primary-key book ID keeps distinct books separate even when names match.
- **Any result order:** Omitting `ORDER BY` is correct and avoids unnecessary sorting solely for presentation.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O((B + O) \log (B + O))$. Let $B$ be the number of Books rows and $O$ the number of Orders rows. A general sort-based join and grouping plan can take $O((B+O)\log(B+O))$ time, matching the manifest. Indexed lookup, hashing, or streaming aggregation may improve the practical plan.
- **Auxiliary Space Complexity:** $O(B + O)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
