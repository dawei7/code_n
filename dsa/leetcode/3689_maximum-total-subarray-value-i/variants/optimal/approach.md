## General

**Bound every subarray by the global range.** Let the global minimum and maximum of `nums` be $m$ and $M$. Every subarray uses elements from the original array, so its minimum is at least $m$ and its maximum is at most $M$. Consequently, no subarray can have value greater than $M-m$.

**Span the two extrema to attain the bound.** This upper bound is attainable. Consider the positions of $m$ and $M$ and take the subarray spanning the earlier position through the later one. That interval contains both values, so its maximum is $M$, its minimum is $m$, and its value is exactly $M-m$.

**Reuse the best interval `k` times.** Because the same interval may be chosen more than once, use this maximum-value subarray for every one of the `k` required choices. Each choice contributes $M-m$, giving `k * (M - m)`. No different collection can do better because every individual contribution is bounded by the same global range. A single scan can obtain both extrema.

## Complexity detail

Let $n = \lvert\texttt{nums}\rvert$. Finding the minimum and maximum examines all $n$ elements, so the time complexity is $O(n)$. The calculation stores only the extrema and final product, requiring $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate every subarray:** Computing each interval's range eventually finds the same global range but costs at least $O(n^2)$ time and is unnecessary once repetition is recognized.
- **Select different intervals greedily:** Distinctness is not required, so ranking or consuming intervals adds constraints absent from the contract.
- **Singleton array:** The minimum equals the maximum, making every possible contribution and the final total zero.
- **All values equal:** As with a singleton, every subarray range is zero for any positive `k`.
- **Large product:** Both the value range and `k` can be large, so fixed-width implementations need a 64-bit result type.
