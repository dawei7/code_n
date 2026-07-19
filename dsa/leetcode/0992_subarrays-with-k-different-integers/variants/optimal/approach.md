## General
**Convert exact counting into two monotone counts:** A sliding window naturally maintains an upper bound on the number of different values, but “exactly” is not monotone as the left endpoint moves. Let $A(m)$ be the number of subarrays containing at most $m$ different integers. Every subarray counted by $A(k)$ either has fewer than $k$ different integers or exactly $k$, while $A(k-1)$ contains precisely the former group. Therefore the requested count is $A(k)-A(k-1)$.

**Count all valid endings with one window:** For a fixed right endpoint, extend the window and update the new value's frequency. While the number of different integers exceeds the limit, move the left endpoint rightward, decrementing frequencies and removing a value from the distinct count when its frequency reaches zero. After shrinking, every start position from `left` through `right` forms a valid subarray ending at `right`, contributing `right - left + 1` to $A(m)$.

Both pointers only move forward, so each element enters and leaves a window at most once. Applying the helper with limits `k` and `k - 1` and subtracting the results counts every exactly-`k` subarray once.

## Complexity detail
Each of the two sliding-window passes processes $N$ right endpoints and advances its left endpoint at most $N$ times, for $O(N)$ total time. Frequencies for values from $1$ through $N$ require $O(N)$ space.

## Alternatives and edge cases
- **Enumerate every start and end:** Growing a distinct-value set from each start is straightforward but takes $O(N^2)$ time in the worst case.
- **One exact-`k` window without extra state:** A single left boundary loses how many removable duplicates precede the first essential value, so it cannot directly count every valid start.
- **All values equal:** With `k = 1`, all $N(N+1)/2$ nonempty subarrays qualify.
- **Too few different values:** If the entire array contains fewer than `k` different integers, the result is zero.
- **Limit zero:** The helper call $A(k-1)$ receives zero when `k = 1`; only the empty window is allowed, so it contributes no nonempty subarrays.
