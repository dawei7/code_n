## General

An unreturned row in `borrowing_records` represents one currently unavailable copy. Filter to those rows during the join with `library_books`, so returned history never enters an aggregate.

Group the joined rows by the book identity, descriptive output fields, and `total_copies`. The inner join also guarantees that every surviving group has at least one current borrower. `COUNT(*)` is therefore the active-loan count for that book. A `HAVING` condition keeps exactly the groups whose count equals `total_copies`, which is equivalent to zero available copies under the stated inventory model.

Project the required book fields and name the aggregate `current_borrowers`. Finally, apply both ordering keys explicitly: larger borrower counts first, and titles alphabetically when counts tie. Since every active borrowing record enters exactly one book group, the aggregate is complete and cannot double-count a record.

## Complexity detail

Let $B$ be the number of catalog rows and $R$ the number of borrowing records. In a comparison-based execution plan without assuming extra covering indexes, joining, grouping, and ordering cost at most $O(B\log B+R\log R)$ time and $O(B+R)$ working space. A database may choose indexed or hash-based operators that improve the practical constants or expected join cost.

The benchmark sets $B=R=S$, with one active loan for each one-copy book. The accepted grouped join processes the relations together, whereas the calibrated correlated alternative scans the entire borrowing table separately for every catalog row, creating quadratic growth.

## Alternatives and edge cases

- **Correlated active-loan count:** A scalar subquery per book is readable, but without a supporting `book_id` index it can rescan all borrowing records and cost $O(BR)$.
- **Left join all books:** It can preserve books with no active loans, which are not requested; an inner join to already filtered active records expresses the contract directly.
- **Returned loans:** Any row with a non-`NULL` `return_date` must be removed before aggregation.
- **Partially available book:** An active-loan count smaller than `total_copies` excludes the book even though it is currently borrowed by someone.
- **Borrower-count tie:** Titles determine the required secondary ascending order.
- **Historical duplicates:** Each borrowing record is a separate transaction, but only currently unreturned transactions contribute to the current count.
