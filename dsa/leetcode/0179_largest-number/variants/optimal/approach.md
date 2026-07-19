## General
The choice between two numbers depends on how they interact after concatenation, not on their individual numeric sizes. Convert every number to a decimal string. For strings `a` and `b`, prefer `a` before `b` exactly when `a + b` is lexicographically greater than `b + a`.

Both candidate concatenations have the same length, so lexicographic comparison agrees with their numeric comparison. For `a = "3"` and `b = "30"`, `"330" > "303"`, so `3` belongs before `30`. For `"12"` and `"121"`, `"12121" > "12112"`, showing why ordinary numeric or prefix ordering is insufficient.

Sort all strings under this pairwise rule, then concatenate them. The greedy justification is an exchange argument: if an arrangement contains adjacent strings in the opposite order, replacing `b + a` with the larger `a + b` improves the complete result while leaving its surrounding prefix and suffix unchanged. A maximum arrangement therefore cannot contain such an inversion, and sorting removes all inversions.

The comparator is a valid ordering for these strings. One way to view it is to compare the infinite periodic forms `aaaa...` and `bbbb...`; comparing `a + b` with `b + a` determines the same relative order, making the relation transitive enough for sorting.

Finally, if the first sorted string is `"0"`, every input value is zero. Return the normalized result `"0"` rather than a representation such as `"000"`.

Consider any two adjacent strings `a` and `b`. If `b + a` is larger than `a + b`, swapping them strictly increases the full concatenation because the unchanged prefix has already tied and both alternatives have equal length. Therefore no globally maximal ordering contains a comparator inversion. The custom sort produces an inversion-free ordering; repeated exchanges transform any other ordering into it without decreasing the result. Its concatenation is thus globally maximal. The final zero normalization changes only redundant leading zeroes, not the represented value.

## Complexity detail
Sorting performs $O(n \log n)$ comparisons. If strings have at most `k` digits, forming or comparing the two concatenation orders costs $O(k)$, for $O(nk \log n)$ time. The converted strings, sorting storage, and result occupy $O(nk)$ space.

## Alternatives and edge cases
- Sorting by integer value fails for `[10, 2]`, where the smaller value must come first in the result.
- Lexicographically sorting individual strings fails on prefix relationships such as `"3"` and `"30"`.
- Padding to a fixed width can misorder repeated-prefix values unless it effectively reproduces the concatenation comparator.
- Enumerating all permutations is factorial.
- Equal comparator pairs may appear in either order without changing the final string.
- Multiple zeroes must collapse to one output zero; mixed zero and nonzero inputs sort naturally without stripping meaningful trailing zeroes.
