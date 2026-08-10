## General

**Any final block must have length equal to the number of ones**

Let `k` be the total number of ones in `data`. Grouping all ones together means that, after the swaps, some contiguous block of exactly `k` positions contains a one in every position. A shorter block cannot hold all `k` ones, and a longer block is unnecessary because the required group itself contains only those ones.

Therefore, every possible final location corresponds to a length-`k` window in the original array. The task is to choose which such window can be turned into the all-one block using the fewest swaps.

The code obtains `k` with `data.count(1)`. Because the array is binary, this is also equal to `sum(data)`.

**Count the misplaced values inside a candidate window**

Suppose a length-`k` window currently contains `t` ones. It then contains `k - t` zeros. Since the entire array contains exactly `k` ones, there must also be exactly `k - t` ones outside the window.

One arbitrary-position swap can exchange one zero inside the window with one one outside it. That single swap increases the number of ones inside by one. Repeating this for every inside zero fills the window after exactly `k - t` swaps.

Fewer swaps are impossible because every zero occupying a desired block position must be replaced, and one swap can remove at most one such zero. Thus the exact cost for a candidate window is `k - t`.

Minimizing `k - t` is the same as maximizing `t`. The algorithm therefore finds `mx`, the greatest number of ones already present in any length-`k` window, and returns `k - mx`.

This argument depends on the move being an arbitrary swap, not necessarily an adjacent swap. Distance does not affect the cost: exchanging two far-apart positions still counts as one.

**Initialize the first fixed-size window**

`sum(data[:k])` counts the ones in indices zero through `k - 1`. This becomes both `t`, the current-window count, and `mx`, the best count seen so far.

The slice is used only for the initial window. Every later window count is updated incrementally rather than recomputed from all `k` positions.

**Slide one position at a time**

The loop starts with `i = k`, the first index just beyond the initial window. Adding `data[i]` includes the new rightmost value. Subtracting `data[i - k]` removes the old leftmost value. After these two operations, `t` is exactly the number of ones in the new window ending at `i` and beginning at `i - k + 1`.

The assignment `mx = max(mx, t)` preserves the largest window count encountered. When the loop finishes, every length-`k` window has been considered exactly once: the initial window before the loop and each subsequent starting position during a slide.

For `[1, 0, 1, 0, 1]`, `k = 3`. The first window contains two ones. The middle window contains one, and the last window contains two. Therefore, `mx = 2` and the answer is `3 - 2 = 1`. Indeed, either best window has one inside zero and one outside one, which can be exchanged in one swap.

**Why the algorithm is correct**

Any valid final arrangement chooses some contiguous block of `k` positions for all ones. For that block's original window, each zero must be replaced by an outside one, requiring at least as many swaps as the number of zeros in the window. That count is `k - t`.

Conversely, exactly `k - t` outside ones exist for those zeros, so pairing and swapping them constructs the desired block in exactly that many moves. The cost formula is therefore both a lower bound and achievable for every candidate.

The sliding window finds the maximum possible `t` over all candidate blocks. Its returned `k - mx` is consequently the smallest achievable cost among all final block locations, proving optimality.

**Why no final array must be constructed**

The problem requests only the minimum number of swaps. The counts prove that an appropriate pairing between inside zeros and outside ones always exists. Recording the specific indices or performing the swaps would add work and storage without changing the number. The solution keeps only the statistic needed to compare candidate windows.

## Complexity detail

Let `n` be `len(data)`. Counting all ones takes `O(n)` time. Creating and summing the initial slice takes `O(k)` time, which is at most `O(n)`. The sliding loop performs constant work for at most `n - k` positions. Total time is `O(n)`.

The manifest states `O(1)` auxiliary space. Algorithmically, the sliding-window state itself is constant-sized: `k`, `t`, `mx`, and `i`.

In exact Python semantics, however, `data[:k]` creates a temporary list containing `k` elements, so peak auxiliary storage can be `O(k)`, which is `O(n)` in the worst case. Replacing `sum(data[:k])` with an index-based sum or `sum(islice(data, k))` would realize the stated constant auxiliary-space bound. The maintained window after initialization uses no growing structure.

## Alternatives and edge cases

- **Recount every candidate window:** Summing all `k` entries for each start takes `O(nk)` time. Sliding updates change only one incoming and one outgoing value.
- **Track zeros instead of ones:** The exact same method can minimize the number of zeros in a length-`k` window directly. Since zeros equal `k - t`, the formulations are equivalent.
- **Record positions of all ones:** One can reason about target locations from the index list, but this uses `O(k)` explicit space and is unnecessary for arbitrary swaps.
- **Adjacent-swap interpretation:** If only adjacent swaps were allowed, distances and median positions would matter. This problem allows swapping any two positions, so each inside-zero and outside-one pair costs one.
- **No ones:** `k = 0`. The exact loop adds and subtracts the same element on every iteration, `mx` remains zero, and the result is zero.
- **Exactly one one:** A one-element block already groups it, so some length-one window contains one and the answer is zero.
- **All ones:** The only length-`n` window has `mx = k = n`, producing zero swaps.
- **Ones already contiguous:** The window covering that block contains `k` ones, so `mx = k` and no swap is needed.
- **Several equally good windows:** Only the minimum count is requested. Keeping the shared maximum number of ones is sufficient; no position needs to be returned.
- **Binary-array guarantee:** Summing a window counts ones only because every element is zero or one. The contract provides this condition.
- **Temporary slice:** The algorithmic idea is constant-state, but the exact initialization allocates `data[:k]`. Complexity documentation should distinguish that Python allocation from the sliding-window state.
