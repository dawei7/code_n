## General
**Preserve each word's internal order**

At any moment, the only legal candidates are the first characters of the two remaining suffixes. Once a character is selected, everything following it in that word must remain behind it. The decision can therefore be represented by two indices rather than by modifying either input.

**Compare the complete remaining suffixes**

If the two available characters differ, choosing the larger one clearly gives the merge a larger first differing character. When they are equal, comparing only those characters reveals nothing: the first later position at which the remaining suffixes differ determines which choice creates the larger continuation. Compare `word1[first:]` with `word2[second:]` lexicographically and take the first character from the larger suffix.

This greedy choice is safe because every valid completion begins with one of those two available characters. Selecting from the larger remaining suffix gives a prefix at least as large as selecting from the other suffix; after removing that selected character, the same argument applies to the two new suffixes. Repeating the choice therefore constructs the maximum merge from left to right.

**Append the exhausted remainder**

Once either index reaches the end of its word, there is no longer a choice. Append the untouched suffix of the other word in one operation to finish the merge.

## Complexity detail
There are $S$ character selections. A comparison between two Python string slices can inspect and copy $O(S)$ characters in the worst case, especially for long equal prefixes, so the accepted implementation takes $O(S^2)$ time. The result and temporary suffix slices require $O(S)$ peak space.

## Alternatives and edge cases
- **Dynamic programming over both indices:** Computing the best merge for every pair of suffix positions is correct, but storing or repeatedly constructing full suffix results makes it substantially more expensive than the greedy comparison.
- **Suffix ranks or rolling hashes:** Preprocessing suffix comparisons can improve the asymptotic running time, but requires a more elaborate ranking or longest-common-prefix mechanism.
- **Compare only the leading characters:** This is insufficient when the available characters tie; a later differing character can reverse which word should contribute first.
- **Equal remaining suffixes:** Either source may contribute the next character because both choices lead to the same final text.
- **One word exhausted:** The entire remaining suffix of the other word must be appended without further comparisons.
- **Long repeated prefixes:** Inputs such as many consecutive `a` characters force suffix comparisons to scan deeply and realize the quadratic worst case.
- **Identical input words:** The ordering of choices may vary, but every optimal choice sequence produces their characters in the same merged order.
- **Minimum-length words:** With one character in each input, the larger character is placed first; equal characters can be taken in either order.
