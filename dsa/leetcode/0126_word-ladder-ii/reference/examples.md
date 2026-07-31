## Examples

**Example 1**

- Input: `beginWord = "hit", endWord = "cog", wordList = ["hot", "dot", "dog", "lot", "log", "cog"]`
- Output: `[["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]]`
- Explanation: There are two shortest sequences: `"hit" -> "hot" -> "dot" -> "dog" -> "cog"` and `"hit" -> "hot" -> "lot" -> "log" -> "cog"`.

**Example 2**

- Input: `beginWord = "hit", endWord = "cog", wordList = ["hot", "dot", "dog", "lot", "log"]`
- Output: `[]`
- Explanation: Because `endWord` (`"cog"`) does not occur in `wordList`, no valid transformation sequence exists.
