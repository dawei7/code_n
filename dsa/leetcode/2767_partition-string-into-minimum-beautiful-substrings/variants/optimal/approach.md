## General

Let `minimum_parts[i]` be the fewest beautiful pieces that partition the prefix `s[:i]`; initialize `minimum_parts[0] = 0` and every other state as unreachable. Precompute the positive powers of $5$ smaller than $2^n$, because no substring of an $n$-bit string can represent a larger value.

For every reachable boundary `start`, skip it if `s[start]` is zero, since any piece beginning there would have a leading zero. Otherwise, extend `end` to the right while building the substring's binary value with `value = value * 2 + int(s[end])`. Whenever that value is in the power-of-five set, relax `minimum_parts[end + 1]` with one more piece.

Every transition appends one beautiful substring to an already valid prefix partition, so each finite DP state represents a valid partition. Conversely, consider an optimal partition and its successive cut boundaries. Each piece begins with one, its incrementally built value is a stored power of $5$, and therefore the DP includes the transition between those boundaries. The final state cannot exceed the optimal count, while validity prevents it from being smaller; hence it is exactly the minimum. If the final boundary remains unreachable, no complete partition exists.

## Complexity detail

There are $n$ possible starts and at most $n$ ends for each start, with constant-time set membership, so the running time is $O(n^2)$. The DP array and the set of relevant powers of $5$ use $O(n)$ space.

## Alternatives and edge cases

- **Backtracking with memoization:** A top-down search over starting indices has the same $O(n^2)$ state-transition bound and is equally valid.
- **Enumerate every cut mask:** Testing all $2^{n-1}$ possible partitions is feasible only because $n \leq 15$, but it scales exponentially.
- **Leading zero:** Any reachable boundary pointing at `'0'` is a dead end; zeros may appear only inside a valid power representation.
- **Power zero:** The one-bit string `"1"` represents $5^0$ and is beautiful.
- **Valid prefix, invalid suffix:** Finding a beautiful prefix is insufficient unless the DP can also reach the end of the string.
