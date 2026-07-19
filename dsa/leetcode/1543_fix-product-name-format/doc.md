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
