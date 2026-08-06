## Description

The `books` table stores a unique identifier, title, author, publication year, and optional rating for each book. A `NULL` value in `rating` means that no rating has been recorded. Find precisely those unrated books; a numeric rating, including zero, is still a recorded value and must not qualify.

Return `book_id`, `title`, `author`, and `published_year`, omitting the `rating` column itself. Sort the result by `book_id` in ascending order so the output order is deterministic. If every book has a rating, return the same four-column table shape with no rows.
