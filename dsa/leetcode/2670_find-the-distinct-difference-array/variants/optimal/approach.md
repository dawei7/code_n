## General

Build a frequency map for the entire array; its number of keys is initially the suffix distinct count before any elements move. Maintain a separate set for values already included in the prefix.

At index `i`, first insert `nums[i]` into the prefix set. Then decrement that value's suffix frequency and remove its key when the count reaches zero, because the suffix begins strictly after `i`. The two container sizes now describe exactly the required prefix and suffix, so append their difference.

After each iteration, the prefix set contains precisely the values in `nums[0:i + 1]`, while the frequency-map keys are precisely the values occurring in `nums[i + 1:n]`. These facts hold initially and are preserved by moving the current occurrence between the structures. Their size difference therefore equals `diff[i]` at every index.

## Complexity detail

The frequency-map construction and left-to-right scan each take $O(n)$ expected time. The set, map, and output use $O(n)$ space. With $n \le 50$, a bounded-domain certificate replaces unreliable runtime tiers with exhaustive small-domain oracle checks and maximum-length boundaries.

## Alternatives and edge cases

- **Rebuild two sets per index:** This follows the definition directly but takes $O(n^2)$ time.
- **Prefix and suffix count arrays:** Two passes can precompute both distinct counts in $O(n)$ time, but storing both arrays is unnecessary.
- The suffix after the final index is empty, so the last answer equals the total number of distinct array values.
- Repeated occurrences do not change a distinct count until the first prefix occurrence or last suffix occurrence crosses the boundary.
- A single-element input returns `[1]`.
