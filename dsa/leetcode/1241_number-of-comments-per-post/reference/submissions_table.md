## Submissions Table

| Column Name | Type |
|---|---|
| `sub_id` | int |
| `parent_id` | int |

The table may contain duplicate rows. A row with `parent_id = NULL` represents a post identified by `sub_id`. A row with a non-null `parent_id` represents a comment whose parent post is identified by that value. A referenced post may have been deleted and therefore may no longer have a post row in the table.
