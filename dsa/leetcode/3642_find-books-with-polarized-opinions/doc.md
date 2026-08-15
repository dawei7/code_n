# Find Books with Polarized Opinions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3642 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/find-books-with-polarized-opinions/) |

## Problem Description

### Goal

The `books` table stores each book's title, author, genre, and page count. The `reading_sessions` table records individual readers' progress and their integer rating from 1 through 5 for the associated book.

A book has polarized opinions only when it has at least five reading sessions, includes at least one high rating of 4 or 5, and includes at least one low rating of 1 or 2. Its rating spread is its highest rating minus its lowest rating. Its polarization score is the fraction of all its sessions whose rating is extreme: at most 2 or at least 4.

Report only books whose polarization score is at least $0.6$. Include the book details, rating spread, and score rounded to two decimal places. Sort by polarization score descending and then by title descending.

### Function Contract

**Inputs**

- `books`: Rows with unique `book_id`, plus `title`, `author`, `genre`, and `pages`.
- `reading_sessions`: Rows with unique `session_id`, a referenced `book_id`, `reader_name`, `pages_read`, and `session_rating` from 1 through 5.

**Return value**

Return the columns `book_id`, `title`, `author`, `genre`, `pages`, `rating_spread`, and `polarization_score` in the required order.

### Examples

#### Example 1

- **Input:** The Great Gatsby has ratings `5, 1, 4, 2, 5`; 1984 has ratings `2, 1, 2, 1, 4, 5`; the remaining books either lack a low rating or have fewer than five sessions.
- **Output:** The Great Gatsby followed by 1984, each with rating spread `4` and polarization score `1.00`.
- **Explanation:** Both returned books have ratings at both extremes, meet the session minimum, and have an extreme rating in every session. Their equal scores are resolved by descending title order.
