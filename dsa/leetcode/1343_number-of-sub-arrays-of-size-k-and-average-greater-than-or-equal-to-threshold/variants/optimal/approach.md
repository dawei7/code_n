## General
**Compare sums instead of dividing**

A length-`k` window has average at least `threshold` exactly when its sum is at least `k * threshold`. This equivalent integer comparison avoids both floating-point representation and accidental truncation.

Compute the sum of the first `k` elements and test it. Then move the window one position at a time: add the newly entering element and subtract the element that just left. Test the updated sum after every move and increment the answer when it reaches the target.

The initial sum is exact for the first window. Each update removes precisely the old left endpoint and adds precisely the new right endpoint, so by induction it remains the exact sum of the current window. Every possible length-`k` start is visited once, proving the final count.

## Complexity detail
The initial window and all subsequent updates together read $O(n)$ elements and take $O(n)$ time. The rolling sum, target, and counter use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Prefix sums:** A prefix array answers every window sum in constant time after $O(n)$ preprocessing, but uses $O(n)$ extra space.
- **Rescan every window:** Explicitly summing each length-`k` subarray takes $O(nk)$ time and can become quadratic.
- **Window length one:** Compare each individual value with the threshold.
- **Whole array window:** When $k=n$, exactly one subarray is tested.
- **Exact threshold:** Equality qualifies.
- **Fractional average:** Compare sums rather than applying integer division.
- **Zero threshold:** Every legal positive-value window qualifies.
- **Overlapping windows:** Count each qualifying start independently.
