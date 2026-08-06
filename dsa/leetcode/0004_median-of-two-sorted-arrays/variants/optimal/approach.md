## General
**Reformulate the median as a balanced cut**

The median separates the combined sorted multiset into a lower half and an upper half. Instead of locating the median value directly, choose a cut in each input so that the combined left side has the required size and every left-side value is no greater than every right-side value.

The active solution first swaps the arrays when necessary so that `nums1` is no longer than `nums2`. Let $m$ and $n$ be their lengths after that swap. The lower half must contain `left_size = (m + n + 1) // 2` values. If `cut1` values come from `nums1`, the other cut is forced to be `cut2 = left_size - cut1`. Only `cut1` is independent, and `low` and `high` binary-search its legal range from 0 through $m$.

**Only four boundary values matter**

Because both arrays are sorted, only values adjacent to the cuts can violate the combined order:

- `left1` is `nums1[cut1 - 1]`, or negative infinity when `cut1 == 0`;
- `right1` is `nums1[cut1]`, or positive infinity when `cut1 == m`;
- `left2` and `right2` are defined symmetrically around `cut2` in `nums2`.

The partition is valid exactly when `left1 <= right2` and `left2 <= right1`. The sentinels make cuts before the first element and after the last element obey the same comparisons as interior cuts.

**Why the binary-search updates are forced**

If `left1 > right2`, `nums1` contributes too many large values to the lower half. Setting `high = cut1 - 1` moves its cut left; because `cut2` then increases, the opposing boundary in `nums2` moves right. Any larger `cut1` would only worsen the failed inequality.

Otherwise the only invalid possibility is `left2 > right1`, so `nums1` contributes too few lower-half values. Setting `low = cut1 + 1` moves its cut right and forces `cut2` left. Any smaller `cut1` cannot repair that violation.

These failures are monotone, so each update discards half the remaining cut positions. Searching the shorter array both gives the required bound and keeps `cut2` within the longer array.

**Recover the median from a valid partition**

When both inequalities hold, `max(left1, left2)` is the greatest value in the lower half. If `total` is odd, the lower half owns the extra element and this value is returned as a float.

For an even `total`, `min(right1, right2)` is the least value in the upper half. Averaging those two boundary values gives the median. For `nums1 = [1, 2]` and `nums2 = [3, 4]`, the valid cuts are `cut1 = 2` and `cut2 = 0`, so the central values are 2 and 3 and the result is 2.5.

The size equation fixes the rank of the cut. Sorted order inside each array supplies the within-array comparisons, and the two tested inequalities supply the cross-array comparisons. Therefore a valid partition places every lower-half value before every upper-half value and identifies the exact combined median.

## Complexity detail
Let $m$ and $n$ be the original input lengths. Binary search considers $min(m,n)+1$ cuts in the shorter array, taking $O(\log(\min(m,n)))$ time. The algorithm stores only search bounds, two cut positions, and four boundary values, so its auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Fully merge:** is straightforward but costs $O(m+n)$ time and $O(m+n)$ additional space.
- **Two-pointer selection:** can stop after reaching the middle and use constant auxiliary space, but still takes linear time.
- **Search the numeric value domain:** complicates duplicate counting and depends on the value range; partition search works directly on ranks.
- **One empty input:** swapping makes `nums1` empty, and infinity sentinels select the middle value or values entirely from `nums2`.
- **Duplicate boundary values:** non-strict inequalities allow equal values to appear on both sides of a valid cut.
- **Invalid contract input:** the final exception is unreachable for legal sorted arrays with a non-empty combined length.
