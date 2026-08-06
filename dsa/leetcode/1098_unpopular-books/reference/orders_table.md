## Orders Table

| Column Name | Type |
|---|---|
| `order_id` | int |
| `book_id` | int |
| `quantity` | int |
| `dispatch_date` | date |

`order_id` is the primary key. Each `book_id` is a foreign key referencing `Books`, and every row records the quantity dispatched for one book order on `dispatch_date`.
