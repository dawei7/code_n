## General

**Summarize each book once.** Group `reading_sessions` by `book_id`. Within each group, count all sessions, retain the minimum and maximum rating, and conditionally count ratings at most 2 or at least 4. Those four aggregates contain everything needed to decide whether a book qualifies.

The minimum and maximum establish both sides of the polarization requirement: a minimum at most 2 proves a low rating exists, while a maximum at least 4 proves a high rating exists. The same values produce the rating spread. Comparing the extreme-rating count with $0.6$ times the total count tests the threshold before rounding, so a displayed two-decimal score cannot incorrectly admit a value just below $0.6$.

Apply all group predicates in `HAVING`, then join only the surviving summaries to `books`. Compute and round the score for display. Descending score order ranks stronger polarization first, and descending title order resolves a tie exactly as required.

## Complexity detail

Let $R$ be the number of reading-session rows and $B$ the number of books. With hash aggregation, the session summary takes expected $O(R)$ time and stores at most one aggregate row per book. Sorting at most $B$ qualifying results takes $O(B\log B)$ time. Total expected time is $O(R+B\log B)$ and auxiliary space is $O(B)$.

The benchmark sets its size $N$ to the book count and supplies six sessions per book, so $R=6N$. The accepted grouped query summarizes the relation once and then sorts the result. The comparison query uses correlated subqueries that rescan `reading_sessions` for every book, giving quadratic work as $N$ grows.

## Alternatives and edge cases

- **Correlated aggregate subqueries:** They can calculate every statistic independently, but repeated scans of `reading_sessions` scale quadratically without supporting indexes.
- **Window aggregates:** They can attach per-book statistics to every session row, but then require deduplication and retain more intermediate data than one grouped row per book.
- **Exactly five sessions:** Five is sufficient; the minimum is inclusive.
- **Threshold before rounding:** Test the unrounded fraction against $0.6$, then round only the returned score.
- **Middle ratings:** A rating of 3 contributes to the total session count but not to the extreme-rating numerator.
- **Both opinion sides:** A book containing only high extremes or only low extremes is not polarized, regardless of its score.
- **Tie order:** Equal polarization scores require `title` in descending lexicographic order.
