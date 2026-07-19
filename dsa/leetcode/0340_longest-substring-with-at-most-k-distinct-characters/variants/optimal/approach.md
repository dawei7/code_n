## General
**Keep one adjustable window**

A valid substring is an interval, so maintain one window `[left, right]` rather than rebuilding character sets for every possible starting index. A frequency map records exactly which characters occur in the current window and how many copies of each remain.

Move `right` across the string. After adding `s[right]`, the window may temporarily contain more than `k` distinct characters. While it is invalid, remove `s[left]` and advance `left`; delete a character from the map only when its count reaches zero. Once the map contains at most `k` keys again, the current window is valid and can update the best length.

**Why shrinking keeps the best suffix**

The decisive property is that, for a fixed `right`, shrinking stops at the smallest feasible `left` reachable from the previous window. Any substring ending at `right` and starting farther right is no longer, so `[left, right]` is the longest valid candidate ending there. Recording its length therefore considers the best candidate for every right endpoint.

**Trace the changing left boundary**

For `"eceba"` with $k = 2$, the window grows to `"ece"`. Adding `b` creates three distinct characters, so the left side moves past both occurrences needed to eliminate `e`; the valid window becomes `"cb"`. The scan continues with the same left pointer rather than restarting.

**Why the maximum is globally optimal**

Every recorded candidate is valid because the update happens only after the distinct count is within the limit. Conversely, take any optimal substring and consider the iteration at its right endpoint. The algorithm's left boundary cannot lie to the right of that optimal start unless the larger window were invalid; since the optimal substring is valid, the algorithm records a window at least as long. Thus the maximum recorded length is exactly optimal.

## Complexity detail
Each character enters the window once through `right` and leaves at most once through `left`, so the total work is $O(n)$ rather than $O(n^2)$. The frequency map holds at most $k + 1$ characters during the brief invalid state and at most `k` after shrinking, which is $O(k)$ auxiliary space.

## Alternatives and edge cases
- **Restart from every left endpoint:** is correct but can take $O(n^2)$, especially when the whole string already uses at most `k` characters.
- **Evict by last-seen position:** also supports a linear scan, but finding the least recent character needs a bounded map scan or an ordered structure.
- If $k = 0$ or the string is empty, the answer is `0`.
- If `k` covers every distinct character in the string, the window never shrinks and the answer is `len(s)`.
- Frequencies are essential: removing one leftmost copy must not delete a character that still occurs elsewhere in the window.
