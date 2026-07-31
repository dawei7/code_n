## General

There are exactly $W=n-m$ possible starts for a subarray of length $m+1$. Inspect each candidate independently and compare its $m$ adjacent pairs with the $m$ pattern entries in the same order.

For two adjacent values `left` and `right`, the expression `(right > left) - (right < left)` evaluates to `1`, `0`, or `-1` according to whether the pair increases, stays equal, or decreases. This gives the exact relation alphabet used by `pattern` without relying on the magnitude of the difference.

Stop checking a candidate as soon as one relation differs. If the inner loop reaches its end, every required comparison holds, so increment the answer. Each increment therefore corresponds to one matching subarray, and every possible start is considered once; overlapping matches are naturally counted separately.

## Complexity detail

In the worst case, all $m$ relations are checked for each of the $W=n-m$ candidate starts, giving $O((n-m)m)$ time. A mismatch may end an individual scan earlier but does not worsen that bound. The method stores only loop indices, adjacent values, and the answer, so it uses $O(1)$ additional space.

## Alternatives and edge cases

- **Comparison array plus string matching:** Convert all $n-1$ adjacent relations first and find `pattern` with KMP or a Z-function in $O(n+m)$ time and $O(n+m)$ space; that machinery is more useful for the much larger limits of the companion problem.
- **Materialized comparison array with window slices:** Comparing each length-$m$ slice is easy to express but uses $O(n)$ storage while retaining $O((n-m)m)$ worst-case time.
- **Repeated full-window rescans:** Recomputing an $O(m)$ aggregate before every one of a candidate's $m$ relation checks is redundant and raises the bound to $O((n-m)m^2)$.
- **Single relation:** When $m=1$, every adjacent pair is an independent candidate and must be compared against the one pattern value.
- **Full-length pattern:** When $m=n-1$, only the complete `nums` array can match.
- **Overlapping matches:** Starts advance by one, so repeated or monotone values may produce several matches sharing elements.
- **Magnitude is irrelevant:** A jump from `1` to `1000000000` represents the same `1` relation as a jump from `1` to `2`.
