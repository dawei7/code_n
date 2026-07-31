## General

**Guarantee linear pattern matching.** Build the KMP failure table for each
pattern. While scanning `s`, a mismatch falls back to the longest prefix that
is also a suffix of the matched portion instead of rechecking text characters.
When a full match is found, record its start and fall back through the same
table, which preserves overlapping occurrences.

**Merge occurrence positions.** Both KMP result lists are sorted. For each
`a` start `i`, advance one pointer past every `b` start smaller than
`i - k`. If the first remaining start is at most `i + k`, it witnesses that
`i` is beautiful. The pointer only advances, so proximity filtering is
linear in the number of matches.

This explicit matcher is material for the II constraints: pattern lengths can
be as large as the 500,000-character text, so restarting a comparison at every
text position can be quadratic on repetitive strings.

## Complexity detail

The two failure tables and text scans take $O(N+A+B)$ time. Merging the
occurrence lists is $O(N)$ in the worst case. The tables, occurrence lists, and
answer require $O(N+A+B)$ auxiliary space.

## Alternatives and edge cases

- **Z algorithm:** Concatenating each pattern with the text and computing Z-values gives the same linear guarantee.
- **Rolling hash:** It can compare substrings quickly but needs collision handling for deterministic correctness.
- **Naive matching:** Restarting a long comparison at every index can cost $O(N(A+B))$ time.
- **Binary search proximity:** Searching `b` starts independently for each `a` start costs an avoidable logarithmic factor.
- **Overlapping occurrences:** KMP fallback after a match retains overlaps.
- **Pattern longer than text:** Its occurrence list is empty.
- **Inclusive boundary:** Distance exactly `k` qualifies.
- **Identical patterns:** One occurrence can witness itself.
