### 1. Description

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the `WordDictionary` class:

- `WordDictionary()` Initializes the object.

- `void addWord(word)` Adds `word` to the data structure, it can be matched later.

- `bool search(word)` Returns `true` if there is any string in the data structure that matches `word` or `false` otherwise. `word` may contain dots `'.'` where dots can be matched with any letter.

**Example:**

```
**Input**
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
**Output**
[null,null,null,null,false,true,true,true]

**Explanation**
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
```

### 2. Function Contract

**Inputs**

- `operations`: App-local commands `["addWord", word]` and `["search", pattern]`, processed against one initially empty dictionary.

**Return value**

Return the boolean result of each `search` command in command order; additions produce no result.

### 3. Constraints

- $1 \le \text{word.length} \le 25$

- `word` in `addWord` consists of lowercase English letters.

- `word` in `search` consist of `'.'` or lowercase English letters.

- There will be at most `2` dots in `word` for `search` queries.

- At most $10^{4}$ calls will be made to `addWord` and `search`.
