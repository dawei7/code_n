## General
**Track both possible directions**

Begin with two flags, one saying the sequence can still be monotone increasing and the other saying it can still be monotone decreasing. Scan adjacent pairs from left to right.

If `nums[i - 1] < nums[i]`, this rise rules out monotone decreasing. If `nums[i - 1] > nums[i]`, the drop rules out monotone increasing. Equality rules out neither direction. Once both flags are false, no later value can repair either earlier violation, so the scan may return `False` immediately.

Checking adjacent pairs is sufficient for the definitions involving every $i \leq j$. If every adjacent relation is $\leq$, chaining those relations gives $\texttt{nums}[i] \leq \texttt{nums}[j]$ for any earlier $i$ and later $j$. The same transitive argument applies to $\geq$. Thus a surviving increasing flag proves monotone increasing, a surviving decreasing flag proves monotone decreasing, and if neither survives the array is not monotonic.

## Complexity detail
The scan examines at most $n-1$ adjacent pairs, so it takes $O(n)$ time. The two direction flags use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Infer a direction from the first unequal pair:** After skipping an equal prefix, check every later pair against that direction; this is also $O(n)$ time and $O(1)$ space.
- **Compare with sorted copies:** Testing `nums == sorted(nums)` or its reverse is concise, but sorting costs $O(n \log n)$ time and $O(n)$ additional space.
- **Check every index pair:** The definition can be evaluated literally, but the resulting $O(n^2)$ time is unnecessary because adjacent relations are transitive.
- **One element:** A singleton is both monotone increasing and monotone decreasing.
- **All values equal:** Both direction flags remain true, so the array is monotonic.
- **Late reversal:** A sequence can satisfy one direction for a long prefix and still fail; every adjacent pair must be inspected unless both flags become false earlier.
- **Boundary values:** Only comparisons are performed, so values at $-10^5$ and $10^5$ require no special arithmetic handling.
