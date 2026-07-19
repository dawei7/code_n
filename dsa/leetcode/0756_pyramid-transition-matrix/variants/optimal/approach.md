## General
**Index every lower pair by its possible tops**

Convert each rule into a map from its first two labels to a list of permitted third labels. A missing pair can then terminate a partial row immediately, while multiple values expose the backtracking choices without rescanning `allowed`.

**Build one upper row from left to right**

For a current row, recursively choose the top for pair `row[i:i + 2]` and append it to a partial next row. Once all adjacent pairs are assigned, recursively ask whether that complete next row can reach the pyramid top. Return as soon as any branch succeeds.

**Memoize complete row states**

Different lower choices often converge to the same upper row. Cache whether each complete row can reach a valid top so its entire suffix search is performed once. Partial rows are local to one transition layer; the future depends only on the completed row string.

Every generated character comes from the rule for exactly the two blocks beneath it, so each completed next row is legal. Backtracking enumerates every combination of permitted tops for the current row. By induction on row length, the cached predicate returns true exactly when some legal sequence of such rows reaches length one.

## Complexity detail
Let $n$ be the bottom length and $a$ the maximum number of top labels permitted for one pair. There are $n(n - 1) / 2$ block positions above the bottom, so the uncached search-tree bound is $O(a^{n(n-1)/2})$; memoization can substantially reduce repeated suffixes but not that general worst case. Cached row states and generated choices use at most $O(a^n)$ space under this loose exponential bound, with $O(n)$ recursion depth.

## Alternatives and edge cases
- **Bitmask transitions:** Encode the possible tops for each pair as a small bitmask over labels `A` through `G`; this reduces constant factors while keeping the same search structure.
- **Backtracking without row memoization:** It remains correct but can recompute the same upper-row failure exponentially many times.
- **Scan the full rule list per pair:** This avoids preprocessing but repeats $O(|allowed|)$ work at every search node.
- **Bottom length two:** Any permitted top for that sole adjacent pair completes the pyramid immediately.
- **Missing adjacent-pair rule:** The current partial construction cannot continue and should fail immediately.
- **Duplicate paths to one row:** Cache by the complete row value, not by the path used to create it.
- **Multiple valid tops:** Short-circuit on the first successful construction; the actual pyramid need not be returned.
