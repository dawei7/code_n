## General

**Count groups by their middle tile**

Every circular group of three has one unique middle index `i`. Its neighbors are `i - 1` and `i + 1`, interpreted modulo $n$. Python's negative index already wraps `i - 1` when `i=0`, while `(i + 1) % n` wraps the right neighbor of the final tile.

Check whether `colors[i]` differs from both neighboring values and add one exactly when it does. Iterating all $n$ middle indices examines every eligible group once, including the two groups that cross the array boundary.

The condition is precisely the definition of an alternating group, so every counted center is valid. Conversely, any valid circular group has a middle index visited by the scan, and both comparisons succeed there, so no valid group is omitted.

## Complexity detail

The scan performs constant work for each of the $n$ tiles. Time complexity is $O(n)$ and auxiliary space is $O(1)$.

Modulo is used only for the right neighbor; the input array is never copied or extended.

## Alternatives and edge cases

- **Extend the array:** Appending the first two colors permits ordinary consecutive windows, but it allocates $O(n)$ extra space unnecessarily.
- **Rotate for every group:** Constructing a fresh rotation around each middle tile is correct but takes $O(n^2)$ time.
- **Linear-only windows:** Scanning only indices `1` through `n-2` misses groups that cross the circular boundary.
- **All equal:** No middle differs from either neighbor, so the answer is zero.
- **Perfect alternation:** When an even-length circle alternates throughout, every tile is a valid middle.
- **Odd length:** A binary odd cycle cannot alternate at every boundary, but several local groups may still qualify.
- **Minimum length:** With three tiles, the same three positions form three oriented groups with different middle tiles.
- **Binary colors:** For this contract, differing from both neighbors also implies the two neighbors share a color.

