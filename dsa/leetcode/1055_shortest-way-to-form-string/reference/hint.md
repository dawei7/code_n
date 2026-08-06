## Hint

**Hint 1:** Determine what condition would make it impossible to form `target`.

**Hint 2:** If `target` contains a character that never appears in `source`, no concatenation of source subsequences can form it.

**Hint 3:** Once construction is known to be possible, consider how to guarantee that the fewest source subsequences are used.

**Hint 4:** For each source copy, compare its leftmost remaining character with the leftmost unmatched character of `target`. When they match, consume both; otherwise discard only the source character. When the current source copy is exhausted, restart from a fresh copy and increment the count. Continue until no target characters remain, then return the count.
