## Description

Use the sales records to report the total quantity sold for every product identifier. All sale rows belonging to the same `product_id` contribute to that product's total, including rows from different years or with different sale identifiers.

Return one result row per product represented in `Sales`. Each row contains the product identifier and its accumulated quantity, and the result rows may be returned in any order.
