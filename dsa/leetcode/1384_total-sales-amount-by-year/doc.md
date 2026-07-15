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

### Required Complexity

- **Time:** $O(P + S + R)$
- **Space:** $O(P + S)$

<details>
<summary>Approach</summary>

#### General

**Materialize the three year intervals.** Create a small common table expression containing each report-year label, its first date, and its last date. Join a sales row to a year exactly when their closed intervals overlap:
$$
	ext{period start} \le 	ext{year end}
\quad\text{and}\quad
	ext{period end} \ge 	ext{year start}.
$$

**Measure only the intersection.** For an overlapping pair, the first counted date is the later of the two starts and the last counted date is the earlier of the two ends. The inclusive day count is the date difference plus one. Multiply it by `average_daily_sales`, then sum these contributions by product and report year.

Join `Product` by `product_id` to obtain the name, and order by the hidden product identifier followed by year. Every covered day belongs to exactly one calendar-year intersection, so cross-year periods are split without omission or double counting.

#### Complexity detail

The year relation has fixed size three. With indexed or hash joins, reading the $P$ products and $S$ sales rows and producing $R$ grouped overlaps takes $O(P + S + R)$ time. Join and grouping state use $O(P + S)$ space. The app artifact uses SQLite Julian-day arithmetic; the native artifact uses equivalent MySQL `DATEDIFF`, `LEAST`, and `GREATEST` functions.

#### Alternatives and edge cases

- **Expand every calendar day:** Generate one row per covered day and group afterward. It is correct but makes work proportional to total interval length.
- **Correlated scan per product-year:** Revisit all sales rows for each product and year. Without an index this takes $O(PS)$ time.
- **Inclusive endpoints:** Add one after subtracting dates; a one-day period must contribute one daily amount.
- **Leap day:** Calendar arithmetic must count `2020-02-29`.
- **Cross-year period:** Split it at each year boundary and use the same daily rate for both portions.
- **Multiple periods:** Sum every overlapping contribution for the same product and year.
- **No sales overlap:** Do not emit a product-year row with a null or zero amount.

</details>
