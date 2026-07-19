# Total Sales Amount by Year

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1384 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open Problem](https://leetcode.com/problems/total-sales-amount-by-year/) |

## Problem Description

### Goal

The `Product` table identifies products and their names. Each row of `Sales` states that one product sold at a fixed `average_daily_sales` amount throughout an inclusive interval from `period_start` through `period_end`. Sales periods fall within calendar years 2018 through 2020 and may cross year boundaries.

For every product and year with covered sales days, report the product identifier, product name, year, and total amount sold during that year's portion of all its periods. Return the rows ordered by product identifier and report year.

### Function Contract

**Inputs**

- `Product(product_id, product_name)`: $P$ product definitions.
- `Sales(product_id, period_start, period_end, average_daily_sales)`: $S$ inclusive constant-rate sales periods.
- The three calendar-year boundaries for 2018, 2019, and 2020 are fixed by the problem.

**Return value**

- A relation with columns `product_id`, `product_name`, `report_year`, and `total_amount`, containing one row for each product-year overlap. Let $R$ be the number of returned rows.

### Examples

**Example 1**

- Input: `Product = [[1,"LC Phone"],[2,"LC T-Shirt"],[3,"LC Keychain"]]`, with sales periods `[[1,"2019-01-25","2019-02-28",100],[2,"2018-12-01","2020-01-01",10],[3,"2019-12-01","2020-01-31",1]]`
- Output: `[[1,"LC Phone","2019",3500],[2,"LC T-Shirt","2018",310],[2,"LC T-Shirt","2019",3650],[2,"LC T-Shirt","2020",10],[3,"LC Keychain","2019",31],[3,"LC Keychain","2020",31]]`

**Example 2**

- Input: one product sold only on `2020-02-29` at `7` per day.
- Output: `[[1,"Leap","2020",7]]`

**Example 3**

- Input: one product sold from `2019-12-31` through `2020-01-01` at `5` per day.
- Output: `[[2,"Boundary","2019",5],[2,"Boundary","2020",5]]`
