## General
**Fix the earliest undecided position**

Maintain an array of length $2n - 1$, initially filled with zeroes, and a set of values already placed. At each recursive step, advance to the first zero position. If a value greater than $1$ is chosen there, its second occurrence has only one possible location: `index + value`. The placement is legal exactly when that paired index is in bounds and still empty. The value $1$ occupies only the current position.

**Try candidates in descending order**

At the first undecided position, consider unused values from `n` down to `1`. This orders the search by lexicographic preference: every completion under a larger current value is lexicographically greater than every completion under a smaller one, regardless of their suffixes. After a legal placement, recurse; if the suffix cannot be completed, erase the placed occurrence or occurrences and try the next value.

**Stop at the first complete arrangement**

When no zero position remains, every value has the required multiplicity because each recursive choice marks one previously unused value, and every value above $1$ was placed at exactly the required index distance. Descending candidate order means all lexicographically greater prefixes were either tried or proved impossible before this complete sequence was reached. Therefore the first complete arrangement is the required maximum, and no enumeration of later valid sequences is necessary.

## Complexity detail
There are at most $n$ candidate values at the first level, at most $n-1$ unused candidates at the next, and so on. The resulting worst-case search is bounded by $O(n!)$ recursive choices; range checks, placements, and removals are constant-time, while filled positions are skipped across a path. The sequence, used-value table, and recursion stack each require $O(n)$ space.

## Alternatives and edge cases
- **Enumerate every valid sequence:** Exploring all complete arrangements and retaining the largest is correct, but it discards the decisive early-stop benefit of descending lexicographic search.
- **Ascending candidate order:** This can find a valid sequence, but its first completion is biased toward the lexicographically smallest prefix and cannot be returned as the requested maximum.
- **Copy state at every recursion:** Passing fresh sequence and used-value copies simplifies undo logic but adds allocation and copying overhead at every search node.
- **The value one:** It occurs once and therefore has no paired index; treating it like the other values would incorrectly require a second copy.
- **Occupied paired positions:** A value above $1$ cannot be placed unless both its current position and `index + value` are empty.
- **Minimum input:** For `n = 1`, the backtracking immediately places the single `1` and returns `[1]`.
