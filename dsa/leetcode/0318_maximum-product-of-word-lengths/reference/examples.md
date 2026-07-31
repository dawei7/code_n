## Examples

**Example 1**

- Input: `words = ["abcw","baz","foo","bar","xtfn","abcdef"]`
- Output: `16`
- Explanation: The disjoint words `"abcw"` and `"xtfn"` both have length `4`, producing `4 * 4 = 16`.

**Example 2**

- Input: `words = ["a","ab","abc","d","cd","bcd","abcd"]`
- Output: `4`
- Explanation: The pair `"ab"` and `"cd"` shares no letter and gives product `2 * 2 = 4`.

**Example 3**

- Input: `words = ["a","aa","aaa","aaaa"]`
- Output: `0`
- Explanation: Every possible pair shares the letter `a`, so no eligible pair exists.
