## General

A substring is valid when it has at most $k$ zeros or at most $k$ ones. Because the connector is “or,” a substring is invalid only when both counts exceed $k$:

$$
\#0>k\quad\text{and}\quad\#1>k.
$$

This condition is monotone when a substring is extended to the left: adding more characters cannot reduce either count. That monotonicity enables a sliding window.

The right boundary `r` moves from left to right. `cnt[0]` and `cnt[1]` store the zero and one counts in the current window `s[l:r+1]`. The loop reads each character as integer `x` through `map(int, s)` and increments the corresponding counter.

If both counts now exceed `k`, the window is invalid. The inner while loop removes `s[l]` from its counter and advances `l` until at least one count is no greater than `k`. At that point `s[l:r+1]` satisfies the constraint.

More is true: `l` is the earliest valid start for this fixed ending `r`. If the while loop moved `l`, the window immediately before its last removal had both counts above $k$ and was invalid. Any even earlier start contains that invalid window plus additional characters, so it is also invalid. If no movement was needed, zero is naturally the earliest possible start.

Every substring ending at `r` and beginning at `l`, `l+1`, ..., `r` is valid. Removing characters from the left can only decrease counts, so once one count is at most $k$, it remains at most $k$ for every shorter suffix. There are `r - l + 1` such starts, which the solution adds to `ans`.

Counting by right endpoint is disjoint: every substring has exactly one ending position. Therefore summing the number of valid starts for each `r` counts every valid substring exactly once without generating it.

For `s = "10101"` and `k = 1`, early windows remain valid. When a window contains at least two zeros and two ones, the while loop advances its left boundary until one count falls back to one. The three excluded long substrings are precisely the ones for which both counts exceed the threshold.

For an all-one string, `cnt[0]` stays zero. The while condition can never be true because zero is not greater than `k`. At each right endpoint, every possible start is counted, yielding $n(n+1)/2$.

**Why the shrink condition uses `and`.** Replacing it with `or` would require both character counts to be at most $k$, solving a stricter problem. A substring with many ones but at most $k$ zeros is valid, as is the symmetric case. Shrinking is necessary only when neither permitted condition holds.

The invariant after the while loop is that the current window is valid and every earlier start is invalid. This invariant directly justifies the added count and is preserved as `r` advances. Since `l` only moves right, the total number of inner-loop iterations over the whole scan is at most $n$.

## Complexity detail

Let $n$ be the string length. The right boundary advances $n$ times, and the left boundary advances at most $n$ times total. Each step performs constant work, so time complexity is $O(n)$.

The two-entry count list, two pointers, current character, and answer use $O(1)$ auxiliary space. `map(int, s)` is lazy and does not create a second list. The input string is immutable and not copied.

The answer can be as large as $n(n+1)/2$. Python integers handle this automatically.

## Alternatives and edge cases

- **Enumerate all substrings:** Maintaining counts for each start gives $O(n^2)$ time. It fits the small version-I bound of fifty but misses the stronger monotonic structure.
- **Prefix counts:** They make one substring check $O(1)$ but still leave $O(n^2)$ pairs of endpoints.
- **Count invalid substrings:** One can count windows where both counts exceed $k$ and subtract from the total. The direct valid-window method is simpler.
- **Shrink with `or`:** This is incorrect because it enforces both counts at most $k$ instead of either count at most $k$.
- **All zeros or all ones:** Every substring is valid because the absent character count is zero.
- **`k >= n`:** No count can exceed $k$, so all $n(n+1)/2$ substrings are counted.
- **Window exactly at a threshold:** A count equal to $k$ satisfies “at most,” so shrinking uses strict `> k`.
- **Alternating string:** Both counts grow together, and the window shrinks only after each has passed the threshold.
- **Single character:** One character type has count one and the other zero, so the sole substring is valid.
- **Parsing characters:** `map(int,s)` produces integer zero or one for the right endpoint, while shrinking uses `int(s[l])`. The binary-string guarantee makes both safe.
- **Earliest-start invariant:** After shrinking, moving `l` one position back would restore a window known to have both counts above `k`. This is why `r - l + 1` is exact rather than merely a lower bound on the number of valid suffixes.
