## General
**Unequal lengths fail before counting**

Anagrams use every character exactly once, so different lengths cannot match.

**Track the net balance of each lowercase letter**

Use 26 counters. Increment for each character of `s` and decrement for the aligned character of `t`. All counters must finish at zero.

After processing a prefix of both strings, each counter equals that letter's occurrences in the processed part of `s` minus its occurrences in the processed part of `t`.

**A zero balance vector is exactly the anagram condition**

If every final counter is zero, both strings contain each lowercase letter equally often, so one can be rearranged into the other. If any counter is nonzero, that letter occurs a different number of times and no rearrangement can repair the mismatch.

## Complexity detail
The strings are scanned once, giving $O(n)$ time. The 26-entry counter array is fixed-size, giving $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Sorting both strings:** is concise but costs $O(n \log n)$.
- **General hash maps:** support arbitrary characters but use alphabet-dependent space.
- Empty strings are anagrams; equal character sets with different counts are not.
