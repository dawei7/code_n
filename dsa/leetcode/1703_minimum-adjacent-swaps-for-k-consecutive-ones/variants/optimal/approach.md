## General
**Choose consecutive ones in occurrence order**

Record the original indices of all ones. An optimal group never skips an occurrence between two chosen ones: replacing an outer chosen one with a skipped inner one cannot increase any movement distance. It is therefore sufficient to inspect each length-`k` window in the ordered list of one positions.

If the selected original positions are `position[j]`, their final consecutive destinations have the form `start + j`. The cost is a sum of `abs(position[j] - (start + j))`. Define an adjusted coordinate `adjusted[j] = position[j] - j`; then the same cost becomes the sum of `abs(adjusted[j] - start)`. Subtracting the occurrence rank removes the one-cell spacing that the chosen ones must retain in the final block. In particular, already-consecutive ones receive identical adjusted coordinates and correctly cost zero.

**Center each window at its adjusted median**

For any fixed window of `k` adjusted coordinates, the sum of absolute distances is minimized by a median. Choose the middle adjusted value and sum distances from all values on its left and right. This median corresponds to the best starting index for the final consecutive block; no separate simulation of swaps or destination positions is needed.

Build prefix sums of the adjusted coordinates. For a window `[left, right)` with median index `middle`, the left distance sum is `median * (middle - left) - (prefix[middle] - prefix[left])`. The right distance sum is `(prefix[right] - prefix[middle + 1]) - median * (right - middle - 1)`. Both expressions are nonnegative because the adjusted positions are non-decreasing.

Slide the window over all $m-k+1$ choices and keep the smallest combined cost. Every feasible optimal group appears as one such window, and the median minimizes its destinations, so the smallest evaluated value is the global optimum.

## Complexity detail
Scanning `nums`, building adjusted positions and prefix sums, and evaluating at most $m$ windows takes $O(n)$ time because $m \le n$. The adjusted coordinates and prefix sums use $O(m)$ auxiliary space.

## Alternatives and edge cases
- **Direct swap simulation:** repeatedly moving chosen ones through zeros can take quadratic time and makes it difficult to compare all possible groups.
- **Evaluate every destination block:** trying every start and summing movement for `k` ones repeats work, taking $O(mk)$ or worse.
- **Median of raw indices:** summing distance to one raw position overcharges the mandatory gaps between consecutive destination ones; subtract each occurrence rank first.
- **Arbitrary subsets of ones:** enumerating combinations is unnecessary because an optimum always uses `k` consecutive occurrences.
- **`k = 1`:** any existing one already forms a valid group, so the cost is zero.
- **Already consecutive:** their adjusted coordinates are equal and the computed cost is zero.
- **Even `k`:** either middle adjusted value minimizes the absolute-distance sum; choosing index `left + k // 2` is valid.
- **Extra ones:** ones outside the selected occurrence window do not have to move and contribute no cost.
