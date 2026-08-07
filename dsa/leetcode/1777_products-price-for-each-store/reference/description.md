## Description

Table: `Products`

| Column Name | Type |
| :--- | :--- |
| `product_id` | `int` |
| `store` | `enum` |
| `price` | `int` |

`(product_id, store)` is the primary key (combination of columns with unique values) for this table.
`store` is an ENUM (category) of type `('store1', 'store2', 'store3')` where each value represents the store this product is available at.
`price` is the price of the product at this store.

Write a solution to find the price of each product in each store.

Return the result table in **any order**.
