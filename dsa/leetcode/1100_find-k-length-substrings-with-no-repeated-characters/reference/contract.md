## Function Contract

**Inputs**

- `s`: a string of lowercase English letters.
- `k`: the exact required substring length.

For every start position where `s[start:start + k]` has length `k`, test whether its $k$ characters are pairwise distinct. Overlapping substrings are separate candidates, and the same text occurring at different starts contributes once per occurrence.

**Return value**

Return the number of length-`k` substrings with no repeated character. Return zero if no complete window exists or if every complete window contains a repetition.
