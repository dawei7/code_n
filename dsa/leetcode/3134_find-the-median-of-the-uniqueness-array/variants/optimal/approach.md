## General

The uniqueness array contains $T=n(n+1)/2$ values. Because an even-length array uses its smaller middle value, the desired element has one-based rank

$$
r = \left\lceil \frac{T}{2} \right\rceil = \left\lfloor \frac{T+1}{2} \right\rfloor.
$$

Constructing and sorting all $T$ distinct counts would be quadratic. Instead, for a candidate threshold $k$, define $F(k)$ as the number of subarrays containing at most $k$ distinct values. The predicate $F(k) \ge r$ is monotone: once enough uniqueness values are at most $k$, every larger threshold also has enough. The answer is therefore the smallest $k$ satisfying this predicate, found by binary search from $1$ through $D$.

For one threshold, use a sliding window. Maintain the smallest left endpoint such that `nums[left..right]` has at most $k$ distinct values. A frequency map supports removing values while the window has too many distinct elements. After restoring validity, every subarray ending at `right` and starting at an index from `left` through `right` is valid, contributing `right - left + 1` to $F(k)$.

The left endpoint never moves backward, so one threshold check is linear. It may stop as soon as the accumulated count reaches $r$. Binary search returns the first threshold whose cumulative count covers the median rank, which is exactly the value at that rank in the sorted uniqueness array.

## Complexity detail

Each threshold check moves both window endpoints at most $n$ positions and costs $O(n)$ time. Binary search performs $O(\log D)$ checks, for $O(n \log D)$ total time. The frequency map contains at most $D$ keys, using $O(D)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate every subarray:** Extend a set from every left endpoint and collect each distinct count. This is straightforward but needs $O(n^2)$ time and cannot handle $n=10^5$.
- **Build and sort the uniqueness array:** Materializing all $T$ counts adds quadratic storage and sorting overhead, far beyond the legal maximum input.
- **Count exactly $k$ distinct values:** Subtracting two at-most counts can recover exact frequencies, but the median needs only the monotone cumulative count, so the subtraction does unnecessary work.
- **Even number of subarrays:** The target rank is the lower of the two middle positions; using `T // 2 + 1` would select the upper median when $T$ is even.
- **All values equal:** Here $D=1$, every uniqueness value is `1`, and binary search returns `1` without a threshold check.
- **Large subarray count:** $T$ can be about $5\times10^9$, so fixed-width implementations must store counts in a 64-bit integer.
