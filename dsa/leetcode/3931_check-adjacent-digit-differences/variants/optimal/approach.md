## General

**Turn the universal condition into a left-to-right check.** The answer is `true` only if every adjacent pair satisfies the same independent inequality. Scan the string from its first pair to its last, keeping only the two characters in the current pair.

Decimal digit characters are consecutive in the character encoding, so `abs(ord(left) - ord(right))` equals the absolute difference between their numeric digit values. If this value is greater than `2`, that pair is a direct counterexample to the required condition and the function can return `false` immediately.

If the scan reaches the end, every adjacent pair has been checked and none violated the limit. Returning `true` is therefore correct. Conversely, whenever the function returns `false`, it has found an actual adjacent pair whose difference is too large, so both possible results follow exactly from the problem's condition.

## Complexity detail

Let $N=\lvert\texttt{s}\rvert$. There are $N-1$ adjacent pairs, and the scan performs constant work for each pair until it either fails or finishes. Its worst-case time is $O(N)$ and it uses $O(1)$ auxiliary space.

This upper bound is asymptotically optimal. On a valid string, an algorithm must rule out a violation at every position: changing an uninspected digit in an all-equal string can make the answer false. Thus the worst-case input-reading lower bound is $\Omega(N)$, matching the scan, so a slower-class runtime benchmark would not provide meaningful replacement evidence.

## Alternatives and edge cases

- **Convert every character first:** Building a list of integer digits and then comparing neighbors is correct and still takes $O(N)$ time, but it uses $O(N)$ extra space that the direct character scan avoids.
- **Use `all` with a generator:** A generator over adjacent pairs expresses the universal condition compactly and short-circuits correctly; the explicit loop makes the rejection boundary and constant-space behavior especially clear.
- **Difference exactly two:** The limit is inclusive, so pairs such as `2` and `4` are valid.
- **Equal digits:** Their difference is zero, so any run of repeated digits is valid by itself.
- **Leading zeroes:** Treat `0` as a normal digit rather than parsing the complete string as one integer.
- **Minimum length:** A two-character string has exactly one adjacent pair, which the same loop checks without a special case.
