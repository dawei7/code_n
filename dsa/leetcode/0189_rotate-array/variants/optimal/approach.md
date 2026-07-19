## General
A rotation by the array length changes nothing, so first reduce the request to `k %= n`. This also handles `k` values much larger than the array. If the normalized value is zero, the array is already in its final state.

Write the original array as two contiguous blocks:

- `A` is the first $n - k$ elements.
- `B` is the last `k` elements.

The requested right rotation is `B A`. Three in-place reversals build exactly that order:

1. Reverse the whole array, producing `reverse(B) reverse(A)`.
2. Reverse the first `k` positions, restoring `B`.
3. Reverse the remaining positions, restoring `A`.

For `[1,2,3,4,5,6,7]` and $k = 3$, the block view is `A = [1,2,3,4]` and `B = [5,6,7]`. Whole-array reversal yields `[7,6,5,4,3,2,1]`; the two local reversals yield `[5,6,7,1,2,3,4]`.

This method is easy to reason about because each reversal is confined to a known range. A small helper that swaps endpoints while moving inward avoids slicing, since slice assignment may allocate temporary storage even though the visible mutation is in place.

The complete reversal transforms `A B` into `reverse(B) reverse(A)`. Reversing the first block transforms `reverse(B)` back to `B`, and reversing the second transforms `reverse(A)` back to `A`. The final array is therefore `B A`, which is precisely a right rotation by the normalized `k`. Reversal only permutes existing positions, so no element is lost or duplicated.

## Complexity detail
Each reversal is linear in the length of its range, and the three ranges total `2n` character swaps up to constants. Time is $O(n)$, and endpoint indices plus one swap temporary use $O(1)$ auxiliary space.

## Alternatives and edge cases
- Concatenating `nums[-k:] + nums[:-k]` is concise but allocates $O(n)$ temporary space.
- Performing `k` one-position shifts can take $O(nk)$ time.
- Cycle replacement also achieves $O(n)$ time and $O(1)$ space, but must track cycle completion carefully when $\gcd(n, k) > 1$.
- $k = 0$, a multiple of `n`, or a one-element array leaves the input unchanged.
- The contract guarantees a nonempty array; otherwise taking $k \bmod n$ would need an empty-input guard.
