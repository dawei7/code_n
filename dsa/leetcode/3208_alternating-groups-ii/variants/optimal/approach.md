## General

**Linearize the circular windows**

A circular block may wrap from the end of `colors` to its beginning. Read indices modulo $n$ through virtual positions `0` to `n + k - 2`. This covers the original circle followed by the first $k-1$ tiles, enough to represent every one of the $n$ possible length-`k` blocks as an ordinary interval.

No extended array is needed: virtual position `p` reads `colors[p % n]`.

**Track the current alternating suffix**

Maintain the length of the longest alternating run ending at the current virtual position. If the current color differs from the previous color, extend the run by one; otherwise reset it to one.

A length-`k` window ending at position `end` alternates exactly when this suffix length is at least $k$. Begin counting only at `end = k - 1`, the first complete window, and stop after `end = n + k - 2`. These bounds test exactly $n$ endings, hence exactly the $n$ circular starts.

The maintained run length is correct by induction: a differing adjacent pair extends every alternating suffix, while an equal pair prevents any suffix of length greater than one. Therefore each counted window has all $k-1$ required differences, and every alternating window is counted at its unique ending position.

## Complexity detail

The virtual scan processes $n+k-1$ positions. Since $k\le n$, this is $O(n)$ time. Only the run length, answer, and indices are stored, so auxiliary space is $O(1)$.

Modulo supplies circular access without copying `colors`.

## Alternatives and edge cases

- **Check every window independently:** Testing all $k-1$ adjacent pairs for each of $n$ starts costs $O(nk)$ time.
- **Duplicate the prefix:** Building `colors + colors[:k - 1]` simplifies indexing but uses $O(k)$ additional space.
- **Count all long-run suffixes:** Counting before the first complete window or beyond the final circular start produces extra groups.
- **Equal adjacent colors:** One equal pair resets the current run and invalidates every length-`k` window containing that pair.
- **Whole-circle window:** When $k=n$, each circular start still defines a block, and alternation is checked only between consecutive tiles inside that length-$n$ order.
- **Even perfect alternation:** Every start is valid for every legal $k$.
- **Odd circle:** Wraparound can break alternation even when the linear array alternates internally.
- **Minimum `k`:** At $k=3$, the condition reduces to the middle tile differing from both neighbors.
