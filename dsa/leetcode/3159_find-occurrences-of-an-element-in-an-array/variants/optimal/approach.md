## General

The queries all ask about the same target `x`, so repeatedly searching `nums` would redo the same work. Instead, scan `nums` once from left to right and append `index` whenever `nums[index] == x`. The resulting `positions` list is already ordered: `positions[0]` is the first occurrence, `positions[1]` is the second, and so on.

For a query `occurrence`, the requested one-based occurrence maps to `positions[occurrence - 1]`. That lookup is valid exactly when `occurrence <= len(positions)`; otherwise fewer copies of `x` exist and the answer is `-1`. Applying this rule independently in query order produces the required result array. The preprocessing records every and only matching index, so each valid lookup returns precisely the requested occurrence.

## Complexity detail

Let $n$ be the length of `nums` and $q$ the length of `queries`. Building `positions` takes $O(n)$ time, and answering all queries takes $O(q)$ time, for $O(n + q)$ total time. At most $n$ matching indices are stored. Excluding the returned answer array, auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Scan once per query:** Count occurrences while traversing `nums` for every query. This uses $O(1)$ auxiliary space but costs $O(nq)$ time in the worst case.
- **Map every value to its indices:** Precompute an index list for every distinct value. This is useful when queries target many different values, but stores information that this single-target problem never uses.
- **Target absent:** `positions` is empty, so every positive query returns `-1`.
- **Repeated or unsorted queries:** Direct lookup answers each query independently and preserves the original query order.
- **Occurrence numbering:** Queries are one-based, while list indices are zero-based; subtracting one is necessary only after confirming the occurrence exists.
