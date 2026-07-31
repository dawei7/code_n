## Examples

**Example 1**

- Input: `s = "aabbab"`
- Output: `0`
- Explanation: The whole string contains three `a` characters and three `b` characters, so it is balanced and can be removed in a single operation. Nothing remains.

**Example 2**

- Input: `s = "aaaa"`
- Output: `4`
- Explanation: Every substring contains only `a` characters, so no nonempty substring has equal numbers of `a` and `b`. No removal is possible.

**Example 3**

- Input: `s = "aaabb"`
- Output: `1`
- Explanation: Remove one occurrence of the substring `"ab"` to obtain `"aab"`. Remove the newly formed `"ab"` to obtain `"a"`. The final character cannot be removed, so the minimum remaining length is `1`.
