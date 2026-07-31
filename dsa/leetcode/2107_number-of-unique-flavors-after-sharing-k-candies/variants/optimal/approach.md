## General

**Track the candies outside the shared block**

Every valid decision removes one window of exactly `k` consecutive candies. The objective concerns the two outside pieces, so maintain frequencies for the candies kept outside the current window rather than frequencies inside the window.

Start with indices $0$ through $k-1$ shared. Build `kept` from the suffix `candies[k:]`; the number of keys in this map is the number of unique flavors currently retained.

**Slide the fixed-length window**

Move the shared window one position right at a time. The candy that leaves its left edge becomes kept, so increment that flavor's outside frequency. The candy that enters the new right edge stops being kept, so decrement its outside frequency and delete the key when the count reaches zero.

After both updates, `len(kept)` is exactly the number of unique flavors in the prefix and suffix outside the new shared block. Record its maximum across the initial placement and every slide.

The invariant follows directly from the two boundary changes: candies strictly outside the window have their true multiplicity in `kept`, and candies inside it contribute nothing. Each possible length-`k` block appears once, so the maximum map size is the best achievable number of retained flavors.

## Complexity detail

Building the initial map and sliding across all window positions takes $O(n)$ expected time under standard hash-table behavior. If $u$ is the number of distinct flavors, the frequency map stores at most $u$ keys and uses $O(u)$ space.

## Alternatives and edge cases

- **Rebuild the kept set for every window:** Scan the prefix and suffix outside each candidate block. This is straightforward and correct but requires $O(n^2)$ time in the worst case.
- **Track window frequencies plus global frequencies:** A flavor remains kept when its window count is smaller than its total count. This also supports $O(n)$ expected time but needs two maps and a more indirect unique-count update.
- **No candies or `k = 0`:** The only shared block is empty, so the answer is the number of distinct input flavors, including zero for an empty array.
- **`k = n`:** The outside map is empty for the sole full-array window, and the answer is zero.
- Repeated occurrences matter only through whether at least one copy remains outside the shared block.
- Deleting zero-count keys is necessary because the map's key count is used as the unique-flavor count.
