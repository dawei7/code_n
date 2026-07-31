## General

Because both conditions use absolute differences, any qualifying pair can be ordered so that $i\le j$. For a fixed right index $j$, the eligible earlier indices are exactly those at most `j - indexDifference`.

Maintain the indices of the minimum and maximum values among that eligible prefix. When advancing `right`, add the newly eligible index `right - indexDifference` to these two extrema. All previously eligible indices remain eligible, so no removal is required.

If some eligible value differs from `nums[right]` by at least `valueDifference`, then it is either at most `nums[right] - valueDifference` or at least `nums[right] + valueDifference`. The prefix minimum detects the first possibility, and the prefix maximum detects the second. Checking only these two indices is therefore sufficient, and either returned pair automatically meets the index requirement.

Conversely, if neither extreme differs enough, every eligible value lies strictly between the two thresholds, so no pair ending at this `right` can work. Scanning all right endpoints finds a valid pair whenever one exists. Starting at `indexDifference` also handles a zero index requirement: index zero becomes eligible at right zero, allowing `[0, 0]` when `valueDifference` is zero.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Each index enters the eligible prefix once and each right endpoint is checked once, so the running time is $O(n)$. Only two stored indices and loop variables are needed, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Compare every index pair:** The direct nested-loop solution is correct but takes $O(n^2)$ time and is too slow for $n=10^5$.
- **Ordered multiset:** Maintaining all eligible values supports threshold queries but uses $O(n)$ space and $O(n\log n)$ time when only the two extremes are necessary.
- **Zero differences:** When both requirements are zero, the same index is a valid pair.
- **Index requirement at least the array length:** No two in-range indices can be far enough apart, so the answer is `[-1, -1]`.
- **Earlier value is larger:** The maintained maximum is necessary in addition to the minimum to detect this direction of absolute difference.
- **Several qualifying pairs:** The contract permits returning the first pair found by the scan.
