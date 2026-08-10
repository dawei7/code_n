## General

**The freedom is a pairing problem.** The product sum is determined by which value from `nums1` is paired with each value from `nums2`. Rearranging `nums1` changes those pairings but does not change either multiset of values. To minimize a sum of products of positive numbers, expensive large multipliers should be paired with the smallest available factors, while small multipliers can absorb the largest factors. The source creates exactly that opposition: `nums1.sort()` places its values in nondecreasing order, and `nums2.sort(reverse=True)` places its values in nonincreasing order. Equal indices then pair the smallest first-array value with the largest second-array value, the next smallest with the next largest, and so on.

**Why sorting both arrays is allowed.** The statement explicitly permits rearranging `nums1`, but the code also sorts `nums2`. Sorting `nums2` does not grant extra mathematical freedom. The product sum is a sum over pairs, and simultaneously reordering the list of pairs does not change that sum. One can imagine first deciding which `nums1` value belongs with each `nums2` value, then listing those pairs in any convenient order. Sorting `nums2` merely chooses the convenient order “largest multiplier first”; placing `nums1` in the opposite order describes the corresponding legal rearrangement. If the original positions of `nums2` had to be retained, the same pairing could be implemented by sorting indexed values and mapping the selected `nums1` elements back to those positions.

**Use a local exchange to prove the arrangement.** Suppose two `nums1` values satisfy $a\le b$ and two `nums2` values satisfy $x\le y$. Compare pairing values in the same order with pairing them in opposite order. The same-order contribution is $ax+by$, while the opposite-order contribution is $ay+bx$. Their difference is

$$
(ax+by)-(ay+bx)=(b-a)(y-x)\ge 0.
$$

Therefore $ay+bx\le ax+by$: assigning the smaller `nums1` value to the larger `nums2` value never increases the product sum. Whenever a proposed arrangement has two pairs ordered in the same direction, swapping their `nums1` assignments is at least as good. Repeating such exchanges removes every same-direction inversion and eventually leaves the arrays oppositely sorted. Because no exchange increases the sum, that final arrangement is globally minimal.

**Duplicates fit the proof naturally.** If `a == b` or `x == y`, the exchange difference is zero. Multiple orderings can therefore attain the same minimum when either array contains duplicates. The algorithm does not need to identify a unique permutation; it needs only the minimum numeric sum. Python's sort may preserve relative order among equal values, but that stability has no effect on any product.

**Compute the paired sum without another data structure.** After sorting, `zip(nums1, nums2)` yields pairs at equal indices. The generator expression `x * y for x, y in zip(nums1, nums2)` produces one product at a time, and `sum(...)` accumulates them. Because the arrays are guaranteed to have equal length, `zip` covers all `n` elements; its usual behavior of stopping at the shorter iterable cannot discard anything under the contract. No array of products is built.

**Trace the first example.** Sorting `nums1 = [5, 3, 4, 2]` produces `[2, 3, 4, 5]`. Sorting `nums2 = [4, 2, 2, 5]` in reverse produces `[5, 4, 2, 2]`. The equal-index pairs are `(2, 5)`, `(3, 4)`, `(4, 2)`, and `(5, 2)`. Their contributions are `10`, `12`, `8`, and `10`, totaling `40`. The arrangement shown in the problem lists the pairs in a different position order, but it represents the same essential pairing multiset: the largest values are matched against the smallest possible partners.

**Why this covers the permitted search space.** Every rearrangement of `nums1` corresponds to a perfect pairing between the values of the two arrays. If a pairing is not oppositely ordered, it contains a pair of same-direction assignments that the exchange calculation can swap without worsening the result. Applying the argument until no such pair remains yields precisely an opposite-order pairing. Thus some optimal solution always has the form constructed by the two sorts. The final generator computes its product sum exactly, so the returned number is the minimum over all legal rearrangements rather than merely a locally good choice.

**Input mutation is part of the exact source behavior.** Both calls to `.sort()` operate in place. The method returns only an integer, but after it returns, `nums1` is ascending and `nums2` is descending. The statement does not require preserving input order, so this is valid for the challenge. A caller that needs the original lists later would have to pass copies or use `sorted(...)`; the current source deliberately avoids allocating two separate sorted arrays at the Python level.

## Complexity detail

Let $n$ be the common array length. Sorting `nums1` costs $O(n\log n)$ time, and sorting `nums2` costs another $O(n\log n)$. Zipping, multiplying, and summing visits all $n$ pairs once for $O(n)$ additional time. The total is therefore $O(n\log n)$, matching the manifest.

The generator used by `sum` needs only constant incremental state; it does not materialize the products. Python's in-place list sort, Timsort, can use up to $O(n)$ temporary auxiliary memory in the worst case, as well as a logarithmic amount of control-stack information. Thus the exact implementation has $O(n)$ worst-case auxiliary space, consistent with the manifest. The mutations reuse the input list storage but do not make the sorting workspace provably constant.

Each input value is at most `100`, and there are at most $10^5$ pairs, so the result is at most $10^9$. This fits in a signed 32-bit integer at the stated bounds, and Python integers are safe regardless. Comparisons and multiplications are constant-time for these bounded values.

Because the value range is only `1` through `100`, an alternative counting implementation can improve the theoretical time to $O(n+K)$ for $K=100$. The checked-in source nevertheless uses comparison sorting, so $O(n\log n)$ is the accurate time bound for this exact implementation even though the problem admits a linear-time bounded-domain solution.

## Alternatives and edge cases

- **Counting frequencies:** Count each value from `1` through `100` in both arrays, then consume the first array upward and the second downward. This achieves $O(n+K)$ time and $O(K)$ space, where $K=100$, but requires more careful pointer and multiplicity bookkeeping than the concise sorting solution.
- **Sort only indexed `nums2` values:** If `nums2` must remain physically unchanged, sort `(value, index)` pairs, assign ascending `nums1` values to descending `nums2` values, and optionally reconstruct a rearranged first array. That adds storage while representing the same proof.
- **Priority queues:** Repeatedly extracting the smallest value from one heap and largest from another also creates opposite pairings, but costs $O(n\log n)$ time with more data-structure overhead and no advantage over sorting all values once.
- **Sorting both arrays in the same direction:** This maximizes rather than minimizes the product sum for nonnegative values. The exchange inequality shows exactly why like-sized values together make the sum no smaller.
- **Single-element arrays:** Both sorts are trivial, `zip` produces one pair, and the only possible product is returned. There is no rearrangement choice to make.
- **Duplicate values:** Equal elements can lead to many optimal permutations. Their relative order is irrelevant, and the exchange proof permits equality without requiring strict inequalities.
- **Input mutation:** The exact method changes both caller-provided lists. Use copies when order preservation is an external requirement; silently claiming this implementation is non-mutating would be inaccurate.
- **Negative-number generalization:** The stated inputs are positive. Opposite sorting is in fact supported by the general rearrangement inequality for real numbers too, but reasoning based only on “large products are expensive” should not be extended casually when signs change; the exchange proof is the reliable justification.
