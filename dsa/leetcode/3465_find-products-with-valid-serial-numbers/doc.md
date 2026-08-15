# Find Products with Valid Serial Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3465 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/find-products-with-valid-serial-numbers/) |

## Problem Description

### Goal

The `products` table stores each product's unique identifier, name, and free-text description. Select every product whose description contains a complete, case-sensitive serial-number token of the form `SNdddd-dddd`, where each `d` is one decimal digit. The token may occur at the beginning, in the middle, or at the end of the description.

The prefix must be uppercase `SN`, and each digit group must contain exactly four digits with one hyphen between them. A longer alphanumeric or underscore-containing word must not qualify merely because it contains a matching-looking substring. Return all three source columns for qualifying products, ordered by `product_id` in ascending order.

### Function Contract

**Input table**

`products`

| Column | Type | Meaning |
|---|---|---|
| `product_id` | int | Unique product identifier |
| `product_name` | varchar | Product name |
| `description` | varchar | Free-text product description to inspect |

**Return value**

Return `product_id`, `product_name`, and `description` for every row containing a valid serial number, sorted by ascending `product_id`.

### Examples

#### Example 1

Input table `products`:

| product_id | product_name | description |
|---:|---|---|
| 1 | Widget A | `This is a sample product with SN1234-5678` |
| 2 | Widget B | `A product with serial SN9876-1234 in the description` |
| 3 | Widget C | `Product SN1234-56789 is available now` |
| 4 | Widget D | `No serial number here` |
| 5 | Widget E | `Check out SN4321-8765 in this description` |

- **Output:** 

| product_id | product_name | description |
|---:|---|---|
| 1 | Widget A | `This is a sample product with SN1234-5678` |
| 2 | Widget B | `A product with serial SN9876-1234 in the description` |
| 5 | Widget E | `Check out SN4321-8765 in this description` |

Product 3 has five digits after the hyphen, and product 4 contains no serial-number token.
