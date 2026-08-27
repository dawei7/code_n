# Guided Example: Find Books with No Available Copies

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"library_books": [{"book_id": 1, "title": "The Great Gatsby", "author": "F. Scott", "genre": "Fiction", "publication_year": 1925, "total_copies": 3}, {"book_id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction", "publication_year": 1960, "total_copies": 3}, {"book_id": 3, "title": "1984", "author": "George Orwell", "genre": "Dystopian", "publication_year": 1949, "total_copies": 1}, {"book_id": 4, "title": "Pride and Prejudice", "author": "Jane Austen", "genre": "Romance", "publication_year": 1813, "total_copies": 2}, {"book_id": 5, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "genre": "Fiction", "publication_year": 1951, "total_copies": 1}, {"book_id": 6, "title": "Brave New World", "author": "Aldous Huxley", "genre": "Dystopian", "publication_year": 1932, "total_copies": 4}], "borrowing_records": [{"record_id": 1, "book_id": 1, "borrower_name": "Alice Smith", "borrow_date": "2024-01-15", "return_date": null}, {"record_id": 2, "book_id": 1, "borrower_name": "Bob Johnson", "borrow_date": "2024-01-20", "return_date": null}, {"record_id": 3, "book_id": 2, "borrower_name": "Carol White", "borrow_date": "2024-01-10", "return_date": "2024-01-25"}, {"record_id": 4, "book_id": 3, "borrower_name": "David Brown", "borrow_date": "2024-02-01", "return_date": null}, {"record_id": 5, "book_id": 4, "borrower_name": "Emma Wilson", "borrow_date": "2024-01-05", "return_date": null}, {"record_id": 6, "book_id": 5, "borrower_name": "Frank Davis", "borrow_date": "2024-01-18", "return_date": "2024-02-10"}, {"record_id": 7, "book_id": 1, "borrower_name": "Grace Miller", "borrow_date": "2024-02-05", "return_date": null}, {"record_id": 8, "book_id": 6, "borrower_name": "Henry Taylor", "borrow_date": "2024-01-12", "return_date": null}, {"record_id": 9, "book_id": 2, "borrower_name": "Ivan Clark", "borrow_date": "2024-02-12", "return_date": null}, {"record_id": 10, "book_id": 2, "borrower_name": "Jane Adams", "borrow_date": "2024-02-15", "return_date": null}]}}`
- **Required output:** `{"columns": ["book_id", "title", "author", "genre", "publication_year", "current_borrowers"], "rows": [[1, "The Great Gatsby", "F. Scott", "Fiction", 1925, 3], [3, "1984", "George Orwell", "Dystopian", 1949, 1]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: $\text{library}_{books}$

The objective is to compute `{"columns": ["book_id", "title", "author", "genre", "publication_year", "current_borrowers"], "rows": [[1, "The Great Gatsby", "F. Scott", "Fiction", 1925, 3], [3, "1984", "George Orwell", "Dystopian", 1949, 1]]}` from `{"tables": {"library_books": [{"book_id": 1, "title": "The Great Gatsby", "author": "F. Scott", "genre": "Fiction", "publication_year": 1925, "total_copies": 3}, {"book_id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction", "publication_year": 1960, "total_copies": 3}, {"book_id": 3, "title": "1984", "author": "George Orwell", "genre": "Dystopian", "publication_year": 1949, "total_copies": 1}, {"book_id": 4, "title": "Pride and Prejudice", "author": "Jane Austen", "genre": "Romance", "publication_year": 1813, "total_copies": 2}, {"book_id": 5, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "genre": "Fiction", "publication_year": 1951, "total_copies": 1}, {"book_id": 6, "title": "Brave New World", "author": "Aldous Huxley", "genre": "Dystopian", "publication_year": 1932, "total_copies": 4}], "borrowing_records": [{"record_id": 1, "book_id": 1, "borrower_name": "Alice Smith", "borrow_date": "2024-01-15", "return_date": null}, {"record_id": 2, "book_id": 1, "borrower_name": "Bob Johnson", "borrow_date": "2024-01-20", "return_date": null}, {"record_id": 3, "book_id": 2, "borrower_name": "Carol White", "borrow_date": "2024-01-10", "return_date": "2024-01-25"}, {"record_id": 4, "book_id": 3, "borrower_name": "David Brown", "borrow_date": "2024-02-01", "return_date": null}, {"record_id": 5, "book_id": 4, "borrower_name": "Emma Wilson", "borrow_date": "2024-01-05", "return_date": null}, {"record_id": 6, "book_id": 5, "borrower_name": "Frank Davis", "borrow_date": "2024-01-18", "return_date": "2024-02-10"}, {"record_id": 7, "book_id": 1, "borrower_name": "Grace Miller", "borrow_date": "2024-02-05", "return_date": null}, {"record_id": 8, "book_id": 6, "borrower_name": "Henry Taylor", "borrow_date": "2024-01-12", "return_date": null}, {"record_id": 9, "book_id": 2, "borrower_name": "Ivan Clark", "borrow_date": "2024-02-12", "return_date": null}, {"record_id": 10, "book_id": 2, "borrower_name": "Jane Adams", "borrow_date": "2024-02-15", "return_date": null}]}}` while avoiding redundant calculations and unnecessary overhead.

A naive or brute-force exploration risks evaluating infeasible states or repeating subproblem computations. The optimal method establishes a clear invariant that advances deterministically toward the goal.

---

## 2. Conceptual Foundation & Invariants

We maintain the core conceptual parameters and state variables:

| State Parameter | Role & Purpose | Initial State |
|---|---|---|
| Primary State | Tracks active elements, frontier indices, or DP table cells | Initialized at boundary |
| Accumulator | Preserves confirmed optimal sub-answers or counts | Empty / Neutral |

> **Invariant.** At every processing step, all previously evaluated subproblems strictly satisfy the problem constraints, and no viable candidate solution has been omitted.

---

## 3. Step-by-Step Worked Execution

### Step 1: Identifying active loans

`return_date IS NULL` is the statement’s exact definition of a currently borrowed copy. A completed record has a non-null return date and must not reduce present availability.

The condition belongs in `WHERE` before grouping. This ensures each group contains active transactions only; counting all records and trying to interpret returned loans afterward would inflate current borrowers.

SQL requires `IS NULL` rather than `= NULL` because null represents an unknown/missing value and ordinary equality with null does not evaluate to true.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"library_books": [{"book_id": 1, "title": "The Great Gatsby", "author": "F. Scott", "genre": "Fiction", "publication_year": 1925, "total_copies": 3}, {"book_id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction", "publication_year": 1960, "total_copies": 3}, {"book_id": 3, "title": "1984", "author": "George Orwell", "genre": "Dystopian", "publication_year": 1949, "total_copies": 1}, {"book_id": 4, "title": "Pride and Prejudice", "author": "Jane Austen", "genre": "Romance", "publication_year": 1813, "total_copies": 2}, {"book_id": 5, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "genre": "Fiction", "publication_year": 1951, "total_copies": 1}, {"book_id": 6, "title": "Brave New World", "author": "Aldous Huxley", "genre": "Dystopian", "publication_year": 1932, "total_copies": 4}], "borrowing_records": [{"record_id": 1, "book_id": 1, "borrower_name": "Alice Smith", "borrow_date": "2024-01-15", "return_date": null}, {"record_id": 2, "book_id": 1, "borrower_name": "Bob Johnson", "borrow_date": "2024-01-20", "return_date": null}, {"record_id": 3, "book_id": 2, "borrower_name": "Carol White", "borrow_date": "2024-01-10", "return_date": "2024-01-25"}, {"record_id": 4, "book_id": 3, "borrower_name": "David Brown", "borrow_date": "2024-02-01", "return_date": null}, {"record_id": 5, "book_id": 4, "borrower_name": "Emma Wilson", "borrow_date": "2024-01-05", "return_date": null}, {"record_id": 6, "book_id": 5, "borrower_name": "Frank Davis", "borrow_date": "2024-01-18", "return_date": "2024-02-10"}, {"record_id": 7, "book_id": 1, "borrower_name": "Grace Miller", "borrow_date": "2024-02-05", "return_date": null}, {"record_id": 8, "book_id": 6, "borrower_name": "Henry Taylor", "borrow_date": "2024-01-12", "return_date": null}, {"record_id": 9, "book_id": 2, "borrower_name": "Ivan Clark", "borrow_date": "2024-02-12", "return_date": null}, {"record_id": 10, "book_id": 2, "borrower_name": "Jane Adams", "borrow_date": "2024-02-15", "return_date": null}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Counting current borrowers per book

The CTE groups active records by `book_id` and evaluates `COUNT(1)`. Since each borrowing record represents one transaction for one copy, this count is the number of currently borrowed copies for that book.

The alias `current_borrowers` is used later for filtering, projection, and ordering.

`GROUP BY 1` is positional shorthand for grouping by the first selected expression, `book_id`.

Books with no active record have no row in `T`. That is desirable because a book with every copy available cannot satisfy “currently borrowed” and “zero copies available.”

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The CTE groups active records by `book_id` and evaluates `CO... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Joining counts to catalog data

`library_books JOIN T USING (book_id)` attaches title, author, genre, publication year, and total copies to each active-loan count.

`library_books.book_id` is unique, and `T` has one aggregate row per book, so the join produces at most one result candidate per catalog book.

The inner join naturally excludes:

- catalog books with no current borrower;
- borrowing aggregates whose book ID has no matching catalog row, should inconsistent data exist.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["book_id", "title", "author", "genre", "publication_year", "current_borrowers"], "rows": [[1, "The Great Gatsby", "F. Scott", "Fiction", 1925, 3], [3, "1984", "George Orwell", "Dystopian", 1949, 1]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"library_books": [{"book_id": 1, "title": "The Great Gatsby", "author": "F. Scott", "genre": "Fiction", "publication_year": 1925, "total_copies": 3}, {"book_id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction", "publication_year": 1960, "total_copies": 3}, {"book_id": 3, "title": "1984", "author": "George Orwell", "genre": "Dystopian", "publication_year": 1949, "total_copies": 1}, {"book_id": 4, "title": "Pride and Prejudice", "author": "Jane Austen", "genre": "Romance", "publication_year": 1813, "total_copies": 2}, {"book_id": 5, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "genre": "Fiction", "publication_year": 1951, "total_copies": 1}, {"book_id": 6, "title": "Brave New World", "author": "Aldous Huxley", "genre": "Dystopian", "publication_year": 1932, "total_copies": 4}], "borrowing_records": [{"record_id": 1, "book_id": 1, "borrower_name": "Alice Smith", "borrow_date": "2024-01-15", "return_date": null}, {"record_id": 2, "book_id": 1, "borrower_name": "Bob Johnson", "borrow_date": "2024-01-20", "return_date": null}, {"record_id": 3, "book_id": 2, "borrower_name": "Carol White", "borrow_date": "2024-01-10", "return_date": "2024-01-25"}, {"record_id": 4, "book_id": 3, "borrower_name": "David Brown", "borrow_date": "2024-02-01", "return_date": null}, {"record_id": 5, "book_id": 4, "borrower_name": "Emma Wilson", "borrow_date": "2024-01-05", "return_date": null}, {"record_id": 6, "book_id": 5, "borrower_name": "Frank Davis", "borrow_date": "2024-01-18", "return_date": "2024-02-10"}, {"record_id": 7, "book_id": 1, "borrower_name": "Grace Miller", "borrow_date": "2024-02-05", "return_date": null}, {"record_id": 8, "book_id": 6, "borrower_name": "Henry Taylor", "borrow_date": "2024-01-12", "return_date": null}, {"record_id": 9, "book_id": 2, "borrower_name": "Ivan Clark", "borrow_date": "2024-02-12", "return_date": null}, {"record_id": 10, "book_id": 2, "borrower_name": "Jane Adams", "borrow_date": "2024-02-15", "return_date": null}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["book_id", "title", "author", "genre", "publication_year", "current_borrowers"], "rows": [[1, "The Great Gatsby", "F. Scott", "Fiction", 1925, 3], [3, "1984", "George Orwell", "Dystopian", 1949, 1]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Join then group:** Joining active borrowing ro:** - **Join then group:** Joining active borrowing rows to the catalog before grouping can produce the same answer, but it repeats book metadata across every active record during aggregation. Pre-aggregating keeps the intermediate relation compact.
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
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(B log B + R log R)$. SQL runtime depends on indexes and the database optimizer. Let `R` be the number of borrowing records and `B` the number of catalog books.
- **Auxiliary Space Complexity:** $O(B + R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
