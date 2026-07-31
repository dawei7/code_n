## General

For every possible window, determine how much of `pattern` matches from the left and how much matches from the right. The Z-algorithm on `pattern + "#" + s` gives the exact prefix-match length between `pattern` and the source suffix beginning at each index. Capping a value at the pattern length yields the matching prefix of that candidate window.

Apply the same construction to the reversed pattern and reversed source. A window beginning at `start` ends at `start + m - 1`, which becomes position `n - start - m` in the reversed source. The corresponding reversed Z-value is therefore the number of matching characters at the original window's right edge.

If a window's matching prefix length plus matching suffix length is at least $m-1$, those exact regions cover every pattern position except possibly one, so the window is almost equal. Conversely, a window with at most one mismatch has exact regions on both sides of that mismatch totaling at least $m-1$. Checking starts in ascending order and returning the first qualifying one produces the required smallest index.

The Z-algorithm remains linear by maintaining the rightmost interval already known to match the text prefix. Positions inside that interval reuse a previous Z-value and compare characters only when extending the interval's right boundary.

## Complexity detail

Let $n=\lvert s\rvert$ and $m=\lvert pattern\rvert$. The two combined strings and their Z-arrays each have $O(n+m)$ length. Building both arrays and scanning all windows takes $O(n+m)$ time and uses $O(n+m)$ auxiliary space.

## Alternatives and edge cases

- **Direct window comparison:** Comparing up to $m$ characters at every start costs $O(nm)$ in repetitive inputs.
- **Rolling hash:** Splitting around a discovered mismatch can be efficient, but collision handling complicates deterministic correctness.
- **Exact match:** Prefix and suffix matches may overlap; the threshold still accepts the window because zero changes are allowed.
- **Mismatch at an endpoint:** One of the two exact regions may have length zero, while the other covers $m-1$ positions.
- **One-character pattern:** Since $m-1=0$, the first source position always qualifies, with at most one change.
