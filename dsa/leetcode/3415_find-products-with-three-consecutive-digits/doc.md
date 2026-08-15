# Find Products with Three Consecutive Digits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3415 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/find-products-with-three-consecutive-digits/) |

## Problem Description

### Goal

The `Products` table contains one row per product, identified by `product_id`, together with its `name`. Find every product whose name contains a run of exactly three consecutive digit characters.

The three digits must form a complete run: neither adjacent character, when present, may also be a digit. A name can contain more than one qualifying run, but each returned product appears only once. Return `product_id` and `name`, ordered by `product_id` in ascending order.

### Function Contract

**Inputs**

- `Products`: A table with unique integer `product_id` values and product names in `name`.

Let $n$ be the number of rows and let

$$
S=\sum_{p\in\texttt{Products}}\lvert p.\texttt{name}\rvert
$$

be the total number of characters across all names.

**Return value**

- A result table with columns `product_id` and `name` for qualifying products, sorted by `product_id` ascending.

### Examples

#### Example 1

- **Input:** `Products = [(1, "ABC123XYZ"), (2, "A12B34C"), (3, "Product56789"), (4, "NoDigitsHere"), (5, "789Product"), (6, "Item003Description"), (7, "Product12X34")]`
- **Output:** `[(1, "ABC123XYZ"), (5, "789Product"), (6, "Item003Description")]`

The names for products 1, 5, and 6 contain the complete three-digit runs `123`, `789`, and `003`. Product 3 has a five-digit run, which does not qualify.

#### Example 2

- **Input:** `Products = [(2, "123"), (1, "X1234Y"), (3, "A123B456C")]`
- **Output:** `[(2, "123"), (3, "A123B456C")]`

A qualifying run may occupy the entire name or appear among other characters; `1234` is too long.
