## General

Let $n$ be the array length and $d$ the maximum decimal digit count.

**Put leading-zero reductions in the searchable direction**

Sort the values numerically. A digit swap that retains the digit count is reversible. The only asymmetric case is a leading-zero result, which has fewer digits and a smaller numeric value. Therefore, if an almost-equal pair needs a swap in only one direction, the later, larger value in sorted order can always be swapped to the earlier, smaller one.

**Enumerate one-swap results once per value**

Process the sorted values from smallest to largest while maintaining frequencies of exact earlier values. For the current value, place the unchanged value in a set, then swap every pair of digit positions, convert the resulting sequence back to an integer, and add it to the set. Using a set matters when equal digits or different swaps produce the same integer.

For every distinct reachable integer, add its earlier frequency to the answer. Then increment the frequency of the current original value.

Every counted earlier value matches the current value after at most one current-digit swap, so each contribution is valid. Conversely, sorting guarantees that any almost-equal pair is discoverable from its later member: same-length swaps can be inverted, while a leading-zero collapse necessarily points from the larger representation to the smaller integer. Processing one later element at a time also counts each index pair exactly once.

## Complexity detail

Sorting costs $O(n \log n)$. Each value enumerates $O(d^2)$ position pairs, and joining and converting a swapped digit list costs $O(d)$, for $O(n \log n + n d^3)$ time in an explicit digit-cost model. The contract fixes $d \le 7$, so this reduces to $O(n \log n)$ with respect to $n$. The frequency map can store $O(n)$ values and the reachable set $O(d^2)$ candidates, for $O(n + d^2)$ space.

## Alternatives and edge cases

- **Check every index pair:** Generating swaps separately for all $O(n^2)$ pairs is correct but repeats the same digit work many times.
- **Compare sorted digits only:** Anagrams may require several swaps, so matching digit multisets is too permissive; `123` and `231` are not almost equal.
- **Require equal digit lengths:** This misses legal leading-zero reductions such as `30` becoming `3`.
- **Count generated values without deduplication:** Equal digits and repeated outcomes can count one earlier index more than once.
- Identical values qualify without performing an operation.
- Swapping equal digits leaves the value unchanged and adds no new reachable result.
- The value `1000000` has seven digits and remains within the bounded enumeration.
- Duplicate array values represent different indices and contribute all corresponding combinations.
- Only one of the two integers may receive one swap; applying one swap to each is not allowed.
