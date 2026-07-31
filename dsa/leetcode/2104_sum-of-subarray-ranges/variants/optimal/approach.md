## General

**Turning ranges into two contribution sums**

For any subarray, its range is its maximum minus its minimum. Summing these terms separately gives

$$
\sum_{\text{subarrays}} \max - \sum_{\text{subarrays}} \min.
$$

Instead of visiting every subarray, count how many times each `nums[i]` supplies each extreme. Suppose the closest boundary on the left is at index $L$ and the closest boundary on the right is at index $R$. If every interval that starts after $L$, ends before $R$, and contains $i$ assigns its extreme to `nums[i]`, then that value contributes to $(i-L)(R-i)$ subarrays.

**Finding all boundaries with monotonic stacks**

Run one stack pass for maxima. Indices remain in non-increasing value order. When a strictly larger value at `right` arrives, pop `middle`; the new stack top is its left boundary and `right` is its right boundary. Add

$$
\texttt{nums[middle]}(\texttt{middle}-L)(R-\texttt{middle})
$$

to the maximum sum. A sentinel step after the array pops every index that has no larger value to its right.

Run the symmetric pass for minima, maintaining non-decreasing values and popping when a strictly smaller value arrives. Subtract this minimum contribution sum from the maximum contribution sum.

**Assigning equal values exactly once**

The comparisons pop only on a strict inequality. Equal values therefore remain together on the stack: the previous equal value acts as the left boundary, while the next strictly better extreme acts as the right boundary. This asymmetric ownership prevents a subarray containing duplicate maxima or minima from being counted for more than one equal index.

Each pop finalizes exactly one index, and every index is eventually popped. The boundary choices enumerate precisely all subarrays for which that index owns the selected maximum or minimum, so the difference of the two complete contribution sums equals the requested sum of ranges.

## Complexity detail

Each index is pushed and popped once in the maximum pass and once in the minimum pass. The total time is $O(n)$. Either monotonic stack can hold all $n$ indices, so the auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Expand every left endpoint:** Maintain a running minimum and maximum while extending each subarray to the right. This is direct and uses $O(1)$ auxiliary space, but takes $O(n^2)$ time.
- **Range-query preprocessing:** Sparse tables can answer each interval's minimum and maximum quickly, yet enumerating all $\Theta(n^2)$ subarrays still makes the overall method quadratic.
- **Equal values:** Strict pop comparisons are essential to give every duplicate-owned subarray to exactly one index.
- A single-element array and an all-equal array both produce zero because every subarray has identical minimum and maximum.
- Negative values require no special ordering rule; their signed maximum and minimum contributions cancel correctly.
- The result can exceed 32-bit integer range even though each input value fits in that range, so fixed-width implementations need a 64-bit accumulator.
