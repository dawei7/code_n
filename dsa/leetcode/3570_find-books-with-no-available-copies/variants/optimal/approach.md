## General

The query first counts active borrowing records per book, then joins those counts to the catalog and keeps books whose active count equals the number of owned copies.

The common table expression `T` separates transaction filtering and aggregation from catalog reporting. This avoids joining every historical borrowing row to full book metadata before inactive records are discarded.

**Identifying active loans**

`return_date IS NULL` is the statement’s exact definition of a currently borrowed copy. A completed record has a non-null return date and must not reduce present availability.

The condition belongs in `WHERE` before grouping. This ensures each group contains active transactions only; counting all records and trying to interpret returned loans afterward would inflate current borrowers.

SQL requires `IS NULL` rather than `= NULL` because null represents an unknown/missing value and ordinary equality with null does not evaluate to true.

**Counting current borrowers per book**

The CTE groups active records by `book_id` and evaluates `COUNT(1)`. Since each borrowing record represents one transaction for one copy, this count is the number of currently borrowed copies for that book.

The alias `current_borrowers` is used later for filtering, projection, and ordering.

`GROUP BY 1` is positional shorthand for grouping by the first selected expression, `book_id`.

Books with no active record have no row in `T`. That is desirable because a book with every copy available cannot satisfy “currently borrowed” and “zero copies available.”

**Joining counts to catalog data**

`library_books JOIN T USING (book_id)` attaches title, author, genre, publication year, and total copies to each active-loan count.

`library_books.book_id` is unique, and `T` has one aggregate row per book, so the join produces at most one result candidate per catalog book.

The inner join naturally excludes:

- catalog books with no current borrower;
- borrowing aggregates whose book ID has no matching catalog row, should inconsistent data exist.

**Testing zero availability**

Available copies are conceptually

`total_copies - current_borrowers`.

This equals zero precisely when

`current_borrowers = total_copies`,

which is the source’s `WHERE` condition. Only fully borrowed titles remain.

The query assumes the transaction data respects inventory and cannot have more simultaneous active borrowings than `total_copies`. If inconsistent data allowed `current_borrowers > total_copies`, availability would be negative rather than literally zero, and the equality filter would exclude it. Under normal library integrity, equality is the exact sold-out/fully-borrowed condition.

**Selecting the requested columns**

The final projection includes:

- book identifier;
- title;
- author;
- genre;
- publication year;
- active borrower count.

`total_copies` is used to decide eligibility but is not requested in the result, so it is correctly omitted.

Borrower names and transaction dates are also unnecessary after aggregation. The result is one row per unavailable book, not one row per borrower.

**Ordering the output**

`ORDER BY 6 DESC, 2` uses output-column positions.

- Column six is `current_borrowers`, sorted descending so books with more active copies appear first.
- Column two is `title`, ascending by default, providing the required tie-breaker.

Book ID, author, genre, and publication year do not participate in ordering.

**A representative flow**

If a catalog book owns three copies and has five historical borrowing records, but only three records have null return dates, `T` produces `current_borrowers=3`. Joining reveals `total_copies=3`, so equality holds and the book is returned.

If another three-copy book has two active and several returned records, only the two active rows are counted. Equality fails, correctly reflecting one available copy.

## Complexity detail

SQL runtime depends on indexes and the database optimizer. Let `R` be the number of borrowing records and `B` the number of catalog books.

The active-record scan is `O(R)`. A sort-based group may cost `O(R\log R)`, while hash aggregation can be expected linear. Joining grouped counts to books can be near `O(B+R)` with hashing or indexed lookups, or require additional sorting under a merge plan. Sorting the final qualifying rows is bounded by `O(B\log B)`.

A conservative sort-based description is

$$
O(R\log R + B\log B),
$$

matching the manifest. An index beginning with `return_date` and/or `book_id` may reduce scan and grouping costs depending on selectivity and plan.

Logical working storage for active aggregates, catalog access, and output is `O(B+R)` in the broad manifest bound. Actual peak memory can be smaller with streaming or larger on disk if grouping/sorting spills.

## Alternatives and edge cases

- **Join then group:** Joining active borrowing rows to the catalog before grouping can produce the same answer, but it repeats book metadata across every active record during aggregation. Pre-aggregating keeps the intermediate relation compact.
- **Correlated count subquery:** Counting active records separately for every catalog row is readable but may repeat work without an effective book-indexed plan.
- **Conditional aggregation:** Grouping all borrowing history and summing `return_date IS NULL` can work, but filtering active rows first avoids carrying returned transactions into grouping.
- **Use COUNT(*) instead of COUNT(1):** In MySQL these are equivalent for counting group rows here; neither depends on nullable column values.
- **No active loans:** `T` is empty and the result is empty.
- **Some copies available:** Active count below total copies fails equality and is excluded.
- **Exactly all copies borrowed:** Equality succeeds, including a one-copy book with one active loan.
- **Returned transactions:** Non-null return dates are removed before counting, regardless of how many historical loans exist.
- **More active records than copies:** The current equality source excludes this inconsistent case; a defensive “no positive availability” policy would use `>=` instead.
- **Catalog book missing from records:** The inner join excludes it, which is correct because it is not currently borrowed.
- **Title ties:** The specified keys do not add another tie-breaker, so rows with equal count and title may appear in any relative order.
- **Null comparison:** `IS NULL` is required; `return_date = NULL` would not select active rows.
- **Positional ordering:** `ORDER BY 6 DESC, 2` is concise but sensitive to select-list reordering. Naming the columns explicitly would be more maintainable without changing behavior.
- **Inventory interpretation:** Each active record is treated as one borrowed copy; `quantity` does not exist in this schema, so transaction-row count is the appropriate measure.
