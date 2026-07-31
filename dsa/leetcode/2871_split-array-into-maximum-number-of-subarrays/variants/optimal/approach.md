## General

**Identify the minimum possible score sum**

Let $G$ be the bitwise AND of the entire array. The score of every segment contains every bit set in $G$, because AND-ing all segment scores together produces $G$. Therefore each nonnegative segment score is at least $G$, and every partition has score sum at least $G$. Keeping the entire array as one subarray attains $G$, so $G$ is the minimum possible sum.

If $G > 0$, a partition with at least two subarrays has score sum at least $2G > G$. Consequently the only minimum-score split is the whole array, and the answer is one.

**Greedily close zero-score segments**

When $G = 0$, the minimum score sum is zero. Since segment scores are nonnegative, every segment in a minimum-score split must itself have AND equal to zero.

Scan from left to right while maintaining the AND of the current unfinished segment. As soon as it reaches zero, close that segment, increment the answer, and reset the running AND for the next value. Once an AND is zero, appending more values cannot change it, so postponing that cut cannot help create additional segments. Moreover, any valid first zero-score segment must end at or after the greedy endpoint. Cutting at the earliest endpoint leaves at least as much suffix for later segments, and the same argument applies after every cut.

If values remain after the last completed zero-score segment, append that suffix to the last segment; its AND stays zero. Thus every greedy cut contributes a valid part, and the earliest-cut exchange argument proves that no valid zero-score partition has more parts. When the scan never reaches zero, $G$ is positive and the required answer is one, expressed as `max(segments, 1)`.

## Complexity detail

Let $n = \lvert\texttt{nums}\rvert$. The scan performs one bitwise AND per element, taking $O(n)$ time. It stores only the running AND and segment count, so it uses $O(1)$ auxiliary space.

The benchmark uses $n$ as `size` and alternates `1` with `0` at sizes 32, 128, and 512. Every adjacent pair forms one zero-AND segment, forcing the full scan while making the expected maximum easy to verify. The greedy method scales linearly. A correct dynamic program that checks every possible segment boundary completes all tiers but exhibits quadratic scaling.

## Alternatives and edge cases

- **Quadratic dynamic programming:** A prefix DP can test every possible final segment and maximize the number of zero-AND parts, but recomputing backward AND values costs $O(n^2)$ time.
- **Sparse table plus binary search:** Range-AND queries can locate zero endpoints, but the extra structure is unnecessary because AND changes monotonically as a segment grows.
- **Positive global AND:** More than one segment would contribute at least two positive copies of $G$, so only the unsplit array attains the minimum sum.
- **All zeros:** Every element can stand alone, producing $n$ minimum-score subarrays.
- **Single element:** Whether zero or positive, a one-element array has exactly one valid subarray.
- **Trailing nonzero suffix:** After at least one zero-AND segment is found, attach any leftover suffix to the last segment without changing its zero score.
- **Reset value:** Starting a fresh running AND at `-1` is safe in Python because `-1 & x == x` for every nonnegative integer `x`.
