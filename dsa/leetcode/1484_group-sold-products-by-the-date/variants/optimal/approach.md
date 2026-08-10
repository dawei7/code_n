## General

**What the query must summarize**

The input contains one row for every recorded sale event. Several rows can have the same `sell_date`, and even the same product can appear more than once on one date because the table has no primary key. The result therefore cannot count rows directly. For each distinct date, it must report one output row containing the number of distinct product names and a comma-separated list containing those same distinct names. Finally, result rows must appear in ascending date order.

The stored SQL expresses that work as one grouped query:

1. `GROUP BY sell_date` partitions all input rows into groups. Every group contains exactly the rows whose dates are equal.
2. `COUNT(DISTINCT product)` counts the different product values in the current group and gives that number the output name `num_sold`.
3. `STRING_AGG(DISTINCT product, ',')` removes repeated product values and combines the remaining values with a comma between adjacent names.
4. `ORDER BY sell_date` sorts the completed output rows from the earliest date to the latest date.

It helps to separate two meanings that are easy to mix up. Grouping controls how many result rows exist: there is one row per distinct `sell_date`. The `DISTINCT` inside each aggregate controls which product values contribute within that row. For example, if one date has the input products `Mask`, `Mask`, and `Pencil`, that date still forms one group. The distinct count is two, and the concatenated set contains `Mask` and `Pencil` once each.

**Why the two aggregates agree**

Both aggregate expressions operate on the same date group and both apply `DISTINCT` to the same `product` column. Consequently, `num_sold` describes the number of names represented by `products` rather than the number of source records. That parallel use of `DISTINCT` is essential. If the count omitted it, duplicated sales would make the number larger than the list. If the string aggregate omitted it, the list could contain repeated names while the count did not.

The separator argument `','` requests commas with no added spaces. A group containing the unique names `Bible` and `Pencil` is therefore represented as `Bible,Pencil`, not as `Bible, Pencil`. A group with one unique product simply produces that product name; no leading or trailing separator is needed.

**The ordering issue in the exact stored source**

There are two independent ordering requirements. The outer `ORDER BY sell_date` handles the order of result rows, and the stored query satisfies that part. The product names inside each aggregated string also have to be lexicographically sorted. The exact stored expression is `STRING_AGG(DISTINCT product, ',')`, with no ordering clause inside the aggregate. Grouping and `DISTINCT` define membership, but they do not define the order in which an SQL engine feeds those members to `STRING_AGG`. An outer date sort cannot repair this because it rearranges whole result rows, not text inside `products`.

Therefore, the stored query reliably produces the correct groups, distinct counts, and distinct membership, but standard SQL semantics do not guarantee that its `products` string is lexicographically ordered. It may happen to look sorted for a particular execution plan or dataset, but that is not a correctness guarantee. In a PostgreSQL-style dialect, the intended deterministic expression would put an ordering term inside the aggregate, such as `STRING_AGG(DISTINCT product, ',' ORDER BY product)`. In a MySQL-style dialect, the corresponding facility is usually `GROUP_CONCAT` with an internal `ORDER BY`. This documentation does not silently attribute that missing behavior to the exact source.

**Why the grouping logic itself is correct**

Take any output date `d`. By the definition of `GROUP BY`, its aggregate group contains every input row with `sell_date = d` and no row with another date. The distinct modifier maps all occurrences of one product name in that group to one aggregate contribution. Thus the count equals the cardinality of the set of products sold on `d`, and the string contains exactly that same set once each. This proves the membership and counting portions of the requested summary.

Every distinct input date creates one group, so no date with activity is omitted. No date absent from the input can create a group, so no extra row appears. The final outer ordering arranges those groups by their date keys. If the aggregate also orders its inputs by `product`, the names in every string are lexicographically ordered, completing the full contract. Without that internal order, only the name-order portion remains unproven in the stored query.

## Complexity detail

Let $R$ be the number of rows in `Activities` and let $P$ be the total number of distinct date-product pairs. Also let $D$ be the number of distinct dates. Any execution must at least inspect the relevant input rows, which contributes $O(R)$ work.

The manifest states $O(R + P \log P)$ time and $O(P)$ space. This is a useful logical upper-bound model when the engine groups the rows and sorts the distinct product values needed for the output strings. Across all date groups, there are $P$ distinct values to retain. Sorting each group separately costs $\sum_d O(P_d \log P_d)$, where $P_d$ is the number of distinct products on date $d$; this is bounded by $O(P \log P)$. Ordering the $D$ output dates can add $O(D \log D)$, which is also bounded by $O(P \log P)$ when every date has at least one product pair.

The working storage used by hash grouping, distinct tracking, aggregation, or sorting can be $O(P)$, apart from the returned strings themselves. The final text also contains the product characters and separators, so a character-precise analysis should include total output length.

SQL complexity is necessarily plan-dependent. A database can choose hash or sort aggregation, exploit an index, spill intermediate data to disk, or parallelize portions of the work. Hash tables also give expected rather than absolute constant-time lookup behavior. The stated bounds describe the algorithmic work of a normal grouping-and-sorting plan, not a promise about one physical query plan. For the exact stored query, an engine may avoid the product sort because no internal order is requested; that can reduce work, but it also causes the correctness gap described above.

## Alternatives and edge cases

- **Ordered string aggregation:** Put `ORDER BY product` inside the string aggregate. This is the direct repair because it preserves the one-pass grouped structure while making the required lexicographic order explicit and deterministic.
- **Deduplicating subquery:** First select distinct `sell_date` and `product` pairs, then group that smaller relation. This makes the logical stages very visible, although the database may already perform equivalent work for the two distinct aggregates.
- **Window functions:** Windowed counts can annotate rows, but an additional distinct-and-collapse stage is still needed to return one row per date. They add complexity without improving this grouped result.
- **Application-side grouping:** Fetching all rows and grouping them in application code can implement the rules, but it moves data unnecessarily and gives up the database engine's aggregation strengths.
- **Duplicate source rows:** Repeated copies of the same date-product pair must affect neither `num_sold` nor the product list. The two `DISTINCT` modifiers handle this correctly.
- **One product on a date:** The count is one and the aggregate string is just that name, with no comma.
- **Several dates with the same products:** Dates are independent groups. The same name can validly appear in several result rows.
- **Lexicographic case behavior:** The exact ordering of uppercase, lowercase, and accented text depends on the database collation. An internal `ORDER BY product` follows that configured collation unless a specific collation is requested.
- **Null products:** The reference describes product names as sale data but does not state null behavior. Standard count and string aggregates commonly ignore nulls; if nulls were permitted and needed special treatment, the contract would have to specify it.
- **Outer versus inner order:** `ORDER BY sell_date` sorts rows only. It never guarantees the ordering of product names within an aggregated string.
