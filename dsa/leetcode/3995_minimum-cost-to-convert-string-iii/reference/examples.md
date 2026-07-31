## Examples

**Example 1**

- Input: `source = "hello", target = "world", rules = [["he","wo"],["llo","rld"]], costs = [3,4]`
- Output: `7`
- **Explanation:** Apply `rules[0]` to replace `"he"` with `"wo"` for `3`, producing `"wollo"`. Then apply `rules[1]` to replace `"llo"` with `"rld"` for `4`, producing `"world"`. The total is `3 + 4 = 7`.

**Example 2**

- Input: `source = "cat", target = "dog", rules = [["c*t","dog"]], costs = [2]`
- Output: `3`
- **Explanation:** Apply the only rule to replace `"cat"` with `"dog"`. Its wildcard matches `'a'`, adding `1` to the base cost `2`, so the total is `3`.

**Example 3**

- Input: `source = "test", target = "next", rules = [["*e*t","next"]], costs = [4]`
- Output: `6`
- **Explanation:** Apply the rule to replace `"test"` with `"next"`. Its first wildcard matches `'t'` and its second matches `'s'`, adding `2` to the base cost `4` for a total of `6`.

**Example 4**

- Input: `source = "ab", target = "bc", rules = [["a*","bd"]], costs = [9]`
- Output: `-1`
- **Explanation:** No sequence of legal rule applications can transform `source` into `target`.
