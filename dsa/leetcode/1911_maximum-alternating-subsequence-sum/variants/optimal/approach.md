## General

**The sign of the next chosen value depends on chosen length.** In a reindexed subsequence, positions zero, two, four, and so on are added; positions one, three, five are subtracted. After choosing an even number of elements, the next chosen number receives a plus sign. After choosing an odd number, the next receives a minus sign. Dynamic programming needs only this parity, not the complete subsequence.

**Define the two prefix states.** `f[i]` is the best alternating sum obtainable from the first `i` input values using an even number of selected elements. `g[i]` is the best using an odd number. The empty subsequence has even length and sum zero. The source initializes both arrays to zero; treating `g[0]` as zero is a permissive baseline, but positive input values ensure it never creates a result better than a genuine odd selection in a harmful way.

**Process one value without using it twice.** For current `x = nums[i - 1]`, an even-length result has two possibilities. Skip `x` and keep `f[i - 1]`, or append `x` with a minus sign to an odd-length subsequence, giving `g[i - 1] - x`. Therefore:

`f[i] = max(g[i - 1] - x, f[i - 1])`.

An odd-length result similarly either skips `x` and keeps `g[i - 1]`, or appends `x` with a plus sign to an even-length subsequence:

`g[i] = max(f[i - 1] + x, g[i - 1])`.

Both transitions read only row `i - 1`. This is important: using a freshly updated state from the same iteration could select `x` twice, once with each sign.

**Why skipping is included.** A subsequence may omit any input value while preserving order. Carrying the previous state forward represents every solution that does not use `x`. The append transition represents every solution that does. Taking the maximum covers the complete choice.

**Trace `[4,2,5,3]`.** Processing four gives odd state four. Processing two can create even state `4 - 2 = 2`. Processing five extends that even state to odd sum `2 + 5 = 7`, representing subsequence `[4,2,5]`. Later value three cannot improve the best odd result, so the answer stays seven.

**Why array order is preserved.** Values are considered left to right, and an append transition always extends a state built only from earlier positions. No transition can reorder elements or go back to a future value. Thus every represented selection is a valid subsequence.

**Why the state meaning is exact.** Initially the even empty state is exact. Assume prefix states contain the best sums for their parity. Every parity-specific subsequence over the next prefix either omits `x` or uses it last. Those two cases are precisely the carry and opposite-parity append transitions. Induction proves both arrays remain optimal.

**Return either parity.** The source returns `max(f[n], g[n])`. With all values positive, an optimal nonempty alternating subsequence normally has odd length because dropping a final subtracted positive value cannot reduce the sum. Returning both remains correct and directly follows the state definition.

**Input remains unchanged.** The method only reads `nums` and allocates DP arrays. It does not reconstruct which subsequence achieved the sum because only the numeric optimum is requested.

## Complexity detail

Let $n$ be the number of values. Each iteration performs constant work, so time is $O(n)$, matching the manifest.

The exact source allocates two arrays of length $n+1$, making auxiliary space $O(n)$. This differs from the manifest's $O(1)$ space label. Because each row depends only on the preceding pair of states, two scalar variables can compress the recurrence to constant space, but that optimization is not present.

The maximum result can scale with the sum of input values, up to about $10^{10}$ under the constraints. Python integers are safe; fixed-width languages need 64-bit arithmetic.

## Alternatives and edge cases

- **Two scalar states:** Retain only previous even and odd best values and update them from saved old values. This achieves the manifest's $O(1)$ space.
- **Greedy valley/peak interpretation:** For positive values, accumulate gains across rising segments or choose alternating local extrema. It can be linear but is less directly general than the parity DP.
- **Enumerate subsequences:** There are $2^n$ choices, far beyond the limit. DP collapses histories sharing prefix and parity.
- **Single element:** Odd state becomes that value, which is the maximum subsequence sum.
- **Strictly increasing input:** Choosing only the final largest value is optimal, and carry transitions preserve it.
- **Equal neighboring values:** Selecting both would add then subtract the same amount with no benefit; DP can skip either.
- **Empty subsequence baseline:** Arrays begin at zero, but positive values ensure the returned optimum uses at least one element.
- **No reconstruction:** If selected indices were required, predecessor decisions would need storage. The numeric problem does not.
- **Manifest space mismatch:** The recurrence is compressible, but the checked-in arrays consume linear memory and must be documented as such.
