## General
**Separate non-wrapping and wrapping shapes**

Every valid circular subarray has one of two forms. It either lies entirely inside the ordinary array, or it wraps across the boundary and consists of a suffix plus a prefix. Standard maximum-subarray dynamic programming finds the best non-wrapping sum in one pass.

For a wrapping choice, consider the elements not selected. They form one ordinary contiguous middle subarray. If the total array sum is $T$ and that excluded middle has sum $M$, the wrapping sum is $T-M$. Maximizing it therefore means excluding the minimum-sum ordinary subarray.

**Track both Kadane recurrences together**

Maintain the best sum ending at the current position for both a maximum subarray and a minimum subarray. For each new value, either start a new subarray there or extend the previous ending subarray. Also accumulate the total sum and the best maximum and minimum seen anywhere.

The answer is the larger of the best ordinary maximum and `total - minimum_sum`. There is one necessary exception: when every value is negative, the minimum subarray is the entire array, and subtracting it would represent an empty selection with sum zero. In that case, return the ordinary maximum, which is the least negative single value. These two structural cases cover every legal circular subarray, so their best valid result is globally optimal.

## Complexity detail
Let $n$ be the length of `nums`. One pass updates a constant number of sums for each element, producing $O(n)$ time. The algorithm stores only the running total and constant-size dynamic-programming state, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Enumerate every circular start and length:** Incrementally summing all $n^2$ candidate subarrays is correct but takes $O(n^2)$ time.
- **Doubled array with a monotonic deque:** Prefix sums over two copies plus a deque can enforce the length-at-most-$n$ rule in $O(n)$ time, but it uses $O(n)$ space and more machinery.
- **All-negative input:** The complement formula would choose the empty subarray; return the ordinary maximum instead.
- **Single element:** The only legal non-empty subarray is the element itself.
- **Zeros:** A zero may be the best answer when every other value is negative.
- **At most one full traversal:** A circular subarray cannot reuse an index, so it may contain no more than $n$ elements.
