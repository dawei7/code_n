## Views Table

| Column Name | Type |
|---|---|
| `article_id` | int |
| `author_id` | int |
| `viewer_id` | int |
| `view_date` | date |

Duplicate rows are allowed. Each row records that `viewer_id` viewed `article_id`, which was written by `author_id`, on `view_date`. Equal `author_id` and `viewer_id` values mean that the author and viewer are the same person.
