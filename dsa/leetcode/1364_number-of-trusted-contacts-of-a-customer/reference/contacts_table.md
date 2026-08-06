## Contacts Table

| Column Name | Type |
|---|---|
| `user_id` | `id` |
| `contact_name` | `varchar` |
| `contact_email` | `varchar` |

The pair (`user_id`, `contact_email`) is the primary key. Each row records one person trusted by the customer identified by `user_id`, including that contact's displayed name and email. A contact may or may not also be a customer of the shop.
