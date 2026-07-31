## General

Join `ProductPurchases` to `ProductInfo` and retain only distinct `(user_id, category)` rows. This deduplication is essential: one customer may buy several products from the same category, but that category must contribute only one membership for that customer.

Self-join the membership relation on equal `user_id` values and require `a.category < b.category`. The strict lexical inequality excludes pairing a category with itself and generates exactly one orientation of every unordered pair. Because each side was already deduplicated, every joined row now represents one unique customer for one category pair.

Group by the two category names and use `COUNT(*)` to obtain the shared-customer count. The inclusive `HAVING COUNT(*) >= 3` condition keeps reportable pairs. Finish with descending count and the two ascending lexical tie-breakers required by the contract.

## Complexity detail

Let $P$, $I$, $U$, and $J$ have the meanings defined in the function contract. In a comparison-based plan, joining and deduplicating purchases costs $O(P\log P + I\log I)$, while grouping the $J$ generated customer-level category pairs costs $O(J\log J)$. Total time is $O(P\log P + J\log J + I\log I)$ and working space is $O(U + J + I)$. Hash joins, hash deduplication, and hash aggregation can make the corresponding stages expected-linear before the required final result sort.

The benchmark size is $P$. Every benchmark user contributes exactly two category memberships, so $U=P$ and $J=P/2$. The accepted grouped join processes that relation once, while the calibrated slower query recomputes the shared-customer count for each outer customer-level pair.

## Alternatives and edge cases

- **Join purchases directly without deduplication:** This overcounts a customer who bought multiple products from either category.
- **Generate both pair orientations:** Using unequal categories without a strict ordering produces both `(A,B)` and `(B,A)` and requires an extra normalization step.
- **Correlated shared-count subquery:** It can produce correct results but may repeatedly rescan the membership relation for every outer pair, yielding quadratic work on the benchmark.
- **Exactly three customers:** The pair qualifies because the reporting threshold is inclusive.
- **Two shared customers:** The pair must be absent regardless of their quantities or spending.
- **One customer in many categories:** Every unordered combination of that customer's distinct categories contributes once.
- **Several products in one category:** They collapse to one customer-category membership before pairs are formed.
- **Output ties:** Equal counts are ordered by `category1` and then `category2`, both lexicographically ascending.
