## General

**Maintain the exact-distinct window**

Scan `nums` from left to right and store the frequencies inside one current
window. `distinct` is the number of keys with positive frequency. Whenever a
new right endpoint makes `distinct > k`, advance `left` until one complete
value leaves and the window again contains at most `k` distinct integers.
Every start before the new `left` necessarily includes too many distinct
values for this right endpoint, so none can qualify.

`qualified` counts how many current distinct values have frequency at least
`m`. A value enters this count exactly when an insertion raises its frequency
to `m`, and leaves it exactly when a left-boundary removal lowers its frequency
from `m` to `m - 1`. The current window meets both problem conditions precisely
when `distinct == k` and `qualified == k`.

**Count every valid start without rescanning it**

Once the current window is valid, its leading value may occur more than `m`
times. Removing that leading occurrence preserves both the set of `k` values
and every frequency threshold, so advance `left` while this surplus exists.
Each removed occurrence exposes one more valid start; `removable_prefix`
stores how many such earlier starts remain valid in addition to the canonical
`left` position.

For the current right endpoint, the valid starts are exactly the canonical
start and those `removable_prefix` earlier positions, contributing
`removable_prefix + 1`. No later start works, because removing the canonical
leading value would reduce its frequency below `m`. Extending the right edge
cannot invalidate previously removed starts unless a new distinct value makes
the window exceed `k`; that overflow discards an entire old value, so the
stored prefix count is reset. These facts account for every qualifying
subarray once, at its right endpoint.

## Complexity detail

Let $N$ be the array length and $K = \texttt{k}$. Each element enters the
frequency map once. The `left` pointer only moves forward, so all shrinking and
surplus-removal iterations total at most $N$. The time complexity is therefore
$O(N)$. After overflow shrinking, the map holds at most $K$ keys (and only
$K+1$ transiently), giving $O(K)$ auxiliary space.

The benchmark defines size as $N$ and uses one repeated value with `k = 1` and
`m = 1`. Every subarray qualifies. The accepted window still performs linear
boundary work, while the correct slower control explicitly enumerates all
$N(N+1)/2$ intervals.

## Alternatives and edge cases

- **Enumerate every start and end:** Maintaining frequencies while extending
  each start is straightforward and correct, but it still visits
  $\Theta(N^2)$ subarrays.
- **Recount each candidate interval:** Rebuilding a map for every interval adds
  another factor and is unnecessary even for a small oracle.
- **Count only one start per right endpoint:** A valid window may have several
  surplus leading occurrences, so omitting `removable_prefix` undercounts.
- **Trim any leading duplicate:** The leading value is removable only while its
  frequency is strictly greater than `m`; trimming at equality destroys the
  per-value requirement.
- **New distinct-value overflow:** Previously removable starts may contain the
  value that must now leave, so the prefix count must reset after shrinking
  back to `k` distinct values.
- **Unreachable thresholds:** If the array never supplies `k` distinct values
  at frequency at least `m`, `qualified == k` never holds and the answer is
  zero.
- **Large answer:** Up to $N(N+1)/2$ intervals can qualify, so fixed-width
  implementations need a 64-bit return type.
