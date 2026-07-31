## General

**Separate the baseline from a window gain.** First compute the original action-price sum. For a candidate window, replacing an action `s` by hold changes its contribution by `-s * price`; replacing it by sell changes the contribution by `(1 - s) * price`. The modified profit is therefore the baseline plus the sum of those deltas over the two half-windows.

Compute the gain of the window beginning at day 0. Because a modification is optional, initialize the best gain with the larger of zero and that value.

**Slide with three changes.** Let `h = k / 2`. When the window start advances from `l` to `l + 1`, day `l` leaves the forced-hold half and regains its original contribution, adding `strategy[l] * prices[l]` to the gain. Day `l + h` moves from forced sell to forced hold; the difference between those two replacement contributions is exactly `-prices[l + h]`. Finally, day `l + k` enters the forced-sell half, adding `(1 - strategy[l + k]) * prices[l + k]`. These constant-time updates evaluate every window.

## Complexity detail

Computing the baseline and first gain takes $O(n)$ time in total, and the window start advances at most $n-k$ times with constant work per move. Total time is $O(n)$ and auxiliary space is $O(1)$.

The benchmark sets size $N=n$, uses `k = N / 2`, and provides tiers 32, 128, and 512 for a 16x span. The accepted rolling update is $O(N)$. A correct method that rebuilds the changed strategy and recomputes the full profit for every start takes $O(N^2)$ time and must finish all tiers but fail scaling.

## Alternatives and edge cases

- **Prefix sums:** Separate prefix sums for original, forced-hold, and forced-sell contributions also evaluate each window in $O(1)$, with $O(n)$ extra space.
- **Rebuild every strategy:** It is straightforward but copies and sums $n$ entries for each of $O(n)$ windows.
- **No modification:** Clamp the best gain at zero because every modification may be harmful.
- **Window covers the array:** There is exactly one candidate modification, still compared with the original strategy.
- **Negative original profit:** The same gain comparison applies; the answer need not be non-negative.
- **Independent trades:** Do not enforce inventory or budget rules that the contract explicitly excludes.
- **Large result magnitude:** Fixed-width implementations need a 64-bit accumulator for up to $10^5$ products of magnitude $10^5$.
