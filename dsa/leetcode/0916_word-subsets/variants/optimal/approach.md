## General
**Replace many subset tests with one requirement profile**

For one candidate word, satisfying every word in `words2` means meeting the largest requested multiplicity of each letter. If one requirement contains two `e` characters and another contains three, a universal word needs three `e` characters—not five—because each subset condition is tested against the same candidate independently.

Build a 26-entry array `required`. Count the letters of each word in `words2`, then update each entry with the componentwise maximum. This single profile is equivalent to the entire second array: a candidate satisfies every original word exactly when its count for every letter is at least the corresponding maximum.

**Filter each candidate once**

For every word in `words1`, build its 26-letter frequency profile and compare it with `required`. Append the original word if all 26 counts meet the thresholds. If any count is too small, reject the candidate immediately.

The componentwise construction proves both directions. Every requirement count is bounded by the stored maximum, so meeting the profile satisfies every word in `words2`. Conversely, any universal word must satisfy the particular requirement that supplied each maximum, so it must meet every entry of the profile.

## Complexity detail
The algorithm reads each input character a constant number of times, giving $O(S)$ time. Both frequency profiles contain exactly 26 integers, so auxiliary space is $O(1)$ because the alphabet is fixed. The returned list is output storage and is not included in the auxiliary-space bound.

## Alternatives and edge cases
- **Test every pair of words:** Checking each candidate against every string in `words2` directly is correct but can take quadratic time in the numbers of strings.
- **Merge requirements by summing counts:** Adding multiplicities across `words2` is incorrect; simultaneous subset conditions require the maximum count per letter, not the sum.
- **Repeated requirement words:** Duplicates in `words2` do not change the componentwise maximum.
- **Multiplicity:** Presence alone is insufficient; a candidate with one copy of a letter cannot satisfy a requirement containing two copies.
- **No universal candidates:** Return an empty list when every word in `words1` misses at least one required letter.
- **Unconstrained letters:** A letter absent from all of `words2` has required count zero and never disqualifies a candidate.
