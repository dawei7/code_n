## General
**Separating invalid centers from complete windows**

Initialize the length-$n$ result with `-1`. A complete window exists only when $W \le n$; otherwise this initialized result is final. When a window does fit, valid centers range from `k` through `n - k - 1`, while the untouched prefix and suffix correctly remain `-1`.

**Reusing almost the entire previous sum**

Compute the first window sum for indices `0` through `2 * k` and write its integer average at center `k`. Advancing the center by one removes exactly the old leftmost element and adds exactly the new rightmost element:

`window_sum += nums[center + k] - nums[center - k - 1]`.

Thus each subsequent average is obtained in constant time rather than summing all $W$ elements again.

**Why every result entry is correct**

Before writing a center, `window_sum` equals the sum of precisely its inclusive radius-$k$ interval. Integer division by the fixed positive length $W$ gives the required truncated average. Every valid center is visited once, and no invalid center overwrites its initial `-1`.

## Complexity detail
The first sum and all sliding updates together inspect $O(n)$ elements, so the time is $O(n)$. Beyond the required output array, the algorithm stores only the window length and running sum, giving $O(1)$ auxiliary space. The returned array itself uses $O(n)$ space.

## Alternatives and edge cases
- **Recompute every window:** Summing all $W$ values independently at each valid center is simple but takes $O(nW)$ time in the worst case.
- **Prefix sums:** A prefix-sum array also obtains each window sum in constant time, with $O(n)$ time overall but $O(n)$ additional space.
- **Convolution:** A box filter expresses the same operation but adds machinery unnecessary for one-dimensional integer windows.
- When `k` is zero, each one-element average equals the original value.
- When $W=n$, exactly one center receives the average of the entire array.
- When $W>n$, every result entry remains `-1`.
- Input values are nonnegative, so truncation toward zero agrees with the floor notation used above.
