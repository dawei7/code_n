## General

**Attach each product's unit price to every sale**

`Sales` contains a quantity but not a price. `Product` contains one price for each unique `product_id`. To calculate money spent, the query joins the two tables with

`JOIN Product USING (product_id)`.

`USING` matches rows on the same-named product ID column. The foreign-key guarantee means every sale refers to a valid product, and Product's uniqueness means each sale receives exactly one price rather than being multiplied by duplicate product rows.

After the join, one sale row contributes

`quantity * price`

to its user's spending.

**Aggregate all sale rows belonging to one user**

A user may have many purchases, including repeated purchases of the same product and purchases of different products. The query groups by `user_id` using `GROUP BY 1`, where one refers to the first selected expression.

Within each user's group, `SUM(quantity * price)` adds the monetary contribution of every joined sale row. The alias `spending` gives this aggregate the exact requested result-column name.

For example, a user buying ten units of a product priced at 10 and one unit of a product priced at 25 has contributions 100 and 25. Grouping puts both rows together and returns spending 125.

There is intentionally no grouping by `product_id`. The task asks for one total per user across all products, so product-level groups would be too fine and would produce multiple rows per user.

**Apply the two ordering rules in priority order**

The result must place larger spending totals first. `ORDER BY 2 DESC` sorts by the second selected expression, `spending`, in descending order.

When two users have equal spending, the next key `1` refers to `user_id` and uses SQL's default ascending direction. The complete clause

`ORDER BY 2 DESC, 1`

therefore implements:

1. spending from greatest to least;
2. for equal spending, user ID from least to greatest.

Ordering keys are applied left to right. A smaller user ID never moves ahead of a user with greater spending; it matters only inside a spending tie.

**Why every returned total is exact**

Fix a user `u`. Every sale row belonging to `u` is joined with the unique price for its product, so its line amount `quantity * price` is correct. `GROUP BY user_id` places all and only `u`'s line amounts into one group. The sum is therefore exactly the total amount spent by `u`.

Each user appearing in Sales creates one group and one result row. No two users are combined because their group keys differ. The primary descending ordering arranges those exact totals as required, and the secondary ascending key resolves every tie deterministically.

Thus the query satisfies both the aggregation contract and the presentation contract.

**Ordinal references are valid but depend on select-list position**

`GROUP BY 1` means group by `user_id` because it is the first selected expression. `ORDER BY 2` means order by the aggregate aliased `spending`, and `ORDER BY ..., 1` uses `user_id`.

These ordinals are concise. Their disadvantage is maintainability: inserting or reordering select-list expressions can change their meaning. Explicit names such as `GROUP BY user_id ORDER BY spending DESC, user_id` would communicate the same logic more directly, but the exact query is correct as written.

## Complexity detail

Let `s` be the number of Sales rows and `p` the number of Product rows. Joining, grouping, and ordering can be implemented through indexes, hashes, and sorts chosen by the MySQL optimizer. A conservative general bound is `O((s + p) \log s)` time, matching the manifest, because grouped results or joined sales may require comparison-based ordering.

Intermediate join and aggregation state can use `O(s + p)` space in the general case. A hash join may build a Product lookup and a user aggregate table; a sort-based plan may use temporary rows or disk. Physical resource placement is engine-dependent, but the amount of represented data is linear.

The final output has one row per distinct user in Sales. Numeric multiplication and summation are treated as constant-time under bounded database integer types, though a production schema must choose types wide enough for large aggregate spending.

## Alternatives and edge cases

- **Correlated subquery for each user:** Select distinct users and recompute their sales total in a subquery. This can repeat work and is more complex than one grouped join.
- **Pre-aggregate quantities by product and user:** Sum quantity per user-product first, join prices, then sum per user. This is correct and may help some data shapes, but the direct grouped line amounts already express the result.
- **Group by user and product:** That reports per-product spending rather than the requested total per user.
- **Sum quantity only:** Products have different prices, so unit count is not monetary spending.
- **Sum price only:** A sale's quantity must multiply the unit price; otherwise multi-unit purchases are undercounted.
- **Order user ID before spending:** That would make user identity the primary order and violate descending spending priority.
- **Omit `DESC`:** SQL defaults to ascending, placing the lowest spenders first.
- **Omit the tie-break:** Equal-spending rows could appear in any order, failing the explicit ascending user-ID requirement.
- **Repeated purchases:** Every sale line contributes, so they are correctly accumulated into the same user group.
- **Several products:** The join attaches the right price independently to every line before the user-level sum.
- **Equal spending:** The secondary ascending user ID produces the required order.
- **One user:** The aggregation returns one row, and ordering is trivial.
- **Product without sales:** It has no joined row and correctly creates no user spending.
- **Invalid missing product row:** The foreign key excludes this. Without it, the inner join would drop the unmatched sale.
- **Duplicate Product IDs:** Uniqueness excludes them. If duplicates existed, joining would multiply sale rows and overcount.
- **Ordinal expressions:** They are correct for the current select list but should be updated if column positions change.
