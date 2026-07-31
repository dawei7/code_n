## General

**Treat the process as a periodic state**

Let $m$ be the length of `nums`. Removing all $m$ elements and then restoring
all $m$ elements takes exactly $2m$ minutes. The array at a time therefore
depends only on `phase = time % (2 * m)`.

For $0 \le \text{phase} < m$, exactly `phase` elements have been removed from
the left. The current array is the original suffix `nums[phase:]`. A queried
current index `index` consequently refers to original position
`phase + index`; it exists precisely when that position is less than $m$.

For $m \le \text{phase} < 2m$, removal is complete and
`phase - m` elements have been restored. The current array is the original
prefix of that length. Its indices already match the original indices, so
`index` is visible exactly when `index < phase - m`.

These two ranges describe every minute in one full cycle. In each range, the
direct lookup returns the element in the corresponding suffix or prefix and
returns $-1$ for every position beyond its current length. Reducing later
times modulo $2m$ preserves the state, so applying the same lookup
independently to every query produces all answers in order.

## Complexity detail

Let $q$ be the number of queries. Each query needs one remainder calculation,
one boundary check, and at most one array lookup, for $O(q)$ time. The returned
list contains $q$ answers and therefore uses $O(q)$ space; excluding that
required output, the algorithm uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Simulate from minute zero for every query:** Replaying every removal and
  replacement produces the right state but can take time proportional to the
  queried timestamps instead of constant time per query.
- **Precompute every state:** Storing the arrays for all $2m$ phases permits
  direct query lookup, but copies up to $O(m^2)$ elements even though the phase
  and index identify the answer arithmetically.
- At `phase = m`, the array is empty, so every query returns $-1$.
- At `phase = 0`, including every multiple of $2m$, the complete original
  array is present.
- During removal, current index zero moves rightward through the original
  array; during replacement, current indices agree with original indices.
- When $m = 1$, the process simply alternates between a one-element array and
  an empty array.
