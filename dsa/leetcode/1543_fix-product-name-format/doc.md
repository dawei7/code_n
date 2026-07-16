# Fix Product Name Format

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1543 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/fix-product-name-format/) |

## Problem Description
### Goal
The `Sales` table records individual sales with a unique sale identifier, a product name, and a sale date. Product names are case-insensitive and may contain spaces at the beginning or end, so differently written values can denote the same product.

Normalize every product name by trimming its surrounding spaces and converting it to lowercase. Combine all sales for the same normalized product and calendar month, report the month in `YYYY-MM` form, and return the number of sales in each group. Sort the result first by normalized product name and then by month, both in ascending order.

### Function Contract
**Inputs**

- `Sales(sale_id, product_name, sale_date)`: $r$ sale rows. Each `sale_id` is unique, each date is in the year 2000, and each product name is compared without regard to case after leading and trailing spaces are removed.
- Let $g$ be the number of distinct normalized-product and calendar-month groups.

**Return value**

A table with columns `product_name`, `sale_date`, and `total`. The first column contains the trimmed lowercase product name, the second contains the month as `YYYY-MM`, and the third counts rows in that group. Rows are ordered by `product_name` and then `sale_date`, both ascending.

### Examples
**Example 1**

- Input: six sales spelling `LCPhone` and `LCKeyChain` with different letter cases, plus one `Matryoshka` sale
- Output: `[["lckeychain", "2000-02", 2], ["lcphone", "2000-01", 2], ["lcphone", "2000-02", 1], ["matryoshka", "2000-03", 1]]`
- Explanation: Case variants share a normalized name, while January and February remain separate groups.

**Example 2**

- Input: `("  Widget  ", "2000-05-04")` and `("widget", "2000-05-20")`
- Output: `[["widget", "2000-05", 2]]`
- Explanation: Trimming and lowercasing make both rows part of one group.

**Example 3**

- Input: one sale each for `"Beta"` in January and `"alpha"` in December
- Output: `[["alpha", "2000-12", 1], ["beta", "2000-01", 1]]`
- Explanation: Product-name ordering takes precedence over chronological ordering between products.

### Required Complexity

- **Time:** $O(r \log r)$
- **Space:** $O(g)$

<details>
<summary>Approach</summary>

#### General

**Normalize before forming groups**

Apply `TRIM` before `LOWER` so surrounding whitespace cannot create artificial product variants. Extract the four-digit year and two-digit month from each `sale_date`; in the app-local SQLite query, `strftime('%Y-%m', sale_date)` produces exactly the required representation. These two expressions define the logical group key.

**Aggregate each normalized product-month pair**

Group the rows by both expressions and use `COUNT(*)` to count sales. Grouping by only the product would incorrectly merge different months, while grouping by the original product text would split capitalization and whitespace variants. Because every source row belongs to exactly one normalized pair, the aggregate counts partition all sales without omission or duplication.

**Return the specified deterministic order**

Order by the normalized `product_name` alias and then the formatted `sale_date` alias. The `YYYY-MM` format has fixed-width components, so lexical ascending order is also chronological ascending order. The native MySQL artifact uses `DATE_FORMAT` for the same operation; only the database-specific date formatter differs.

#### Complexity detail

For $r$ input rows, normalization and month extraction are constant work per row. A database engine can build the $g$ aggregate groups with a hash table and then sort the result, or use sorting for grouping as well. The portable upper bound is therefore $O(r \log r)$ time. The aggregation state stores one count per distinct group, using $O(g)$ auxiliary space; the engine may also allocate sorting workspace proportional to the data it sorts.

#### Alternatives and edge cases

- **Pre-normalized computed columns:** storing an indexed normalized name and month can reduce repeated expression work, but it changes the schema and is unnecessary for this query.
- **Correlated count per sale:** counting matching rows in a subquery can produce the same values, but repeats the scan for many rows and degrades toward $O(r^2)$.
- Leading and trailing whitespace must be removed before grouping; internal spaces remain part of the product name.
- Product names differing only by letter case belong to the same group.
- Sales of one product in different months must remain separate.
- The output month needs a zero-padded two-digit month so lexical and chronological order agree.
- Sorting is by product first, even when that places a later month before an earlier month belonging to another product.

</details>
