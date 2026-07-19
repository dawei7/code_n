## General
**Trace one droplet across non-rising levels**

Start a candidate destination at `k`. To inspect the left side, move one position at a time while the next height is no greater than the current height; the droplet cannot cross the first upward step. Whenever a strictly lower height is found, remember its index. Updating only on a strict decrease preserves the position closest to `k` when the lowest level is a plateau.

If the left scan found a position lower than `k`, settle there immediately. Otherwise repeat the same scan to the right. If neither direction records a lower position, increment `heights[k]`.

**Apply droplets sequentially**

After each chosen destination is incremented, start the next droplet from the updated profile. This is essential because one unit of water can change the next unit's reachable path or preferred side.

For one direction, the scan visits exactly the contiguous positions the droplet can traverse before an upward barrier. The remembered closest occurrence of the minimum height is therefore its prescribed settling point on that side. Trying the entire left rule before the right rule enforces the required preference, and falling back to `k` covers the only remaining outcome. Repeating this faithful transition produces the final profile.

## Complexity detail
Let `n` be the terrain length and `v` the volume. Each droplet scans at most `n` positions across the two directions, so total time is $O(vn)$. The profile is updated in place using a constant number of indices, giving $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Enumerate every candidate and recheck its path:** This can reproduce the same choice but may take $O(vn^2)$ time.
- **Balanced structures for basins:** More elaborate range and level data structures can batch large volumes, but they add substantial complexity for the bounded input.
- **Flat lower plateau:** Settle at the lowest position closest to `k`, not at the far end of the plateau.
- **Both sides lower:** The left side has priority even if the right side also offers a valid low point.
- **No lower side:** The droplet stays directly at `k`.
- **Single terrain position:** Every droplet increments that only height.
- **Changing profile:** Never compute all destinations from the original terrain; earlier droplets affect later ones.
