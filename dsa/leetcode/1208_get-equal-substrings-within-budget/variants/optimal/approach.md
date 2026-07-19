## General
**Convert the strings into nonnegative costs conceptually.** At index `i`, the only relevant quantity is `abs(ord(s[i]) - ord(t[i]))`. A candidate substring is affordable exactly when the sum of these per-index costs over its contiguous interval does not exceed `maxCost`.

**Maintain the longest affordable suffix.** Extend a right pointer one index at a time and add that position's cost to a running total. If the total exceeds the budget, repeatedly subtract the cost at the left pointer and advance `left` until the current window becomes affordable again.

**Why discarded starts never become useful.** Every cost is nonnegative. Once the window ending at the current right boundary is over budget, keeping its leftmost position cannot help any extension; adding later positions can only preserve or increase the total. Removing left positions until affordability is restored therefore discards no possible optimal future window. After restoration, the current left boundary is the earliest affordable start for this right endpoint, so the window is its longest valid ending interval. Taking the maximum of those lengths gives the global optimum.

## Complexity detail
The right pointer visits each of the $n$ positions once. The left pointer also advances at most $n$ times across the entire run, so total time is $O(n)$. Costs are computed when they enter and leave the window; only the two pointers, running cost, and best length are stored, giving $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Enumerate every start:** Extending a fresh substring from each starting index is correct but takes $O(n^2)$ time when many long windows are affordable.
- **Prefix sums plus binary search:** A prefix-cost array can test interval sums and locate a boundary in $O(n\log n)$ time with $O(n)$ space.
- **Binary search the answer length:** Nonnegative costs make feasibility monotone by length, but each feasibility scan adds a logarithmic factor.
- **Zero budget:** Only contiguous runs of positions with zero conversion cost are usable.
- **No affordable character:** If every single-position cost exceeds the budget, return 0.
- **Identical strings:** Every position costs zero, so the entire string is valid.
- **Exact budget:** A total equal to `maxCost` is allowed.
- **One expensive index:** Shrinking may remove several cheap positions along with it; the pointers still consider the longest interval for every right endpoint.
