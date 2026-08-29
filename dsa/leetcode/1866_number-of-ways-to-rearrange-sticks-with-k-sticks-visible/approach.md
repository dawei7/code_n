## General

**Build arrangements by adding the new shortest stick.** Let `f[i][j]` be the number of permutations of `i` uniquely sized sticks with exactly `j` visible from the left.

To derive the recurrence, take an arrangement of `i - 1` sticks, conceptually increase every length by one, and insert a new shortest stick of length one. Relative comparisons among existing sticks do not change.

There are `i` insertion positions: before every existing stick and after the last.

**Insert at the very front.** The shortest stick is visible only when nothing lies to its left. Placing it in the first position adds one visible stick, while all previously visible sticks remain visible behind it because this new stick is shorter than everything.

To end with `j` visible sticks, the old arrangement must have `j - 1`. This contributes `f[i - 1][j - 1]` ways.

**Insert in any other position.** There are `i - 1` non-front positions. In each, at least one longer stick lies to the left, so the new shortest stick is hidden. It does not block any existing stick because it is shorter, so the visible count remains `j`.

For every old arrangement counted by `f[i - 1][j]`, there are `i - 1` such insertion choices. This contributes `f[i - 1][j] * (i - 1)`.

Combining the disjoint cases gives:

`f[i][j] = f[i - 1][j - 1] + (i - 1) * f[i - 1][j]`.

**Base case with the empty arrangement.** `f[0][0] = 1` means there is one way to arrange zero sticks with zero visible sticks: choose nothing. This neutral base lets the first stick arise from the front-insertion term, producing `f[1][1] = 1`.

All other cells begin at zero. Impossible states such as more visible sticks than total sticks remain zero automatically.

**Fill in increasing stick count.** The outer loop raises `i` from one through `n`, so row `i - 1` is complete before row `i` uses it. The inner loop computes visible counts one through `k`. Values beyond requested `k` are unnecessary for the final answer because the recurrence for smaller `j` never depends on larger columns.

**Trace `n = 3, k = 2`.** With two sticks, there is one arrangement with two visible sticks and one with one visible stick. Adding the new shortest stick for `i = 3`:

- front insertion into the one-visible arrangements contributes one way;
- either of two non-front positions in a two-visible arrangement contributes two ways.

The total is three, matching the sample.

**Why insertion is a bijection.** Every permutation of `i` sticks contains the unique shortest stick. Removing it and reducing all other labels by one recovers one unique `i - 1` arrangement and its insertion position. The shortest stick is visible exactly in the front case. Therefore the recurrence neither misses nor double-counts any arrangement.

**Modulo handling.** Counts are added and multiplied modulo `1,000,000,007` at every cell. Modular arithmetic preserves the requested final remainder and keeps table values bounded.

## Complexity detail

The nested loops compute `n * k` states, each in constant time. Running time is `O(nk)`.

The exact source allocates a full `(n + 1)` by `(k + 1)` table, so its space usage is `O(nk)`. This differs from the manifest’s `O(k)` claim, which would require retaining only the previous row or updating a one-dimensional array in descending `j` order.

## Alternatives and edge cases

- **Rolling two rows:** Only row `i - 1` is needed, reducing space to `O(k)` without changing time.
- **One-dimensional descending update:** Updating visible counts from high to low also achieves `O(k)` space.
- **All sticks visible, `k = n`:** Only strictly increasing order works, and the recurrence returns one.
- **Exactly one visible stick:** The longest stick must be first, while the remaining sticks can appear in any order.
- **Single stick:** It is necessarily visible, giving one way for `k = 1`.
- **Impossible `k > n` outside constraints:** Corresponding states remain zero.
- **Front insertion:** The shortest stick gains visibility but cannot hide any existing stick.
- **Non-front insertion:** A longer left neighbor hides the new shortest stick, leaving visibility unchanged.
- **Unique sizes:** The removal-and-relabel bijection depends on one uniquely identifiable shortest stick.
- **Modulo placement:** Each state can be reduced immediately because only addition and multiplication follow.
- **Full-table mismatch:** The checked-in code does not realize the manifest’s rolling-space optimization.
- **Zero base state:** `f[0][0]` is a combinatorial neutral case, not a physical nonempty arrangement.
- **Columns above `i`:** States with more visible sticks than total sticks remain zero because neither recurrence source can make them nonzero.
- **Columns above requested `k`:** They are omitted safely because `f[i][j]` depends only on columns `j` and `j - 1`, never on a larger visible count.
- **Why adding the shortest is convenient:** Adding the tallest would change visibility for sticks to its right and complicate the state. The shortest affects only whether it is itself visible, giving the clean two-case recurrence.
- **Arrangement labels:** Relabeling old lengths upward by one preserves every longer-than comparison among them, so it preserves their complete visibility pattern before insertion.
