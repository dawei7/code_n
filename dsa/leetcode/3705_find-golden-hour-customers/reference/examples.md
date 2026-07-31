## Examples

**Example 1**

- Input: `restaurant_orders table (16 rows)`
- Output: `customers 103, 101, and 105 with computed metrics`
- Explanation: The input table is:

| `order_id` | `customer_id` | `order_timestamp` | `order_amount` | `payment_method` | `order_rating` |
|---:|---:|---|---:|---|---:|
| 1 | 101 | `2024-03-01 12:30:00` | 25.50 | `card` | 5 |
| 2 | 101 | `2024-03-02 19:15:00` | 32.00 | `app` | 4 |
| 3 | 101 | `2024-03-03 13:45:00` | 28.75 | `card` | 5 |
| 4 | 101 | `2024-03-04 20:30:00` | 41.00 | `app` | `NULL` |
| 5 | 102 | `2024-03-01 11:30:00` | 18.50 | `cash` | 4 |
| 6 | 102 | `2024-03-02 12:00:00` | 22.00 | `card` | 3 |
| 7 | 102 | `2024-03-03 15:30:00` | 19.75 | `cash` | `NULL` |
| 8 | 103 | `2024-03-01 19:00:00` | 55.00 | `app` | 5 |
| 9 | 103 | `2024-03-02 20:45:00` | 48.50 | `app` | 4 |
| 10 | 103 | `2024-03-03 18:30:00` | 62.00 | `card` | 5 |
| 11 | 104 | `2024-03-01 10:00:00` | 15.00 | `cash` | 3 |
| 12 | 104 | `2024-03-02 09:30:00` | 18.00 | `cash` | 2 |
| 13 | 104 | `2024-03-03 16:00:00` | 20.00 | `card` | 3 |
| 14 | 105 | `2024-03-01 12:15:00` | 30.00 | `app` | 4 |
| 15 | 105 | `2024-03-02 13:00:00` | 35.50 | `app` | 5 |
| 16 | 105 | `2024-03-03 11:45:00` | 28.00 | `card` | 4 |

The result is:

| `customer_id` | `total_orders` | `peak_hour_percentage` | `average_rating` |
|---:|---:|---:|---:|
| 103 | 3 | 100 | 4.67 |
| 101 | 4 | 100 | 4.67 |
| 105 | 3 | 100 | 4.33 |

- **Customer 101:** All four orders are in peak hours. Three of four are rated, and `(5 + 4 + 5) / 3 = 4.67`; every threshold is satisfied.
- **Customer 102:** Two of three orders are in peak hours and two are rated, but `(4 + 3) / 2 = 3.5`, so the average-rating rule excludes this customer.
- **Customer 103:** All three evening orders are in peak hours and rated. Their average is `(5 + 4 + 5) / 3 = 4.67`, so this customer qualifies.
- **Customer 104:** None of the three orders is in a peak interval, giving 0%; this customer fails the peak-hour rule.
- **Customer 105:** All three lunch orders are in peak hours and rated. Their average is `(4 + 5 + 4) / 3 = 4.33`, so this customer qualifies.

Customers 103 and 101 tie on average rating, so the descending customer-ID tie-break places 103 first. Customer 105 follows with the lower average.
