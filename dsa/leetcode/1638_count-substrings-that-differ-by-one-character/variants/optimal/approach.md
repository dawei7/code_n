## General
**Classify substrings by their ending positions.** For each pair of positions `i` in `s` and `j` in `t`, track two quantities for equal-length substrings ending there. `equal[i][j]` is the length of the longest equal suffix, while `one[i][j]` is the number of suffix lengths that contain exactly one mismatch. Each valid substring pair has a unique pair of ending positions, so summing `one[i][j]` counts every choice once.

**Extend along the previous diagonal.** When `s[i] == t[j]`, the equal suffix extends by one, and every suffix that already had one mismatch at `i-1,j-1` remains valid after appending the matching character. Therefore `equal` becomes the previous diagonal `equal` plus one, while `one` copies the previous diagonal `one`.

When the current characters differ, an exactly-one-mismatch suffix must use this position as its sole mismatch. It may prepend any equal suffix ending at `i-1,j-1`, including the empty suffix, so `one` becomes the previous diagonal `equal` plus one; `equal` resets to zero. No suffix that already had one mismatch may be extended through a second mismatch.

**Roll the rows.** Every transition reads only the preceding row and diagonal column. Keep arrays for the previous and current rows rather than the full tables. The transitions enumerate every possible ending pair and count precisely the suffixes with one mismatch, establishing both completeness and exclusion of zero- or multiple-mismatch pairs.

## Complexity detail
There are $mn$ position pairs, and each transition takes constant time, for $O(mn)$ total time. Four rows of length $n+1$—two previous states and two current states—use $O(n)$ auxiliary space. The strings may be swapped first if $O(\min(m,n))$ space is desired.

## Alternatives and edge cases
- **Left/right matching tables:** Precompute equal-run lengths ending before and starting after every position pair. Each mismatching center contributes the product of the available left and right extension counts, also in $O(mn)$ time and space unless rows are compressed carefully.
- **Extend every starting pair:** Compare characters forward from every pair of starts until a second mismatch appears. This is direct but takes $O(mn\min(m,n))$ time in the worst case.
- **Enumerate all substring texts:** Materializing and comparing every substring pair uses substantially more time and storage and can obscure that occurrences at different positions count separately.
- Equal one-character substrings contribute zero, while unequal one-character substrings each contribute one.
- Entirely equal strings may still produce valid pairs at different offsets; the requirement applies to the selected substring texts, not to whether `s` and `t` are different strings.
- A pair with zero differences or two differences must not be counted.
- Repeated characters can make many positional choices yield identical text; each occurrence pair remains a separate way.
