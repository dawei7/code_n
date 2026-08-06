## Likes Table

| Column Name | Type |
|---|---|
| `user_id` | int |
| `page_id` | int |

The pair `(user_id, page_id)` is the composite primary key, so a user-page like appears at most once. Each row records that the identified user likes the identified page.
