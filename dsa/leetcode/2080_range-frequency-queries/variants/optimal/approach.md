## General

**Preprocess positions because the array never changes**

The class receives the array once, then answers as many as $10^5$ range-frequency queries. Scanning `arr[left:right + 1]` for every call would repeat work on the same unchanging data and could become quadratic across all queries.

The useful information for a particular value is not every element in a requested interval. It is the sorted list of indices where that value occurs.

The constructor creates `self.g` as a mapping from each value to a list of positions. It traverses `arr` from left to right with `enumerate`. For every index `i` holding value `x`, it appends `i` to `self.g[x]`.

Because indices are encountered in increasing order, each position list is automatically sorted. No separate sorting pass is required.

For example, if

`arr = [12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]`,

then the relevant lists include:

- `self.g[33] = [1, 7]`;
- `self.g[22] = [4, 8]`;
- `self.g[56] = [3, 11]`.

A query for value 33 can now ignore every position belonging to other values.

**Turn an inclusive interval into two insertion boundaries**

For `query(left, right, value)`, the variable `idx` refers to the sorted occurrence list for `value`. The answer is the number of entries in `idx` that satisfy

$$
\texttt{left}\le \text{index}\le \texttt{right}.
$$

The code finds the first qualifying list position with

`l = bisect_left(idx, left)`.

`bisect_left` returns the insertion position before any existing entry equal to its target. Therefore, all entries before `l` are strictly less than `left`, and every entry from `l` onward is at least `left`.

For the other boundary, the source uses

`r = bisect_left(idx, right + 1)`.

Since indices are integers, being strictly less than `right + 1` is equivalent to being at most `right`. Thus `r` is the first list position after all occurrences inside the query's right boundary.

The half-open slice of relevant occurrence entries is conceptually `idx[l:r]`, so its size is `r - l`. The source returns that difference without actually creating the slice.

This is a standard way to handle an inclusive interval: search for the first position at least `left` and the first position at least `right + 1`.

**A concrete query trace**

Using `self.g[33] = [1, 7]`, consider `query(0, 11, 33)`.

- The first index at least 0 is at list position 0, so `l = 0`.
- The first index at least 12 lies after both entries, so `r = 2`.
- The difference is 2, matching the two occurrences at array indices 1 and 7.

Now consider `query(2, 7, 33)`.

- `bisect_left([1, 7], 2)` returns 1 because index 1 is too small and index 7 is the first qualifying occurrence.
- `bisect_left([1, 7], 8)` returns 2 because both stored indices are below 8.
- The answer is $2-1=1$, counting the occurrence exactly at the inclusive right boundary.

If the value appears only outside the requested interval, the two boundaries can be equal, and the method naturally returns zero.

**Why absent values need no special branch**

`self.g` is a `defaultdict(list)`. Accessing `self.g[value]` for a value not present in the original array yields an empty list. Both binary searches on an empty list return 0, so `r - l` is 0.

This avoids an explicit membership test. One subtle implementation detail is that accessing a missing key inserts it into the mapping with an empty list. It does not affect correctness, though many distinct absent queried values can create up to one empty entry per such value.

**Why the returned count is correct**

For a query value, `idx` contains every array index holding that value and no index holding a different value. Its increasing order follows directly from the constructor's left-to-right scan.

The first binary search partitions `idx` so that entries before `l` are outside the range on the left, while entries at or after `l` satisfy the lower boundary. The second partitions it so entries before `r` satisfy the inclusive upper boundary, while entries at or after `r` lie beyond the range.

Consequently, exactly the entries at list positions `l` through `r - 1` satisfy both range boundaries. There are `r - l` of them. Each corresponds one-to-one with an occurrence of `value` in `arr[left...right]`, proving the result.

The preprocessing retains positions but does not keep or mutate the original array. That is sufficient because all later operations ask only about occurrence counts in index ranges.

## Complexity detail

Let $n$ be the length of `arr`, let $Q$ be the number of calls to `query`, and let $f_v$ be the total frequency of the queried value $v$ in the full array.

The constructor visits each element once and appends once, taking $O(n)$ time. Its lists collectively store exactly $n$ indices.

One query performs two binary searches in the list for its value, taking $O(\log f_v)$ time. Since $f_v\le n$, this is $O(\log n)$ in the worst case. Across $Q$ calls, total construction-plus-query time is $O(n+Q\log n)$.

The occurrence lists use $O(n)$ space. Because `defaultdict` creates an empty list for each previously absent value queried, up to $O(Q)$ additional empty mapping entries can appear over the object's lifetime. This matches the manifest's conservative $O(n+Q)$ space bound. If only values present in `arr` are queried, the structure remains $O(n)$.

Each individual query uses only the list reference and two integer boundary positions, so its temporary auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Scan the subarray per query:** This needs no preprocessing beyond retaining the array, but a wide query costs $O(n)$. With up to $10^5$ calls, repeated scanning is too expensive.
- **Prefix counts for every possible value:** A two-dimensional prefix table can answer in $O(1)$ time, but it uses array length times value-domain storage. Position lists provide a better sparse representation and logarithmic queries.
- **Segment tree of frequency maps:** This can answer range counts and support extensions such as updates, but the input is immutable. Its construction, storage, and query logic are more complex than per-value indices.
- **Using `bisect_right(idx, right)`:** This is equivalent to `bisect_left(idx, right + 1)` for integer indices. The source chooses the latter to express the upper boundary as a half-open endpoint.
- **Inclusive right endpoint:** Searching for `right` with `bisect_left` would exclude an occurrence exactly at `right`. Adding one is essential.
- **Value absent from the array:** `idx` is empty, both boundaries are zero, and the answer is zero.
- **Interval contains no occurrence:** Even for a globally present value, `l == r` when no stored position lies inside the range.
- **Single-index interval:** When `left == right`, the result is one exactly when that array position contains `value`, otherwise zero.
- **Whole-array query:** The boundaries span the entire occurrence list, so the answer is the value's full frequency.
- **Repeated identical queries:** No state relevant to answers changes; every call returns the same count. Only a first query for an absent value may create its harmless empty mapping entry.
- **Sortedness dependency:** Binary search is correct because indices are appended during a left-to-right traversal. Appending in arbitrary order would require sorting each list first.
- **No slice allocation:** Returning `r - l` counts the conceptual sublist without copying its elements, keeping per-query space constant.
