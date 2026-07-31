# Calculate Product Final Price

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3293 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/calculate-product-final-price/) |

## Problem Description

### Goal

The `Products` table identifies every product, its category, and its price. The `Discounts` table optionally assigns a percentage discount from 0 through 100 to a category. Each product ID is unique, and each discounted category appears at most once.

Report every product with its price after applying the matching category discount. A product whose category has no row in `Discounts` keeps its original price. Include `product_id`, the calculated `final_price`, and `category`, and order the result by `product_id` in ascending order.

### Function Contract

**Inputs**

- `Products(product_id, category, price)`: One row per product, with `product_id` as its unique key.
- `Discounts(category, discount)`: At most one percentage discount per category, with `category` as its primary key.

**Return value**

- A table with columns `product_id`, `final_price`, and `category`, ordered by ascending `product_id`.

For a matching discount $d$, the final price is $price\cdot(100-d)/100$. Without a match, use $d=0$.

### Examples

**Example 1**

`Products`

| product_id | category | price |
|---:|---|---:|
| 1 | Electronics | 1000 |
| 2 | Clothing | 50 |
| 3 | Electronics | 1200 |
| 4 | Home | 500 |

`Discounts`

| category | discount |
|---|---:|
| Electronics | 10 |
| Clothing | 20 |

Output:

| product_id | final_price | category |
|---:|---:|---|
| 1 | 900 | Electronics |
| 2 | 40 | Clothing |
| 3 | 1080 | Electronics |
| 4 | 500 | Home |
