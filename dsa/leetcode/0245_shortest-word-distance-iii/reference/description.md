### 1. Description

Given an array of strings `wordsDict` and two strings that already exist in the array `word1` and `word2`, return *the shortest distance between the occurrence of these two words in the list*.

### 2. Function Contract

**Inputs**

- `wordsDict`: List of strings $\text{List}[str]$.
- `word1`: Target word string (may equal `word2`).
- `word2`: Target word string (may equal `word1`).

**Return value**

Integer representing the shortest distance between occurrences of `word1` and `word2` in `wordsDict`.

### 3. Note

that `word1` and `word2` may be the same. It is guaranteed that they represent **two individual words** in the list.

### 4. Examples

#### Example 1

- **Input:** $wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"$
- **Output:** `1`
#### Example 2

- **Input:** $wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "makes"$
- **Output:** `3`

### 5. Constraints

- $1 \le \text{wordsDict.length} \le 10^{5}$

- $1 \le \text{wordsDict}[i].length \le 10$

- $\text{wordsDict}[i]$ consists of lowercase English letters.

- `word1` and `word2` are in `wordsDict`.