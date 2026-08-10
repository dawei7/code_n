## General

**Simulate droplets sequentially**

Each unit of water changes one column level, which can change where the next unit settles. The exact solution processes `volume` droplets one at a time and mutates `heights` to represent terrain plus accumulated water.

For each droplet, it searches left first, then right, and finally settles at `k` if neither direction offers an eventual fall. This ordering exactly matches the problem’s preference rule.

**Search one direction across non-increasing levels**

For direction `d`, where `-1` means left and `1` means right, both `i` and candidate `j` begin at `k`.

The scan may continue while the next index is in bounds and

`heights[i + d] <= heights[i]`.

A higher adjacent column is a ridge that water cannot cross. An equal or lower column can be traversed while checking whether movement eventually reaches a lower level.

**Record only actual downward progress**

Whenever the next level is strictly lower, the code sets `j = i + d`. This records a location where the droplet would genuinely fall.

The scan still moves across following equal-height cells, but `j` is not changed by equality. After first falling onto a flat low plateau, moving farther along that plateau does not create another eventual fall, so the recorded settle point remains where the strict decrease was reached.

If the scan later finds another strict decrease, `j` updates again because that farther position is at an even lower reachable level.

**Why a candidate different from `k` proves movement**

If `j != k` after scanning, at least one strict descent was reachable in that direction without crossing a higher column. The droplet settles at `j`, so `heights[j]` is incremented and the direction loop breaks.

Because left is tried first, a left candidate wins even if a right-side fall is closer or deeper. That priority is explicitly required.

**Try right only when left cannot fall**

If the left scan ends with `j == k`, moving left never reaches a lower level. The for-loop proceeds to direction right and applies the same logic.

If both direction attempts finish without breaking, Python’s `for ... else` executes and increments `heights[k]`. The droplet rises at its original column because neither direction can eventually fall.

**Trace a plateau**

Suppose the levels near `k` are `[2, 1, 1, 2]` with the drop at the rightmost level two. Scanning left first moves from two to the adjacent one, a strict decrease, so that position becomes `j`. The scan may continue across the equal one, but equality does not change `j`. The droplet settles at the first lower position reached from `k`.

This matches the rule: after falling there, moving farther left along an equal level would not make it fall again.

**Why the current height array is the complete state**

Water and terrain affect future motion only through the total level at each column. Incrementing the chosen column incorporates the droplet permanently. No separate water matrix or history of paths is needed.

The infinitely high terrain outside the array is modeled by stopping at bounds; a droplet can never leave the array.

Because every unit is indivisible, incrementing exactly one entry per iteration also preserves the total-volume invariant: after `r` iterations, the sum of all levels has increased by exactly `r`.


For each direction, the scan follows exactly the maximal path that never steps upward. `j` records the most recent position reached by a strict decrease, so it is the correct settling site if that direction eventually falls. The left search is accepted before right, and `k` is used only if neither has a lower reachable point.

Thus one iteration places one droplet according to all priority rules. Because the height is updated before the next iteration, induction over `volume` proves the final levels are correct.

## Complexity detail

Let `n` be the number of columns and `v` the volume. A directional scan can traverse `O(n)` columns, and at most two directions are scanned for each droplet. Total time is `O(vn)`.

Only indices, a direction, and the existing height array are used. Auxiliary space is `O(1)`. The input list is mutated and returned.

## Alternatives and edge cases

- **Precompute fixed basins once:** This fails because every droplet changes levels and therefore future basins.

- **Choose the globally lowest reachable column:** The rule is directional and left-preferring, not a global minimum search.

- **Update candidate on equal height:** That would move water across a flat plateau even though it does not eventually fall there. Update only on strict decreases.

- **Left and right both offer falls:** Left wins regardless of depth or distance.

- **No fall in either direction:** Increase the level at `k` through the loop’s `else` clause.

- **Zero volume:** The outer loop runs zero times and returns the original levels.

- **Boundary drop index:** The out-of-bounds side is treated as an impassable infinitely high wall.

- **Input mutation:** Returned entries are final total levels, and the original list object is changed in place.
