## General

**Resolve product identifiers to names**

`Sales` records what each buyer purchased using `product_id`, while the conditions are stated using names `S8` and `iPhone`.

The query joins:

```sql
FROM
    Sales
    JOIN Product USING (product_id)
```

`Sales.product_id` is a foreign key and `Product.product_id` is a primary key. Every sale matches exactly one product row, so the join attaches one trustworthy `product_name` without losing or multiplying sales.

Other product attributes, such as unit price, do not affect eligibility.

**Group complete purchase history by buyer**

The query selects `buyer_id` and uses:

```sql
GROUP BY 1
```

One refers to the first select-list expression, so this is equivalent to `GROUP BY buyer_id`.

Every joined purchase row for one buyer enters the same group. This is the right grain because eligibility depends on whether anything in the buyer's entire history matches either product name.

Repeated sales remain inside the group but cannot create repeated result rows. Grouping returns at most one row per buyer.

**Turn name comparisons into numeric indicators**

In MySQL, a Boolean equality expression used numerically evaluates to one when true and zero when false.

Therefore:

```sql
product_name = 'S8'
```

is one for an S8 purchase and zero for every other product.

Summing it:

```sql
SUM(product_name = 'S8')
```

counts how many S8 sale rows the buyer has. The exact count is not required, but whether it is positive establishes existence.

The same technique counts iPhone rows:

```sql
SUM(product_name = 'iPhone')
```

Purchases of G4 or any other product contribute zero to both sums and do not affect the decision.

**Require at least one S8**

The first `HAVING` condition is:

```sql
SUM(product_name = 'S8') > 0
```

A positive sum means at least one row in this buyer's group is an S8 purchase.

Using equality to one would be wrong because a buyer may purchase S8 several times and should still qualify.

**Forbid every iPhone purchase**

The second condition is:

```sql
SUM(product_name = 'iPhone') = 0
```

Zero means no row in the complete buyer group is an iPhone purchase.

The two conditions are connected with `AND`, so both must hold. A buyer who bought both products fails the second condition even though the first is true.

**Why HAVING is the correct stage**

The eligibility tests depend on all rows of one buyer after grouping. `WHERE` filters individual rows before aggregation.

If the query used `WHERE product_name = 'S8'`, iPhone rows would disappear before the query checked for them, causing buyers of both products to look incorrectly eligible.

`HAVING` sees the complete joined history and can express simultaneous existence and nonexistence conditions safely.

**Why the result is exact**

For a returned buyer, the positive S8 indicator sum proves at least one S8 purchase, while the zero iPhone sum proves no iPhone purchase. Every returned buyer satisfies the contract.

Conversely, any buyer with at least one S8 and no iPhone has a positive first sum and zero second sum, so the group passes and is returned.

Grouping by buyer produces one row regardless of repeated qualifying sales, establishing the requested output grain.

**Other sales do not matter**

A buyer may purchase any number of unrelated products. Those rows remain in the group but contribute zero to both Boolean sums, correctly leaving eligibility unchanged.

Seller, date, quantity, and price are similarly irrelevant and need not appear in the select or grouping.

**Empty or entirely ineligible data**

If `Sales` is empty, no buyer groups exist and the output is empty.

If every buyer lacks S8 or has at least one iPhone, every group fails at least one `HAVING` condition and the result is also empty.

## Complexity detail

Let `P` be the number of product rows and `R` the number of sales rows.

A hash join can build product lookup state and scan sales in expected `O(P + R)` time. Grouping buyers with a sort-based plan can require `O(R log R)` time and `O(R)` working space.

The manifest records `O(P + R log R)` time and `O(P + R)` space, matching a join plus sort-based aggregation plan.

A hash join followed by hash aggregation may run in expected linear time with space proportional to products plus distinct buyers. The database optimizer and indexes determine the actual physical strategy.

## Alternatives and edge cases

- **NOT EXISTS:** Select distinct S8 buyers and reject any for whom an iPhone purchase exists. This often expresses the English condition directly.
- **NOT IN:** It works because `buyer_id` is guaranteed non-null, but `NOT EXISTS` is generally safer when nulls are possible.
- **Set difference:** Build the set of S8 buyers and subtract the set of iPhone buyers.
- **Conditional CASE aggregates:** `SUM(CASE WHEN ... THEN 1 ELSE 0 END)` is more portable across SQL dialects than MySQL Boolean arithmetic.
- **WHERE only S8:** It is incorrect because it hides iPhone evidence before grouping.
- **Buyer with several S8 purchases:** The first sum is greater than one and still passes.
- **Buyer with S8 and iPhone:** The iPhone sum is positive, so the buyer is rejected.
- **Buyer with only unrelated products:** The S8 sum is zero, so the buyer is rejected.
- **Repeated Sales rows:** Counts increase but group output remains one buyer row.
- **Product names:** Matching is exact and case-sensitive according to the database collation rules in use.
- **Non-null buyer identifier:** Every grouped row has a real buyer key.
- **Any output order:** No `ORDER BY` is required.
- **GROUP BY 1:** It refers to selected `buyer_id`; naming the column explicitly would be equivalent.
