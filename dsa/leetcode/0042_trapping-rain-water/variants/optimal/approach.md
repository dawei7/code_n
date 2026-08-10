## General

**Water above one position is controlled by two walls**

Water cannot remain above bar `i` unless some bar at or to its left and some bar at or to its right contain it. Let the tallest height on the left side, including `i`, be $L_i$, and let the tallest height on the right side, also including `i`, be $R_i$. The water surface at that position can rise only to the shorter of those two boundaries:

$$
W_i = \min(L_i, R_i) - \texttt{height}[i].
$$

Including the current bar in both maxima guarantees $L_i$ and $R_i$ are each at least `height[i]`, so $W_i$ is never negative. A taller wall on only one side is insufficient: water spills over the shorter side, which is why the formula uses `min` rather than `max`.

Because every bar has width 1, a vertical depth of $W_i$ at one index contributes exactly $W_i$ unit squares of water. The total answer is the sum over all indices.

**Precompute the left boundary at every index**

The list `left` has length `n`. It starts filled with `height[0]`, and the forward recurrence is

$$
L_i = \max(L_{i-1}, \texttt{height}[i]).
$$

This recurrence is correct because the prefix ending at `i` consists of the preceding prefix plus the current bar. Its maximum must be either the old prefix maximum or the new height. After the forward assignments, `left[i]` equals the tallest bar among indices 0 through `i`.

For example, heights `[4, 2, 0, 3, 2, 5]` produce left maxima `[4, 4, 4, 4, 4, 5]`. A shorter bar never lowers the known boundary; a taller bar replaces it.

**Build right boundaries in the same loop**

The list `right` begins filled with `height[-1]`. During forward loop counter `i`, the code updates position `n - i - 1`, thereby moving from right to left. Its recurrence is

$$
R_j = \max(R_{j+1}, \texttt{height}[j]).
$$

where `j = n - i - 1`. The position `j + 1` has already been computed, so this records the maximum height from `j` through the final index.

Combining both recurrences in one `for` loop is only a compact scheduling choice. The left update depends on the previously completed position to its left, while the right update depends on the previously completed position to its right. They write different arrays and do not interfere.

For the same example, right maxima are `[5, 5, 5, 5, 5, 5]` because the final height 5 dominates every suffix. The per-index depths are then `[0, 2, 4, 1, 2, 0]`, which sum to 9.

**Why the final expression is complete**

`zip(left, right, height)` aligns the two boundary maxima with the original bar at every index. For each triple `(l, r, h)`, `min(l, r) - h` is the water depth derived above. `sum` adds all unit-width columns.

This column-by-column accounting neither double-counts nor misses water. Every trapped unit square lies vertically above exactly one array index, and its height is below both that index's best left boundary and best right boundary. Conversely, every vertical level counted by the formula has walls at least that high on both sides, so it cannot escape horizontally.

At the first and last positions, one boundary maximum equals the bar itself. Their contribution is therefore zero, matching the physical fact that water cannot be held outside the elevation map.


After the forward part has processed index `i`, `left[i]` is the maximum of the complete prefix through `i`. This follows by induction from `left[0] = height[0]` and the maximum recurrence. The mirrored induction proves that each filled `right[j]` is the maximum of the suffix beginning at `j`.

Once those invariants hold for all positions, the shorter maximum is the highest level supported on both sides. Subtracting the bar height gives exactly the supported water depth, and summing gives the total trapped volume. Thus the method returns the required answer.

**A source-versus-manifest space discrepancy**

The selected file is algorithmically a dynamic-programming precomputation, not a constant-space two-pointer implementation. It allocates both `left` and `right`, each with $n$ entries. Therefore, its exact auxiliary-space complexity is $O(n)$. The variant manifest claims $O(1)$ space, but that claim does not match the selected source. The explanation must follow the executable implementation; treating its arrays as constant-space would be incorrect.

The source is safe under the given constraint $n \ge 1$, which makes both `height[0]` and `height[-1]` valid. It does not contain a separate empty-list guard because an empty elevation map is outside the documented input domain.

## Complexity detail

Creating each length-$n$ list takes $O(n)$ time. The combined precomputation loop performs $n - 1$ constant-time updates, and the zipped generator scans $n$ aligned elements for the sum. Total time is $O(n)$.

The two maximum arrays contain $2n$ values, so auxiliary space is $O(n)$. The generator passed to `sum` is lazy and uses only constant iterator state, but it does not eliminate the already allocated arrays. The returned integer uses $O(1)$ space. Consequently, the time claim in the manifest is satisfied, while its $O(1)$ space claim is not satisfied by this exact selected implementation.

## Alternatives and edge cases

- **Two pointers with running maxima:** Move inward from both ends and process the side with the smaller boundary. It computes the same per-column depths in $O(n)$ time and genuinely $O(1)$ auxiliary space, but its correctness invariant is subtler than explicit boundary arrays.
- **Monotonic decreasing stack:** When a taller bar arrives, pop basin bottoms and calculate horizontally bounded layers. It runs in $O(n)$ time and uses $O(n)$ stack space, with more involved width and bounded-height calculations.
- **Split at a global maximum:** Scan toward the tallest bar from each side, maintaining the best wall seen. The global maximum guarantees closure for both directional scans and uses constant extra space.
- **Brute-force boundaries:** For each index, rescan left and right for maxima. It implements the formula directly but costs $O(n^2)$ time.
- **Strictly increasing or decreasing heights:** One side never supplies a higher closing wall, so every computed depth is zero.
- **Flat terrain:** Left and right maxima equal every bar height, producing zero water.
- **Repeated peaks:** Equal-height walls contain water normally; the use of `max` and `min` does not require a unique maximum.
- **Valleys of height zero:** Zero is a valid bar height and simply increases possible depth when bounded by taller bars.
- **Single bar:** Both arrays contain that height and the only contribution is zero.
- **Empty list outside the contract:** Accessing `height[0]` would fail. The documented constraint starts at one element, so the selected source intentionally relies on that precondition.
- **Input preservation:** The method reads `height` and creates separate maximum arrays; it does not modify the elevation map.
