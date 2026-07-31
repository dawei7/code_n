# Find Books with No Available Copies

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3570 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/find-books-with-no-available-copies/) |

## Problem Description

### Goal

A library catalog records each book's descriptive fields and the total number of copies owned. A separate borrowing history records individual loans. A loan is still active when its `return_date` is `NULL`; returned loans must not reduce current availability.

Find every book that has at least one active loan and no copy currently available. In other words, the number of active borrowing records for the book must equal its `total_copies`.

For each qualifying book, return its identifier, title, author, genre, publication year, and number of current borrowers. Sort books by that borrower count in descending order, then by title in ascending order.

### Function Contract

**Inputs**

- `library_books`: A table keyed by `book_id`, with columns `title`, `author`, `genre`, `publication_year`, and `total_copies`.
- `borrowing_records`: A table keyed by `record_id`, with `book_id`, `borrower_name`, `borrow_date`, and nullable `return_date`. A `NULL` return date identifies a currently active loan.

**Return value**

Return columns `book_id`, `title`, `author`, `genre`, `publication_year`, and `current_borrowers`, ordered by `current_borrowers` descending and `title` ascending. Include only books whose active-loan count equals their owned-copy count.

### Examples

**Example 1**

- Input: A six-book catalog in which *The Great Gatsby* has three active loans for three copies and *1984* has one active loan for one copy; all other books retain at least one available copy.
- Output: Rows for *The Great Gatsby* with `current_borrowers = 3`, followed by *1984* with `current_borrowers = 1`.
- Explanation: Returned records are excluded before counting, so only these two books have zero availability.

---
