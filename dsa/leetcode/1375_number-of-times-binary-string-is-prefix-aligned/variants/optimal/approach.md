## General
**Replace the bit string with one boundary.** After `i` steps, exactly `i` distinct positions are on. Those positions are exactly $1, 2, \ldots, i$ if and only if none lies to the right of `i`. Track the largest position encountered so far as `rightmost`.

At step `i`, every seen position is at most `i` exactly when `rightmost == i`. Since there are `i` distinct seen positions drawn from the `i` available positions in that prefix, they must fill the entire prefix. Conversely, a prefix-aligned state cannot contain an on bit beyond `i`, so its maximum is necessarily `i`. Count each step satisfying this equality.

## Complexity detail
The scan processes each of the `n` flips once and performs constant work per entry, so time is $O(n)$. The running maximum and answer counter use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Materialize and rescan the bits:** Mark each flipped position and test the current prefix after every step. This is correct but can take $O(n^2)$ time.
- **Track a set of missing positions:** Removing each flip and checking whether the prefix is complete works, but requires $O(n)$ additional space.
- **First position delayed:** No alignment occurs until every earlier gap is filled, even if many positions to its right are already on.
- **Already ordered flips:** For `[1,2,...,n]`, every step is prefix-aligned.
- **Reverse order:** Only the final step is aligned when positions are flipped from `n` down to `1`.
- **Final step:** It always counts because all `n` positions are on and the running maximum equals `n`.
