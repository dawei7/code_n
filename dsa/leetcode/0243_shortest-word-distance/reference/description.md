## Description

Given an array of strings `wordsDict` and two different strings that already exist in the array `word1` and `word2`, return *the shortest distance between these two words in the list*.
### Function Contract

**Inputs**

- `wordsDict`: List of strings $\text{List}[str]$.
- `word1`: Target word string.
- `word2`: Target word string.

**Return value**

Integer representing the shortest distance between `word1` and `word2` in `wordsDict`.

### Examples

#### Example 1

- **Input:** $wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"$
- **Output:** `3`
#### Example 2

- **Input:** $wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"$
- **Output:** `1`
### Constraints

- $2 \le \text{wordsDict.length} \le 3 * 10^{4}$

- $1 \le \text{wordsDict}[i].length \le 10$

- $\text{wordsDict}[i]$ consists of lowercase English letters.

- `word1` and `word2` are in `wordsDict`.

- $word1 \neq word2$