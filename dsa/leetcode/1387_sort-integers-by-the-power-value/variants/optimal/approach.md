## General
**Memoize complete sequence suffixes.** Start with power `0` for `1`. To evaluate a number, follow its Collatz sequence while recording previously unknown states until reaching a memoized value. Walk the recorded path backward, assigning each state one more step than its successor.

Every later sequence that meets any cached state can stop immediately. Thus shared suffixes across the interval are evaluated once rather than rediscovered for every starting integer.

**Sort with both ordering keys.** Evaluate the power of each integer from `lo` through `hi`, then sort using the pair `(power, value)`. Including the value as the second key implements the required tie rule directly. Return index `k - 1` from the sorted list.

## Complexity detail
Each of the $U$ distinct Collatz states is transitioned and memoized once, costing $O(U)$ time and space. Sorting the $R$ interval values costs $O(R \log R)$ time and stores $O(R)$ values. Together the bounds are $O(U + R \log R)$ time and $O(U + R)$ space.

## Alternatives and edge cases
- **Recompute every sequence:** Calculate each starting value's full power independently. It is correct but repeats shared Collatz suffixes.
- **Comparator recomputation:** Invoke uncached power calculations during every sort comparison. This can multiply sequence work by $O(R \log R)$ comparisons.
- **Bottom-up only to `hi`:** Collatz sequences can rise above `hi`, so a fixed array limited to the input interval is insufficient.
- **Power tie:** Place the smaller integer first.
- **Range containing one:** The power of `1` is zero.
- **Single-value range:** The only value is returned for `k = 1`.
- **One-indexed rank:** Convert `k` to list index `k - 1`.
