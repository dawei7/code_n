## General

**Maintain both directions of the assignment**

After each query, we need the number of colors currently used by at least one ball. Recomputing all colored balls each time would be too slow.

The exact solution maintains:

- `g[x]`: the current color assigned to ball `x`;
- `cnt[y]`: the number of balls currently assigned color `y`.

The number of distinct active colors is exactly `len(cnt)`, provided zero-count entries are removed.

Only balls that have appeared in a query need entries in `g`. The parameter `limit` can be as large as $10^9$, so allocating an array for all labels would be wasteful. The dictionary makes storage depend on the number of queries instead.

**Process one recoloring**

For query `[x, y]`, the code first increments `cnt[y]` because ball `x` will have new color `y`.

If `x` already exists in `g`, the ball previously contributed one owner to old color `g[x]`. That old count is decremented. If it becomes zero, the key is popped so it no longer contributes to `len(cnt)`.

Then `g[x] = y` records the new assignment, and `len(cnt)` is appended to the answer.

Incrementing the new color before decrementing the old one is safe even when the colors are identical. Suppose ball `x` is recolored from $y$ to $y$. The count temporarily rises by one and then falls by one, returning to its original positive value. It is not mistakenly removed.

**Invariant**

After each completed query:

- `g` contains exactly one current color for every ball colored so far;
- for every key $c$ in `cnt`, `cnt[c]` equals the number of `g` values equal to $c$;
- `cnt` contains no zero-count key.

The invariant holds initially for two empty structures.

For an uncolored ball, incrementing the new count and adding `g[x]` introduces exactly one new assignment. For an already colored ball, decrementing the old count removes its former contribution, incrementing the new count adds its current contribution, and popping zero removes precisely a color with no owners. Thus the invariant is preserved.

Because the keys of `cnt` are exactly colors with at least one owner, `len(cnt)` is the requested distinct-color count.

**Example**

For queries `[1,4]`, `[2,5]`, `[1,3]`, `[3,4]`:

1. Ball 1 gets color 4: counts are `{4:1}`, answer 1.
2. Ball 2 gets color 5: counts are `{4:1,5:1}`, answer 2.
3. Ball 1 changes from 4 to 3: color 4 drops to zero and is removed; active colors are 3 and 5, answer 2.
4. Ball 3 gets color 4: active colors are 3, 5, and 4, answer 3.

The number of colored balls and number of distinct colors are different: several balls may share a color, which is why owner counts rather than a simple color set are necessary.

**Why uncolored is absent**

Initially uncolored balls contribute no color by the statement. The method stores no default value for them and does not include an “uncolored” key. The huge number of never-mentioned balls therefore has no effect.

## Complexity detail

Let $q$ be the number of queries.

Each query performs a constant number of expected-time dictionary or counter operations, so total expected time is $O(q)$.

At most $q$ distinct ball labels appear in `g`, and at most $q$ active colors appear in `cnt`. Auxiliary space is $O(q)$. The answer list uses another $O(q)$ required output space.

The manifest writes $O(n)$ time and space where $n$ denotes the query count; this matches the exact source.

The value of `limit` does not enter the complexity because the method never enumerates all possible balls.

Hash-table expected constant-time behavior is assumed.

## Alternatives and edge cases

- **Recount colors after every query:** Scanning all colored balls per query can take $O(q^2)$ time.
- **Color set only:** A set cannot tell whether removing one ball's old color should remove the color entirely when other balls still use it.
- **Array indexed by ball label:** It requires $O(limit)$ memory, impossible when `limit` is $10^9$.
- **Coordinate compression:** It can replace the ball dictionary after reading all queries, but adds preprocessing without improving asymptotic bounds.
- **First assignment to a ball:** There is no old count to decrement.
- **Recolor to the same color:** Increment-then-decrement leaves counts and the distinct answer unchanged.
- **Old color shared by others:** Its count stays positive and the key remains active.
- **Old color loses its last ball:** The zero count is popped, reducing `len(cnt)`.
- **New color already active:** Its owner count increases but distinct-color count does not.
- **New color unseen:** A new counter key raises the distinct count by one.
- **Uncolored balls:** They have no `g` entry and never contribute a color.
- **Unused limit:** It only validates legal labels; sparse dictionaries intentionally make it unnecessary to the computation.
- **One answer per query:** The append occurs after both the old-color removal and new assignment are complete, so the returned list has exactly one fully updated distinct-color count for every query.
