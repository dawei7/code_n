## General

**Start from every product, not from every discount.** The output must contain one row for each row of `Products`, including products whose category has no entry in `Discounts`. That requirement determines the join direction. The query writes `Products LEFT JOIN Discounts USING (category)`, so every product survives. When a category exists in both tables, the matching discount is attached. When no match exists, the joined `discount` value is SQL `NULL` rather than the product row disappearing.

An inner join would be wrong for the same reason: it would silently remove an undiscounted product such as the example's `Home` item. A right join would preserve discounts that have no products, which are irrelevant output rows. The left join exactly matches the “all products, optional discount” relationship.

**Why one join match cannot duplicate a product.** `Discounts.category` is the table's primary key, so at most one discount row has a given category. Each product therefore joins to zero or one discount row. Even if many products share a category, each product gets the same single category discount and still produces exactly one result row. This schema guarantee is what makes the plain join sufficient; no grouping or deduplication is needed.

The `USING (category)` syntax is shorthand for an equality join on the same-named `category` column. It also exposes one merged `category` column rather than two separately qualified copies. The output selects that category along with `product_id` and the calculated price.

**Convert a percentage discount into a multiplier.** A discount of $d$ percent means the customer pays $100-d$ percent of the original price. Therefore the final price is

$$
\text{price}\cdot\frac{100-d}{100}.
$$

The SQL expression is `price * (100 - COALESCE(discount, 0)) / 100`. For a $10$ percent discount, the multiplier is $90/100$, and a price of $1000$ becomes $900$. For a $100$ percent discount, the multiplier is zero. For a zero percent discount, it is one.

**Treat a missing row as zero discount.** A product without a matching category has `discount = NULL` after the left join. SQL arithmetic involving `NULL` normally produces `NULL`, which would not mean “unchanged price.” `COALESCE(discount, 0)` returns the first non-`NULL` argument, substituting zero only when the joined discount is missing. The same formula then yields `price * 100 / 100`, preserving the price.

This use of `COALESCE` is different from converting an actual zero discount: both yield zero numerically, but one came from a present row and one from the absence of a row. The output does not need to distinguish them, so combining those cases is correct.

**Name and order the result.** The calculated expression has the alias `final_price`. MySQL permits an alias without the optional `AS` keyword, so `... / 100 final_price` is valid. The selected columns are, in order, `product_id`, `final_price`, and `category`.

`ORDER BY 1` means order by the first expression in the select list, which is `product_id`. Ascending is SQL's default ordering direction, so the result satisfies the required increasing product-ID order. Writing `ORDER BY product_id ASC` would be more explicit but would produce the same result.

**Why the query is complete.** Take any product row. The left join preserves it. If its category has a discount, primary-key uniqueness supplies exactly that percentage and the arithmetic applies it. If its category has no discount, `COALESCE` supplies zero and the price is unchanged. Thus every required product appears exactly once with the right calculated price. Finally, ordering changes only row presentation, not values or membership, and puts those rows in the required sequence.

The calculation retains SQL numeric semantics. Because `price` is declared `decimal`, MySQL performs decimal arithmetic rather than intentionally rounding to a whole integer. If a percentage creates a fractional result, the scale and display depend on MySQL's decimal-expression rules and the input column's declared precision and scale. The query should not insert an unrequested `ROUND`, because the problem asks for the arithmetic result and does not specify rounding.

## Complexity detail

Let $P$ be the number of rows in `Products` and $D$ the number in `Discounts`. Logical query complexity depends on the execution plan and available indexes. A typical plan can index or hash the primary-key categories and match all products in $O(P+D)$ expected work, then sort the $P$ output rows by `product_id` in $O(P\log P)$ time. This gives the safe overall characterization $O(P+D+P\log P)$, commonly summarized by the manifest as $O((P+D)\log(P+D))$.

If `Products.product_id` has a usable unique-key index and the optimizer scans it in order, the explicit sort may be avoided; physical database costs are therefore plan-dependent. Materializing a hash table and sorting result rows can use $O(P+D)$ working space, while an index-nested-loop plan may use less. The returned result itself contains $P$ rows. SQL complexity statements describe a representative upper-bound plan, not a guarantee that MySQL must implement the relational expression in one particular way.

## Alternatives and edge cases

- **Inner join:** This incorrectly drops products whose categories have no discount, directly violating the unchanged-price requirement.
- **Correlated scalar subquery:** Looking up the discount separately for every product can express the same logic, but it is less direct and may lead to repeated lookups unless the optimizer rewrites it.
- **`CASE WHEN discount IS NULL`:** A `CASE` expression can substitute zero or return `price` explicitly. `COALESCE` is shorter and communicates the missing-value fallback precisely.
- **Subtracting the discount amount:** `price - price * discount / 100` is algebraically equivalent for matched rows, but it still needs a `NULL` fallback. The multiplier form handles matched and unmatched rows uniformly.
- **No matching discount:** The left join produces `NULL`, `COALESCE` converts it to zero, and the formula returns the original price.
- **Zero-percent discount:** The joined row exists, but the formula also returns the original price. No special branch is needed.
- **One-hundred-percent discount:** `100 - discount` becomes zero, so `final_price` is zero as expected.
- **Many products in one category:** Primary-key uniqueness in `Discounts` lets all of them reuse one discount without multiplying rows.
- **Discount category with no product:** Starting from `Products` means such a discount generates no output, which is correct because the result is about products.
- **Fractional decimal result:** The exact query does not round. Adding `ROUND` or converting to an integer would impose behavior absent from the contract.
- **`ORDER BY 1` maintainability:** It is valid and exact here, but reordering select columns could silently change the sort key. `ORDER BY product_id ASC` is clearer in evolving production SQL.
- **`NULL` product category:** The documented schema does not state such rows are possible. Under ordinary SQL equality semantics, `NULL` would not match another `NULL` category and would therefore receive zero discount through `COALESCE`.
