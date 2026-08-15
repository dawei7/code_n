# Find Product Recommendation Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3521 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/find-product-recommendation-pairs/) |

## Problem Description

### Goal

The `ProductPurchases` table records which products each customer bought and the quantity purchased. The `ProductInfo` table supplies the category and price of every product.

Identify pairs of distinct products that are suitable for recommendation because at least three different customers bought both products. Represent every unordered pair once, placing the smaller product identifier in `product1_id` and the larger identifier in `product2_id`. For each qualifying pair, report both product categories and the number of distinct shared customers.

Order recommendations by decreasing shared-customer count. Break ties first by increasing `product1_id`, then by increasing `product2_id`.

### Function Contract

**Inputs**

- `ProductPurchases(user_id, product_id, quantity)`: Purchase records with a unique `(user_id, product_id)` pair. `quantity` is positive and does not change whether that customer bought the product.
- `ProductInfo(product_id, category, price)`: One row per product, containing its category and price.

Let $P$ be the number of purchase rows, $I$ the number of product-information rows, and

$$
J = \sum_u \binom{d_u}{2},
$$

where $d_u$ is the number of distinct products bought by customer $u$. Thus, $J$ is the number of customer-level product pairs generated before equal product pairs are grouped together.

**Return value**

Return columns `product1_id`, `product2_id`, `product1_category`, `product2_category`, and `customer_count`. Include only pairs shared by at least three distinct customers, and enforce `product1_id < product2_id`. Sort by `customer_count` descending, then both product identifiers ascending.

### Examples

#### Example 1

- **Input:** Customers 1 and 4 buy products 101, 102, and 103; customer 2 buys 101, 102, and 104; customer 3 buys 101, 103, and 105; customer 5 buys 102 and 104. Product categories are Electronics, Books, Clothing, Kitchen, and Sports respectively.
- **Output:** `(101, 102, Electronics, Books, 3)`, `(101, 103, Electronics, Clothing, 3)`, and `(102, 104, Books, Kitchen, 3)`.

#### Example 2

- **Input:** Three customers each buy products 7 and 12, with arbitrary positive quantities.
- **Output:** One recommendation `(7, 12, ..., ..., 3)`; quantities do not multiply the customer count.

#### Example 3

- **Input:** Only two customers share the same two products.
- **Output:** No rows, because a recommendation needs at least three distinct customers.
