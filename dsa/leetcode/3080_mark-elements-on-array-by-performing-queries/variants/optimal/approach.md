## General

**Maintain the sum rather than recomputing it.** `s = sum(nums)` begins as the sum of all unmarked elements. Whenever an element is marked for the first time, subtract its value. Then `s` is always the answer after the current query.

Boolean list `mark` records whether each index has already been removed from that sum, preventing double subtraction.

**Pre-sort the global marking priority.** `arr` contains pairs `(value,index)` sorted by Python tuple order. Values come first, and equal values are ordered by smaller index. This exactly matches the rule for choosing smallest unmarked elements with index tie-breaking.

**Use one persistent cursor.** `j` points into sorted `arr` and never moves backward. For a query, the while-loop examines candidates in priority order:

- if the candidate index is unmarked, mark it, subtract its value, and decrement local `k`;
- if it was already marked explicitly or by an earlier query, skip it;
- advance `j` in either case.

Once a sorted candidate has been examined, it can never become unmarked later, so revisiting it is unnecessary. Persistence makes total while-loop iterations across all queries at most $N$.

**Handle the query's explicit index first.** If `index` is unmarked, mark and subtract it before selecting $k$ smallest remaining elements. This ordering matters: the explicit element must not also consume one of the $k$ automatic selections.

If it is already marked, nothing changes and the query still marks up to $k$ other unmarked elements.

**A trace.** Suppose the smallest sorted pair points to an index explicitly marked in the first query. When automatic selection reaches it later, `mark` is true, so it advances without decrementing $k$ or subtracting again. The next genuinely unmarked pair becomes the selection.

**Fewer than $k$ elements remaining.** The condition `j < n` stops at the end of `arr`. If no unmarked values remain, the loop ends even with positive `k` and answer sum is zero.
Before each query, `s` equals the sum of indices whose mark flag is false, and `j` has passed only entries already marked. Explicit handling applies the first required action. The sorted cursor then chooses exactly the next $k$ unmarked entries in value-index order. Each first marking updates flag and sum consistently, preserving the invariant. Appending `s` therefore records the required result.

**Why total automatic work is linear after sorting.** A candidate skipped because already marked never needs another look. A candidate selected becomes marked forever. Every cursor increment permanently eliminates one sorted entry, so nested-looking query loops do not multiply to $MN$.

## Complexity detail

Sorting $N$ pairs costs $O(N\log N)$. Initial sum and pair construction cost $O(N)$. Query headers cost $O(M)$, while all cursor-loop iterations together cost $O(N)$. Total time is $O(N\log N+M)$.

`mark`, `arr`, and output `ans` use $O(N+M)$ space; with $M\le N$, this is $O(N)$. Input arrays are not modified, although local loop variable `k` is decremented.

## Alternatives and edge cases

- **Min-heap:** Store all value-index pairs and pop until finding unmarked entries. It also works in $O((N+M)\log N)$ but pays logarithmic cost per automatic marking.
- **Re-sort remaining elements per query:** It can become quadratic or worse and repeats a fixed global ordering.
- **Recompute unmarked sum:** Scanning `nums` after every query costs $O(MN)$.
- **Explicit index already marked:** It is skipped without subtracting twice.
- **Explicit index is next smallest:** Marking it first makes the cursor skip it, so $k$ additional elements are still chosen.
- **Equal values:** Tuple sorting chooses smaller original index.
- **$k=0$:** Only the explicit index action occurs.
- **Too few unmarked elements:** All remaining ones are marked and the sum becomes zero.
- **All elements marked early:** Later queries append zero with no further cursor work.
- **Persistent cursor:** Its monotonicity is the key to the linear post-sort processing bound.
- **Why explicit marking does not move `j` immediately:** That index may lie later in sorted order. Leaving the cursor unchanged is safe because its mark flag will cause a skip when reached.
- **Sum invariant starts correctly:** Before any marks, every index is unmarked, so `sum(nums)` exactly matches the invariant's definition.
- **Query order matters:** Mark flags persist across queries, and answers are appended after each query. Reordering queries could change which elements remain for later automatic choices.
- **Local `k` mutation:** Unpacking each query creates a new integer reference. Decrementing it does not alter the nested list in `queries`.
- **Positive values:** Subtracting newly marked values makes `s` monotonically nonincreasing and never negative under correct one-time marking.
- **Output size:** One sum is appended per query, so `len(ans)==len(queries)` even after all elements are marked.
- **Why cursor order remains valid after explicit marks:** Removing arbitrary elements from a fixed total order leaves the relative priority of every surviving element unchanged.
- **Index tie-break is encoded once:** Sorting tuples eliminates the need to compare indices inside every query loop.
