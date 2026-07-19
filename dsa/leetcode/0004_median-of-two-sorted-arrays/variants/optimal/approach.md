## General
**Reformulate the median as a balanced cut**

The median separates the combined sorted multiset into a lower half and an upper half. Instead of locating the median value directly, choose a cut in each input so that:

- the combined left side contains exactly half the elements, with the extra element on the left when the total is odd;
- every value on the left is at most every value on the right.

Let `A` be the shorter array and `B` the longer one. If `i` elements of `A` go left, the required left-half size fixes the other cut:

`j = (m + n + 1) // 2 - i`.

There is only one independent choice, `i`, and it ranges from zero through `m`.

**Only four boundary values matter**

Because each array is already sorted, internal elements cannot violate the combined partition. Define:

- `Aleft = A[i - 1]` and `Aright = A[i]`;
- `Bleft = B[j - 1]` and `Bright = B[j]`.

The cut is valid exactly when `Aleft <= Bright` and `Bleft <= Aright`. Treat a missing left boundary as negative infinity and a missing right boundary as positive infinity. These sentinels let empty sides use the same comparisons as interior cuts.

**Why binary search knows which direction to move**

If `Aleft > Bright`, too many large values from `A` were placed on the left. Decreasing `i` moves `Aleft` downward and, because `j` increases, moves `Bright` upward; cuts farther right cannot repair the violation.

If `Bleft > Aright`, the cut in `A` is too far left. Increasing `i` moves `Aright` upward and decreases `j`, moving `Bleft` downward. Cuts farther left cannot repair this violation.

Those monotone failures justify discarding half the remaining cuts at each step. Searching the shorter array is essential: it gives the required logarithmic bound and keeps the complementary cut `j` within the longer array.

**Recover the median from a valid partition**

Once both cross-boundary inequalities hold, the left side contains exactly the lower half of the combined order. Its largest value is `max(Aleft, Bleft)`. If the total length is odd, that value is the median because the left side owns the extra element.

For an even total, the smallest upper-half value is `min(Aright, Bright)`, and the median is the average of those two boundary values.

For `A = [1, 2]` and `B = [3, 4]`, the valid cuts are $i = 2$ and $j = 0$. The boundaries are `2`, positive infinity, negative infinity, and `3`. The central values are therefore `2` and `3`, giving `2.5`.

**Why the partition proof is sufficient**

The size equation guarantees the correct number of elements on each side. Within each array, sorted order already places left elements before right elements. The two cross comparisons add the only missing relationships between arrays. Therefore every left-side element is at most every right-side element, so the cut lies exactly at the combined median rank.

## Complexity detail
Binary search considers $m + 1$ cuts in the shorter array, taking $O(\log(\min(m, n)))$ time. It stores only cut indices and four boundary values, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Fully merge:** is straightforward but costs $O(m + n)$ time and additional output-sized space.
- **Two-pointer selection:** can stop after reaching the middle and use constant space, but still takes linear time.
- **Search the numeric value domain:** complicates duplicate counting and depends on value range; partition search works directly on ranks.
- One input may be empty, duplicate values may straddle the cut, and odd/even totals use different final formulas. Sentinels handle empty partition sides without a separate algorithm.
