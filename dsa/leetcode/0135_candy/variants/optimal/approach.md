## General
**Each neighbor direction contributes an independent lower bound**

Initialize every child with one candy, the unconditional minimum. In a left-to-right pass, whenever `ratings[i] > ratings[i - 1]`, set `candies[i] = candies[i - 1] + 1`. This computes the smallest count forced by an increasing run from the left. Equal or lower ratings impose no left-neighbor increase.

Scan back from right to left to enforce the symmetric requirement. When `ratings[i] > ratings[i + 1]`, child $i$ needs at least `candies[i + 1] + 1`; take the maximum of that value and the amount already required by the left pass. The maximum is essential at a peak, where replacing the first value outright could break the longer slope on its other side.

**The pointwise maximum is the unique minimum contribution at every position**

Any valid distribution must meet both directional lower bounds for each child. The two passes assign exactly their maximum, so every strict rating comparison receives a corresponding strict candy comparison. Increasing a value is unnecessary, while decreasing any value below its computed bound would violate at least one adjacent requirement. Consequently the sum of the resulting array is globally minimal.

## Complexity detail
The two directional scans and the final sum take $O(n)$ time. The `candies` lower-bound array uses $O(n)$ auxiliary space.

## Alternatives and edge cases
- **Repeatedly repair violated neighbors:** eventually converges but can require $O(n^2)$ updates on a long slope.
- **Process children by sorted rating:** can propagate from lower-rated neighbors but costs $O(n \log n)$ time and needs original positions.
- **Track ascending and descending slopes in one pass:** achieves $O(1)$ auxiliary space but requires more delicate peak and plateau accounting.
- Equal adjacent ratings impose no relative candy requirement.
- A single child receives one candy.
- Strictly rising or falling ratings receive counts `1..n` in the corresponding direction, while a peak must satisfy both slopes.
