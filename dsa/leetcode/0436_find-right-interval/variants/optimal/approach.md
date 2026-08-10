## General

**Each query asks for a lower bound among start coordinates**

For interval `i = [start_i,end_i]`, a right interval must have `start_j >= end_i`, and among those starts it must be the smallest. This is exactly a lower-bound query: find the first sorted start coordinate that is not less than `end_i`.

Performing a linear search for every interval would cost $O(n^2)$. The solution preprocesses all starts once, sorts them, and answers every endpoint query with binary search.

**Preserve original indices while sorting**

The list

`arr = sorted((st, i) for i, (st, _) in enumerate(intervals))`

contains `(start, original_index)` pairs. Sorting tuples orders them primarily by `start`. The problem guarantees all start values are unique, so the secondary index order is never needed to break an equal-start tie, but retaining the index is necessary for the output.

The original `intervals` list remains in its input order. `ans` is initialized as `[-1] * n`, making “no right interval” the default for every position.

**Locate the smallest qualifying start**

For original interval index `i`, only its endpoint `ed` matters to the query. The expression

`bisect_left(arr, (ed, -inf))`

returns the insertion position of tuple `(ed,-inf)` in sorted `arr`.

Python tuple comparison first compares starts. Every pair whose start is less than `ed` appears before the insertion point. A pair with start exactly equal to `ed` compares greater than `(ed,-inf)` because every finite original index is greater than negative infinity, so it appears at or after the insertion point. Thus the returned position is the first pair with `start >= ed`.

Using negative infinity in the second tuple component ensures an exact-start match is included. A very large second component could place the insertion point after the matching start and incorrectly skip it.

If `j < n`, `arr[j]` is the smallest qualifying start pair, and `arr[j][1]` is written to `ans[i]`. If `j == n`, every start is smaller than the endpoint, so the initialized `-1` remains.

**Why the first binary-search result is the right interval**

Sorted order guarantees all earlier entries have starts below `end_i` and are invalid. The entry at `j`, if it exists, satisfies the inequality. Every later entry has a start at least as large, so none can improve the minimized-start requirement. Unique starts make the chosen original index unambiguous.

For intervals `[[3,4],[2,3],[1,2]]`, sorted starts are `[(1,2),(2,1),(3,0)]`. Endpoint 4 has insertion index 3 and yields `-1`. Endpoint 3 finds `(3,0)`. Endpoint 2 finds `(2,1)`. Writing by original indices produces `[-1,0,1]`.

**Why an interval may point to itself**

The constraints allow `start_i == end_i`, and the definition permits `i == j`. For such a zero-length interval, its own start equals its end and is a valid qualifying start. Since starts are unique, it is the smallest possible value equal to the endpoint, and binary search can return its own index correctly.

For ordinary intervals with `start_i < end_i`, the interval's own start cannot satisfy `start_i >= end_i`, so it will not select itself.

**One preprocessing order supports all queries**

Only start coordinates are searched. Sorting entire intervals by some combined start/end rule would lose the simple lower-bound relationship or require restoring indices. The pair array isolates the search key while carrying exactly the answer payload.

## Complexity detail

Let $n$ be the number of intervals. Building `arr` takes $O(n)$ time and space. Sorting takes $O(n\log n)$. Each of $n$ endpoint queries takes $O(\log n)$ with `bisect_left`, for another $O(n\log n)$ time. Total time is $O(n\log n)$.

`arr` and `ans` each contain $n$ entries, so space is $O(n)$. The returned `ans` is required output; even excluding it, preprocessing uses $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Linear scan per interval:** Directly test all starts and track the smallest valid one. It is simple but costs $O(n^2)$ time.
- **Separate sorted starts plus a start-to-index map:** Binary-search an integer list and map the found unique start back to its index. This has the same bounds; storing tuples combines both pieces.
- **Ordered tree queries:** Insert starts into a balanced search structure and request ceilings. It is useful for dynamic updates but unnecessary for a static array.
- **Sort endpoints and starts with two pointers:** Offline queries can be processed in sorted endpoint order in $O(n\log n)$ total time, but binary search is more direct.
- **Exact boundary match:** `start_j == end_i` is valid and must not be skipped; `(ed,-inf)` enforces lower-bound behavior.
- **No qualifying start:** Binary search returns `n`, leaving `-1`.
- **Single nonzero-length interval:** Its start is below its end, so no right interval exists.
- **Zero-length interval:** It may correctly select itself.
- **Negative coordinates:** Tuple ordering and negative infinity handle the full range normally.
- **Unique starts:** They guarantee there is only one answer for the minimized start; no tie-breaking rule is needed.
- **Original output order:** Queries iterate over original `intervals`, and results are written to `ans[i]`, independent of sorted preprocessing order.
