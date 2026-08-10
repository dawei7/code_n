## General

**Store positives in arrival order instead of physically prepending.** The problem describes putting each positive value at the front of `seen`. Repeated insertion at the front of a Python list would shift all existing elements and could make the algorithm quadratic.

The source instead appends positives to the end. The most recently seen positive is then the last list element, the second most recent is the second-to-last, and so on. Python negative indexing retrieves exactly that order:

- `seen[-1]` is the first element of the conceptual front-prepended list;
- `seen[-2]` is the second;
- `seen[-k]` is the $k$-th.

This representation preserves the required semantics with constant-time append and lookup.

**Track only the current consecutive run of queries.** Variable `k` counts how many consecutive `-1` values have appeared since the latest positive integer. It starts at zero.

When current `x` is positive, the code appends it to `seen` and resets `k = 0`. Resetting is essential: a later `-1` begins a new query run and should request the most recently visited positive again.

When `x == -1`, the code increments `k`. If `k <= len(seen)`, the requested value exists and `seen[-k]` is appended to `ans`. Otherwise, there have not been enough positive visits to answer the $k$-th query, so `-1` is appended.

**The two meanings of `-1` do not conflict.** In `nums`, `-1` is a query marker. In `ans`, `-1` means the requested historical positive does not exist. Positive input values are guaranteed greater than zero, so no actual visited value can be confused with this sentinel.
After processing any prefix:

- `seen` contains all positive values from that prefix in chronological order;
- `k` is the length of the suffix of consecutive query markers in that prefix;
- `ans` contains one correct answer for each query marker processed.

A positive input preserves the first invariant by appending, makes the current query suffix empty by resetting `k`, and adds no answer. A query preserves `seen`, increases the suffix length by one, and selects the $k$-th item from the reverse chronological order using `seen[-k]`, or the sentinel when that item does not exist. Induction proves the invariants and final answer.

**Trace `[1,2,-1,-1,-1]`.** Positive visits create `seen = [1,2]`. The first query has `k=1` and returns `seen[-1]=2`. The second has `k=2` and returns `seen[-2]=1`. The third has `k=3 > len(seen)` and returns `-1`.

For `[1,-1,2,-1,-1]`, the first query returns one. Seeing two appends it and resets `k`. The next query returns the newest value two, and the consecutive query after it returns one.

**Why old positives remain useful.** A positive does not clear `seen`; it only resets query rank. Earlier positives remain behind the new one and can be returned by the second, third, or later consecutive query. Clearing the history on every positive would make the second example incorrect.

**Why no deque is needed.** A deque supports efficient insertion at the front, but the source's append-plus-negative-index representation is even simpler for this access pattern. It never removes historical positives and needs random access by rank, which a list provides directly.

The result includes exactly one entry per `-1` input and none for positives. Its length can therefore range from zero to $n$.

## Complexity detail

The loop processes each of $n$ inputs once. List append, length checking, negative indexing, and answer append are amortized or worst-case constant time, so total time is $O(n)$.

`seen` can hold every input when all values are positive, and `ans` can hold every input when all are queries. Total allocated space including output is $O(n)$. Auxiliary history excluding the required answer is also $O(n)$ in the worst case. These bounds match the manifest.

## Alternatives and edge cases

- **Prepend literally:** `seen.insert(0, x)` matches the prose but shifts a growing list and can take $O(n^2)$ total time.
- **Deque front insertion:** It makes prepending efficient, but indexed access to the $k$-th item is not the deque's strongest operation.
- **Queries before any positive:** Every one returns `-1` because `seen` is empty.
- **Positive resets `k`:** The next query always asks for the newest positive, not the next rank from an older query run.
- **History is retained:** Reset the query count, not the `seen` list.
- **No queries:** Return an empty answer list.
- **Long query run:** Once `k` exceeds history length, all later queries in that same run also return `-1`.
- **Duplicate positives:** Each occurrence is a separate visit and occupies its own historical position.
- **Why negative indexing is safe:** The source evaluates `seen[-k]` only when `k <= len(seen)`. That guard prevents an out-of-range access while mapping query number one to the newest appended value, query number two to the second newest, and so on.
- **Queries are numbered within a run:** Only consecutive `-1` operations increase `k`. Encountering a positive integer ends that run before the next query begins again at rank one.
