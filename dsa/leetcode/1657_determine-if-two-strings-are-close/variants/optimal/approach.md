## General
**Identify what operations cannot change.** Arbitrary position swaps preserve every character count. A global exchange swaps the counts attached to two existing character labels. Therefore both operations preserve the set of characters that occur and the multiset of their positive frequencies. Different lengths, different character support, or different frequency multisets make transformation impossible.

**Count both fixed alphabets.** Build a frequency map for each word. Compare their key sets to verify that no character would need to be introduced or removed. Then sort the two collections of positive counts and compare them. Sorting at most 26 counts is constant work relative to the input length.

**Why the invariants are sufficient.** When support sets match and the frequency multisets match, pair each target character with a source character having its required count. Global exchanges can permute the count assignments among the existing labels to realize that pairing. Once every label has the target count, arbitrary position swaps can arrange the characters into `word2`. Thus the two comparisons exactly characterize closeness.

## Complexity detail
Counting scans all $N$ characters once. Key and frequency comparisons involve at most 26 lowercase letters, so they add constant work. Total time is $O(N)$ and the fixed-size counters use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Fixed arrays:** Two arrays of 26 counts avoid hash maps and test positive positions plus sorted count arrays directly, with the same $O(N)$ time and $O(1)$ space.
- **Sort every character:** Full string sorting can derive frequency runs but costs $O(N\log N)$ and still needs separate support and run-length comparisons.
- **Compare only sorted frequencies:** This wrongly accepts strings such as `aabb` and `ccdd`, because global exchanges may use only characters already present.
- **Compare only character sets:** Matching support does not help when the occurrence-count multisets differ.
- Strings of different lengths are never close because both operations preserve length.
- Two permutations of the same multiset are close using only position swaps.
- A one-character string is close only to the same one-character string.
- Repeated global exchanges may permute frequencies arbitrarily among present characters, but cannot introduce a missing letter.
- Equal frequency values are interchangeable and require no special matching order.
