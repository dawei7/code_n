## General

**Recognize that the source contains two alternatives**

The competitive file does not contain one query with two coordinated phases.
It places a `NOT IN` query immediately before a left-join query, without a
semicolon separating them. Each `SELECT` is an independent proposed solution.
As one submitted SQL script, the file is therefore malformed in the expected
single-statement interface and is likely to produce a syntax error at the
second `SELECT`.

Understanding this distinction prevents a misleading explanation. The two
statements solve the same anti-relationship problem in different ways; they
are not meant to feed data into each other. Exactly one should be retained in
an executable submission.

**First alternative: exclude IDs with `NOT IN`**

The first statement selects `Name AS Customers` from the customer table. Its
subquery collects every `CustomerId` present in `Orders`, and its outer
predicate retains a customer only when `Id` is not in that collection.

This follows directly from the relationship: an occurrence of customer ID
$x$ in `Orders.CustomerId` proves that customer $x$ ordered at least once. An
absence of $x$ means the customer never ordered. Repeated orders need no
special treatment because membership is boolean; finding the same ID several
times does not change the decision.

For the sample, the subquery produces IDs 3 and 1. Joe and Sam are excluded,
while Henry and Max remain. The projection discards IDs and exposes their
names under the required alias `Customers`.

This alternative has the standard `NOT IN` null hazard. If the subquery emits
even one `NULL`, comparisons against the list can become unknown and unmatched
customers may be filtered out. The problem's intended orders have customer
owners, but the local schema text does not explicitly state that the foreign
key is non-null. A robust general-purpose query should account for that.

**Second alternative: make missing matches visible**

The second statement begins with all `Customers` rows and left-joins `Orders`
where `Customers.Id = Orders.CustomerId`. A left join preserves every customer.
When matching orders exist, their right-side columns are populated. When no
order matches, SQL creates one joined row whose `Orders` columns are null.

The subsequent condition `Orders.CustomerId IS NULL` keeps precisely those
null-extended rows. A matched order cannot satisfy this condition under the
equality join: its `CustomerId` equals the non-null customer primary key. An
unrelated order whose `CustomerId` itself is null matches no customer, so it
does not suppress valid results. This makes the left-join alternative safer
than `NOT IN` in the presence of nullable order references.

The parentheses around `(Customers LEFT JOIN Orders ...)` do not create a
derived table and are not needed here. They merely group the join expression.
The core idea is the combination of a preserving left join and a null test on
the right side.

**Why the left-join filter is exact**

If a customer is returned, the joined row has no right-side `CustomerId`.
Because every matching order would supply that value, there can be no order
whose customer ID equals the returned customer's ID.

Conversely, if a customer has no order, the left join cannot find a match but
must still preserve the customer row. It fills the order columns with nulls,
the `IS NULL` test succeeds, and the customer's name is selected. Thus the
second alternative returns exactly the never-ordering customer rows.

**Why joining does not duplicate the final answers**

A customer with several orders creates several joined rows, but every one has
a populated `Orders.CustomerId` and is removed. A customer with no orders
creates exactly one null-extended row and is returned once. Therefore the
query needs neither grouping nor `DISTINCT`.

Filtering by `Customers.Id`, rather than by name, also respects customers with
identical names. If two different never-ordering customer rows share a name,
both rows remain. The result contract requests qualifying customer rows, not
the set of unique name strings.

**Projection and ordering**

Both alternatives use `AS Customers`, converting the source name column into
the exact output heading. Neither uses `ORDER BY`, which is appropriate because
the Reference accepts any order. Physical join or scan order must not be
treated as stable.

**Interpret the source complexity comments cautiously**

The file labels its time as $O(n^2)$ and space as $O(1)$, but neither statement
forces those bounds. A nested-loop plan without a useful index can indeed be
quadratic, while a hash anti-join or indexed lookup can be linear or nearly
linear. Likewise, hash tables, materialized subqueries, or sort buffers consume
working space. The manifest's $O(c + o)$ bounds describe an efficient plan more
faithfully than the source comments.

## Complexity detail

Let $c$ be the number of customers and $o$ the number of orders. For either
alternative, an efficient engine can build a hash structure for the order-side
IDs in $O(o)$ time and space and scan the customer side in $O(c)$ expected time.
That yields $O(c + o)$ time and $O(c + o)$ auxiliary space as recorded in the
manifest.

With an index on `Orders.CustomerId`, an optimizer may perform indexed probes;
with sorting, the cost can include logarithmic factors. A naive nested-loop
execution may take $O(co)$ time. SQL complexity is plan-dependent, so these
bounds describe the intended algorithmic strategy, not all possible engines.

## Alternatives and edge cases

- **Submit only one statement:** The stored file's adjacent `SELECT` statements are not a valid single solution; choose and terminate one query.
- **`NOT EXISTS`:** A correlated absence test states the intent directly and avoids `NOT IN`'s null semantics.
- **`NOT IN`:** Concise and correct when every subquery value is guaranteed non-null.
- **Left anti-join:** The second stored alternative is robust to unrelated null foreign-key rows and naturally exposes missing matches.
- **Pandas `isin`:** Negate membership in the order customer-ID series, then select and rename the name column.
- **Many orders for one customer:** All joined matches are filtered, so that customer never appears.
- **Duplicate customer names:** Preserve separate qualifying customer rows; do not add `DISTINCT` casually.
- **Empty `Orders`:** Every customer is returned by either valid standalone alternative.
- **Empty `Customers`:** The result is empty.
- **Nullable order reference:** Prefer the left anti-join or `NOT EXISTS`; unguarded `NOT IN` can reject everything.
- **Any order:** No sorting is required or guaranteed.
