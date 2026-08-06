## Description

The `Submissions` table stores posts and their direct comments together. Duplicate post rows still describe one post, and duplicate comment rows with the same comment identifier still describe one unique comment for that post.

For every distinct post currently represented in the table, report its identifier and the number of distinct comment identifiers that directly reference it. Preserve posts that have no comments with a count of zero. A comment whose parent post is absent contributes to no result row.

Return the columns `post_id` and `number_of_comments`, ordered by `post_id` in ascending order.
