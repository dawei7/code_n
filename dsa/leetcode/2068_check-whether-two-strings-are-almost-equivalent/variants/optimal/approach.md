## General
**Accumulate one signed difference per letter**

Create 26 counters initialized to zero. Scan the strings together. For each position, increment the counter belonging to the character from `word1` and decrement the counter belonging to the character from `word2`. After the scan, a counter equals that letter's first frequency minus its second frequency.

**Check the inclusive threshold**

Inspect all 26 counters and return true only when every absolute value is at most $3$. The counters capture all occurrences because each character in each string changes exactly one corresponding entry. Thus passing every threshold is precisely the definition of almost equivalence, while any failed entry identifies a disqualifying letter.

## Complexity detail
The paired scan processes the $n$ positions once, and checking 26 counters is constant work, for $O(n)$ time. The fixed-size frequency-difference array uses $O(26)=O(1)$ auxiliary space.

## Alternatives and edge cases
- **Two frequency maps:** Count each string separately and compare their entries; this is also $O(n)$ but stores two sets of counters.
- **Recount for each occurrence:** Repeatedly scanning both strings for every encountered character is correct but can take $O(n^2)$ time.
- A difference of exactly $3$ is valid; the comparison is inclusive.
- Letters absent from both strings have difference zero and require no special handling.
- Equal string length does not guarantee almost equivalence because the excess counts may belong to different letters.
- Identical strings are always almost equivalent.
