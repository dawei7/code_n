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
