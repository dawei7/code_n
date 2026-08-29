## General

The result is about **customers and categories**, but the purchase table is recorded at the finer level of customers and products. A customer may buy several products from the same category. Counting those rows directly would overcount that customer, so the query first converts the raw data into one membership row per `(user_id, category)`. It then forms category pairs within each customer and finally counts how many customers support each pair.

The two common table expressions make those stages explicit:

1. `user_category` builds unique customer-category memberships.
2. `pair_per_user` builds each customer’s unordered category pairs exactly once.

The outer query aggregates, filters, and orders those pairs.

**Stage 1: translate products into category memberships**

`ProductPurchases JOIN ProductInfo USING (product_id)` matches every purchased product with its category. `USING (product_id)` is appropriate because both tables use the same join-column name, and `ProductInfo.product_id` uniquely identifies one product description.

Only `user_id` and `category` are selected. The purchased `quantity` does not affect whether the customer bought from a category: buying one unit or many units creates the same membership. The product `price` is also irrelevant to the requested count.

The crucial word is `DISTINCT`:

`SELECT DISTINCT user_id, category`

Suppose one customer bought two different book products, or has multiple qualifying product rows that map to Books. After the join, Books could appear more than once for that user. `DISTINCT` collapses those rows into one `(user, Books)` membership. This ensures later work counts a customer’s presence in a category, not the number of products or purchases.

After this CTE, it is helpful to imagine each customer owning a set of categories. For example, a customer associated with Books, Clothing, and Electronics contributes exactly those three set members.

**Stage 2: create each unordered pair once per customer**

`pair_per_user` joins `user_category` to itself. Aliases `a` and `b` represent two category memberships belonging to the same customer. The first join condition,

`a.user_id = b.user_id`,

prevents categories belonging to different customers from being paired.

The second condition,

`a.category < b.category`,

does three jobs at once:

- it prevents pairing a category with itself;
- it chooses one canonical orientation for an unordered pair;
- it prevents both `(Books, Clothing)` and `(Clothing, Books)` from appearing.

The comparison follows the database’s string collation, which is also the natural mechanism used by the final lexicographic ordering. The smaller category becomes `category1` and the larger becomes `category2`.

If one user has `c` distinct categories, this self-join emits exactly

$$
\binom{c}{2} = \frac{c(c-1)}{2}
$$

rows for that user. Because `user_category` was deduplicated first, each particular `(user_id, category1, category2)` combination occurs once.

For a user with Books, Clothing, and Electronics, the generated rows are Books-Clothing, Books-Electronics, and Clothing-Electronics. No reverse pairs and no same-category pairs are generated.

**Stage 3: count shared customers**

The outer query groups rows by `category1` and `category2`. Every row in one group represents a customer who belongs to both categories, so

`COUNT(DISTINCT user_id) AS customer_count`

gives the number of unique shared customers.

Given the preceding `DISTINCT` and strict pair construction, each user already contributes at most one row to a particular pair. Thus plain `COUNT(*)` would be equivalent for this exact query. Keeping `COUNT(DISTINCT user_id)` makes the intended business meaning explicit and protects the count if the earlier CTE is later changed in a way that reintroduces duplicates.

`GROUP BY 1, 2` is positional shorthand for grouping by the first and second selected expressions, namely `category1` and `category2`.

**Stage 4: keep only reportable pairs**

The threshold applies after customers have been counted, so it belongs in `HAVING` rather than `WHERE`:

`HAVING customer_count >= 3`.

`WHERE` filters individual input rows before aggregation and cannot express a condition on the completed group count. In MySQL, the alias `customer_count` is available in `HAVING`, so the query can use the readable alias instead of repeating the aggregate expression.

Pairs supported by one or two customers are removed. A pair supported by exactly three customers remains because the condition is inclusive.

**Stage 5: apply every requested tie-breaker**

`ORDER BY 3 DESC, 1, 2` uses select-list positions:

- column 3, `customer_count`, descending;
- column 1, `category1`, ascending by default;
- column 2, `category2`, ascending by default.

This exactly implements the required priority. Higher shared-customer counts come first. When counts tie, `category1` decides; if that also ties, `category2` decides.

The final table contains only the two canonical category names and the number of distinct customers common to them. No purchase quantity, product, price, or user detail leaks into the output.

## Complexity detail

SQL complexity depends on indexes, join algorithms, collation, whether common table expressions are materialized, and whether `DISTINCT`, grouping, and ordering use hashing or sorting. The query text specifies the relational operations but does not force one physical execution plan.

For a useful output-sensitive description, let `P` be the number of rows produced by joining purchases to product information, `U` the number of distinct `(user, category)` memberships, `J` the number of per-user category-pair rows, and `I` the number of category-pair groups that survive or reach the final ordering stage.

With sort-based implementations, deduplicating the joined memberships can cost `O(P \log P)`, grouping the `J` generated pair rows can cost `O(J \log J)`, and ordering `I` aggregate rows costs `O(I \log I)`. This gives the manifest-style bound

$$
O(P\log P + J\log J + I\log I),
$$

in addition to the underlying table scan and join work. Hash-based distinct and aggregation can reduce the expected deduplication and grouping portions toward linear time, while the final ordered result still requires sorting unless an execution plan can supply the order another way.

The potentially dominant quantity is `J`. If user `u` belongs to `c_u` distinct categories, then

$$
J = \sum_u \binom{c_u}{2}.
$$

This is inherent to explicitly producing every category pair supported by every customer.

Materializing the stages can require `O(U + J + I)` working space for unique memberships, generated pair rows, and aggregate/output rows. A database engine may pipeline, spill, or use indexes to change peak memory, so this is a logical upper-bound description rather than a guarantee about a particular server’s physical memory plan.

## Alternatives and edge cases

- **Correlated existence checks:** One could enumerate category pairs and test how many users have purchases in both categories, but repeated scans or correlated subqueries tend to do much more work than building memberships and grouping once.
- **Conditional aggregation:** Pivoting categories into columns can count co-occurrence for a small fixed category set, but categories here are data values rather than a fixed schema, so a self-join is the general solution.
- **Skip the membership deduplication:** Joining raw purchase rows to themselves would multiply combinations when a customer owns several products in one category. Even `COUNT(DISTINCT user_id)` could recover the final count, but the intermediate join could become dramatically larger.
- **Use `COUNT(*)`:** It is correct after the exact `DISTINCT user_id, category` CTE because one user-pair row is unique. `COUNT(DISTINCT user_id)` communicates the contract more defensively.
- **Canonical pair orientation:** The strict condition `a.category < b.category` is essential. Using inequality alone would generate both orientations; using `<=` would also generate same-category pairs.
- **Exactly three customers:** Such a pair passes because `HAVING` uses `>= 3`.
- **A customer in only one category:** That user creates no row in `pair_per_user`, which is correct because one category cannot form a pair.
- **Several products in one category:** `DISTINCT` reduces them to one membership, so they do not inflate `customer_count`.
- **Quantities and prices:** Neither changes whether a customer has purchased from a category, so excluding them is intentional.
- **No reportable pairs:** After `HAVING`, the query returns an empty result table, which is the correct representation.
- **String collation:** Both `<` and the ascending order use the database collation. If a system requires a specific case-sensitive or locale-specific lexical definition, the query would need an explicit collation; the supplied category data and MySQL environment define the intended behavior here.
- **Positional clauses:** `GROUP BY 1, 2` and `ORDER BY 3 DESC, 1, 2` are concise but depend on select-column order. Naming the expressions explicitly would be more resilient to later reordering without changing the algorithm.
