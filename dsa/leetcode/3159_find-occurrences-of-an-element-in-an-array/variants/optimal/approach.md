## General

**Precompute the ordered occurrence positions once**

Every query asks about the same target value `x`. Scanning `nums` independently for each query would repeat identical work.

The list comprehension

`ids = [i for i, v in enumerate(nums) if v == x]`

collects exactly the zero-based indices where `x` occurs. Because `enumerate` visits the array from left to right, `ids` is already in increasing order.

Its entries have a direct meaning:

- `ids[0]` is the first occurrence's index;
- `ids[1]` is the second occurrence's index;
- in general, `ids[k - 1]` is the $k$th occurrence's index.

No sorting or frequency map is required.

**Convert one-based query numbers to zero-based list positions**

Query values are one-based ordinals. For query `i`, the desired list position is `i - 1`.

If `i - 1 < len(ids)`, that occurrence exists and the code returns `ids[i - 1]`. Otherwise, fewer than `i` copies of `x` exist, so it returns -1.

The constraints guarantee `i >= 1`, making `i - 1` nonnegative. Without that guarantee, query zero would incorrectly use Python's negative indexing when `ids` is nonempty.

The output list comprehension preserves query order. Queries do not need to be sorted, and repeated queries correctly produce repeated answers.

**Example**

For `nums = [1,3,1,7]` and `x = 1`, preprocessing produces `ids = [0,2]`.

- Query 1 reads `ids[0] = 0`.
- Query 3 requests position 2, which is not less than list length 2, so it returns -1.
- Query 2 reads `ids[1] = 2`.
- Query 4 also returns -1.

This produces `[0,-1,2,-1]`.

If `x` never appears, `ids` is empty. Every positive query has `i - 1 >= 0 = len(ids)`, so all answers are -1 without any special branch.


During preprocessing, an index enters `ids` if and only if the value at that index equals `x`. Since indices are visited in increasing order, the list is exactly the occurrence sequence required by ordinal queries.

For a query $k$, if $k\le\lvert\texttt{ids}\rvert$, the element at zero-based position $k-1$ is by construction the $k$th occurrence. If $k$ exceeds the list length, no $k$th occurrence exists and -1 is required. The conditional implements these two exhaustive cases.

**Why limit the stored information to x**

Queries never ask about another target value. Storing positions for every distinct number would use more memory and preprocessing bookkeeping without helping. A single filtered index list is the exact reusable information.

The indices are original array positions. The method never removes elements or creates a compressed version of `nums` that would change them.

**Why direct ordinal lookup is possible**

An occurrence number is a rank among matches, not an array index and not a value count within a prefix supplied by the query. Once all matching positions are written in sorted order, the rank-to-index relationship never changes. The first list entry always represents rank one, even when its original array index is large; gaps occupied by non-`x` values simply do not appear in `ids`.

This also explains why binary search is unnecessary. Binary search would answer questions such as “how many occurrences lie before array position $p$?” Here the query already supplies the desired rank, which is the exact list offset after subtracting one.

Preprocessing is shared by all queries. Even if the same very large ordinal appears many times, each answer requires only the same bounds comparison and does not rescan either input.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$, $q=\lvert\texttt{queries}\rvert$, and $r$ be the number of occurrences of `x`.

Preprocessing scans $n$ values and takes $O(n)$ time. Each query is answered in $O(1)$, so query processing takes $O(q)$. Total time is $O(n+q)$.

The occurrence list uses $O(r)$ auxiliary space, bounded by $O(n)$. The returned answer uses $O(q)$ required output space. Excluding output, the tighter space bound is $O(r)$.

All list accesses and comparisons are constant time. The input arrays are not modified.

This is asymptotically optimal when both the array and all queries must be read.

## Alternatives and edge cases

- **Scan for each query:** It uses no occurrence list but can take $O(nq)$ time.
- **Map every value to positions:** Useful if queries named different target values, but wasteful when all ask about one fixed `x`.
- **Binary search cumulative counts:** A prefix count array plus binary search can locate occurrences, but direct stored indices answer faster and use comparable space.
- **Sort queries by ordinal:** Unnecessary because lookup is already constant time and output must preserve original order.
- **x absent:** `ids` is empty and every answer is -1.
- **x at every position:** `ids` contains `0,1,\ldots,n-1`, so query $k$ returns $k-1$ when in range.
- **First occurrence:** Query 1 maps to list index 0.
- **Too-large query:** The length comparison returns -1 without an out-of-range access.
- **Repeated queries:** Each independently reads the same stored index and returns the same result.
- **Unsorted queries:** Their order has no effect on correctness.
- **Positive-query guarantee:** It prevents accidental negative indexing for query zero.
- **Input preservation:** Only a new occurrence list and result list are created.
