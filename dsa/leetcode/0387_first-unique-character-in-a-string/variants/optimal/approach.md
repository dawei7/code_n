## General
**Frequency is a whole-string property**

Whether a position is unique cannot be decided from its prefix alone because the same character may reappear later. First scan the complete string and count each lowercase letter in a fixed array of 26 entries.

**Use the original order only after counts are known**

Scan `s` again from left to right. The first position whose counter equals one is unique globally, and left-to-right inspection makes it the earliest such position. If the scan ends without finding one, every character occurs at least twice and the answer is `-1`.

**Why two passes are sufficient**

The first pass records the exact multiplicity of every possible character. The second tests positions in increasing index order against those final multiplicities. Returning at the first count of one therefore satisfies both requirements—global uniqueness and minimum index—while no omitted earlier position could be unique.

## Complexity detail
For a string of length `n`, the two scans take $O(n)$ time. The frequency array always has 26 entries, so its space usage is $O(1)$.

## Alternatives and edge cases
- **Hash-map counts:** has the same linear time and works for an unrestricted alphabet, using space proportional to the number of distinct characters.
- **Queue of candidate indices:** supports streaming updates but adds storage that is unnecessary when the full string is already available.
- **Call a counting operation at every position:** can repeatedly scan the string and take $O(n^2)$ time.
- A one-character string returns index zero.
- If every character is repeated, return `-1`.
- The first unique character may appear only at the last index.
- Later duplicates can invalidate characters that looked unique in an early prefix.
