## General
**Count only partners that precede the current index.** Scan `nums` from left
to right while a frequency table records the values at earlier indices. When
the current value is `value`, an earlier value forms a valid pair exactly when
it is `value - k` or `value + k`. Add both stored frequencies before recording
the current value.

**Why every pair is counted exactly once.** Consider any valid pair $(i,j)$
with $i<j$. At index $j$, `nums[i]` is already in the frequency table and is
one of the two required partner values, so the pair is counted. It cannot be
counted earlier because its second endpoint has not yet been visited, and it is
never counted later because additions always pair the current index with a
previous one. Since $k$ is positive, `value - k` and `value + k` are distinct,
so the two lookups cannot count the same earlier index.

## Complexity detail
Here $N$ is the length of `nums`. Each element causes a constant number of
average-case hash-table operations, giving $O(N)$ time. The table can contain
up to $N$ distinct values, so it uses $O(N)$ space.

## Alternatives and edge cases
- **Examine every index pair:** Testing all $\binom{N}{2}$ pairs is direct but
  takes $O(N^2)$ time.
- **Frequency product after a full pass:** Build all frequencies, then sum
  `count[x] * count[x + k]` once per value. This is also linear in the input
  plus the number of distinct values, but the one-pass method naturally
  enforces $i<j$.
- Duplicate occurrences must be counted by position; two copies on each side
  of the required difference contribute four pairs.
- A one-element array has no index pair and therefore returns zero.
- Values outside the observed range simply have frequency zero; no special
  boundary branch is needed for `value - k` or `value + k`.
