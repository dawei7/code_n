## General

Use SQL's dedicated null predicate to retain rows where `rating IS NULL`. Equality does not model this condition: `rating = NULL` evaluates to unknown rather than true, so it cannot select unrated books.

Project exactly `book_id`, `title`, `author`, and `published_year`. Leaving `rating` out of the `SELECT` list is part of the required output contract, even though that column supplies the filter.

Apply `ORDER BY book_id ASC` to the result. The input table has no guaranteed presentation order, and filtering alone does not establish one. Because `book_id` is unique, this key gives a complete deterministic ordering without a tie breaker.

Every returned row has a null rating because it passes the `IS NULL` predicate. Conversely, every unrated row passes that predicate, retains all four requested fields, and appears exactly once because the query neither joins nor groups. Sorting changes only row order, so the result is precisely the unrated subset in ascending identifier order.

The remotely Accepted MySQL query also runs unchanged in the app's SQLite fixture engine because `IS NULL`, projection, and ascending ordering have the same relevant semantics in both dialects.

## Complexity detail

Let $n$ be the number of rows in `books` and $k$ the number of unrated rows. Without assuming indexes, filtering scans all $n$ rows and sorting the selected rows costs $O(k\log k)$, giving $O(n\log n)$ worst-case time. The database may use $O(k)$, hence $O(n)$, workspace for the result and sort. A suitable index can reduce physical work, but the logical query does not rely on one.

The benchmark size is $n$, with every second row unrated and the input identifiers stored in descending order. The reference performs one scan and orders the qualifying rows. A correlated baseline that redundantly counts preceding identifiers for every retained row performs repeated table scans and exhibits quadratic growth.

## Alternatives and edge cases

- **`rating = NULL`:** SQL comparisons with `NULL` produce unknown, so this condition returns no qualifying rows.
- **`NOT rating`:** Truthiness is not the contract and would incorrectly treat a numeric zero rating as missing in dialects that allow the expression.
- **`COALESCE(rating, 0) = 0`:** This merges absent ratings with genuine zero ratings and is therefore semantically wrong.
- **Correlated existence or count check:** It can preserve the same rows when made tautological, but repeated per-row scans add needless quadratic work.
- **No null ratings:** Return the required four columns with an empty row set.
- **Every rating null:** Return every book, still sorted by `book_id`.
- **Unsorted source rows:** Only the outer `ORDER BY book_id ASC` determines the required result order.
- **Projection:** Do not include `rating` in the output, despite using it in the predicate.
