## General

Count valid subarrays by their right endpoint. While scanning index `index`, remember three positions:

- `last_invalid`, the latest element outside the inclusive interval from `minK` to `maxK`;
- `last_minimum`, the latest occurrence of `minK`;
- `last_maximum`, the latest occurrence of `maxK`.

Any subarray ending at `index` must start after `last_invalid`; otherwise it contains a value smaller than the required minimum or larger than the required maximum. It must also start no later than both remembered bound positions so that it contains at least one occurrence of each required value.

Therefore, its valid start indices are exactly

$$
\texttt{last\_invalid}+1,\ldots,
\min(\texttt{last\_minimum},\texttt{last\_maximum}).
$$

The number of such starts is
`max(0, min(last_minimum, last_maximum) - last_invalid)`. Add this contribution for every endpoint.

Every counted subarray contains both bounds and no value outside them, so its minimum and maximum are exactly the required values. Conversely, every fixed-bound subarray satisfies those position constraints and is counted once at its unique right endpoint.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. The algorithm performs constant work at each index, taking $O(n)$ time. Four integer accumulators use $O(1)$ auxiliary space.

The answer can be as large as $n(n+1)/2$, so fixed-width implementations must use a 64-bit result.

## Alternatives and edge cases

- **Enumerate all subarrays:** Updating a running minimum and maximum for every start/end pair is correct but costs $O(n^2)$ time.
- **Two at-most counts:** Inclusion-exclusion over subarrays constrained by thresholds can solve the problem, but the last-position formulation is more direct.
- **Equal bounds:** When `minK == maxK`, the two last-seen positions update together and every all-equal run contributes all of its subarrays.
- **Out-of-range value:** It invalidates every subarray crossing its position and resets the earliest allowed start.
- **Missing bound:** Until both required values have appeared after the latest invalid element, the contribution is zero.
- **Repeated bounds:** Only the latest occurrences matter for counting all valid starts at the current endpoint.
- **Overlapping subarrays:** Each endpoint contribution intentionally counts many starts; overlaps are distinct subarrays.
