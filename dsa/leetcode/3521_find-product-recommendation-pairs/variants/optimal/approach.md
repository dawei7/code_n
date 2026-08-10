## General

**Interpret a purchase row as customer-product presence**

`ProductPurchases` has a unique key on `(user_id, product_id)`. Therefore, a user has at most one row for a particular product. `quantity` tells how many units were purchased, but recommendation eligibility depends only on whether the customer purchased both products, not on units. The query correctly does not use `quantity`.

The central task is to turn each customer's purchased products into distinct unordered pairs, count how many users generated each pair, keep counts of at least three, and attach the two product categories.

**Self-join purchases by the same user**

The query gives `ProductPurchases` two aliases, `pp1` and `pp2`, and joins them on:

`pp2.user_id = pp1.user_id`.

This creates combinations of two products bought by the same customer. A user who bought `d` distinct products could otherwise produce ordered pairs in both directions and pairs of a product with itself.

The additional predicate:

`pp2.product_id > pp1.product_id`

solves both problems:

- strict inequality excludes self-pairs;
- greater-than fixes the canonical orientation `product1_id < product2_id`;
- each unordered pair for one user appears once rather than as both `(a,b)` and `(b,a)`.

Because `(user_id, product_id)` is unique, one user cannot produce duplicate joined rows for the same canonical pair. This property is central to the customer count.

**Attach each side's category independently**

The joined purchase aliases contain product IDs but not categories. The query joins `ProductInfo` twice:

- `pi1.product_id = pp1.product_id` supplies `product1_category`;
- `pi2.product_id = pp2.product_id` supplies `product2_category`.

`product_id` is the primary key of `ProductInfo`, so each dimension join matches at most one row and does not multiply co-purchase rows. The selected categories therefore correspond to the correct side of the ordered pair.

`price` is not part of the requested output or eligibility rule, so it is intentionally unused.

**Group all customers for the same product pair**

After the joins, each logical row means:

“this one user bought `pp1.product_id` and `pp2.product_id`.”

The query groups by both product IDs and both selected category values. All users contributing the same ordered product pair enter the same group.

It computes:

`COUNT(DISTINCT pp1.user_id) AS customer_count`.

The `DISTINCT` expresses the business rule directly: count different customers, never purchase rows. Under the supplied keys, it is also defensive redundancy. The purchase self-join produces at most one row per user and pair, and the primary-key information joins do not duplicate it, so `COUNT(*)` would have the same result under the contract. Keeping `DISTINCT` protects the intended meaning visibly.

**Filter groups, not individual rows**

The rule requires at least three different customers for a product pair. This count exists only after aggregation, so the query uses:

`HAVING COUNT(DISTINCT pp1.user_id) >= 3`.

`WHERE` would be the wrong stage because no single co-purchase row knows its pair's final customer count. `HAVING` filters completed groups and keeps the inclusive boundary: exactly three customers qualifies.

**Apply the full ordering contract**

The final rows are ordered by:

1. `customer_count DESC`, placing the most frequent co-purchases first;
2. `product1_id ASC` for ties;
3. `product2_id ASC` for any remaining ties.

The selected aliases can be referenced in the `ORDER BY` clause. Because the pair orientation is already canonical, the two ID tie-breakers are deterministic and match the requested result.

**Trace one customer's contribution**

If user 4 purchased products `101`, `102`, `103`, and `104`, the self-join with strict greater-than generates exactly:

`(101,102), (101,103), (101,104), (102,103), (102,104), (103,104)`.

It does not generate `(102,101)` or `(101,101)`. Each pair receives one user-4 contribution. When rows from all users are grouped, pairs such as `(101,102)` accumulate their distinct customer counts. Only after that accumulation does the threshold of three apply.

**Why the result is correct**

For every output group, each underlying joined row proves that its user bought both named products, the inequality proves the IDs are ordered and distinct, and the distinct aggregate gives exactly the number of such users. The `HAVING` clause proves every returned pair meets the recommendation threshold. Dimension joins provide the unique categories, and final sorting satisfies all ordering rules.

Conversely, take any eligible product pair `(a,b)` with `a < b`. Every customer who bought both has one `pp1` row for `a` and one `pp2` row for `b`, so the self-join creates one row for that customer and pair. Grouping collects all of them, its count is at least three, and the pair survives `HAVING`. Therefore no eligible pair is omitted.

## Complexity detail

Let `P` be the number of `ProductPurchases` rows, `I` the number of `ProductInfo` rows, and:

`J = sum over users u of C(d_u, 2)`,

where `d_u` is the number of distinct products purchased by user `u`. `J` is the logical number of canonical same-user co-purchase rows generated by the self-join.

Actual SQL cost depends on indexes, statistics, join algorithms, and whether grouping uses hashing or sorting. With sort-based processing, organizing purchases and information rows, materializing or streaming `J` joined combinations, aggregating them, and sorting result groups supports the manifest-style bound `O(P log P + J log J + I log I)`. With useful indexes and hash aggregation, some stages can be closer to linear expected time.

The unavoidable logical workload can still be large: one customer purchasing many products contributes quadratically many pairs. No query can output or aggregate those pair relationships without accounting for that `J` cardinality in some form.

Intermediate join and aggregation state can require `O(J + I)` space in a materializing plan, matching the manifest. A streaming or indexed database plan may use less memory and temporary disk. The final result has at most the number of distinct product pairs.

## Alternatives and edge cases

- **Join with product IDs not equal:** `pp1.product_id <> pp2.product_id` would create both orientations. It would require a later normalization and could double counts if handled carelessly.
- **Use less-than instead of greater-than:** `pp1.product_id < pp2.product_id` is logically equivalent. The protected predicate expresses the same canonical orientation from the second alias.
- **Group by user first:** One can derive each user's product pairs in a CTE and aggregate afterward. The direct self-join already performs that relational expansion.
- **Count purchase quantities:** Summing `quantity` would answer a different question. Eligibility is based on distinct customers who bought both products.
- **COUNT(*) under declared keys:** It would equal the distinct-user count because each user-product row and each ProductInfo row is unique. `COUNT(DISTINCT ...)` makes the business requirement robust and explicit.
- **Filter with WHERE:** Aggregate thresholds belong in `HAVING`. `WHERE` filters source rows before customer counts exist.
- **Customer bought only one product:** That user creates no self-join row and contributes to no recommendation pair.
- **Customer bought exactly two products:** The user contributes exactly one canonical pair.
- **Exactly three customers:** The inclusive `>= 3` condition keeps the pair.
- **Multiple quantities in one row:** Quantity does not create repeated customer contributions.
- **Missing ProductInfo row:** The inner joins would omit any pair side lacking product information. The schema normally implies referenced products are represented; if not, left joins would be needed to retain unknown categories, but that is not the protected query.
- **Same category on both products:** Products remain a valid distinct pair; category equality does not affect grouping or eligibility.
- **Tied customer counts:** Ascending product IDs supply the required deterministic order.
- **ProductInfo price:** It is deliberately ignored because neither output nor filtering uses it.
- **Data violating the unique purchase key:** Duplicate user-product rows could multiply the self-join. `COUNT(DISTINCT user_id)` would still protect the aggregate count, although join work would grow.
