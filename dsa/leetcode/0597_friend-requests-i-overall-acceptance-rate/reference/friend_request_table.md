## Friend Request Table

| Column Name | Type |
|---|---|
| `sender_id` | int |
| `send_to_id` | int |
| `request_date` | date |

The table has no primary key and may contain duplicate rows. Each row records the sender, receiver, and date of one friend-request event.
