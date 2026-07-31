# Fill Missing Data

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2887 |
| Difficulty | Easy |
| Category | pandas |
| Topics | Uncategorized |
| Supported Languages | python |
| Official Link | [LeetCode](https://leetcode.com/problems/fill-missing-data/) |

## Problem Description

### Goal

A product DataFrame contains the columns `name`, `quantity`, and `price`. Some rows have no stored value in the `quantity` column.

Replace every missing quantity with `0`. Return the resulting DataFrame with the same columns and row order, preserving each product name, price, and every quantity that was already present. The correction is limited to missing values in `quantity`.

No product row is added or removed by this cleanup.

### Function Contract

**Inputs**

- `products`: A pandas DataFrame with an object column `name` and numeric columns `quantity` and `price`; `quantity` may contain missing values.

Let $n$ be the number of product rows.

**Return value**

Return the product DataFrame after replacing each missing value in `quantity` with `0`, without changing other cells.

### Examples

**Example 1**

- Input: `products = [{"name": "Wristwatch", "quantity": null, "price": 135}, {"name": "WirelessEarbuds", "quantity": null, "price": 821}, {"name": "GolfClubs", "quantity": 779, "price": 9319}, {"name": "Printer", "quantity": 849, "price": 3051}]`
- Output: `[{"name": "Wristwatch", "quantity": 0, "price": 135}, {"name": "WirelessEarbuds", "quantity": 0, "price": 821}, {"name": "GolfClubs", "quantity": 779, "price": 9319}, {"name": "Printer", "quantity": 849, "price": 3051}]`

**Example 2**

- Input: `products = [{"name": "Cable", "quantity": null, "price": 12}, {"name": "Adapter", "quantity": null, "price": 19}]`
- Output: `[{"name": "Cable", "quantity": 0, "price": 12}, {"name": "Adapter", "quantity": 0, "price": 19}]`

**Example 3**

- Input: `products = [{"name": "Notebook", "quantity": 4, "price": 7}, {"name": "Pen", "quantity": 25, "price": 2}]`
- Output: `[{"name": "Notebook", "quantity": 4, "price": 7}, {"name": "Pen", "quantity": 25, "price": 2}]`
