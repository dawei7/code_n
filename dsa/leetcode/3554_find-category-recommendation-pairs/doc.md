# Find Category Recommendation Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3554 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/find-category-recommendation-pairs/) |

## Problem Description

### Goal

Analyze which product categories are purchased by the same customers. For every pair of different categories, count the unique users who have purchased at least one product from each category.

Report a category pair only when at least three different customers belong to both categories. Represent every unordered pair once, with the lexicographically smaller category in `category1` and the larger category in `category2`.

Order the result by `customer_count` descending. Break equal-count ties by `category1` ascending and then `category2` ascending.

### Function Contract

**Inputs**

- `ProductPurchases`: Rows `(user_id, product_id, quantity)`, uniquely identified by `(user_id, product_id)`.
- `ProductInfo`: Rows `(product_id, category, price)`, uniquely identified by `product_id`.

`quantity` and `price` describe purchases and products but do not change whether a customer belongs to a category. Let $P$ be the number of purchase rows, $I$ the number of product rows, $U$ the number of distinct `(user_id, category)` memberships, and $J$ the number of customer-level unordered category pairs generated from those memberships.

**Return value**

Return columns `category1`, `category2`, and `customer_count` for every category pair shared by at least three unique customers, in the required order.

### Examples

#### Example 1

- **Input:** The sample purchase data has five users buying products from Books, Clothing, Electronics, Kitchen, and Sports.
- **Output:** `[(Books,Clothing,3), (Books,Electronics,3), (Clothing,Electronics,3), (Electronics,Sports,3)]`
- **Explanation:** Each listed pair is shared by exactly three customers. Other pairs have fewer than three shared customers. Since the reported counts tie, the category names determine their order.

---
