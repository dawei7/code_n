## General
**Attach product names to purchases:** Join `Sales` with `Product` on `product_id`. Filtering by numeric identifiers alone would assume which rows represent `S8` and `iPhone`; the contract identifies them by `product_name`.

**Summarize both conditions per buyer:** Group the joined rows by `buyer_id`. A conditional sum counts rows named `S8`, and another counts rows named `iPhone`. Keep a group only when the first count is positive and the second equals zero.

Every retained buyer has witnessed at least one `S8` row and no `iPhone` row by the two `HAVING` predicates. Conversely, any buyer satisfying the requested purchase history has a positive first count and zero second count, so that buyer's group is retained exactly once. Other product names contribute zero to both counts and cannot change eligibility.

## Complexity detail
A hash join can build a $P$-row product lookup and process $R$ sales in expected $O(P+R)$ time. Sort-based grouping and deterministic output ordering can add $O(R\log R)$ time. Join, grouping, and sort state use up to $O(P+R)$ execution space; indexes and the optimizer may choose another plan.

## Alternatives and edge cases
- **Set difference:** Select distinct `S8` buyers and subtract distinct `iPhone` buyers. It directly models the condition but may require two scans or engine-specific set syntax.
- **Correlated anti-subquery:** Start with `S8` purchases and test separately for an `iPhone` purchase per buyer. It is correct but can repeatedly rescan sales without a suitable index.
- **Filter out iPhone rows before grouping:** It is incorrect because deleting the disqualifying evidence can make an iPhone buyer appear eligible.
- **Several S8 purchases:** Return the buyer once, not once per sale.
- **S8 plus other products:** The buyer remains eligible unless one of those products is `iPhone`.
- **iPhone without S8:** The buyer does not qualify.
- **Product identifiers:** Resolve names through `Product`; do not assume fixed IDs for the named products.
