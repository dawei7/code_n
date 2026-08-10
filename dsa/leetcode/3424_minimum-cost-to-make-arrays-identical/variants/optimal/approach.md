## General

**There are only two meaningful strategies: never rearrange or rearrange once.** Changing an element from $a$ to $b$ costs $\lvert a-b\rvert$, because the cheapest operation is to add or subtract exactly their difference.

If the fixed-cost rearrangement is never used, every position in `arr` must be changed into the value at the same position in `brr`. The source computes

`c1 = sum(abs(a - b) for a, b in zip(arr, brr))`.

This is the complete optimal cost under the original positional pairing.

If rearrangement is used, paying `k` once is enough to realize any permutation of `arr`. The operation permits splitting the array into any number of contiguous subarrays. In particular, split it into $n$ one-element subarrays; those singleton blocks can be reordered arbitrarily. Paying the fixed cost more than once offers no additional permutation power, so an optimum never pays it twice.

After deciding to pay `k`, the remaining question is an assignment problem: which original `arr` value should be changed into each `brr` value?

**Sorted pairing minimizes total absolute difference.** Sort both arrays and pair values at equal sorted positions. This minimizes

$$
\sum_i\lvert a_{\pi(i)}-b_i\rvert
$$

over all permutations $\pi$.

The reason is an exchange argument. Suppose $a_1\le a_2$ and $b_1\le b_2$. Pairing them in the same order never costs more than crossing the assignments:

$$
\lvert a_1-b_1\rvert+\lvert a_2-b_2\rvert
\le
\lvert a_1-b_2\rvert+\lvert a_2-b_1\rvert.
$$

Whenever an assignment has two crossed pairs, swapping them does not increase cost. Repeating these uncrossing swaps eventually gives sorted-to-sorted pairing, so that pairing is globally optimal.

The source sorts `arr` and `brr` in place, then computes

`c2 = k + sum(abs(a - b) for a, b in zip(arr, brr))`.

Finally, `min(c1, c2)` chooses whether the fixed rearrangement fee is worthwhile.

For the first example, direct positional changes cost

$$
\lvert-7-7\rvert+\lvert9-(-2)\rvert+\lvert5-(-5)\rvert=35.
$$

Sorted arrays are `[-7,5,9]` and `[-5,-2,7]`. Their adjustment cost is $2+7+2=11$, and adding $k=2$ gives $13$, which wins.

**Why element changes before or after rearrangement do not create a third case.** Any sequence that pays for rearrangement establishes some matching between original elements and target positions. The total element-change cost for that matching is the sum of absolute differences between matched values, regardless of whether individual additions/subtractions occur before or after the permutation. Sorted pairing is the cheapest possible matching, so `c2` covers all strategies that use rearrangement.

Any sequence that never rearranges cannot change which original position maps to which target position, so `c1` covers all strategies without it. These cases are exhaustive, proving that the smaller cost is globally optimal.

**The method mutates both input arrays.** `arr.sort()` and `brr.sort()` reorder the supplied lists in place. The direct cost is deliberately computed first, while original positional order still exists. After the method returns, callers see both arrays sorted. This side effect is allowed by the judge but is important exact-source behavior. A preservation-oriented version would use `sorted(arr)` and `sorted(brr)`.

Negative values and duplicates require no extra rules. Numeric sorting places negatives correctly, absolute differences measure adjustment cost, and equal copies are interchangeable in the assignment proof.

## Complexity detail

Let $n$ be the common array length. Computing `c1` takes $O(n)$ time. Sorting both lists dominates at $O(n\log n)$ time, and computing `c2` takes another $O(n)$. Total time is $O(n\log n)$.

Python's in-place list sort uses temporary working memory that can be $O(n)$ in the worst case, so the manifest's $O(n)$ auxiliary-space bound is safe. The generator expressions for the sums are lazy and use constant additional iterator state. The input lists themselves are reused but mutated.

## Alternatives and edge cases

- **Try every permutation:** There are $n!$ assignments. The sorted exchange property reduces this factorial search to two sorts.
- **Dynamic programming over blocks:** Because singleton splitting permits any permutation for one fixed fee, retaining original block structure is unnecessary.
- **Pay rearrangement multiple times:** One rearrangement already reaches every permutation, so another payment can never reduce the adjustment cost further.
- **Arrays already identical:** `c1` is zero, the smallest possible answer, even if `k` is also zero.
- **Zero rearrangement fee:** The answer is the sorted-pair adjustment cost or the direct cost, whichever is smaller; sorted assignment can never be worse than the direct assignment, so `c2` wins or ties.
- **Very large \(k\):** Direct positional changes may be cheaper even when rearrangement would greatly reduce element adjustments. Taking the minimum handles this.
- **Length one:** Rearrangement cannot change anything. `c2 = k + c1`, so the direct cost is returned.
- **Duplicate values:** Sorting aligns multiplicities naturally; no identity needs to be attached to equal copies.
- **Negative values:** The exchange argument applies on the full ordered number line, and absolute difference remains the operation cost.
- **Input mutation:** Sorting occurs after `c1` is computed. Moving it earlier would destroy the original-position cost and could return an incorrect result.
