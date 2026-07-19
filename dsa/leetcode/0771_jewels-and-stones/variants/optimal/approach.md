## General
**Build a membership set once**

Insert all `j` jewel characters into a set. Then scan the `s` stone characters and increment the answer whenever the current character belongs to that set.

The set contains exactly the symbols classified as jewels. Each position in `stones` is tested once and contributes one precisely when its symbol is in that classification, so repeated occurrences are counted independently and non-jewels never contribute.

## Complexity detail
Building the set takes $O(j)$ time and scanning the stones takes $O(s)$ expected time, for $O(j + s)$ total. The set stores at most `j` symbols, using $O(j)$ space; with the fixed letter alphabet this is also bounded by a constant.

## Alternatives and edge cases
- **Boolean lookup table:** Mark letter codes in a fixed-size array for the same $O(j + s)$ time and constant bounded space.
- **Search the jewel string for every stone:** This avoids a separate set but takes $O(js)$ time in the worst case.
- **Frequency counter for stones:** Summing counts for jewel symbols is correct, but stores more information than direct membership counting needs.
- **Case sensitivity:** `a` and `A` must remain separate symbols.
- **Repeated stones:** Every matching occurrence increments the result.
- **No matching stones:** Return zero.
- **Every stone is a jewel:** Return `len(stones)`.
