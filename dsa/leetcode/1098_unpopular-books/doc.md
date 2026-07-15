# Unpopular Books

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1098 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open](https://leetcode.com/problems/unpopular-books/) |

## Problem Description

### Goal

`Books` contains each book's identifier, name, and release date. `Orders` records an order's book, quantity, and dispatch date; `book_id` in `Orders` references `Books`.

Assume the current date is `2019-06-23`. Report the identifiers and names of books that have been available for strictly more than one month and sold fewer than 10 copies during the preceding year. Books with no orders in that one-year window have sold zero copies and may qualify. Return the result in any order.

### Function Contract

**Input tables**

- `Books(book_id, name, available_from)`: one row per book, with `book_id` as its primary key.
- `Orders(order_id, book_id, quantity, dispatch_date)`: one row per order, with `order_id` as its primary key and `book_id` referencing `Books`.

Let $B$ and $O$ be the row counts of `Books` and `Orders`.

**Return value**

A relation with columns `book_id` and `name` for every book with `available_from < '2019-05-23'` whose total ordered quantity from `2018-06-23` through `2019-06-23`, inclusive, is less than 10.

### Examples

**Example 1**

`Books`

| book_id | name | available_from |
|---:|---|---|
| 1 | Kalila And Demna | 2010-01-01 |
| 2 | 28 Letters | 2012-05-12 |
| 3 | The Hobbit | 2019-06-10 |
| 4 | 13 Reasons Why | 2019-06-01 |
| 5 | The Hunger Games | 2008-09-21 |

`Orders`

| order_id | book_id | quantity | dispatch_date |
|---:|---:|---:|---|
| 1 | 1 | 2 | 2018-07-26 |
| 2 | 1 | 1 | 2018-11-05 |
| 3 | 3 | 8 | 2019-06-11 |
| 4 | 4 | 6 | 2019-06-05 |
| 5 | 4 | 5 | 2019-06-20 |
| 6 | 5 | 9 | 2009-02-02 |
| 7 | 5 | 8 | 2010-04-13 |

Output:

| book_id | name |
|---:|---|
| 1 | Kalila And Demna |
| 2 | 28 Letters |
| 5 | The Hunger Games |

### Required Complexity

- **Time:** $O((B + O) \log (B + O))$
- **Space:** $O(B + O)$

<details>
<summary>Approach</summary>

#### General

**Filter eligibility by release date.** A book released exactly on `2019-05-23` has been available for one month, not strictly more than one month, so only rows with `available_from < '2019-05-23'` qualify.

**Restrict orders in the join condition.** Left join each eligible book to orders dispatched from `2018-06-23` through `2019-06-23`, inclusive. Keeping the date predicate in `ON` rather than `WHERE` preserves books with no matching recent order.

**Aggregate recent quantities per book.** Group by the book's identifier and name, sum the matched quantities, and replace the null sum for an unmatched book with zero. Retain groups whose total is strictly less than 10. Orders outside the window never enter the aggregate, regardless of their quantity.

The release filter selects exactly the sufficiently old books. For each selected book, the restricted left join contains every and only order in the stated year, while still producing one null-extended row when there are none. The grouped sum is therefore the required sales total, and the final threshold selects exactly the unpopular books.

#### Complexity detail

A standard sort-based join and grouping plan takes $O((B + O) \log(B + O))$ time and $O(B + O)$ working space. Hash joins and hash aggregation can approach $O(B + O)$ expected time. The actual plan depends on the database engine and available indexes.

#### Alternatives and edge cases

- **Pre-aggregate recent orders:** Group the one-year orders by `book_id` first and left join those totals to `Books`; this is equally valid and can reduce join rows.
- **Correlated quantity subquery:** Summing `Orders` separately for every book is concise but may require $O(BO)$ work without an index.
- **No recent orders:** The book's one-year total is zero, so `COALESCE` must allow it to qualify.
- **Exactly ten copies:** The book is not unpopular because the threshold is strictly fewer than 10.
- **Release cutoff:** `2019-05-23` itself is excluded because the book must be available for more than one month.
- **Order-window endpoints:** Orders on both `2018-06-23` and `2019-06-23` count toward the total.

</details>
