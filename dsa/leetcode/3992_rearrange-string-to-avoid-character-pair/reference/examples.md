## Examples

**Example 1**

- Input: `s = "aabc", x = "a", y = "c"`
- Output: `"cbaa"`
- **Explanation:** `"cbaa"` uses exactly the characters of `"aabc"`, and its only `c` appears before both occurrences of `a`.

**Example 2**

- Input: `s = "dcab", x = "d", y = "b"`
- Output: `"cabd"`
- **Explanation:** `"cabd"` is a permutation of the input, and its `b` occurs before its `d`.

**Example 3**

- Input: `s = "axe", x = "o", y = "x"`
- Output: `"axe"`
- **Explanation:** The original order is already valid. Because `o` does not occur, the required relationship is satisfied automatically.
