## General
**Each recursion level chooses one IPv4 segment boundary**

Backtrack from the current string index with a path of completed segments. The next segment can contain one, two, or three digits. Accumulate its numeric value incrementally and stop once it exceeds `255`, since adding another digit can only increase it.

If the segment begins with `0`, allow the one-character segment `"0"` and stop before trying a longer length. This rejects noncanonical forms such as `"00"` and `"01"` without rejecting zero itself.

**Remaining digits must fit the remaining segment count**

If `r = 4 - len(path)` segments remain, the unconsumed suffix must contain at least `r` digits and at most `3r`. Fewer digits cannot give every segment one character; more digits cannot fit under the three-character limit. Reject either state before parsing candidates.

Emit only when four segments have been chosen and the index is exactly at the string end. Reaching four segments early or consuming all digits with fewer than four segments is not a valid address.

**The path represents the source prefix without losing digits**

The path contains valid canonical segments whose concatenated digit text equals exactly `s[:index]`. Every recursive branch chooses a different next boundary, and popping after recursion restores the parent prefix. No branch reorders, inserts, or discards a source digit.

**Trace leading-zero pruning**

For `010010`, the first segment must be `0`. Subsequent valid choices produce `0.10.0.10` and `0.100.1.0`; choices such as `01` are rejected by the leading-zero rule.

**Segment boundaries are the complete address search space**

Every emitted path contains four segments, each satisfying the length, leading-zero, and numeric-range rules, and consumes the entire source. It therefore spells a valid restored address.

Conversely, any valid restoration chooses three boundaries that divide the source into four lengths from one through three. The search enumerates those segment lengths, and its checks accept every segment that belongs to the valid address. Different boundary sequences produce different dotted strings, so all restorations appear once.

## Complexity detail
IPv4 fixes four segments of at most three digits, so at most $3^{4}$ bounded branches and constant-size paths are explored; under the public contract this is $O(1)$ time and auxiliary space. Returned strings are also bounded in count and length.

## Alternatives and edge cases
- **Enumerate three dot indices:** is also bounded and correct but has less direct segment-level pruning.
- **Regular expressions:** can validate a finished address but do not naturally generate all partitions.
- **Parse arbitrary-length prefixes:** wastes work because IPv4 segments can never exceed three digits.
- Strings shorter than four or longer than twelve digits fail immediately through the remaining-length bound.
- Output order is unrestricted. Converting a candidate segment to an integer must not erase its original leading-zero evidence before validation.
