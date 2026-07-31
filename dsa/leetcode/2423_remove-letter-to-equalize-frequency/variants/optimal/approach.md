## General

**Positions with the same letter are equivalent.** Removing any occurrence of a particular character changes only that character's frequency, so there is no need to try every index. Count the letters once, then consider each distinct character as the removed letter type.

For one candidate, decrement its count by one. Ignore any resulting zero because a letter absent from the new string is not required to match the others. Collect the remaining positive frequencies: the candidate succeeds exactly when there is at most one distinct value. Restore the decremented count before testing the next character.

This examines every possible effect of deleting one character. If a successful character type exists, deleting any one of its occurrences produces equal positive frequencies. If every type leaves at least two different positive frequencies, no index can work.

## Complexity detail

Building the frequency table takes $O(n)$ time. At most 26 character types are tested, and each test scans at most 26 counts, which is constant work for the fixed lowercase English alphabet. The total time is therefore $O(n)$. The frequency table and temporary frequency set contain at most 26 entries, so the auxiliary space is $O(1)$ under the fixed-alphabet contract.

## Alternatives and edge cases

- **Remove every index and recount:** This directly tests the definition but rebuilds frequencies up to $n$ times and costs $O(n^2)$ time.
- **Classify frequency-of-frequency patterns:** The valid configurations can be characterized algebraically, but the case analysis is easier to get wrong than testing the 26 possible letter types.
- **Exactly one deletion:** A word whose current frequencies are equal may still return `false` if every mandatory deletion makes them unequal.
- **Delete a unique letter:** A frequency-one character may disappear entirely, leaving the other positive frequencies equal.
- **One distinct letter:** Removing any occurrence leaves at most one positive frequency, so the result is `true`.
- **Two-character word:** Deleting either character leaves one letter, which always has uniform frequency.
- **Zero counts:** Characters removed completely must be excluded from the equality comparison.
