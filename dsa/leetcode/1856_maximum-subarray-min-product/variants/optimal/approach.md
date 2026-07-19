## General
**Turn each value into a candidate minimum**

For a fixed element value, every array entry is positive, so the best subarray using that value as its minimum is the widest contiguous interval around it containing no smaller value. Extending within that legal region increases the sum without lowering the chosen minimum.

Maintain an increasing stack of pairs `(left, minimum)`. Each pair says that `minimum` can govern an interval beginning at `left` and continuing through the processed suffix. When a new value is no greater than the stack top, the top cannot extend across the new position. Pop it and evaluate its maximal interval ending immediately before the current index.

Carry the popped entry's left boundary into the new value. This allows the smaller or equal value to govern everything the popped minimum could cover. Popping equal values assigns their combined widest interval to one representative and avoids losing candidates on plateaus.

**Read interval sums in constant time**

A prefix-sum array gives the sum of `[left, right)` as `prefix[right] - prefix[left]`. After the scan, every remaining stack entry can extend to the array end, so evaluate those final intervals as well. Compare full integer products throughout and apply the modulus only once to the greatest product.

## Complexity detail
Prefix sums take $O(n)$ time and space. Every index is pushed once and popped at most once from the monotonic stack, so all boundary processing is $O(n)$ time. The prefix array and stack each use $O(n)$ space.

## Alternatives and edge cases
- **Enumerate all subarrays:** Maintaining a running sum and minimum avoids a third loop but still costs $O(n^2)$ time.
- **Separate left and right boundary arrays:** Two monotonic-stack passes are equally linear but store more explicit boundary state.
- **Equal minima:** A consistent strict/non-strict boundary rule is required so plateaus receive their full interval.
- **Strictly increasing input:** No stack entry pops during the scan; the final flush must evaluate every suffix.
- **Strictly decreasing input:** Each new element pops earlier minima and inherits their left boundary.
- **Single element:** Its min-product is the square of that value.
- **Modulo timing:** Maximize unreduced products first, then reduce only the answer.
- **Large sums:** Implementations with fixed-width integers need a 64-bit type for sums and products.
