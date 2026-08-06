## Function Contract

**Input table**

- `Views(article_id, author_id, viewer_id, view_date)`: article-view events. Duplicate rows are permitted, and an author may also be the viewer.

Let $R$ be the number of rows in `Views`.

A person qualifies if there is at least one `view_date` on which that `viewer_id` is associated with two or more distinct `article_id` values. Author identity does not affect qualification.

**Return value**

- A one-column table named `id` containing each qualifying `viewer_id` exactly once, in ascending order. If no person qualifies, return the same column with no rows.
