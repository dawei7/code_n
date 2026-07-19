## General
**Build failure links for one pattern**

For each pattern, construct its KMP prefix table. At each pattern position, the
table records the longest proper prefix that is also a suffix of the prefix
ending there. When a comparison fails, this table identifies the longest
already-known candidate alignment instead of restarting from the beginning.

**Scan the word without retreating**

Traverse `word` once for that pattern while maintaining the number of matched
characters. On mismatch, follow prefix-table links until the current character
can extend the match or the match becomes empty. Reaching the full pattern
length proves that this array entry contributes one, so its scan may stop.

KMP examines each word character and each prefix-table link only a constant
amortized number of times. Repeating the independent test for every array
entry also naturally counts duplicate patterns separately, while stopping at
the first occurrence prevents multiple matches of one entry from being
overcounted.

## Complexity detail
Building all prefix tables over time costs $O(T)$. Scanning the length-$M$ word
once for each of the $P$ patterns costs $O(PM)$, giving
$O(T+PM)$ total time. Only the current pattern's prefix table is retained, so
the auxiliary space is $O(L)$.

## Alternatives and edge cases
- **Language substring operator:** This is concise and correct, but its
  algorithmic guarantees may be implementation-dependent.
- **Try every starting position:** Compare the pattern from scratch at each
  word position. Repeated near-matches can take $O(PML)$ time.
- **Aho-Corasick automaton:** Search all patterns together in one word scan.
  It can improve multi-pattern asymptotics but is substantially more complex
  for these small limits and must track duplicate multiplicities.
- A pattern longer than `word` cannot occur.
- Multiple occurrences of one pattern still contribute only one.
- Duplicate entries in `patterns` each contribute independently.
