## General

**First construct the exact target permutation.** Wonderful integers are the digit permutations larger than `num` in increasing numeric order. Because every candidate has the same length, this order is lexicographic order on the digit strings. Applying the standard next-permutation operation once produces the smallest larger distinct permutation; applying it `k` times produces the `k`-th smallest wonderful integer.

The code converts `num` to mutable list `s` and repeats `next_permutation(s)` exactly `k` times. The tests guarantee that the target exists, so the helper’s Boolean result does not need to be checked.

**How next permutation works.** It finds the rightmost index `i` with `nums[i] < nums[i + 1]`. The suffix after `i` is nonincreasing. If no pivot exists, the arrangement is maximal, though the input guarantee prevents this before all `k` requested steps.

It then finds the rightmost suffix digit strictly greater than the pivot, swaps them, and reverses the suffix into nondecreasing order. This preserves the longest possible prefix, increases the pivot minimally, and makes the remainder minimal, yielding the immediate next distinct arrangement even with duplicate digits.

**Map target occurrences back to original positions.** Once `s` is the target, the remaining question is the minimum number of adjacent swaps to transform `num` into `s`.

`d` is an array of ten lists. For every original character, the code appends its index to the list for that digit. These index lists are increasing. `idx` records how many original occurrences of each digit have already been assigned.

Scanning target `s` from left to right, each target digit is matched to the earliest unused original occurrence of the same digit. Its original index is stored in `arr`. Equal digits are interchangeable, and matching them in stable order is optimal: crossing two equal occurrences would add swaps without changing the visible target string.

For example, if the target order draws characters from original indices `[0, 2, 1]`, then the last two original characters must reverse their relative order.

**Adjacent swaps equal inversion count.** `arr` lists original positions in the order those characters must appear in the target. A pair of target positions `j < i` is inverted when `arr[j] > arr[i]`: the character that must appear earlier currently lies to the right. Those two characters must cross at least once.

One adjacent swap changes the relative order of exactly one neighboring inverted pair. Standard bubble-style movement can realize the target using exactly one swap per inversion. Therefore the minimum adjacent-swap count is the inversion count of `arr`.

The exact return expression examines every pair with `j < i` and sums the Boolean condition `arr[j] > arr[i]`. Python treats true as one and false as zero.

**Trace the conceptual stages.** For `"00123"` and `k = 1`, next permutation produces `"00132"`. Stable occurrence mapping assigns both zeros and the one to their same early positions, while the final three and two map in reversed original order. `arr` has one inversion, so one adjacent swap is necessary and sufficient.

**Why stable duplicate matching is necessary.** If two identical digits occur at original positions one and five and target positions require two copies, assigning the later original copy first would create a crossing with the earlier copy for no observable benefit. Earliest-unused assignment avoids all inversions among equal digits and minimizes the remaining crossing count.
Repeated next permutation constructs exactly the required wonderful number. Stable occurrence mapping turns transformation into a permutation of distinct original positions without adding unnecessary equal-digit crossings. The inversion theorem then gives exactly the minimum number of adjacent swaps. All three stages preserve the digit multiset.

## Complexity detail

Let `n = len(num)`. One next-permutation step takes `O(n)` time, including suffix reversal, so `k` repetitions take `O(kn)`.

Building digit-position lists and `arr` takes `O(n)`. The exact inversion count uses two nested loops over all index pairs and therefore takes `O(n^2)` time. Total exact running time is `O(kn + n^2)`.

This differs from the manifest’s `O(kn + n log n)` claim, which would require a Fenwick tree, merge-sort inversion counter, or similar structure absent from the checked-in source. Lists `s`, `d`, `idx`, and `arr` use `O(n)` total space; permutation reversal slices can also allocate `O(n)` temporary space.

## Alternatives and edge cases

- **Fenwick-tree inversion count:** Process mapped indices and count earlier greater positions in `O(n log n)`, matching the manifest’s faster bound.
- **Merge-sort inversion count:** Also reduces the counting phase to `O(n log n)` with `O(n)` auxiliary space.
- **Simulate adjacent swaps directly:** Repeatedly locate each target digit and bubble it left; this is intuitive and `O(n^2)`.
- **Duplicate digits:** Stable earliest-unused mapping prevents artificial crossings among indistinguishable copies.
- **Leading zeros:** Fixed-length lexicographic order still matches numeric order among these permutations.
- **Guaranteed target existence:** The exact loop ignores the helper’s false result because tests promise `k` successors.
- **`k = 1`:** Only one next-permutation transformation is needed before counting swaps.
- **Already nearby target:** The inversion count can be one or another small number even when target generation scans the whole string.
- **No inversions:** This would mean target order matches original order, which cannot occur for a strictly larger distinct target, but the formula would correctly return zero generally.
- **Quadratic exact count:** At `n = 1000`, pair enumeration is finite but is not the advertised `n log n` method.
- **Input preservation:** `num` remains immutable; mutations occur on list `s`.
- **Boolean summation:** Each true inverted pair contributes integer one to the returned total.
