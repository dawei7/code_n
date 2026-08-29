# Guided Example: Books with NULL Ratings

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"books": [{"book_id": 1, "title": "The Great Gatsby", "author": "F. Scott", "published_year": 1925, "rating": 4.5}, {"book_id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "published_year": 1960, "rating": null}, {"book_id": 3, "title": "Pride and Prejudice", "author": "Jane Austen", "published_year": 1813, "rating": 4.8}, {"book_id": 4, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "published_year": 1951, "rating": null}, {"book_id": 5, "title": "Animal Farm", "author": "George Orwell", "published_year": 1945, "rating": 4.2}, {"book_id": 6, "title": "Lord of the Flies", "author": "William Golding", "published_year": 1954, "rating": null}]}}`
- **Required output:** `{"columns": ["book_id", "title", "author", "published_year"], "rows": [[2, "To Kill a Mockingbird", "Harper Lee", 1960], [4, "The Catcher in the Rye", "J.D. Salinger", 1951], [6, "Lord of the Flies", "William Golding", 1954]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `books`

The objective is to compute `{"columns": ["book_id", "title", "author", "published_year"], "rows": [[2, "To Kill a Mockingbird", "Harper Lee", 1960], [4, "The Catcher in the Rye", "J.D. Salinger", 1951], [6, "Lord of the Flies", "William Golding", 1954]]}` from `{"tables": {"books": [{"book_id": 1, "title": "The Great Gatsby", "author": "F. Scott", "published_year": 1925, "rating": 4.5}, {"book_id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "published_year": 1960, "rating": null}, {"book_id": 3, "title": "Pride and Prejudice", "author": "Jane Austen", "published_year": 1813, "rating": 4.8}, {"book_id": 4, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "published_year": 1951, "rating": null}, {"book_id": 5, "title": "Animal Farm", "author": "George Orwell", "published_year": 1945, "rating": 4.2}, {"book_id": 6, "title": "Lord of the Flies", "author": "William Golding", "published_year": 1954, "rating": null}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**Start from the only table involved.** Every required output row comes from `books`, so the query uses a direct `FROM books` scan with no join, grouping, or subquery. The unique key `book_id` identifies each source row, which means the result cannot acquire duplicates from relational combination.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"books": [{"book_id": 1, "title": "The Great Gatsby", "author": "F. Scott", "published_year": 1925, "rating": 4.5}, {"book_id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "published_year": 1960, "rating": null}, {"book_id": 3, "title": "Pride and Prejudice", "author": "Jane Austen", "published_year": 1813, "rating": 4.8}, {"book_id": 4, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "published_year": 1951, "rating": null}, {"book_id": 5, "title": "Animal Farm", "author": "George Orwell", "published_year": 1945, "rating": 4.2}, {"book_id": 6, "title": "Lord of the Flies", "author": "William Golding", "published_year": 1954, "rating": null}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

**Filter with SQL's dedicated NULL predicate.** The requirement is specifically to find rows whose `rating` is missing. SQL `NULL` does not behave like an ordinary value. It represents an unknown or absent value, and comparisons involving it use three-valued logic.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Writing `rating = NULL` would not produce true even when `rating` is null. The equality result is unknown, and a `WHERE` clause keeps only rows whose predicate is true. The exact source correctly uses

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["book_id", "title", "author", "published_year"], "rows": [[2, "To Kill a Mockingbird", "Harper Lee", 1960], [4, "The Catcher in the Rye", "J.D. Salinger", 1951], [6, "Lord of the Flies", "William Golding", 1954]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"books": [{"book_id": 1, "title": "The Great Gatsby", "author": "F. Scott", "published_year": 1925, "rating": 4.5}, {"book_id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "published_year": 1960, "rating": null}, {"book_id": 3, "title": "Pride and Prejudice", "author": "Jane Austen", "published_year": 1813, "rating": 4.8}, {"book_id": 4, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "published_year": 1951, "rating": null}, {"book_id": 5, "title": "Animal Farm", "author": "George Orwell", "published_year": 1945, "rating": 4.2}, {"book_id": 6, "title": "Lord of the Flies", "author": "William Golding", "published_year": 1954, "rating": null}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["book_id", "title", "author", "published_year"], "rows": [[2, "To Kill a Mockingbird", "Harper Lee", 1960], [4, "The Catcher in the Rye", "J.D. Salinger", 1951], [6, "Lord of the Flies", "William Golding", 1954]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **`rating = NULL`:** This is incorrect because equality with `NULL` evaluates to unknown rather than true.
- **`rating IS NOT NULL`:** It selects the opposite set: books that already have ratings.
- **Explicit ordering name:** `ORDER BY book_id ASC` is equivalent here and more robust if the select-list order changes.
- **Ordinal ordering:** `ORDER BY 1` refers to `book_id` only because it is the first projected expression.
- **Default direction:** Omitting the direction means ascending, which matches the requirement.
- **Numeric rating zero:** Zero is not null and must not be returned.
- **All ratings null:** Every row survives, then all rows are sorted by identifier.
- **No ratings null:** The result is an empty table with the projected schema.
- **Single matching row:** Sorting has no visible effect but remains correct.
- **Unique identifier:** `book_id` uniqueness removes ordering ties and prevents duplicate source identities.
- **Nullable descriptive columns:** Even if title or author were null, row selection still depends only on `rating`.
- **Projection order:** The output columns appear in the exact sequence written in `SELECT`.
- **No `SELECT *`:** Selecting all columns would incorrectly include `rating` and make the output depend on future schema additions.
- **No join:** A join would add unnecessary work and risk multiplying rows.
- **Index availability:** It may improve the physical plan but does not change query semantics.
- **MySQL comment:** The leading source comment is inert and simply identifies the expected SQL dialect.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n log n)$. Let $n$ be the number of rows in `books` and $r$ the number with null ratings. In a generic execution without a helpful index, filtering scans $O(n)$ rows and sorting the survivors costs $O(r\log r)$ time. Since $r\le n$, the manifest summarizes this as $O(n\log n)$ time.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
