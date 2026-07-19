## General
**Reduce all pairs to sorted neighbors.** Sort the distinct values. If two selected values have another array value between them in sorted order, then at least one of the two adjacent gaps is strictly smaller than their difference. Therefore a globally minimum pair must consist of adjacent sorted values; no non-adjacent pair needs to be examined.

**Track every equal minimum in one scan.** Traverse consecutive sorted values and compute `gap = right - left`. When `gap` is smaller than the best seen, replace the result with the current pair. When it equals the best, append the current pair. Larger gaps are ignored. Since the traversal follows ascending values, appended pairs are already in the required ascending order.

## Complexity detail
Sorting $n$ values costs $O(n\log n)$ time, and examining the $n-1$ adjacent gaps costs $O(n)$, so the overall time is $O(n\log n)$. The sorted copy and returned pairs can each occupy $O(n)$ space; the scan state itself is $O(1)$.

## Alternatives and edge cases
- **Compare every pair:** Exhaustive comparison is correct but requires $O(n^2)$ time.
- **Value-presence table:** The bounded coordinate range permits scanning possible gaps, but a direct table spans two million positions and complicates finding all pairs.
- **Two elements:** Their sole pair is necessarily the answer.
- **Negative values:** Sorting makes subtraction `right - left` equal the absolute difference without special handling.
- **Several minimum pairs:** Every adjacent gap equal to the global best must be returned, not only the first.
- **Distinctness:** The minimum difference is positive because duplicate values are excluded.
- **Input order:** The output is determined by numeric order, regardless of how values appear in `arr`.
- **Extreme coordinates:** Subtracting $-10^6$ from $10^6$ remains within ordinary integer ranges, while the same algorithm handles the full domain.
