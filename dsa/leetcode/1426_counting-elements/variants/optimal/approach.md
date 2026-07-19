## General
**Separate membership from multiplicity.** Build a set containing every distinct value in `arr`. Then scan the original array, adding one for each occurrence whose successor `value + 1` belongs to the set.

**Why duplicates are counted correctly.** The set answers only whether a successor exists, which matches the condition; it does not consume or pair successor occurrences. Scanning the original array rather than the set preserves multiplicity. Therefore each qualifying position contributes exactly once and every nonqualifying position contributes zero.

## Complexity detail
Building the set and checking all $n$ occurrences take $O(n)$ expected time. The set stores at most $n$ distinct values and uses $O(n)$ space.

## Alternatives and edge cases
- **List membership per element:** Test `value + 1 in arr` directly for every position. It is concise but takes $O(n^2)$ time in the worst case.
- **Frequency map:** Store counts by value and sum the frequency of each key whose successor exists. This also takes $O(n)$ time and space.
- **Duplicates:** Every copy of a qualifying value counts; successor multiplicity is irrelevant.
- **Successor absent:** An element contributes nothing even if smaller or larger unrelated values exist.
- **Largest value:** A value of `1000` cannot qualify under the stated input range because `1001` cannot appear.
- **No distinct successors:** The answer is zero, including arrays of one repeated value.
