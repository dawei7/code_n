### 1. Description

A **transformation sequence** from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words $beginWord -> s_{1} -> s_{2} -> ... -> s_{k}$ such that:

- Every adjacent pair of words differs by a single letter.

- Every $s_{i}$ for $1 \le i \le k$ is in `wordList`. Note that `beginWord` does not need to be in `wordList`.

- $s_{k} = endWord$

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return *the **number of words** in the **shortest transformation sequence** from* `beginWord` *to* `endWord`*, or *`0`* if no such sequence exists.*

### 2. Function Contract

**Inputs**

- `beginWord`: The first word in the transformation sequence.
- `endWord`: The required final word.
- `wordList`: The allowed words after `beginWord`.

**Return value**

Return the number of words in the shortest valid sequence, including both endpoints, or `0` when none exists.

### 3. Examples

#### Example 1

- **Input:** $beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]$
- **Output:** `5`
- **Explanation:** One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
#### Example 2

- **Input:** $beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]$
- **Output:** `0`
- **Explanation:** The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

### 4. Constraints

- $1 \le \text{beginWord.length} \le 10$

- $\text{endWord.length} = \text{beginWord.length}$

- $1 \le \text{wordList.length} \le 5000$

- $\text{wordList}[i].length = \text{beginWord.length}$

- `beginWord`, `endWord`, and $\text{wordList}[i]$ consist of lowercase English letters.

- $beginWord \neq endWord$

- All the words in `wordList` are **unique**.