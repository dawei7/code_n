## General

**Translate “never ordered” into set exclusion**

The two tables describe opposite sides of one relationship. `Customers.id` is
the unique identifier of a registered customer, while `Orders.customerId`
records which customer placed an order. A customer has ordered something when
that customer's ID occurs at least once in the order table. Consequently, a
customer has never ordered when the ID does not occur there at all.

This reformulation is important because the required output is not an order
count. It is an anti-membership question: retain rows from `Customers` for
which no related row exists in `Orders`.

**Construct the set of IDs that have ordered**

The inner query selects `customerId` from every order. Conceptually, this is
the collection of customer IDs that must be excluded:

`SELECT customerId FROM Orders`

Several orders may belong to the same customer, so the collection can contain
duplicates. Those duplicates do not affect membership. If ID 3 appears once
or one hundred times, the outer condition still learns the same fact: customer
3 has placed at least one order. For that reason, the subquery does not need a
`DISTINCT` operation.

**Keep IDs absent from that collection**

The outer query scans customer rows and evaluates `id NOT IN (...)`. A row
survives exactly when its ID is not among the IDs produced by the inner query.
The row's name is then projected as the answer.

The alias in `name AS Customers` is part of the result contract. The source
column is named `name`, but the requested one-column table must be headed
`Customers`. The alias changes result metadata, not the stored value.

**Walk through the example**

The order table contains `customerId` values 3 and 1. The conceptual exclusion
set is therefore `{1, 3}`.

- Joe has ID 1, which is in the set, so Joe is removed.
- Henry has ID 2, which is absent, so Henry remains.
- Sam has ID 3, which is in the set, so Sam is removed.
- Max has ID 4, which is absent, so Max remains.

Projecting and renaming the surviving names produces Henry and Max under the
column `Customers`. Their relative order is immaterial because the Reference
allows any order.

**Why the membership test selects exactly the intended rows**

Suppose a customer is returned. The `NOT IN` predicate succeeded, so no value
emitted by the order subquery equals that customer's ID. Since every order
stores its owner in `customerId`, no order belongs to this customer.

Now suppose a customer has never placed an order. No order row can contain
that customer's ID, so the ID is absent from the subquery result and the outer
predicate retains the row. These two directions show that, under ordinary
two-valued membership behavior, the returned names are neither too many nor
too few.

**The important SQL `NULL` qualification**

SQL predicates use three-valued logic. If the subquery contains a `NULL`, then
an expression such as `2 NOT IN (1, NULL)` evaluates to unknown rather than
true. A `WHERE` clause discards unknown, potentially causing every otherwise
unmatched customer to disappear.

The local description calls `customerId` a foreign key and describes each
order as belonging to a customer, but it does not explicitly spell out a
`NOT NULL` constraint. The stored solution therefore relies on the intended
problem data having a real customer ID in every order row. If nullable foreign
keys had to be supported, `NOT EXISTS` or a left anti-join would express the
meaning safely without this trap.

**Why customer names need not be unique**

Filtering is performed with the primary key `id`, not with `name`. Two
different customers may share a name and still have different order histories.
Each qualifying customer row produces one output row. If two never-ordering
customers have the same name, the output can legitimately contain that name
twice; adding `DISTINCT name` would silently change the row-based contract.

**Why there is no ordering clause**

The query contains no `ORDER BY`, which exactly matches the any-order
requirement. A database may happen to return primary-key order for one plan,
but that observation is not a guarantee and must not become part of the
algorithm's reasoning.

## Complexity detail

Let $c$ be the number of rows in `Customers` and $o$ the number of rows in
`Orders`. An engine can materialize or hash the order IDs in $O(o)$ time and
$O(o)$ space, then test all customers in $O(c)$ expected time. This gives the
manifest bounds $O(c + o)$ time and $O(c + o)$ space.

SQL text specifies a relational result, not one mandatory physical plan. An
optimizer may instead use an index, transform `NOT IN` into an anti-join, or
choose a less efficient nested strategy. Appropriate indexes can reduce extra
memory, while a naive repeated scan can approach $O(co)$ time. The manifest
describes the intended efficient execution class rather than a promise about
every database configuration.

## Alternatives and edge cases

- **Correlated `NOT EXISTS`:** Test that no order has `customerId = Customers.id`; this is explicit anti-membership and remains safe when unrelated nulls occur.
- **Left anti-join:** Left-join orders and retain rows whose right-side key is null; often clear to beginners and optimizer-friendly.
- **Pandas exclusion:** Use negated `isin` on customer IDs, then select and rename `name`, as the local editorial demonstrates.
- **Duplicate orders:** Repeated order IDs for one customer do not change membership, so no `DISTINCT` is necessary.
- **Duplicate customer names:** Filter by ID and preserve one result row per qualifying customer rather than deduplicating names.
- **No orders:** With an empty subquery, every customer qualifies.
- **Every customer ordered:** Every ID is excluded, producing an empty table.
- **No customers:** There are no outer rows to return.
- **Nullable `customerId`:** A null can poison `NOT IN`; prefer `NOT EXISTS` unless non-nullness is guaranteed.
- **Any result order:** Do not add sorting unless a separate presentation requirement asks for it.
