### 1. Description

Design a special dictionary that searches the words in it by a prefix and a suffix.

Implement the `WordFilter` class:

- `WordFilter(string[] words)` Initializes the object with the `words` in the dictionary.

- `f(string pref, string suff)` Returns *the index of the word in the dictionary,* which has the prefix `pref` and the suffix `suff`. If there is more than one valid index, return **the largest** of them. If there is no such word in the dictionary, return `-1`.

### 2. Function Contract

**Methods**

- `WordFilter(words: List[str])`: Initializes the data structure.
- `f(pref: str, suff: str) -> `int``: Executes operation.

### 3. Examples

#### Example 1

```
**Input**
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
**Output**
[null, 0]
**Explanation**
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = "e".
```

### 4. Constraints

- $1 \le \text{words.length} \le 10^{4}$

- $1 \le \text{words}[i].length \le 7$

- $1 \le \text{pref.length}, \text{suff.length} \le 7$

- $\text{words}[i]$, `pref` and `suff` consist of lowercase English letters only.

- At most $10^{4}$ calls will be made to the function `f`.
