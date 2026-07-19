## General
**Turn selection into a monotone counting question**

For a candidate sum limit $x$, count how many non-empty subarrays have sum at most $x$. This count never decreases as $x$ grows. Therefore, the requested answer is the smallest $x$ for which the count reaches at least `k`.

The answer lies between the smallest single element and

$$
S = \sum_{i=0}^{N-1} \texttt{nums[i]},
$$

so binary search can find that first sufficient limit.

**Count qualifying subarrays with one sliding window**

Fix a candidate $x$ and move a right endpoint from left to right. Add the new value to a running window sum. While that sum exceeds $x$, remove values from the left.

Because every array value is positive, once the window sum is at most $x$, every subarray ending at the current right endpoint and starting between `left` and `right` also has sum at most $x$. There are `right - left + 1` such subarrays. Any earlier start would have a larger sum and cannot qualify, so adding this quantity counts exactly all qualifying subarrays ending at that position.

At the end of the binary search, every smaller limit has fewer than `k` qualifying sums, while the returned limit has at least `k`. This is precisely the value occupying rank `k`, including when several different subarrays share that value.

## Complexity detail
For each tested limit, both sliding-window pointers move forward at most $N$ times, so counting costs $O(N)$. The inclusive search range has width at most $S$, requiring $O(\log S)$ counting passes and $O(N \log S)$ time overall. The algorithm stores only scalar indices, sums, counts, and binary-search bounds, giving $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Enumerate and sort every subarray sum:** This direct method materializes $N(N+1)/2$ values, requiring $O(N^2)$ space and at least quadratic work before sorting.
- **Prefix sums plus per-start binary search:** Prefix sums can count valid endpoints in $O(N \log N)$ per candidate, but positivity permits the faster linear sliding-window count.
- **Smallest rank:** The first value is the minimum array element because every longer positive subarray has a strictly larger sum than each of its elements.
- **Largest rank:** Rank $N(N+1)/2$ selects the sum of the entire array.
- **Repeated sums:** Equal numeric sums occupy separate ranks when they come from different subarrays.
- **Single element:** The only legal rank is one, and its answer is that element.
