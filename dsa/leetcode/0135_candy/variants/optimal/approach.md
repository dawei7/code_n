## General
**Left-to-right propagation establishes every left-neighbor lower bound**

Initialize every child with one candy, the unconditional minimum. Scan left to right; when `ratings[i] > ratings[i - 1]`, set `candies[i] = candies[i - 1] + 1`. Equal or lower ratings impose no requirement to exceed the left neighbor, so their current one-candy baseline remains sufficient for this direction.

**Right-to-left propagation adds the opposite lower bound without erasing the first**

Scan right to left. When `ratings[i] > ratings[i + 1]`, the right-side rule requires at least `candies[i + 1] + 1`. Assign the maximum of this requirement and the existing left-pass value. Overwriting unconditionally could reduce a peak below the amount required by a longer rising slope on its left.

**Each child's final candy count is the maximum of two necessary bounds**

After the first pass, all constraints from a lower-rated left neighbor hold with minimal directional counts. During the second pass, processed constraints from lower-rated right neighbors also hold. Taking maxima can only increase counts, so it cannot invalidate a previously satisfied inequality.

**Trace a valley and a peak**

The forward pass gives `[1,1,2]`. The backward comparison raises the first child above rating `0`, producing `[2,1,2]` and total five.

**Two directional lower bounds meet at each child**

The left-to-right pass computes the minimum candy count required by increasing rating runs from the left. The right-to-left pass supplies the analogous lower bound from the right.

Any valid distribution must satisfy both bounds at every child, so their maximum is necessary. Assigning exactly that maximum also satisfies each neighboring inequality in its relevant direction. No position can be lowered without violating a bound, making the total minimal.

## Complexity detail
Two scans and one sum take $O(n)$ time. The candy lower-bound array uses $O(n)$ space.

## Alternatives and edge cases
- **Repeatedly repair violations:** may require $O(n^2)$ updates.
- **Sort children by rating:** can work with indices but uses $O(n \log n)$ time.
- **One-pass slope accounting:** can achieve $O(1)$ space but is more intricate around peaks and equal ratings.
- Equal adjacent ratings impose no relative candy constraint. A one-child input returns one.
- Strictly rising or falling ratings receive `1..n` in the appropriate direction; peaks must satisfy both slopes.
