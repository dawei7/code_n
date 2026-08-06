## Examples

**Example 1**

- Input: `sentence1 = ["great","acting","skills"], sentence2 = ["fine","drama","talent"], similarPairs = [["great","fine"],["drama","acting"],["skills","talent"]]`
- Output: `true`
- Explanation: The arrays have the same length, and each word in `sentence1` is similar to the word at the corresponding position in `sentence2`.

**Example 2**

- Input: `sentence1 = ["great"], sentence2 = ["great"], similarPairs = []`
- Output: `true`
- Explanation: A word is always similar to itself.

**Example 3**

- Input: `sentence1 = ["great"], sentence2 = ["doubleplus","good"], similarPairs = [["great","doubleplus"]]`
- Output: `false`
- Explanation: The two sentences have different lengths, so they cannot be similar.
