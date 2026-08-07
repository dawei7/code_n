## Examples

**Example 1**

- Input: `Products` table:
  | product_id | store | price |
  | :--- | :--- | :--- |
  | 0 | store1 | 95 |
  | 0 | store3 | 105 |
  | 0 | store2 | 100 |
  | 1 | store1 | 70 |
  | 1 | store3 | 80 |

- Output: | product_id | store1 | store2 | store3 |
  | :--- | :--- | :--- | :--- |
  | 0 | 95 | 100 | 105 |
  | 1 | 70 | null | 80 |

- Explanation: - Product 0 prices are 95 for store1, 100 for store2, and 105 for store3.
  - Product 1 prices are 70 for store1, 80 for store3, and it's not sold in store2.
