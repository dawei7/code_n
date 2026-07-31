## General

**Choose a unique element that certifies each good subarray**

The OR of a subarray contains every bit set by any element in that range. It equals a particular element `x` in the subarray exactly when no other element contributes a bit that is absent from `x`.

A good subarray may contain several occurrences equal to its OR. Assign that subarray to the **rightmost** such occurrence. This makes the witness unique without changing which subarrays qualify.

Fix index `i` as the chosen witness and write `x = nums[i]`. On the left, find the nearest index whose value contains a bit absent from `x`; the left endpoint must come after this blocker. On the right, the endpoint must stop before both the nearest such incompatible value and the next occurrence equal to `x`. The second boundary guarantees that `i` remains the rightmost OR-valued witness.

If `left_blocker[i]` is the left incompatible index and `right_limit` is the smaller right boundary, there are `i - left_blocker[i]` legal left endpoints and `right_limit - i` legal right endpoints. Their product is the number of good subarrays assigned to `i`.

**Find incompatibility boundaries one bit at a time**

All legal values use at most 30 bits. In a left-to-right pass, remember the last index containing each bit. For `x`, the nearest left blocker is the maximum remembered index among bits that `x` does not contain. A symmetric right-to-left pass uses the next index containing every bit; a map simultaneously supplies the next equal value.

Every interval counted for `i` contains `x` and contains no bit outside `x`, so its OR is exactly `x`. Conversely, take any good subarray and its rightmost element equal to the OR. No incompatible value lies inside the interval, and no equal value lies to that witness's right, so its endpoints fall within the counted bounds for that index. Thus every good subarray is counted exactly once.

## Complexity detail

Each of the $n$ elements examines exactly 30 bit positions in each directional pass, so the fixed legal value width gives $O(n)$ time. The left-blocker array and next-equal map use $O(n)$ auxiliary space; the two bit-position arrays use constant space.

The benchmark defines size as $n$ and uses arrays of `1` values with lengths `16`, `64`, and `256`. Every subarray is good. The accepted boundary method and an independent same-class implementation should scale linearly, while a correct implementation that enumerates all endpoint pairs must inspect all $n(n+1)/2$ subarrays and should fail only the scaling verdict.

## Alternatives and edge cases

- **Enumerate all endpoint pairs:** Extending an OR from every left endpoint is straightforward and correct, but requires $O(n^2)$ time even if membership is maintained in a set.
- **Distinct suffix-OR states:** Compressing the different OR values of subarrays ending at each index limits each step to the bit width, but additional bookkeeping is needed to prove that the OR occurs within each represented range.
- **Monotonic-stack boundaries:** Numeric greater-than order does not capture the bitwise-subset relation, so an ordinary maximum stack cannot identify all incompatible values by itself.
- **Repeated witness values:** The next-equal boundary assigns an interval only to its rightmost OR-valued occurrence and prevents duplicate counting.
- **Zero:** A zero-only subarray has OR `0` and is good; a zero beside a nonzero value adds no bits and cannot invalidate that nonzero witness.
- **Single element:** Every one-element subarray is good because its OR is its only value.
- **Large answer:** Up to $n(n+1)/2$ intervals may qualify, so the result can exceed a signed 32-bit integer.
