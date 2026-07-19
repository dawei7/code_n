## General
**Pair opposite extremes**

Sort the values of `nums1` in ascending order and the values of `nums2` in descending order. Multiply corresponding positions and sum them. Sorting `nums2` is an analytical reordering of the pairs: the resulting multiset matching can always be realized by permuting `nums1` into the corresponding original `nums2` positions.

**Why aligned ordering cannot be better**

Suppose two first-array values satisfy $a \le b$ and their paired second-array values satisfy $c \le d$. Pairing them in the same order contributes $ac+bd$. Swapping the first-array assignments contributes $ad+bc$, and

$$
(ac+bd)-(ad+bc)=(b-a)(d-c)\ge 0.
$$

Thus pairing the larger first value with the smaller second value never increases the sum.

**Remove every inversion**

Any matching that is not oppositely ordered contains a same-order pair of the form above. Swapping it does not increase the product sum. Repeating this exchange removes all such inversions and reaches the opposite-order pairing, proving that the constructed sum is globally minimal. Equal values simply make some exchanges neutral.

## Complexity detail
Sorting both length-$N$ arrays takes $O(N\log N)$ time, and the final paired scan takes $O(N)$. Python's sorting implementation may use $O(N)$ auxiliary workspace in the worst case, so the overall space bound is $O(N)$. The returned result itself is one integer.

## Alternatives and edge cases
- **Frequency counting:** Because values lie from `1` through `100`, two frequency arrays and opposing pointers can achieve $O(N+100)$ time and $O(100)$ space.
- **Enumerate permutations:** It checks every possible arrangement but requires factorial time.
- **Quadratic selection sort:** It produces the same optimal ordering but costs $O(N^2)$ time.
- **Duplicate values:** Preserve their multiplicities; their internal order is irrelevant.
- **All values equal:** Every rearrangement has the same product sum.
- **Single element:** Return its sole product.
- **Rearranging `nums2` in the implementation:** Only the induced matching matters, and the same matching is realizable by rearranging `nums1` alone.
