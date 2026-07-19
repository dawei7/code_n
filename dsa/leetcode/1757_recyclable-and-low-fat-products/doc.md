# Recyclable and Low Fat Products

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1757 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/recyclable-and-low-fat-products/) |

## Problem Description

### Goal

The `Products` table records each product's identifier and two independent yes-or-no properties. The `low_fats` column indicates whether the product is low fat, while `recyclable` indicates whether it can be recycled.

Find the products for which both properties are marked `"Y"`. Return only their `product_id` values. Products satisfying just one of the two conditions must not appear, and the result rows may be returned in any order.

### Function Contract

**Inputs**

- `Products(product_id, low_fats, recyclable)`: one row per product, with `product_id` as the primary key and each property containing either `"Y"` or `"N"`.

Let $R$ be the number of product rows and $K$ the number of rows satisfying both predicates.

**Return value**

- Return a one-column table named `product_id`.
- Include exactly those identifiers whose rows have both `low_fats = "Y"` and `recyclable = "Y"`.

### Examples

**Example 1**

- Input: products `1` and `3` have both flags set to `"Y"`, while the other rows fail at least one flag.
- Output: product identifiers `1` and `3`.
- Explanation: Both required predicates hold for exactly those two rows.

**Example 2**

- Input: one product has `low_fats = "Y"` and `recyclable = "N"`.
- Output: an empty result.
- Explanation: Being low fat alone does not satisfy the conjunction.

**Example 3**

- Input: every product has both flags set to `"Y"`.
- Output: every product identifier.
- Explanation: No qualifying row is excluded by the projection.
