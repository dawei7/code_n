## General
**Restrict attention to legal starting positions**

A length-`k` subarray beginning at index `i` ends at `i + k - 1`, so its start must satisfy $0 \le i \le n-k$. Values after index `n-k` can occur inside a candidate but cannot begin one. Scan exactly this legal prefix of starting positions.

**Use the first differing value**

Every pair of candidates has different first elements because all values in `nums` are distinct. Their lexicographic comparison is therefore decided immediately at position zero; no later element can overturn it. The candidate whose starting value is greatest is the unique largest candidate.

Track the index of the greatest value among `nums[0]` through `nums[n-k]`. Once the scan finishes, return the `k` consecutive elements starting at that index. The scan considers every legal candidate, and the distinctness guarantee proves that the chosen starting value beats every other candidate at their first comparison position.

## Complexity detail
Scanning the $n-k+1$ legal starting positions and copying the $k$ result elements takes $O(n-k+1+k)=O(n)$ time. Apart from the returned length-$k$ list, the scan stores only one index, so total space is $O(k)$ and auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Materialize and compare every window:** generating all slices and taking their maximum is direct, but copying $k$ elements for each of $n-k+1$ windows costs $O((n-k+1)k)$ time and space across the generated candidates.
- **Sort candidate starts:** sorting the legal indices by their first values finds the same start in $O(n\log n)$ time, although only one maximum is needed.
- **Compare candidates element by element:** this is unnecessary under the distinct-values guarantee because candidates always differ at their first element.
- **Entire array:** when `k == n`, index `0` is the only legal start and the whole array is returned.
- **Single element:** when `k == 1`, choose the maximum value as a one-element result.
- **Late maximum:** the largest value in the entire array may lie after index `n-k` and therefore cannot start a valid window.
- **Value magnitudes:** only relative order matters; the greedy argument does not depend on the gaps between values.
- **Contiguity:** return a slice of the original order rather than the globally largest `k` values.
