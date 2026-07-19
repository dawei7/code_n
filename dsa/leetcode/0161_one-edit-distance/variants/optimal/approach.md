## General
The important phrase is **exactly one edit**. Equal strings must be rejected, and a length difference greater than one is immediately impossible because a single insertion or deletion changes the length by only one.

Assume `s` is no longer than `t`; swapping the names does not change the question. Walk from the beginning until the first position `i` where the characters differ. Everything before `i` already agrees, so any valid transformation must spend its one edit at that first mismatch.

What happens next is forced by the lengths:

- If the strings have equal length, the only possible edit is a replacement. Skip `s[i]` and `t[i]`, then require the remaining suffixes to be identical.
- If `t` is one character longer, the only possible edit is inserting `t[i]` into `s` (equivalently, deleting it from `t`). Skip only `t[i]`, then require `s[i:]` to equal `t[i + 1:]`.

There is one subtle case: the scan may reach the end of the shorter string without finding a mismatch. Then the transformation is valid only if the longer string has exactly one trailing character. Thus `"ab"` and `"abc"` are one edit apart, while `"ab"` and `"ab"` are zero edits apart.

For example, compare `"cab"` with `"crab"`. The common prefix is `"c"`; the first mismatch is `a` versus `r`, and the second string is longer. Ignoring only `r` aligns the remaining suffixes `"ab"` and `"ab"`, so one insertion suffices. By contrast, `"cab"` and `"crop"` still disagree after that skip, proving that a second edit would be needed.

Before the first mismatch, the prefixes are identical and therefore require no edit. At the mismatch, the length relationship uniquely determines the only edit type that can restore alignment: replacement for equal lengths, or insertion/deletion for a one-character length difference. If the suffixes match after that forced skip, exactly one edit transforms one string into the other. If they do not match, another edit would be necessary. If no mismatch occurs, exactly one unmatched trailing character is both necessary and sufficient. These cases cover every possible location and type of a single edit.

## Complexity detail
Finding the first mismatch and comparing the remaining suffixes examines at most $O(m + n)$ characters. An index-based implementation uses $O(1)$ auxiliary space; languages where slicing copies strings should compare by index rather than materializing suffixes to preserve that bound.

## Alternatives and edge cases
- Full edit-distance dynamic programming is unnecessary here: it solves arbitrary edit distance in $O(mn)$ time instead of exploiting the distance-one limit.
- Generating all strings reachable by one edit creates avoidable temporary strings and may require iterating over an alphabet.
- `""` and `""` are zero edits apart and return `False`; `""` and `"x"` return `True`.
- Character comparison is case-sensitive, so `"a"` and `"A"` differ by one replacement.
- Swapping the inputs when the first is longer lets one insertion case represent deletion symmetrically.
