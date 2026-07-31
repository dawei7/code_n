## Trips Table

| Column Name | Type |
|---|---|
| `id` | int |
| `client_id` | int |
| `driver_id` | int |
| `city_id` | int |
| `status` | enum |
| `request_at` | varchar |

`id` is the table's primary key. `client_id` and `driver_id` refer to `Users.users_id`. The `status` value is one of `completed`, `cancelled_by_driver`, or `cancelled_by_client`.
