## General

**Track the candies kept, not the block given away**

The sister must receive exactly `k` consecutive candies. The desired score is the number of flavors remaining outside that block.

The source maintains `cnt` as the frequency map of candies currently kept. A flavor is counted exactly when its map entry is positive, so `len(cnt)` is the current number of unique kept flavors.

The first possible shared block is indices 0 through `k - 1`. The kept candies are the suffix `candies[k:]`, so initialization is

`cnt = Counter(candies[k:])`.

`ans` begins as the number of keys in that counter.

**Slide the shared block one position right**

Suppose the current shared block starts at `i - k` and ends at `i - 1`. Moving it right makes two membership changes:

- `candies[i - k]` leaves the shared block and returns to the kept collection, so its count is incremented;
- `candies[i]` leaves the kept collection and enters the shared block, so its count is decremented.

The loop performs exactly these updates for `i` from `k` through `n - 1`.

If the decremented flavor reaches zero, the source removes its key with `pop`. This is essential because `len(cnt)` should count only flavors that still occur among kept candies. Leaving zero-count keys would overstate the answer.

After both updates, the map represents the next shared block, and `ans` is compared with its number of keys.

**Trace a window shift**

For `candies = [1, 2, 2, 3, 4, 3]` and `k = 3`, the first shared block is `[1, 2, 2]` and the initial kept suffix is `[3, 4, 3]`, with two flavors.

At `i = 3`:

- flavor 1 at index 0 returns to the kept side;
- flavor 3 at index 3 enters the shared block.

The shared block is now indices 1 through 3, flavors `[2, 2, 3]`. Kept flavors are 1, 4, and 3, giving three unique flavors and the optimal result in the example.

**Why outside pieces need no separate counters**

The candies kept form a prefix plus a suffix, which are not contiguous together. A single frequency counter can summarize their union. When the shared block moves, one candy transfers from shared to the left prefix and another transfers from the right suffix to shared.

The two frequency updates maintain the combined outside collection without storing prefix and suffix separately.

**Why `k = 0` works**

When no candies are shared, initialization counts all candies. In each loop iteration, `candies[i - k]` and `candies[i]` are the same candy because `k = 0`.

Its count is incremented and then decremented, producing no net change. Since the original count was positive, it does not become zero. `ans` remains the number of unique flavors in the full array.

**Why `k = n` works**

If all candies are shared, `candies[k:]` is empty, so the counter and answer start at zero. The loop range begins at `n` and is empty. Zero unique flavors are kept.

The same code therefore handles both extreme window sizes without special branches.

**Why the algorithm is correct**

Initially, `cnt` exactly describes candies outside the first legal shared block. Each iteration removes from the map the new right-edge candy entering the shared block and adds the old left-edge candy leaving it. By induction, it exactly describes the kept candies for every consecutive block of length `k`.

Removing zero keys makes `len(cnt)` precisely the number of flavors with at least one kept candy. The loop considers every possible shared block once, and `ans` retains the maximum value, so the returned result is optimal.

The input array is never modified.

## Complexity detail

Let $n$ be the number of candies and $u$ the number of distinct flavors.

Building the initial counter costs $O(n-k)$ expected time. The loop performs $n-k$ shifts, each with expected constant-time counter operations. Total time is $O(n)$.

The counter stores at most $u$ positive-frequency entries, so auxiliary space is $O(u)$, which is $O(n)$ in the worst case.

No window contents are copied during shifting; the initial slice `candies[k:]` itself temporarily allocates $O(n-k)$ space in Python in addition to the counter. Thus the exact peak auxiliary allocation can be $O(n)$ even when the final counter has fewer keys, while the manifest describes the persistent frequency state as $O(u)$.

## Alternatives and edge cases

- **Recount kept flavors for every block:** This can take $O(n^2)$ because most candies are reconsidered. Sliding updates only two memberships.
- **Track the shared block's frequencies:** One could derive kept presence from global counts minus shared counts. That needs two maps; tracking kept counts directly makes `len(cnt)` the answer.
- **Separate prefix and suffix sets:** Their intersection complicates unique counting. One combined counter handles duplicates across both sides.
- **Zero-count keys:** They must be removed or `len(cnt)` will include flavors no longer kept.
- **`k == 0`:** Incrementing and decrementing the same entry cancel, preserving all flavors.
- **`k == n`:** The kept collection is empty and the answer is zero.
- **Empty candy array:** Valid only with `k = 0`; initialization and loop both remain empty and return zero.
- **All candies one flavor:** The answer is one unless all copies are shared.
- **All flavors distinct:** Keeping $n-k$ candies preserves exactly $n-k$ flavors.
- **Flavor appears on both outside sides:** The combined counter correctly treats it as one unique flavor with multiple occurrences.
- **Initial slice allocation:** Python slicing adds a temporary linear allocation even though sliding itself is in place over the counter.
- **Input preservation:** Only frequencies change; `candies` remains intact.
