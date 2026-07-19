## General
For each value, only its most recent occurrence matters. At index `i`, that occurrence gives the smallest distance from `i` among all earlier equal values; every still earlier occurrence is farther away.

Maintain a map from value to latest index. Before overwriting an entry, check whether `i - latest[value] <= k`. If so, the two distinct indices witness a valid pair. Otherwise update the entry to `i`, because this occurrence is the best candidate for all future positions.

For `[1,2,1,1]` with $k = 1$, the occurrence of `1` at index 2 is too far from index 0, but the map is updated. The next `1` at index 3 is only one position from index 2 and correctly qualifies. Keeping only the first occurrence would miss that pair.

Before index `i`, the map stores the greatest earlier index for each encountered value. If the current value's stored index lies within `k`, a valid equal pair exists. If it lies farther than `k`, every other earlier equal index is smaller and therefore even farther, so none can pair with `i`. Updating to `i` preserves the latest-index property. Thus every current occurrence is compared with the only earlier occurrence capable of giving its minimum distance, and the final result is exact.

## Complexity detail
Expected $O(1)$ map work per element gives expected $O(n)$ time. The map can contain one entry for every distinct value, using $O(n)$ space.

## Alternatives and edge cases
- A set containing only the previous `k` values uses $O(\min(n,k))$ space, but must expire the value leaving the window in the correct order.
- Comparing every index with the preceding `k` indices costs $O(nk)$.
- Storing the first occurrence rather than the latest can miss a closer later pair.
- $k = 0$ cannot satisfy two distinct indices. Adjacent duplicates qualify whenever $k \ge 1$.
