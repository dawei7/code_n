## Examples

**Example 1**

- Input: `words = ["ntgwz","zwntg"]`
- Output: `1`
- **Explanation:** For `"ntgwz"`, the even-index sequence is `"ngz"` and the odd-index sequence is `"tw"`. Shifting each sequence one position to the right produces `"zng"` and `"wt"`. Placing them back into even and odd positions gives `"zwntg"`. The two strings are therefore equivalent and may share one group.

**Example 2**

- Input: `words = ["abc","cab","bac","acb","bca","cba"]`
- Output: `3`
- **Explanation:** A minimum partition is `['abc','cba']`, `['cab','bac']`, and `['acb','bca']`. The two strings within each listed group are equivalent.

**Example 3**

- Input: `words = ["leet","abb","bab","deed","edde","code","bba"]`
- Output: `5`
- **Explanation:** The strings can be partitioned into `['abb','bba']`, `['deed','edde']`, `['leet']`, `['bab']`, and `['code']`. Every pair of strings in each group is equivalent, and no partition into fewer groups satisfies the requirement.
