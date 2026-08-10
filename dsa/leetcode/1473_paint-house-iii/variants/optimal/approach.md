## General

**A state must remember the last color and neighborhood count.** Define `f[i][j][k]` as the minimum cost to finish houses zero through `i` when house `i` has color `j` and the prefix contains exactly `k` neighborhoods. Color indices run from one through `n`; index zero is unused.

The table begins at positive infinity, meaning unreachable. A finite value always describes a valid coloring that respects every prepainted house.

**Initialize the first house.** Any nonempty painted prefix has one neighborhood. If house zero is unpainted, every color `j` is possible at cost `cost[0][j-1]`. If it is prepainted, only its fixed color is possible and costs zero.

No other first-row state becomes finite. This prevents repainting and prevents zero or multiple neighborhoods at one house.

**Determine whether the next house extends or starts a neighborhood.** For current color `j` and previous color `j0`, equal colors keep neighborhood count `k` unchanged. A different color starts a new neighborhood, so the previous prefix must have `k - 1` neighborhoods.

If house `i` is unpainted, the code tries every current color and adds `cost[i][j-1]` to either predecessor. If already painted, it fixes `j = houses[i]` and adds no cost.

The loop for `k` stops below `min(target + 1, i + 2)`. After processing `i + 1` houses, at most `i + 1` neighborhoods can exist, and values above target never help.

**Why all previous colors are examined.** The cheapest way to reach the same current color and count may end the previous prefix with any color. For equal `j0` the count stays; for every different `j0` it increases. Taking the minimum across all choices preserves the optimal prefix.

Positive infinity propagates safely: adding a finite paint cost to an unreachable predecessor remains unreachable.

**Extract exactly the target.** After the last house, the final color is unrestricted. The answer is the minimum `f[m-1][j][target]` across colors. If all are infinite, no valid coloring exists and the method returns `-1`.

**Trace one transition carefully.** Suppose the current prefix should end with color two and contain three neighborhoods. A predecessor ending in color two must already have three neighborhoods because appending the same color extends its final group. A predecessor ending in color one or three must have only two neighborhoods because changing to color two creates the third. If the current house is unpainted, the cost of color two is added to every candidate; if it is fixed as color two, that addition is zero. The minimum over these alternatives becomes the state value.

The recurrence never needs to remember where earlier neighborhood boundaries occurred. Their exact locations cannot affect future cost once the prefix length, last color, and count are known. This sufficiency of state is what prevents exponential enumeration of complete color sequences.
Every valid coloring of a state has a unique previous color. Removing the last house yields exactly the equal-color or different-color predecessor used by the recurrence. Conversely, every finite transition appends a permitted color, pays exactly its required cost, and updates neighborhoods correctly. Induction over houses proves each table entry is minimal.

**Be precise about stored complexity.** The source has states for house, color, and neighborhood, then loops over every previous color. It therefore takes `O(m target n^2)` time. It allocates all house layers, using `O(m target n)` space.

The manifest's `O(m target n)` time would require optimizing the previous-color minimum, and its `O(target n)` space would require rolling layers. Neither optimization appears in this exact file.

## Complexity detail

There are `O(m target n)` relevant states. Each examines `n` previous colors, producing `O(m target n^2)` time. Initialization and final extraction are smaller.

The three-dimensional table contains `m(n+1)(target+1)` entries, so exact auxiliary space is `O(m target n)`. Loop variables add constant space.

Rolling the house dimension would reduce space to `O(target n)`. Tracking the smallest and second-smallest previous-color values for each neighborhood count can remove the inner color factor and approach the manifest time.

The infinity sentinel is safe because all real painting costs are finite and nonnegative.

## Alternatives and edge cases

- **Rolling two house layers:** Only row `i-1` is read, reducing space to `O(target n)`.
- **Best and second-best previous colors:** This can choose the cheapest different-color predecessor in constant time per state, reducing the extra `n` transition factor.
- **Top-down memoization:** Cache house index, previous color, and neighborhood count; it explores the same decisions recursively.
- **All houses prepainted:** No costs are added; the fixed neighborhood count either matches target or yields `-1`.
- **First house prepainted:** Only its color gets finite cost zero at one neighborhood.
- **Same adjacent color:** It remains within the current neighborhood.
- **Different adjacent color:** It increases the count by one.
- **Target one:** Every final house must share one continuous color, subject to fixed houses.
- **Target equals m:** Every adjacent pair must differ.
- **Impossible fixed pattern:** Infinity survives to the target layer and returns `-1`.
- **Unpainted house:** Every color is tried with its exact row cost.
- **Prepainted house:** Other colors are never considered and no repaint cost is charged.
- **Neighborhood cap during filling:** Counts larger than the number of processed houses are impossible, and counts above target can never later decrease, so skipping them is safe.
- **Several equal-cost colorings:** The table retains their common minimum value; reconstructing a particular coloring is not requested.
- **Complexity reporting:** Use `O(m target n^2)` time and `O(m target n)` space for this source.
