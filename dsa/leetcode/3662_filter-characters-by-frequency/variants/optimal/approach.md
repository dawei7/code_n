## General

A decision about one occurrence cannot be made from its prefix alone: qualification depends on how many times that character appears in the entire original string. First build a frequency table for all characters in `s`.

Scan `s` again from left to right. Append a character exactly when its stored frequency is strictly less than `k`. Since every occurrence of a character reads the same completed count, either all occurrences of that character are retained or all are removed. Appending during the original-order scan preserves the required relative order automatically.

The first pass makes every frequency exact. The second pass applies the contract's strict predicate independently to every occurrence, so no disqualified occurrence enters the result and no qualified occurrence is omitted. Joining the retained characters therefore produces exactly the requested string, including the empty result when none qualifies.

## Complexity detail

Let $n$ be the length of `s` and $d$ its number of distinct letters. Counting takes $O(n)$ expected time, and filtering visits all $n$ positions once, so total time is $O(n)$. The frequency table stores $d$ entries and the output may store $O(n)$ characters; excluding the required output, auxiliary space is $O(d)$. Since the alphabet is fixed to 26 lowercase letters, $d\le26$.

The legal domain ends at $n=100$. Across that bounded range, execution overhead and native string-operation costs prevent reliable scaling from distinguishing the two-pass counter from repeated full-string counts. The package therefore uses a bounded-domain certificate: inspection of the accepted source proves exactly one counting visit and one filtering lookup per character, and boundary cases cover the maximum length and strict threshold.

## Alternatives and edge cases

- **Call `s.count` for each occurrence:** This is concise and correct, but repeated full-string scans take $O(n^2)$ time.
- **Fixed 26-entry array:** Indexing by `ord(character) - ord("a")` gives deterministic $O(n)$ time and $O(1)$ bounded storage.
- **Frequency exactly k:** The condition is strictly fewer than `k`, so equality removes every occurrence.
- **k equals one:** No nonempty-string character can occur fewer than once, so the result is empty.
- **All characters qualify:** The original string is returned unchanged, including its order.
- **No characters qualify:** Return `""`, not a placeholder or null value.
- **Interleaved occurrences:** Retention is based on total frequency, while output order remains the original sequence.
