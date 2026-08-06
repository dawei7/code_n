## Examples

**Example 1**

- Input: `sentence1 = ["great","acting","skills"], sentence2 = ["fine","drama","talent"], similarPairs = [["great","good"],["fine","good"],["drama","acting"],["skills","talent"]]`
- Output: `true`
- Explanation: The sentences have equal lengths, and the words at every corresponding position are similar. In particular, `"great"` and `"fine"` are connected through `"good"`.

**Example 2**

- Input: `sentence1 = ["I","love","leetcode"], sentence2 = ["I","love","onepiece"], similarPairs = [["manga","onepiece"],["platform","anime"],["leetcode","platform"],["anime","manga"]]`
- Output: `true`
- Explanation: The chain `"leetcode" -> "platform" -> "anime" -> "manga" -> "onepiece"` makes the final words similar, while the first two aligned words are identical. Therefore the sentences are similar.

**Example 3**

- Input: `sentence1 = ["I","love","leetcode"], sentence2 = ["I","love","onepiece"], similarPairs = [["manga","hunterXhunter"],["platform","anime"],["leetcode","platform"],["anime","manga"]]`
- Output: `false`
- Explanation: `"leetcode"` and `"onepiece"` do not belong to the same similarity group.
