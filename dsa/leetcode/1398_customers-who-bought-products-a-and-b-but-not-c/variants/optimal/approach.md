## General

**Create one group per customer**

The output needs customer identity and name, while qualification depends on all orders belonging to that customer. The query starts from `Customers` and left-joins `Orders` by their shared `customer_id`. This expands each customer into zero or more joined order rows.

`GROUP BY 1` groups by the first selected expression, `customer_id`. Since customer ID is unique in `Customers`, `customer_name` is functionally determined by the group and can be selected alongside it.

The group is the right unit of reasoning: the query must answer whether products A, B, and C occur anywhere in the complete purchase history, not whether one individual order row qualifies.

**Turn Boolean conditions into counts**

In MySQL, a comparison such as `product_name = 'A'` evaluates to one when true and zero when false. Summing it across a customer group therefore counts that customer's orders for A.

The three `HAVING` conditions express the contract directly:

- `SUM(product_name = 'A') > 0` means at least one A purchase exists.
- `SUM(product_name = 'B') > 0` means at least one B purchase exists.
- `SUM(product_name = 'C') = 0` means no C purchase exists.

Repeated A or B orders merely make a positive sum larger; the greater-than-zero test still represents presence. Other products contribute zero to all three sums and do not affect eligibility.

Using `COUNT(product_name = 'A')` would be wrong. `COUNT` counts non-null expression results, and both true and false Boolean results are non-null. It would count almost every order rather than only A orders.

**Why filtering belongs in `HAVING`**

`WHERE` filters individual rows before grouping. If C rows were removed there, a customer who did buy C could appear to have no C purchase and qualify incorrectly. `HAVING` runs after aggregation and can inspect the complete group's three conditional counts.

Similarly, requiring A and B in a row-level `WHERE` cannot work because one order row has only one `product_name`. The conditions describe the set of rows together.

**What the left join does for customers without orders**

A left join preserves a customer even when no order matches, producing one null-extended joined row. Comparisons such as `NULL = 'A'` evaluate to null, and `SUM` over only null values returns null. The tests `NULL > 0` and `NULL = 0` are not true, so the customer is excluded.

An inner join would produce the same final qualifying customers because anyone with both A and B necessarily has orders. The left join makes the customer-driven output model explicit and safely retains all customers until group qualification.

**Following the sample**

Daniel's group contains A, B, D, and C. The A and B sums are positive, but the C sum is also positive, so the third condition fails.

Elizabeth's group contains A, B, and D. Its conditional sums for A, B, and C are one, one, and zero. All three conditions pass, so her ID and name are returned.

Jhon has only C, and Diana has only A. Each fails at least one required positive test.

**Ordering and projection**

The outer select contains exactly `customer_id` and `customer_name`. Aggregate counts are used only to filter and do not appear in the result.

`ORDER BY 1` sorts by the first selected expression, customer ID, meeting the explicit ascending-order requirement. As with positional grouping, `ORDER BY customer_id` would be more descriptive but equivalent here.

**Why the query is correct**

For each customer, the three sums equal the numbers of A, B, and C orders in that customer's full joined group. The `HAVING` conjunction passes exactly when the first two counts are positive and the third is zero, which is precisely the qualification rule. Grouping yields at most one output row per unique customer ID, and ordering arranges those exact qualifying rows by ID. Therefore the result is complete and contains no invalid customer.

## Complexity detail

Let $C$ be the customer count, $O$ the order count, and $R$ the result size. Under a standard hash-join and hash-aggregation plan, scanning both inputs and updating customer aggregates takes expected $O(C+O)$ time. Producing results costs $O(R)$. This matches the manifest's $O(C+O+R)$ logical work.

The required `ORDER BY` may add $O(R\log R)$ time if no plan or index already yields qualifying customer IDs in order. Hash structures can use $O(C)$ aggregation state plus join lookup storage; the manifest summarizes auxiliary space as $O(C)$. Physical SQL costs vary with indexes and optimizer choices.

## Alternatives and edge cases

- **Three `EXISTS` predicates:** Require an A order, require a B order, and reject an existing C order. With indexes this is clear and can short-circuit, though it repeats correlated lookups.
- **Set intersection and difference:** Build customer-ID sets for A, B, and C, then compute $A\cap B\setminus C$. It expresses the set logic directly but needs joins to recover names.
- **Inner join:** It is sufficient for the final answer because qualification requires orders, but the left join makes customer preservation explicit.
- **Filter C in `WHERE`:** This is incorrect because it erases evidence that should disqualify a customer.
- **Repeated A or B purchases:** Positive-sum conditions remain true and output still has one grouped row.
- **Repeated C purchases:** Any positive C count disqualifies the customer.
- **Other products:** Their comparisons are all false and they do not change the three conditions.
- **No orders:** Null aggregate comparisons do not pass, so the customer is excluded.
- **Only A or only B:** One required positive sum fails.
- **A, B, and C:** The C-zero condition fails even though both required products exist.
- **Unique customer ID:** It makes the selected name functionally dependent on `GROUP BY customer_id`.
- **Positional clauses:** `GROUP BY 1` and `ORDER BY 1` refer to `customer_id`; explicit column names are safer during future edits.
- **Required order:** The final sort is necessary because grouping alone does not promise customer-ID order.
