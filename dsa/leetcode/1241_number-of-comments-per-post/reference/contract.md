## Function Contract

**Input table**

`Submissions(sub_id, parent_id)` may contain duplicate rows. Null `parent_id` values identify post rows; non-null values identify the parent post of a comment row.

Let $r$ be the total number of rows in `Submissions`.

**Return value**

- Return exactly the columns `post_id` and `number_of_comments`.
- Produce one row for every distinct `sub_id` appearing on a row where `parent_id IS NULL`.
- Count distinct comment `sub_id` values separately for each matching `parent_id`.
- Return zero for a post with no matching comments and ignore comments whose parent post is absent.
- Order the rows by `post_id` in ascending order.
