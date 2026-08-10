## General

**Convert the signed problem into a nonnegative one**

The smallest subset sum is obtained by including every negative original element and no positive element. Let that minimum be `min(sums)` and define

`m = -min(sums)`.

Thus $m$ is the sum of the absolute values of the original negative elements.

The source adds $m$ to every supplied subset sum and stores the shifted multiset in a `SortedList`. This shifted collection is exactly the subset-sum multiset of the unknown elements' absolute values.

To see why, consider an original negative value $-x$. In a supplied subset, including it contributes $-x$; after adding the total $m$, that contribution is canceled, while excluding it leaves the corresponding $+x$ inside the shift. This complements the inclusion choice for every negative element. Positive elements keep their ordinary inclusion choice. Across all subsets, the shifted sums therefore enumerate all subsets of the nonnegative magnitudes.

**Why a sorted multiset is required**

Subset sums can repeat, especially when elements are equal or zero. A plain set would lose multiplicities and make later removals incorrect. `SortedList` retains duplicates, supports finding the smallest remaining value at index zero, and removes one occurrence at a time.

The shifted multiset contains zero for the empty magnitude subset. The source removes exactly one zero before recovery begins.

**Recover magnitudes from smallest remaining sums**

After empty zero is removed, the smallest remaining subset sum must be the smallest element magnitude, so the source begins `ans = [sl[0]]`.

The recovery invariant is: before selecting the next element, remove all nonempty subset sums that can be formed entirely from magnitudes already recovered. Once those known sums are removed, the smallest remaining value must be the next smallest unrecovered magnitude. Its singleton subset exists, and every subset containing an unrecovered magnitude is at least as large because all magnitudes are nonnegative.

The loop implements removals by highest included index. At stage `i`, the newest known magnitude has index `i - 1`. It enumerates all masks over the first `i` known values but processes only masks whose bit `i - 1` is set. Those are exactly the known-element subsets containing the newest value. Subsets not containing it were removed in earlier stages.

For each such mask, it recomputes the subset sum and removes one matching occurrence from `sl`. After all these removals, `sl[0]` is appended as the next magnitude.

This scheme handles duplicates correctly because removal is by multiset occurrence, not unique numeric value.

**Understand zero-valued elements**

If the unknown array contains zero, the shifted multiset contains multiple zeroes. Removing the empty-subset zero leaves another zero as `sl[0]`, so zero is recovered as an element. Later subset removals consume the correct additional zero occurrences. No special zero branch is needed.

**Restore which magnitudes were negative**

The first phase recovers only absolute values. The shift amount $m$ tells how to restore signs: the magnitudes that were originally negative must sum to $m$.

The final loop enumerates every subset mask of the recovered `ans` and computes its sum. When it finds a subset totaling `m`, it multiplies exactly those selected magnitudes by negative one and stops.

Such a subset is guaranteed to exist because the original negative magnitudes themselves have total $m$. Multiple sign assignments may work, and the contract permits any valid recovered array.

**Why the restored array has the supplied sums**

Before sign restoration, `ans` has exactly the shifted subset-sum multiset. Choose a magnitude subset totaling $m$ and negate those elements. For each subset of the signed result, complement inclusion of every negated element. This creates a one-to-one correspondence with a magnitude subset whose sum is the signed subset sum plus $m$.

Therefore, subtracting the common shift $m$ from the recovered magnitude sums produces precisely the original `sums` multiset. The returned signed array is valid.

**A small signed example**

For original values `[1, -3]`, subset sums are `[-3, -2, 0, 1]`. The minimum is -3, so $m=3$. Shifting gives `[0, 1, 3, 4]`, the subset sums of magnitudes `[1, 3]`.

Recovery finds one and three. The sign search finds the subset `{3}` totaling $m$, negates it, and returns `[1, -3]`.

## Complexity detail

Let $N$ be the unknown array length and $Q=2^N$ the number of supplied sums. Sorting the initial values costs $O(Q\log Q)=O(N2^N)$. The recovery and sign-search loops enumerate $O(2^N)$ masks and compute each selected sum in up to $O(N)$ time. `SortedList.remove` also costs logarithmic time, $O(\log Q)=O(N)$.

Total time is $O(N2^N)$ and space is $O(2^N)$ for the multiset, input-derived values, and recovered array. The implementation trades repeated subset-sum computation for simple code.

## Alternatives and edge cases

- **Recursive partition by a candidate magnitude:** Split sorted sums into pairs differing by that magnitude and recurse on the half containing zero; this is another standard $O(N2^N)$ strategy.
- **Plain set:** Incorrect because repeated subset sums carry essential multiplicity.
- **Recover signs during magnitude extraction:** Possible, but the shift cleanly separates magnitude recovery from one final subset-sum sign choice.
- **All elements nonnegative:** The minimum sum is zero, $m=0$, and the empty sign subset succeeds without negating anything.
- **All elements negative:** Their magnitudes sum to $m$, so the sign search can negate the full recovered array.
- **Zero elements:** Repeated zero sums allow zero magnitudes to be recovered correctly.
- **Duplicate magnitudes:** `SortedList` removes one occurrence at a time, preserving multiplicity.
- **Several valid arrays:** Any recovered order and any sign subset totaling $m$ is accepted.
- **Guaranteed solvability:** Every requested removal and the final sign subset exist for valid generated input.
- **Exponential input size:** $O(2^N)$ space is unavoidable merely to receive all supplied sums.
- **Imported data structure:** The exact source assumes `SortedList` is provided by the execution environment.
- **Input preservation:** It creates shifted values rather than sorting or changing `sums` itself.
