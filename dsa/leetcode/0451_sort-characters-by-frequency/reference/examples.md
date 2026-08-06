## Examples

**Example 1**

- Input: `s = "tree"`
- Output: `"eert"`
- **Explanation:** The character `e` occurs twice, while `r` and `t` each occur once, so both copies of `e` must come first. The string `"eetr"` is also valid because the single-occurrence groups may trade places.

**Example 2**

- Input: `s = "cccaaa"`
- Output: `"aaaccc"`
- **Explanation:** Both `a` and `c` occur three times, so either `"aaaccc"` or `"cccaaa"` is valid. The alternating string `"cacaca"` is invalid because occurrences of the same character must be adjacent.

**Example 3**

- Input: `s = "Aabb"`
- Output: `"bbAa"`
- **Explanation:** The string `"bbaA"` is another valid ordering of the two single-occurrence groups. The unchanged string `"Aabb"` is invalid because the two copies of `b` have the greatest frequency and must come first. `A` and `a` are different characters.
