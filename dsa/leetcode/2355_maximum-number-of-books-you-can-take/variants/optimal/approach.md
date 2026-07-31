## General

**Fix the right endpoint.** Suppose a valid section ends at shelf $i$. To
maximize its total, take all `books[i]` books from that final shelf. Moving one
position left can reduce the chosen quantity by at least one, so shelf $p$
could contribute at most
$\texttt{books[i]}-(i-p)$. This descending arithmetic sequence is optimal
until an earlier shelf's own capacity becomes the tighter restriction.

**Recognize when an earlier optimum can be reused.** Rewrite the comparison
between shelf $j$ and the arithmetic sequence ending at $i$:

$$
\texttt{books[j]} < \texttt{books[i]}-(i-j)
\quad\Longleftrightarrow\quad
\texttt{books[j]}-j < \texttt{books[i]}-i.
$$

Let $j$ be the nearest earlier index satisfying that strict inequality. The
best section ending at $j$ can remain unchanged, and shelves $j+1$ through $i$
can follow the maximal consecutive quantities ending at `books[i]`. Any
intervening index whose `books[index] - index` is greater than or equal to the
current value cannot be this boundary for the current shelf or for a later
shelf that discards it, so a monotonic stack can remove it permanently.

**Sum the new arithmetic segment.** If no reusable boundary exists, use
$j=-1$. There are at most $i-j$ new shelves, but positive strictly increasing
quantities ending at `books[i]` contain at most `books[i]` terms. Therefore

$$
m=\min(\texttt{books[i]},\,i-j)
$$

and the first quantity is $\texttt{books[i]}-m+1$. Their sum is

$$
\frac{m\bigl(2\texttt{books[i]}-m+1\bigr)}{2}.
$$

Define `dp[i]` as the largest valid total for a section ending at $i$. Add this
arithmetic sum to `dp[j]` when $j\ge 0$, or to zero otherwise. The boundary
choice is correct because every index after $j$ is governed by the arithmetic
descent from $i$, while the strict transformed inequality guarantees the
optimal section ending at $j$ remains strictly below its first appended
quantity. Taking the maximum `dp[i]` over all endpoints considers every
possible optimal section.

## Complexity detail

Each index is pushed onto the monotonic stack once and popped at most once.
All arithmetic and dynamic-programming work outside those stack operations is
constant per index, so the running time is $O(n)$. The stack and `dp` array can
each hold $n$ entries, giving $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Scan left from every endpoint:** Building the maximal descending sequence
  separately for each right endpoint is correct, but takes $O(n^2)$ time on
  long increasing-capacity arrays.
- **Segment tree dynamic programming:** Range searches can locate the previous
  compatible boundary in $O(\log n)$ per shelf, but the monotonic structure
  makes that machinery unnecessary.
- **Zero-capacity shelves:** A zero cannot contribute a positive quantity, so
  the formula chooses zero new terms when it is the endpoint and naturally
  prevents a positive sequence from extending through it.
- **Equal transformed values:** The stack must pop on equality as well as on a
  greater value; the reusable boundary requires a strict inequality.
- **Large totals:** Up to $10^5$ shelves may each contribute near $10^5$, so
  the total must be accumulated with a 64-bit integer type outside Python.
