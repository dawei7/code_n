## Examples

**Example 1**

- Input:
  `Delivery` table:
  | delivery_id | customer_id | order_date | customer_pref_delivery_date |
  | :--- | :--- | :--- | :--- |
  | 1 | 1 | 2019-08-01 | 2019-08-02 |
  | 2 | 5 | 2019-08-02 | 2019-08-02 |
  | 3 | 1 | 2019-08-11 | 2019-08-11 |
  | 4 | 3 | 2019-08-24 | 2019-08-26 |
  | 5 | 4 | 2019-08-21 | 2019-08-22 |
  | 6 | 2 | 2019-08-11 | 2019-08-13 |

- Output:
  | immediate_percentage |
  | :--- |
  | 33.33 |

- Explanation: The orders with delivery id 2 and 3 are immediate while the others are scheduled.
