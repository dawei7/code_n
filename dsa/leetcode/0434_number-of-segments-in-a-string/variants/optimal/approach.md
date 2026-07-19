## General
**Count transitions into non-space text**

A segment begins exactly where the current character is not a space and either it is at index zero or the previous character is a space. Count positions satisfying that condition during one left-to-right scan.

**Why one transition represents one whole segment**

Every maximal non-space run has one first character, and that character satisfies the start condition. No later character in the same run satisfies it because its predecessor is non-space. Conversely, every counted position begins a nonempty run that continues until a space or the string end, so the count is neither missing nor duplicating segments.

## Complexity detail
The scan performs constant work for each of `n` characters, giving $O(n)$ time. A single integer counter uses $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Built-in split:** splitting on spaces and discarding empty pieces is concise but materializes $O(n)$ additional text.
- **Explicit in-segment flag:** track whether the previous position belongs to a segment; this is equivalent to checking the preceding character.
- **Walk backward at every character:** rediscovering each character's segment start is correct but takes $O(n^2)$ on one long segment.
- **Empty or all-space string:** no position starts a segment.
- **Repeated spaces:** only the first following non-space character is counted.
- **Punctuation:** punctuation is part of a segment because only the space character separates segments.
