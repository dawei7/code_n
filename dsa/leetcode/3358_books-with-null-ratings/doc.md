# Books with NULL Ratings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3358 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/books-with-null-ratings/) |

## Problem Description

### Goal

The `books` table stores a unique identifier, title, author, publication year, and optional rating for each book. A `NULL` value in `rating` means that no rating has been recorded. Find precisely those unrated books; a numeric rating, including zero, is still a recorded value and must not qualify.

Return `book_id`, `title`, `author`, and `published_year`, omitting the `rating` column itself. Sort the result by `book_id` in ascending order so the output order is deterministic. If every book has a rating, return the same four-column table shape with no rows.

### Function Contract

**Inputs**

Table `books`:

- `book_id`: An integer that uniquely identifies a book.
- `title`: The book title as a `varchar` value.
- `author`: The author's name as a `varchar` value.
- `published_year`: The book's publication year as an integer.
- `rating`: A decimal rating or `NULL` when the book has not yet been rated.

Let $n$ be the number of rows in `books`.

**Return value**

Return columns `book_id`, `title`, `author`, and `published_year` for rows whose `rating` is `NULL`, ordered by `book_id ASC`.

### Examples

**Example 1**

Input table:

| book_id | title | author | published_year | rating |
|---:|---|---|---:|---:|
| 1 | The Great Gatsby | F. Scott | 1925 | 4.5 |
| 2 | To Kill a Mockingbird | Harper Lee | 1960 | `NULL` |
| 3 | Pride and Prejudice | Jane Austen | 1813 | 4.8 |
| 4 | The Catcher in the Rye | J.D. Salinger | 1951 | `NULL` |
| 5 | Animal Farm | George Orwell | 1945 | 4.2 |
| 6 | Lord of the Flies | William Golding | 1954 | `NULL` |

Output:

| book_id | title | author | published_year |
|---:|---|---|---:|
| 2 | To Kill a Mockingbird | Harper Lee | 1960 |
| 4 | The Catcher in the Rye | J.D. Salinger | 1951 |
| 6 | Lord of the Flies | William Golding | 1954 |

Only identifiers 2, 4, and 6 have no rating, and the rows appear in ascending identifier order.
