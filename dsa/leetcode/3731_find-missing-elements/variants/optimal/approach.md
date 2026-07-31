## General

Put every supplied value into a set so membership can be tested directly. The guaranteed surviving endpoints are `min(nums)` and `max(nums)`, which recover the exact bounds of the original range.

Visit every integer from the minimum through the maximum in increasing order. Append a value precisely when it is absent from the set. This produces sorted output without a separate sort, includes neither endpoint because both are guaranteed present, and returns an empty list naturally when the range has no gap.

## Complexity detail

Let $n$ be the length of `nums` and let $R=\max(\texttt{nums})-\min(\texttt{nums})+1$ be the recovered range width. Building the set takes expected $O(n)$ time, and scanning the range takes expected $O(R)$ time, for expected $O(n+R)$ total time. The set and output require $O(n+R)$ space in the worst case. Under the source bounds, both $n$ and $R$ are at most 100.

## Alternatives and edge cases

- **Sort and inspect adjacent gaps:** This also recovers every missing value but takes $O(n\log n+R)$ time and may mutate the input.
- **Boolean presence array:** A fixed array of 101 flags gives the same linear behavior under the stated value bound, but the set expresses membership without tying indices to that constant.
- **No missing values:** Every membership check succeeds, so the result remains empty.
- **Only endpoints remain:** Every interior integer is returned in increasing order.
- **Unsorted input:** Minimum, maximum, and set membership do not depend on the original order.
- **Range outside the endpoints:** Values below the minimum or above the maximum were never part of the recovered original range and must not be returned.
