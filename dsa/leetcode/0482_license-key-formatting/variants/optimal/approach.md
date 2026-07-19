## General
**Normalize the meaningful characters**

Scan the input once, skip every dash, and append the uppercase form of each remaining character. Existing group boundaries have no effect on the new layout.

**Determine the first group from the remainder**

If `length % k` is nonzero, that remainder is the first group length. Otherwise the first group also has length `k`. After it, slice consecutive groups of exactly `k` characters and join all groups with one dash.

**Why this layout is unique**

The normalized character order cannot change. Requiring every group except possibly the first to have size `k` fixes all boundaries when counted backward from the end, and the remainder fixes the only shorter prefix.

## Complexity detail
Normalization and grouping each process `n` characters at most once, giving $O(n)$ time. The cleaned characters, groups, and returned string use $O(n)$ space.

## Alternatives and edge cases
- **Build backward:** scan from right to left, insert a dash after every `k` retained characters, then reverse the result.
- **Repeated string prepending:** is correct but can copy the growing output on every character and take $O(n^2)$ time.
- **All dashes:** produces an empty key without a leading or trailing dash.
- **$k = 1$:** every retained character becomes its own group.
- **Exact multiple of `k`:** the first group has full size rather than zero length.
- **Digits:** remain unchanged while letters are uppercased.
- **Consecutive input dashes:** are all discarded and never create empty groups.
