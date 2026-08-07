### 1. Description

A **transformation sequence** from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words $beginWord -> s_{1} -> s_{2} -> ... -> s_{k}$ such that:

- Every adjacent pair of words differs by a single letter.

- Every $s_{i}$ for $1 \le i \le k$ is in `wordList`. Note that `beginWord` does not need to be in `wordList`.

- $s_{k} = endWord$

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return *all the **shortest transformation sequences** from* `beginWord` *to* `endWord`*, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words *$[beginWord, s_{1}, s_{2}, ..., s_{k}]$.

### 2. Function Contract

**Inputs**

- `beginWord`: The first word in every transformation sequence.
- `endWord`: The required final word.
- `wordList`: The allowed words after `beginWord`.

**Return value**

Return every shortest valid transformation sequence. The order of the returned sequences is not significant, but word order within each sequence is.

### 3. Examples

#### Example 1

- **Input:** $beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]$
- **Output:** `[["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]`
- **Explanation:** There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
#### Example 2

- **Input:** $beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]$
- **Output:** `[]`
- **Explanation:** The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

### 4. Constraints

- $1 \le \text{beginWord.length} \le 5$

- $\text{endWord.length} = \text{beginWord.length}$

- $1 \le \text{wordList.length} \le 500$

- $\text{wordList}[i].length = \text{beginWord.length}$

- `beginWord`, `endWord`, and $\text{wordList}[i]$ consist of lowercase English letters.

- $beginWord \neq endWord$

- All the words in `wordList` are **unique**.

- The **sum** of all shortest transformation sequences does not exceed $10^{5}$.