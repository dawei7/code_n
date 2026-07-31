## General

Join `ProductPurchases` to itself on equal `user_id` values. Add the strict condition `pp2.product_id > pp1.product_id` inside the join. This creates exactly one row for every unordered pair bought by a customer: it excludes pairing a product with itself and prevents the reversed duplicate.

Group those rows by the two product identifiers. Because `(user_id, product_id)` is unique, each joined row represents one distinct customer for its pair; `COUNT(DISTINCT pp1.user_id)` nevertheless states the customer-count requirement directly and remains robust to intermediate duplication. A `HAVING` clause retains only groups whose count is at least three.

Join `ProductInfo` once for each side of the pair to obtain the categories. The price and purchase quantity columns are irrelevant: the report asks whether a customer bought both products, not how many units were bought or how expensive they were. Finish with the required descending count and ascending identifier tie-breakers.

## Complexity detail

Let $P$, $I$, and $J$ have the meanings defined in the function contract. Sorting or indexing the purchase and product tables costs $O(P\log P + I\log I)$ in a comparison-based plan. The ordered self-join emits $J$ customer-level pairs, and grouping them costs $O(J\log J)$, for $O(P\log P + J\log J + I\log I)$ time and $O(J + I)$ working space. Hash joins and hash aggregation can reduce the expected grouping work to $O(P + J + I)$ before the required result sort.

The benchmark size is $P$. Each benchmark customer buys exactly two products, so $J=P/2$ and the accepted grouped join grows near-linearly apart from indexing and aggregation. The calibrated slower query recomputes a full shared-customer join for every outer customer-level pair and therefore performs quadratic work on the same legal inputs.

## Alternatives and edge cases

- **Generate both pair directions and normalize later:** Using `LEAST` and `GREATEST` can be correct, but it creates both orientations and requires extra deduplication work that the strict inequality avoids.
- **Correlated count per outer pair:** This can express the result, but repeatedly rescanning purchases for every outer row leads to quadratic work on the benchmark.
- **Exactly three shared customers:** The pair qualifies because the threshold is inclusive.
- **Only two shared customers:** The pair must be removed by `HAVING`, even when both customers bought large quantities.
- **One customer buys many products:** Every unordered combination of that customer's products must be generated once.
- **Repeated quantities:** `quantity` does not affect `customer_count`; the table's unique key already guarantees one purchase row per customer and product.
- **Product order:** The smaller identifier must always be `product1_id`, independent of purchase order.
- **Output ties:** Equal counts are ordered by `product1_id` and then `product2_id`, both ascending.
