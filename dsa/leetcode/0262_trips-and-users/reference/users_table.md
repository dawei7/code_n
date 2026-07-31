## Users Table

| Column Name | Type |
|---|---|
| `users_id` | int |
| `banned` | enum |
| `role` | enum |

`users_id` is the table's primary key. `banned` is either `Yes` or `No`, and `role` is one of `client`, `driver`, or `partner`.
