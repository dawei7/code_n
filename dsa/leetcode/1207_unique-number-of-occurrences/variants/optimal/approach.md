## General
**Count values before comparing counts.** Traverse `arr` once and store each value's frequency in a hash map. At the end, that map contains exactly one integer count for each of the $k$ distinct input values.

**Use a second set for the codomain.** Traverse the frequency values. If a count is already in a set of previously observed counts, two distinct input values share that frequency, so return `false` immediately. Otherwise insert the count and continue. Reaching the end means every frequency was new and the answer is `true`.

This test is exact because the map associates one frequency with every distinct array value, and set insertion detects precisely whether the mapping from values to frequencies is one-to-one. The identities and signs of the input values do not matter after their counts are known.

## Complexity detail
Building the frequency map takes $O(n)$ expected time, and checking its $k$ values takes $O(k)$ expected time. Since $k\le n$, total expected time is $O(n)$. The map and frequency set together store $O(k)$ entries.

## Alternatives and edge cases
- **Sort the array:** Equal values become contiguous and their run lengths can be inserted into a set, but sorting raises the time bound to $O(n\log n)$.
- **Recount each distinct value:** Calling a full-array count for every value takes $O(nk)$ time.
- **Pairwise frequency comparison:** After counting, comparing every pair of the $k$ frequencies takes $O(k^2)$ time instead of using a set.
- **Single distinct value:** Its only frequency is necessarily unique, so the result is `true`.
- **All values distinct:** When $n>1$, every value has frequency one, so the result is `false`.
- **Negative and zero values:** Hash keys handle them exactly like positive values.
- **Late collision:** Equal frequencies must be detected even when the corresponding values occur far apart in the array.
